# D&D Class Mapping (master file)

**Status:** research and design proposal, codex only. Nothing here is on the page. Built for the author of Goblin Smashing from the repo (Physical Arts, Books, Mastery, races, archetypes, the ability audit) plus public D&D sources. Every D&D fact below is paraphrased, never copied. Later entries in `outline/canon-ledger.md` override earlier ones, and canon beats anything proposed here.

**Tags used in every file of this set**
- **[SRC]** a claim about D&D, Pathfinder or another game, with its URL.
- **[CANON]** a claim about HGO that is already in the repo (file named).
- **[PROPOSAL]** anything invented here. Names are easy to rename.

**The set (all new files, nothing existing was edited)**
- This file: ground rules, bands, the conversion table, the thirteen class overview, the archetype crosswalk, the cast crosswalk.
- `codex/combat/dnd-classes-barbarian-fighter-monk.md`
- `codex/combat/dnd-classes-rogue-ranger-paladin.md`
- `codex/lore/dnd-classes-cleric-druid-bard.md`
- `codex/lore/dnd-classes-sorcerer-warlock-wizard-artificer.md`
- `codex/lore/dnd-older-editions-crosswalk.md` (3.5, Pathfinder 1e and 2e)
- `codex/lore/dnd-skills-and-stats-mapping.md`
- `codex/lore/dnd-racial-abilities-mapping.md`
- `codex/characters/goblin-baseline-skill-kit.md`

Build on, do not repeat: `outline/research/ability-system-audit.md` (rules brief) and `outline/research/dnd-martial-ability-research.md` (Barbarian, Battle Master, Bladesinger, Swashbuckler, Kensei and the Wyx and Sevish palettes). Where this set reuses their names (Reckless Swing, Momentum Chain, Reaping Arc, Bloodlust, Earthsplitter, Afterimage Cut, Winding Step, Defiant Whirl, Dance of Blades, Tempo, Pain Is Proof, Challenging Howl) it says so.

---

## 1. The ground rule: six categories and nothing else

The author's rule: no ability may exist outside these.

