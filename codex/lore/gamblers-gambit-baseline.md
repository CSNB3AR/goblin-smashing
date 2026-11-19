# Gambler's Gambit: baseline (PROPOSAL, full working system)

Builds on `codex/objects/gamblers-earring.md`, the ledger section "Tatsuya's build, Flamonta, the Gambit dice, the necklace and secondary stats", and `codex/lore/secondary-stats-baseline.md`. Everything below is PROPOSAL unless the page has already shown it. Page facts so far: a d6 (Chapter Five, "ROLL: 3", drop chance increased), one loot roll per day (Lucky Break, Chapter Four), the earring is UNIQUE and sellable, and Rune Priming rolls a die and still costs mana on a low roll (Chapter Ten).

## The core rule
Gambler's Gambit is a d6 gamble attached to the Gambler's Earring. Every use rolls one d6, adds the dice modifier, reads the table, and multiplies the base strength of whatever the roll was made on. A natural 1 is always a FAILED ROLL and always breaks the item the roll was made on. The earring never rolls on itself and never breaks. Design rule: every gamble carries a risk, so there is always a cutoff.

## What rolls it covers
| Roll type | Trigger | What the multiplier changes |
|---|---|---|
| Loot | Lucky Break, once per day after combat (on page) | Drop chance and quality odds. Fortune sets the base odds, the multiplier scales them. |
| Attack | From level 10, the player may roll before an ability | Damage of the next ability, see the AP link below. |
| Enchantment | Rolled when an enchant is applied to a weapon or shield | Enchant potency and duration. |
| Rune | Rolled by Rune Priming, and any rune set under Gambit | Rune damage or field strength. A fail fizzles it and still costs the mana. |
| Buff | Rolled on a buff or field effect for himself or his party within 15 seconds | Buff strength and duration. |

Only one Gambit roll is live at a time. The attack and buff roll shares a 90 second cooldown. Loot stays once per day. Enchant and rune rolls cost no cooldown but their own normal cost.

## The d6 table and the AP formula
The page formula is: ability damage = tier base x (1 + AP / 100), with AP the Physical, Magic or Ranged AP the art requires. The Gambit multiplier multiplies the TIER BASE and never replaces AP:

final damage = tier base x Gambit multiplier x (1 + AP / 100)

Worked example (PROPOSAL numbers): tier base 40, Magic AP 52. Unrolled: 40 x 1.52 = 60.8. Roll 4 (125 percent): 40 x 1.25 x 1.52 = 76. Roll 6 (160 percent): 40 x 1.6 x 1.52 = 97.3.

| Natural roll | Result | Multiplier |
|---|---|---|
| 1 | FAIL. The rolled item breaks. A crit fail debuff follows if the crit fail condition below is met. | 0 |
| 2 | Weak. Lands at base, no boost. | 100 percent |
| 3 | Normal. | 110 percent |
| 4 | Good. | 125 percent |
| 5 | Strong. | 140 percent |
| 6 | Crit. Bonus effect: one free extra stack, one cooldown refunded, or one rarity step up on a loot roll. | 160 percent |

The modifier is added before the table is read. The table reads at most 6. Each point above 6 adds 5 percent to the multiplier, up to plus 30 percent (so the best result is 190 percent). The modifier cannot turn a natural 1 into anything: a natural 1 always fails.

Crit fail condition: a natural 1 is an ordinary FAIL (item breaks, nothing else). It becomes a CRIT FAIL when the roll was an attack or buff roll made in combat, or when Fortune is below 10 times the dice tier number (a long streak of bad luck). In practice: any fight roll that comes up 1 is a crit fail.

## What a failed roll breaks, and what is protected
Breaks, always the item the roll was made on:
- Loot roll: the drop that the roll was applied to turns to scrap (the roll is made on the dropping item, so a failure costs that one drop, never the whole day's haul).
- Enchantment roll: the weapon or shield loses the enchant and drops one durability tier. A smith repairs it.
- Rune roll: the rune fizzles, the priming components are consumed, and the mana is spent.
- Attack roll: the weapon or focus used is damaged to Cracked (halved stats until repaired).
- Buff roll: the buff fails and the targeted ally item is unharmed (the cost is the debuff and the lost cooldown).

Protected: the Gambler's Earring, anything Bound, anything Unique (these lose the enchant and take a 60 second lock instead of breaking), the death penalty exemption items, and any item not named as the roll's target. Worn armor is never rolled on.

## Crit fail debuffs (pick one, 20 to 60 seconds, scaled by tier)
- Power loss: minus 25 percent damage dealt.
- Silenced: cannot cast.
- Fumble: the next Physical Art fails and its stamina is spent.
- Hexed: minus 20 percent resists.

## Upgrade ladder (every 10 levels until 80)
| Level | Die | Modifier | Effect |
|---|---|---|---|
| 1 | Plain bronze die | +0 | Loot roll only (on page). |
| 10 | Worn die | +1 | Unlocks the attack and buff roll (the next ability, or the party's, within 15 seconds). This is the power boost. |
| 20 | Pipped die | +2 | Enchantment and rune rolls unlocked. |
| 30 | Silver die | +3 | A failed roll breaks only Common or Uncommon gear, higher rarity takes the lock instead. |
| 40 | Gilt die | +4 | Crit fail debuff halved in length and strength. |
| 50 | Brass and bone die | +5 | A natural 6 also grants a short shield. |
| 60 | Bone die | +6 | One reroll of a failed roll per day. |
| 70 | Gold die | +6 | The table moves up one step (a 2 reads as a 3, and so on up to 6). |
| 80 | Gambler's die | +6 | Cap. A chosen bonus effect on every 6. |

The dice tier is the earring's own level, and Tatsuya does not know it scales yet (see the earring file). He finds out at level 10.

## Interaction with Fortune
Fortune does not change the d6. It does three things: it sets the base odds of the loot roll (Lucky Break), it adds a Saved Roll chance (5 percent per 10 Fortune, cap 30 percent) that turns a natural 1 into a 2 and spares the item, and it raises crit chance on the ability that follows. Tatsuya's Fortune is 12 on the page, so his Saved Roll chance is 5 percent.

## Open questions
- The earring file header still says Rare, the page says UNIQUE.
- The old "crit fail breaks the item he just received" note is generalised here to the item the roll was made on.
- The exact Gambit tier base numbers need the full AP chart.
