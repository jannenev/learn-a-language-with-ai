# Woven stories

A woven story is a story in English with words of the language being learned put in place of their English ones: a few at first, more at each reading. You read the story as you would in English, and the new words come along with it.

It is extra reading beside the numbered texts.

## What is in this folder

| File or folder                             | What it is |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| [`WHAT-IS-WEAVING.md`](WHAT-IS-WEAVING.md) | What weaving is, what it is called elsewhere, what it can and cannot teach, and which kind is used here |
| [`HOW-TO-WEAVE.md`](HOW-TO-WEAVE.md)       | How to weave a text: choosing the words, the levels, the rules for swapping, the checks; for a person or an AI assistant |
| [`originals/`](originals/)                 | The English stories as they were before weaving, each with its source and copyright status |

What belongs to one language is with that language. For Cebuano:

| Folder                                            | What it is |
| ------------------------------------------------- | ----------------------------------------------------- |
| [`cebuano/texts-woven/`](../cebuano/texts-woven/) | The woven stories, to read |
| [`cebuano/weaving/`](../cebuano/weaving/)         | For making more: the swaps decided so far for Cebuano |

## How to read a woven story

1. Start with the version that has the fewest words woven in.
2. Look through the word table above the story once. Do not memorise it.
3. Read the story as you would in English. When a woven word comes up and you have forgotten it, the sentence usually tells you; if not, look back at the table.
4. Later, read the same story again in the next version. It keeps the words you have met and adds new ones, listed last in the table, nearest the story. Knowing the story makes the new words easier.

A woven story teaches words, the common ones that return in every text. It does not teach how a sentence is built in the language; the numbered texts do that. It is also not how anyone speaks: it is a device for reading.

## Adding a story to this repository

How the weaving itself is done is in [`HOW-TO-WEAVE.md`](HOW-TO-WEAVE.md). This is where the files go.

1. **The original.** Only a text that is free to use. Save it untouched in [`originals/`](originals/) as plain text, and add its entry to [`originals/README.md`](originals/README.md): source, date fetched, copyright status.
2. **The woven versions.** One file per version, named `<story>.<N>-words.md`, N being the number of words woven in. A new version goes in `<language>/texts-woven/draft/` and moves up to `<language>/texts-woven/` when the learner has read and accepted it. Add it to the list in that folder's `README.md`.
3. **The swaps.** What was decided for each word goes into `<language>/weaving/SWAPS.md`, so that the next story starts from it.

A woven story file has, in this order:

1. The title, woven like the text.
2. One line saying what the file is: how many words, which reading of the story it is, and a link to the version before or after.
3. **Status:** the original and its copyright status; for Cebuano, that the weaving was done with AI assistance and has not been checked by a native speaker; that it is a reading device, not a sample of speech.
4. **How to read it,** in two or three sentences.
5. The word tables: the words of the earlier versions first, the new words last, nearest the story. Three columns: the word, the English, the times it occurs in the story. The columns padded so that they line up in plain text.
6. One line with the count: how many of the story's words are woven.
7. The story.
8. **Notes on the weaving:** for each new word, what it stands for and which occurrences were left in English and why; any English word dropped; where each word first appears in the numbered texts.
