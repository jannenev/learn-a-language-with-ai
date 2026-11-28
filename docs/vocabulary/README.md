# The core words: choosing them, checking them, changing them

The method starts from a list of core words (step 2 of `METHOD.md`). This document says how such a list is made, why it then has to be checked, the ways of checking and what each can and cannot show, and how a list is changed once texts are built on it.

The worked example is Cebuano: [`cebuano/docs/vocabulary/`](../../cebuano/docs/vocabulary/) has how that list was made, the check of it with its figures, and what was decided.

**Status.** Written on 2026-11-28 with AI assistance, from one language and one round of checking. Where a lesson is called general, that is our reading of one case.

## 1. Making the list

1. **The goal first.** For understanding speech the list must hold what is heard, which is mostly small words: pronouns, markers, particles, fillers. For reading it would hold more nouns.
2. **By category, not by rank.** Go through the categories and take the commonest items of each: persons; the glue words (markers, articles, prepositions); particles; yes, no and "there is"; question words; greetings and social words; the commonest verbs; nouns of home, food, money and people; time; describing words; pointing words. Then add the fillers and exclamations, which word lists tend to miss.
3. **Tiers.** About 60 entries to start, about 50 more, then a backlog kept in compact form.
4. **An entry is a root** with the forms actually heard, or a tight cluster such as the numbers one to ten.
5. **Write down how the list was made:** the date, who or what made it, from which sources, and for a word that was a close call, why it went in or stayed out. The Cebuano list has no such record for its words, and a later session could not tell a choice from an oversight.

Why by category: a ranking by frequency alone is headed by grammatical words and has no greeting, no water and no money in it, the words of the situations a learner meets. The check of the Cebuano list supports both halves of the choice. The small words of its first tier are the commonest words of every text counted; and its words for situations (thank you, wait, delicious) are rare in every text and are needed all the same.

## 2. Why the list has to be checked

An assistant writes such a list in minutes, from what it knows of the language, and for a small language it knows less. What can be wrong, each with what the Cebuano check found:

- **A common word is in no tier.** *O*, or; *mas*, more.
- **A common word is in too low a tier.** *Kay*, because, was in the second tier and is commoner than most of the first.
- **A small word that only this language has is missed,** because no list in another language suggests it. *Ka*, the word between a number and a noun, is among the forty commonest words of Cebuano text and was not an entry.
- **The estimate of how much speech the tiers cover is a guess.** The second tier added about half of what had been assumed, the third a little more than half.

**Check early.** The Cebuano list was checked after five texts had been written on its first tier, and by then the first tier could only be kept as it was. Before the first text is written, every change is free.

## 3. The ways of checking

| Way                                                                    | What it shows                                                                                                                    | What it cannot show |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Count the list in ordinary text of the language                        | How much of real text each tier covers; frequent words that are in a low tier or in none; the small words only this language has | Words that are only spoken: a filler is never written. Whether a rare word is needed for a situation |
| Match a spoken frequency list of a well-counted language, word by word | A complete list of the everyday meanings the tiers lack                                                                          | Words with no counterpart in that language. How common the matched word is in the language being learned |
| Ask a native speaker                                                   | Which of two or three words is the one people say; whether a word is said at all                                                 | A complete list of what is missing, from memory |
| A published frequency list of the language                             | The same as counting, ready-made                                                                                                 | Anything, until the list has been opened and looked at (section 4) |
| The course's own texts                                                 | Which words a reader of the course has met                                                                                       | Anything about frequency: the texts were written to use those words |

### Counting in ordinary text

`tools/wordfreq.py` counts the entries of the list, by root, in any plain text, and lists the commonest words that matched nothing. Its tables are Cebuano and are replaced for another language, as in `wordcheck.py`.

- **Several sources of different kinds, reported side by side and never merged.** For Cebuano: everyday sentences, news, and an old formal translation. Where all three agree, the finding does not depend on the kind of text.
- **Every source has words of its own.** News has the city and the victim, a Bible the king and the earth, and a small collection of sentences may have one contributor's fifty sentences about running. A word that is frequent in one source only belongs to that source.
- **The count is rough.** The affixes are stripped lightly, so some forms are missed and a few credited wrongly. Read a figure to about a tenth of its size, and look at the forms that were counted before trusting a row.

### Matching a spoken list of another language

Take the commonest words of speech in a language that has been counted well, and mark each: a core word of tier 1, 2 or 3; a word of the language that is in no tier; or no separate word in this language. For English the list is the New General Service List-Spoken (see `weaving/WORD-LISTS.md`); its 300 commonest words are about three quarters of everything said.

The result is a list of candidates, not a list of words to add:

- **It suggests too much** where the two languages divide meaning differently. English "get" and "take" are among the commonest words of speech; Cebuano *kuha* is rare in text.
- **It cannot see** what the other language has no word for. The Cebuano particles *man* and *mao* have no English counterpart and came out of the text count, not this one.
- **The matching is a judgment** about each word, and needs a speaker's eye as much as the list does.

### Asking a native speaker

- **Give a list to mark, not a question to answer from memory.** "Which of these do you say every day?" and "Is there a word here you would not say?" are easy. "Which common words are missing from these sixty?" is hard, and the answer is not complete. (The learner's observation, 2026-11-28.)
- **Ask for a choice among near-synonyms.** Which of three words for "maybe" is the one said.
- **Ask last,** with the candidates from the other two ways. The words those ways cannot settle are the spoken ones, which is what a speaker knows best.
- Ten minutes, on paper or a phone; `tools/sheet.py --form` prints such a list with boxes to tick and lines to write on. Note the place and roughly the age of the speaker, not the name.

## 4. Open a source before trusting it

Two of the sources named in advance for Cebuano were not what their labels said. The published word list for Cebuano turned out to be counted almost wholly from Wikipedia articles of one pattern, so its commonest words were "species" and "insect". A file of Cebuano subtitles held English and Turkish.

Three looks, a few minutes each, before any counting:

1. **Where the text comes from.** If the source lists its pages, count them by site.
2. **The thirty commonest words.** They should be the small words of the language.
3. **Twenty lines, read.**

A count of words is a fact and may be kept and published. The texts themselves belong to others: keep downloaded text out of the repository, and record where it was fetched and how it was prepared, so that the count can be repeated.

## 5. Reading the result

- **Two ways agree:** a strong case. A word frequent in text and common in the spoken list of the other language belongs higher.
- **One way only:** a question for a speaker.
- **Rare in text, and in the first tier for a situation:** keep it. That is the method, not a fault of the list.
- **Coverage:** compare the measured shares with the estimate the plan was built on, and say which kind of text they were measured on. Written text is not speech.

## 6. Changing a list that texts are built on

- **One file under one name.** Everything links to it. A version is marked with a git tag on the last commit before the change, and the file says at its top which version it is and where the reasons are.
- **What the learner has met is not taken out.** Changes go into the tiers not yet taught: which words they hold, and in what order they come.
- **A new version is a draft** in the language's `docs/vocabulary/draft/` until the learner approves it.
- **Then the rest follows:** the tables of `wordcheck.py` and `wordfreq.py`, the planned rows in the index of the texts, the pronunciation lexicon, and a dated line in the language's log.
- **Record what changed and why,** beside the check that led to it.

## 7. For a new language

1. Draft the list by category, and write down how (section 1).
2. Find two or three sources of ordinary text, and open each (section 4).
3. Put the list into the tables of `tools/wordfreq.py`, and count.
4. Match the spoken list of a well-counted language against the tiers.
5. Ask a speaker, with a list to mark.
6. Revise the list, and only then write the first text.
