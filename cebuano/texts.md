# The texts: index, plan and record

One row per text, written or planned. For a written text the row records the scene, the words it brought in and the patterns it exercises; for a planned text it is the brief to write from. The row is filled before a text is written and dated when it is done, so the plan and the record are the same table. The word columns are checked against the texts: `python3 tools/wordcheck.py --new cebuano/texts/src/*.txt` lists the entries that first appear in each text, `--counts` the occurrences per entry. The characters and the stages are below; the words themselves are in `vocabulary.md`, and how a text is written in `CREATING-TEXTS.md` at the top level.

Everything here was written with AI assistance and has not been checked by a native speaker.

## Characters and stages

Recurring characters, so that the words recur naturally:

- **Ana** — young woman, lives in Cebu with her family.
- **Jun** — her younger brother. Ana calls him *Dong* (the everyday way to address a boy / young man).
- **Mama** — works at the market: her stall is a small table of fish under a tin roof ("at work" in 002; *merkado*, the one Tier 2 word allowed in Stage A, names the place from 003 on).
- Later: a friend of Ana, a shopkeeper, a jeepney ride, a visit to the beach.

| Stage | Texts | Words allowed | Length | Themes |
|---|---|---|---|---|
| A | 001–006 | Tier 1 only (65) | 14–16 lines for the first two, then 25–30, dialogue | morning at home, eating, where is who, going somewhere, simple wants |
| B | 007–014 | Tier 1 + Tier 2 (57 entries, 6–8 new per text) | 30–40 lines, dialogue | market and money, family, feelings (tired/hungry/sick), time of day, weather |
| C | 015– about 031 | + Tier 3 in batches of 8–10 per text (about 145 candidates) | 40–60 lines, dialogue and short narrative | friends, school/work, transport, the beach, longer stories |

The whole course is roughly thirty texts for about 260 roots: six at Tier 1, eight for Tier 2, fifteen or so for Tier 3. The texts get longer as the known base grows: with more known words a longer text still keeps unknown words rare, and each reading then gives more encounters per word. Stage C is where narrative (a paragraph of story between the lines of dialogue) can come in, because by then the *ni- / nag- / gi-* forms are familiar. The printed pocket page is part of the length question: the texts up to 003 fit one A4 page with the word-for-word footnote, which proved convenient; a text that spills by a few lines wastes a sheet, while trimming a text to fit costs content. Text 004 as drafted (28 lines) spilled about five footnote rows onto a second page; revised to 25 lines with six scene lines it fit once two long lines were shortened (2026-11-11), so the working limit is about 25 to 27 lines of dialogue with the scene lines and the footnote. Whether a longer text should take two pages or be trimmed is still open; no text has needed it yet.

## Stage A: Tier 1 only (65 entries), texts 001–006

Goal: after 006, every Tier 1 entry at five occurrences or more (`--counts`). After 005 every entry has appeared (2026-11-11: sila, ug, kasabot and *na* = that moved from 004 to 005, with the forms nag- / mag-, nimo, kinsa'y, ba'y and wala + ni- to 005 and 006, so that 004 brings seven words and one new verb pattern).

Renumbered on 2026-11-14: the first text, with 40 new words, was split into 001 and 002, about twenty each, and the texts after it moved up by one. This file uses today's numbers throughout, also where it gives an earlier date.

