# The Cebuano word list: how it was made, checked and changed

The list itself is [`cebuano/vocabulary.md`](../../vocabulary.md), and that is the file to use. This folder is about the list: where it came from, what a check of it found, and what is decided about changing it. How a word list is made and checked for any language is in the top-level [`docs/vocabulary/`](../../../docs/vocabulary/).

**Status.** The list and everything in this folder were written with AI assistance and have not been checked by a native speaker.

## What is in this folder

| File or folder                                               | What it is |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`CHECK-2026-11-28.md`](CHECK-2026-11-28.md)                 | The check: the tiers counted in three kinds of Cebuano text and matched against the 300 commonest words of spoken English, with the sources, the figures and the limits |
| [`QUESTIONS.md`](QUESTIONS.md)                               | The sheet to give to a native speaker: lists to mark, on what the check leaves open. It holds only what the speaker needs; how to ask is in the section below |
| [`data/tier-counts.tsv`](data/tier-counts.tsv)               | Every entry of the three tiers, and 40 words that are in no tier, with occurrences per 10,000 words in each source |
| [`data/version-2/`](data/version-2/)                         | The same tables counted again after version 2 of the list |
| [`data/no-tier-*.tsv`](data/)                                | For each source, the 300 commonest words that matched nothing: where to look for further candidates |
| [`data/spoken-english-300.tsv`](data/spoken-english-300.tsv) | The 300 commonest words of spoken English, each with its Cebuano word and the tier it is in, or "none", or "no word" |
| [`CHANGES-v2.md`](CHANGES-v2.md)                             | Version 2 of the list: which seventeen words came into Tier 2 and why, what did not change, what waits for the speakers' answers, and what is still to do in other files |

## How the list was made

On 2026-09-20, in one pass, by an AI assistant (Claude) from what it knew of the language. The learner had asked for 50 to 100 common words, "not directly necessarily ranked most common, but taking into account what categories are used", for understanding speech. No frequency list, corpus or dictionary was consulted, and no native speaker. Nothing was written down about single words: why one is in Tier 1 and another in Tier 3 is not recorded anywhere.

Changes since then:

| Date       | Change                                                                                                                                                       | Why |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| 2026-10-06 | Eight spoken words added to Tier 2 as section 2.9: *mao, kuan, kanang, murag, siguro, basta, gani, sus*                                                      | The estimate of how much speech the tiers cover showed that they were missing |
| 2026-11-11 | *merkado* moved from Tier 3 to Tier 2                                                                                                                        | Text 003 needed it to name the place |
| 2026-11-28 | Version 2: seventeen words into Tier 2 (nine from no tier, eight from Tier 3), the commonest Tier 2 words named, 28 candidates into Tier 3. Tier 1 unchanged | The check of the same day; see `CHANGES-v2.md` |

The estimate of 2026-10-06 (`../../PLAN.md`, section 2) was a reasoned guess, not a measurement.

## What is built on the list

- **Texts 001 to 005** use Tier 1 only, and all its 65 entries have appeared by 005. One Tier 2 word, *merkado*, is in 003.
- **`tools/wordcheck.py`** holds its own copy of Tier 1, to be kept in sync by hand. It does not read the list. Tier 2 is not in it yet.
- **`tools/wordfreq.py`** takes Tier 1 from `wordcheck.py`, holds its own copy of Tier 2 (that of version 2), and reads Tier 3 from the list.
- **The woven stories** take their words from Tiers 1 and 2 (`../../weaving/WORD-ORDER.md`), and have already brought in Tier 2 words such as *pero, tanan, niingon, usa*.
- **The pronunciation lexicon** and the published PDFs follow the texts.

## What the check found

In short, and about version 1 of the list; the figures are in [`CHECK-2026-11-28.md`](CHECK-2026-11-28.md).

