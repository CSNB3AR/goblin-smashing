# NPC Tag System

A visible on-screen tag lets a player tell where they stand with any NPC at a glance, introduced on the page in Chapter 3 (Sevish and Wyx's gold tags).

## Facts

- **White** — ally/friendly. Goblins read other goblins of their own clan as white by default (Tatsuya, playing a goblin, sees Bloodhurst's own camp this way). A human player would likely see the same camp as yellow instead, tag color is relationship- and species-dependent, not a fixed universal read.
- **Yellow** — neutral, conditional, can turn hostile depending on the player's own behavior.
- **Red** — enemy. Goblins of a rival or feral clan read red to a Thrash-clan goblin, see `codex/lore/goblin-clan-culture-and-feral-stigma.md`.
- **Gold** — world-boss-tier or otherwise quest-critical/important NPC. Sevish and Wyx Thrash both carry gold tags. Gold tags essentially never go hostile, except under real provocation, an attack inside a settlement, or a player reckless enough to strike one directly. If a gold tag does flip hostile, it's never just that one NPC, it's whatever faction stands behind them, short of something as extreme as a clean assassination.
- **Yellow tags and below can die permanently.** An NPC's death means their file is gone, no respawn, real stakes for any fight involving a named or tagged NPC, not just Tatsuya's own player-death penalty (see `codex/lore/preserved-misc-mechanics.md`, seven-day death lock).
- **A generic role-title nameplate signals a disposable, mob-tier NPC; a proper name signals someone significant.** "Thrash Clan Enforcer" versus "Sevish Thrash" or "Wyx Thrash" is the tell, independent of tag color, a reusable convention for the reader to learn to read at a glance.
- **Blue is a separate axis: it always means player, never NPC.** White/yellow/red/gold are all relationship-dependent NPC reads (per the note above, the same NPC can show a different color to a different viewer). Blue doesn't work that way, it's a fixed identifier layered on top of the relationship system, not a fifth relationship state. Any other player Tatsuya encounters shows blue regardless of standing; an empty field of white/yellow/gold with zero blue tags is itself a signal, confirmation no other players are nearby.
