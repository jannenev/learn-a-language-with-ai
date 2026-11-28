# Version 2 of the word list: what changes and why

Proposed and approved on 2026-11-28. Version 2 is the list in use, [`cebuano/vocabulary.md`](../../vocabulary.md); version 1 is kept under the git tag `vocabulary-v1`.

**Status.** Written with AI assistance. The new entries and their examples are not checked by a native speaker. The figures are from [`CHECK-2026-11-28.md`](CHECK-2026-11-28.md).

## In short

|                        | Version 1        | Version 2 |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------- |
| Tier 1                 | 65 entries       | 65, unchanged |
| Tier 2                 | about 59         | about 76: nine words that were in no tier, eight from Tier 3; nothing leaves |
| Tiers 1 and 2 together | about 124        | about 141 |
| Tier 3, the backlog    | about 131        | about 151: the eight leave, 28 words found by the count come in as candidates |
| Order inside Tier 2    | by category only | by category, with the commonest named as the ones to bring in first |

Only words on which both ways of checking agree are taken into Tier 2: common in Cebuano text, and, where English has the word, common in spoken English.

## The words that come into Tier 2

Occurrences per 10,000 words; the last column is the place of the English word in spoken English.

| Word        | From    | Meaning                     | tatoeba | news | English | Section of the list |
| ----------- | ------- | --------------------------- | ------- | ---- | ------- | -------------------------- |
| ka          | no tier | between a number and a noun | 38      | 122  | none    | 2.8 Numbers |
| may         | no tier | there is (= *naa*)          | 28      | 14   | none    | 2.9 Spoken words |
| kang        | no tier | to or of a person           | 16      | 12   | none    | 2.1 Connectors and markers |
| o           | no tier | or                          | 11      | 11   | 43      | 2.1 |
| tungod      | no tier | because of                  | 8.3     | 26   | none    | 2.1 |
| ana / ani   | no tier | like that / like this       | 23      | 3.2  | none    | 2.9 |
| mas         | no tier | more                        | 6.4     | 4.8  | 77      | 2.7 Describing words |
| butang      | no tier | thing; put                  | 3.7     | 3.2  | 55      | 2.5 Nouns |
| bahin       | no tier | about; part                 | 4.6     | 12   | 42      | 2.1 |
| aron        | Tier 3  | so that                     | 16      | 22   | none    | 2.1 |
| bisan       | Tier 3  | even; any-                  | 13      | 14   | 88      | 2.1 |
| kinahanglan | Tier 3  | need, must                  | 23      | 5.5  | 98      | 2.4 Verbs |
| human       | Tier 3  | finished; after             | 12      | 47   | 157     | 2.6 Time |
| tuig        | Tier 3  | year                        | 16      | 17   | 86      | 2.6 |
| uban        | Tier 3  | others; with                | 8.3     | 21   | 38      | 2.7 |
| bag-o       | Tier 3  | new                         | 18      | 9.0  | 177     | 2.7 |
| lain        | Tier 3  | other, different            | 7.3     | 12   | 79      | 2.7 |

For scale: the middle entry of Tier 2 has 7.3 and 2.7, so each of these is commoner than the usual Tier 2 word. Together the seventeen were expected to raise what Tiers 1 and 2 cover from 60 to about 62 percent of the Tatoeba sentences, from 54 to about 58 of the news, and from 66 to about 70 of the Bible. The count after the change gave 62.5, 57.7 and 70.3.

## The order inside Tier 2

The list now says which Tier 2 words are the commonest, to be brought in by the first texts of Stage B: *kay, man, mao, kung, pero, usa* with *ka*, *para, tanan, o, may, kang*.

In the plan as it stands (`cebuano/texts.md`), *man* comes in text 007, *tanan* in 009, *kay* and *pero* in 010, *mao* in 011, and *kung* and *para* only in 014, the last text of the stage.

## What does not change, and why

- **Tier 1.** Decided on 2026-11-28: it stays as taught. So *may* is an entry of its own in Tier 2 and not a form under *naa*, and *o*, or, is an entry of its own although the short *oo*, yes, is also said *o*.
- **No Tier 2 word is moved down.** The rare ones in the count are words of speech or of the scenes (*kuan* does not occur once in writing; *barato, kape, lagi, sus*), and a count of written text cannot judge those.
- **The examples of version 1** are untouched.

## Waiting for the speakers' answers

These do not hold up version 2. An answer changes a form inside an entry, or moves one word, and can be made as a small correction to version 2.

| Question in [`QUESTIONS.md`](QUESTIONS.md)                                  | What the answer decides |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| A: naa · may · duna                                                         | Whether *may* stays an entry or becomes a note under *naa* |
| A: o · or; mas · pa; kinahanglan · kailangan · need                         | The form given first in those entries |
| A: butang · kuan                                                            | Whether *butang* earns its place in Tier 2 |
| B: sama, gihapon, nahitabo, diha, diay, sakto, dayon                        | Whether these come up from Tier 3 too; the counts rest on one kind of text, or the meaning is spread over several words |
| B: basin, sulay, gamit, klase, pasabot, medyo; A: siyempre, sigurado, kaysa | Whether these are said at all in everyday talk; they are common in spoken English and hardly occur in the Cebuano sources |
| A: ganahan · gusto                                                          | Whether *ganahan* comes up from Tier 3 |

## What followed, and what is still to do

Done on 2026-11-28:

1. **The list.** The tag `vocabulary-v1` was set on the last commit before the change, and version 2 put in place as `cebuano/vocabulary.md`.
2. **The counting tool.** In `tools/wordfreq.py` the seventeen words are in the Tier 2 table. The table of words in no tier keeps the fourteen that are still in none.
3. **Counted again** on the same three sources; the figures are at the end of the check, the tables in `data/version-2/`.

Still to do, each on its own:

4. **The plan of the texts.** Stage B in `cebuano/texts.md` is laid out as eight texts for 57 entries. With 76 entries at six to eight a text it is ten to twelve texts, and their order changes so that the commonest words come first. To be proposed row by row.
5. **The pronunciation lexicon.** Seventeen words to add to `cebuano/pronunciation/lexicon.tsv`, marked `check`.
6. **The woven stories.** In `cebuano/weaving/WORD-ORDER.md`, rows of the commonest English words that say "none" now have a core word: or (*o*), with (*uban*), more (*mas*), other (*lain*), year (*tuig*), new (*bag-o*), thing (*butang*), need (*kinahanglan*), after (*human*), any (*bisan*), about (*bahin*). Each still has to be looked at where it stands, as that file says. No word already woven changes.
7. **The figures in other files.** "About 120 words" in `README.md`, `METHOD.md`, `cebuano/PLAN.md` and the booklet intro is now about 140.
8. **`tools/wordcheck.py`** has no Tier 2 yet; when it gets one (plan, step 5), it is this one.
