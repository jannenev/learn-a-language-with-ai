#!/usr/bin/env python3
"""Count which Tier 1 vocabulary entries a text file uses, and flag words outside the list.

Usage:
    python3 tools/wordcheck.py cebuano/texts/src/001.txt                 # one text
    python3 tools/wordcheck.py cebuano/texts/src/001.txt cebuano/texts/src/002.txt   # cumulative over several texts
    python3 tools/wordcheck.py --counts cebuano/texts/src/*.txt          # occurrences per entry, in exposure bands
    python3 tools/wordcheck.py --new cebuano/texts/src/*.txt             # which entries each text brings in for the first time
    python3 tools/wordcheck.py --chains cebuano/texts/src/*.txt          # lines with three or more small words in a row (--chains=2 for pairs)
    python3 tools/wordcheck.py --list cebuano/texts/src/002.txt          # the words a text brings in, with their glosses (what render.py and print.py show)

It reads the Cebuano column of cebuano/texts/src/NNN.txt ("Speaker | Cebuano | English"); the old v1 markdown
layout (numbered lines with the Cebuano in bold) is still accepted.
Matching is by surface form plus a light prefix/suffix strip (mo-, ni-, nag-, gi-, ... ; -on, -a).
Two words are ambiguous in Cebuano. When the source has a gloss line under the sentence, the gloss decides
(ni=of, ni=this, na=that); without one a heuristic is used:
    ni  -> "of" when the next word is a capitalised name, otherwise "this" (kini)
    na  -> the particle "already/now" (it can also be "that", kana).
Anything it cannot match is printed as UNMATCHED so you can decide whether it is a name, a loanword,
a form the list should know about, or a word that does not belong in the text yet.
The small words (pronouns, markers, particles) are hard to parse when several stand in a row and are
new (na mo sa, pa ko og); --chains lists such lines with each member's exposure before that line.
"""
import re
import sys
from pathlib import Path

# Tier 1: entry name -> surface forms (lowercase). Keep in sync with vocabulary.md, section "Tier 1".
TIER1 = {
    # 1.1 pronouns
    "ako": {"ako", "ko", "nako", "akong", "akoa"},
    "ikaw": {"ikaw", "ka", "nimo", "imong", "imoha"},
    "siya": {"siya", "niya", "iyang", "iyaha"},
    "kita (we)": {"kita", "ta", "nato", "atong", "atoa"},
    "kami": {"kami", "mi", "namo", "among", "amoa"},
    "kamo": {"kamo", "mo", "ninyo", "inyong", "inyoha"},
    "sila": {"sila", "nila", "ilang", "ilaha"},
    # 1.2 markers
    "ang": {"ang"},
    "si": {"si"},
    "sa": {"sa"},
    "og": {"og"},
    "ug": {"ug"},
    "nga": {"nga"},          # also credited when a word ends in the -ng linker, see below
    "mga": {"mga"},
    "ni (of)": set(),        # filled by the ni-heuristic
    # 1.3 particles
    "ba": {"ba"},
    "na": {"na"},
    "pa": {"pa"},
    "lang": {"lang", "ra", "lamang"},
    "gyud": {"gyud", "jud", "gyod", "gayod"},
    "kaayo": {"kaayo"},
    "pud": {"pud", "sad", "usab"},
    # 1.4 yes / no / there is
    "oo": {"oo", "o"},
    "dili": {"dili", "di"},
    "wala": {"wala", "wa", "walay"},
    "naa": {"naa", "naay", "aduna", "duna"},
    # 1.5 question words
    "unsa": {"unsa", "unsay"},
    "kinsa": {"kinsa", "kinsay"},
    "asa": {"asa", "hain", "diin"},
    "pila": {"pila", "tagpila"},
    # 1.6 greetings & social
    "maayo": {"maayo"},
    "maayong buntag/hapon/gabii": set(),   # filled by the bigram check
    "kumusta": {"kumusta", "musta"},
    "salamat": {"salamat"},
    "sige": {"sige"},
    "Dong/Day": {"dong", "day", "dodong", "inday"},
    "ayaw": {"ayaw"},
    # 1.7 verbs (roots; affixed forms are stripped to the root)
    "adto": {"adto"},
    "kaon": {"kaon"},
    "inom": {"inom"},
    "tulog": {"tulog"},
    "trabaho": {"trabaho"},
    "gusto": {"gusto"},
    "kahibalo": {"kahibalo", "kabalo", "kabaw", "hibalo"},
    "kasabot": {"kasabot", "sabot"},
    "dali": {"dali"},
    "hulat": {"hulat"},
    # 1.8 nouns
    "balay": {"balay"},
    "tubig": {"tubig"},
    "pagkaon": {"pagkaon"},
    "kwarta": {"kwarta", "kuwarta"},
    "tawo": {"tawo"},
    "Mama/Papa": {"mama", "papa", "ma"},
    # 1.9 time
    "karon": {"karon", "ron"},
    "ugma": {"ugma"},
    "unya": {"unya"},
    "buntag/hapon/gabii": {"buntag", "hapon", "gabii"},
    # 1.10 describing
    "dako": {"dako", "dagko"},
    "gamay": {"gamay", "gagmay"},
    "daghan": {"daghan"},
    "lami": {"lami"},
    # 1.11 pointing
    "kini/ni (this)": {"kini"},   # bare "ni" added by the heuristic
    "kana/na (that)": {"kana"},   # bare "na" is credited here only when its gloss says "that"
    "diri": {"diri", "dinhi", "ari"},
    "didto": {"didto"},
}

