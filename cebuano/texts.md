# The texts: index, plan and record

One row per text, written or planned. For a written text the row records the scene, the words it brought in and the patterns it exercises; for a planned text it is the brief to write from. The row is filled before a text is written and dated when it is done, so the plan and the record are the same table. The word columns are checked against the texts: `python3 tools/wordcheck.py --new cebuano/texts/src/*.txt` lists the entries that first appear in each text, `--counts` the occurrences per entry. The characters and the stages are below; the words themselves are in `vocabulary.md`, and how a text is written in `CREATING-TEXTS.md` at the top level.

Everything here was written with AI assistance and has not been checked by a native speaker.

## Characters and stages

Recurring characters, so that the words recur naturally:

- **Ana** — young woman, lives in Cebu with her family.
- **Jun** — her younger brother. Ana calls him *Dong* (the everyday way to address a boy / young man).
- **Mama** — works at the market (introduced as "at work" in Tier 1, "merkado" arrives with Tier 2).
- Later: a friend of Ana, a shopkeeper, a jeepney ride, a visit to the beach.

| Stage | Texts | Words allowed | Length | Themes |
|---|---|---|---|---|
| A | 001–005 | Tier 1 only (65) | 25–30 lines, dialogue | morning at home, eating, where is who, going somewhere, simple wants |
| B | 006–013 | Tier 1 + Tier 2 (57 entries, 6–8 new per text) | 30–40 lines, dialogue | market and money, family, feelings (tired/hungry/sick), time of day, weather |
| C | 014– about 030 | + Tier 3 in batches of 8–10 per text (about 145 candidates) | 40–60 lines, dialogue and short narrative | friends, school/work, transport, the beach, longer stories |

The whole course is roughly thirty texts for about 260 roots: five at Tier 1, eight for Tier 2, fifteen or so for Tier 3. The texts get longer as the known base grows: with more known words a longer text still keeps unknown words rare, and each reading then gives more encounters per word. Stage C is where narrative (a paragraph of story between the lines of dialogue) can come in, because by then the *ni- / nag- / gi-* forms are familiar. The printed pocket page is part of the length question: 001 and 002 fit one A4 page with the word-for-word footnote, which proved convenient; a text that spills by a few lines wastes a sheet, while trimming a text to fit costs content. Text 003 as drafted (28 lines) fills page 1 and spills about five footnote rows; it is the trial case for whether a two-page pocket version works or the footnote layout should absorb it (noted 2026-11-07, not decided).

## Stage A: Tier 1 only (65 entries), texts 001–005

Goal: after 005, every Tier 1 entry at five occurrences or more (`--counts`). After 003 every entry has appeared and none is below two.

| Text | Status | Scene | Words | Patterns to exercise |
|---|---|---|---|---|
| 001 [Buntag sa balay](texts/001-buntag-sa-balay.md) | written 2026-09-20 | Morning at home. Ana and Jun; Mama already at work. | 40 Tier 1 entries first appear | na / pa; naa'y, naa ko'y; root + ta; mo- vs ni-; kaayo |
| 002 [Hapon: sa trabaho ni Mama](texts/002-hapon-sa-trabaho-ni-mama.md) | written 2026-10-06 | Afternoon at Mama's stall; many people. | 15 more first appear: kami, kamo, og, ni (of), dili, pila, ayaw, inom, dali, hulat, tubig, tawo, hapon / gabii, kana (as na), diri | plural you / we (mo, mi); ni and na double duty; dili na vs naa pa; gikaon; sige as goodbye |
| 003 Gabii sa balay | drafted 2026-11-07, to review | Evening at home. Someone at the door: Mama is back with food, one big and one small; no work tomorrow. | the last 10: siya, sila, ug, mga, kinsa, tulog, kasabot, ugma, dako, gamay; a second encounter for ni (of), dili, pila, ayaw, inom, kahibalo, tawo, diri, gabii, na = that | he / she / they; mga; ma- / na- on tulog; dili vs wala'y; og vs ug; the 'y family (naa'y, wala'y, kinsa'y, ba'y) |
| 004 | planned | Next morning, Mama at home. Jun is not in the house; Ana and Mama look for him; he was outside with water. | the look-alike sets side by side: dili / diri / didto, kini / kana, ni / na, wala / naa; asa, kinsa, siya; tubig, inom; pila; karon, unya; and unsa, salamat, kwarta, lami, which 003 did not use | where-is-who frames (asa si, naa sa, wala siya diri); kana vs kini; kumusta; hulat; ayaw |
| 005 | planned | Evening of that day, all three: what each will do tomorrow, and what each wants. The readiness check for Tier 2. | every entry below five cumulative occurrences after 004 (`--counts`), expected to include the full pronouns kami / kamo / kita, gyud, ba, og, pila, ayaw, kasabot, dako / gamay | plans with mo- / mag- / ma-; stacked particles (na ba, pa gyud, lang pud); all seven pronouns; the readiness rule: about 90 % on first read → Stage B |

## Stage B: Tier 2 (57 entries, 6–8 new per text), texts 006–013

The grouping follows the themes and the storyline. Before 006: decide whether *merkado* moves from Tier 3 to Tier 2 (the storyline assumes it does), and extend `tools/wordcheck.py` and the pronunciation lexicon with Tier 2.

| Text | Status | Scene | New entries | Patterns to exercise |
|---|---|---|---|---|
| 006 | planned | Morning. Ana's friend comes to the house and meets Jun and Mama. | man, amigo / amiga, igsoon, pamilya, anak, bata, anhi (7) | man in questions; kinsa siya? akong igsoon; bata pa siya; nianhi / moanhi |
| 007 | planned | To the market with Mama: buying food for the house. | palit, isda, kan-on, kape, mahal, barato, gikan (7), and merkado if promoted | mopalit ko og; mahal / barato kaayo; gikan sa |
| 008 | planned | Paying: prices and change. | numbers (Cebuano and Spanish-derived), bayad, hatag, kuha, tanan, pwede (6; the numbers count as one entry but are many forms) | pila tanan? baynte pesos; ihatag, kuhaa; pwede ba |
| 009 | planned | Hot afternoon. Everyone tired and hungry; Jun is not well. | kapoy, gutom, sakit, init, tugnaw, kay, pero (7) | ___ na ko (gutom na ko, kapoy na ko); kay = because; pero |
| 010 | planned | Evening talk: the fillers of real speech. | mao, kanang, murag, siguro, ambot, hala / ay, ngano, paminaw (8) | mao na / mao ba / mao gyud; kanang as a filler; murag; ngano man; paminaw! |
| 011 | planned | Looking for something lost in the house. | tan-aw, kita (see), kuan, buhat, ingon, unsaon, lagi (7) | tan-awa!; nakita nimo?; kuan as a placeholder; ingon niya; unsaon ni |
| 012 | planned | Days and times: when Mama works, when the friend comes back. | kanus-a, gahapon, ganina, kanunay, adlaw, oras, una (7) | kanus-a; gahapon / ganina / ugma; unsang orasa; kaon una |
| 013 | planned | Going out and coming back; a nice place, described without its name (the beach is Tier 3). | lakaw, balik, para, kung, basta, gani, sus, nindot (8) | molakaw na ko; balik ugma; para sa; kung gusto ka; nindot kaayo |

## Stage C: Tier 3 in batches, texts 014 onward

Not planned text by text yet. The Tier 3 backlog is grouped by topic in `vocabulary.md`; each Stage C text would promote one group of 8–10 (people, places, food, time, describers, particles, body and things, and the verbs in two or three batches) into full entries and use them, with the earlier words still carrying the text. About fifteen texts.
