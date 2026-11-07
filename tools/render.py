#!/usr/bin/env python3
"""Render a dialogue source file (<language>/texts/src/NNN.txt) into the three-block learner layout.

Block 1  Cebuano only, for a cold read or for listening along.
Block 2  Cebuano on the left, English on the right.
Block 3  Word by word: each Cebuano word with its meaning aligned under it, plus notes.

Who is speaking is shown by indentation (first speaker at the left margin, the next one
indented, the next one indented further), so names are not repeated on every line.
With --names a name column is printed instead.

Source format
  title: ...                   header lines, before the first dialogue line
  intro: ...
  tier: ...
  speakers: Ana | Jun | Mama   speakers in indent order. Any other speaker gets an inline label.
  @ scene marker               shown in blocks 1 and 2
  Speaker | Cebuano | English
      word=gloss word=gloss    (indented) one token per Cebuano word, in order; glosses carry
                               no spaces (hyphenate), a bare word means "no gloss"
      ! note                   (indented, starts with !) shown under the gloss
  ===                          everything after this line is copied verbatim

Usage
  python3 tools/render.py cebuano/texts/src/002.txt > cebuano/texts/002-xxx.md
  python3 tools/render.py --names cebuano/texts/src/002.txt > cebuano/texts/002-xxx.md
"""
import re
import sys
import textwrap
from pathlib import Path

STEP1 = 8     # indent per speaker level, block 1
STEP2 = 4     # indent per speaker level, block 2
EN_W = 38     # wrap width for the English column
GAP = 3       # spaces between the Cebuano and English columns

HOWTO = ("How to use: read block 1 on its own first. Then block 2 to check what you understood. "
         "Block 3 only for the words you could not place. The English in block 2 stays close to the "
         "Cebuano words, so it is not always natural English; where the real meaning differs, block 3 says so.")


def parse(path):
    header, entries, tail = {}, [], []
    n, in_tail = 0, False
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if in_tail:
            tail.append(raw)
            continue
        if raw.strip() == "===":
            in_tail = True
            continue
        if not raw.strip():
            continue
        if raw.startswith("@"):
            entries.append({"type": "scene", "text": raw[1:].strip()})
            continue
        if raw[0].isspace():
            cur = entries[-1]
            s = raw.strip()
            if s.startswith("!"):
                cur["notes"].append(s[1:].strip())
            else:
                cur["gloss"] = [t.split("=", 1) if "=" in t else [t, ""] for t in s.split()]
            continue
        if not entries and re.match(r"^[a-z]+:\s", raw):      # header line, before any dialogue
            k, v = raw.split(":", 1)
            header[k.strip()] = v.strip()
            continue
        if " | " in raw:
            spk, ceb, en = [x.strip() for x in raw.split("|")]
            n += 1
            entries.append({"type": "line", "n": n, "speaker": spk, "ceb": ceb, "en": en,
                            "gloss": [], "notes": []})
            continue
        raise SystemExit(f"cannot parse: {raw}")
    return header, entries, tail


def validate(entries):
    for e in entries:
        if e["type"] != "line" or not e["gloss"]:
            continue
        words = e["ceb"].split()
        gw = [w for w, _ in e["gloss"]]
        if gw != words:
            raise SystemExit(f"line {e['n']}: gloss words do not match the text\n  text : {words}\n  gloss: {gw}")


def left(e, levels, step, name_w):
    """The Cebuano side of a line: indented by speaker level, or prefixed by a name column."""
    if levels is None:
        return f"{e['speaker']:<{name_w}}{e['ceb']}", 0
    lvl = levels.get(e["speaker"])
    if lvl is None:
        return f"{e['speaker']}: {e['ceb']}", 0
    return " " * (lvl * step) + e["ceb"], lvl * step


def legend(levels):
    names = sorted(levels, key=levels.get)
    parts = [f"{names[0]} speaks from the left margin"]
    if len(names) > 1:
        parts.append(f"{names[1]} indented")
    for nm in names[2:]:
        parts.append(f"{nm} indented further")
    return "Who speaks: " + ", ".join(parts) + ". Names are not repeated."


def render(header, entries, tail, names_mode=False):
    lines = [e for e in entries if e["type"] == "line"]
    levels = None if names_mode else (
        {s.strip(): i for i, s in enumerate(header["speakers"].split("|"))} if "speakers" in header else None)
    name_w = max(len(e["speaker"]) for e in lines) + 2
    out = [f"# {header['title']}", ""]
    for key in ("intro", "tier"):
        if key in header:
            out += [header[key], ""]
    out += [HOWTO, ""]

    # Block 1
    out += ["## 1 · Read (Cebuano only)", ""]
    if levels:
        out += [legend(levels), ""]
    out.append("```")
    for i, e in enumerate(entries):
        if e["type"] == "scene":
            if i:
                out.append("")
            out += [f"({e['text']})", ""]
        else:
            out.append(left(e, levels, STEP1, name_w)[0])
    out += ["```", ""]

    # Block 2
    out += ["## 2 · Side by side (close English)", ""]
    if levels:
        out += [legend(levels), ""]
    out.append("```")
    width = max(len(left(e, levels, STEP2, name_w)[0]) for e in lines) + GAP
    for i, e in enumerate(entries):
        if e["type"] == "scene":
            if i:
                out.append("")
            out += [f"({e['text']})", ""]
            continue
        lt, _ = left(e, levels, STEP2, name_w)
        en = textwrap.wrap(e["en"], EN_W) or [""]
        out.append(f"{lt:<{width}}{en[0]}")
        for cont in en[1:]:
            out.append(" " * width + cont)
    out += ["```", ""]

    # Block 3
    out += ["## 3 · Word by word", ""]
    out.append("```")
    for e in lines:
        if e["gloss"]:
            widths = [max(len(w), len(g)) + 2 for w, g in e["gloss"]]
            l1 = "".join(f"{w:<{wd}}" for (w, _), wd in zip(e["gloss"], widths)).rstrip()
            l2 = "".join(f"{g:<{wd}}" for (_, g), wd in zip(e["gloss"], widths)).rstrip()
            out += [f"{e['n']:>2}  {l1}", f"    {l2}"]
        else:
            out.append(f"{e['n']:>2}  {e['ceb']}")
        for note in e["notes"]:
            out.append(f"    · {note}")
        out.append("")
    if out[-1] == "":
        out.pop()
    out += ["```", ""]
    out += tail
    return "\n".join(out).rstrip() + "\n"


def main(argv):
    names_mode = "--names" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__)
        return 1
    header, entries, tail = parse(paths[0])
    validate(entries)
    sys.stdout.write(render(header, entries, tail, names_mode))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