NAMES = {"ana", "jun"}
NAME = "[name]"      # the entry given to a proper name by resolve()

# The small grammatical words: pronouns, markers, particles and the short pointing words. Used by --chains.
SMALL = {"ako", "ikaw", "siya", "kita (we)", "kami", "kamo", "sila",
         "ang", "si", "sa", "og", "ug", "nga", "mga", "ni (of)",
         "ba", "na", "pa", "lang", "gyud", "pud",
         "kini/ni (this)", "kana/na (that)"}

PREFIXES = ["naka", "maka", "nag", "mag", "pag", "mo", "mi", "ni", "gi", "ma", "na", "ka", "i"]
SUFFIXES = ["on", "a"]

form_to_entry = {}
for entry, forms in TIER1.items():
    for f in forms:
        form_to_entry[f] = entry


def lookup(tok):
    """Return the Tier 1 entry for a token, trying the bare form, then affix stripping."""
    if tok in form_to_entry:
        return form_to_entry[tok]
    if tok.endswith("ng") and tok[:-2] in form_to_entry:      # -ng linker: maayong, daghang
        return form_to_entry[tok[:-2]]
    for p in PREFIXES:
        if tok.startswith(p) and len(tok) > len(p) + 2:
            rest = tok[len(p):].lstrip("-")
            if rest in form_to_entry:
                return form_to_entry[rest]
            for s in SUFFIXES:
                if rest.endswith(s) and rest[: -len(s)] in form_to_entry:
                    return form_to_entry[rest[: -len(s)]]
    for s in SUFFIXES:
        if tok.endswith(s) and tok[: -len(s)] in form_to_entry:
            return form_to_entry[tok[: -len(s)]]
    return None


def cebuano_lines(path):
    """Yield the Cebuano text of each dialogue line.

    Accepts the markdown layout (numbered lines with the Cebuano in bold) and the
    plain-text source layout used by tools/render.py ("Speaker | Cebuano | English").
    """
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if str(path).endswith(".txt"):
            if " | " in line and not line[0].isspace() and not re.match(r"^[a-z]+:\s", line):
                yield line.split("|")[1].strip()
            continue
        if re.match(r"^\*\*\d+\.", line):
            bolds = re.findall(r"\*\*(.+?)\*\*", line)
            if len(bolds) >= 2:
                yield bolds[-1]


def cebuano_entries(path):
    """Yield (cebuano_text, glosses) per dialogue line of a plain-text source; glosses is the list of
    (word, gloss) pairs from the indented gloss line, or None when the line has none."""
    if not str(path).endswith(".txt"):
        for text in cebuano_lines(path):
            yield text, None
        return
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if " | " in line and not line[0].isspace() and not re.match(r"^[a-z]+:\s", line):
            gl = None
            for nxt in lines[i + 1:]:
                if not nxt[:1].isspace():
                    break
                s = nxt.strip()
                if s and not s.startswith("!"):
                    gl = [t.split("=", 1) if "=" in t else [t, ""] for t in s.split()]
                    break
            yield line.split("|")[1].strip(), gl


