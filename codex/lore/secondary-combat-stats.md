# Secondary Combat Stats

Derived from the six primary disciplines (see `codex/lore/five-disciplines-stat-system.md`). These are not investable points — a player never spends a discipline point into a secondary stat directly. They are output values, calculated from primary discipline investment plus equipped gear, and they are what combat actually runs on under the hood.

**Display format:** Unlike primary disciplines, secondary stats show as flat derived numbers, not an invested-plus-gear split.

```
[PHYSICAL AP: 84] [MAGIC AP: 61]
[PHYSICAL EVASION: 43] [MAGIC EVASION: 29]
[CRIT RATE: 18%] [CRIT MULTIPLIER: 1.6x]
[PHYSICAL CC RESIST: 12%] [MENTAL RESIST: 8%]
```

In story, these surface only when competitive stakes are genuinely live: a real fight's HUD, a character review screen, or a specific in-chapter callout when a threshold or resistance is actively relevant. Never dumped as a narrator stat block — always filtered through Tatsuya's HUD perception per the existing house style (see `style-guide/craft-rules.md`).

---

## Offensive

| Secondary Stat | Derives from | Governs |
|---|---|---|
| **Physical AP** | Power (primary), Speed (partial) | Melee and physical damage output. The core offensive number for Berserker, Ironbreaker, and Shadowveil builds. Speed's partial contribution reflects that faster strikes carry their own hit weight. |
| **Magic AP** | Wisdom | Spell damage output. Already implied in the Five Disciplines ("Wisdom scales magic damage"); this formalizes it as a named secondary stat. Tatsuya's Ancient Bone Flame Barrage output runs on this number. |
| **Ranged AP** | Speed (primary), Power (partial) | Projectile and thrown damage — arrows, thrown items, thrown bombs. Speed is primary because ranged output depends on timing, arc, and release more than raw force. Windrider builds and Tatsuya's bomb kit both run here. |
| **Accuracy** | Speed + Wisdom (joint) | Whether attacks actually land against evasive targets. Speed covers reflexive aim tracking; Wisdom covers reading movement patterns ahead of the motion. Both matter. |
| **Crit Rate** | Fortune | Chance for a critical hit to proc. Already dramatized across chapters 1–8; this formalizes the governing stat. |
| **Crit Multiplier** | Fortune | How hard a crit hits when it procs. Higher Fortune increases both the frequency and the spike, not just one or the other. |
| **Armor Pierce** | Power | Reduces how much of the target's Physical Damage Reduction actually applies to an incoming hit. High-Power builds punch through tank builds; without Armor Pierce investment, a flat PDR absorbs the same amount regardless of raw AP. |

---

## Defensive

| Secondary Stat | Derives from | Governs |
|---|---|---|
| **Physical Evasion** | Speed | Dodge chance against melee and physical projectiles. Already dramatized; Speed governs reactive evasion timing. |
| **Magic Evasion** | Wisdom | Chance to analytically read a spell's path and move out of it before it lands. Not immunity — it's awareness, not magic nullification. |
| **Physical Damage Reduction** | Power + gear armor | Flat damage absorbed when a physical attack lands after evasion fails. The tank feel. Ironbreaker's primary defensive stat. |
| **Magic Resistance** | Wisdom + Courage | Reduces magic damage taken when Magic Evasion doesn't fully cover it. Distinct from evasion: this absorbs damage that already landed, not damage that was dodged. Courage contributes the mental fortitude component. |
| **Block Rate** | Power (shield equipped only) | Active block chance for shield builds. Zero without a shield equipped — this stat simply does not exist for unshielded characters. |

---

## Utility

| Secondary Stat | Derives from | Governs |
|---|---|---|
| **Movement Speed** | Speed | Literal character movement rate in the world. Speed is the sole driver. |
| **Initiative** | Speed + Fortune | Who acts first in a combat exchange. Speed is the reflex start; Fortune is the lucky break that lets a slower character catch an early window. |
| **Perception Radius** | Wisdom | Detection range for enemies, traps, and hidden items. Wisdom's analytical awareness extends the radius of what a character actively clocks without being told. |
| **HP Regen** | Courage + Energy | Out-of-combat HP recovery rate. Courage is the willpower to push through and recover; Energy is the raw pool that fuels the regeneration. |
| **SP Regen** | Speed + Energy | Stamina recovery rate between physical and item ability uses. Speed governs how fast the body resets from physical output; Energy is the fuel. |
| **MP Regen** | Wisdom + Energy | Mana recovery rate between casts. Wisdom governs the clarity and discipline of magical recovery; Energy is the raw pool. |

---

## Resistances

Connects directly to the debuff resolution framework in `codex/crafting/debuffs-and-resistances.md`. Every debuff resolves in order against: the source's applied strength, the target's racial baseline, and any gear or consumable bonus on top. Secondary stats are where those baselines and gear bonuses land mechanically.

| Secondary Stat | Derives from | Notes |
|---|---|---|
| **Physical CC Resistance** | Power + Courage | Partial resist on Stun, Knockback, Root, and Slow. The debuffs doc states these are "partially resisted by Power/Courage at high investment, not a clean elemental-style resistance stat" — this names that named stat formally. High investment in both disciplines moves the needle; neither alone covers the gap cleanly. |
| **Mental Resistance** | Courage | Resists Fear, panic, and despair effects. Already stated in the debuffs doc: "Fear resisted by Courage." |
| **Curse Resistance** | Fortune | Partial self-resist on curse-family and Fortune-drain debuffs. Already stated: high Fortune allows a resist check against the character's own stat. |
| **Elemental Resistance (Fire/Frost/Shock)** | Race baseline + gear | Not discipline-derived. Augmented by Rimeiron-forged gear (Frost), Sunforged Iron gear (Fire), and equivalent material-crafted items. See `codex/materials/overview.md` and each race file under `codex/races/`. |
| **Toxin Resistance** | Race baseline + gear (Alchemy) | Not discipline-derived. Goblins carry a flat zero racial baseline, making this a real, felt build decision — gear and Alchemy-crafted antidotes are the only lever. See `codex/crafting/debuffs-and-resistances.md`. |
| **Silence Resistance** | None — intentionally absent | The debuffs doc locks this explicitly: "No dedicated racial resistance exists for this category, deliberately — it's meant to stay a genuine hard counter." No gear or build path closes this gap either. |

---

## Enemy-Type Modifiers

Gear-derived, not discipline-derived. These do not exist as secondary stats in the same sense — they are gear affixes that apply conditionally depending on what the character is hitting.

| Modifier | Source | Notes |
|---|---|---|
| **Bonus vs. Creatures** | Gear | PvE damage modifier against monster types. Fortune affects clean-kill procs on top of this. |
| **Bonus vs. Players** | Gear (PvP-oriented builds) | Separate from the PvE creature bonus. A character has to invest in PvP-oriented gear to close the gap against players who have. |
| **Creature-type bonus** | Gear | Bonus damage vs. specific creature classes: beast, undead, humanoid, demihuman. Connects to the creature class files. |

---

## Cross-references

- `codex/lore/five-disciplines-stat-system.md` — the six primary disciplines these stats derive from.
- `codex/lore/hp-sp-mp-resource-pools.md` — HP, SP, and MP as distinct from the secondary regen stats above.
- `codex/crafting/debuffs-and-resistances.md` — the debuff resolution framework these resistances plug into.
- `codex/materials/overview.md` — regional materials that source elemental resistance gear.
- `codex/races/` — each race's baseline resistance profile.
