# Affiliation & Reputation System

**Status:** New mechanic, distinct from and layered on top of the already-locked Karma/Alignment axis (see `codex/lore/preserved-misc-mechanics.md`). The clan meter first lands on the page in Chapter 8, but an individual NPC's meter shows up much earlier: Wyx's ticks 45% to 52% in Chapter 6, because she finds him interesting from the first meeting (author-stated).

## Two separate axes, do not conflate them

- **Karma/Alignment (already locked).** A single, global standing. Purely punitive: killing players outside sanctioned PvP, or mistreating NPCs and a region's people (see `codex/lore/player-owned-economy-and-living-world-npcs.md`), shifts it negative and visibly flips a nameplate white to red, "Blood Tinted." One number, applies everywhere, never goes up on its own, only down through real wrongdoing.
- **Affiliation (new, this file).** A per-faction, per-region standing meter, 0-100, that rises or falls independently for every distinct faction a player has contact with. Thrash clan's read on Tatsuya and, say, a Lunarest merchant guild's read on him are two entirely separate numbers. Rises through in-character behavior that specific faction actually values, not a global reputation score.

## Bands

| Band | Range | Reads as |
|---|---|---|
| Hostile | below 0 | Actively opposed, may attack on sight depending on faction. |
| Wary-Neutral | 0-24 | Tolerated, not trusted. Access is conditional, favors aren't owed. |
| Friendly | 25-49 | Real goodwill, minor favors and discounts open up. |
| Trusted | 50-79 | Genuine standing, real requests get taken seriously, some restricted access opens. |
| Allied | 80-100 | Full standing, the faction treats the player as one of their own. |

## Starting values and the floor (author-stated)

- **Nobody starts below 20%.** The lowest a starting affiliation can be is about 20%, because anything under 20% starts hitting into the negative pools, and once it reaches 0 and goes below, people start to hate you. Going negative takes real wrongdoing: a character builds negative influence in towns and cities through their own actions.
- **Goblins among their own start high.** A goblin who spawns into a goblin camp typically starts with the goblin NPCs at about 40 to 50%, and their actions can spike it from there. Right now Tatsuya sits at about 40 to 50% with Sevish and the Thrash clan, and how he talks to them and how valuable he proves is what builds it.
- **Goblins among humans do not start better.** A goblin dealing with a human in Lunarest starts low, around the 20% floor, and that includes shopkeepers, who give worse deals when affiliation is bad.
- Low affiliation is felt in prices and access, not just attitude. The bands below describe where a meter can go, and the floor above is where it starts.

## Racial starting modifiers

A character's race sets a real, felt starting offset with certain factions before they've done anything at all, distinct from anything they earn. Goblins in particular start with a visible penalty in human-dominated regions like Lunarest, a mechanical expression of the already-locked feral stigma (see `codex/lore/goblin-clan-culture-and-feral-stigma.md`), a low but non-hostile read, not an arrest trigger, just a visibly suspicious one. The same goblin starts at a real, positive baseline with Myrrhwood's own goblin clans instead, before any individual reputation is built at all.

## Landing on the page, Chapter 8: Thrash clan

Tatsuya's own standing with the Thrash clan specifically starts around **45%** (the normal 40 to 50% a goblin has with a goblin camp), consistent with "ally of Thrash" being real and already warm but not yet earned or settled, a status handed to him for one act. It moves through in-character behavior, choosing his words the way an actual outsider earning trust would, not through simply being tactically correct. A visible tick up (never a jump straight to Allied in one scene) is the mechanical payoff for Chapter 8's assault and the diplomacy that gets him the room to attempt it in the first place.

## How this actually moves: the reactive NPC layer underneath it

Affiliation isn't a flat formula, it moves because the NPC on the other end is actually parsing what the player says and does, per the reactive-AI system now formalized in `codex/lore/npc-tag-system.md`. This is also why register matters, not just intent: speaking to an NPC in metagame/gamer-slang doesn't register as real input and won't move the meter, speaking in a way that NPC's own worldview can process does. See `style-guide/race-dialect-and-voice.md` for the per-race voice rules this depends on.

## Allied band, earned vs. unearned (Act Three forward-plot)

Affiliation being at Allied with a given faction is not the same thing as an unearned title. Tatsuya's "elder" address, granted the moment the Call of the Bones Necklace bond took (see `codex/lore/goblin-clan-culture-and-feral-stigma.md`), is real but unearned, and already on the page by Chapter 8. The distinct, later payoff is his Affiliation with the Thrash clan collectively, not just one companion's individual reading, actually crossing into Allied band, at which point Sevish and Wyx start treating the same title as genuinely earned rather than granted. Same word, two different, explicitly distinguished states, see `outline/act-three-myrrhwood-expedition.md`.

## Rare edge case: NPC personal interest, not a formal system

At the very top of Affiliation, a small number of AI-driven, adaptive NPCs (flagged as such elsewhere, see `codex/lore/npc-tag-system.md`) can start registering something closer to genuine personal interest in a specific player, not just faction trust. This isn't a systemized "romance mechanic" available to every player, it's a rare, character-specific extension of how an advanced NPC reads someone it's actually come to know well. Wyx's own growing interest in Tatsuya (see `codex/characters/wyx-thrash.md`) is the one confirmed instance of this so far, kept to narrative texture, not a UI-facing mechanic.

## Cross-references

- `codex/lore/preserved-misc-mechanics.md` — the separate, already-locked Karma/Alignment axis.
- `codex/lore/goblin-clan-culture-and-feral-stigma.md` — the racial starting-modifier basis for goblins specifically.
- `codex/lore/npc-tag-system.md` — the visible tag-color system this sits alongside, and the reactive-NPC-AI system that actually drives this meter; tag color and Affiliation band are related but not identical, a Friendly-band NPC still reads by the existing white/yellow/red/gold rules, Affiliation is the number underneath that color.
- `style-guide/race-dialect-and-voice.md` — the roleplay-register requirement this depends on.
- `codex/lore/mastery-system.md` — a third, separate progression axis. Affiliation is who trusts you, Mastery is what you're actually capable of, don't conflate the two.

## Fame (Hearthfire canon)

**Fame** sits beside karma and Affiliation as a third public-facing meter: how widely a player is known, as opposed to how NPCs feel about them (Affiliation) or how their actions read morally (karma). **Goblins start infamous**, and Beastfolk, goblins and dwarves carry bad infamy in Lunarest, while elves get special treatment under an elven law (see `codex/lore/lunarest-royal-court.md`). Fame carries into Node Wars standing and seasonal standing (see `codex/lore/hearthfire-expansion-and-seasons.md`). NPCs react to a player's fame and race as lived reality, never as news to them (see `style-guide/craft-rules.md`).
