# Learning Cebuano / Bisaya (the language of Cebu) — Plan

## 1. Goal

**Primary:** understand everyday *spoken* Cebuano — greetings, small talk, shopping, family talk, directions.
**Secondary:** read simple written Cebuano (text messages, signs, short posts).
**Not a goal (for now):** speaking or writing fluently. Recognition first, production later.

### Which language exactly?

- The language spoken in Cebu (and Bohol, Negros Oriental, most of Mindanao: Davao, Cagayan de Oro, General Santos) is **Cebuano**.
- Locals almost never say "Cebuano" — they say **Bisaya** (or *Binisaya*). Same language.
- **"Visayan"** is a *family* name. It also covers Hiligaynon/Ilonggo (Iloilo, Bacolod) and Waray (Samar, Leyte), which are *different* languages, not mutually intelligible with Cebuano.
- **This project = Cebuano/Bisaya as spoken in and around Cebu.** Mindanao Bisaya is close, but mixes in more Tagalog; notes will flag differences when relevant.

## 2. Method

1. **Curated core vocabulary in tiers**, not a raw frequency ranking. A pure frequency list is dominated by particles and pronouns; a learner also needs *coverage* of the situations that actually occur (greetings, food, family, money, time). So: pick by category, keep the most frequent items of each category.
   - Tier 1 = 65 entries — survival core. Enough to follow a simple dialogue.
   - Tier 2 ≈ 58 entries — everyday. Total ≈ 123.
   - Tier 3 — a backlog of candidates, added in small batches when Tiers 1–2 feel solid.
   - See `vocabulary.md`.