def resolve(text, gl):
    """Resolve one dialogue line into (surface, entry, extras, boundary, gloss) per token, in order.

    entry is the Tier 1 entry, NAME for a proper name, or None when nothing matched. extras lists
    (entry, form) pairs credited on the side: maayo and the -ng linker in "maayong buntag", the
    linker on words like daghang. boundary is True when punctuation follows the token. gloss is
    the token's gloss from the gloss line, "" when there is none."""
    toks = re.findall(r"([A-Za-z'\-]+)([^A-Za-z'\-]*)", text)
    # contractions: naa'y, ko'y, wala'y, unsa'y -> drop the 'y
    raw = [(w.replace("'y", "").replace("'", ""), bool(re.search(r"[.,!?;:\u2026]", t))) for w, t in toks]
    raw = [(w, b) for w, b in raw if w]
    # the gloss of each token, when the gloss line lines up with the tokens
    glosses = [g for w, g in gl if re.search(r"[A-Za-z]", w)] if gl else []
    if len(glosses) != len(raw):
        glosses = [""] * len(raw)
    out = []
    i = 0
    while i < len(raw):
        w, brk = raw[i]
        lw = w.lower()
        g = glosses[i]
        nxt_raw, nxt_brk = raw[i + 1] if i + 1 < len(raw) else ("", False)
        nxt = nxt_raw.lower()
        if lw == "maayong" and nxt in {"buntag", "hapon", "gabii"}:
            out.append((lw + " " + nxt, "maayong buntag/hapon/gabii", [("maayo", "maayong"), ("nga", "-ng")], nxt_brk,
                        (g + " " + glosses[i + 1]).strip()))
            i += 2
            continue
        if lw == "ni" or (lw == "na" and g.lower() == "that"):
            if lw == "na":
                entry = "kana/na (that)"
            elif g.lower() in ("of", "this"):
                entry = "ni (of)" if g.lower() == "of" else "kini/ni (this)"
            else:
                entry = "ni (of)" if nxt_raw[:1].isupper() else "kini/ni (this)"
            out.append((lw, entry, [], brk, g))
        elif lw in NAMES:
            out.append((lw, NAME, [], brk, g))
        else:
            entry = lookup(lw)
            extras = [("nga", "-ng")] if entry and lw.endswith("ng") and lw[:-2] in form_to_entry else []
            out.append((lw, entry, extras, brk, g))
        i += 1
    return out


def analyse(paths):
    covered = {}       # entry -> set of surface forms seen
    unmatched = {}     # token -> count
    counts = {}        # entry -> number of occurrences
    for path in paths:
        for text, gl in cebuano_entries(path):
            for w, entry, extras, _, _ in resolve(text, gl):
                if entry is None:
                    unmatched[w] = unmatched.get(w, 0) + 1
                    continue
                if entry == NAME:
                    continue
                covered.setdefault(entry, set()).add(w)
                counts[entry] = counts.get(entry, 0) + 1
                for e, form in extras:
                    covered.setdefault(e, set()).add(form)
                    counts[e] = counts.get(e, 0) + 1
    return covered, unmatched, counts


def root_of(w, entry):
    """The listed form an affixed token reduces to (moinom -> inom, daghang -> daghan), or None when the
    token is itself a listed form of its entry."""
    forms = TIER1.get(entry, set())
    if not forms or w in forms:
        return None
    if w.endswith("ng") and w[:-2] in forms:
        return w[:-2]
    for pre in PREFIXES:
        if w.startswith(pre):
            rest = w[len(pre):].lstrip("-")
            if rest in forms:
                return rest
            for suf in SUFFIXES:
                if rest.endswith(suf) and rest[: -len(suf)] in forms:
                    return rest[: -len(suf)]
    for suf in SUFFIXES:
        if w.endswith(suf) and w[: -len(suf)] in forms:
            return w[: -len(suf)]
    return None


def new_in_text(path):
    """The entries a text brings in, compared with the lower-numbered sources in its folder (by the three-digit
    number, so 002b is compared with 001 only): a list of (surface, gloss, entry) in order of first appearance,
    the gloss taken from the gloss line of that first occurrence, with the root in parentheses when the text
    has an affixed form (moinom  will-drink (inom)). Used by render.py and print.py."""
    path = Path(path)
    num = path.stem[:3]
    earlier = sorted(q for q in path.parent.glob("*.txt") if q.stem[:3].isdigit() and q.stem[:3] < num)
    seen = set()
    if earlier:
        covered, unmatched, _ = analyse(earlier)
        seen = set(covered) | set(unmatched)      # a word outside the tiers counts as seen once a text used it
    out, found, side = [], set(), {}
    for text, gl in cebuano_entries(path):
        for w, entry, extras, _, g in resolve(text, gl):
            if entry == NAME:
                continue
            key = entry or w.lower()               # a word outside the tiers is new to the reader too (002: merkado)
            if key not in seen and key not in found:
                found.add(key)
                root = root_of(w, entry) if entry else None
                out.append((w, f"{g} ({root})".strip() if root else g, key))
            for e, form in extras:
                if e not in seen and e not in found:
                    side.setdefault(e, form)
    for e, form in side.items():          # entries met only on the side, such as nga as the -ng linker
        if e not in found:
            found.add(e)
            out.append((form, "linker" if e == "nga" else e, e))
    return out


