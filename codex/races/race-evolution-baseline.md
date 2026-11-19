# Race Evolution Baseline

One row per playable race. Base races and their abilities come from the race files. The Goblin line (Goblin, Hobgoblin, Shiv Goblin) is CANON. Every other evolution is a PROPOSAL, kept to one or two steps, so the story has something to point at when a non-goblin evolves. Nothing here is a D&D rules import; the D&D column only says which familiar race to picture.

Sources: `codex/races/*.md`, `codex/lore/playable-races-and-character-creation.md`, `codex/lore/companion-troop-system.md`, `codex/lore/goblin-clan-culture-and-feral-stigma.md`, `codex/locations/bloodhurst.md`.

## The table

| Race (base) | D&D baseline | Evolution path | Racial abilities | Home zone | Culture and gear flavour | Alignment lean |
|---|---|---|---|---|---|---|
| **Human** | Human | PROPOSAL: Human to **Paragon** (earned by a long run of trained Disciplines; Adaptable bonus doubles and a second Discipline counts as recently trained). Optional second step **Exemplar** (a title-bearing rank, mostly social). | Adaptable (bonus to the last trained Discipline). No resistances. Full magic access. | Lunarest | Court, guild halls, mixed mail and cloth, heraldry, the standard kit others are measured against. | Neutral, spread widely. Lawful in the capital. |
| **Elf** | Elf (High Elf is the rare variant) | PROPOSAL: Elf to **High Elf** (rare, already named in canon; Mana Sight reaches farther and reads spell tiers). Second step **Elder Elf** for very high Wisdom. | Mana Sight. Resists Storm, weak to Earth. Full magic access. | Azure Expanse | Peak domains, spellforged gear, bows and focus rings, long memory and law. | Lawful or neutral good, proud. Elves get special treatment under Lunarest's elven law. |
| **Dwarf** | Dwarf | PROPOSAL: Dwarf to **Runesmith Dwarf** (crafting yield bonus grows, rune slots on gear). Second step **Deepforged** (iron body: Iron Constitution also trims burst damage). | Iron Constitution. Resists Earth, weak to Storm. No magic at all; crafting edge instead. | Valefrost | Forges, hallmarked plate, hammers and axes, kin before coin. Carries bad infamy in Lunarest. | Lawful, neutral. |
| **Orc** | Orc | PROPOSAL: Orc to **Warborn Orc** (Unbroken covers the first two stuns). Second step **Warchief**, a leader form that buffs nearby allies. | Unbroken. Resists Poison, weak to Frost. Physical Arts by default. | Sunmarch | Banners, scarred plate and hide, heavy axes, honor through fighting. Wicked by reputation, not by nature. | Chaotic neutral, with any shading possible. |
| **Goblin** | Goblin | **CANON:** Goblin to **Hobgoblin** (leveling through combat without dying, or a direct blessing). Separate branch: Goblin to **Shiv Goblin** (necklace bond). PROPOSAL: a third, rough branch of the Hobgoblin, the **Bugbear** form (see below). | Scavenger's Eye, Nimble Hands. No resistances. Physical Arts by default. Infamous at start. | Myrrhwood (Black Lands, west) | Bone cord, mismatched shields, camp stew, scavenged blades, arcane tech tools. Only Thrash goblins may enter villages. | Chaotic neutral by reputation, honorable inside the clan. |
| **Beastfolk** | Tabaxi or Lycan flavour | PROPOSAL: Beastfolk to **Wildblood** (Enrage starts at 50% HP instead of 40%, stack cap stays tied to survival gear). Second step **Totem Bearer**, with a band of one animal spirit. | Predator's Instinct, Enrage (x12 under 40% HP). Resists Frost, weak to Fire. No magic at all. | Myrrhwood (kingdom side) | Organized kingdom, royal house, hide and claw weapons, hunt rights. Carries bad infamy in Lunarest. | Neutral, tribal loyalty over law. |
| **Drakekin** | Dragonborn | PROPOSAL: Drakekin to **Wyrmtouched** (Draconic Presence widens to a short fear aura). Second step **Dragonheart**, a lineage form. | Draconic Presence. Resists Fire, weak to Poison. Full magic access. | None (achievement race) | Scaled lineage, ancestral blades, rare and watched. Wicked by reputation, individuals vary. | Lawful or neutral, honor driven. |
| **Frostborn** | Goliath (frost kin) | PROPOSAL: Frostborn to **Rimeblooded** (Cold Endurance also gives a Frost aura on the body). Second step **Glacier Bound**. | Cold Endurance. Resists Frost, weak to Fire. Partial magic access, rune and elemental flavored. | Valefrost | Ice halls, rune furs, shared kingdom with the dwarves, endurance as virtue. | Lawful neutral. |

## The goblin line in detail

- **Goblin.** Base stats 4/4/2/7/9/4. Weakest floor in the game, highest Fortune.
- **Hobgoblin (CANON).** Taller, human height, markings, speech without contractions. Goblin abilities evolve (Goblin Gas becomes Toxic Breath). Ru is blessed from level 1 to level 5 directly by Shiv. Zinka is level 7, Wyx level 25, Sevish level 80. Stat deltas are PROPOSAL: about +2 Courage, +2 Power, +1 Wisdom, with Fortune unchanged.
- **Shiv Goblin (CANON).** Reached only by bonding with the Call of the Bones Necklace. Tatsuya grows taller, gains a pale lock in his hair, red eyes, and Shaman's Veil. The mark is legible to older goblins on sight.
- **Bugbear form (PROPOSAL).** A Hobgoblin who evolves down the brute road: bigger frame, long arms, heavy hide, Power over Speed, fewer words. Feral clans produce more of them than Thrash does, and the stigma follows them.

## Rules of evolution in this world

1. **Evolution is earned, not selected.** Nobody picks it at creation. It costs time, risk or a bond.
2. **Three triggers exist:** a level threshold reached without dying, a world quest or item bond, and a direct blessing from a patron or spirit. [PROPOSAL for the grouping, CANON for each example]
3. **Who grants it.** A god or spirit blesses; the world only unlocks it. Shiv's blessing is the goblin example: a fading ash spirit gave Ru his Hobgoblin step, and the Necklace gave Tatsuya the Shiv Goblin one.
4. **A blessing is rare and personal.** Shiv's gift to Ru was a one time act. It does not loosen the normal path for anyone else.
5. **Players and NPCs differ.** Players follow the stat sheet and the quest. NPC evolution is slower and quieter, and NPCs mostly do not know how it works (Sevish and Wyx do not know the mechanics). Troops evolve through the rank up system in `codex/lore/companion-troop-system.md`.
6. **Gold tag NPCs do not level** while they are not troops, so their evolved rank is a fixed point, not a goal.
7. **Evolution changes the race entry, not just looks.** It changes stats, one or two abilities, and how other people read you. It does not remove the base race's weaknesses outright.
8. **Culture reacts.** Evolved forms get recognized on sight. A Shiv Goblin is read as Shiv marked by old goblins; a Hobgoblin is read as a leader.
9. **Evolutions stay short.** At most two steps per race in this baseline. More would be a story decision, not a default.
10. **Reputation does not evolve with the body.** Goblin, Orc, Beastfolk and Drakekin carry their stigma into the evolved form unless the player works it down through Karma and Affiliation.
