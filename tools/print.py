#!/usr/bin/env python3
"""Make a printable A4 PDF of a text: the "pocket" version, the language on the left and the close
English on the right, meant to be folded or covered for a cold read. One PDF per text, written to
<language>/print/<language>-NNN-pocket.pdf; with --all also a booklet holding every text given,
<language>/print/<language>-pocket-NNN-MMM.pdf, with an intro page made from <language>/booklet-intro.md
(if present) followed by the generated facts: variant, a table of the texts with their dates and word counts
(core entries used, new in the text, known after it; counted by tools/wordcheck.py), commit.

Usage:
  python3 tools/print.py cebuano/texts/src/002.txt
  python3 tools/print.py --all cebuano/texts/src/*.txt
  python3 tools/print.py --html cebuano/texts/src/002.txt     also keep the intermediate HTML
  python3 tools/print.py --glosses cebuano/texts/src/001.txt  add a "word for word" footnote for the lines
                                                              whose English does not follow the words
  python3 tools/print.py --tag b cebuano/texts/src/001.txt    write 001b-pocket.pdf instead of 001-pocket.pdf
  python3 tools/print.py --full cebuano/texts/src/001.txt     the full version instead: all three blocks, the
                                                              notes, and the sections after the text (needs pandoc)

Every page carries a footer with the repository address (from the git remote, as a clickable link)
and the content date: the date of the last commit that touched the text's source, or the file's own
date if it has uncommitted changes or git is absent. For a file with several texts it is the newest
of their dates. The footer is left out when there is no git remote.

Needs Google Chrome, which is run headless to print the HTML to PDF.
"""
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render import parse, validate, legend  # noqa: E402
try:
    from wordcheck import analyse, TIER1, new_in_text  # noqa: E402   # the core-word table; Cebuano-specific
except ImportError:                                                   # another language without a word checker
    analyse = TIER1 = new_in_text = None

CHROME = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "google-chrome", "chromium", "chromium-browser"]

CSS = """
@page { size: A4 portrait; margin: 10mm 11mm 8mm 11mm; }
div.foot { position: fixed; bottom: 0; left: 0; right: 0; font-size: 7.5pt; text-align: center; }
div.foot a { color: #000; text-decoration: none; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.3; color: #000; margin: 0; }
section { page-break-after: always; }
section:last-child { page-break-after: auto; }
h1 { font-size: 14pt; margin: 0 0 2pt 0; font-weight: 600; }
p.intro { margin: 0 0 4pt 0; font-size: 9.5pt; }
p.howto { margin: 0 0 6pt 0; font-size: 8.5pt; }
p.new { margin: 0 0 6pt 0; font-size: 8.5pt; line-height: 1.3; }
div.newlist { columns: 3; column-gap: 14pt; font-size: 9.5pt; margin-bottom: 4pt; }
div.newlist p { margin: 0 0 1pt 0; break-inside: avoid; }
table { border-collapse: collapse; width: 100%; }
td { vertical-align: top; padding: 1pt 0; }
td.ceb { width: 54%; padding-right: 10pt; }
td.en  { width: 46%; border-left: 0.6pt solid #000; padding-left: 10pt; }
td.l1 { padding-left: 14pt; }
td.l2 { padding-left: 28pt; }
td.l1 .lbl, td.l2 .lbl { display: none; }
tr.scene td { font-style: italic; padding-top: 5pt; padding-bottom: 2pt; }
span.who { font-size: 9pt; }
h2 { font-size: 10pt; margin: 8pt 0 1pt 0; font-weight: 600; }
p.gnote { font-size: 8.5pt; margin: 0 0 3pt 0; }
div.gl { column-count: 2; column-gap: 16pt; }
h2.blk { font-size: 11pt; margin: 12pt 0 4pt 0; break-after: avoid; }
div.read p { margin: 0; padding: 1pt 0; }
div.read p.l1 { padding-left: 14pt; }
div.read p.l2 { padding-left: 28pt; }
div.read p.scene { font-style: italic; padding-top: 5pt; padding-bottom: 2pt; }
div.wbw { break-inside: avoid; margin: 0 0 5pt 0; }
div.wbw .n { display: inline-block; width: 16pt; font-size: 8.5pt; vertical-align: top; padding-top: 1pt; }
div.il { display: inline-flex; flex-wrap: wrap; column-gap: 9pt; row-gap: 2pt; width: calc(100% - 18pt); vertical-align: top; }
div.il span { display: inline-block; }
div.il span i { display: block; font-style: normal; font-size: 8.5pt; }
div.wbw p.note { margin: 1pt 0 0 16pt; font-size: 8.5pt; }
table.pg { width: 100%; border-collapse: collapse; }
table.pg > tbody > tr > td.pgc { padding: 0; }
table.pg > tfoot > tr > td.sp { height: 14pt; padding: 0; }
section.intro { font-size: 10.5pt; }
section.intro h1 { font-size: 15pt; margin-bottom: 8pt; }
section.intro p { margin: 0 0 7pt 0; }
section.intro table.facts { width: auto; margin-top: 10pt; font-size: 9.5pt; }
section.intro table.facts td, section.intro table.facts th { padding: 1pt 12pt 1pt 0; text-align: left; font-weight: normal; }
section.intro table.facts th { font-weight: 600; border-bottom: 0.6pt solid #000; }
section.intro table.facts td.n, section.intro table.facts th.n { text-align: right; }
section.intro p.words { font-size: 9pt; margin-top: 4pt; }
div.tail { font-size: 9.5pt; }
div.tail h2 { font-size: 10pt; margin: 9pt 0 2pt 0; }
div.tail p, div.tail li { margin: 0 0 2pt 0; }
div.tail ul { margin: 0; padding-left: 14pt; }
p.g { font-size: 9pt; line-height: 1.25; margin: 0 0 1pt 0; break-inside: avoid; }
p.g b { font-weight: 600; }
"""

