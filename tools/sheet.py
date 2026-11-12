#!/usr/bin/env python3
"""Print a reference sheet written in markdown (<language>/<name>.md) to <language>/print/<language>-<name>.pdf,
in the same style as the pocket pages. Meant for the one-page sheets beside the texts, such as the word sets.

Understood: '# ' and '## ' headings, paragraphs, '- ' lists, pipe tables (first row the header, second the
'|---|' rule), and inline **bold**, *italic* and `code`. Nothing else; keep the sheet simple.

Usage:  python3 tools/sheet.py cebuano/word-sets.md            (add --two for two columns on the page)
Needs Google Chrome, as print.py does.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import print as pr  # noqa: E402   the CSS, footer, Chrome

CSS = """
@page { margin: 9mm 10mm 7mm 10mm; }
body { font-size: 8.6pt; line-height: 1.24; }
section.sheet h1 { font-size: 14pt; margin: 0 0 3pt 0; }
section.sheet h2 { font-size: 9.8pt; margin: 5pt 0 2pt 0; break-after: avoid; }
section.sheet p { margin: 0 0 4pt 0; }
section.sheet p.lead { font-size: 8.4pt; }
section.sheet ul { margin: 0 0 4pt 0; padding-left: 14pt; }
section.sheet table { width: 100%; border-collapse: collapse; margin: 0 0 4pt 0; break-inside: avoid; }
section.sheet th { text-align: left; font-weight: 600; border-bottom: 0.6pt solid #000; padding: 1pt 6pt 1pt 0; vertical-align: bottom; }
section.sheet td { padding: 1pt 6pt 1pt 0; vertical-align: top; }
section.sheet div.two { column-count: 2; column-gap: 18pt; }
section.sheet div.two table.wide { column-span: all; }
"""


def inline(text):
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def to_html(md):
    out, para, table, items = [], [], [], []

    def flush():
        nonlocal para, table, items
        if para:
            cls = " class='lead'" if not out or out[-1].startswith("<h1") else ""
            out.append(f"<p{cls}>{inline(' '.join(para))}</p>"); para = []
        if table:
            head, body = table[0], [r for r in table[1:] if not re.match(r"^\|?\s*:?-{2,}", r)]
            rows = ["<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells(head)) + "</tr>"]
            rows += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>" for r in body]
            wide = " class='wide'" if len(cells(head)) >= 5 else ""      # a wide table spans both columns
            out.append(f"<table{wide}>" + "".join(rows) + "</table>"); table = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"); items = []

    for line in md.splitlines():
        if line.startswith("# "):
            flush(); out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("## "):
            flush(); out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("|"):
            if para or items: flush()
            table.append(line)
        elif line.startswith("- "):
            if para or table: flush()
            items.append(line[2:])
        elif not line.strip():
            flush()
        else:
            if table or items: flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


def main(argv):
    two = "--two" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__); return 1
    for p in paths:
        body = to_html(p.read_text(encoding="utf-8"))
        if two:                                     # the title and lead paragraph span the page, the rest in two columns
            m = re.match(r"(<h1>.*?</h1>\n<p class='lead'>.*?</p>\n)(.*)", body, re.S)
            body = (m.group(1) + "<div class='two'>" + m.group(2) + "</div>") if m else body
        section = f"<style>{CSS}</style><section class='sheet'>{body}</section>"
        lang = p.parent.name
        out = p.parent / "print" / f"{lang}-{p.stem}.pdf"
        out.parent.mkdir(exist_ok=True)
        pr.to_pdf(pr.document([section], pr.content_date(p)), out)
        print(f"{p} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