| # | Category | What it is | Canon anchor |
|---|---|---|---|
| 1 | **Physical Art** | A technique in one of five Ways (Fist, Spear, Blade, Axe, Bow), tier 1 to 7, paid in SP, with a cooldown. Includes perception arts (Veil-Pierce Gaze) and the clan-tagged Thrash technique (Challenging Howl). | [CANON] `codex/combat/physical-arts-overview.md` |
| 2 | **Spell** | An effect from one of eight Books (Embers, Frost, Tempest, Stone, Tides, Radiance, Veil, Arcane), tier 1 to 8, paid in MP, needs Wisdom 18 to open (or a bond like Shiv's). | [CANON] `codex/magic/overview.md` |
| 3 | **Passive** | No activation cost. Must have a trigger and a limiter. Amplifies or reacts to what the owner already does. | [CANON] audit section 2.4; Gambler's Gambit, Bone Surge, Whispers of Shiv, Momentum Charm |
| 4 | **Racial ability** | Granted by the race entry. Includes racial skills that cost SP (Goblin Gas, Goblin Flare, Toxic Breath) and racial passives (Scavenger's Eye, Unbroken). | [CANON] `codex/races/` |
| 5 | **Mastery** | The 1 to 10 meter, grown by use, gates tier access, unlocks teaching at 10. Not a passive and not purchasable. | [CANON] `codex/lore/mastery-system.md` |
| 6 | **Item** | Gear, battle items and consumables whose card names the ability they unlock (Call of the Bones Necklace, Gambler's Earring, Goblin Gadget Belt, Doppelganger's Band, elixirs). | [CANON] `codex/lore/deck-building-rarity-and-classes.md` |

Not combat abilities, so outside the rule but still part of a character: **Titles** (`[THE FIRST DESCENDANT OF SHIV]`), **Posts** (jobs from the Support Tree), **supplementary classes** (Tinker, Field Medic, Scout), **Codex Entries** (skills, feats and gear, introduced two to four per major arc). [CANON] `codex/lore/leveling-and-progression.md`, `codex/lore/merchant-license-auction-and-jobs.md`.

**Canon rules every conversion in this set obeys**
1. Physical Arts are SP, Power and Speed driven, not Wisdom gated; spells are MP and scale with Wisdom. [CANON] `codex/lore/hp-sp-mp-resource-pools.md`.
2. Abilities have real cooldowns and drain pools. No spamming. [CANON] same file.
3. A passive has no cost, so its power comes from a trigger, a condition, a roll or a drawback, and anything that boosts without a ceiling needs a limiter. [CANON] audit 2.4.
4. Stat points: 2 per level, each stat caps at 75, no ability-score bumps. [CANON] `codex/lore/leveling-and-progression.md`.
5. Elemental and Toxin resistance come from race baseline plus gear, not from disciplines. Goblins are flat zero. Silence has no resistance by design and is a hard counter that stops spells and Physical Arts for anyone without a melee weapon already drawn. [CANON] `codex/lore/secondary-combat-stats.md`, `codex/crafting/debuffs-and-resistances.md`.
6. No creature summoning in Tatsuya's build (conjured daggers, the Doppelganger's Band and small constructs are allowed). [CANON] `codex/subplots/tatsuya-trap-bomber-brigand-archetype.md`. Other archetypes (Wildcaller, Windrider) keep pets and summons.
7. Resurrection is not a class feature: 72 hour death lock, Cathedrals, and the Staff of the Mist God (once per seven days). [CANON] `codex/lore/preserved-misc-mechanics.md`, `codex/subplots/tatsuya-trap-bomber-brigand-archetype.md`.
8. NPCs run reactive AI and parse in-character speech; gold tags have long memory and almost never flip hostile. So no mind control on NPCs and no memory edits. [CANON] `codex/lore/npc-tag-system.md`.
9. Mastery gates tier: about 25 percent opens half a Book's tiers, tiers 6 and 8 stay locked under about 75 percent. [CANON] `codex/lore/mastery-system.md`.
10. Hushveil, a field spell, drains mana continuously while up and does not tell friend from foe. [CANON] `codex/magic/book-of-tempest.md`.

---

## 2. Conventions used in every table

### 2.1 Tier meaning [CANON]
Physical Arts: T1 one basic technique (three per Way as the starting kit); T2 to 3 refinement and small chains; T4 to 5 real combos; T6 signature recognised on sight; T7 battlefield altering and rare. Spells: T1 to 2 single small effect; T3 to 4 area or duration control; T5 to 6 chained effects; T7 reshapes the field; T8 the ceiling. (Sources: `codex/combat/physical-arts-overview.md`, `codex/magic/overview.md`.)

### 2.2 Cost and cooldown bands [PROPOSAL, extends audit gaps G3 and G4]
Cost is a share of the pool being spent (SP for arts, MP for spells) at the level the tier is normally met.

| Code | Cost band | Typical tiers | Canon anchor |
|---|---|---|---|
| **C1** | 10 to 20 percent | T1 to 2 | Goblin Flare is 5 of 25 SP (20 percent) |
| **C2** | 20 to 35 percent | T2 to 4 | proposed Momentum Chain 30 percent |
| **C3** | 40 to 80 percent | T4 to 6 | Ancient Bone Flame Barrage is 25 of 32 MP (78 percent); Goblin Gas is 10 of 25 SP (40 percent) |
| **C4** | 80 to 100 percent, or part paid in HP or Energy, or a once-per-fight charge | T6 to 8 | Bone Surge Reflect crashes Energy to 1 |

| Code | Cooldown band | Typical tiers | Canon anchor |
|---|---|---|---|
| **D1** | 6 to 20 s | T1 to 2 | Rune Priming retry is 6 s |
| **D2** | 30 to 60 s | T3 to 4 | Goblin Gas, Goblin Flare and Hushveil are all 30 s |
| **D3** | 90 to 180 s | T5 to 6 | proposed Earthsplitter 3 minutes |
| **D4** | once per fight (about 5 minutes) or once per real day | T7 to 8 | Gambler's Gambit once a day; Phoenix Elixir 24 hours |

A low-level pool is small, so early racial skills run hot (Goblin Gas is C3 at level 1). Bands describe the level where the tier is normally reached.

### 2.3 Rarity [PROPOSAL, from `outline/research/martial-teaching-and-mastery-proposal.md` section 1.1]
Ladder is canon: Common, Uncommon, Rare, Legendary, World (World is reserved for World Quest rewards and is never taught). The page also prints **UNIQUE** (Gambler's Gambit); its place on the ladder is open, so this set never uses it.

| Entry | Common | Uncommon | Rare | Legendary |
|---|---|---|---|---|
| Physical Art | T1 to 2 | T3 | T4 to 5 | T6 to 7 |
| Spell | T1 to 2 | T3 to 4 | T5 to 6 | T7 to 8 |
| Passive | baseline habit | useful on one build | class defining | capstone only |

One step up is allowed for a unique mechanic. Label a skill on the page only where rarity matters.

### 2.4 Level ladder [PROPOSAL, anchored on canon data points]
D&D class level to HGO character level. Anchors: Tatsuya level 8 uses a Tier 5 spell through setup and Amplify; Arya level 10 to 11 cannot cast Tier 6 (needs about 75 percent Mastery); Wyx is level 25 with a Tier 5 Rare; Sevish is level 80 with a Tier 6 Rare and a held back Tier 7; level 150 is the first major milestone. [CANON] audit section 1.5, `codex/characters/thrash-siblings-ability-lists.md`, `codex/lore/leveling-and-progression.md`.

| D&D level | HGO level | Expected top Art | Expected top spell | Advanced class slot |
|---|---|---|---|---|
| 1 | 1 | T1 | T1 | none |
| 2 | 5 | T1 to 2 | T2 | none |
| 3 to 4 | 10 | T3 | T3 (Hushveil sits here) | **Slot I: advanced class chosen** (the Support Tree also opens at 10) |
| 5 to 8 | 25 | T4 to 5 | T4 (T5 only by setup and Amplify) | **Slot II** |
| 9 to 12 | 50 | T5 | T5 to 6 (needs about 75 percent Mastery for 6) | **Slot III** |
| 13 to 16 | 80 | T6 (T7 held back) | T6 to 7 | **Slot IV** |
| 17 to 20 | 100 to 150 | T7 | T7 to 8 | capstone near the level 150 milestone |

Tier is capped by points and Mastery, not by a level number. The ladder says what to expect, not what is allowed.

### 2.5 Words for class layers [PROPOSAL, anchored on canon]
- **Base class** = a D&D class. Canon calls them base classes (Spellforger, Ironbreaker and so on) and uses "knight-to-paladin promotion" as its example of a promotion. [CANON] `codex/lore/deck-building-rarity-and-classes.md`, `codex/lore/playable-races-and-character-creation.md`.
- **Advanced class** = a D&D subclass. Canon already says Tatsuya's Arcane Bomber is a "unique advanced class" and the page shows Wyx as "Blade Dancer" and Sevish as "Berserker".
- **Supplementary class** = the Support Tree (level 10). Gives no stat points.
- **Hybrid/Custom** = D&D multiclassing: gear driven, with the Mastery gate stopping a freshly mixed caster from using tiers they have only unlocked on paper. [CANON] `codex/lore/mastery-system.md`.

### 2.6 Resource key
SP = stamina (Physical Arts, racial skills, item abilities). MP = mana (spells, Rune Priming). "SP+MP" = hybrid, mana pushed into the body or weapon, which is the northern idea of **Reinforced Arts** (canon flavour for Physical Arts). [CANON] `codex/combat/physical-arts-overview.md`.

### 2.7 Race access gate
Casting needs the race to allow it and Wisdom 18. Humans, Elves and Drakekin are open; Frostborn partial; Orcs and Goblins restricted (a hard climb from a low Wisdom, not a wall); Beastfolk and Dwarves fully locked. [CANON] `codex/races/overview.md`. Every caster class below inherits this. A locked race can still use runed gear and potions (items).

---

## 3. D&D features that break our rules, and the fix

D&D facts here are [SRC] from the SRD 5.1 pages named in section 9. Every fix is a [PROPOSAL] unless a canon anchor is shown.

| # | D&D feature | Why it breaks | Fix in our system |
|---|---|---|---|
| 1 | **Short rest recharge** (Second Wind, Action Surge, Channel Divinity, warlock slots, ki). A short rest is at least an hour of light activity. [SRC] https://5thsrd.org/adventuring/resting/ | HGO has no rests as a mechanic; it has cooldowns, "once per day after combat" (Gambler's Gambit) and "per encounter" (Orc Unbroken). | Convert to a cooldown band (D1 to D3). "Per fight" resets after 60 s out of combat. Never an hour. |
| 2 | **Long rest recharge** (rage uses, spell slots, Lay on Hands pool). A long rest is 8 hours, once per 24 hours. [SRC] same page | Sleeping does not refill the player; Rested Travel is only a 50 percent XP buff. | "Once per real day" (D4), the same clock as Phoenix Elixir (24 h) and Bone Surge Amplify (once a day). HP comes back through HP Regen (Courage plus Energy), healing spells and potions; Meditation refills SP and MP slowly, never HP. |
| 3 | **Spell slots by level**, upcasting, slot conversion (Font of Magic). | HGO has one MP pool and tiers. | One MP pool; cost band by tier; upcasting becomes **Amplify** (extra MP to push above the unlocked tier, real cost and real risk). [CANON] `codex/magic/overview.md` |
| 4 | **Prepared spell lists** and spellbooks. [SRC] https://5thsrd.org/character/classes/wizard/ | HGO casters know a Book's tree (points plus Mastery) and carry skill cards. | Known spells per Book. Optional **skill deck**: a limit on equipped active cards (suggest 4 at L1, 6 at L10, 8 at L25, 10 at L50, 12 at L80). Copying costs become manuals and library time (Wisdom plus Speed joint check). [CANON] `codex/lore/five-disciplines-stat-system.md` |
| 5 | **Cantrips at will.** | "No spamming, no infinite use." | Tier 1 spells at band C1/D1 (cheap, short cooldown). Only Meditation and passives are truly free. |
| 6 | **Concentration** (a Constitution save when hit; one spell at a time). [SRC] https://5thsrd.org/spellcasting/casting_a_spell/ | No turn structure, no Constitution stat. | Sustained spells **drain MP every second** while up (Stormwall precedent). Stun, Silence or heavy CC ends them. One field spell at a time. Dual-casting stays the canon Wisdom gated spike. |
| 7 | **Action, bonus action, reaction** economy. | Real time combat. | A short global cooldown (about 1 s) between skills. A **reaction art** fires on a trigger (a miss, a hit taken) with its own cooldown, one per 6 s. Parry Riposte (Blade T1) is the canon example. |
| 8 | **Opportunity attacks**, Disengage, Dash. | No turns, no threat ranges. | Reach counters are a Spear and Blade passive (**Guard Check**); Dash and Disengage become movement arts (Winding Step, Wind Step, Cunning Footwork). |
| 9 | **Advantage and disadvantage** (roll two d20, keep one). | No d20 on the page; resolution is narrative with numbers only when a gamble is live. [CANON] `codex/lore/five-disciplines-stat-system.md` | Accuracy, Crit Rate and Evasion modifiers (10 to 20 percent) and short states (**Exposed**, **Guarded**). Never both at once. A Fortune chain is the goblin way to "advantage". |
| 10 | **Saving throws against a DC.** [SRC] https://5thsrd.org/rules/abilities/saving_throws/ | HGO resolves debuffs against source strength, racial baseline and gear. | Use the secondary resist stats (Physical CC Resist, Mental Resist, Curse Resist, Magic Evasion). A large level gap can bypass CC resist. [CANON] `codex/crafting/debuffs-and-resistances.md`. Full table in `codex/lore/dnd-skills-and-stats-mapping.md`. |
| 11 | **Hit Dice, healing surges.** | HP is 50 plus 3 per level; HP Regen is a stat. | HP Regen, healing spells, potions, Phoenix style items. |
| 12 | **Temporary hit points.** | One HP pool only. | A **Ward** (barrier that absorbs, then breaks); Warding Circle is the canon Radiance model; wards do not stack, the strongest applies. |
| 13 | **Ability Score Improvement and feats at levels 4, 8, 12.** [SRC] https://5thsrd.org/character/classes/barbarian/ | Stat points are 2 per level. | No ASI. D&D feats become **feat Codex Entries** (canon lists feats as a Codex Entry type), granted two to four per major arc. |
| 14 | **Proficiency bonus** (+2 to +6 on everything trained). | HGO uses a 1 to 10 Mastery meter and tiers. | "Proficient" = the skill is unlocked and Mastery 1 or more. Scaling = Mastery rank plus tier. No flat bonus on every roll. |
| 15 | **Expertise, Jack of All Trades, Reliable Talent.** | Same. | **Specialty** (small passive on one non-combat skill), **Many Hands** (half Mastery on an untrained skill), **Steady Craft** (a floor on a trained skill's outcome at Mastery 8 or more). |
| 16 | **Sneak Attack dice.** [SRC] https://5thsrd.org/character/classes/rogue/ | Dice damage scaling by level; needs advantage or an adjacent ally. | **Opening Strike**, a passive: bonus damage on a target that is unaware, flanked or already engaged by an ally; once per target per 8 s; scales with Mastery, not level. |
| 17 | **Rage** (uses per day, damage and resistance, ends if you do not fight). [SRC] https://5thsrd.org/character/classes/barbarian/ | Uses per day; stacks with Beastfolk Enrage (up to x12) if left alone. | **Fury Stance**, an SP drain art with a crash (Winded) when it ends. It does not stack with Enrage: take the higher bonus. |
| 18 | **Exhaustion levels** (Berserker Frenzy). | No exhaustion track. | **Winded** (SP Regen halved, Physical Evasion down, 15 to 30 s) and **Nauseous** (canon: fumble chance and lower stamina regen). |
| 19 | **Wild Shape and Polymorph** (swap to a beast's hit points). [SRC] https://5thsrd.org/character/classes/druid/ | No polymorph in canon; HP pool swap and gear drop are clumsy in full dive. | **Beast Aspect**, a Tier 3 to 6 spell in the nearest Book by element. A body overlay for 60 to 120 s, stat tweaks, bite and claw arts; no HP swap, no gear loss, Silence still applies, no casting except its own arts. |
| 20 | **Familiars, companions, summons.** | Canon: no creature summoning for Tatsuya only; Windrider has pets and Wildcaller has beast summons. | Player pets: one slot, level with the owner, kills credit the owner (the troop rule). Tatsuya may conjure daggers, use the Band, and field small constructs; never creatures. [CANON] `codex/subplots/tatsuya-trap-bomber-brigand-archetype.md` |
| 21 | **Teleportation, planar travel, flight.** | Players hold no waypoints; travel is physical (a ship crossing is four to five days); no flight in canon. | Blinks of 6 m or less are Tier 3 and up (Gale Step is the canon mobility spell). Long range teleport and planar features are cut or become a Legendary relic effect. Flight becomes a long leap or glide art. |
| 22 | **Revivify, Raise Dead, Death Ward, Relentless Rage.** | 72 hour lock; resurrection only by relic. | No player resurrection spell. "Cheat death" features become **Stand Again** (once per fight, refresh 24 h, then an Energy crash). |
| 23 | **Charm, Dominate, Suggestion, memory edits.** | Reactive NPC AI, Affiliation, gold tags with long memory. | Mobs only: a short **Daze** or **Calm**. Players: Mental states (Fear) resisted by Courage. No NPC mind control; no memory edit. |
| 24 | **Illusion doubles and Mirror Image.** | Canon: any duplicate trick is the Doppelganger's Band. | Item only (the Band, 60 MP to activate). Afterimage **hits** (Wyx) are arts, visual only. |
| 25 | **Divination oracles** (Augury, Commune, Portent). | The world is real; no free answers. | Perception Radius effects and Codex hints. Portent becomes **Foresight Marks** (see Wizard). |
| 26 | **Languages** (Druidic, Thieves' Cant). | No language mechanic; speech register matters instead. | Flavour: **Brigand Sign** and **Wild Tongue** are in-world habits with no mechanics. [CANON] `style-guide/race-dialect-and-voice.md` |
| 27 | **Alignment detection** (Divine Sense, Detect Evil). | Two axes exist: Karma (Blood Tinted) and the patron alignment tree. | **Karma Sense** reads nameplates and creature types, nothing more. |
| 28 | **Spell components V, S, M.** | Silence is a hard counter by design. | V is covered by Silence. S needs a free hand. M becomes a focus or a consumable. **Subtle Spell cannot bypass Silence.** |
| 29 | **Death saves.** | 72 hour lock instead. | None. |
| 30 | **Attunement.** | Eleven equip slots and bound items instead. | Slots are the limiter. |
| 31 | **Flat immunities** (poison, charm, fear). | Resists are race baseline plus gear plus Courage; goblins have none. | Timed buff states or capped partial resists, never permanent immunity. |
| 32 | **Random tables** (Wild Magic Surge). | No GM table. | A small Fortune weighted effect table fired by **Amplify**, the canon gamble. |
| 33 | **Rituals.** | Long casts exist as prep. | Prep actions like **Rune Priming** (roll required, mana each attempt, 6 s retry). |
| 34 | **Mounts** (Cavalier). | Mounts are not established in canon (the Haya EB is a real scooter). | Open question; see Fighter file. |
| 35 | **Psionics.** | No psionic category in canon. | Folded into Book of the Arcane force spells or Reinforced Arts. |

---

## 4. The twelve core classes plus the Artificer

D&D columns are [SRC]: hit die, saving throws and casting stat from https://5thsrd.org/character/classes/{class}/ (the Artificer from https://dnd5e.wikidot.com/artificer). Everything else is [PROPOSAL] except where [CANON] is marked. Every spellcaster class collapses onto one casting stat in HGO, **Wisdom**, because there is no Intelligence or Charisma [CANON] `codex/lore/five-disciplines-stat-system.md`. Their differences come from Book, from the second stat they lean on (Courage for presence, Fortune for gambles, Speed for finesse) and from the advanced class.

### 4.1 Identity table

| D&D class [SRC] | Our archetype and in-world name | Ways | Books | Resource | Race note |
|---|---|---|---|---|---|
| **Barbarian** (d12; Str, Con saves; no casting) | **Berserker** [CANON archetype: melee DPS, rage and cleave]. In-world: Berserker. | Axe first; Fist and Spear | none | SP, then Energy crash | Open. Beastfolk (Enrage), Orc (Unbroken) and Hobgoblin (Sevish) are the natural fits. |
| **Bard** (d8; Dex, Cha; Cha casting) | **Songwright** [NEW]. In-world: Songwright. | Blade (Swords line), Fist (dance) | Radiance, Tempest, Arcane, Veil | MP plus SP | Casting gate applies. |
| **Cleric** (d8; Wis, Cha; Wis casting) | **Warden** [CANON archetype: support and cleric, healing and buffs]. In-world: Warden of a patron or domain. | Blade, Axe, light Spear for the war lines | Radiance plus the domain's Book | MP (SP for rites) | Casting gate. The healer-class cleanse rule applies. |
| **Druid** (d8; Int, Wis; Wis casting) | **Wildcaller** [CANON archetype: summoner and druid, beast summons and terrain control]. In-world: Wildcaller. | Fist, Spear (Aspect forms) | Tempest, Tides, Stone, Frost, Radiance, Embers | MP; SP upkeep for Aspects | Casting gate. |
| **Fighter** (d10; Str, Con; no casting) | **Vanguard** [NEW umbrella]. Specialises into **Ironbreaker** (shield, taunt), **Berserker** (axe, rage) or **Windrider** (bow). In-world: Vanguard. | All five | none (Runeblade: Arcane) | SP | Open to every race. |
| **Monk** (d8; Str, Dex; no casting) | **Stillfist** [NEW]. In-world: Stillfist. | Fist; Blade or Spear for the Kensei line | none (Elemental Palm optional) | SP (ki is SP) | Open to every race, including the magic locked ones. Silence caution in section 3 row 28 and the Monk file. |
| **Paladin** (d10; Wis, Cha; Cha casting) | **Paladin** [CANON word: the codex uses "knight-to-paladin promotion"]. A promotion from Ironbreaker or Warden. In-world: Paladin, by Oath. | Blade, Spear, Axe, shield | Radiance (Veil for the Hollow Oath) | SP plus MP | Oath arts need no casting; Radiance spells need Wisdom 18. |
| **Ranger** (d10; Str, Dex; Wis casting) | **Windrider** [CANON archetype: archer and hunter, ranged DPS and pets]. In-world: Windrider. | Bow first; Spear, Blade | Tempest, Stone, Tides, Radiance (all light) | SP; MP optional | Most Windriders never open a Book. |
| **Rogue** (d8; Dex, Int; no casting) | **Shadowveil** [CANON archetype: rogue and assassin, stealth and crits]. In-world: Shadowveil. | Blade (daggers), Bow, Fist | none (Veilhand: Arcane, Veil) | SP | Goblins are natural Shadowveils (Nimble Hands). |
| **Sorcerer** (d6; Con, Cha; Cha casting) | **Surgeborn** [NEW label inside Spellforger]. In-world: Surgeborn. | none | by origin: Embers, Frost, Tempest, Veil, Radiance, Arcane | MP; Amplify is the core | Casting gate. Drakekin suit Wyrmblood. |
| **Warlock** (d8; Wis, Cha; Cha casting, short pact slots) | **Veilbound** [NEW]. In-world: Veilbound. | Blade for the Hexblade line | Veil, Arcane | MP | A bond can bypass the Wisdom gate (Shiv's necklace is the canon case). |
| **Wizard** (d6; Int, Wis; Int casting) | **Spellforger** [CANON archetype: mage, elemental burst and crowd control]. In-world: Spellforger. | Blade for Bladesinging | all eight | MP | Casting gate. Elves, Humans, Drakekin first. |
| **Artificer** (d8; Con, Int; Int casting) [SRC] https://dnd5e.wikidot.com/artificer | **Gearwright** [NEW]. Tatsuya's **Arcane Bomber** is the unique advanced class beside it. In-world: Gearwright. | Blade or none | Arcane, Embers, Stone | MP plus SP plus items | Dwarves and Beastfolk can wield **runed gear** made by others but cannot cast. |

### 4.2 Signature passives and racial-style flavour

Passives follow the rule of section 1: no cost, a trigger, a limiter. Names are [PROPOSAL].

| Class | Signature passives (limiter in brackets) | Racial-style flavour and warnings |
|---|---|---|
| **Berserker** | **Bare Hide** (evasion while the chest slot is bare or Common hide; gone in heavy chest armour). **Gut Warning** (a cue before a telegraphed area hit; not while Deafened). **Cleaver's Luck** (Crit Multiplier up, Crit Rate untouched; two handed only). **Stand Again** (once per fight, refresh 24 h, then Energy crash). | Enrage and Fury Stance never stack. Orc Unbroken already resists the first stagger, so do not also hand Orcs an extra stagger passive. |
| **Songwright** | **Many Hands** (half Mastery on skills you have not trained). **Steady Chorus** (allies near you gain Fear and daze resist from Courage; one aura at a time). **Resting Song** (camp regen bonus while stationary). **Borrowed Verse** (learn up to two spells from another Book, tier 5 or under, Mastery required). | A goblin Songwright leans on Rude-song humour and Rally; Elves and Humans get the stage presence. |
| **Warden** | **Healer's Surplus** (heals add a small bonus; extra only when the target is under half HP). **Warding Hand** (healing another also wards you for a short time). **Blessed Edge** (once per 6 s a weapon hit adds the patron's element). | Domains map onto the five patrons only as a working match; see the Cleric file. |
| **Wildcaller** | **Trail Foot** (difficult terrain costs no speed). **Wild Tongue** (flavour only). **Clear Blood** (a timed Toxin resist after Meditation; not in combat). | Beastfolk cannot cast, so Beastfolk Wildcallers are pet and Aspect-art builds. Tatsuya never summons creatures; Wildcallers do. |
| **Vanguard** | **Catch Breath** (self heal art, D3). **Shake It Off** (once per day, auto-resist one failed CC). **Keen Edge** (Crit Rate up with the chosen Way's weapon only). **Way Stance** passives replace Fighting Style. | The Way T3 chains are the canon "Extra Attack": Momentum Chain, Flowing Edge, Serpent's Reach, Volley Draw, Silent Three Fang. |
| **Stillfist** | **Light Footing** (evasion with no chest armour). **Feather Drop** (smaller fall damage; reaction). **Slip the Blast** (half damage on a failed dodge of an area hit). **Clear Head** (cleanse Fear once per 60 s). **Clean Body** (timed Toxin resist after Meditation). | Goblin Stillfists have the speed and no Toxin resist; Clean Body is a buff, not an immunity. |
| **Paladin** | **Oath Aura** (allies near you gain CC and Mental Resist from your Courage; the highest aura only). **Fearless Aura** (Fear resist). **Radiant Brand** (a Blade, Spear or Axe art with an MP surcharge, Reinforced Arts style). **Healing Hands** (a Radiance T2 spell). | Chaotic goblins can swear Oaths, but Karma matters: breaking one flips the nameplate to Blood Tinted. |
| **Windrider** | **Quarry Lore** (information on a creature type, not damage). **Trail Sense** (Perception Radius up in terrain you know). **Quarry Mark** (first hit on a marked target each 8 s adds damage). | Pets level with the owner and credit kills to the owner. Beastfolk and Hobgoblin scouts (Zinka) fit. |
| **Shadowveil** | **Opening Strike** (once per target per 8 s; unaware, flanked or engaged by an ally). **Half-Step** (reaction, D2). **Slip the Blast.** **Specialty** (one non-combat skill). **Lucky Break** (capstone: once per day turn one miss into a hit, Fortune scaled). | **Nimble Hands** is the goblin version of a rogue's mage-hand trick: pick pockets through doors, with Karma and Affiliation costs and no player pickpocketing in green zones. |
| **Surgeborn** | **Born Affinity** (small Magic AP bonus in the origin's Book only). **Spell Riders** (see section 3 row 4; riders are bought per spell like Hushveil's Silence upgrade). **Amplify Control** (your Amplify has a lower failure rate, never zero). | Elf passive "spells cost less mana" is the Elf differential; do not give it to Surgeborn of other races. |
| **Veilbound** | **Kill Ward** (a short Ward after a kill; once per 6 s). **Veil Gifts** (upgrade branches on Veil Bolt, the way Hushveil upgrades to Silence). **Bound Weapon** (a conjured dagger or blade, not a creature). | The Veil is rare and bottlenecks on teachers; a bond (a spirit, a haunting, a debt) is the other route. Shiv is the canon spirit. [CANON] `codex/magic/book-of-the-veil.md` |
| **Spellforger** | **Mana Recall** (once per fight regain a slice of MP; D4). **Codex of Spells** (manual learning by the Wisdom plus Speed joint check). **Book Savant** (faster Mastery in the chosen Book, not extra power). | Elf Mana Sight is the racial; Arya is the canon Tempest Spellforger. |
| **Gearwright** | **Tinker's Touch** (the Support Tree Tinker supplement). **Infusions** (gear upgrades through Enchanting and Rune Priming; limited by equip slots). **Quick Mind** (a short assist to an ally's Challenge; once per fight). | The goblin trade company and the turret are Gearwright material; Tatsuya's Gadget Belt is the personal version. |

---

## 5. Where the existing HGO archetypes sit in the D&D picture

[CANON] archetype descriptions from `codex/lore/deck-building-rarity-and-classes.md`. Examples are canon characters from the codex and the ledger.

| HGO archetype or page label | Closest D&D classes | Best fitting subclasses | Canon examples | Notes |
|---|---|---|---|---|
| **Spellforger** (mage, elemental burst and crowd control) | Wizard, Sorcerer | Evocation, War Magic, Storm Sorcery, Bladesinging (hybrid) | Arya (L10 Elf, Tempest), Dosuke AI (a unique Spellforger), Eren's stolen build, Spellweaver_Lyn (Elf, L14) | Wisdom 18 gate. "Spellforger, never mage" is a ledger rule. |
| **Ironbreaker** (tank, shield and taunt) | Fighter (defender), Paladin, Barbarian (Bear line), Cleric (War, Forge), Artificer (Armorer) | Cavalier, Banneret, Crown and Devotion Oaths, Ancestral Guardian, Armorer | Rian (Human tank and shot-caller, L13), Ru (frontal spearman wall) | Block Rate exists only with a shield. |
| **Shadowveil** (rogue and assassin, stealth and crits) | Rogue, Monk (Shadow), Ranger (Gloom Stalker) | Assassin, Thief, Scout, Phantom | The Shadowveils in the Thornwatch broadcast, the only class that could have slipped antidotes to the poisoned Aogiri leader | Canon ties Shadowveil to poison and antidotes, which is the Assassin's poisoner's kit. |
| **Windrider** (archer and hunter, ranged DPS and pets) | Ranger, Fighter (Arcane Archer) | Hunter, Beast Master, Gloom Stalker, Drakewarden | Wyx's Bow note in the Way file is stale; she is Blade | Pets are canon here. |
| **Warden** (support and cleric, healing and buffs) | Cleric, Bard, Paladin (Redemption), Monk (Mercy), Druid (Dreams) | Life, Peace, Order, Light | The Church of Seranis healers | Cleanses come only from healer classes or towns, and cost something. |
| **Wildcaller** (summoner and druid, beast summons and terrain control) | Druid, Ranger (Beast Master), Warlock (Chain), Artificer (Battle Smith) | Shepherd, Moon, Spores, Wildfire | Ryo Tachibana (off-meta Wildcaller) | Tatsuya is the one build barred from creature summons. |
| **Berserker** (melee DPS, rage and cleave) | Barbarian, Fighter (Champion) | Berserker, Totem, Zealot, Beast | Sevish (L80 Hobgoblin, Axe), Pac_Pac (Beastfolk tank and brawler) | Enrage plus Fury Stance never multiply. |
| **Hybrid/Custom** (gear driven multiclassing) | Multiclassing, Eldritch Knight, Rune Knight, Magus (PF1) | Runeblade line, Psi Warrior merged in | the off-meta builds | The Mastery gate stops paper-only unlocks. |
| **Arcane Bomber** (Tatsuya's unique advanced class; the file name still says Trap Bomber Brigand) | Artificer (Alchemist, Artillerist), Rogue (Thief, Arcane Trickster flavour), Warlock (Hexblade curse, Fiend luck), Wizard (Evocation), PF1 Alchemist bombs | see Gearwright and Veilbound | Tatsuya, Level 8 Shiv Goblin | Amplifier: low raw damage multiplied by stacked debuffs. Control, stack, ignite, finish. Not a healer, not a tank, not a hard CC caster. |
| **Blade Dancer** (page label for Wyx, L25) | Bard (Swords), Rogue (Swashbuckler), Wizard (Bladesinging), Fighter (Echo Knight), Monk (Kensei) | Echo Knight is the cleanest match for her afterimage hits | Wyx Thrash (martial only) | Dual sabres, Way of the Blade. Her echoes are arts, not spells. |
| **Enchanter and support** (role label) | Bard, Artificer, Cleric (Order), Wizard (Enchantment) | Eloquence, Alchemist | Joss (Beastfolk, L12) | Beastfolk cannot cast; Joss's enchants must come from items and crafting. This is a canon wrinkle, see section 10. |
| **Scout** (role label) | Rogue (Scout), Ranger | Scout, Gloom Stalker | Zinka (Hobgoblin, L7), Kesh | Zinka carries Toxic Breath. |

---

## 6. Cast crosswalk (canon characters in the D&D picture)

[CANON] facts from `codex/characters/`, `codex/lore/companion-troop-system.md` and `outline/canon-ledger.md`. The D&D analog column is [PROPOSAL] and only a lens for the writer.

| Character | Race and level | Canon label | Nearest D&D lens | Kit category check |
|---|---|---|---|---|
| **Tatsuya (Nykri)** | Shiv Goblin, L8 | Arcane Bomber (unique advanced class). Pseudo caster, enchanter style. | Artificer (Alchemist for elixirs and poison, Artillerist for bombs and the future turret) with a Warlock bond (Hexblade's Curse is the stacking mark; the Fiend's luck rider is Fortune) and a Rogue Arcane Trickster hand (Nimble Hands is a mage-hand trick without the spell). | Goblin Gas and Shiv-Touched Flare (racial skills, SP). Rune Priming (a Veil or Arcane prep spell, MP, roll required, 6 s retry). Call of Command (granted by Whispers of Shiv). Bone Surge (item passive). Gambler's Gambit (unique passive from the Mystery Box). Whispers of Shiv (passive). Ancient Bone Flame Barrage (Tier 5 spell on the Chapter 11 page). Everything fits a category. |
| **Arya** | Elf, L10 to 11 | Spellforger, Tempest | Wizard (Evocation) crossed with Storm Sorcery; control caster. | Static Lash, Tempest Fan, Storm Shear, Stormwall, Hushveil (all spells, MP). |
| **Pac_Pac** | Beastfolk | Tank and brawler | Barbarian (Berserker or Zealot's death-defying rage) with a Fighter's shield habits. | Predator's Instinct and Enrage (racials); the rest is Physical Arts. Magic locked. |
| **Ru** | Hobgoblin, L5 | Frontal spearman, vanguard | Fighter (Cavalier's marking, Banneret's rally, a shield art from rare gear). | Toxic Breath (evolved racial skill). Way of the Spear or Fist (the Fist file calls Ru's path Fist; the companion file calls him a spearman). |
| **Zinka** | Hobgoblin, L7 | Scout | Rogue (Scout). | Toxic Breath; scout arts. |
| **Drosh** | Hobgoblin lieutenant | Disciplined, tattooed | Monk (Open Hand with a Scout's eye). | Silent Three Fang (Fist T2 to 3), Veil-Pierce Gaze (Fist T4 to 5). |
| **Wyx Thrash** | Hobgoblin, L25 | Blade Dancer, gold tag, martial only | Echo Knight (afterimage hits) with Swashbuckler footwork and Bladesinger poise, but no magic. | Afterimage Cut, Winding Step, Defiant Whirl, Dance of Blades (Rare), Challenging Howl (taunt), Tempo (passive); Toxic Breath listed, never used. |
| **Sevish Thrash** | Hobgoblin, L80 | Berserker, gold tag, martial only | Barbarian (Path of the Berserker) with a Zealot's honour. | Reckless Swing, Momentum Chain, Reaping Arc, Bloodlust, Challenging Howl (immobilise), Earthsplitter (Rare), Pain Is Proof (Rare passive). |
| **Rian** | Human, L13 | Frontline tank, shot-caller | Fighter (Banneret) or Paladin (Crown Oath). | Physical Arts and shield. |
| **Talo** | Dwarf, L12 | Bruiser | Barbarian (Battlerager). | Dwarf Iron Constitution; resists the gas. |
| **Spellweaver_Lyn** | Elf, L14 | Mage | Wizard. | Spells. |
| **Joss** | Beastfolk, L12 | Enchanter and support | Artificer, Bard (Eloquence) or Cleric (Order). | Enchants through crafting and the Doppelganger's Band (an item). See section 10, row 7. |

---

## 7. New names proposed (all [PROPOSAL], easy to rename)

Canon archetype names are single coined words (Spellforger, Ironbreaker, Shadowveil, Windrider, Warden, Wildcaller, Berserker). The additions follow that pattern.

| Name | Fills which D&D gap | Why a new name |
|---|---|---|
| **Vanguard** | Fighter | Canon has a tank and a rage DPS and an archer, but no weapon master who is none of them (Battle Master, Champion, Banneret). |
| **Stillfist** | Monk | Way of the Fist exists but no archetype names its master. |
| **Songwright** | Bard | No performer class; ties to Fame, Loop and Hearthfire streaming culture. |
| **Veilbound** | Warlock | The Book of the Veil says it finds casters through a bond, a haunting or a debt. That is the warlock shape. |
| **Surgeborn** | Sorcerer | Canon says battlefield-taught casters land in Book of the Arcane; instinct casters need a lane inside Spellforger. |
| **Gearwright** | Artificer | The goblin trade company, the turret and the Gadget Belt need a crafted gadget caster beside Tatsuya's unique Arcane Bomber. |

Advanced class names in the subclass files follow the same pattern (two coined words or "Warden of X"). They are suggestions; the author can replace any of them.

---

## 8. Famous subclass shortlist (full tables are in the class files)

Per [SRC] https://dnd5e.wikidot.com class pages and https://5thsrd.org class pages: SRD 5.1 itself carries one subclass per class (Berserker, College of Lore, Life Domain, Circle of the Land, Champion, Way of the Open Hand, Oath of Devotion, Hunter, Thief, Draconic Bloodline, the Fiend, School of Evocation). The Player's Handbook, Xanathar's Guide, Tasha's Cauldron and others add the rest. The class files cover every official subclass listed on the wikidot class pages.

| Class | The famous ones | Where the full table is |
|---|---|---|
| Barbarian | Berserker, Totem Warrior, Zealot | `codex/combat/dnd-classes-barbarian-fighter-monk.md` |
| Fighter | Champion, Battle Master, Eldritch Knight | same |
| Monk | Open Hand, Shadow, Four Elements | same |
| Rogue | Thief, Assassin, Arcane Trickster, Swashbuckler | `codex/combat/dnd-classes-rogue-ranger-paladin.md` |
| Ranger | Hunter, Beast Master, Gloom Stalker | same |
| Paladin | Devotion, Vengeance, Ancients | same |
| Cleric | Life, War, Trickery | `codex/lore/dnd-classes-cleric-druid-bard.md` |
| Druid | Land, Moon, Spores | same |
| Bard | Lore, Valor, Swords | same |
| Sorcerer | Draconic, Wild Magic, Storm | `codex/lore/dnd-classes-sorcerer-warlock-wizard-artificer.md` |
| Warlock | Fiend, Great Old One, Hexblade | same |
| Wizard | Evocation, Bladesinging, Necromancy | same |
| Artificer | Alchemist, Artillerist | same |

Older editions (3.5 prestige classes, Tome of Battle maneuvers, Pathfinder Alchemist, Gunslinger, Magus, Kineticist, Witch and others) are in `codex/lore/dnd-older-editions-crosswalk.md`.

---

## 9. Sources

All fetched during this task unless marked.

- SRD 5.1 class pages (hit die, saves, features, SRD subclass): https://5thsrd.org/character/classes/barbarian/ , /bard/ , /cleric/ , /druid/ , /fighter/ , /monk/ , /paladin/ , /ranger/ , /rogue/ , /sorcerer/ , /warlock/ , /wizard/ (same path prefix).
- SRD 5.1 rules: https://5thsrd.org/rules/abilities/ability_checks/ , https://5thsrd.org/rules/abilities/saving_throws/ , https://5thsrd.org/adventuring/resting/ , https://5thsrd.org/spellcasting/casting_a_spell/ , https://5thsrd.org/character/backgrounds/
- SRD licensing: https://www.dndbeyond.com/resources/1781-systems-reference-document-srd (SRD 5.1 is available under CC-BY-4.0 and OGL 1.0a; SRD 5.2 under CC-BY-4.0 only and without the Artificer).
- Subclass feature pages (one per subclass, named in the class files): https://dnd5e.wikidot.com/{class}:{subclass}
- Subclass lists with sources: https://dnd5e.wikidot.com/barbarian , /fighter , /monk , /rogue , /ranger , /paladin , /cleric , /druid , /bard , /sorcerer , /warlock , /wizard , /artificer
- Feat list: https://www.aidedd.org/feat-dnd5/
- Artificer: https://dnd5e.wikidot.com/artificer
- Earlier research in this repo: `outline/research/ability-system-audit.md`, `outline/research/dnd-martial-ability-research.md`, `outline/research/martial-teaching-and-mastery-proposal.md`

---

## 10. Conflicts with canon, and how they were resolved

Canon wins every time. Rows are ranked by how much they could change the page.

| # | Conflict | Resolution |
|---|---|---|
| 1 | The brief says a few players start with a Newcomer Mystery Box instead of a role. The later ledger entry (L255) says HGO hands the box to every new player as a welcome gift. | Ledger wins. Everyone gets the box. The role pick is a separate step, and Tatsuya's glitch skipped it, which is why his sheet held only the racial kit and the box. |
| 2 | **Beastfolk are locked out of all magic** [CANON], yet Joss (Beastfolk) is the party's enchanter and support. | Not resolved here. Suggested reading: enchanting is an item and crafting skill (the Enchanting profession, the Doppelganger's Band), not casting. Needs an author ruling. |
| 3 | The Wisdom 18 gate means Charisma casters (Bard, Sorcerer, Warlock, Paladin) cannot exist without a Wisdom investment. | All casting is Wisdom. The Veilbound bond route (Shiv's necklace) and the Paladin's non-casting Oath arts are the two ways around the gate. |
| 4 | The Fist Way has no weapon, and Silence disables Physical Arts for anyone without a melee weapon already drawn. This hits Stillfists and the hand-to-hand Tatsuya. | Proposal: a Fist weapon (knuckles, wraps with a weapon tag) counts as drawn. Needs an author ruling. |
| 5 | Canon says any duplicate trick is the Doppelganger's Band. D&D has Mirror Image, Invoke Duplicity, Illusory Self, Echo Knight, Manifest Echo. | Doubles are item-only. Wyx's afterimage **hits** stay as arts because they are strikes, not copies. |
| 6 | `codex/combat/way-of-the-bow.md` calls Bow "Wyx's category" and `codex/objects/call-of-the-bones-necklace.md` gives her daggers. | Ledger and page win: Wyx is Way of the Blade, dual sabres. The two files are stale (already flagged in the audit). |
| 7 | Goblins are not locked from any base class [CANON], but the Wisdom floor is 2. | All thirteen classes are open to a goblin in principle. Casting classes are a hard climb or need a bond. Martial classes are the default. |
| 8 | Ru's Way: the Fist file says Fist, the companion file says spearman. | Kit file treats Fist as the weaponless default and Spear as the Hobgoblin's drilled weapon. |
| 9 | "Arcane Bomber" versus the file name "trap-bomber-brigand". | The ledger adopts the name Arcane Bomber. "Brigand" stays as a self-description. |
| 10 | The audit says never use UNIQUE or Legendary for an NPC ability unless the author opens that question. | This set uses only Common to Legendary for player-facing entries, never UNIQUE, and never gives an NPC a Legendary. |
| 11 | Mounts and flight are not established. | Cavalier and wing features are held as open questions or converted to leaps. |
| 12 | The Elf passive "spells cost less mana" is meant to stay an Elf differential. | Not copied to Surgeborn or other casters. |
| 13 | Hobgoblin has no race file; its evolution gate is not stated. | Level 5 is proposed from Ru (1 to 5) and Zinka (a Hobgoblin at 7). |
| 14 | Goblin resistances are deliberately flat. | PF2 heritages that grant resistances appear only as rare-variant roll ideas in the racial file. |

**Open questions for the author (ranked)**
1. Approve or rename the six new archetype names (Vanguard, Stillfist, Songwright, Veilbound, Surgeborn, Gearwright).
2. Confirm the advanced class gate at level 10 and the four slots at 10, 25, 50 and 80.
3. Rule on Fist weapons and Silence (conflict 4).
4. Rule on Joss and enchanting (conflict 2).
5. Decide whether mounts and flight exist.
6. Decide whether to cap equipped skill cards (the skill deck idea).