HOWTO = "Cover the right column and read the left; uncover to check. The English is word for word, not natural English."


def git(*args):
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True, timeout=20)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def repo_url():
    """The repository's web address from its git remote, or empty."""
    url = git("remote", "get-url", "origin")
    if url.startswith("git@"):
        url = "https://" + url[4:].replace(":", "/", 1)
    if url.endswith(".git"):
        url = url[:-4]
    return url if url.startswith("http") else ""


def content_date(path):
    """Date of the last commit touching the file, or the file's date if changed since or not in git."""
    path = Path(path)
    if git("status", "--porcelain", "--", str(path)) == "":
        d = git("log", "-1", "--format=%cs", "--", str(path))
        if d:
            return d
    import datetime
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()


def footer(date):
    url = repo_url()
    if not url:
        return ""
    shown = url.replace("https://", "").replace("http://", "")
    return f"<div class='foot'><a href='{html.escape(url)}'>{html.escape(shown)}</a> · {html.escape(date)}</div>"


def find_chrome():
    for c in CHROME:
        if Path(c).exists() or shutil.which(c):
            return c
    raise SystemExit("Google Chrome not found; it is needed to print the HTML to PDF.")


def words(text):
    """Lowercased words of an English string or of a gloss, for comparing the two."""
    t = text.lower().replace("-", " ").replace("[?]", " questionmarker ").replace("(", " ").replace(")", " ")
    t = t.replace("what's", "what").replace("that's", "that").replace("it's", "it")
    out = []
    for w in re.findall(r"[a-z']+", t):
        w = {"ok": "okay", "too": "also", "me": "i", "mom": "ma"}.get(w, w)
        if w in ("is", "are", "am", "it", "the", "a", "an"):      # English glue with no Cebuano counterpart
            continue
        out.append(w)
    return out


