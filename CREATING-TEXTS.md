# Creating a text

How a new text is made for any language in this repository, from its row in the plan to the printed page, and the rules the text follows. `METHOD.md` says why texts are made this way; this file says how. The examples are from Cebuano, the first language done. What is specific to one language lives in that language's folder and in the tool tables; the last section says where.

## The steps

1. **Start from the row.** `<language>/texts.md` has one row per text, planned or written: the scene, the words it must bring in or introduce, the patterns to exercise. If the row is missing, write it first, looking at the words still under-exposed (`python3 tools/wordcheck.py --counts <language>/texts/src/*.txt`) and at the characters and the stage table at the top of `texts.md`. Two writers working from the same row produce the same words in different sentences; without the row they would also pick different words.
2. **Write the source**, `<language>/texts/src/NNN.txt`, in the format documented in `tools/render.py`: header lines (title, intro, tier, speakers), scene markers, one line per turn as `Speaker | text | close English`, an indented gloss line with one token per word, `!` notes, and after `===` the tail sections described below.
3. **Check it** before anyone reads it:
   - `python3 tools/wordcheck.py <language>/texts/src/NNN.txt`: nothing unmatched except names; the coverage count goes into the Word check section.
   - `python3 tools/wordcheck.py --new <language>/texts/src/*.txt`: the entries the text brings in match its row.
   - `python3 tools/wordcheck.py --chains <language>/texts/src/*.txt`: no chain against the small-words rule below.
   - `python3 tools/render.py` refuses a gloss line that does not line up with the words; `wordcheck.py --list` shows the "New in this text" list the readers will see.
4. **Show the source** to whoever reviews before rendering. A change is cheaper in the source than after three generated files exist.
5. **Generate**: the rendered text `<language>/texts/NNN-title.md` with `tools/render.py`; the pronunciation files with `tools/pron.py` if the language has them; the pocket PDF with `tools/print.py --glosses`, the booklet with `--all`.
6. **Record**: date the row in `texts.md` and add a dated line to the language's log. Nothing is committed until the reviewer agrees.

## The rules

### Words

- Only the tiers the text is allowed, plus the names of the characters. The row says which entries the text brings in; from the second tier on, five to eight per text. Where the scene allows, a new entry occurs more than once in the text that brings it in.
- Keep re-using the earlier words. The count that matters is occurrences across all texts (`--counts`): the entries at one or two occurrences are the next text's job. The goal per stage is set in the language's `texts.md` (Cebuano Stage A: every Tier 1 entry at five or more after text 005).

### Scene

Same characters, same setting, one continuing story, so the words come back on their own. A scene marker (`@ ...`) says where and when and is shown in blocks 1 and 2. Speakers are shown by indentation, in the order of the `speakers:` header; with four or more, render with `--names`.

The scene must be picturable (rule from 2026-11-10): something seen and something that happens, not a description. Objects and events go into the Cebuano where the tier allows, and into the English intro and scene markers where it does not; the English costs nothing from the tier. Events over states: water poured into two cups, a plate pointed at, money refused.

Where it comes from: the first Cebuano 002 was written to exercise words, walk, many people, eat, drink, go home. Reading it on 2026-11-10, the learner could picture nothing and afterwards not say what it had been about; the one line that stayed was the money refused, *Ayaw na, Day. Imoha na.* Their observation: they remember in pictures, and the common core words are mostly abstract, so the text has to supply the pictures around them. Concrete, imageable words are learned faster and kept longer than abstract ones (dual coding; de Groot and Keijzer 2000), for everyone and more so for a visual thinker; the core of a language is made of the abstract ones, which is the price of choosing words by frequency. 002 now has the hot streets, the stall with fish under a tin roof, Mama pouring water, and *merkado* to name the place.

### Length

Set by stage in the table at the top of the language's `texts.md`: short dialogues first (25 to 30 lines), longer as the known base grows, narrative paragraphs only once the verb forms are familiar. About 27 lines of dialogue fit one printed A4 page with the word-for-word footnote. Whether a longer text should take two pages or be trimmed is open; Cebuano 003 was trimmed to fit (2026-11-11), so no text has needed two pages yet.

### One new thing per sentence (rule from 2026-11-10)

A sentence brings in one new thing: a new word, a new form of a known word (*akong*, *gikaon*), a new pattern, or a chain of known small words, never two of them. Everything else in the sentence is known, so the reader can hold it steady and look at the one thing that moved. Stage A sentences average under three words; that is the rule at work, not thinness. The small-words rule below is the special case for pronouns, markers and particles.

Where it comes from: Cebuano 002, read on 2026-11-10 after the small-words revision, was still hard, and the hardest line was *Dili na, Ma. Daghan na kaayo ang akong gikaon*: *na*, *kaayo* stacked on it, the new form *akong* and the *gi-* verb used as a noun, in one sentence of five words, with the English "What I ate is already very much" unable to show which word did what. The learner asked whether separate sentences would be easier. The line is now *Dili na, Ma. Daghan na. Nikaon na ko.*, three sentences of a known word plus *na*, and *akong* and *gikaon* wait for 005. The rule serves the way the learner actually reads: pick a sentence, work out what it meant, memorise it or a part of it, one at a time.

### Small words one at a time (rule from 2026-11-08)

The small grammatical words, pronouns, markers and particles, are what a learner hears most and parses worst, and a chain of them is the hardest thing on the page: three in a row, each new or nearly new, and the close English cannot show which bit is which. So:

