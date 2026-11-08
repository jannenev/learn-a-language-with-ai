# The method: learn the core of a language from texts built on its core words

How the Cebuano material in this repository was made, so that the same can be done for another language, by hand or by an AI assistant that has read this file.

## In short

1. **Decide what the course is for.** For Cebuano: understanding everyday speech, in the Cebu variety, with English as the pivot language. The material then serves everyone with that goal.
2. **Pick the core words.** About 60 that everyday speech is made of, chosen by category (greetings, the small grammatical words, food, family, money, time), then about 50 more, then a backlog. Add the fillers and exclamations that word lists tend to miss.
3. **Write short dialogues using only those words.** Same characters, same setting, so the words keep coming back. Later texts add five to eight new words each. The number in the file name is the reading order. Plan the texts a few ahead in an index of the texts, one row per text: the scene, the words it must bring in or introduce, and the patterns it exercises. The row is the brief while the text is unwritten and the record afterwards; a text written to such a row drifts less between writers.
4. **Show every word's meaning.** Beside each line, an English that follows the words rather than reading naturally; under each word, its literal meaning; idioms explained in a note, never substituted.
5. **Lay it out so the text can be read alone first.** The target language on its own, then with the English beside it, then word by word with notes.
6. **Read each text about six times over a month**, cold first, then check. Add audio when you can. Have a native speaker check everything before trusting it, and say it is unchecked until then.

Reading is the channel available today, not a constraint. The same texts are scripts for listening, and for spoken practice once a voice assistant can hold a conversation in the language: it says a line in the language and then in English, or translates on request, and the learner answers.

## Why

**The words.** A raw frequency list is dominated by grammatical words; choosing by category covers the situations that actually happen. Counting by root, about 120 words cover roughly two thirds of everyday conversation and more in simple exchanges such as greetings and shopping, by our estimate. The small words (particles, markers, fillers) are most of what is heard, so they go in even though they are hard to gloss.

**The texts.** Comprehension needs a high share of known words, so the texts are restricted to the words introduced so far. Recurring characters make the words recur naturally. Counting how often each core word has appeared tells you which words the next text must use; after the first two Cebuano texts only three words had appeared ten or more times.

**The translation.** A natural translation hides the words; the point is to learn them. Cebuano *Dali diri!* is shown as "Quick, here!", not "Come here!", and *dali* is glossed as "quick", with "this is how you say come here" in the note. The first draft got that backwards and the learner caught it; it is the easiest mistake to make.

**The layout.** Interleaving a translation under every line pulls the eye off the target language, and markup in front of every line is an obstacle. Reading the target text alone first is retrieval practice, which beats re-reading.

**The repetition.** Research on learning words from reading puts the threshold at roughly ten spaced encounters for a first grip and twenty or more for solid knowledge, with decay if a word is not met again within a couple of weeks. Six readings per text on expanding intervals (day 0 twice, then days 1, 3, 7, 14 and about 30), with the words recurring across texts, gets each word to ten to twenty encounters or more. A word counts as learned when it is read cold without hesitation on two spaced passes and, with audio, recognised in speech. The next tier starts when a new text at the current tier is understood on first read at about ninety percent.

**The checking.** An AI assistant's output in a small language is a draft. Meanings are usually right; stress, idiom and naturalness are where errors hide.

Of all this, the research-backed parts are the spacing, reading cold before checking, and keeping unknown words rare. The rest is what worked for one learner and one language, and plain choices such as tier sizes and file formats.

## Files and tools

A language lives in its own folder, like `cebuano/`:

```
PLAN.md             goal, decisions, estimates, open questions, dated log
vocabulary.md       the tiers, with spoken forms and one example per entry
grammar-notes.md    the few patterns a listener needs to recognise: markers, verb forms, particles, contractions, sentence frames
texts.md            index of the texts: one row per text, planned or written, with scene, words brought in, patterns
texts/src/NNN.txt   each text as written: speaker, sentence, close English, a gloss line, notes
texts/NNN-title.md  the same text rendered into the three blocks; generated, not edited
audio.md            the listening side: pronunciation data, the voices tried, and what a native speaker said of them
pronunciation/      optional: per-word stress marks, a rule block for AI voices, generated files per text
print/              one-page A4 PDFs of the texts, target language left and English right; generated
```

How one text is made, step by step, with the rules it follows and where they came from, is `CREATING-TEXTS.md` at the top level.

The scripts in `tools/` document their own formats and usage; run any of them without arguments to see.

- `render.py` turns a text source into the three-block layout. Language-neutral.
- `wordcheck.py` reports which core words a text uses, which are still unused, anything outside the list, and occurrences per word. Its word table and affix list are Cebuano and must be replaced for another language.
- `pron.py` generates the pronunciation files. Its spelling-to-sound rules are Cebuano; a language with good text-to-speech may not need it.
- `print.py` makes the one-page PDFs for paper, through Chrome. Language-neutral.

What is specific to Cebuano or to the learner is marked as such in the files: the comparisons to Finnish in the grammar notes, for instance, are asides, not part of the method. The dated log in `cebuano/PLAN.md` records each decision, including the ones that were reversed, and is the most honest account of how this was built.