def sentences(e):
    """Split a line into sentences: list of (cebuano, gloss_tokens, english). Falls back to the whole line
    when the Cebuano and the English do not split into the same number of sentences."""
    groups, cur = [], []
    for w, g in e["gloss"]:
        cur.append((w, g))
        if w[-1] in ".!?…":
            groups.append(cur); cur = []
    if cur:
        groups.append(cur)
    ens = re.split(r"(?<=[.!?…])\s+", e["en"].strip())
    if len(groups) != len(ens):
        return [(e["ceb"], e["gloss"], e["en"])]
    return [(" ".join(w for w, _ in grp), grp, en) for grp, en in zip(groups, ens)]


def is_direct(gloss, en):
    """True when the English uses the gloss words, in any order, with only English glue words added."""
    if not any(g for _, g in gloss):
        return True
    gl = []
    for w, g in gloss:
        gl += words(g if g else w)
    return sorted(words(en)) == sorted(gl)      # order ignored: Cebuano puts the predicate first


def unexplained(gloss, en):
    """The Cebuano words of a sentence whose gloss words are not visible in the English."""
    pool = list(words(en))
    out = []
    for w, g in gloss:
        if not g:
            continue
        gw = words(g)
        if all(x in pool for x in gw):
            for x in gw:
                pool.remove(x)
        else:
            out.append(w.strip("!?.,…").lower())
    return out


def footnote(entries):
    """One entry per sentence that contains a word not visible in the English and not explained
    earlier in this text, so each such word is explained once."""
    items, seen = [], set()
    for e in entries:
        if e["type"] != "line" or not e["gloss"]:
            continue
        for ceb, gloss, en in sentences(e):
            if is_direct(gloss, en):
                continue
            new_words = [w for w in unexplained(gloss, en) if w not in seen]
            if not new_words:
                continue
            seen.update(new_words)
            literal = " ".join(g if g else w.strip("!?.,…") for w, g in gloss)
            items.append(f"<p class='g'><b>{html.escape(ceb)}</b> &nbsp;{html.escape(literal)}</p>")
    if not items:
        return ""
    return ("<h2>Word for word</h2><p class='gnote'>Where the English does not follow the Cebuano word by word, each word explained once. "
            "A hyphen joins one word's meaning (will-eat); [?] is the question marker.</p>"
            "<div class='gl'>" + "\n".join(items) + "</div>")


def new_words(path):
    """(count, [(word, gloss), ...]) for the words a text brings in, or (0, []) when unknown."""
    if not (new_in_text and path):
        return 0, []
    items = new_in_text(path)
    return len(items), [(w, g) for w, g, _ in items]


def text_section(header, entries, glosses=False, path=None):
    levels = {s.strip(): i for i, s in enumerate(header["speakers"].split("|"))} if "speakers" in header else None
    out = [f"<section><h1>{html.escape(header['title'])}</h1>"]
    if "intro" in header:
        out.append(f"<p class='intro'>{html.escape(header['intro'])}</p>")
    who = legend(levels).replace("Who speaks: ", "") if levels else "Speaker names at the left."
    out.append(f"<p class='howto'>{html.escape(HOWTO)} {html.escape(who)}</p>")
    n, pairs = new_words(path)
    if n:
        joined = " · ".join(f"<b>{html.escape(w)}</b> {html.escape(g)}" for w, g in pairs)
        out.append(f"<p class='new'><b>New in this text ({n}):</b> {joined}</p>")
    out.append("<table>")
    for e in entries:
        if e["type"] == "scene":
            out.append(f"<tr class='scene'><td colspan='2'>({html.escape(e['text'])})</td></tr>")
            continue
        cls, label = "ceb", ""
        if levels is None:
            label = f"<span class='who'>{html.escape(e['speaker'])}</span>&nbsp; "
        else:
            lvl = levels.get(e["speaker"])
            if lvl is None:
                label = f"<span class='who'>{html.escape(e['speaker'])}:</span> "
            elif lvl:
                cls += f" l{min(lvl, 2)}"
        out.append(f"<tr><td class='{cls}'>{label}{html.escape(e['ceb'])}</td><td class='en'>{html.escape(e['en'])}</td></tr>")
    out.append("</table>")
    if glosses:
        out.append(footnote(entries))
    out.append("</section>")
    return "\n".join(out)