def chains(paths, n):
    """Print the lines where n or more small words stand in a row, with each member's exposure so far."""
    prior, forms = {}, set()
    print(f"Chains of {n} or more small words in a row (pronouns, markers, particles; punctuation breaks a chain).")
    print("The number after a word is how often its entry occurred in these texts before that line; * = fewer than 5;")
    print("'new form' = this form of the entry (nimo for ikaw, mi for kami) has not appeared before.\n")
    for path in paths:
        print(Path(path).name)
        n2 = n3 = ln = 0
        for ln, (text, gl) in enumerate(cebuano_entries(path), 1):
            items = resolve(text, gl)
            runs, run = [], []
            for w, entry, extras, brk, _ in items:
                if entry in SMALL:
                    run.append((w, entry))
                if entry not in SMALL or brk:
                    if len(run) >= 2:
                        runs.append(run)
                    run = []
            if len(run) >= 2:
                runs.append(run)
            longest = max((len(r) for r in runs), default=0)
            n2 += longest >= 2
            n3 += longest >= 3
            shown = [r for r in runs if len(r) >= n]
            if shown:
                print(f"  {ln:2d}  {text}")
                for r in shown:
                    print("      " + "   ".join(
                        f"{w}({prior.get(e, 0)}{'*' if prior.get(e, 0) < 5 else ''}"
                        f"{', new form' if w not in forms else ''})" for w, e in r))
            for w, entry, extras, brk, _ in items:
                if entry and entry != NAME:
                    prior[entry] = prior.get(entry, 0) + 1
                    forms.add(w)
                    for e, _ in extras:
                        prior[e] = prior.get(e, 0) + 1
        print(f"  lines: {ln}; with two small words in a row: {n2}; with three or more: {n3}\n")


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    show_counts = "--counts" in argv
    show_new = "--new" in argv
    chain_n = next((int(a.split("=", 1)[1]) if "=" in a else 3 for a in argv if a.startswith("--chains")), None)
    show_list = "--list" in argv
    argv = [a for a in argv if not a.startswith("--")]
    total = len(TIER1)
    if show_list:
        for path in argv:
            items = new_in_text(path)
            print(f"{Path(path).name}: {len(items)} entries first appear here")
            for w, g, e in items:
                print(f"  {w:18s} {g:16s} ({e})")
        return 0
    if chain_n:
        chains(argv, chain_n)
        return 0
    if show_new:
        seen = set()
        for path in argv:
            here = set(analyse([path])[0])
            new = [e for e in TIER1 if e in here and e not in seen]
            seen |= here
            print(f"{Path(path).name}: {len(new)} entries first appear here (cumulative {len(seen)} / {total})")
            print("  " + (", ".join(new) if new else "none"))
        left = [e for e in TIER1 if e not in seen]
        print(f"\nStill unused after these texts: {', '.join(left) if left else 'none'}")
        return 0
    covered, unmatched, counts = analyse(argv)
    print(f"Files: {', '.join(Path(p).name for p in argv)}")
    print(f"Tier 1 coverage: {len(covered)} / {total} entries\n")
    if show_counts:
        print(f"Occurrences per entry ({sum(counts.values())} Tier 1 tokens). Research puts the learning threshold "
              "at roughly 10 spaced encounters; multiply by the number of times you read the texts.")
        bands = [("10+", 10, 10**9), ("5-9", 5, 9), ("2-4", 2, 4), ("1", 1, 1), ("0", 0, 0)]
        for label, lo, hi in bands:
            items = [f"{e} ({counts.get(e, 0)})" for e in TIER1 if lo <= counts.get(e, 0) <= hi]
            print(f"  [{label}] {len(items):2d}: " + ", ".join(items))
        print()
        return 0
    print("Covered:")
    for e in TIER1:
        if e in covered:
            print(f"  {e:28s} {', '.join(sorted(covered[e]))}")
    print("\nNot yet used:")
    for e in TIER1:
        if e not in covered:
            print(f"  {e}")
    print("\nUNMATCHED (names, loanwords, or words outside Tier 1):")
    if unmatched:
        for w, n in sorted(unmatched.items()):
            print(f"  {w} x{n}")
    else:
        print("  none")
    print("\nNote: 'na' counts as 'that' (kana) only where the gloss line says so; otherwise it is the particle.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
