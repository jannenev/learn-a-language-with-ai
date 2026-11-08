# Audio for the Cebuano texts

The listening side of the material: the pronunciation data that software needs, the voices that could speak the texts, the tests, and what a native speaker said of them. This is the record and reference, as `texts.md` is for the texts; `PLAN.md` keeps the decision, the open question and the dated log.

**Status (2026-11-08):** nothing has been generated or heard yet. The pronunciation marks were written with AI assistance and have not been checked by a native speaker; the lexicon's `status` column says which entries most need it.

## 1. The pronunciation layer (2026-10-07)

Pronunciation data lives in `pronunciation/`, separate from the texts, so the reading files stay clean and the audio side can be handed to software. Cebuano spelling is almost one letter, one sound; the two things it does not show are **stress** (pilá "how much" vs píla "a queue") and the **word-final glottal stop** (walâ "none" vs walá "left"). Those come from `pronunciation/lexicon.tsv`, one row per word, using the Philippine dictionary convention: acute = stressed syllable, grave on the final vowel = final glottal stop, circumflex = both. One-syllable clitics carry no mark. A `status` column marks entries to verify with a native speaker or Wolff's dictionary.

`tools/pron.py` turns a text into three machine files in `pronunciation/`:

- `NNN.paste.txt`: `rules-for-ai.txt` followed by the Cebuano lines with the marks, to paste into a chat voice such as ChatGPT voice mode.
- `NNN.ipa.txt`: one IPA transcription per line, syllables separated by dots. Reference, and nearly the input the Toucan engine below wants.
- `NNN.ssml.xml`: IPA inside SSML phoneme tags, written for an Azure Filipino voice. Dead target: found 2026-11-08 that Azure accepts no phoneme tags for its Filipino voices (section 2). To be replaced by the input forms of the engines that do take IPA.

Prefixed verb forms (mo-, ni-, nag-, gi-, ...) inherit the root's stress automatically; suffixed forms (-on, -a) move the stress and are listed explicitly. Words the lexicon does not know are printed and written in brackets so they can be added.

## 2. Voices surveyed (2026-11-08)

What can speak the texts falls into two kinds: engines that take a pronunciation description, so that stress and the glottal stops come from the lexicon and can be corrected, and engines that take only the spelling, so that stress is whatever the model learned.

**Driven by our pronunciation files** (the IPA that `tools/pron.py` already produces):

- *ElevenLabs v4 and v3.* Cebuano is a listed language for both model families, code `ceb`. v4 takes IPA inline: a word written between slashes in the text is spoken from the IPA, so a text goes in as plain Cebuano with IPA only where stress or a glottal stop matters. The documentation puts IPA consistency at 80–90 percent, a strong hint rather than a guarantee. Cloud service; the free tier is 10,000 characters a month and a text is 400–700, so the free tier covers the tests. Output MP3.
- *IMS Toucan* (University of Stuttgart, open source, Apache-2.0). Runs on a CPU, and its text front-end takes IPA lines directly (`input_is_phones=True` on the model call), skipping its own text-to-phoneme step, so our IPA is followed exactly. Cebuano is in its language list, but as one of 7,000 languages covered by zero-shot generalisation, not by Cebuano training data; voice quality unknown until tried. Its IPA symbol set is close to ours.
- *eSpeak NG.* A language can be added by writing spelling-to-sound rules and a word list, short for Cebuano, but the output is formant synthesis and sounds like a 1990s computer. Last resort.
- *Azure Filipino voices*: does **not** work. The language-support table marks every fil-PH voice "Phonemes, custom lexicon, and visemes aren't supported", so the `NNN.ssml.xml` files cannot drive stress there. `pron.py` should write the ElevenLabs form (text with IPA in slashes) and the Toucan form (IPA lines) instead.

**Plain text in, no pronunciation control:**

- *Meta MMS* (`facebook/mms-tts-ceb`). One small VITS model per language, trained on New Testament readings by a single speaker, about thirty hours; it learned Cebuano spelling-to-sound itself. Free, runs locally with torch and transformers, writes 16 kHz WAV. One voice for all speakers and a Bible-reading delivery, "robotic" but real Cebuano. Punctuation is largely ignored, so synthesise line by line and join the clips with silence. Licence: see section 6.
- *Google Gemini-TTS.* Cebuano (`ceb-PH`) is a preview language in the Cloud Text-to-Speech API. Delivery is steered by a natural-language prompt; no IPA and no per-word control. Probably the most natural and the least correctable: a comparison, not a source.
- *ChatGPT voice mode* with `NNN.paste.txt`: approximate, weak on stress and glottal stops.
- *macOS built-in voices*: none for Filipino or Cebuano.

A Cebuano speaker recording the texts (an italki or Preply tutor, for instance) stays the best audio in principle: stress, glottal stops and rhythm guaranteed, and unnatural lines caught at the same time. It costs a tutor's hour per batch and a wait for each new text, so the generated routes are what every text gets first, and a recording can be added later for the texts that stay in use.

## 3. Verification

A native speaker listening to generated clips and marking the words that sound wrong is a much smaller ask than recording the texts, and it checks the lexicon's `check` entries at the same time. The engines that take IPA can then be corrected; the plain-text ones cannot. The loop: generate a text with two or three engines, send the clips with the text to a speaker, fix the lexicon, regenerate.

## 4. Order to try

1. ElevenLabs v4 with plain text and the `ceb` code on the free tier, to hear whether it knows Cebuano or fakes it from Filipino.
2. The same with IPA on the marked words, to see whether the slashes override what it would have said.
3. Meta MMS locally, the free baseline that needs no account.
4. Toucan with the IPA lines, if the ElevenLabs IPA proves unreliable.
5. The best clips to a native speaker (section 3).

Gemini-TTS for comparison. Once an engine is chosen: retarget `tools/pron.py` to its input form, and add a `tools/speak.py` that writes `audio/NNN.mp3` for a text.

## 5. Playback

The output is audio files, so the learner needs nothing special:

- one track per text as `audio/NNN.mp3`, lines joined with pauses, for the listening-alone pass of the schedule in `PLAN.md`, section 2;
- later, per-line clips with a small HTML page showing block 1 and a play button on each line, for the pass with the text in view;
- the same files could be served from GitHub Pages next to the texts, with the licence and the unchecked status beside them.

## 6. Licence for published audio

Meta MMS weights are CC-BY-NC 4.0. A free repository is non-commercial, so audio made with it may be published here with attribution (Meta MMS, model `facebook/mms-tts-ceb`, CC-BY-NC 4.0) and a note that the audio files carry that licence even though the rest of the repository does not. Whether a model's licence reaches its output at all is unsettled; the cautious reading is to say so and costs nothing. A commercial use would have to replace the audio, by a speaker's recording or an engine with a permissive licence. Audio from a cloud service follows that service's terms; check them before publishing.

## 7. Tests and what the speaker said

None yet. Record here per test: date, engine and settings, text, who listened, which words were flagged, and what changed in the lexicon as a result.
