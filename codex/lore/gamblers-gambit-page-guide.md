# Gambler's Gambit: page guide (PROPOSAL)

Companion to `codex/lore/gamblers-gambit-baseline.md`. Chapters are NOT changed by this file. It gives the system lines, the short wording to add, and a list of every place that should change.

## System lines for the page (one to two lines each)
A roll:
**[GAMBLER'S GAMBIT: ROLL 4 +1 = 5 | STRONG | x1.40]**

A break (failed roll):
**[GAMBLER'S GAMBIT: ROLL 1 | FAILED | GOBLIN FANG ENCHANT BROKEN]**

An upgrade (level 10, with the second line only when it matters):
**[DICE UPGRADED: WORN DIE | MODIFIER +1 | ATTACK AND BUFF ROLL UNLOCKED]**

A crit fail (add the debuff line):
**[CRIT FAIL: HEXED, MINUS 20 PERCENT RESISTS, 30 SECONDS]**

## Short wording to add where the Gambit or die is described
One line, said by the system or by Tatsuya in thought:
- System: **[ANY FAILED ROLL BREAKS THE ITEM IT WAS ROLLED ON. THE DICE GROW STRONGER EVERY 10 LEVELS.]**
- Tatsuya: *"A one breaks whatever I rolled it on. That's the price."*
Keep it to those two lines so the early chapters read as a light touch, not an info dump. The "grows every 10 levels" half should stay hidden until Tatsuya learns it (see the earring file), so add only the first half in Chapters Four to Seven.

## Lines that should change (file, line, current, proposed)
Line numbers are as read now.

1. `chapters/chapter-04.md` line 87. Current: **[PASSIVE ACQUIRED: GAMBLER'S GAMBIT]**. Proposed: add a line after it: **[RISK: ANY FAILED ROLL BREAKS THE ITEM IT WAS ROLLED ON.]**
2. `chapters/chapter-04.md` line 93. Current: **[ACTIVE: Once per day, after combat ends, roll for a chance at Rare or higher quality loot. Fortune stat increases success rate.]**. Proposed: "...roll a d6 for a chance at Rare or higher quality loot. A roll of 1 breaks the dropped item. Fortune stat increases success rate."
3. `chapters/chapter-04.md` line 107. Current: **[ABILITY: LUCKY BREAK - Once per day after combat, roll for a chance at Rare or higher quality loot. Fortune stat increases success rate.]**. Proposed: same change as item 2, and drop the dash in the ability label if the style rule applies (write "LUCKY BREAK:").
4. `chapters/chapter-04.md` line 111. Current: "The roll only fired after combat, so I'd still have to farm..." Proposed: add "A one would break whatever it landed on, and I'd have to live with that."
5. `chapters/chapter-05.md` line 141. Current: **[ROLL GAMBLER'S GAMBIT TO INCREASE DROP CHANCE? YES / NO]**. Proposed: **[ROLL GAMBLER'S GAMBIT TO INCREASE DROP CHANCE? A ROLL OF 1 BREAKS THE DROP. YES / NO]**
6. `chapters/chapter-05.md` line 151 area. Current: **[ROLL: 3]**. Proposed: **[ROLL: 3 | NORMAL | x1.10]** then the existing "DROP CHANCE INCREASED".
7. `chapters/chapter-05.md` line 153 (Tatsuya's thought). Current: "Does a higher roll mean a better drop?" Proposed: add "And a one?" so the risk is planted.
8. `chapters/chapter-06.md` line 11. Current: "The Gambit got me lucky early money, but luck runs out..." Proposed: "The Gambit got me lucky early money, but a bad roll breaks the thing it's rolled on, and luck runs out..."
9. `chapters/chapter-06.md` line 209. Current: "...and the Gambit only fired once a day." Proposed: "...and the Gambit only fired once a day, and a one would have turned that into scrap."
10. `chapters/chapter-06.md` line 211. Current: "What does this die do as it climbs?" Proposed: no change needed (it plants the hidden upgrade). Keep.
11. `chapters/chapter-07.md` line 41. Current: **[GAMBLER'S EARRING - UNIQUE (EQUIPPED)]**. Proposed: no change to the title; optionally add **[NEVER BREAKS FROM A FAILED ROLL]** if the sale screen shows tags.
12. `chapters/chapter-06.md` line 37. Current: "The dice on my earring ticked against my jaw when I swallowed." Proposed: no change.
13. `chapters/in-progress/now/chapter-10-assembling-the-assault-team.md` lines 145 to 147. Current: **[SETS A RUNE ON A SURFACE. ROLL REQUIRED. COSTS MANA ON EVERY ATTEMPT.]** and Leon: "Low roll and it fizzles, and it still eats the mana." Proposed: if Rune Priming is Gambit powered, add "A one breaks the rune chalk too." Otherwise keep it as a separate spell roll and do not link it to the Gambit.
14. `chapters/in-progress/now/chapter-09-the-first-disciple.md`: no Gambit, die or earring mention found (only a hit on "die" as a verb at line 373). No change.

Notes: no chapter in 4 to 7 or 9 and 10 describes the upgrade ladder, so the ladder stays unwritten until level 10.
