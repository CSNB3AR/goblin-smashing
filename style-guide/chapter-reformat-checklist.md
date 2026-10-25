# Chapter Reformat Checklist

How to bring an old chapter (4 to 10) up to the format set by `chapters/chapter-01.md`, `chapter-02-new.md` and `chapter-03-new.md`. One chapter at a time, written to `chapters/chapter-NN-new.md`; the old file stays until the author says to renumber.

## Run it

1. `python3 tools/chapter_check.py chapters/chapter-04.md` lists certain rule breaks (MUST FIX) and lines worth a look (LOOK AT). It never edits.
2. Rewrite into `chapters/chapter-04-new.md` using the format below.
3. Run the checker on the new file until MUST FIX is empty, and clear the LOOK AT lines that are real.
4. `python3 tools/build_chapter.py chapters/chapter-04-new.md` makes the docx and md to send (needs `pip install python-docx`).
5. Commit and push, then send the files.

## The format

- Title `# Chapter Four: Title`, end marker `**[END CHAPTER FOUR]**`.
- First person, past tense, inside Tatsuya's head. Narration never says he, his or Tatsuya about him (the checker flags these; ignore lines about other men).
- Direct thoughts are `*"..."*`, quotes and italics. Reflection stays narration.
- System text `**[...]**`. Lumi `***[...]***`. Dialogue in plain quotes, one speaker per paragraph.
- No em dashes. The only exception is Lumi's cut-off `ch—` in bold-italic system text.
- Concrete detail over figures. Keep a figure only if it comes from his world and makes the scene clearer (see `concrete-detail-and-figurative-language.md`).
- Cues follow `style-guide/cue-bank.md`: his signature thinking tell is scratching the thin goatee (once or twice a chapter), crutch cues (jaw, stomach, pulse, breath, shoulders, knee, hands flat) are capped at once per chapter and not repeated from the previous chapter, and builds were drawn on tablets, never graph paper.
- Tatsuya is not a fan. No esports vocabulary, no meta talk, no outside knowledge he would not have.
- Emotion fits each scene and shifts with it: name what he feels coming in, what turns it, and what he leaves with (see `craft-rules.md`, "Emotion fits the scene").
- Humor is an occasional drip, honest, aimed at people who earned it, never at Haruto.

## Canon to match (the ledger wins)

`outline/canon-ledger.md` is authoritative. Quick reminders from the first three chapters: Thornwatch is the finale site (proposal); Yuna and Kazuku appear only as avatars; the scooter is black with a fingerprint lock and visor helmet; Mom (Ohema) is in a coma; Dad's letter is folded in the manual; the 72-hour lock; shillings and HGO Coin; Goblin and Seranis by default after the glitch. Do not resolve OPEN items.

## Per-chapter pass

Read the old chapter whole, mark every line that breaks the format or the ledger, change only those lines and the beats around them, keep the author's content and voice, reread the whole chapter, then run the checker.
