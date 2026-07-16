# The Deck-Building Layer

Ties directly to Pillar 3 of `story/premise.md`: a player's permanent, earned inventory functions as their deck, and what they bring into a competitive match matters as much as their class. Never named as its direct inspiration (Chaotic TCG) on the page, described functionally only.

## Base classes / build paths

Background texture, world-building rather than something Tatsuya gets boxed into, his goblin kit (Physical Arts, Shaman's Veil, the Call of the Bones Necklace) stays its own thing. What other players and pro teams draw from: **Spellforger** (mage, elemental burst/crowd control), **Ironbreaker** (tank, shield and taunt), **Shadowveil** (rogue/assassin, stealth and crits), **Windrider** (archer/hunter, ranged DPS and pets), **Warden** (support/cleric, healing and buffs), **Wildcaller** (summoner/druid, beast summons and terrain control), **Berserker** (melee DPS, rage and cleave), and **Hybrid/Custom** (gear-driven multi-classing, consistent with the deck-building pillar, meta-breaking off-builds live here).

## Per-race base stats (first-pass proposal, flagged for review)

Every playable race (see `codex/lore/playable-races-and-character-creation.md`) starts with a base line across the six Disciplines+Energy stats (`codex/lore/five-disciplines-stat-system.md`), before any player-allocated leveling points (`codex/lore/leveling-and-progression.md`) get added on top. Illustrative starting values, not hard-locked, meant to read as flavor consistent with each race's established identity:

| Race | Courage | Power | Wisdom | Speed | Fortune | Energy |
|---|---|---|---|---|---|---|
| Human | 6 | 6 | 6 | 6 | 6 | 6 |
| Elf | 4 | 3 | 9 | 6 | 5 | 5 |
| Orc | 6 | 9 | 3 | 5 | 4 | 7 |
| Beastfolk | 5 | 8 | 3 | 8 | 4 | 6 |
| Goblin | 4 | 4 | 2 | 7 | 9 | 4 |
| Dwarf | 8 | 7 | 4 | 3 | 5 | 7 |
| Frostborn | 8 | 6 | 5 | 4 | 4 | 7 |
| Drakekin | 7 | 7 | 7 | 6 | 6 | 7 |

Human reads balanced, no bias, matching Lunarest's "central hub" flavor. Elf leans hard into Wisdom (magic affinity), the natural draw for Tatsuya's original build plan before the glitch. Orc and Beastfolk both lean Power/Speed with a real Wisdom penalty. Goblin's low Wisdom is the already-established Wisdom penalty (negated only by the Call of the Bones Necklace, see `codex/objects/call-of-the-bones-necklace.md`), offset by the race's signature high Fortune, the highest in the game at any race's base line, essentially nobody else builds around it the way a goblin can. Dwarf and Frostborn both read sturdy, Courage/Power-leaning. Drakekin, the rare achievement race, reads strong across the board, no clean single bias, consistent with it not being tied to a starting zone.

### Racial abilities (baseline, every member of the race gets these)

Separate from rare-variant rolls (`codex/lore/playable-races-and-character-creation.md`), which layer on top of these, not replace them. One short passive per race:

| Race | Racial Ability |
|---|---|
| Human | **Adaptable** — small bonus to whichever Discipline was last actively trained, reads as the race's "no real weakness" identity mechanically, not just flavor. |
| Elf | **Mana Sight** — can visually perceive active magic effects and residual mana traces others can't, a real informational edge in any fight involving casters. |
| Orc | **Unbroken** — resists the first stagger/stun effect taken in a fight per encounter, fits the race's Power-lean and battlefield-durability identity. |
| Beastfolk | **Predator's Instinct** — bonus initiative and a passive read on the nearest real threat in a room, matches the race's Speed/Power lean. |
| Goblin | **Scavenger's Eye** — passively identifies which nearby loot is actually worth picking up before it's touched, the race's baseline economic edge, distinct from Tatsuya's own Gambler's Gambit below. |
| Dwarf | **Iron Constitution** — reduced Energy loss from sustained (non-burst) damage, fits the race's Courage/Power-leaning sturdiness. |
| Frostborn | **Cold Endurance** — full immunity to environmental cold/exposure effects, a survival-flavored racial rather than a combat one. |
| Drakekin | **Draconic Presence** — a minor passive intimidation aura, weaker enemies hesitate half a beat before engaging, consistent with the race's no-clean-bias, strong-across-the-board identity. |

### Racial resistances

A per-race lean on elemental/damage-type resistance, not hard immunities, flavor-consistent nudges rather than a second full stat system layered on top of the six Disciplines:

| Race | Notable resistance | Notable weakness |
|---|---|---|
| Human | none, flat baseline | none, flat baseline |
| Elf | Storm | Earth |
| Orc | Poison | Frost |
| Beastfolk | Frost | Fire |
| Goblin | none, deliberately flat/unspecialized across the board, consistent with the race's low-floor, no-hard-walls identity | none, same reason |
| Dwarf | Earth | Storm |
| Frostborn | Frost | Fire |
| Drakekin | Fire | Poison |

### Goblin racial passive: Gambler's Gambit (corrected, replaces the earlier "Long Shot" placeholder)

Not a generic racial trait, a rare-variant roll result specific to Tatsuya (see `codex/lore/playable-races-and-character-creation.md`), a Fortune bonus and a once-per-day chance after combat to roll for Rare-or-higher loot. It manifests physically as the **Gambler's Earring** (see `codex/objects/gamblers-earring.md`), equipped as soon as he's actually in the game world, not an abstract passive with nothing to hold. This is his real income engine early on, the concrete reason he has something to actually farm for during his window before Chiyo's back, not just XP. **This governs loot only, not the World Quest activation itself**, see `codex/lore/world-quests.md` and `codex/subplots/world-quest-call-of-the-bones-camp-arc.md` for why "Call of the Bones" actually activates (a keyword/philosophy trigger the camp's AI recognizes). In Chapter 3, it procs on the kill that happens to also trigger the quest, landing him the goblin gadget belt and a couple of sellable potions off two otherwise-worthless camp goblins, see `codex/objects/goblin-gadget-belt.md`. Later, the Call of the Bones Necklace grants a separate combat ability, The Bones Speak (Amplify/Reflect), unrelated to Gambler's Gambit beyond sharing a Fortune/gambling theme, see `codex/objects/call-of-the-bones-necklace.md`.

