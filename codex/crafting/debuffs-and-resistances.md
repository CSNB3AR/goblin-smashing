# Debuffs & Resistances Framework

**Status:** New system, extends the already-established per-race elemental resistance baseline (see `codex/races/`) to a real, gear/consumable-facing framework.

## Core rule

A debuff (poisoned, silenced, slowed, blinded, burning, chilled, and so on, several already dramatized on the page, see `codex/objects/call-of-the-bones-necklace.md` and `codex/magic/book-of-tempest.md`'s Hushveil) always resolves against three things in order: the source's applied strength, the target's racial resistance baseline (see each file under `codex/races/`), and any additional resistance granted by gear, food, or a crafted consumable. A racial resistance of zero, like Goblin's deliberately flat, unspecialized baseline, means gear and consumables are the only lever a goblin player has for shoring up a weak spot, a real, felt build decision rather than a stat that quietly protects itself.

## Resistance sourcing

Crafted resistance almost always traces back to a regional material (see `codex/materials/overview.md`): Rimeiron-forged gear carries innate Frost resistance, Sunforged Iron gear runs the same way for Fire, and so on. This is deliberate, it ties the debuff/resistance layer directly into the same regional-materials system rather than existing as a separate, disconnected mechanic.

## Debuff categories (representative, not exhaustive)

| Category | Example | Notes |
|---|---|---|
| **Elemental** | Burning (Fire), Chilled (Frost), Shocked | Resisted by the matching elemental resistance stat. Stacks additively; Burning specifically can be triggered by an ignited gas cloud, see the Goblin Gas + Flare combo, `codex/lore/preserved-misc-mechanics.md`. |
| **Toxin** | Poisoned (Goblin Gas family, `codex/lore/preserved-misc-mechanics.md`) | Resisted by a dedicated Toxin resistance stat, distinct from elemental, ties to Alchemy-crafted antidotes. Stacks up to 4x (already dramatized, Chapter 3), each added stack raising tick damage and, at max stack, applying **Nauseous** (a real fumble chance plus reduced stamina regeneration, its own minor debuff riding on top of Toxin). |
| **Sensory: Silence** | Hushveil (advanced), `codex/magic/book-of-tempest.md` | **Full lock, not magic-only:** disables spellcasting *and* Physical Arts for anyone without a melee weapon already drawn, plus genuine auditory loss in full-dive VR, no footsteps, no attack cues. This is the locked, correct version, a narrower "spells only" reading of Silence is not canon. No dedicated racial resistance exists for this category, deliberately, it's meant to stay a genuine hard counter. |
| **Sensory: Deafen** | New, not yet dramatized on the page | Distinct from Silence: mutes and distorts ambient audio without necessarily locking abilities, footsteps, incoming-attack cues, ally voice-pings, and even system notification chimes all come through muffled, delayed, or dropped entirely. In full-dive VR this reads as a genuine sensory violation, the game's realness is part of what a Deafen effect is attacking. Mechanically: reduces sound-based detection range (a real problem against stealth/ambush play), raises the odds of getting caught flat-footed by an audio-timed dodge, garbles voice comms if a party's using them. Partially resisted by high Wisdom (situational awareness) or crafted ear-slot gear (see `codex/crafting/recipes-spirit-line.md`'s Echoing Bone Helm). |
| **Physical** | Slowed, Stunned, Rooted | Partially resisted by Power/Courage at high investment, not a clean elemental-style resistance stat. Slowed can stack multiplicatively from a world-tier presence specifically (Flamonta, already dramatized Chapter 7, `[STATUS: SLOWED x4]`), distinct from and worse than a normal Slowed application. |
| **Mental** | Fear, Curse of the Bones | Fear resisted by Courage. Curse-family debuffs (a gradual Fortune drain, thematically an "anti-gambler's" effect) are the one category a high-Fortune character can partially self-mitigate by rolling a resist check against their own stat, consistent with Fortune's established role as a proc/luck-resistance stat as well as an offensive one. |

## Interaction notes

- **Gas + ignite** stacks Burning on top of an existing Poison application, the core goblin gas-combat identity already established Chapter 3, not a new interaction.
- **Silence + Deafen together** is a real worst-case for a Spirit Magic caster specifically, locked out of every ability and unable to hear the fight happening around them at the same time. Two separate debuffs, not one combined effect, so they have to be applied by two separate sources.
- **A Toxin stack pushing a target into Nauseous** is a real self-sabotage risk for a gas-heavy build (goblins specifically), part of why gas-users lean on a disciple or party support to cover them mid-application rather than soloing a gas combo blind.

## Cross-references

- `codex/materials/overview.md` — where resistance-granting materials come from.
- `codex/crafting/overview.md` — how resistance gets crafted into gear in the first place.
- `codex/races/` — each race's baseline resistance profile.