- A small word first appears in a sentence where it is the only new one, next to words already known: *Kumusta mo?* before *Nikaon na mo?*
- At most two small words in a row until each of them has been met on its own. Three or more only when all are familiar, and then a note spells the chain out: *na mo sa* = now + you(pl) + to.
- Look-alikes get a contrast pair in the same text, a few lines apart: *Gusto ka?* / *Gusto ba ka?*, *Dili na* / *Naa pa*.
- `wordcheck.py --chains` lists the chains with each member's exposure before that line; the set of small words is a table in it.

Where it comes from: reading Cebuano 002 (2026-11-08), the learner's hard spots were the sentences with several small words in a row, *pa* and *na* and the pronouns and markers around them: *Moinom pa ko og tubig*, *Nikaon na mi sa balay*, *Adto na mo sa balay*, *Moadto ba ka sa balay*. In each, three small words stand together, sometimes one of them new in that very line (*og*, *nimo*), and the English tells neither which word is which nor which comes first. Text 001 has no such chain; 002 had six lines with one, out of 27. The learner's own suggestion became the first bullet above: a sentence with one such word, saying clearly what it is, and the combination only later. The principle is older than this project: Ørberg's *Lingua Latina* introduces each new structure in a sentence where it is the only unknown, and graded readers keep to one new thing at a time.

### Close English

The English beside each line follows the words and, where English allows, their order, so every word of the text has a visible counterpart: *Dali diri!* → "Quick, here!", *trabaho ni Mama* → "the work of Mama". When one word's counterpart is two English words and another word would come between them, they are hyphenated, as in the gloss line: *naa pa* → "there-is still", not "there still is" (2026-11-07). It is deliberately not natural English; the note says what the line really means.

The order matters as much as the words. In Cebuano 003, *Daghan pa* first stood beside "Still a lot", and the learner read *pa* as "a lot", because the English put the Cebuano's last word first; "Much still" keeps the order and the reading right (2026-11-07). Where English cannot follow the order, the gloss line is the place that shows it, and a note says so.

### Glosses

One token per word, in order, no spaces inside a gloss (hyphenate: *there-is*, *to-a-boy*, *the(subj)*). The gloss is the word's literal core meaning, never the idiom: *dali* = quick, with a note "this is how you say come here", not *dali* = come. The first Cebuano draft had that backwards and the learner caught it; it is the easiest mistake to make, because the natural translation is what comes to mind first. A word with two jobs is glossed by the job it does in that line (*ni* = of or this, *na* = already, now or that), and the word checker reads the gloss to count it right.

### Notes

Short, under the gloss line, starting with `!`. They say what the idiom means, name the pattern (*root + ta = let's*), point out a contrast, or spell out a chain. An explanation longer than a line belongs in the language's grammar notes; the note points there.

### The tail

After `===`, copied as written:

- **Listen for**: the three to six patterns the text exercises, with the lines they are in.
- **Self-check**: read block 1 only and count the lines understood fully; the threshold is about 90 percent (24 of 27), below it re-read the earlier texts.
- **Word check**: the tiers used, the proper names, the coverage count from `wordcheck.py` for this text and cumulative, and the entries still unused.

## The layout, and the alternatives considered

Each text is rendered into a list of the words it brings in, each with the gloss of its first occurrence, and then three blocks: the text alone, for the cold read and for listening; the text with the close English beside it, for checking; word by word with notes, for looking up. For paper, `print.py` puts the text left and the close English right on one page, with the word-for-word as a footnote for the lines whose English does not already contain the gloss words. The booklet (`--all`) adds an intro page with a table of the texts and their word counts.

The layouts not chosen, and why (2026-10-07 and 2026-11-08):

- **English interleaved under each line**, as in Assimil and most textbooks. The first version here did that, with bold line numbers and speaker names in front of each line; the text never read as a conversation and the eye slid to the English. Dropped.
- **A natural translation on a facing page**, as in the bilingual readers. Reads well and hides the words. Useful at a later stage, when the reader already parses the sentence and only confirms the meaning.
- **Interlinear gloss only**, the Hamiltonian system, Interlinear Books. Dense, good for lookup, poor for reading. That is block 3, kept apart on purpose.
- **A lesson with a word list before the text and questions after**, the classic textbook shape. Pre-teaching the new words gives a modest, consistent gain, so the word list is taken over (2026-11-08): "New in this text" before block 1, generated from the gloss lines, in the rendered text, the full version and, as one compact line, on the pocket page; the self-check stands in for the questions.
- **Listening first** (Pimsleur, TPR) waits for audio.

No layout has been shown better than another in studies. What the studies support is the share of known words (about 95 percent and up for comfortable reading), spaced re-reading, retrieving before checking, glosses available but out of the way, and reading while listening; the three blocks and the schedule in `METHOD.md` keep to those. What a layout cannot do is make a chain of new small words parseable from a translation; that is solved in the writing, by the rule above.

## What is specific to a language

- Which words are small, how affixes are stripped, the names of the characters: the tables at the top of `tools/wordcheck.py`.
- The characters, the stages and the goal per stage: the top of the language's `texts.md`.
- Spelling conventions and the spoken forms: the top of the language's vocabulary file.
- Pronunciation: `tools/pron.py` and the language's `pronunciation/` folder, if any.