## Race/class magic-access restrictions

Not every race can freely learn every skill tree. A D&D-style convention: races with a Wisdom penalty (Orc, Beastfolk, Goblin) have restricted access to high-tier arcane/Spellforger-path trees by default, they lean into Physical Arts (see `codex/lore/preserved-misc-mechanics.md`) instead. Elves and Humans have full, unrestricted magic access. Dwarves and Frostborn sit in between, partial access, more elemental/rune-utility flavored than pure arcane.

**Goblin specifically isn't locked out of any base class the way its magic-access restriction might imply.** No class ceiling stops a goblin player from building toward anything on the base-class list (`codex/lore/deck-building-rarity-and-classes.md` §Base classes). What actually holds most goblin builds back is the race's weak starting stat line (`codex/lore/deck-building-rarity-and-classes.md` §Per-race base stats), a hard climb from a low floor, not a hard wall. This is what Tatsuya works out for himself during Chapter 5's morning research, nobody's given the race a real shot because the base stats scare people off day one, not because the class options are actually closed to it.

This is exactly what makes Tatsuya's eventual spellcasting capability as a goblin, unlocked specifically through the Shiv bond and the Shaman's Veil path (see `codex/objects/call-of-the-bones-necklace.md`), a real, remarked-upon anomaly in-world rather than a background non-event, a goblin who can genuinely cast is not supposed to happen.

## Rarity ladder

A single color-coded rarity scale used consistently for both skills and items, and doubling as the card border color in the menu presentation below:

- **Common** — white/gray
- **Uncommon** — green
- **Rare** — blue
- **Legendary** — gold
- **World** — purple, reserved for World Quest rewards, globally unique, matches the "world-level item" concept: nerfed for competitive balance, but still matters even in ranked play.

## Presentation: cards and the blue box

Equipped items and known skills appear in Tatsuya's menu/blue-box UI as cards: name, rarity-colored border, the stat bonuses it grants, and description text that explicitly names any ability it unlocks, so an item and the skill it grants always visibly correspond on the page rather than being left implied. That's the "deck" the reader can actually see.

In VR, the card is not the object. The item is real: worn, held, used physically in the scene, the necklace's bones actually rattle at his throat, a blade is actually swung, Chaotic-TCG-style. The card is how the system represents the item to the player; it isn't what the item is in the world. Per the house style reminder in `codex/lore/five-disciplines-stat-system.md`, don't menu-dump every card on the page, surface a card only when Tatsuya is actually checking his loadout or something changes.

**Pickup requires a physical claim.** A dropped item sits in the world, visibly present, but isn't in a player's inventory automatically. It has to be physically walked over and touched, that's the action that actually converts it into a card in inventory. Nothing is pure abstraction, even loot pickup is something a player's character does in the scene, not a UI action layered on top of it.

**Player death penalty.** On death, a player has a chance to drop one item from their inventory, not the whole inventory, and the odds skew toward their better/rare items specifically rather than junk. Real, meaningful stakes tied to the seven-day death lock (see `codex/lore/preserved-misc-mechanics.md`), not just a respawn timer. **Exception:** race-roll and World Quest-origin bound items are exempt from this roll entirely, for Tatsuya specifically the Call of the Bones Necklace and the Gambler's Earring (see `codex/objects/call-of-the-bones-necklace.md` and `codex/objects/gamblers-earring.md`). Everything else he carries or wears, including future legendary-tier gear, stays at normal drop risk.

- **Creature/Hero cards** (narrative shorthand, not literally shown to the reader as cards for every NPC): name, race/class/path, the six Discipline+Energy stats, abilities (innate/activated/triggered), rarity from the ladder above.
- **Battlegear / items:** equipped gear (the Call of the Bones Necklace, later Warset pieces, other earned items) grants stat bonuses and unlocks abilities. Limited equip slots keep loadouts meaningful.
- **Skills:** played for damage, buffs, direct effects, or to trigger a Gamble. Some require winning a Discipline or Fortune Challenge to land.
- Competitive matches (see `codex/lore/competitive-pvp-and-esports-structure.md`) are where the deck-building layer is most visible on the page: players bring their earned kit in alongside their base class, and world-level items are nerfed for balance but still matter.
