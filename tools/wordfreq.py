#!/usr/bin/env python3
"""Count how often the entries of the Cebuano word list occur in ordinary Cebuano text.

It answers two questions about cebuano/vocabulary.md that the course's own texts cannot answer, since
they were written to use those words: how much of real text each tier covers, and which frequent words
are in a low tier or in none.

Usage:
    python3 tools/wordfreq.py NAME=FILE [NAME=FILE ...]            # print the coverage and the commonest entries
    python3 tools/wordfreq.py --out DIR NAME=FILE [NAME=FILE ...]  # also write the tables into DIR
    python3 tools/wordfreq.py --leipzig-part SITE FOLDER > FILE    # take one site's sentences out of a Leipzig corpus

FILE is plain text, one sentence or paragraph per line; NAME is a short label for it (news, bible).
With --out it writes
    tier-counts.tsv      one row per entry: tier, entry, occurrences per 10,000 words in each source, commonest forms
    no-tier-NAME.tsv     the 300 commonest words of that source that matched nothing, with a mark on likely names
FOLDER is an unpacked corpus of the Leipzig Corpora Collection (the files NAME-sentences.txt, NAME-sources.txt
and NAME-inv_so.txt); SITE is a piece of the source address, such as sunstar.com.ph.

How it counts. Tier 1 is the table of wordcheck.py; Tier 2 is the table below; Tier 3 is read from the
backlog in cebuano/vocabulary.md; NONE below holds words that are in no tier and that a check turned up,
so that they are counted by name and not lost among the unmatched. The tables follow version 2 of the list. A word is matched whole, then with the
linker (-ng, -g) or the short "ang" (-y) taken off, then, for content words only, with a light strip of
affixes. The strip is rough: it misses some forms and now and then credits a wrong one, so read the
figures to about a tenth of their size and look at the "commonest forms" column before trusting a row.
Not separated: ni "of" from ni "this", na "already" from na "that", and the senses of ingon, kita and una.
A word written with a capital inside a sentence and matching nothing is taken as a name and left out of
the coverage.

The tables are Cebuano; for another language replace them, as in wordcheck.py.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import wordcheck  # noqa: E402   the Tier 1 table

VOCABULARY = Path(__file__).resolve().parent.parent / "cebuano" / "vocabulary.md"

# ---------------------------------------------------------------- Tier 1: wordcheck's table, with the
# forms that ordinary text adds (older spellings, the long forms of the pronouns, short written forms)
T1 = {k: set(v) for k, v in wordcheck.TIER1.items()}
T1["oo"].discard("o")                       # in running text "o" is nearly always "or"
T1["ni (of)"] = {"ni"}                      # of / this cannot be told apart without a gloss
T1.pop("kini/ni (this)")
T1["kini (this)"] = {"kini", "niini", "ning", "niining"}
T1["kana/na (that)"] = {"kana", "niana"}
T1["maayong buntag/hapon/gabii"] = set()    # counted under maayo and under buntag/hapon/gabii
T1["ako"] |= {"kanako", "akoa", "ako-a", "akoy", "koy"}
T1["ikaw"] |= {"kanimo", "imo", "imuha", "imo-a", "ikay"}
T1["siya"] |= {"kaniya", "iya", "siyay"}
T1["kita (we)"] |= {"kanato", "ato"}
T1["kami"] |= {"kanamo", "amo"}
T1["kamo"] |= {"kaninyo", "inyo"}
T1["sila"] |= {"kanila", "ila", "silay"}
T1["gyud"] |= {"gayud"}
T1["pud"] |= {"pod", "sab"}
T1["dili"] |= {"dli"}
T1["wala"] |= {"way"}
T1["na"] |= {"nay"}
T1["pa"] |= {"pay"}
T1["naa"] |= {"anaa", "adunay", "dunay"}
T1["kumusta"] |= {"kamusta"}
T1["kasabot"] |= {"sabut", "kasabut"}
T1["karon"] |= {"karong"}
T1["Mama/Papa"] = {"mama", "papa", "nanay", "tatay", "inahan", "amahan"}
T1["buntag/hapon/gabii"] |= {"gabi-i"}
T1["dako"] |= {"daku"}

# ---------------------------------------------------------------- Tier 2: keep in sync with vocabulary.md
T2 = {
    "man": {"man"}, "kay": {"kay"}, "pero": {"pero", "apan"}, "kung": {"kung", "kon", "kun"},
    "gikan": {"gikan"}, "para": {"para", "alang"}, "tanan": {"tanan"}, "una": {"una"},
    "ambot": {"ambot"}, "lagi": {"lagi"}, "hala/ay": {"hala", "ay", "uy"},
    "kanus-a": {"kanus-a", "anus-a", "kanusa"}, "ngano": {"ngano", "nganong"},
    "unsaon": {"unsaon", "giunsa"},
    "palit": {"palit"}, "bayad": {"bayad", "bayran"}, "hatag": {"hatag"}, "kuha": {"kuha"},
    "buhat": {"buhat"}, "ingon": {"ingon"}, "tan-aw": {"tan-aw", "tanaw"},
    "kita (see)": {"makita", "nakita", "kit-an", "nakit-an", "makit-an", "gikita",
                   "nakakita", "makakita", "nakitan", "makitan"},
    "paminaw": {"paminaw"}, "lakaw": {"lakaw"}, "balik": {"balik"}, "anhi": {"anhi"},
    "pwede": {"pwede", "puede", "puwede", "mahimo"},
    "amigo/amiga": {"amigo", "amiga", "higala"}, "pamilya": {"pamilya"}, "anak": {"anak"},
    "igsoon": {"igsoon", "igsuon"}, "bata": {"bata"}, "kan-on": {"kan-on", "kanon", "humay", "bugas"},
    "isda": {"isda"}, "kape": {"kape"}, "adlaw": {"adlaw"}, "oras": {"oras"},
    "merkado": {"merkado"}, "gahapon": {"gahapon"}, "ganina": {"ganina"},
    "kanunay": {"kanunay", "pirmi", "permi"}, "mahal": {"mahal"}, "barato": {"barato"},
    "init": {"init"}, "tugnaw": {"tugnaw", "bugnaw"}, "kapoy": {"kapoy"},
    "gutom": {"gutom", "busog"}, "sakit": {"sakit"}, "nindot": {"nindot"},
    "numbers 1-10": {"usa", "duha", "tulo", "upat", "lima", "unom", "pito", "walo", "siyam",
                     "napulo", "uno", "dos", "tres", "kwatro", "singko", "syete", "otso",
                     "nwebe", "dyes", "baynte", "singkwenta", "syento"},
    "mao": {"mao"}, "kuan": {"kuan", "kuwan"}, "kanang": {"kanang"}, "murag": {"murag", "mura"},
    "siguro": {"siguro"}, "basta": {"basta"}, "gani": {"gani"}, "sus": {"sus"},
    # the seventeen entries that version 2 of the list added (2026-11-28)
    "o (or)": set(), "ka (after a number)": set(),        # both decided by the neighbouring word, see count()
    "kang": {"kang"}, "tungod": {"tungod", "tungud"}, "aron": {"aron"}, "bisan": {"bisan"},
    "bahin": {"bahin", "kabahin"}, "kinahanglan": {"kinahanglan"}, "butang": {"butang"},
    "tuig": {"tuig"}, "human": {"human"}, "bag-o": {"bag-o"}, "lain": {"lain"}, "uban": {"uban"},
    "mas": {"mas"}, "may": {"may"},
    "ana / ani": {"ana", "anang", "ani", "aning", "ingon-ana", "ingon-ani", "ingana", "ingani"},
}

# ---------------------------------------------------------------- Tier 3: read from the backlog
T3_SPELLINGS = {"lalaki": {"lalake"}, "babaye": {"babae"}, "hangtod": {"hangtud"},
                "syudad": {"siyudad", "ciudad", "dakbayan"},
                "kadto": {"kato"}, "tibuok": {"tibook"}, "palihug": {"palihog"}, "sama": {"susama"},
                "hitabo": {"panghitabo"}, "himo": {"himuon"}, "dala": {"dad-on", "dad-a", "dalha"}}


def read_backlog(path=VOCABULARY):
    """The entries of '## Tier 3' in vocabulary.md: 'word — meaning' items separated by ' · '."""
    table = {}
    backlog = Path(path).read_text(encoding="utf-8").split("## Tier 3", 1)[1]
    for line in backlog.splitlines():
        if not line.startswith("**"):
            continue
        for item in line.split(":**", 1)[1].split(" · "):
            if "→" in item or " — " not in item:        # a pointer to an entry of Tier 1 or 2
                continue
            forms = set()
            for w in re.split(r"[/,]", item.split(" — ", 1)[0]):
                w = w.strip().lower()
                if re.fullmatch(r"[a-z\-']+", w) and len(w) > 2:
                    forms.add(w.replace("'", "").strip("-"))
            if forms:
                table[" / ".join(sorted(forms))] = forms
    for listed_elsewhere in ("ra", "pud", "pasabot"):       # pasabot is counted under its root, kasabot
        table.pop(listed_elsewhere, None)
    for entry, more in T3_SPELLINGS.items():
        if entry in table:
            table[entry] |= more
    return table


T3 = read_backlog()

# ---------------------------------------------------------------- in no tier: words the checks turned up.
# Version 2 of the list took nine of the first forty into Tier 2 and eighteen into the backlog; these remain.
NONE = {
    "ngadto (to, toward)": {"ngadto"}, "niadtong (last ..., back when)": {"niadtong"},
    "mahitungod (concerning)": {"mahitungod"}, "patay (dead, die)": {"patay", "namatay", "mamatay", "kamatayon"},
    "ha (tag)": {"ha"}, "buot (want, formal)": {"buot"}, "busa (so, therefore)": {"busa"},
    "pinaagi (by means of)": {"pinaagi"}, "batok (against)": {"batok"},
    "labi / labing (most)": {"labi", "labing", "pinaka"}, "nasod / nasud (country)": {"nasod", "nasud"},
    "libro (book)": {"libro"}, "iro (dog)": {"iro"}, "hinuon (instead, however)": {"hinuon", "hinoon"},
}

TIERS = (("1", T1), ("2", T2), ("3", T3), ("none", NONE))

# Only content words are reached by stripping affixes; the small words are matched whole.
ROOTS_1 = {"maayo", "adto", "kaon", "inom", "tulog", "trabaho", "gusto", "kahibalo", "kasabot", "dali",
           "hulat", "balay", "tubig", "kwarta", "tawo", "buntag/hapon/gabii", "dako", "gamay", "daghan", "lami"}
ROOTS_2 = {"palit", "bayad", "hatag", "kuha", "buhat", "ingon", "tan-aw", "paminaw", "lakaw", "balik", "anhi",
           "anak", "bata", "isda", "adlaw", "oras", "mahal", "init", "tugnaw", "kapoy", "gutom", "sakit", "nindot",
           "kinahanglan", "butang", "tuig", "human", "bag-o", "lain", "uban"}
NOT_ROOTS_3 = {"diay", "kaha", "unta", "daw / kuno", "bitaw", "matag", "kada", "bisan", "aron", "samtang",
               "sorry", "dayon", "hangtod", "usahay", "puhon", "driver", "jeep",
               "gud", "basin", "medyo", "kaysa", "hapit", "pipila", "gihapon", "diha", "kadto", "sama",
               "siyempre", "sigurado", "palihug"}
strippable = set()
for _table, _keep in ((T1, ROOTS_1), (T2, ROOTS_2), (T3, set(T3) - NOT_ROOTS_3)):
    for _entry in _keep:
        strippable |= _table.get(_entry, set())

form_to = {}
for _tier, _table in TIERS:
    for _entry, _forms in _table.items():
        for _f in _forms:
            form_to.setdefault(_f, (_tier, _entry))

PREFIXES = ["nanag", "nagpa", "magpa", "pagka", "gipa", "naga", "maga", "naka", "maka", "paga",
            "nag", "mag", "pag", "nang", "mang", "pang", "ming", "mo", "mi", "ni", "gi", "ma",
            "na", "ka", "pa", "i"]
SUFFIXES = ["hon", "han", "on", "an", "a", "i"]
NUMBERISH = T2["numbers 1-10"] | {"pila", "pipila", "daghan", "gatus", "gatos", "libo", "napulog"}


def lookup(tok):
    """(tier, entry) for a lowercase word, or None."""
    if tok in form_to:
        return form_to[tok]
    if tok.endswith("ng") and tok[:-2] in form_to:                    # the linker: maayong, kining
        return form_to[tok[:-2]]
    if tok.endswith("g") and len(tok) > 3 and tok[:-1] in form_to:    # daghang, tanang; siyag = siya og
        return form_to[tok[:-1]]
    if tok.endswith("y") and len(tok) > 3 and tok[:-1] in form_to:    # walay, maoy, unsay
        return form_to[tok[:-1]]
    for p in PREFIXES:
        if tok.startswith(p) and len(tok) > len(p) + 2:
            rest = tok[len(p):].lstrip("-")
            if len(rest) >= 4 and rest in strippable:
                return form_to[rest]
            for s in SUFFIXES:
                if rest.endswith(s) and len(rest) - len(s) >= 4 and rest[:-len(s)] in strippable:
                    return form_to[rest[:-len(s)]]
    for s in SUFFIXES:
        if tok.endswith(s) and len(tok) - len(s) >= 4 and tok[:-len(s)] in strippable:
            return form_to[tok[:-len(s)]]
    return None


def tokens(line):
    """(lowercase word, written with a capital inside a sentence) per word; a number comes out as "0"."""
    out = []
    first = True
    for m in re.finditer(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’\-]*|[0-9][0-9.,:]*|[.!?]", line):
        w = m.group(0)
        if w in ".!?":
            first = True
            continue
        if w[0].isdigit():
            out.append(("0", False))
            first = False
            continue
        w = w.replace("’", "'").replace("'y", "").replace("'", "").strip("-")
        if not w:
            continue
        out.append((w.lower(), w[0].isupper() and not first))
        first = False
    return out


def count(path):
    """Count one source. Returns a dict with the totals, per tier, per entry, the forms seen and the unmatched."""
    r = {"words": 0, "tier": Counter(), "entry": Counter(), "forms": defaultdict(Counter),
         "unmatched": Counter(), "capital": Counter()}
    for line in open(path, encoding="utf-8", errors="ignore"):
        toks = tokens(line)
        for i, (w, cap) in enumerate(toks):
            if w == "0":
                continue
            r["words"] += 1
            prev = toks[i - 1][0] if i else ""
            if w == "ka" and (prev == "0" or prev in NUMBERISH):      # tulo ka bata: not "you"
                hit = ("2", "ka (after a number)")
            elif w == "o":
                hit = ("2", "o (or)")
            else:
                hit = lookup(w)
            if hit:
                r["tier"][hit[0]] += 1
                r["entry"][hit] += 1
                r["forms"][hit][w] += 1
            else:
                r["unmatched"][w] += 1
                if cap:
                    r["capital"][w] += 1
    r["names"] = sum(n for w, n in r["unmatched"].items() if r["capital"][w] > 0.7 * n)
    return r


def leipzig_part(site, folder):
    """Print the sentences of a Leipzig corpus folder whose source address contains `site`."""
    folder = Path(folder)

    def one(suffix):
        found = list(folder.glob(f"*-{suffix}.txt"))
        if not found:
            sys.exit(f"no *-{suffix}.txt in {folder}")
        return found[0]

    wanted = set()
    for line in open(one("sources"), encoding="utf-8", errors="ignore"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2 and site in p[1]:
            wanted.add(p[0])
    source_of = {}
    for line in open(one("inv_so"), encoding="utf-8", errors="ignore"):
        p = line.split("\t")                 # source number, sentence number
        if len(p) >= 2:
            source_of[p[1].strip()] = p[0].strip()
    n = 0
    for line in open(one("sentences"), encoding="utf-8", errors="ignore"):
        p = line.rstrip("\n").split("\t", 1)
        if len(p) == 2 and source_of.get(p[0]) in wanted:
            print(p[1])
            n += 1
    print(f"{len(wanted)} sources, {n} sentences", file=sys.stderr)


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    if argv[0] == "--leipzig-part":
        if len(argv) != 3:
            print(__doc__)
            return 1
        leipzig_part(argv[1], argv[2])
        return 0
    out = None
    if argv[0] == "--out":
        out = Path(argv[1])
        argv = argv[2:]
    sources = [a.split("=", 1) for a in argv if "=" in a]
    if not sources or len(sources) != len(argv):
        print(__doc__)
        return 1
    results = {name: count(path) for name, path in sources}

    print("Share of the words that are not names:")
    print(f"  {'source':<12}{'words':>9}{'names':>8}{'Tier 1':>9}{'1-2':>8}{'1-3':>8}{'+ none':>9}")
    for name, r in results.items():
        base = r["words"] - r["names"]
        t1, t2, t3, tn = (r["tier"][k] for k in ("1", "2", "3", "none"))
        print(f"  {name:<12}{r['words']:>9}{r['names']:>8}{100 * t1 / base:>8.1f}%{100 * (t1 + t2) / base:>7.1f}%"
              f"{100 * (t1 + t2 + t3) / base:>7.1f}%{100 * (t1 + t2 + t3 + tn) / base:>8.1f}%")
    print("  ('+ none' adds the words of the NONE table, which are in no tier)")

    def per10k(r, key):
        return 10000 * r["entry"][key] / r["words"]

    first = next(iter(results.values()))
    keys = [(tier, entry) for tier, table in TIERS for entry in table]
    print(f"\nThe 60 commonest entries of the first source, occurrences per 10,000 words ({', '.join(results)}):")
    for tier, entry in sorted(keys, key=lambda k: -first["entry"][k])[:60]:
        row = "".join(f"{per10k(r, (tier, entry)):>8.1f}" for r in results.values())
        print(f"  {tier:<5}{entry:<34}{row}")

    if out:
        out.mkdir(parents=True, exist_ok=True)
        with open(out / "tier-counts.tsv", "w", encoding="utf-8") as f:
            f.write("tier\tentry\t" + "\t".join(results) + "\tcommonest forms (in the first source that has any)\n")
            for tier, entry in keys:
                forms = ""
                for r in results.values():
                    if r["forms"][(tier, entry)]:
                        forms = " ".join(f"{w}:{n}" for w, n in r["forms"][(tier, entry)].most_common(5))
                        break
                f.write(f"{tier}\t{entry}\t" + "\t".join(f"{per10k(r, (tier, entry)):.1f}" for r in results.values())
                        + f"\t{forms}\n")
        for name, r in results.items():
            with open(out / f"no-tier-{name}.tsv", "w", encoding="utf-8") as f:
                f.write("word\toccurrences\tper 10,000 words\tname?\n")
                for w, n in r["unmatched"].most_common(300):
                    mark = "name?" if r["capital"][w] > 0.7 * n else ""
                    f.write(f"{w}\t{n}\t{10000 * n / r['words']:.1f}\t{mark}\n")
        print(f"\nWritten to {out}: tier-counts.tsv, " + ", ".join(f"no-tier-{n}.tsv" for n in results))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