def tail_html(tail):
    md = "\n".join(tail).strip()
    if not md:
        return ""
    if not shutil.which("pandoc"):
        return "<pre>" + html.escape(md) + "</pre>"
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html"], input=md, capture_output=True, text=True)
    return r.stdout


def full_section(header, entries, tail, path=None):
    levels = {s.strip(): i for i, s in enumerate(header["speakers"].split("|"))} if "speakers" in header else None
    out = [f"<section><h1>{html.escape(header['title'])}</h1>"]
    for key in ("intro", "tier"):
        if key in header:
            out.append(f"<p class='intro'>{html.escape(header[key])}</p>")
    n, pairs = new_words(path)
    if n:
        out.append(f"<h2 class='blk'>New in this text ({n})</h2>")
        out.append("<p class='howto'>The words this text brings in, each with the meaning it has here. Read them once before block 1.</p>")
        out.append("<div class='newlist'>" + "".join(f"<p><b>{html.escape(w)}</b> {html.escape(g)}</p>" for w, g in pairs) + "</div>")
    # block 1: the language only
    out.append("<h2 class='blk'>1 · Read (Cebuano only)</h2>")
    if levels:
        out.append(f"<p class='howto'>{html.escape(legend(levels))}</p>")
    out.append("<div class='read'>")
    for e in entries:
        if e["type"] == "scene":
            out.append(f"<p class='scene'>({html.escape(e['text'])})</p>")
            continue
        lvl = levels.get(e["speaker"]) if levels else None
        label = "" if (levels and lvl is not None) else f"<span class='who'>{html.escape(e['speaker'])}:</span> "
        cls = f" class='l{min(lvl, 2)}'" if lvl else ""
        out.append(f"<p{cls}>{label}{html.escape(e['ceb'])}</p>")
    out.append("</div>")
    # block 2: side by side (same table as the pocket page)
    out.append("<h2 class='blk'>2 · Side by side (close English)</h2>")
    pocket = text_section(header, entries)
    out.append(pocket[pocket.index("<table>"):pocket.index("</table>") + 8])
    # block 3: word by word with notes
    out.append("<h2 class='blk'>3 · Word by word</h2>")
    for e in entries:
        if e["type"] != "line":
            continue
        pairs = "".join(f"<span>{html.escape(w)}<i>{html.escape(g) if g else '&nbsp;'}</i></span>" for w, g in e["gloss"]) \
            if e["gloss"] else f"<span>{html.escape(e['ceb'])}</span>"
        notes = "".join(f"<p class='note'>· {html.escape(n)}</p>" for n in e["notes"])
        out.append(f"<div class='wbw'><span class='n'>{e['n']}</span><div class='il'>{pairs}</div>{notes}</div>")
    out.append("<div class='tail'>" + tail_html(tail) + "</div></section>")
    return "\n".join(out)


def intro_section(lang, paths, variant, dates):
    """The booklet's first page: the hand-written intro (booklet-intro.md), then the generated facts."""
    md_path = lang / "booklet-intro.md"
    body = tail_html(md_path.read_text(encoding="utf-8").splitlines()) if md_path.exists() else ""
    kind = {"pocket": "This is the pocket version: one page per text, with the word-for-word notes below the dialogue.",
            "full": "This is the full version: for each text, the Cebuano alone, the Cebuano beside the English, and the word-by-word block with notes."}[variant]
    counting = analyse is not None
    rows = ["<tr><th>Text</th><th>Date</th>" + ("<th class='n'>Words used</th><th class='n'>New here</th><th class='n'>Known after</th>" if counting else "") + "</tr>"]
    seen = set()
    for p, d in zip(paths, dates):
        header, _, _ = parse(p)
        cells = f"<td>{html.escape(header['title'])}</td><td>{d}</td>"
        if counting:
            used = set(analyse([p])[0])
            new = used - seen
            seen |= used
            cells += f"<td class='n'>{len(used)}</td><td class='n'>{len(new)}</td><td class='n'>{len(seen)}</td>"
        rows.append(f"<tr>{cells}</tr>")
    words_note = ""
    if counting:
        words_note = (f"<p class='words'>Words are counted as entries of the core list, {len(TIER1)} in Tier 1; an entry is a word with "
                      "its spoken forms (kaon, mokaon, nikaon count as one). The columns give how many entries the text uses, how many "
                      "appear in it for the first time, and how many have appeared by the end of it.</p>")
    commit = git("log", "-1", "--format=%h", "--", *[str(p) for p in paths])
    facts = (f"<p>{kind}</p><table class='facts'>" + "".join(rows) + "</table>" + words_note
             + (f"<p style='font-size:9pt'>Version: content dated {max(dates)}, commit {commit}.</p>" if commit else ""))
    return f"<section class='intro'>{body}{facts}</section>"