- **Tier 1 holds.** Its small words are the commonest words of every source, and it covers about half of the running words of everyday sentences, as estimated.
- **Tiers 2 and 3 add less than estimated:** about 8 points each on everyday sentences, where the plan assumed 15 and 11.
- **Some Tier 2 words are commoner than most of Tier 1:** *kay, man, mao, kung, pero, usa*.
- **Some common words are in no tier:** *ka* after a number, *may, kang, o, tungod, ana / ani, mas*.
- **Some Tier 3 words are common:** *aron, uban, kinahanglan, human, tuig, bisan, bag-o*.
- **Some Tier 1 words are rare in every text** (*lami, tulog, hulat, salamat*). They are there for the situations, which is the method's choice.

## What is decided (2026-11-28)

- **One file.** The list stays `cebuano/vocabulary.md`, and says at its top which version it is. Version 1 is the git tag `vocabulary-v1`.
- **Version 2 is the list in use,** approved by the learner on 2026-11-28.
- **Tier 1 stays as it is for now:** the 65 entries the texts have taught.
- **The speakers' answers come as corrections to version 2,** not as a new list: a form inside an entry, or one word moving.

## What is open

- **The work in other files that version 2 brings:** the plan of Stage B, the pronunciation lexicon, the table of the woven stories, and the figure "about 120 words". Listed in `CHANGES-v2.md`.
- **The answers to the questions,** and with them whether *may* stays an entry of its own and which further words come up from Tier 3.
- **Whether Tier 1 should grow** by the few words that are commoner than most of it. It would mean one or two more texts in Stage A.
- **The estimate in the plan and in the README** ("roughly two thirds of everyday conversation") is still the guess of 2026-10-06. The check measured written text, not conversation, so it does not simply replace it.
- **`wordcheck.py` knows only Tier 1,** and Tier 3 has never been counted in the course's own texts.

## Asking the questions

[`QUESTIONS.md`](QUESTIONS.md) is the sheet for the speaker, and nothing else is on it. This section is for the one who hands it out.

- **Why lists to mark.** The check counted written text, and written text does not show which words people say. The sheet puts to a speaker what the counting could not settle. Every part is a list to mark, because seeing what is odd in a list is easy, and thinking of what is missing from one is hard and gives an incomplete answer. (The learner's observation, 2026-11-28.) Only part D asks for words from memory.
- **Where the words come from.** Part A: words on which the sources disagree, and pairs where the word list gives two forms. Part B: words that are common in written Cebuano or in spoken English and are in Tier 2, Tier 3 or no tier. Part C: Tier 1. The words and their English were written with AI assistance and are not checked.
- **To print:** `python3 tools/sheet.py --form cebuano/docs/vocabulary/QUESTIONS.md` makes `cebuano/print/cebuano-questions.pdf`, two pages, for one sheet of paper printed on both sides.
- **How to ask.** Hand over the paper, or show the file on a phone, or read the lists aloud. Say that it is about everyday talk, not about correct Cebuano.
- **The answers.** One file per speaker in this folder, `answers-YYYY-MM-DD.md`, with the marks typed in, the place the speaker is from and roughly the age. No names in this repository. And a row here:

| Date | Speaker (place, rough age) | Parts answered | File |
| ---- | -------------------------- | -------------- | ---- |
|      |                            |                | |

## Before changing the list again

1. Read `docs/vocabulary/README.md`, sections 5 and 6, and the check and `CHANGES-v2.md` in this folder.
2. A correction that follows from a speaker's answer goes straight into the list, with a line in `CHANGES-v2.md` saying what and why.
3. A change of more than a few words is a new version: write it as a draft in `draft/` here, with a table of what changes and why beside it, and wait for the learner's approval.
4. On approval: set the tag for the version being left (`vocabulary-v2`), replace the list, mark the new version at its top, bring the tables of `tools/wordcheck.py` and `tools/wordfreq.py` and the planned rows of `../../texts.md` into line, and add a dated line to `../../LOG.md`.
5. Run `tools/wordfreq.py` again on the same sources and put the new figures beside the old.
