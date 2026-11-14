# Cebuano: the PDFs

Ready-made PDFs of the Cebuano material, for reading on screen or printing on A4. Click a file to open it; the download button is at the top right of the page that opens.

| File | What it is | Pages | Holds | Built from | Content date |
|---|---|---|---|---|---|
| [cebuano-texts-full.pdf](cebuano-texts-full.pdf) | The full booklet: an intro page, then each text three times, on its own, beside the English, and word by word with notes. The one to start with. | 15 | texts 001–004 | `tools/print.py --all --full` on `texts/src/001.txt` to `004.txt` | 2026-11-14 |
| [cebuano-texts-pocket.pdf](cebuano-texts-pocket.pdf) | The pocket booklet: an intro page, then one page per text, Cebuano left and English right, for re-reading. | 5 | texts 001–004 | `tools/print.py --all --glosses` on the same four sources | 2026-11-14 |
| [cebuano-word-sets.pdf](cebuano-word-sets.pdf) | One page: the small words in their sets (persons, pointing words, verb shapes, particles, markers). | 1 | forms marked against texts 001–004 | `tools/sheet.py --two` on `word-sets.md` | 2026-11-14 |

These files are copies, made at a milestone, of what the tools build into the local folder `cebuano/print/`, which is not in the repository. The texts in [`../texts/`](../texts/) can be newer than the PDFs; the table above says which texts each PDF holds.