| Text | Status | Scene | Words | Patterns to exercise |
|---|---|---|---|---|
| 001 [Maayong buntag](texts/001-maayong-buntag.md) | written 2026-11-14, from the first half of the first text (2026-09-20) | Morning at home. Ana at the table with a plate of rice and fish; Jun comes in, just up. They greet and eat. | 21 Tier 1 entries first appear | the set phrases of greeting (Maayong buntag; Kumusta ka? Maayo, salamat. Ikaw? Maayo pud; Nikaon na ka? Wala pa); naa'y; ba; kaayo; gusto ka / gusto ko; root + ta; gusto + mo- verb |
| 002 [Asa si Mama?](texts/002-asa-si-mama.md) | written 2026-11-14, from the second half of the first text | The same morning, still at the table: a small bowl with a lid that neither can name. Mama is at work; they will go there later. | 19 more first appear: Dong, ni (this), unsa, kabalo, lang, gyud, daghan, ang, si, Mama, asa, sa, balay, trabaho, adto, karon, unya, didto, kwarta | unsa ni / wala ko kabalo; daghan ang; si + name; asa si, naa sa, wala sa; adto ta and moadto ko; karon / unya as one-word answers; naa ko'y |
| 003 [Hapon: sa trabaho ni Mama](texts/003-hapon-sa-trabaho-ni-mama.md) | written 2026-10-06, revised 2026-11-08 and 2026-11-11 | Afternoon at Mama's stall in the market: a table of fish under a tin roof, many people. | 14 more first appear: kami, kamo, og, ni (of), dili, pila, ayaw, inom, dali, hulat, tubig, tawo, hapon / gabii, diri; and merkado from Tier 2, once | plural you / we (mo, mi); ni = this and ni = of in consecutive lines (16–17); dili na vs naa pa; one na with three English faces in one line (18); the second-position slot (adto na ta, gusto ba mo); sige as goodbye; small words at most two in a row |
| 004 [Gabii sa balay](texts/004-gabii-sa-balay.md) | drafted 2026-11-07, revised 2026-11-11, to review | Evening at home: the lamp on, a knock at the door, Mama back with two bundles of food, one big and one small; no work tomorrow. | 7 first appear: siya, mga, kinsa, tulog, ugma, dako, gamay; second encounters for ni (this), dili, pila, ayaw, inom, kahibalo, tawo, diri, gabii; new shapes: matulog / natulog, wala'y, akoa, ra | he / she; mga; the three shapes of tulog (bare root, ma-, na-); dili vs wala'y; the 'y family (naa'y, wala'y, ko'y); lang vs ra; the describing word first (dako ni, gamay ni); one new thing per sentence, no three-word chains |
| 005 | planned | Next morning, Mama at home. Jun is not in the house; Ana and Mama look for him; he was outside with water. | the last four Tier 1 entries, moved here from 004 on 2026-11-11: sila, ug, kasabot, na = that (kana); the look-alike sets side by side: dili / diri / didto, kini / kana, ni / na, wala / naa; asa, kinsa, siya; tubig, inom; pila; karon, unya; and unsa, salamat, kwarta, lami, which 004 did not use | where-is-who frames (asa si, naa sa, wala siya diri); kana vs kini, ni = this vs na = that in one line; kinsa'y and ba'y; kumusta; hulat; ayaw |
| 006 | planned | Evening of that day, all three: what each will do tomorrow, and what each wants. The readiness check for Tier 2. | every entry below five cumulative occurrences after 005 (`--counts`), expected to include the full pronouns kami / kamo / kita, gyud, ba, og, pila, ayaw, kasabot, dako / gamay | plans with mo- / mag- / ma-; nag- (naghulat mi), nimo and wala + ni- verb (wala pa ko niinom), moved here from 004 on 2026-11-11; stacked particles (na ba, pa gyud, lang pud); all seven pronouns; akong and the gi- glimpse (ang akong gikaon = what I ate), moved here from 003 on 2026-11-11; the readiness rule: about 90 % on first read → Stage B |

## Stage B: Tier 2 (57 entries, 6–8 new per text), texts 007–014

The grouping follows the themes and the storyline. *merkado* moved from Tier 3 to Tier 2 on 2026-11-11 and is used once in 003 to name Mama's place; before 007, extend `tools/wordcheck.py` and the pronunciation lexicon with Tier 2.

| Text | Status | Scene | New entries | Patterns to exercise |
|---|---|---|---|---|
| 007 | planned | Morning. Ana's friend comes to the house and meets Jun and Mama. | man, amigo / amiga, igsoon, pamilya, anak, bata, anhi (7) | man in questions; kinsa siya? akong igsoon; bata pa siya; nianhi / moanhi |
| 008 | planned | To the market with Mama: buying food for the house. | palit, isda, kan-on, kape, mahal, barato, gikan (7); merkado again | mopalit ko og; mahal / barato kaayo; gikan sa |
| 009 | planned | Paying: prices and change. | numbers (Cebuano and Spanish-derived), bayad, hatag, kuha, tanan, pwede (6; the numbers count as one entry but are many forms) | pila tanan? baynte pesos; ihatag, kuhaa; pwede ba |
| 010 | planned | Hot afternoon. Everyone tired and hungry; Jun is not well. | kapoy, gutom, sakit, init, tugnaw, kay, pero (7) | ___ na ko (gutom na ko, kapoy na ko); kay = because; pero |
| 011 | planned | Evening talk: the fillers of real speech. | mao, kanang, murag, siguro, ambot, hala / ay, ngano, paminaw (8) | mao na / mao ba / mao gyud; kanang as a filler; murag; ngano man; paminaw! |
| 012 | planned | Looking for something lost in the house. | tan-aw, kita (see), kuan, buhat, ingon, unsaon, lagi (7) | tan-awa!; nakita nimo?; kuan as a placeholder; ingon niya; unsaon ni |
| 013 | planned | Days and times: when Mama works, when the friend comes back. | kanus-a, gahapon, ganina, kanunay, adlaw, oras, una (7) | kanus-a; gahapon / ganina / ugma; unsang orasa; kaon una |
| 014 | planned | Going out and coming back; a nice place, described without its name (the beach is Tier 3). | lakaw, balik, para, kung, basta, gani, sus, nindot (8) | molakaw na ko; balik ugma; para sa; kung gusto ka; nindot kaayo |

## Stage C: Tier 3 in batches, texts 015 onward

Not planned text by text yet. The Tier 3 backlog is grouped by topic in `vocabulary.md`; each Stage C text would promote one group of 8–10 (people, places, food, time, describers, particles, body and things, and the verbs in two or three batches) into full entries and use them, with the earlier words still carrying the text. About fifteen texts.
