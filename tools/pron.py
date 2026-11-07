#!/usr/bin/env python3
"""Generate pronunciation files for a text, for software and AI voices rather than for reading.

For <language>/texts/src/NNN.txt it writes into <language>/pronunciation/:
  NNN.paste.txt   rules-for-ai.txt followed by the Cebuano lines with stress and glottal marks,
                  ready to paste into a chat voice (ChatGPT voice mode and the like)
  NNN.ipa.txt     one IPA transcription per line, syllables separated by dots
  NNN.ssml.xml    SSML with <phoneme alphabet="ipa"> per word, for an Azure Filipino voice

Marks come from <language>/pronunciation/lexicon.tsv. Words not in the lexicon are tried as prefix + root
(mo-, ni-, nag-, gi-, ... keep the root's stress). Anything still unknown is printed and written
in [brackets] so it can be added to the lexicon.

Usage:  python3 tools/pron.py cebuano/texts/src/002.txt
"""
import csv
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from wordcheck import cebuano_lines  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def language_dir(path):
    """The language folder: the nearest ancestor of the text that holds a pronunciation/ directory."""
    for d in Path(path).resolve().parents:
        if (d / "pronunciation").is_dir():
            return d
    raise SystemExit(f"no pronunciation/ folder found above {path}")

PREFIXES = ["naka", "maka", "nag", "mag", "pag", "mo", "mi", "ni", "gi", "ma", "na", "ka", "i"]
VOICE = "fil-PH-BlessicaNeural"
ACUTE, GRAVE, CIRC = "́", "̀", "̂"
VOWEL_IPA = {"a": "a", "e": "ɛ", "i": "i", "o": "o", "u": "u"}
CONS_IPA = {"j": "dʒ", "y": "j", "r": "ɾ", "c": "k", "q": "k", "z": "s", "v": "b", "f": "p", "x": "ks"}
GLIDES = {"ɾ", "l", "w", "j"}


def load_lexicon(lex_path):
    lex = {}
    with lex_path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f, delimiter="\t") if r and not r[0].startswith("#")]
    for r in rows[1:]:
        r += [""] * (5 - len(r))
        lex[r[0].lower()] = {"marked": r[1], "status": r[2], "ipa": r[4]}
    return lex


def marked_form(word, lex):
    """Return (marked, how) for a surface word; how = lexicon | derived | unknown."""
    key = word.lower().replace("'", "")
    if key in lex:
        return lex[key]["marked"], "lexicon"
    for p in PREFIXES:
        if key.startswith(p) and len(key) > len(p) + 2:
            rest = key[len(p):]
            hyph = rest.startswith("-")
            rest = rest.lstrip("-")
            if rest in lex and lex[rest]["marked"] != rest:   # root must be a real stressed word
                return p + ("-" if hyph else "") + lex[rest]["marked"], "derived"
    return word, "unknown"


def to_ipa(marked, override=""):
    """Marked spelling -> IPA. Stress from the acute/circumflex, final glottal from grave/circumflex."""
    if override:
        return override
    s = unicodedata.normalize("NFD", marked.lower())
    units = []        # each: dict(sym, vowel, stress, glottal)
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in (ACUTE, GRAVE, CIRC):
            if units:
                if ch in (ACUTE, CIRC):
                    units[-1]["stress"] = True
                if ch in (GRAVE, CIRC):
                    units[-1]["glottal"] = True
            i += 1
            continue
        if s.startswith("ng", i):
            units.append({"sym": "ŋ", "vowel": False}); i += 2; continue
        if s.startswith("ts", i):
            units.append({"sym": "tʃ", "vowel": False}); i += 2; continue
        if ch == "-":
            units.append({"sym": "ʔ", "vowel": False}); i += 1; continue
        if ch == "'":
            i += 1; continue
        if ch in VOWEL_IPA:
            units.append({"sym": VOWEL_IPA[ch], "vowel": True, "stress": False, "glottal": False}); i += 1; continue
        units.append({"sym": CONS_IPA.get(ch, ch), "vowel": False}); i += 1
    # syllabify: onset = consonants before a vowel; a run between vowels splits before its last consonant,
    # unless the run is a two-consonant cluster ending in a glide (tr, kw, sy, ...), which stays together.
    vidx = [k for k, u in enumerate(units) if u["vowel"]]
    if not vidx:
        return "".join(u["sym"] for u in units)
    sylls = []
    start = 0
    for n, v in enumerate(vidx):
        if n == len(vidx) - 1:
            end = len(units)
        else:
            run = units[v + 1:vidx[n + 1]]
            if len(run) <= 1:
                end = v + 1
            elif len(run) == 2 and run[1]["sym"] in GLIDES and run[0]["sym"] != "ʔ":
                end = v + 1
            else:
                end = vidx[n + 1] - 1
        sylls.append(units[start:end])
        start = end
    out = []
    for syl in sylls:
        txt = "".join(u["sym"] for u in syl)
        vow = next(u for u in syl if u["vowel"])
        if vow["glottal"] and syl is sylls[-1]:
            txt += "ʔ"
        out.append(("ˈ" if vow["stress"] else "") + txt)
    ipa = ".".join(out).replace(".ˈ", "ˈ")
    return ipa


