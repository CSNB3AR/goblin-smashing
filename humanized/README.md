# Humanized chapters (Royal Road live drafts)

## Two versions of every chapter (author-stated)

- `chapters/` holds the **original (unhumanized)** version of each chapter and stays untouched, so there is always a clean version to check against if something feels off.
- `humanized/chapter-NN.md` holds the **Royal Road live-draft** version of the same chapter. It is assembled from finished sections in `humanized/parts/`.
- `humanized/pre-walter/` keeps Claude's text from before it went through Walter, for reference.
- Rule: any continuity or canon change is made in the original first, then carried into the humanized version, so the two never drift.
- Purpose: the author writes and directs the chapter; Walter smooths the wording so it does not read as AI slop; Claude repairs what the humanizer breaks (meaning errors, dashes, ellipses, thoughts, lowercase) without rewriting its wording. For Royal Road readers, not print; an editor comes after Book One.

## Process per section (about 1,400 words, under Walter's 1,500 limit)

1. Section goes through Walter. 2. Claude compares it to the original and fixes meaning errors, dashes, ellipses, thought formatting, capitalization and canon slips, keeping Walter's wording. 3. Check with `python3 tools/chapter_check.py --chunk <file>`. 4. Author runs the detector (ZeroGPT, Pangram). Aim: no meaning errors, no rule breaks, and roughly 60 percent AI or lower per section.

Lesson learned: restoring Claude's own original wording raises the detector score (one section jumped to 93 percent AI). Voice lines are better dictated by the author in their own words.

## Status

- Chapter One: done. `humanized/chapter-01.md` (about 3,570 words). Part 1 reads 31 percent AI (before the grammar cleanup), part 2 reads 56 percent AI, part 3 reads 10 percent AI (ZeroGPT).
