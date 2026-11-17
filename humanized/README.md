# Humanized chapter sections (live-draft versions)

Sections that went through Walter and then a repair and voice pass. The canon chapter files in `chapters/` stay the continuity source; these are the Royal Road live-draft wording. Each file is checked with `python3 tools/chapter_check.py --chunk <file>` and holds under 1,500 words.

- `chapter-01-part-1.md`: Chapter One, first section (about 1,430 words). Walter's cleanup kept; meaning errors fixed (hardly anyone, gas signs, hand controls, locs, the 23rd, the king, death lock); dashes and ellipses removed; Tatsuya's voice lines, thoughts and Chiyo's text restored from the original; title restored to "The Countdown Starts".

## Two versions of every chapter (author-stated, latest)

- `chapters/` holds the **original (unhumanized)** version of each chapter. It stays untouched once a humanized version exists, so there is always a clean version to check against if something feels off.
- `humanized/` holds the **Royal Road live-draft** version, one file per chapter with the same number (for example `humanized/chapter-01.md`), assembled from the finished sections. Sections live here as `chapter-NN-part-N.md` until every part of the chapter is done.
- Purpose: the author writes and directs the chapter; Walter smooths the wording so it does not read as AI slop; Claude repairs meaning errors, dashes, ellipses and thoughts and restores Tatsuya's voice. This is for Royal Road readers, not print; an editor comes after Book One.
- Rule: any continuity or canon change is made in the original first, then carried into the humanized version, so the two never drift.
- `chapter-01-part-2.md`: Chapter One, second section (about 1,470 words). Meaning fixes (ZONE: CONTESTED, the surgery and the "tenth" line, Kazuku as the CG bear and not a costume, Haoyu and the Knights' plan, the six-for-London line, the forever-after-two-hours line), dashes, ellipses, ampersands and slashes removed, thoughts restored, dropped voice and character lines restored (Dad's redundancy line, the reinforcements, "I felt nothing about it", his suspicion of Kazuku).
