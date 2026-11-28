# For AI assistants working with this repository

This repository holds a method for learning the core of a language from short texts built on its most common words (`METHOD.md`; reading is the channel available today, the same texts serve listening and spoken practice) and ready-made material for Cebuano (Bisaya) in `cebuano/`. The Cebuano material was written with AI assistance and has not been checked by a native speaker; say so when it matters, and keep that status visible in anything you produce from it.

## Helping someone learn Cebuano with what is here

- Start them on `cebuano/texts/001-maayong-buntag.md`, then 002 and onward in number order. Each text has three blocks: the Cebuano alone, to be read cold first; the Cebuano with a close English beside it, to check; the word-by-word block with notes, to look things up. The close English follows the Cebuano words on purpose and is not natural English.
- Follow the reading schedule in `cebuano/PLAN.md`, section 2: each text about six times on expanding intervals (day 0 twice, then days 1, 3, 7, 14 and about 30), always cold first. Do not have the learner memorise the vocabulary list; the texts do that work. Move to the next tier when a new text is understood on first read at about ninety percent.
- Answer questions about words from `cebuano/vocabulary.md`, about patterns from `cebuano/grammar-notes.md`, about the sets the small words form (persons, pointing words, verb shapes, particles, markers) from `cebuano/word-sets.md`, and about pronunciation from `cebuano/pronunciation/lexicon.tsv`, mentioning when an entry is marked `check`. For reading aloud, `cebuano/pronunciation/NNN.paste.txt` holds the rule block and the stress-marked text for a voice. For paper, `python3 tools/print.py --glosses cebuano/texts/src/NNN.txt` makes a one-page A4 PDF of a text, Cebuano left and English right with a word-for-word footnote, and `python3 tools/sheet.py --two cebuano/word-sets.md` the one-page sheet (both need Chrome).

## Extending the Cebuano material

- Follow `CREATING-TEXTS.md`: start from the text's row in `cebuano/texts.md` (write the row first if it is missing), write `cebuano/texts/src/NNN.txt` to the rules there, run the checks, show the source before rendering, then render, generate the pronunciation files and the PDF, date the row and log the work with the date in `cebuano/LOG.md`.
- To check or change the word list (`cebuano/vocabulary.md`): follow `docs/vocabulary/`, and first read what was checked and decided for Cebuano in `cebuano/docs/vocabulary/`. A new version of the list stays a draft there until the learner approves it.

## Doing the same for another language

- Follow `METHOD.md` and produce the same kinds of files as in `cebuano/`, in a folder named after the language. The scripts in `tools/` document their own formats; `wordcheck.py` and `pron.py` contain Cebuano specifics to replace.
- For the core words, follow `docs/vocabulary/`: how to choose them, and how to check the list before texts are built on it.
