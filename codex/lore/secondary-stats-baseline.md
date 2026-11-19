# Secondary stats: baseline (PROPOSAL, extend as we go)

Builds on `codex/lore/secondary-combat-stats.md` (the named stats and what feeds them). This file only adds the minimum arithmetic a writer needs. Nothing here is canon until the author accepts it. No numbers go on the page for gold-tag NPCs.

## The one rule that holds the rest together
Every secondary stat is a flat number derived from disciplines and gear. Rough scale used by the page so far: **Magic AP is about 4 times Wisdom** (Tatsuya at level 8: Wisdom 13 with the necklace gives Magic AP 52, from Chapter Eleven's old draft), and **Physical AP is about 4 times Power plus a share of Speed**. Defence stats use the same 4 times scale on their feeder discipline plus gear.

## Baseline formulas (PROPOSAL)
| Stat | Baseline |
|---|---|
| Ability damage | tier base x (1 + AP / 100), where AP is Physical, Magic or Ranged AP as the art or spell requires |
| Hit chance | 50 percent plus (Accuracy minus target Evasion) / 4, clamped to 5 to 95 percent |
| Crit | Crit Rate from Fortune (Tatsuya about 36 percent at level 8 with the earring), Crit Multiplier about 1.6 at low levels up to about 2.1 |
| Physical Damage Reduction | Power x 4 plus armour, subtracted per hit after Armor Pierce, never below 10 percent of the hit |
| Magic Resistance | (Wisdom + Courage) x 2, as a percent cut, capped at 60 percent before buffs |
| CC resist | Power or Courage x 1 percent per point for physical CC, Wisdom for mental, large level gaps bypass it (canon, debuffs file) |
| Resistance buff / debuff | adds or subtracts flat percent points to the resist, never above 75 percent, never below minus 50 |

## Level bands (typical, PROPOSAL)
| Level | Physical or Magic AP | PDR | Magic Resistance | HP |
|---|---|---|---|---|
| 1 | 8 to 16 | 2 | 5 percent | 53 |
| 8 | 24 to 52 | 6 | 15 percent | 65 (page) |
| 25 | 90 to 130 | 25 | 30 percent | 125 |
| 50 | 200 to 260 | 60 | 45 percent | 200 |
| 80 | 340 to 420 | 110 | 55 percent | 290 |

HP uses 50 plus 3 per level as in the NPC notes, with the page's 65 at level 8 taking precedence for Tatsuya.

## How the Gambit dice plug in
A d6 roll sets a multiplier on the next ability's damage or buff strength (see `codex/lore/gamblers-gambit-baseline.md`). It multiplies the ability's base, so it scales with the same AP formula and never replaces it.

## Conflicts to settle later
- The old draft's Ancient Bone Flame Barrage numbers (840 base, 1,840 total) are a Tier 5 burst plus Bone Surge amplify and do not come from this formula.
- HP at higher levels is a proposal, the page only fixes level 8 at 65.
