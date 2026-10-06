#!/usr/bin/env python3
"""Count which Tier 1 vocabulary entries a text file uses, and flag words outside the list.

Usage:
    python3 tools/wordcheck.py texts/001-*.md            # one text
    python3 tools/wordcheck.py texts/001-*.md texts/002-*.md   # cumulative over several texts

It reads the bold Cebuano segment of every numbered dialogue line ("**1. Ana:** **Cebuano here**").
Matching is by surface form plus a light prefix/suffix strip (mo-, ni-, nag-, gi-, ... ; -on, -a).
Two words are ambiguous in Cebuano and are resolved by a heuristic:
    ni  -> "of" when the next word is a capitalised name, otherwise "this" (kini)
    na  -> always counted as the particle "already/now"; it can also be "that" (kana), so check by eye.
Anything it cannot match is printed as UNMATCHED so you can decide whether it is a name, a loanword,
a form the list should know about, or a word that does not belong in the text yet.
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
    "kana/na (that)": {"kana"},   # bare "na" is NOT credited here; check by eye
    "diri": {"diri", "dinhi", "ari"},
    "didto": {"didto"},
}

NAMES = {"ana", "jun"}

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
    """Yield the Cebuano text of each numbered dialogue line."""
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if re.match(r"^\*\*\d+\.", line):
            bolds = re.findall(r"\*\*(.+?)\*\*", line)
            if len(bolds) >= 2:
                yield bolds[-1]


def analyse(paths):
    covered = {}       # entry -> set of surface forms seen
    unmatched = {}     # token -> count
    for path in paths:
        for text in cebuano_lines(path):
            raw = re.findall(r"[A-Za-z'\-]+", text)
            # contractions: naa'y, ko'y, wala'y, unsa'y -> drop the 'y
            raw = [w.replace("'y", "").replace("'", "") for w in raw]
            raw = [w for w in raw if w]
            lower = [w.lower() for w in raw]
            i = 0
            while i < len(lower):
                w = lower[i]
                nxt_raw = raw[i + 1] if i + 1 < len(raw) else ""
                nxt = nxt_raw.lower()
                if w == "maayong" and nxt in {"buntag", "hapon", "gabii"}:
                    covered.setdefault("maayong buntag/hapon/gabii", set()).add(w + " " + nxt)
                    covered.setdefault("maayo", set()).add("maayong")
                    covered.setdefault("nga", set()).add("-ng")
                    i += 2
                    continue
                if w == "ni":
                    entry = "ni (of)" if nxt_raw[:1].isupper() else "kini/ni (this)"
                    covered.setdefault(entry, set()).add("ni")
                    i += 1
                    continue
                if w in NAMES:
                    i += 1
                    continue
                entry = lookup(w)
                if entry:
                    covered.setdefault(entry, set()).add(w)
                    if w.endswith("ng") and w[:-2] in form_to_entry:
                        covered.setdefault("nga", set()).add("-ng")
                else:
                    unmatched[w] = unmatched.get(w, 0) + 1
                i += 1
    return covered, unmatched


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    covered, unmatched = analyse(argv)
    total = len(TIER1)
    print(f"Files: {', '.join(Path(p).name for p in argv)}")
    print(f"Tier 1 coverage: {len(covered)} / {total} entries\n")
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
    print("\nNote: bare 'na' is counted as the particle; if the text uses it as 'that' (kana), credit that by eye.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
