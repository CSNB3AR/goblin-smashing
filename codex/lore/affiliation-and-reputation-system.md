# Affiliation & Reputation System

**Status:** New mechanic, distinct from and layered on top of the already-locked Karma/Alignment axis (see `codex/lore/preserved-misc-mechanics.md`). First lands on the page in Chapter 8.

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

## Racial starting modifiers

A character's race sets a real, felt starting offset with certain factions before they've done anything at all, distinct from anything they earn. Goblins in particular start with a visible penalty in human-dominated regions like Lunarest, a mechanical expression of the already-locked feral stigma (see `codex/lore/goblin-clan-culture-and-feral-stigma.md`), a low but non-hostile read, not an arrest trigger, just a visibly suspicious one. The same goblin starts at a real, positive baseline with Myrrhwood's own goblin clans instead, before any individual reputation is built at all.

## Landing on the page, Chapter 8: Thrash clan

Tatsuya's own standing with the Thrash clan specifically starts around **10%**, low Wary-Neutral, consistent with "ally of Thrash" (granted Chapter 3) being real but early and unconsolidated, a status handed to him for one act, not yet a settled relationship. It moves through in-character behavior, choosing his words the way an actual outsider earning trust would, not through simply being tactically correct. A visible tick up (never a jump straight to Allied in one scene) is the mechanical payoff for Chapter 8's assault and the diplomacy that gets him the room to attempt it in the first place.

## How this actually moves: the reactive NPC layer underneath it

Affiliation isn't a flat formula, it moves because the NPC on the other end is actually parsing what the player says and does, per the reactive-AI system now formalized in `codex/lore/npc-tag-system.md`. This is also why register matters, not just intent: speaking to an NPC in metagame/gamer-slang doesn't register as real input and won't move the meter, speaking in a way that NPC's own worldview can process does. See `style-guide/race-dialect-and-voice.md` for the per-race voice rules this depends on.

## Cross-references

- `codex/lore/preserved-misc-mechanics.md` — the separate, already-locked Karma/Alignment axis.
- `codex/lore/goblin-clan-culture-and-feral-stigma.md` — the racial starting-modifier basis for goblins specifically.
- `codex/lore/npc-tag-system.md` — the visible tag-color system this sits alongside, and the reactive-NPC-AI system that actually drives this meter; tag color and Affiliation band are related but not identical, a Friendly-band NPC still reads by the existing white/yellow/red/gold rules, Affiliation is the number underneath that color.
- `style-guide/race-dialect-and-voice.md` — the roleplay-register requirement this depends on.
