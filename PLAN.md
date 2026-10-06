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

### Readiness rule

Move to the next tier when a *new* text at the current tier is understood on first read (later: first listen) at roughly 90%. If not, write more texts at the same tier rather than adding words.

## 3. Text format (decision v1 — revisit after texts 001–003)

Each file `texts/NNN-title.md` has:

1. **Header** — title, setting, which tiers are allowed, new words introduced (if any).
2. **Body** — numbered lines. Each line:
   - Cebuano first, in bold.
   - English translation below it, natural rather than literal.
   - A gloss line (`word = meaning · word = meaning`) that pins each Cebuano word to its meaning. First texts: full gloss on every line. Later texts: gloss only new or tricky words.
3. **Listen for** — the 2–4 grammar patterns the text exercises.
4. **Word check** — list of any words outside the allowed tiers (target: zero, except proper names and obvious loanwords), plus a **coverage count**: how many of the tier's entries this text uses, and the cumulative count over all texts so far. Run `python3 tools/wordcheck.py texts/001-*.md texts/002-*.md` to get it.
5. **Cold read** (from text 002 on, experimental) — the same dialogue as plain Cebuano lines at the end, so you can test yourself without the English in view.

Why this format: the eye lands on Cebuano first; the gloss answers "which word is which"; the natural English keeps the meaning honest even where word order differs.

Alternatives to consider later: (a) Cebuano-only version of each text for a "cold read" before looking at the English; (b) a story in prose rather than dialogue; (c) audio per line.

## 4. Repository layout

```
PLAN.md            this file: goals, method, decisions, progress log
vocabulary.md      Tier 1, Tier 2 (full entries) and Tier 3 backlog
grammar-notes.md   listening grammar: what to recognise, not what to produce
texts/             graded texts, numbered 001, 002, ...
tools/wordcheck.py counts which Tier 1 entries a text uses; flags words outside the list
```

## 5. Storyline for the texts

Recurring characters so words recur naturally:

- **Ana** — young woman, lives in Cebu with her family.
- **Jun** — her younger brother. Ana calls him *Dong* (the everyday way to address a boy / young man).
- **Mama** — works at the market (introduced as "at work" in Tier 1, "merkado" arrives with Tier 2).
- Later: a friend of Ana, a shopkeeper, a jeepney ride, a visit to the beach.

Planned sequence:

| Stage | Texts | Words allowed | Themes |
|---|---|---|---|
| A | 001–005 | Tier 1 only | morning at home, eating, where is who, going somewhere, simple wants |
| B | 006–012 | Tier 1 + Tier 2 (added 5–8 per text) | market and money, family, feelings (tired/hungry/sick), time of day, weather |
| C | 013+ | + Tier 3 batches | friends, school/work, transport, longer stories |

## 6. Conventions

- **Spelling:** standard modern Cebuano orthography, with the spoken/texting form given alongside where it differs: *gyud* (also *jud*), *dili* / *di*, *wala* / *wa*, *kini* / *ni*, *kana* / *na*, *kahibalo* / *kabalo*.
- **Hyphen = glottal stop** (a small catch in the throat): *bag-o* (new), *kan-on* (rice), *tan-aw* (look), *kanus-a* (when).
- **Verbs are listed by root**, with the forms you will actually hear: *kaon* → *mokaon* (will eat), *nikaon* (ate), *nagkaon* (is eating), *gikaon* (was eaten).
- **Vowels** are pure: a, e, i, o, u as in Spanish or Finnish. In speech *o/u* and *e/i* swap freely (*babaye* ~ *babayi*, *tulo* ~ *tulu*).
- **Pronouns**: the short forms (*ko, ka, ta, mi, mo*) are what you hear; full forms (*ako, ikaw, kita, kami, kamo*) appear at the start of a sentence or for emphasis.

## 7. Open questions

- **Audio.** Listening is the goal, so an audio source is needed: a Cebuano speaker recording the texts, YouTube/vlogs in Bisaya, or text-to-speech. Cebuano TTS quality varies a lot; test a couple (e.g. Meta MMS has a Cebuano voice) before relying on one.
- **Frequency cross-check.** The lists are curated from knowledge of the language, not derived from a corpus. Worth checking Tier 1–2 against a real frequency list (e.g. from OPUS subtitles or a Cebuano Wikipedia dump), keeping in mind that written corpora under-represent spoken particles. The coverage estimate in section 2 is a reasoned guess and would be the first thing such a check would correct.
- **Tier sizes.** 65 / ~50 are starting guesses. Prune Tier 1 if the first texts feel crowded.
- **Cebu vs Mindanao.** Decide whether to note Davao-style variants at all, or stick to Cebu only.

## 8. Progress log

- **2026-09-20** — Project started. Wrote PLAN.md, vocabulary.md (Tier 1 = 65, Tier 2 ≈ 50, Tier 3 backlog), grammar-notes.md, and the first sample text `texts/001-buntag-sa-balay.md` (Tier 1 only) to test the format.
- **2026-10-06** — Text 002 `texts/002-hapon-sa-trabaho-ni-mama.md` (Tier 1 only, 27 lines, continues the same day; adds a Cebuano-only cold-read block as an experiment). Added `tools/wordcheck.py` and coverage counts to both texts: 001 uses 40/65 Tier 1 entries, 002 uses 51/65, together 55/65. Still unused after two texts: siya, sila, ug, mga, kinsa, tulog, kasabot, ugma, dako, gamay.
- **2026-10-06** — Estimated how much everyday speech each tier covers (section 2). Added eight high-frequency spoken words to Tier 2 as section 2.9: mao, kuan, kanang, murag, siguro, basta, gani, sus. Tier 2 is now ≈ 58, total ≈ 123. Repository put under git.

## 9. Next steps

1. Review Tier 1: cut anything that feels unnecessary, add anything missing. Decide whether the cold-read block in 002 is worth keeping (and adding to 001).
2. Write texts 003–005 (Tier 1 only), same characters. Text 003 should bring in the ten entries still unused: siya, sila, ug, mga, kinsa, tulog, kasabot, ugma, dako, gamay — a natural fit is the evening at home: Mama comes back, who was there, going to sleep, plans for tomorrow.
3. Decide on an audio source and try it on text 001.
4. When Tier 2 texts start, extend `tools/wordcheck.py` with a Tier 2 table.
5. Start Stage B when texts 001–005 are understood on first read.