2. **Minimal "listening grammar"**: the handful of patterns needed to *parse* speech — verb prefixes (mo-/ni-/nag-/gi-), the little markers (ang, sa, og, si, nga), particles (na, pa, lang, gyud, ba), negation (dili vs wala), and spoken contractions (naa'y, wala'y, unsa'y, di, wa, jud). No production drills. See `grammar-notes.md`.
3. **Graded texts** in `texts/`: short dialogues and mini-stories written using (almost) only the words introduced so far.
   - Heavy repetition of core words; new words in small doses (roughly 5–8 per text once Tier 2 starts).
   - Texts are connected: same characters, same setting, so vocabulary recurs naturally instead of each text pulling random words.
   - Each text tells you which tier(s) it uses and lists any word outside those tiers.
4. **Loop:** read → (listen, once an audio source exists) → self-check comprehension → add words → next text.

### How much real speech do the tiers cover? (estimate, 2026-10-06)

Rough estimates, not measurements: there is no public frequency list of *spoken* Cebuano. Reasoning is by analogy with spoken corpora in other languages (a few dozen function words carry about half of all speech) and from the fact that Cebuano conversation is even more dominated by particles, pronouns and markers. Counted by root: once *kaon* and the prefix table are known, *mokaon / nikaon / gikaon* all count as known.

| Vocabulary known | Shop, jeepney, greetings, "have you eaten" | Casual chat among family or friends |
|---|---|---|
| Tier 1 (65) | 65–75% of words | 45–55% |
| Tier 1+2 (≈ 123) | 80–85% | 60–70% |
| Tier 1+2+3 (≈ 260) | 85–90% | 72–80% |

What it means: listening research puts comfortable comprehension of unscripted speech at about 95% known words and rough gist at about 90%. So Tiers 1–2 give near-full understanding of transactional exchanges and the *topic* of family talk; Tier 3 makes family talk about food, plans, feelings and who-went-where followable with effort. Comfortable understanding of free conversation needs roughly 1,500–2,000 roots plus the affix system; gist with effort, about 800–1,000. The tiers are the start of that ramp.

Two things push the real figure up for a European learner in Cebu City: heavy mixing of English into casual speech (*busy kaayo ko*, *i-check nako*), and Spanish-derived numbers, times, days and months. Worth perhaps 5–10 extra points on the casual column.

The estimate also exposed a gap: eight very high-frequency conversational words (*mao, kuan, kanang, murag, siguro, basta, gani, sus*) were missing from all tiers. They are now Tier 2, section 2.9.

### How many readings does it take? (estimate, 2026-10-07)

**What the research says.** Studies of learning words incidentally from reading put the threshold at roughly 6 to 10 encounters for a first grip on the meaning and 20 or more for solid, lasting knowledge (Horst, Cobb and Meara 1998: 8; Saragi, Nation and Meister 1978: 10; Webb 2007: 10 or more; Waring and Takaki 2003: 20 or more, and most of the gain was lost after three months when the words were not met again). A 2019 meta-analysis of 26 studies (Uchihara, Webb and Yanagisawa) found a medium overall effect of repetition (r = .34) and a stronger one when learners re-read the same text within a day (r = .46). Reading while listening retained more than reading alone. Deliberate study of a word list with spaced retrieval is faster per word than meeting words in texts, but gives weaker knowledge of how the word behaves in sentences; the two complement each other.

**What the texts give.** `python3 tools/wordcheck.py --counts` shows occurrences per Tier 1 entry. After texts 001 and 002 (217 Tier 1 tokens in total):

| Occurrences in 001+002 | Entries | Examples |
|---|---|---|
| 10 or more | 3 | ako/ko, na, Mama |
| 5 to 9 | 15 | ikaw/ka, sa, ang, naa, kaayo, maayo, salamat, sige, adto, kaon, balay, unya |
| 2 to 4 | 27 | og, nga (as -ng), ba, pa, lang, gyud, pud, wala, unsa, asa, gusto, dali, pagkaon, daghan, lami, didto |
| 1 | 10 | dili, pila, ayaw, inom, kahibalo, tawo, diri, ni (of), kana (counted by eye; the script cannot separate it from *na*) |
| 0 | 10 | siya, sila, ug, mga, kinsa, tulog, kasabot, ugma, dako, gamay |

So a single read of both texts gets only three words past the threshold. Repetition has to come from re-reading and from later texts re-using the same words, which is the design.

**Reading schedule (decision).** Read each text about six times on an expanding schedule: day 0 (twice, the second time an hour or more later), day 1, day 3, day 7, day 14, and once more around day 30. Every pass starts with block 1 cold, which is retrieval practice, and only then block 2. Block 3 is for the first two passes. Once audio exists, the day 3 pass onward should be listening with the text in view, then listening alone. Six passes turn the table above into: words with 2 to 4 occurrences reach 12 to 24 encounters within a month, words with one occurrence reach 6 and depend on the next text to re-use them, and the zeros depend on text 003.

**Time.** A 27-line text takes about 2 minutes to read cold, 5 minutes with the English check, and 10 to 15 minutes the first time with block 3. Six passes are roughly 40 minutes per text spread over a month. Starting one new text every 3 to 4 days gives 10 to 15 minutes a day and brings Tier 1 (texts 001 to 005) to the threshold in 6 to 8 weeks, Tier 2 in a further 2 to 3 months.

**Where the variation is.** Between learners the spread is easily two- to threefold. Between words it is larger and predictable: Spanish and English loans (*kwarta, trabaho, pamilya, kape, pero, siguro*) stick in one to three encounters; the small particles (*na, pa, lang, man, gyud*) are recognised fast because they are everywhere, but their feel takes weeks of exposure; sets that look or sound alike (*dili / diri / didto / diha*, *kini / kana / kadto*, *nako / nimo / nato / namo / nila*, and the double-duty *ni* and *na*) take two to three times longer and need side-by-side contrast; hearing a word lags reading it, so expect to need the same number of encounters again in the audio versions before it is recognised in speech. Knowledge also decays: a word not met again within about two weeks slides back, which is why later texts keep re-using earlier words rather than introducing new ones.

**When a word counts as learned.** It is read cold without hesitation on two spaced passes, and then recognised in audio without the text. Until the audio side exists, use the first criterion only.

### Readiness rule

Move to the next tier when a *new* text at the current tier is understood on first read (later: first listen) at roughly 90%. If not, write more texts at the same tier rather than adding words.

## 3. Text format

The source format, the three-block layout and the rules for writing a text (close English, glosses, notes, small words one at a time, length) are language-neutral and live in `CREATING-TEXTS.md` at the top level, with the reasons and the alternatives considered. Cebuano specifics:

- Speakers Ana, Jun and Mama are shown by indentation in that order (`speakers:` header); a fourth speaker would call for `--names`.
- The small words for the chain rule are the pronouns, markers, particles and the short pointing words *ni* and *na*; the set, the affix list and the names are tables in `tools/wordcheck.py`. *Kaayo* is not counted as one.
- *Word check* coverage is against Tier 1 (65 entries); Tier 2 is to be added to the checker before Stage B.
- History: layout v1 (2026-09-20) had the English under each numbered line; v2, the three blocks, was adopted 2026-10-07 and both texts rewritten as sources (log). The hyphen rule for two-word counterparts was added 2026-11-07, the small-words rule 2026-11-08.

## 4. Repository layout

```
README.md                  what the project is and how to use it
METHOD.md                  the language-neutral instructions: how to build such a course with an AI
CREATING-TEXTS.md          how one text is made: steps, rules, and the reasons behind them
tools/render.py            renders <language>/texts/src/NNN.txt into the three-block layout
tools/wordcheck.py         counts which Tier 1 entries a text uses; flags words outside the list
tools/pron.py              generates the pronunciation files for a text
tools/print.py             makes one-page A4 PDFs of the texts (Cebuano left, English right) through Chrome
cebuano/PLAN.md            this file: goals, method, decisions, progress log for Cebuano
cebuano/texts.md           the texts: characters and stages, then one row per text, planned or written
cebuano/audio.md           the listening side: pronunciation data, voices surveyed, tests, what a native speaker said
cebuano/vocabulary.md      spelling conventions; Tier 1, Tier 2 (full entries) and Tier 3 backlog
cebuano/grammar-notes.md   listening grammar: what to recognise, not what to produce
cebuano/texts/src/         the texts as written: NNN.txt, one line per sentence with English and gloss
cebuano/texts/             the rendered texts, NNN-title.md (generated, do not edit by hand)
cebuano/pronunciation/     for software, not for reading: lexicon.tsv (stress and glottal marks per word),
                           rules-for-ai.txt, and per text NNN.paste.txt / NNN.ipa.txt / NNN.ssml.xml (see audio.md)
cebuano/print/             generated PDFs for printing; not committed until the layout is settled
```

## 5. Storyline for the texts

The characters, the stage table (texts, words allowed, length, themes) and the text-by-text plan and record are in `texts.md` (moved there 2026-11-08). Before Stage B: decide whether *merkado* moves from Tier 3 to Tier 2; the storyline assumes it does.

## 6. Conventions

Spelling, the spoken forms, verbs by root, vowels and the pronoun forms are at the top of `vocabulary.md` (moved there 2026-11-08).

## 6a. Pronunciation and audio (2026-10-07, 2026-11-08)

Pronunciation data lives in `cebuano/pronunciation/`, separate from the texts, so the reading files stay clean and the audio side can be handed to software: a lexicon marking stress and the word-final glottal stop, the two things Cebuano spelling does not show, and per-text files generated by `tools/pron.py` (decision 2026-10-07). The file formats, the voices surveyed on 2026-11-08, the verification loop with a native speaker, the licence note for published audio and the test record are in `cebuano/audio.md`. Found 2026-11-08 that the Azure SSML target of `pron.py` is dead: Azure accepts no phoneme tags for its Filipino voices.

## 7. Open questions

- **Audio.** Listening is the goal, so an audio source is needed. A Cebuano speaker recording the texts (italki/Preply tutor) would be best; the generated routes, surveyed 2026-11-08, are in `audio.md` with the order to try them. Decision pending those tests. The Azure SSML route is dead.
- **Conversation mode.** The texts are also scripts for spoken practice: a voice assistant on a phone that says a line in Cebuano and then in English, or translates on request, and lets the learner answer. Not possible with reliable Cebuano pronunciation yet; keep in mind as voice assistants improve. Noted 2026-11-07.
- **Verify the lexicon.** Entries marked `check` in `cebuano/pronunciation/lexicon.tsv` (e.g. dali, sige, palihug, kuan, the suffixed verb forms) need a native-speaker or dictionary check before the audio is trusted for stress.
- **Frequency cross-check.** The lists are curated from knowledge of the language, not derived from a corpus. Worth checking Tier 1–2 against a real frequency list (e.g. from OPUS subtitles or a Cebuano Wikipedia dump), keeping in mind that written corpora under-represent spoken particles. The coverage estimate in section 2 is a reasoned guess and would be the first thing such a check would correct.
- **Tier sizes.** 65 / ~50 are starting guesses. Prune Tier 1 if the first texts feel crowded.
- **Cebu vs Mindanao.** Decide whether to note Davao-style variants at all, or stick to Cebu only.
- **Text length and the printed page.** Whether a text that spills over one pocket page takes two pages or the footnote layout absorbs it; 003 is the trial case. The reasoning is with the stage table in `texts.md` and under Length in `CREATING-TEXTS.md`. Noted 2026-11-07.

## 8. Progress log

- **2026-09-20** — Project started. Wrote PLAN.md, vocabulary.md (Tier 1 = 65, Tier 2 ≈ 50, Tier 3 backlog), grammar-notes.md, and the first sample text `cebuano/texts/001-buntag-sa-balay.md` (Tier 1 only) to test the format.
- **2026-10-06** — Text 002 `cebuano/texts/002-hapon-sa-trabaho-ni-mama.md` (Tier 1 only, 27 lines, continues the same day; adds a Cebuano-only cold-read block as an experiment). Added `tools/wordcheck.py` and coverage counts to both texts: 001 uses 40/65 Tier 1 entries, 002 uses 51/65, together 55/65. Still unused after two texts: siya, sila, ug, mga, kinsa, tulog, kasabot, ugma, dako, gamay.
- **2026-10-06** — Estimated how much everyday speech each tier covers (section 2). Added eight high-frequency spoken words to Tier 2 as section 2.9: mao, kuan, kanang, murag, siguro, basta, gani, sus. Tier 2 is now ≈ 58, total ≈ 123. Repository put under git.
- **2026-10-07** — Layout v2 adopted (section 3): texts 001 and 002 rewritten as plain-text sources in `cebuano/texts/src/` and rendered with the new `tools/render.py`: three blocks, speaker by indentation, close English, literal glosses. *dali* corrected to "quick" (the phrase *Dali diri!* is "come here"); *ang* glossed as the(subj) and the *ang* vs *naa'y* point added to grammar-notes. `wordcheck.py` reads the sources.
- **2026-10-07** — Pronunciation files (section 6a): `cebuano/pronunciation/` with a lexicon of 226 words marked for stress and final glottal stop, the rule block for AI voices, and `tools/pron.py` generating paste / IPA / SSML files for texts 001 and 002.
- **2026-10-07** — Repetition estimate and reading schedule (section 2), with `wordcheck.py --counts` showing occurrences per entry. Surveyed outside readers and resources (section 10).
- **2026-11-07** — Preparing to publish: all Cebuano material moved into `cebuano/` so the repository can hold the method and tools at the top level and other languages beside it; `tools/pron.py` finds the language folder from the text's path.
- **2026-11-07** — Pocket print version, first tries. `tools/print.py` turns a text source into an A4 PDF, Cebuano left and close English right, to cover for a cold read. Lessons so far: grey text printed weak, so everything is solid black; Chrome stamps the time into the PDF, so the script pins it and an unchanged text regenerates byte-identical; a "Word for word" footnote lists only the sentences whose English does not use the gloss words (order ignored, English glue such as *is* and *the* ignored), as the words in order without repeating the Cebuano, in two columns; margins down to 10 mm and the dialogue at 10.5 pt so a 27-line text fits one page. Open: whether the footnote version replaces the plain one; how to show *Day* and *Dong* (gloss as to-a-girl / to-a-boy, translate, or a note); whether to cap text length for one page or let longer texts take a sheet. PDFs not committed until the version settles. A full variant (`--full`: all three blocks, notes, and the sections after the text) exists for the first reading; the pocket page for the later passes. Decision: the printable page is defined as HTML and CSS; Chrome is only the current printer (one small function), so another engine, Edge, Chromium, WeasyPrint, or printing the HTML from any browser, can replace it later without touching the layout.
- **2026-11-07** — Text plan: the texts are now planned a few ahead in `texts.md`, one row per text with its scene, the words it must bring in or introduce, and the patterns it exercises; the row becomes the record once the text is written, which is why it is its own file and not part of this plan. Stage B laid out as eight texts (006–013) covering the 57 Tier 2 entries, Stage C estimated at about fifteen more; text length to grow by stage (section 5). `tools/wordcheck.py --new` added: it lists the entries that first appear in each text (001: 40, 002: 15, 003: the last 10), and the checker now reads the gloss lines, so *ni* = of / this and *na* = that are counted from the gloss instead of guessed. The booklet intro page (`tools/print.py --all`) now carries a table of the texts with words used, new and known after each. Text 003 drafted as `cebuano/texts/src/003.txt`, to be reviewed before rendering.
- **2026-11-07** — Print footer overlap fixed. The footer is a fixed-position element, which Chrome repeats on every page but which reserves no room, so on the first full page (003 with the footnote) the last line printed under it. Chrome clips fixed elements to the page area, so the footer cannot be moved into the margin; instead the page content is wrapped in a table whose empty footer row Chrome repeats at every page break, keeping 14 pt clear at the foot of each page. The alternative, a CSS `@page` margin box, would fit two more footnote rows but cannot hold the clickable link.
- **2026-11-07** — Publishing files added at the top level: README.md (the idea, how it works, the Cebuano material, status), METHOD.md (the method in six steps, the reasons, files and tools), and AGENTS.md with CLAUDE.md importing it, telling an assistant how to help a learner with the existing material, extend it, or do the same for another language.
- **2026-11-08** — Audio sources surveyed, written up as `cebuano/audio.md`, the record of the listening side beside `texts.md`; PLAN.md keeps the decision (section 6a) and the pointers. The Azure SSML target of `pron.py` turned out dead: Azure's Filipino voices accept no phoneme tags. Two engines take our IPA directly, ElevenLabs v4 (Cebuano listed, IPA inline in slashes, free tier enough for tests) and the open-source IMS Toucan (Cebuano in its list, zero-shot, quality unknown); Google Gemini-TTS has Cebuano in preview without pronunciation control; Meta MMS stays the free local baseline, its CC-BY-NC licence allowing the audio in this repository with attribution. Verification idea: a native speaker listens to generated clips and marks the wrong words, a smaller ask than recording. Nothing generated yet.
- **2026-11-08** — Reading 002, the learner found the chains of small words hard (*pa ko og*, *na mo sa*, *ba ka sa*: three in a row, new or nearly new, the English not showing which is which). Rule "small words one at a time" written into the new top-level `CREATING-TEXTS.md`, which now holds how a text is made (steps, rules, the observations behind them, the layout alternatives considered); `tools/wordcheck.py --chains` lists such lines with each member's exposure. This file slimmed to goal, method parameters, open questions, log and next steps: text format to `CREATING-TEXTS.md`, audio to `audio.md`, characters and stages to `texts.md`, spelling conventions to `vocabulary.md`. 002 to be revised to the rule; the 003 draft to be reviewed against it.

## 9. Next steps

1. Verify the entries marked `check` in `cebuano/pronunciation/lexicon.tsv` with a native speaker or Wolff's dictionary (dali, sige, palihug, kuan, the suffixed verb forms).
2. Revise 002 to the small-words rule in `CREATING-TEXTS.md` (seven lines, see `wordcheck.py --chains`) and re-render it; decide the "New in this text" line before block 1. Then review the draft of text 003 (`cebuano/texts/src/003.txt`) against the same rule, render it, generate its pronunciation files and PDF, and write 004 and 005 from their rows in `texts.md`. After 005, check with `wordcheck.py --counts` that no Tier 1 entry is below five occurrences.
3. Decide the audio source: run the tests in `audio.md`, section 4, on text 001 (ElevenLabs v4 plain and with IPA, Meta MMS locally, Toucan if needed), send the clips to a native speaker, then retarget `tools/pron.py` from the Azure SSML to the chosen engine's input and add a `tools/speak.py` that writes `cebuano/audio/NNN.mp3`.
4. Follow the reading schedule in section 2 for 001 and 002 while 003 to 005 are written.
5. Before Stage B: decide whether *merkado* moves from Tier 3 to Tier 2 (the storyline in `texts.md` assumes it does), and extend `tools/wordcheck.py` and the lexicon with Tier 2.

## 10. Outside resources (checked 2026-10-07)

Names to search under, because each turns up different things: *Bisaya* (what speakers say), *Binisaya* / *Sinugbuanong Binisaya* (the school name, used by DepEd materials), *Cebuano* (academic and English), *Visayan* (the family; also covers Hiligaynon and Waray).

**Graded readers for adults:** essentially none in the usual sense. Closest: a 20-story A1–A2 digital collection sold on Etsy (quality unknown); *Immersive Reader: Cebuano Visayan* (Borello, 25 lessons); Judy Diel Li's bilingual children's series with pronunciation guides.

**Free leveled children's books (the real readers):** Bloom Library's Cebuano section (bloomlibrary.org, language ceb); Let's Read by the Asia Foundation (app and web, Philippine languages including Cebuano); StoryWeaver by Pratham (Cebuano and Sinugbuanong Binisaya); the DepEd *Pagbasa* Grade 1 Cebuano reading workbook (free PDF). Expect the written narrative register and concrete nouns (animals, colours, nature), with the spoken particles mostly absent.

**Textbooks and reference:** Bunye and Yap, *Cebuano for Beginners* (University of Hawaii Press 1971, open access); Wolff, *Beginning Cebuano* (Yale) and Wolff's dictionary (online at SEAlang); Raisanen, *A Handbook of Cebuano Visayan*; binisaya.com dictionary.

**How to use them here:** paste the text of a candidate book into a file and run `tools/wordcheck.py` on it to see how much of it is Tier 1–2 before spending time on it. Prefer adapting an outside story into the tiers over reading it raw.
