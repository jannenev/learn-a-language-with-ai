# How to weave a story

Given an English text and a list of words in the language being learned, how to weave the one into the other well. For a person or an AI assistant; the same for a story meant for this repository and for a book woven for one's own reading. The rules come from weaving the first tale for Cebuano, and are to be corrected as more are made; the examples are Cebuano.

What weaving is and why it is done this way: [`WHAT-IS-WEAVING.md`](WHAT-IS-WEAVING.md). Where the files of a story go in this repository: [`README.md`](README.md).

## The text

Any English text can be woven. Prefer a story with dialogue and everyday content: the common words of a language come up most there.

- **For publishing,** in this repository or anywhere else, the text must be free to use: out of copyright (the author and, for a translation, the translator dead for more than seventy years) or under a free licence.
- **For one's own reading,** in many countries, most of the EU among them, a book one has lawfully obtained may be edited for one's own use, and weaving is such an edit. The law differs by country, so check your own. The steps are the same; the result stays with the reader. More in "Weaving one's own book" in [`WHAT-IS-WEAVING.md`](WHAT-IS-WEAVING.md).

## Steps

1. **Count the words of the text** and list the most frequent ones.
2. **Match them to the language's core list.** For each frequent English word: is there a core word for it, and can it be swapped without changing the sentence? If the language has a file of swaps already decided (for Cebuano, [`cebuano/weaving/SWAPS.md`](../cebuano/weaving/SWAPS.md)), start from it.
3. **Choose the words for the level** by how often they occur in the text, among the core words. Not by what the text is about: a word that appears once or twice teaches little, and a story word that is not core (wolf) is not woven at all.
4. **Swap, one occurrence at a time,** by the rules below. Look at every occurrence in its sentence; never replace a word everywhere without looking.
5. **Check** (see Checks).
6. **Write down what was decided:** for each word, what it stands for and which occurrences were left in English and why. The reader needs it as notes under the story; the next weaver needs it in the language's swaps file.

## Levels

A text is woven several times, each version keeping all the words of the one before and adding more. The reader reads the versions in order, the same story again each time.

- **The first version is the hardest for the reader.** Keep it to about a dozen words, the commonest plain swaps: and, he and she, then, they, not, a few describing words and things.
- **Each later version can add about nine or ten,** and can take harder kinds of swap, because the story and the earlier words are familiar by then: first the remaining plain ones (but, all, I, you, we), then words that hide a distinction English makes (his and her as one word), then words with forms of their own (go, went), then the general place word.
- **About a quarter of the words woven** was still easy reading on a fourth pass. Where the limit lies is not known.

## Rules for swapping

1. **Swap only where the word is right in that sense.** If the language uses another word for this sense, leave the English. "You will know him by his voice" keeps *know*: knowing a person is not *kabalo*.
2. **Leave set phrases alone.** "At once", "with all speed", "one after another", "on your guard", "dear little mother".
3. **Keep the English sentence as it is.** Do not reorder. A word that would have to move (Cebuano *kaayo*, very, comes after its word) waits for a later level or is left out.
4. **One English word, two words in the language: choose each time, or wait.** "Not" is *dili* where something is refused or denied and *wala* where something is absent or did not happen; "we" is *kami* or *kita* by whether the listener is counted in; "you" is *ikaw* or *kamo* by number. Bring in one of a pair first and leave the other's places in English until its level.
5. **One word in the language, several in English: swap all that fit.** *Siya* for he and she, *iyang* for his and her, *sa* for in, into, at and to. The reader loses a distinction English makes and has to take it from the sentence; say so in the notes.
6. **Forms.** Use the form the language would use: *niadto* for went, *moadto* for a going not yet done. A word that does not change for time (*gusto*, *kabalo*) stands for all the English forms. A bare root after "to" (*to inom*) is acceptable at an early level.
7. **An English helper word with no counterpart may be dropped when it stands between two woven words or directly beside one,** and only then: "did not find" became *wala find*, "wanted to go" *gusto moadto*, "into the forest" *sa forest*. Count these and report them in the notes. Nothing else of the original is removed, and nothing is added.
8. **Capitals** as in English: a woven word takes a capital only at the start of a sentence. English "I" becomes *ako*, not *Ako*, inside a sentence.

## Checks

- The woven text has the same number of words as the original, less the helper words dropped under rule 7.
- Every swap has been seen in its sentence.
- The count given for each word matches the text.
- Every occurrence left in English on purpose is accounted for, by kind.
- No word outside the level's list has been woven in.

There is no script for these; they have been done with short one-off scripts.
