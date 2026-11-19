# D&D Class Mapping (master file)

**Status:** design proposal, codex only. Nothing here is on the page. It lets the author reuse D&D class ideas without importing D&D rules. Tags: [CANON] already in the repo, [PROPOSAL] invented here (every name, tier and cost in the tables is a PROPOSAL and easy to rename), [SRC] D&D fact, paraphrased from SRD 5.1 (https://5thsrd.org/character/classes/ and https://dnd5e.wikidot.com/ class pages).

Companions: `codex/characters/goblin-baseline-skill-kit.md`, `codex/lore/five-disciplines-stat-system.md`, `codex/lore/secondary-combat-stats.md`, `codex/combat/physical-arts-overview.md`, `codex/magic/overview.md`, `codex/lore/mastery-system.md`.

---

## 1. Ground rules

**Every skill is exactly one of six things** [CANON]:

| Category | Rule |
|---|---|
| Physical Art | One of five Ways (Fist, Spear, Blade, Axe, Bow), tier 1 to 7, paid in SP, has a cooldown. |
| Spell | One of eight Books (Embers, Frost, Tempest, Stone, Tides, Radiance, Veil, Arcane), tier 1 to 8, paid in MP, needs Wisdom 18 (or a bond like Shiv's). |
| Passive | No cost. Must have a trigger and a limiter. |
| Racial ability | From the race entry. Racial skills may cost SP (Goblin Gas); racial passives are free. |
| Mastery | The 1 to 10 meter, grown by use. Gates tier access, unlocks teaching at 10. Never purchased. |
| Item | Gear and consumables whose card names the ability it grants. |

**Tiers** [CANON]: Art T1 single technique, T2 to 3 small chains, T4 to 5 real combos, T6 signature, T7 battlefield altering (practical ceiling). Spell T1 to 2 one small effect, T3 to 4 area or duration, T5 to 6 chained effects, T7 reshapes the field, T8 ceiling.

**Rarity ladder** [CANON]: Common, Uncommon, Rare, Legendary, World (World Quest rewards only, never taught). [PROPOSAL] mapping: Art T1 to 2 Common, T3 Uncommon, T4 to 5 Rare, T6 to 7 Legendary. Spell T1 to 2 Common, T3 to 4 Uncommon, T5 to 6 Rare, T7 to 8 Legendary. Passives: baseline habit Common, one build Uncommon, class defining Rare, capstone Legendary.

**Cost and cooldown bands** [PROPOSAL]: C1 10 to 20 percent of the pool, T1 to 2 (Goblin Flare, 5 of 25 SP). C2 20 to 35 percent, T2 to 4. C3 40 to 80 percent, T4 to 6 (Goblin Gas, 10 of 25 SP). C4 80 to 100 percent, or paid in HP or Energy, or once per fight, T6 to 8. Cooldowns: D1 6 to 20 s, D2 30 to 60 s (Gas, Flare, Hushveil are 30 s), D3 90 to 180 s, D4 once per fight or per day.

**Layers** [PROPOSAL, anchored on canon]: D&D class = base class. D&D subclass = advanced class (slots at levels 10, 25, 50, 80; Tatsuya's Arcane Bomber is the canon "unique advanced class"). Support Tree (level 10) = supplementary class, no stat points. Multiclassing = Hybrid/Custom, gear driven, held back by the Mastery gate.

**Resource key:** SP stamina (arts, racial skills). MP mana (spells). SP+MP is Reinforced Arts, mana pushed into body and weapon [CANON].

**Race gate** [CANON]: Humans, Elves, Drakekin open to casting; Frostborn partial; Orcs and Goblins restricted (a hard climb, not a wall); Beastfolk and Dwarves locked. Locked races use runed gear and potions (items).

---

## 2. The table: twelve core classes and main subclasses

Columns: D&D class and subclass, HGO archetype, Way or Book, resource, signature art or spell with tier, signature passive (limiter in brackets), rarity (signature / passive). Tiers are the tier the advanced class reaches around levels 10 to 50.

| D&D class, subclass | HGO archetype | Way or Book | Res. | Signature (tier) | Passive (limiter) | Rarity |
|---|---|---|---|---|---|---|
| **Barbarian**, Berserker | Berserker (Frenzy) [CANON archetype] | Axe | SP | Reckless Swing (T3) | Bare Hide (evasion; bare or Common chest only) | Unc / Unc |
| Barbarian, Totem Warrior | Berserker (Totem) | Axe, Fist | SP | Totem Stance (T4), one damage type halved 10 s | Gut Warning (cue before area hit; not while Deafened) | Rare / Unc |
| Barbarian, Zealot | Berserker (Oathfury) | Axe | SP | Reaping Arc (T4) | Stand Again (survive a killing blow at 1 HP; once per fight) | Rare / Rare |
| Barbarian, Wild Heart | Berserker (Beast) | Fist, Axe | SP | Hide Rend (T3) | Predator's Lunge (first strike after a sprint; 8 s) | Unc / Unc |
| **Bard**, Lore | Songwright (Lorebinder) | Arcane | MP | Discord (T3, debuff) | Many Hands (half Mastery on untrained skills) | Unc / Unc |
| Bard, Valor | Songwright (Battle) | Blade; Radiance | SP+MP | Rallying Verse (T3) | Steady Chorus (Fear and daze resist from Courage; one aura) | Unc / Unc |
| Bard, Swords | Songwright (Blade) | Blade | SP | Flourish Chain (T3) | Resting Song (small HP Regen after Meditation; out of combat) | Unc / Com |
| Bard, Eloquence | Songwright (Silvertongue) | Radiance | MP | Calm (T3, mobs only; Daze) | Silver Tongue (NPC register bonus; no effect on players) | Unc / Unc |
| **Cleric**, Life | Warden (Life) [CANON archetype] | Radiance | MP | Mending Light (T2 heal) | Healer's Surplus (extra only if target under half HP) | Com / Unc |
| Cleric, Light | Warden (Dawn) | Radiance, Embers | MP | Dawnflare (T4) | Warding Hand (healing another also wards you; short) | Unc / Unc |
| Cleric, War | Warden (War) | Blade, Axe; Radiance | SP+MP | Battle Blessing (T3 buff) | Blessed Edge (art adds light damage; one art per 8 s) | Unc / Rare |
| Cleric, Trickery | Warden (Dusk) | Veil | MP | Dusk Cloak (T3) | Slip Away (reaction step; D2) | Unc / Unc |
| **Druid**, Land | Wildcaller (Landbound) [CANON archetype] | Stone, Tides | MP | Rootbind (T3, terrain control) | Trail Foot (rough terrain costs no speed) | Unc / Unc |
| Druid, Moon | Wildcaller (Aspect) | Fist, Spear | SP+MP | Beast Aspect (T4, a stance, not polymorph) | Clear Blood (timed Toxin resist; after Meditation only) | Rare / Unc |
| Druid, Spores | Wildcaller (Rot) | Veil | MP | Spore Cloud (T3) | Clear Blood | Unc / Unc |
| Druid, Shepherd | Wildcaller (Herd) | Tides | MP | Call Beasts (T4, summon) | Wild Tongue (flavour only) | Rare / Com |
| **Fighter**, Champion | Vanguard (Champion) [NEW umbrella] | any Way | SP | Cutting Finish (T4) | Keen Edge (Crit Rate up; chosen Way only) | Rare / Unc |
| Fighter, Battle Master | Vanguard (Maneuver); Ironbreaker | Blade, Spear | SP | Momentum Chain (T4) | Way Stance (one stance at a time) | Rare / Unc |
| Fighter, Eldritch Knight | Runeblade [Hybrid] | Blade; Arcane | SP+MP | Arcane Edge (T3 spell) | Rune Sheath (weapon rune survives disarm; once per fight) | Unc / Unc |
| Fighter, Banneret | Ironbreaker (Rally) [CANON archetype: tank] | Spear, Blade, shield | SP | Shield Wall (T3, taunt) | Guard Check (reach counter on Spear and Blade) | Unc / Unc |
| **Monk**, Open Hand | Stillfist (Open Palm) [NEW] | Fist | SP | Silent Three Fang (T3) [CANON] | Light Footing (evasion; no chest armour) | Unc / Unc |
| Monk, Shadow | Stillfist (Shade) | Fist; Veil | SP+MP | Veil-Pierce Gaze (T4) [CANON] | Slip the Blast (half damage on a failed dodge of an area hit) | Rare / Unc |
| Monk, Four Elements | Stillfist (Elemental Palm) | Fist; one Book | SP+MP | Ember Palm (T3 art, Book tag) | Feather Drop (smaller fall damage; reaction) | Unc / Com |
| Monk, Kensei | Stillfist (Kensei) | Blade, Spear | SP | Calm Cut (T3) | Steady Grip (no disarm from Physical CC) | Unc / Unc |
| **Paladin**, Devotion | Paladin (Devotion) [CANON word] | Blade; Radiance | SP+MP | Warding Circle (T3) [CANON model] | Oath Aura (CC and Mental Resist from Courage; highest aura only) | Unc / Rare |
| Paladin, Vengeance | Paladin (Vengeance) | Blade, Spear | SP | Radiant Brand (T4) | Hunter's Oath (damage up on one marked target) | Rare / Rare |
| Paladin, Ancients | Paladin (Green) | Spear; Stone, Tides | SP+MP | Rootbind (T3) | Bloom Aura (small HP Regen; weaker than any heal) | Unc / Unc |
| Paladin, Crown | Paladin (Crown) | Spear, shield | SP | Call to Heel (T3, taunt) | Oath Aura | Unc / Rare |
| **Ranger**, Hunter | Windrider (Hunter) [CANON archetype: archer] | Bow | SP | Piercing Shot (T3) | Quarry Mark (first hit on marked target; 8 s) | Unc / Unc |
| Ranger, Beast Master | Windrider (Packbound) | Bow; Arcane | SP+MP | Call Companion (T3 spell; one pet slot) | Pack Bond (pet levels with owner; dies to a kill) | Unc / Unc |
| Ranger, Gloom Stalker | Windrider (Dusk) | Bow | SP | Dread Volley (T4) | Ambush Step (bonus on first shot after stealth; 8 s) | Rare / Unc |
| Ranger, Drakewarden | Windrider (Drakebound) | Bow; Embers | SP+MP | Drake Breath (T3 spell) | Pack Bond | Unc / Unc |
| **Rogue**, Thief | Shadowveil (Cutpurse) [CANON archetype: rogue] | Blade, Fist | SP | Swift Draw (T2) | Specialty (small bonus on one non-combat skill) | Com / Com |
| Rogue, Assassin | Shadowveil (Assassin) | Blade | SP | Backstab Chain (T4) | Opening Strike (once per target per 8 s; unaware or flanked) | Rare / Rare |
| Rogue, Arcane Trickster | Shadowveil (Veilhand) | Blade; Arcane, Veil | SP+MP | Hushveil (T3) [CANON] | Half-Step (reaction; D2) | Unc / Unc |
| Rogue, Swashbuckler | Shadowveil (Duelist) | Blade | SP | Winding Step (T3) | Duelist's Poise (Crit Rate up in a one on one; ends when a second enemy engages) | Unc / Rare |
| **Sorcerer**, Draconic | Surgeborn (Drakeblood) [NEW] | Embers | MP | Drake Breath (T4) | Born Affinity (small Magic AP in the origin Book only) | Unc / Unc |
| Sorcerer, Wild Magic | Surgeborn (Fortune) | Arcane | MP | Amplify Surge (T4) | Wild Table (Fortune weighted effect, fired only by Amplify) | Unc / Rare |
| Sorcerer, Storm | Surgeborn (Storm) | Tempest | MP | Stormwall (T4) | Born Affinity | Unc / Unc |
| Sorcerer, Shadow | Surgeborn (Veil) | Veil | MP | Veil Bolt (T2) | Kill Ward (short Ward after a kill; 6 s) | Com / Unc |
| **Warlock**, Fiend | Veilbound (Cinder Pact) [NEW] | Veil, Embers | MP | Cinder Pact (T4) | Kill Ward | Unc / Unc |
| Warlock, Great Old One | Veilbound (Deep) | Veil | MP | Mind Lash (T4, Mental) | Veil Gifts (upgrade branches, as Hushveil gains Silence) | Unc / Rare |
| Warlock, Hexblade | Veilbound (Hexblade) | Blade; Veil | SP+MP | Hex Cut (T3 art) | Bound Weapon (conjured dagger; one at a time) | Unc / Unc |
| Warlock, Celestial | Veilbound (Dawn) | Radiance | MP | Healing Light (T3) | Kill Ward | Unc / Unc |
| **Wizard**, Evocation | Spellforger (Burst) [CANON archetype: mage] | Embers, Tempest | MP | Static Lash (T2) [CANON] | Mana Recall (regain a slice of MP; once per fight) | Com / Unc |
| Wizard, Abjuration | Spellforger (Ward) | Radiance, Arcane | MP | Ward (T3) | Mana Recall | Unc / Unc |
| Wizard, Necromancy | Spellforger (Grave) | Veil | MP | Wither (T4) | Book Savant (faster Mastery in one chosen Book) | Rare / Unc |
| Wizard, Bladesinging | Bladesinger [Hybrid] | Blade; Arcane | SP+MP | Songblade Step (T4) | Poise (evasion with blade drawn, no heavy armour) | Rare / Unc |
| Wizard, Divination | Spellforger (Seer) | Arcane | MP | Foresight Mark (T3) | Codex of Spells (learn by the Wisdom plus Speed check) | Unc / Unc |
| **Artificer**, Alchemist | Gearwright (Alchemist) [NEW; optional 13th] | Arcane | MP | Elixir Burst (T3) | Tinker's Touch (Support Tree Tinker supplement) | Unc / Unc |
| Artificer, Artillerist | Gearwright (Artillerist); Arcane Bomber is the unique cousin | Bow (thrown); Arcane | SP+MP | Rune Turret (T3 item art) | Infusions (gear upgrades; limited by equip slots) | Unc / Unc |
| Artificer, Battle Smith | Gearwright (Smith) | Blade; Arcane | SP+MP | Steel Companion (T3) | Quick Mind (short Wisdom assist; once per fight) | Unc / Unc |

**Canon cast, one line each:** Arya Spellforger (Tempest, L10). Pac_Pac Berserker (Beastfolk). Ru Hobgoblin vanguard (Spear or Fist). Zinka Hobgoblin scout. Drosh Stillfist (Fist). Wyx Blade Dancer (Echo Knight lens, martial only). Sevish Berserker (Axe, martial only). Rian Ironbreaker. Joss enchanter (item based). Tatsuya Arcane Bomber.

---

## 3. D&D features that do not fit, and the conversion

| D&D feature | Why it fails | Conversion [PROPOSAL] |
|---|---|---|
| Short and long rest recharge (Second Wind, Action Surge, ki, slots) | No rests; Meditation is the only refill habit | Cooldown bands D1 to D4; "once per day" only for D4 items and Gambler's Gambit |
| Spell slots, upcasting, prepared lists | One MP pool, tiers | Cost band by tier; upcasting is **Amplify** (extra MP, real risk); known list is the Book tree plus skill cards |
| Cantrips at will | No infinite use | Tier 1 at band C1 and D1 |
| Concentration | No turns or Constitution | Sustained spells end when the caster is stunned, silenced or out of MP; one sustained spell at a time |
| Action, bonus action, reaction; opportunity attacks | Real time combat | Global cooldown about 1 s; reaction arts fire on a trigger with their own cooldown; Guard Check for reach counters |
| Advantage and disadvantage, d20, DC saves | Narrative resolution, numbers only for a live gamble | Compare source strength to the secondary resist stat; Fortune weights gambles |
| Hit Dice, temporary HP | HP is 50 plus 3 per level, one pool | HP Regen, potions, healing spells; temp HP becomes a **Ward** (absorbs then breaks; strongest only) |
| ASI and feats | 2 stat points per level, cap 75 | No ASI; feats become Codex Entries (two to four per arc) |
| Proficiency bonus, Expertise, Jack of All Trades | Mastery 1 to 10 | Proficient means unlocked at Mastery 1 or more; Specialty and Many Hands are passives |
| Sneak Attack dice | No dice | **Opening Strike** passive (limiter above) |
| Rage uses per day, Exhaustion | Beastfolk Enrage exists; no exhaustion track | Rage is an SP art with a **Winded** crash (SP Regen halved, Evasion down, 15 to 30 s) |
| Wild Shape, polymorph | Clumsy in full dive | A Way stance (Aspect) that buffs the body; never swaps HP |
| Familiars, summons | Canon limits them | One pet slot, levels with owner, dies for real; Wildcaller beast summons only |
| Teleport, flight, planar travel | Travel is physical | Blinks of 6 m or less at T3 and up; no flight |
| Revivify, Death Ward, death saves | 72 hour lock; resurrection by relic only | No player resurrection; "cheat death" is **Stand Again** (once per fight) |
| Charm, Dominate, memory edit | NPC AI and Affiliation | Mobs only, short Daze or Calm; players resist through Courage |
| Illusion doubles, Mirror Image | The Doppelganger's Band owns that effect | Item only; Afterimage hits are visual arts |
| Divination oracles | No free answers | Perception Radius and Codex hints; Portent is **Foresight Mark** |
| Alignment detection, Divine Sense | Karma and patron trees exist | **Karma Sense** reads nameplates only |
| Spell components, Subtle Spell | Silence is a hard counter | Verbal covered by Silence; somatic needs a free hand; material is a focus item; Subtle cannot bypass Silence |
| Attunement | Eleven equip slots | Slots are the limiter |
| Flat immunities (poison, charm, fear) | Resists come from race, gear, Courage | Timed buff states or capped partial resists |
| Wild Magic table, rituals, mounts, psionics | No GM table; mounts open | Amplify fires a small Fortune table; rituals are prep like Rune Priming; mounts open question; psionics fold into Arcane force spells or Reinforced Arts |

---

## 4. D&D skills and ability scores mapped to our system

**The six numbers** [CANON]: Courage, Power, Wisdom, Speed, Fortune (the five disciplines) plus Energy (HP and fuel).

**Ability scores**

| D&D score | Our discipline | Secondary stats it drives |
|---|---|---|
| Strength | Power | Physical AP, Armor Pierce, Physical Damage Reduction, Block Rate (shield only) |
| Dexterity | Speed | Physical Evasion, Ranged AP, Accuracy (with Wisdom) |
| Constitution | Energy, with Power for toughness | HP, SP, MP pools; PDR |
| Intelligence | Wisdom (knowledge side) | Magic AP, Magic Evasion, Accuracy |
| Wisdom | Wisdom (perception side), Speed for reflexive awareness | Magic Resistance, Magic Evasion |
| Charisma | Courage (talk and nerve), Fortune for gambles | Mental Resist, Magic Resistance, Crit Rate and Crit Multiplier (Fortune) |

**Saving throws** [PROPOSAL]: Strength save is Physical CC Resist. Dexterity save is Physical Evasion. Constitution save is the Toxin and Stun resists plus HP Regen. Intelligence save is Magic Evasion. Wisdom save is Magic Resistance. Charisma save is Mental Resist (Courage).

**Skills** [PROPOSAL; a skill is "proficient" when unlocked at Mastery 1 or more]

| D&D skills | Discipline | Notes |
|---|---|---|
| Athletics, Intimidation | Power | Lift, carry, break (canon: Tatsuya cannot do heavy labour); intimidation is Power |
| Acrobatics, Sleight of Hand, Stealth | Speed | Nimble Hands is the goblin racial for Sleight of Hand |
| Arcana, History, Nature, Religion, Investigation, Medicine, Survival | Wisdom | Codex Entries and Crafting Manuals; Medicine feeds Field Medic |
| Perception | Wisdom (deliberate) or Speed (reflexive) | Perception Radius; Scavenger's Eye is loot perception |
| Insight | Wisdom | Reads NPCs; paired with Courage in dialogue |
| Persuasion, Deception, Performance, Animal Handling | Courage | The talk face of Courage; Persuasion and Deception carry Affiliation and Karma effects |
| Gambling, thieving odds, loot (no D&D skill) | Fortune | Gambler path, drops, random events |

**Not mapped:** languages, tool proficiencies (these are Crafting Professions with their own Mastery), and background skills (Support Tree supplements).
