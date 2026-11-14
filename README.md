# Learn a language with AI

Use an AI assistant to build the core of a language fast, and learn it by reading, and by listening once there is a voice for it. The assistant picks the words everyday speech is made of, writes short connected texts that use only those words, graded readers in the usual term, though here they are dialogues with the meaning of every word shown. You read the texts a few times each on a schedule, and the words stick because they keep coming back in context. The method is written up so that it can be repeated for another language; the first language it has been used for is Cebuano, called Bisaya by its speakers, the language of Cebu in the Philippines.

## How it works

1. **The core words.** The assistant builds a list of about 120 word roots in tiers, chosen by category (greetings, the small grammatical words, food, family, money, time) rather than by raw frequency, so that the situations that actually happen are covered. Our estimate is that this covers roughly two thirds of everyday conversation and more in simple exchanges such as greetings and shopping. That is an estimate, not a measurement.
2. **The texts.** The assistant writes short dialogues with recurring characters, using only the words introduced so far. The first texts use about sixty words; later ones add five to eight each. The numbers in the file names are the reading order.
3. **The layout.** Each text comes in three blocks: the language on its own, for reading cold; the language with a close English beside it, which follows the words rather than reading naturally, so the words stay visible; and a word-by-word block with the literal meaning under each word and short notes.
4. **The repetition.** Each text is read about six times on an expanding schedule (day 0 twice, then days 1, 3, 7, 14 and about 30). Because the words recur from text to text, each word is met ten to twenty times or more over the course, which is the range research associates with learning a word from reading.

The full instructions, with the prompts used, are in [METHOD.md](METHOD.md).

## Cebuano (Bisaya)

Free material for beginners. Everything for Cebuano is in [`cebuano/`](cebuano/):

- the word list in tiers: [vocabulary.md](cebuano/vocabulary.md)
- a short grammar sheet for listeners: [grammar-notes.md](cebuano/grammar-notes.md)
- the small words in their sets, one page to glance at: [word-sets.md](cebuano/word-sets.md)
- the texts, to be read in order: [001 Maayong buntag](cebuano/texts/001-maayong-buntag.md), [002 Asa si Mama?](cebuano/texts/002-asa-si-mama.md), [003 Hapon: sa trabaho ni Mama](cebuano/texts/003-hapon-sa-trabaho-ni-mama.md), [004 Gabii sa balay](cebuano/texts/004-gabii-sa-balay.md), [005 Buntag: asa si Jun?](cebuano/texts/005-buntag-asa-si-jun.md) (new, not yet read through by the learner)
- pronunciation files for software and AI voices, in [`cebuano/pronunciation/`](cebuano/pronunciation/): paste `NNN.paste.txt` into a chat voice that reads aloud to hear a text
- the listening side, the voices that could speak the texts and what has been tried: [audio.md](cebuano/audio.md)
- the plan: [PLAN.md](cebuano/PLAN.md); the dated log of the work: [LOG.md](cebuano/LOG.md)

To use it: skim Tier 1 of the word list once without memorising it, then read text 001, cold first, and follow the schedule above. The texts open in the browser on GitHub, so nothing needs to be installed. For paper, `tools/print.py` makes a one-page A4 version of a text, Cebuano left and English right with a word-for-word footnote; ready-made PDFs will be added once the layout is settled.

## Another language

[METHOD.md](METHOD.md) gives the method in six steps, the reasons, and the files and tools involved, in a language-neutral way; [CREATING-TEXTS.md](CREATING-TEXTS.md) is the step-by-step for one text, with the rules it follows. An AI assistant pointed at this repository can follow it directly ("read METHOD.md and set this up for French"); a person can follow it by hand. Expect hand work for a new language, especially a small one.

## Status

Early, and not yet verified. The Cebuano texts, word lists, grammar notes and pronunciation marks were written with AI assistance (Claude) and have not been checked by a native speaker. Meanings are probably right; stress marks and naturalness are where errors would hide, and the lexicon's `status` column says which entries most need checking. Corrections from Cebuano speakers are very welcome: open an issue or a pull request.

## Licence

The texts and documents in this repository (the method, the Cebuano material and the PDFs made from it) are under the [Creative Commons Attribution-ShareAlike 4.0 International](LICENSE) licence (CC BY-SA 4.0). You may use, change and share them, also commercially, as long as you credit the source and release what you make from them under the same licence. The scripts in [`tools/`](tools/) are under the [MIT licence](tools/LICENSE).

To credit: "Learn a language with AI" by Janne Nevalainen, github.com/jannenev/learn-a-language-with-ai, CC BY-SA 4.0.
