# Debuffs & Resistances Framework

**Status:** New system, extends the already-established per-race elemental resistance baseline (see `codex/races/`) to a real, gear/consumable-facing framework.

## Core rule

A debuff (poisoned, silenced, slowed, blinded, burning, chilled, and so on, several already dramatized on the page, see `codex/objects/call-of-the-bones-necklace.md` and `codex/magic/book-of-tempest.md`'s Hushveil) always resolves against three things in order: the source's applied strength, the target's racial resistance baseline (see each file under `codex/races/`), and any additional resistance granted by gear, food, or a crafted consumable. A racial resistance of zero, like Goblin's deliberately flat, unspecialized baseline, means gear and consumables are the only lever a goblin player has for shoring up a weak spot, a real, felt build decision rather than a stat that quietly protects itself.

## Resistance sourcing

Crafted resistance almost always traces back to a regional material (see `codex/materials/overview.md`): Rimeiron-forged gear carries innate Frost resistance, Sunforged Iron gear runs the same way for Fire, and so on. This is deliberate, it ties the debuff/resistance layer directly into the same regional-materials system rather than existing as a separate, disconnected mechanic.

## Debuff categories (representative, not exhaustive)

| Category | Example | Notes |
|---|---|---|
| **Elemental** | Burning, Chilled, Shocked | Resisted by the matching elemental resistance stat. |
| **Toxin** | Poisoned (Goblin Gas family) | Resisted by a dedicated Toxin resistance stat, distinct from elemental, ties to Alchemy-crafted antidotes. |
| **Sensory** | Silenced, Blinded, Deafened (Hushveil family) | No dedicated racial resistance exists yet for this category, deliberately, it's meant to stay a genuine hard counter rather than something a build can fully wall off. |
| **Physical** | Slowed, Stunned | Partially resisted by Power/Courage at high investment, not a clean elemental-style resistance stat. |

## Cross-references

- `codex/materials/overview.md` — where resistance-granting materials come from.
- `codex/crafting/overview.md` — how resistance gets crafted into gear in the first place.
- `codex/races/` — each race's baseline resistance profile.