def document(sections, date=""):
    body = "\n".join(sections)
    foot = footer(date) if date else ""
    if foot:
        # The footer is position: fixed, which Chrome repeats on every page but which reserves no room, so
        # on a full page the last line would print under it. Wrapping the content in a table whose empty
        # <tfoot> Chrome repeats at every page break keeps that much space clear at the foot of each page.
        body = ("<table class='pg'><tfoot><tr><td class='sp'></td></tr></tfoot>"
                "<tbody><tr><td class='pgc'>\n" + body + "\n</td></tr></tbody></table>")
    return ("<!doctype html><html><head><meta charset='utf-8'><title>pocket</title>"
            f"<style>{CSS}</style></head><body>\n" + foot + "\n" + body + "\n</body></html>\n")


def to_pdf(html_text, pdf_path, keep_html=False):
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html_path = pdf_path.with_suffix(".html") if keep_html else Path(tempfile.mkdtemp()) / "pocket.html"
    html_path.write_text(html_text, encoding="utf-8")
    cmd = [find_chrome(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
           f"--print-to-pdf={pdf_path.resolve()}", html_path.resolve().as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not pdf_path.exists():
        raise SystemExit(f"Chrome did not write {pdf_path}:\n{r.stderr[-800:]}")
    # Pin the creation and modification dates Chrome writes into the PDF, so that regenerating an
    # unchanged text gives a byte-identical file and git does not record a new version each time.
    # Same-length replacement keeps the PDF's internal byte offsets valid.
    data = pdf_path.read_bytes()
    pdf_path.write_bytes(re.sub(rb"D:\d{14}\+00'00'", b"D:20000101000000+00'00'", data))
    if not keep_html:
        html_path.unlink(missing_ok=True)


def main(argv):
    want_all = "--all" in argv
    keep_html = "--html" in argv
    glosses = "--glosses" in argv
    full = "--full" in argv
    tag = argv[argv.index("--tag") + 1] if "--tag" in argv else ""
    if tag:
        argv = [a for a in argv if a != tag]
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 1
    sections, dates = [], []
    out_dir = lang = None
    for p in paths:
        header, entries, tail = parse(p)
        validate(entries)
        lang = next(d for d in p.resolve().parents if (d / "texts").is_dir())
        out_dir = lang / "print"
        stem = p.stem[:3] + tag
        variant = "full" if full else "pocket"
        sec = full_section(header, entries, tail, p) if full else text_section(header, entries, glosses, p)
        pdf = out_dir / f"{lang.name}-{stem}-{variant}.pdf"
        date = content_date(p)
        to_pdf(document([sec], date), pdf, keep_html)
        print(f"{p.name} -> {pdf.relative_to(lang.parent)}  ({date})")
        sections.append(sec)
        dates.append(date)
    if want_all and len(sections) > 1:
        variant = "full" if full else "pocket"
        first, last = paths[0].stem[:3], paths[-1].stem[:3]
        pdf = out_dir / f"{lang.name}-{variant}{tag}-{first}-{last}.pdf"
        intro = intro_section(lang, paths, variant, dates)
        to_pdf(document([intro] + sections, max(dates)), pdf, keep_html)
        print(f"booklet -> {pdf.relative_to(out_dir.parent.parent)}  ({max(dates)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