def tokens(line):
    """Split a Cebuano line into (word, trailing punctuation) pairs, keeping other characters."""
    return re.findall(r"([A-Za-z'\-]+)|([^A-Za-z'\-]+)", line)


def process(path):
    lang = language_dir(path)
    out_dir = lang / "pronunciation"
    lex = load_lexicon(out_dir / "lexicon.tsv")
    stem = re.match(r"(\d{3})", Path(path).name).group(1)
    lines = list(cebuano_lines(path))
    marked_lines, ipa_lines, ssml_lines, unknown, derived = [], [], [], {}, {}
    for line in lines:
        m_parts, i_parts, s_parts = [], [], []
        for word, other in tokens(line):
            if other:
                m_parts.append(other); i_parts.append(other); s_parts.append(escape(other)); continue
            marked, how = marked_form(word, lex)
            if how == "unknown":
                unknown[word] = unknown.get(word, 0) + 1
                m_parts.append(f"[{word}]"); i_parts.append(f"[{word}]"); s_parts.append(escape(word)); continue
            if how == "derived":
                derived[word] = marked
            if word[0].isupper():
                marked = marked[0].upper() + marked[1:]
            key = word.lower().replace("'", "")
            ipa = to_ipa(marked, lex.get(key, {}).get("ipa", ""))
            m_parts.append(marked); i_parts.append(ipa)
            s_parts.append(f'<phoneme alphabet="ipa" ph="{ipa.replace(".", "")}">{escape(word)}</phoneme>')
        marked_lines.append("".join(m_parts)); ipa_lines.append("".join(i_parts))
        ssml_lines.append("".join(s_parts))

    rel = Path(path).resolve().relative_to(ROOT).as_posix()
    header = f"Generated by tools/pron.py from {rel} and {lang.name}/pronunciation/lexicon.tsv. Do not edit by hand."
    (out_dir / f"{stem}.paste.txt").write_text(
        (out_dir / "rules-for-ai.txt").read_text(encoding="utf-8").rstrip() + "\n\n" + "\n".join(marked_lines) + "\n", encoding="utf-8")
    (out_dir / f"{stem}.ipa.txt").write_text("# " + header + "\n" + "\n".join(ipa_lines) + "\n", encoding="utf-8")
    ssml = ['<?xml version="1.0" encoding="UTF-8"?>', f"<!-- {header} -->",
            '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="fil-PH">',
            f'  <voice name="{VOICE}">', '    <prosody rate="-10%">']
    for s in ssml_lines:
        ssml.append(f"      <s>{s}</s>")
        ssml.append('      <break time="700ms"/>')
    ssml += ["    </prosody>", "  </voice>", "</speak>"]
    (out_dir / f"{stem}.ssml.xml").write_text("\n".join(ssml) + "\n", encoding="utf-8")

    print(f"{Path(path).name}: {len(lines)} lines -> {lang.name}/pronunciation/{stem}.paste.txt, {stem}.ipa.txt, {stem}.ssml.xml")
    if derived:
        print("  derived from a root: " + ", ".join(f"{w}→{m}" for w, m in sorted(derived.items())))
    if unknown:
        print("  UNKNOWN (add to lexicon): " + ", ".join(sorted(unknown)))
    checks = sorted({w.lower() for l in lines for w, _ in tokens(l) if w and lex.get(w.lower().replace("'", ""), {}).get("status") == "check"})
    if checks:
        print("  marked 'check' in lexicon: " + ", ".join(checks))


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    for p in sys.argv[1:]:
        process(p)
