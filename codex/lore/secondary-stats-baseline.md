# Secondary stats: baseline (PROPOSAL, complete working chart)

Builds on `codex/lore/secondary-combat-stats.md` (named stats and feeders), `codex/lore/five-disciplines-stat-system.md`, `codex/lore/hp-sp-mp-resource-pools.md` and `codex/crafting/debuffs-and-resistances.md`. Every formula and number below is PROPOSAL unless marked page or canon. No numbers go on the page for gold tag NPCs. On the page, show only the result in Tatsuya's HUD, never the arithmetic.

## The turn order of one attack
1. Hit roll: hit chance = 50 percent + (Accuracy minus target Evasion) / 4, clamped 5 to 95 percent.
2. Block roll (shield only).
3. Crit roll.
4. Damage = base x (1 + AP/100) x crit multiplier x any Gambit or Amplify multiplier.
5. Mitigation: physical hits lose PDR (flat), magic hits lose Magic Resistance (percent). Floor: a hit never drops below 10 percent of its pre mitigation damage.
6. Percent Physical Resistance or elemental resistance applies last.

Base is the weapon, art or spell tier base. Gear adds flat points to the stat, never to the base.

## Stat chart (feeder, formula)
| Stat | Feeder | Formula |
|---|---|---|
| Physical AP (melee) | Power, Speed | 4 x Power + 1 x Speed + gear |
| Ranged AP | Speed, Power | 4 x Speed + 1 x Power + gear |
| Magic AP | Wisdom | 4 x Wisdom + gear (page: Wisdom 13 gives 52) |
| Accuracy | Speed, Wisdom | 2 x (Speed + Wisdom) + gear |
| Physical Evasion | Speed | 3 x Speed + gear |
| Magic Evasion | Wisdom | 2 x Wisdom + gear |
| Armor Pierce | Power | Power x 1 percent of target PDR ignored, cap 50 |
| Physical Defense (PDR) | Power, armour | 1 x Power + armour rating, flat per hit |
| Magical Defense (Magic Resistance) | Wisdom, Courage | (Wisdom + Courage) x 0.5 percent, cap 60 before gear and buffs |
| Physical Resistance | gear, race, buffs only | percent cut after PDR, base 0 (no discipline feeds it) |
| Crit Rate | Fortune | 5 + Fortune percent + gear, cap 75 |
| Crit Multiplier | Fortune | 1.5 + 0.0075 x Fortune, cap 2.5 |
| Block Rate | Power, shield | 0.5 x Power + shield rating percent, cap 50; zero without a shield |

A blocked hit takes 50 percent less, plus the shield's quality (up to 25 more points). Physical CC Resistance is (Power + Courage) x 0.5 percent, Mental Resistance is Courage x 1 percent, cap 60 each. Elemental and Toxin resistance come from race baseline and gear only (Goblin baseline 0); Silence has none, by canon.

## Typical values by level (single focus build, PROPOSAL)
| Level | Phys / Ranged / Magic AP | PDR | Magic Resist | Crit Rate | Crit Mult | Phys Evasion | Block (shield) | HP |
|---|---|---|---|---|---|---|---|---|
| 1 | 8 to 16 | 2 | 5 percent | 11 percent | 1.5 | 9 | 11 percent | 53 |
| 8 | 24 to 52 | 6 | 15 percent | 15 percent | 1.55 | 30 | 15 percent | 65 (page) |
| 25 | 90 to 130 | 25 | 28 percent | 30 percent | 1.7 | 66 | 25 percent | 125 |
| 50 | 200 to 260 | 60 | 48 percent | 45 percent | 1.9 | 120 | 38 percent | 200 |
| 80 | 340 to 420 | 110 | 58 percent | 60 percent | 2.1 | 195 | 50 percent | 290 |

Low end of an AP band is a hybrid or support build, high end a dedicated damage dealer. Tatsuya sits low on purpose (Power 4, Energy and Wisdom heavy).

