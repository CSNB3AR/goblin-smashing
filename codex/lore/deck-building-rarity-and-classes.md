# The Deck-Building Layer

Ties directly to Pillar 3 of `story/premise.md`: a player's permanent, earned inventory functions as their deck, and what they bring into a competitive match matters as much as their class. Never named as its direct inspiration (Chaotic TCG) on the page, described functionally only.

## Base classes / build paths

Background texture, world-building rather than something Tatsuya gets boxed into, his goblin kit (Physical Arts, Shaman's Veil, the Call of the Bones Necklace) stays its own thing. What other players and pro teams draw from: **Spellforger** (mage, elemental burst/crowd control), **Ironbreaker** (tank, shield and taunt), **Shadowveil** (rogue/assassin, stealth and crits), **Windrider** (archer/hunter, ranged DPS and pets), **Warden** (support/cleric, healing and buffs), **Wildcaller** (summoner/druid, beast summons and terrain control), **Berserker** (melee DPS, rage and cleave), and **Hybrid/Custom** (gear-driven multi-classing, consistent with the deck-building pillar, meta-breaking off-builds live here).

## Per-race stats, abilities, and resistances

Moved to `codex/races/`, one file per playable race, split out of the shared tables that used to live here. See `codex/races/overview.md` for the index and the magic-access summary across all eight races.

## Race/class magic-access restrictions

Not every race can freely learn every skill tree. See `codex/races/overview.md` for the current per-race breakdown (fully open, partial, restricted, or fully locked) and `codex/magic/overview.md` for the tier-1 Wisdom-18 threshold itself.

**Goblin specifically isn't locked out of any base class the way its magic-access restriction might imply.** No class ceiling stops a goblin player from building toward anything on the base-class list (§Base classes above). What actually holds most goblin builds back is the race's weak starting stat line (`codex/races/goblin.md`), a hard climb from a low floor, not a hard wall. This is what Tatsuya works out for himself during Chapter 5's morning research, nobody's given the race a real shot because the base stats scare people off day one, not because the class options are actually closed to it.

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
- Competitive matches (see `codex/pro-scene/tournaments-and-events.md`) are where the deck-building layer is most visible on the page: players bring their earned kit in alongside their base class, and world-level items are nerfed for balance but still matter.

**Where gear actually comes from.** PvE is the real source of the deck: crafted, farmed, and quest-earned gear built up outside ranked play. Player-crafted gear is the preferred competitive standard in PvP specifically because it's balanced and scales predictably, not because World-tier drops are weak, they're genuinely powerful, just nerfed for competitive balance the way the rarity ladder above already states. This is why a serious competitive build still runs mostly player-crafted pieces even once World-tier items are in reach.