## How gear and buffs stack
- Gear adds flat to the stat before anything else. Gear slots obey the page format `[STAT: subtotal] (+X)`.
- Buffs on AP, Evasion or Accuracy add percent points of the final stat. Different named buffs add together; two buffs of the same name do not stack, the stronger applies.
- Multipliers (crit, Gambler's Gambit d6, Bone Surge amplify) multiply the ability, never the stat, and multiply each other.
- Resistance buffs add percent points to a resistance. Resistance debuffs subtract points from it. Net resistance is clamped to a maximum of 75 percent and a minimum of minus 50 percent (a target at minus 50 takes 150 percent). A debuff cannot lower a stat that does not exist (Block with no shield).
- Physical CC and Mental resists are bypassed by a large level gap, per the debuffs file.

## Worked examples

**Tatsuya, level 8 (HP 65, SP 32, MP 32).** Power 4, Speed 12, Wisdom 13 with the necklace, Fortune 16 (assumed), earring adds 15 crit.
- Magic AP = 4 x 13 = 52 (page). Shiv-Touched Flare, tier base 2.6: 2.6 x 1.52 = 3.95, shown as 4 (page).
- Physical AP = 4 x 4 + 12 = 28. Fists, base 5: 5 x 1.28 = 6.4, shown as 6 (page).
- Crit Rate = 5 + 16 + 15 = 36 percent (page). Multiplier = 1.5 + 0.12 = 1.62. A crit Flare is 3.95 x 1.62 = 6.4, shown 6.
- Evasion 36, PDR 6 (Power 4 + armour 2), Magic Resist about 12 percent.
- Against the level 6 raider below: fists do 1 (see raider PDR). Flare does 4 (raider Magic Resist about 5 percent). The story point: his fists are useless on armour, his magic is not.

**Level 5 to 6 raider (level 6 shown, HP 68; level 5 is HP 65, one tick weaker).** Power 7, Speed 8, Wisdom 3, Courage 4, leather armour 2, short blade base 9.
- Physical AP = 28 + 8 = 36. Hit on Tatsuya: 9 x 1.36 = 12.2, minus PDR 6 = 6 per hit. Tatsuya dies in about 11 hits.
- Accuracy = 2 x 11 = 22 against Tatsuya's Evasion 36: 50 + (22 minus 36)/4 = 46 percent per swing.
- PDR = 7 + 2 = 9. Tatsuya's fist (6.4) minus 9 falls under the floor, so it deals the 10 percent minimum, 0.6, shown as 1. Magic Resist = (3 + 4) x 0.5 = 3.5 percent.

**Wyx, level 25 (PROPOSAL build: Windrider archer, not read from canon).** Speed 28, Power 12, Wisdom 14, Fortune 18.
- Ranged AP = 4 x 28 + 12 = 124. Arrow, base 14: 14 x 2.24 = 31.4. Crit Rate 5 + 18 + 5 gear = 28 percent, multiplier 1.5 + 0.135 = 1.64, crit arrow 51.
- Against a level 25 Ironbreaker with PDR 30: Armor Pierce 12 percent, effective PDR 26.4, arrow deals 5. Against a robed caster with PDR 8: 23. Archers beat soft targets and struggle on plate, which is the intended identity.
- Accuracy 2 x 42 = 84 against Evasion 66: 50 + 4.5 = 54 percent hit.

**Sevish, level 80 (PROPOSAL build: Wisdom caster, not read from canon).** Wisdom 95, Courage 50, Fortune 40, Magic AP 4 x 95 + 20 gear = 400.
- A tier 5 spell, base 60: 60 x 5.0 = 300. Crit Rate 45 percent, multiplier 1.8, crit 540.
- Target (level 80) Magic Resist 58 percent: 300 x 0.42 = 126. Resistance buff on target of plus 15 points makes it 73 percent, damage 81. A resistance debuff of minus 20 on the original 58 gives 38 percent, damage 186. A Gambit roll of 1.5 on the spell base lifts the 126 line to 189.
- Sevish's own Magic Resist = (95 + 50) x 0.5 = 72.5, capped at 60 before gear; two resist buffs of 10 each bring it to 75 and no further.

## Conflicts with canon and earlier baseline
- Earlier baseline said PDR is Power x 4 plus armour and Magic Resistance (Wisdom + Courage) x 2. Both blow past its own level table (a Power 4 character would have PDR 16 at level 8, Tatsuya's table value is 6). Changed here to Power x 1 and x 0.5. If the author prefers the old scale, damage bases must be roughly tripled.
- Earlier Magic Resist table values (30, 45, 55) shifted slightly to 28, 48, 58 to match the formula.
- Accuracy is now 2 x (Speed + Wisdom); the secondary stats file only says Speed + Wisdom joint.
- Physical Resistance (percent, gear only) is new; the secondary stats file lists only PDR. Delete it if one physical defense number is wanted.
- Tatsuya's Speed 12, Fortune 16 and earring value 15 are inferred to land the page numbers (6, 36 percent), not stated anywhere. Wyx and Sevish have no stat sources in the files read.
- Level 5 raider HP 65 equals Tatsuya's page HP at level 8 by the 50 + 3 per level rule, which may look odd on the page.
- Ancient Bone Flame Barrage (840 base, 1,840 total) still does not come from this formula; it is a Tier 5 burst plus Bone Surge amplify.
- Gambit d6 multiplier: unchanged, see `codex/lore/gamblers-gambit-baseline.md`.
