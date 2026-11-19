# D&D Gear Baseline for HGO (the hub)

**Status:** Research and proposal file, not canon until the author accepts it. It translates how Dungeons and Dragons handles weapons, armor, shields, adventuring gear and magic-item rarity into our system (Ways, eleven gear slots, the Common to World ladder, six professions). It edits no existing file. Wording and layout are mine, never copied. Where a proposal collides with canon, canon wins and the collision is listed at the end.

**Sibling files.**
- `codex/materials/dnd-gear-material-map.md`: the Gear Tier ladder (GT1 to GT8), every codex material mapped to tier, profession and station, and an item trace table.
- `codex/lore/dnd-camp-gear-tools-and-mounts.md`: tools, adventuring and camp gear, kits, mounts, vehicles, trade goods.
- `codex/lore/dnd-class-dress-and-casting-foci.md`: how each archetype dresses, and caster foci for the eight Books.
- `codex/lore/dnd-racial-gear-sets.md`: a baseline kit for every playable race.
- `codex/lore/goblin-gear-and-camp-realism.md`: goblin and hobgoblin gear, the Common tier, and the camp realism sheet (why tent doors are wrong, and twelve improvised shields and barricades).

**Tags used in every file.**
- **[SRC]** from an outside source, paraphrased, URL given on or just above the line.
- **[CANON]** already in this repo, file named. Items from `codex/materials/blacksmithing-and-farm-resources-book-one.md` are in the repo but that file calls itself a proposal, so they are soft canon.
- **[PAGE]** shown in a chapter.
- **[PROPOSAL]** my invention or adaptation.

---

## 1. Translation rules: D&D concept to HGO concept

The system already has the right hooks. `codex/lore/secondary-combat-stats.md` gives Physical Damage Reduction (Power plus gear armor), Physical Evasion (Speed), Block Rate (Power, only with a shield), Magic Resistance, elemental and toxin resistance, and gear affixes. So I do not invent a new combat layer. I only map D&D's armor and weapon vocabulary onto what is already there.

Source for the D&D side of this table: [SRC] https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment and https://dnd5e.wikidot.com/armor and https://dnd5e.wikidot.com/weapons .

| D&D concept [SRC] | HGO version [PROPOSAL unless marked] |
|---|---|
| Armor Class: armor base plus Dexterity | **Guard** (a flat armor value from gear, feeding Physical Damage Reduction) plus **Physical Evasion** from Speed plus **Block Rate** from a shield. All three already exist [CANON] |
| Light, medium, heavy armor | **Light, Medium, Heavy kit.** Light lets Speed's Evasion count in full. Medium caps it. Heavy gives no Evasion from Speed (D&D: Dex bonus full, max +2, none) |
| Strength requirement (13 for chain mail, 15 for splint and plate; speed drops 10 ft if short) | **Power floor.** Short of it, Movement Speed and SP Regen drop. Placeholder floors: Medium 8, Ring and Mail Hauberk 10, Splint and Plate 12 (racial Power runs 3 to 9, two points per level) |
| Stealth disadvantage (padded, scale, half plate, ring, chain, splint, plate) | **Noisy** tag: sound-based detection range against the wearer grows. Ties to Perception Radius and the Deafen framework [CANON] |
| Don and doff time: light 1 min, medium 5 min, heavy 10 min to don; shield one action | Donning time, same numbers. Out of combat only. A camp caught at night does not get to armor up. In combat only hands and belt consumables change [PROPOSAL, strongly supported by Ch10, where Tatsuya pulls the chest straps tight himself] |
| Armor proficiency (none means disadvantage and no spellcasting) | **Archetype fit**, a soft rule, not a lock. An off-fit weight class costs MP regen or cooldowns, never access. See `codex/lore/dnd-class-dress-and-casting-foci.md` |
| Weapon proficiency (simple, martial) | **Way fit and Mastery** [CANON]. A Way technique needs a weapon of that Way equipped. Any other weapon gives plain strikes only |
| Damage dice (1d4 to 2d6) | **Edge band E1 to E5.** Relative, no dice on the page. Physical AP already carries the numbers [CANON] |
| Weapon properties (light, finesse, heavy, reach, thrown, two-handed, versatile, loading, ammunition, special) | Property tags, section 6 below |
| Magic weapon, armor and shield bonuses and rarity | The rarity ladder and the stat-line step, section 3 |
| Attunement: three items at a time [SRC] https://roll20.net/compendium/dnd5e/Magic%20Items | The **eleven slots** are the limit. No separate attunement. Bound items, Warset and relics are already limited by slot [CANON] |
| Equipment size variant: fitting costs 10 to 40 percent of price [SRC] DDB equipment page above | **Fit pass.** Gear made for another frame needs a refit at a bench for that fraction of its price, or carries a small penalty. See the racial file |
| Coin: 10 cp = 1 sp, 10 sp = 1 gp | Shillings. Index only: 1 gp is roughly 15 shillings at the Common level (OPEN). Real canon anchors are 10 shillings = 1 HGO Coin = 4 yen and the Book One material bands [CANON] |
| Encumbrance by carrying capacity | **Power** governs carry [CANON five-disciplines]. Ch11 notes "nothing pinged encumbrance", so encumbrance exists but is quiet |

---

## 2. Gear Tiers in one table

Full ladder, materials and professions are in `codex/materials/dnd-gear-material-map.md`. The names are mine, not Albion's.

| GT | Name | Level band (OPEN) | Typical rarity | Reads like in D&D |
|---|---|---|---|---|
| 1 | Scrap | 1 to 10 | Common | improvised and starting gear |
| 2 | Camp | 8 to 25 | Common | simple weapons, leather armor |
| 3 | Shop | 20 to 45 | Common, Uncommon | studded leather, chain shirt, martial weapons |
| 4 | Garrison | 40 to 70 | Uncommon, Rare | standard soldier issue |
| 5 | Guild | 65 to 100 | Rare | half plate, plus-one gear |
| 6 | Captain | 95 to 125 | Rare, Legendary | plus-two gear |
| 7 | Marshal | 120 to 150 | Legendary | plus-three gear |
| 8 | Crown | 150 and up | Legendary (World by quest only) | artifact-adjacent |

---

## 3. The Common to World ladder applied to gear

The ladder is [CANON] (`codex/lore/deck-building-rarity-and-classes.md`). The D&D side: a weapon's +1, +2 or +3 is Uncommon, Rare, Very Rare, armor's is Rare, Very Rare, Legendary, a shield's is Uncommon, Rare, Very Rare [SRC] https://api.open5e.com/v1/magicitems/weapon-1-2-or-3/ and https://dnd-srd-sphinx.readthedocs.io/en/latest/magic-item/armor.html and https://dnd-srd-sphinx.readthedocs.io/en/latest/magic-item/shield.html . D&D has six rarities and we have five, so I fold Very Rare into the low end of Legendary and Artifact into World.

The stat-line step is fitted to the three numbers already on the page: `[+1 ENERGY]` on a Common chest, `+3 FORTUNE` on the Gambler's Earring, `[+5 WISDOM]` on the World necklace [PAGE and CANON]. So one step per rarity: Common 1, Uncommon 2, Rare 3, Legendary 4, World 5 [PROPOSAL].

| Rarity | Colour | GT | Stat lines [PROPOSAL] | Insignia seats [CANON-ish] | What it can carry | Trade | D&D equivalent | On the page |
|---|---|---|---|---|---|---|---|---|
| **Common** | white or gray | 1 to 3 | none or one line of +1 | 0 or 1 | nothing special | sells instantly to standing buy orders [CANON] | mundane gear | Common Goblin Leather Chest `[+1 ENERGY]`, Common Goblin Boots, Goblin Gadget Belt (all [PAGE Ch5, Ch10]) |
| **Uncommon** | green | 2 to 5 | one line, +2 | 1 | a passive or a minor weapon trait | sells fast | +1 weapon, +1 shield | Minor Elixir is Uncommon, the consumable analog [PAGE Ch5] |
| **Rare** | blue | 4 to 7 | one or two lines, +3 | 2 | **one named art** (Ru's shield art "unlocks through rare-tier gear" [CANON]) | moves player to player | +2 weapon, +1 armor, +2 shield | Ironhide Chestplate, Vanguard's Greaves, PK Raiding Crest [PAGE Ch11 draft, flagged for rewrite] |
| **Legendary** | gold | 5 to 8 | two or three lines, +4 (up to +5) | 3 | a signature passive or art, set bonus | scarce, millions at the top | +3 weapon, +2 and +3 armor | Shivbone Staff (+Wisdom and Fortune, Spirit Echo) [PAGE Ch11 draft, CANON recipes-spirit-line] |
| **World** | purple | 8 | three or more lines, +5 and up | World Quest only | named abilities that rewrite a build | **bound**, reward only, scaled down in organised guild events [CANON] | artifact | Call of the Bones Necklace `[+5 WISDOM]`, Bone Surge, Shaman's Veil [PAGE Ch9] |

Four tags sit beside the ladder, not on it [CANON]: **Unique** (the race-roll Gambler's Earring, tagged UNIQUE on the page), **Legacy** (old-account gear such as the Doppelganger's Band), **Relic** (the seven patron weapons) and **Bound** (cannot be dropped or traded, exempt from the death-drop roll for race-roll and World Quest items).

### Item card format

The page already shows two shapes: a received line, `[ITEM RECEIVED: COMMON GOBLIN LEATHER CHEST (+1 ENERGY)]`, and a card, `[COMMON GOBLIN LEATHER CHEST] [+1 ENERGY] [COMMON]` [PAGE Ch10, Ch11]. The naming pattern is **Rarity, Make or Race, Material, Slot**, with the material dropped when obvious ("Common Goblin Boots"). Sample cards for the writer [PROPOSAL]:

- `[COMMON GOBLIN HIDE SHIELD] [BLOCK] [COMMON]` (no stat line, GT1)
- `[UNCOMMON THRASH BOARHIDE JERKIN] [+2 COURAGE] [UNCOMMON]` (GT3)
- `[RARE HALLMARKED MAIL HAUBERK] [+3 COURAGE] [SEAT 1/2] [UNLOCKS: SHIELD WALL STEP] [RARE]` (GT5)
- `[RARE THICKHIDE SHIELD] [+3 POWER] [UNLOCKS: GUARD THE LINE] [RARE]` (the kind of piece Ru is waiting for)
- `[LEGENDARY MONO STEEL EDGE] [+4 SPEED] [SEAT 1/3] [LEGENDARY]` (GT6 to GT7)
- `[CALL OF THE BONES NECKLACE: WORLD] [+5 WISDOM] [BOUND]` [PAGE Ch9]

---

## 4. The eleven slots at a glance

[CANON] `codex/lore/equipment-and-gear-slots.md`: necklace, two accessories, belt, chest, legs, boots, gauntlets, helmet, two hand slots (two one-handed items, or one two-handed weapon in both). Full per-slot detail with light, medium and heavy forms follows in section 5.

| Slot | D&D analog | What lives here in HGO [PROPOSAL] | Page |
|---|---|---|---|
| Helmet | helm, hood, cap | hoods, caps, bone and iron helms, horn ports | Ru's dented cap [PAGE Ch9] |
| Chest | body armor | jerkins to plate harness. Pauldrons are part of the chest piece unless a set says otherwise | Common Goblin Leather Chest, Ironhide Chestplate |
| Legs | greaves, chausses | wraps, leggings, mail chausses, cuisses and greaves | Vanguard's Greaves, Wyx's skirt |
| Boots | boots | wraps, hide boots, hobnailed boots, sabatons | Common Goblin Boots |
| Gauntlets | gloves, bracers | wraps, bracers, studded gloves, gauntlets. Covers hands and forearms. Fist Way gauntlets have a striking face | Wyx's leather arm bands and spiked bone guard |
| Belt | belt and pouches | sash, satchel belt, war belt. Carries **sockets** for pouches, gadgets, quiver, sheaths, potion loops | Goblin Gadget Belt, Sevish's brass-buckled belt |
| Necklace | amulet, holy symbol | fang and bone necklaces, amulets, holy symbols | Call of the Bones Necklace, Wyx's fang necklace |
| Accessory 1 and 2 | rings, cloaks, charms | rings, earrings, crests, charms, bracelets, and a cloak **when it carries a stat** (a plain cloak is a cosmetic layer on the chest piece) | Gambler's Earring, Doppelganger's Band, Wyx's torn cloak |
| Hand slots | weapon, shield, focus, light | weapon, second light weapon, shield, focus (wand, orb, tome, talisman), torch or lantern. A two-handed weapon fills both | Sevish's axe, Mateo Silva's Talisman (World off-hand focus) |

No slot exists for a quiver, a back sling, a bag or a mount. [PROPOSAL] Quiver, sheaths and ammo pouches are belt sockets, a back sling for a big axe is a chest-piece harness socket (Sevish's axe rides "in the sling across his back" [PAGE Ch6]), and a mount is an item, not a slot (see the camp gear file). The belt is already modular and upgradable in place [CANON `codex/objects/goblin-gadget-belt.md`].


---

## 5. Armor, slot by slot

### 5.1 D&D armor mapped to HGO kits

Source for the left columns: [SRC] https://dnd5e.wikidot.com/armor and https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment . Guard is the D&D armor bonus over an unarmored 10, so a full set of a given kit matches its D&D class [PROPOSAL]. Names in the first column are in-world [PROPOSAL]. "Capped" means Evasion from Speed counts only up to a cap.

| HGO name | D&D analog (cost, AC, weight) | Kit | Guard (full set) | Evasion | Power floor | Noisy | Don | Typical materials | GT | Who wears it |
|---|---|---|---|---|---|---|---|---|---|---|
| Quilted Wrap | Padded (5 gp, 11 + Dex, 8 lb) | Light | 1 | full | none | yes | 1 min | quilted canvas, sinew thread | 1 to 2 | recruits, field casters |
| Tanned Jerkin | Leather (10 gp, 11 + Dex, 10 lb) | Light | 1 | full | none | no | 1 min | Tanned Beast Leather | 2 to 4 | scouts, rogues, **the Common Goblin line** |
| Riveted Leather | Studded leather (45 gp, 12 + Dex, 13 lb) | Light | 2 | full | none | no | 1 min | Boarhide, Old Kingdom Rivets | 3 to 6 | rangers, Shadowveil |
| Thickhide | Hide (10 gp, 12 + Dex max 2, 12 lb; D&D files it as medium) | Medium | 2 | capped | 8 | no | 5 min | Boarhide, furs, Barrow Bear Hide | 2 to 6 | frontier fighters, druids, orcs |
| Mail Shirt | Chain shirt (50 gp, 13 + Dex max 2, 20 lb) | Medium | 3 | capped | 8 | no | 5 min | Garrison Steel rings | 4 to 6 | garrison soldiers, guards, captains |
| Scale Coat | Scale mail (50 gp, 14 + Dex max 2, 45 lb) | Medium | 4 | capped | 8 | yes | 5 min | Thornback Scale, Warlord Chitin, iron scales | 3 to 7 | beastfolk and orc skirmishers |
| Cuirass | Breastplate (400 gp, 14 + Dex max 2, 20 lb) | Medium | 4 | capped | 8 | no | 5 min | Hallmarked Steel plates | 5 to 7 | officers, guild leads |
| Half-Plate | Half plate (750 gp, 15 + Dex max 2, 40 lb) | Medium | 5 | capped | 8 | yes | 5 min | Hallmarked or Mono Steel | 5 to 8 | captains, champions |
| Thorn-coat | Spiked armor (75 gp, 14 + Dex max 2; **non-SRD**, listed on the wikidot page) | Medium | 4 | capped | 8 | yes | 5 min | barbed Thornwood Bark, Boar Tusk | 3 to 5 | goblin and orc raiders (the Thornhide line in the Book One file) |
| Ring Hauberk | Ring mail (30 gp, 14, 40 lb) | Heavy | 4 | none | 10 | yes | 10 min | iron rings on Boarhide | 2 to 5 | militias, cheap heavies |
| Mail Hauberk | Chain mail (75 gp, 16, Str 13, 55 lb) | Heavy | 6 | none | 10 | yes | 10 min | Garrison Steel | 4 to 7 | heavy infantry |
| Splint Harness | Splint (200 gp, 17, Str 15, 60 lb) | Heavy | 7 | none | 12 | yes | 10 min | Hallmarked Steel | 5 to 8 | dwarven houses |
| Plate Harness | Plate (1,500 gp, 18, Str 15, 65 lb) | Heavy | 8 | none | 12 | yes | 10 min | Hallmarked, Mono Steel, Fallstone | 6 to 8 | Ironbreaker summits, Crown sets |

**Slot shares of a full set** [PROPOSAL]: chest 40 percent, legs 20, helmet 15, gauntlets 15, boots 10. D&D has one body item. We have five armor slots, so a single chest piece is less than the full kit, and a character with chest only (Tatsuya, Ch10) has a fraction of it. This is the mechanical reason his kit reads "trash tier" ([CANON] `codex/lore/equipment-and-gear-slots.md`).

**Evasion, Power floor, Noisy and donning** work as in the translation table. Short of the Power floor, a goblin or elf in a hauberk is slowed. Armor has a **fit class** too: a set made for a Medium frame does not close on a four-foot goblin. See the racial file.

**Elemental and toxin gear comes from materials, not weight class** [CANON `codex/crafting/debuffs-and-resistances.md`]: Rimeiron gear carries Frost, Sunforged Iron Fire, Barrow Bear Hide Toxin. A goblin has zero racial resistance, so his material choice is his only lever.

### 5.2 The five armor slots and the jewelry, belt and hands

| Slot | Light form | Medium form | Heavy form | Common materials | Stat lines it favors [PROPOSAL] | Art it can unlock (Albion pattern, [SRC] https://heaven-guardian.com/albion-online-gear-guide/) |
|---|---|---|---|---|---|---|
| **Helmet** | hood, cap, bone cap | kettle cap, bone helm with cheek guards, horn-ported helm | full helm, great helm | leather, Sturdy Beast Bone, Ironvein, Garrison Steel, Warlord Chitin | Wisdom, Courage | counters a debuff (Echoing Bone Helm eases Deafen, [CANON recipes-spirit-line]) |
| **Chest** | Tanned Jerkin, Riveted Leather, Quilted Wrap | Thickhide, Mail Shirt, Scale Coat, Cuirass, Half-Plate | Ring or Mail Hauberk, Splint or Plate Harness | as the kit table | Energy, Courage, Power | the piece's active ability, often the most important art on a build |
| **Legs** | wraps, leggings, kilt, skirt | mail chausses, scale skirt | cuisses and greaves | leather, scale, steel | Speed, Energy | stance or step arts |
| **Boots** | Common Goblin Boots, soft wraps | hobnailed boots, hide-lined boots | sabatons | Tanned Leather, bone toggles, iron nails | Speed | mobility art ("Hush Step", a footfall dull, from the Thornhide Vest example in the Book One file) |
| **Gauntlets** | leather bands, bracers, wraps | studded gloves, bone guards (spiked bone guard), Warlord Chitin bracers | steel gauntlets | leather, bone, chitin, steel | Power, Speed | grip and strike arts. **Fist Way** gauntlets carry a striking face and make unarmed arts hit as weapons |
| **Belt** | sash, rope belt, satchel belt (**Goblin Gadget Belt**) | war belt with sockets | harness belt | leather, tin buckles, brass buckles | Energy, Fortune | modular sockets and gadget slots [CANON] |
| **Necklace** | fang, claw and bone necklaces, charms | amulets, holy symbols (Radiance foci) | none by weight | bone, silver, Clearquartz | Wisdom, Courage, Fortune | channeling or a passive (the Call of the Bones Necklace is the World case) |
| **Accessory x2** | rings, earrings, bracelets, crests, cloak when stat-bearing | none by weight | none by weight | silver, bone, bronze, thread | Fortune, Speed | small triggers (Gambler's Earring, Doppelganger's Band) |
| **Hands x2** | weapon, second light weapon, buckler, torch | weapon and shield, focus and off-hand | two-handed weapon, tower board | see section 6 | Power, Wisdom | the Way's arts, the shield's art, the focus's channel |

### 5.3 Shields

D&D 5e has a single shield, +2 AC, 6 lb, 10 gp [SRC] https://dnd5e.wikidot.com/armor . Pathfinder splits shields into buckler (+1), light (+1), heavy (+2) and tower (+4, with a cover option and a big armor-check penalty) [SRC] https://www.d20pfsrd.com/equipment---final/armor/ . Real shields were wood, wicker and hide with bosses, rims and leather faces, and the pavise was a big free-standing shield propped for archers behind [SRC] https://en.wikipedia.org/wiki/Shield and https://en.wikipedia.org/wiki/Pavise . I use the Pathfinder split because it gives the camp a real ladder. A shield sits in a hand slot and is the only thing that gives **Block Rate** [CANON secondary stats]. Block bands 1, 2 and 4 copy the D&D and Pathfinder +1, +2 and +4 [PROPOSAL].

| HGO shield | D&D analog | Hand | Block | Power floor | Materials | GT | Notes |
|---|---|---|---|---|---|---|---|
| Camp board | improvised | 1 | 1 (breaks) | none | plank, barrel lid, cart panel, wicker and hide | 1 | what the line holds on the page; see the camp sheet |
| Buckler | PF buckler (5 gp) | 1, belt-hung | 1 | none | wood and hide, iron boss | 1 to 6 | frees the hand for a second grip |
| Light round board | PF light shield | 1 | 1 | none | plank or wicker, hide face | 2 to 6 | goblin and scout shield |
| Round board (the standard "Shield") | 5e Shield (10 gp, +2), PF heavy | 1 | 2 | 8 | planks, rawhide, iron rim and boss | 3 to 8 | garrison default; the Hallmarked and Mono Steel versions carry arts at Rare |
| Kite board | laminated kite and heater | 1 | 2 | 8 | laminated plank, leather | 4 to 7 | mounted troops, covers a leg |
| Tower board or pavise | PF tower shield, medieval pavise | 1 (carried) or planted | 4, or cover | 10 | planks, canvas or hide face, spike foot | 3 to 7 | holds a line or shelters an archer; a pavise is propped and used by a second hand |

**Shield wall** [PROPOSAL, from the plan in `outline/canon-ledger.md`: "a wall holds as a unit even with weak arms"]: adjacent shields add a fraction of their Block to each neighbour. It is a formation property, not an item. **Shield arts** unlock at Rare and carry the art name on the card (Ru's pending shield art, `codex/characters/young-goblin-companion-candidate.md`).


---

## 6. Weapons, per Way

### 6.1 The rule

[CANON] There are five Ways: Fist, Spear, Blade, Axe, Bow (`codex/combat/physical-arts-overview.md`). Abilities fire off "a drawn arrow plus the intent" or a weapon action, and Albion's lesson that the weapon decides the abilities is already the house style (`style-guide/inspirations-and-borrowing.md`). [PROPOSAL] So a Way technique needs a weapon of that Way equipped. Fist needs bare hands, a gauntlet, or an improvised weapon. Put the wrong weapon in the hand and you have plain strikes and no arts, which is exactly Tatsuya's problem in Ch11, "mechanically hand-to-hand" with no weapon equipped [CANON `codex/lore/equipment-and-gear-slots.md`].

### 6.2 Property tags

D&D definitions: [SRC] https://dnd5e.wikidot.com/weapons . HGO column [PROPOSAL].

| Tag | D&D meaning | HGO |
|---|---|---|
| Light | small, suited to two-weapon fighting | may fill **both hand slots** (Wyx's dual sabres); arts cost a little less SP |
| Finesse | Strength or Dexterity for attack and damage | Physical AP leans on **Speed** as well as Power (it is normally Power first, Speed partial [CANON]) |
| Heavy | Small or Tiny wielders have disadvantage | a **Small frame** (a four-foot goblin) loses Edge and reach with it. Hobgoblins and humans do not. Explains why Sevish carries a two-handed axe and camp goblins carry clubs |
| Two-handed | needs two hands to attack | fills both hand slots [CANON] |
| Versatile | one or two hands, bigger die in two | one slot (with a shield) or both slots for about half a band more Edge |
| Reach | adds 5 ft | adds about one pace and hits first. The Spear Way's whole identity |
| Thrown | can be thrown with the melee modifier | thrown use runs on Ranged AP (Speed primary) [CANON]. The item lands in the world and must be walked over to collect (pickup needs a physical claim [CANON]) |
| Ammunition | consumed, about half recoverable | a stack in a quiver socket. Half can be collected after the fight by walking the ground |
| Loading | one shot per action | a short reload beat or cooldown |
| Range | normal and long, beyond normal is hard | meters on the page: shortbow about 25 and 100, longbow about 45 and 180, light crossbow about 25 and 100, heavy crossbow about 30 and 120, sling about 9 and 37, thrown spear about 6 and 18 (D&D feet converted) |
| Special | unusual rules | nets, lances (mounted), see 6.4 |

**Edge bands** [PROPOSAL], from average D&D weapon damage, kept off the page: **E1** (1d4), **E2** (1d6), **E3** (1d8), **E4** (1d10 to 1d12), **E5** (2d6).

**Material ladder for all weapons** (details in the material map): metal heads and blades go GT1 scrap iron or sharpened bone, GT2 Clanmark or Ironvein, GT3 Greywall Iron, GT4 Garrison Steel, GT5 Hallmarked Steel, GT6 Mono Steel (holds a Physical Arts augment), GT7 Fallstone Iron. Hafts go Scrap Wood, Planks, Thornwood or Bonewood, Hollow Heartwood. Bowstaves go Thornwood Bark, Bonewood, Hollow Heartwood with sinew strings. Rarity follows crafter and grade, so any row below runs Common at GT1 to GT3 and climbs.

### 6.3 Weapon tables

D&D analog costs and properties: [SRC] https://dnd5e.wikidot.com/weapons (weapon names marked non-SRD there are left out unless noted). Names in the first column are in-world [PROPOSAL].

**Way of the Fist.** [CANON] Unarmed and improvised-weapon combat, the default for those with no signature weapon, Ru's path. Techniques: Guard Break, Low Sweep, Palm Check, Silent Three Fang, Veil-Pierce Gaze.

| HGO item | D&D analog | Props | Hands | Edge | GT (rarity) | Who |
|---|---|---|---|---|---|---|
| Hand wraps | unarmed strike | Light | both hands | E1 | 1 to 6 (Common to Rare) | brawlers, Beastfolk, recruits |
| Fist-guards (a gauntlet with a striking face) | none in SRD | Light | Gauntlets slot | E1 to E2 | 2 to 7 (Common to Legendary) | brawlers, Pac_Pac-type tanks |
| Camp club | Club (1 sp, 1d4) | Light | 1 | E1 | 1 to 2 (Common) | camp goblins, the enforcers' belts [PAGE Ch6] |
| Great cudgel | Greatclub (2 sp, 1d8) | Two-handed | 2 | E3 | 1 to 3 (Common) | orcs, goblin heavies |
| Improvised weapon | improvised (about 1d4) [SRC] DDB equipment page | varies | 1 | E1 | 1 (Common) | tent poles, barrel staves, ladles, cart rails: anything in a camp raid |
| Thong-lash | Whip (2 gp, 1d4, finesse, reach) | Finesse, Reach | 1 | E1 | 3 to 7 | handlers; the Rare+ Spiritlash Whip [CANON] sits here (OPEN placement) |
| Shield strike | shield bash | none | shield hand | E1 | any | uses Guard Break and Palm Check |

**Way of the Spear.** [CANON] Reach-focused, controlled distance. Techniques: Thrust Line, Guard Sweep, Butt Check, Serpent's Reach. Ru's weapon.

| HGO item | D&D analog | Props | Hands | Edge | GT | Who |
|---|---|---|---|---|---|---|
| Thrash spear | Spear (1 gp, 1d6, thrown, versatile 1d8) | Thrown, Versatile | 1 or 2 | E2 | 1 to 8 | camp goblins, guards, Ru |
| Dart-spear | Javelin (5 sp, 1d6, thrown 30/120) | Thrown | 1 | E2 | 1 to 6 | scouts, skirmishers, the **throwing option under a shield wall** |
| Bo shaft | Quarterstaff (2 sp, 1d6, versatile 1d8) | Versatile | 1 or 2 | E2 | 1 to 6 | travelers, monks, casters' backup |
| Fork-spear | Trident (5 gp, 1d6, thrown, versatile) | Thrown, Versatile | 1 or 2 | E2 | 2 to 6 | coastal and Tides-leaning fighters |
| Bill-glaive | Glaive (20 gp, 1d10, heavy, reach) | Heavy, Reach, Two-handed | 2 | E4 | 3 to 8 | guards |
| Hook-bill | Halberd (20 gp, 1d10, heavy, reach) | Heavy, Reach, Two-handed | 2 | E4 | 3 to 8 | garrison polearm |
| **Wall-pike** | Pike (5 gp, 1d10, heavy, reach, 18 lb) | Heavy, Reach, Two-handed | 2 | E4 | 2 to 6 | formation troops: "spears over the shield wall" is a Kingdom-style line [CANON ledger] |
| Charge-lance | Lance (10 gp, 1d12, reach, special) | Reach, Special (mounted) | 1 | E4 | 4 to 8 | mounted knights, Wyvern riders |

**Way of the Blade.** [CANON] The most common trained weapon in Eryndal. Techniques: Clean Draw, Parry Riposte, Guard Break Swing, Flowing Edge. Wyx's Way.

| HGO item | D&D analog | Props | Hands | Edge | GT | Who |
|---|---|---|---|---|---|---|
| Cut-knife | Dagger (2 gp, 1d4, finesse, light, thrown 20/60) | Finesse, Light, Thrown | 1 | E1 | 1 to 8 | rogues, casters' backup, enforcer belts |
| Scrap cleaver | none in D&D. Pathfinder's dogslicer is a crude single-piece curved goblin blade that often snaps [SRC] https://pathfinderwiki.com/wiki/Dogslicer | Light | 1 | E1 to E2 | 1 to 2 | camp goblins. May **break** on a low roll [PROPOSAL] |
| Short blade | Shortsword (10 gp, 1d6, finesse, light) | Finesse, Light | 1 | E2 | 2 to 8 | Tatsuya's backup on the gadget belt [CANON archetype file] |
| **Sabre** | Scimitar (25 gp, 1d6 slashing, finesse, light) | Finesse, Light | 1, pair | E2 | 3 to 8 | **Wyx's two sabres** [CANON ledger], also the goblin boss and Wildcallers in D&D |
| Arming blade | Longsword (15 gp, 1d8, versatile 1d10) | Versatile | 1 or 2 | E3 | 3 to 8 | garrison default, hobgoblin officers in D&D |
| Needle-blade | Rapier (25 gp, 1d8, finesse) | Finesse | 1 | E3 | 4 to 8 | duelists |
| Two-hand blade | Greatsword (50 gp, 2d6, heavy, two-handed) | Heavy, Two-handed | 2 | E5 | 4 to 8 | champions |
| Reaping hook | Sickle (1 gp, 1d4, light) | Light | 1 | E1 | 1 to 4 | druids, Wildcallers (OPEN placement) |

**Way of the Axe.** [CANON] Heavy and momentum-driven. Techniques: Split Strike, Hook Pull, Haft Check, Momentum Chain. Sevish's Way. [PROPOSAL] Head-and-haft hammers, picks and maces live here too, since a mace is momentum on a haft and no sixth Way exists.

| HGO item | D&D analog | Props | Hands | Edge | GT | Who |
|---|---|---|---|---|---|---|
| Hatchet | Handaxe (5 gp, 1d6, light, thrown 20/60) | Light, Thrown | 1 | E2 | 1 to 8 | everyone, thrown |
| Fighting axe | Battleaxe (10 gp, 1d8, versatile 1d10) | Versatile | 1 or 2 | E3 | 2 to 8 | Thrash axes, dwarves, orcs |
| **War axe** | Greataxe (30 gp, 1d12, heavy, two-handed) | Heavy, Two-handed | 2 | E4 | 4 to 8 | **Sevish** [CANON], Shiv's war axe [CANON], Berserkers |
| Crow-pick | War pick (5 gp, 1d8 piercing) | none | 1 | E3 | 3 to 8 | armor-breakers |
| Hammer | Warhammer (15 gp, 1d8, versatile 1d10) | Versatile | 1 or 2 | E3 | 2 to 8 | dwarves, Wardens |
| Sledge-maul | Maul (10 gp, 2d6, heavy, two-handed) | Heavy, Two-handed | 2 | E5 | 3 to 8 | orcs, wall-breakers |
| Flanged mace | Mace (5 gp, 1d6) | none | 1 | E2 | 2 to 7 | Wardens, temple guards |
| Tack hammer | Light hammer (2 gp, 1d4, light, thrown 20/60) | Light, Thrown | 1 | E1 | 1 to 5 | tinkers, brigands |
| Morning star | Morningstar (15 gp, 1d8 piercing) | none | 1 | E3 | 3 to 7 | goblin bosses and bugbears in D&D |
| Spiked flail | Flail (10 gp, 1d8) | none | 1 | E3 | 3 to 7 | raiders |

**Way of the Bow.** [CANON] Ranged, Speed and Wisdom-adjacent precision. Techniques: Steady Draw, Snap Loose, Pin Shot, Volley Draw. [PROPOSAL] Slings, darts, crossbows and blowguns are Bow Way "draw-less" cousins with a reduced technique list (no Volley Draw for loading weapons). OPEN.

| HGO item | D&D analog | Props | Hands | Edge | GT | Who |
|---|---|---|---|---|---|---|
| Horn shortbow | Shortbow (25 gp, 1d6, 80/320) | Ammunition, Two-handed | 2 | E2 | 1 to 6 | goblin archers (the six who "learn in half an hour" [CANON ledger]), scouts |
| Warbow | Longbow (50 gp, 1d8, 150/600, heavy) | Ammunition, Heavy, Two-handed | 2 | E3 | 3 to 8 | elves, hobgoblin and human archers, Windriders. Small frames struggle |
| Hand-bolt thrower | Hand crossbow (75 gp, 1d6, 30/120) | Light, Loading | 1 | E2 | 4 to 7 | Shadowveil |
| Lever crossbow | Light crossbow (25 gp, 1d8, 80/320) | Loading, Two-handed | 2 | E3 | 3 to 7 | garrisons, tinkers |
| Siege crossbow | Heavy crossbow (50 gp, 1d10, 100/400) | Heavy, Loading, Two-handed | 2 | E4 | 4 to 8 | dwarf wall guards |
| Herder's sling | Sling (1 sp, 1d4, 30/120) | Ammunition | 1 | E1 | 1 to 4 | goblins, shepherds. Bone or stone bullets |
| Throwing dart | Dart (5 cp, 1d4, finesse, thrown 20/60) | Finesse, Thrown | 1 | E1 | 1 to 5 | Shadowveil, poisoners |
| Reed dart-tube | Blowgun (10 gp, 1 piercing, 25/100) | Ammunition, Loading | 1 | E0 plus coating | 2 to 5 | goblin silent weapon (Hollowreed Stalk, Nightveil needles) |

**Ammunition** [SRC] DDB equipment page: arrows 1 gp per 20, bolts 1 gp per 20, sling bullets 4 cp per 20, blowgun needles 1 gp per 50. HGO ammunition ladder [PROPOSAL]: GT1 fire-hardened shaft or bone tip, GT2 flint or iron tip, GT3 Greywall tip, GT5 steel bodkin, GT6 Glassfang or Mono Steel tip, GT7 spirit-fletched.

### 6.4 Special, gadget and relic items (no Way required)

| Item | D&D analog | HGO |
|---|---|---|
| Net | Net (1 gp, thrown 5/15, restrains Large or smaller, DC 10 Strength to break or 5 slashing) [SRC] DDB equipment page | Skitterling Silk net. A trap-line tool, not a Way item |
| Snares and tripwires | hunting trap (5 gp, 25 lb) | Hookvine Cord line [CANON Book One file], trap crafting |
| Gadget line | alchemist's fire, acid | Smoke Bomb, Gas Bomb, Ignition Gas Grenade, Rune-Primed Flare Launcher [CANON recipes] |
| Steampunk sidearm | none | Tatsuya's two-handed tank-fed Gas and Flare shooter [CANON battle-items file]. SP, a Physical Arts identity, not a Way |
| Staves, wands, orbs, tomes | arcane focus (crystal 10, orb 20, rod 10, staff 5, wand 10 gp) [SRC] DDB equipment page | caster foci, see the class file |
| World weapons | artifacts | seven patron relics, for example the three-form Staff of the Mist God [CANON patrons file] |

---

## 7. Adventuring and camp gear, baseline list

Full tool, kit, mount and vehicle tables are in `codex/lore/dnd-camp-gear-tools-and-mounts.md`. Costs [SRC] https://dnd5e.wikidot.com/adventuring-gear and https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment . Because the HGO inventory is a pocket ("the flare materialized in my hand" [PAGE Ch5]), bulky kit is **placed in the world and walked back to** (pickup needs a physical claim [CANON]), and ready items live in belt sockets.

| HGO item | D&D analog (cost, weight) | Where it sits | GT | Notes |
|---|---|---|---|---|
| Satchel and pouches | backpack (2 gp, 5 lb), pouch (5 sp) | belt sockets | 1 to 3 | quick-use items; a backpack expands ready sockets [PROPOSAL] |
| Bedroll and blanket | bedroll (1 gp, 7 lb), blanket (5 sp) | placed | 1 | straw-stuffed patched bedroll in the holding tent [PAGE Ch6] |
| Tent, scouting | tent, two-person (2 gp, 20 lb) | placed | 2 | the scouting tent keeps a character in place when the player logs off [CANON preserved-misc] |
| Hide A-frame tent | none (large) | placed, camp | 2 | the camp's tents [PAGE Ch4] |
| Rope, hemp or sinew | rope 50 ft (1 gp, 10 lb) | belt coil | 1 to 3 | Nab's coil [PAGE Ch10]. 2 hit points, burst DC 17 in D&D |
| Torch and cresset | torch (1 cp), lantern (5 gp) | hand or pole | 1 to 3 | torches in iron cressets along the stakes [PAGE Ch10] |
| Oil lamp | lamp (5 sp), oil (1 sp) | hook | 2 | the holding tent's lamp [PAGE Ch6] |
| Fire kit | tinderbox (5 sp) | belt | 1 | Portable Campfire Kit is the goblin craft default [CANON] |
| Iron pot, bowls, ladle | iron pot (2 gp, 10 lb), mess kit (2 sp) | camp | 2 | the stew pot and wooden bowls [PAGE Ch4] |
| Rations | rations (5 sp, 2 lb) | pocket | 1 | Clanmark Trail Ration [CANON food file] |
| Waterskin and barrel | waterskin (2 sp), barrel (2 gp, 70 lb) | belt, camp | 1 | the water barrel [PAGE Ch4] |
| Hammer, crowbar, shovel, pick | hammer (1 gp), crowbar (2 gp), shovel (2 gp), miner's pick (2 gp) | tool hooks | 1 to 3 | doubles as improvised weapon |
| Spikes, pitons, stakes | pitons (5 cp), spikes (1 gp per 10) | belt | 1 | sharpened stakes line the clearing [PAGE Ch4] |
| Caltrops | caltrops (1 gp per 20) | belt | 1 | scrap-iron, Smithing T1 |
| Signal whistle and bell | whistle (5 cp), bell (1 gp) | belt | 1 | Scout's Whistle battle item [CANON] |
| Climber's kit | climber's kit (25 gp, 12 lb) | belt | 3 | rope-down flanks, the east rockslide |
| Healer's kit | healer's kit (5 gp) | belt | 2 | the lean-to healers (cut from Ch10 but a camp would have them) |
| Potion of healing analog | potion of healing (50 gp) | belt loop | 2 | Minor Elixir restores 30 mana [PAGE Ch5] |
| Chest and crates | chest (5 gp, 25 lb) | camp | 1 | Wyx's crate, the war tent chest [PAGE Ch6, Ch10] |

---

## 8. How each archetype dresses (summary)

Full table, caster foci and level-band kits are in `codex/lore/dnd-class-dress-and-casting-foci.md`. D&D proficiencies: [SRC] https://api.open5e.com/v1/classes/ (fighter and paladin all armor and shields, barbarian, ranger and cleric light and medium and shields, rogue and bard and warlock light only, druid light and medium and no metal, monk, wizard and sorcerer none). Base classes are [CANON] (`codex/lore/deck-building-rarity-and-classes.md`). The fit column is [PROPOSAL].

| Base class | D&D cousins | Kit | Shield | Ways | Hands | Dress in one line |
|---|---|---|---|---|---|---|
| Ironbreaker | fighter, paladin | Heavy, Medium | yes | Spear, Blade, Axe | weapon and shield | plate, round board, taunt arts |
| Berserker | barbarian | Light, none, Thickhide | no | Axe, Blade | two-handed or paired | big edge, little cloth (Sevish wears a vest) |
| Shadowveil | rogue | Light | no | Blade, Bow | paired light blades or crossbow | quiet leather, thieves' kit |
| Windrider | ranger | Light, Medium | optional | Bow, Spear | bow | leather, quiver, pet harness |
| Spellforger | wizard, sorcerer | Light or cloth | no | none (focus) | staff or wand and orb | robe, focus matched to a Book |
| Warden | cleric | Medium | yes | Axe (mace), Spear | mace and shield, holy symbol | mail under a surcoat, Radiance symbol |
| Wildcaller | druid | Light, Thickhide, no metal | wood only | Spear, Blade (sickle) | totem or wooden staff | hide and wood, no iron |
| Hybrid and Custom | bard, monk, warlock | any | any | any | any | gear-driven, Tatsuya's Arcane Bomber is the model |

---

## 9. Where the page's items already sit

| Item | Slot | Rarity, GT | Source |
|---|---|---|---|
| Spawn rags (patched with mismatched leather), bare feet | none | GT1, no stats | [PAGE Ch4] |
| Gambler's Earring `[+3 FORTUNE]` | Accessory | Unique (object file says Rare), GT n/a | [PAGE Ch4], [CANON] object file |
| Goblin Gadget Belt | Belt | Common, GT2 | [PAGE Ch5] |
| Enforcer's blade, club at belt | Hands | GT2 | [PAGE Ch4, Ch6] |
| Common Goblin Leather Chest `[+1 ENERGY]` | Chest | Common, GT1 to 2 | [PAGE Ch10] |
| Common Goblin Boots | Boots | Common, GT1 to 2 | [PAGE Ch10] |
| Call of the Bones Necklace `[+5 WISDOM]` | Necklace | World, bound | [PAGE Ch9] |
| Sevish: war axe, burgundy vest, sash, brass-buckled belt, tooth pendant, ring and bead earrings | Hands, chest, belt, necklace, accessory | level 80, high GT | [PAGE Ch5] |
| Wyx: two sabres, spiked bone guard, leather arm bands, fang necklace, skull at the belt, torn cloak, ear hoops | Hands, gauntlets, necklace, belt, accessory | level 25, high GT | [PAGE Ch5], [CANON] sabres |
| Ru: patched leather vest and dented cap a size too big | Chest, helmet | GT1 | [PAGE Ch9] |
| Zinka: a wrap of dark cloth over one shoulder | Chest layer | GT1 to 2 | [PAGE Ch10] |
| Defenders: a different shield each (tent door, barrel lid, cart panel), a club | Hands | GT1 | [PAGE Ch10] |
| Iron cressets, sharpened stakes, bone totems, blue banners | camp | GT1 to 2 | [PAGE Ch4, Ch6, Ch10] |
| Ironhide Chestplate, Vanguard's Greaves, PK Raiding Crest, Shivbone Staff, Doppelganger's Band | Chest, Legs, Accessory, Hands, Accessory | Rare, Rare, Rare, Legendary, Legacy | [PAGE Ch11 draft] |

---

## 10. Conflicts with canon and open items

Canon wins in every case below.

1. **Gambler's Earring rarity.** `codex/objects/gamblers-earring.md` says Rare. The page says UNIQUE. I treat Unique as a tag beside the ladder.
2. **Wyx's weapon.** `codex/combat/way-of-the-bow.md` calls the Bow Wyx's category and `codex/objects/call-of-the-bones-necklace.md` says dual daggers. The ledger and `codex/characters/thrash-siblings-ability-lists.md` settle on **dual sabres, Way of the Blade**, and the ledger says to fix the stale files. Those files are not edited here. The Ch4-era "quiver across her back" was superseded by the reference image.
3. **Tent doors.** Ch10 says "a tent door, a barrel lid, a cart panel" but the camp's tents have flaps tied shut. Canon seed, see `codex/lore/goblin-gear-and-camp-realism.md` for the fix options.
4. **Epic tier.** Four material and recipe files say "Epic". The ladder has none. I read it as Legendary.
5. **D&D hobgoblins wear chain mail, half plate or plate.** Canon hobgoblin officers (Sevish, Wyx) wear no plate. Canon wins. Plate belongs to dwarves, humans and Ironbreakers.
6. **D&D goblins are leather-and-shield skirmishers.** HGO camp goblins are clubs, boards and patched hide, GT1 to 2, which is poorer than D&D's goblin. That fits "what they raided with" and the clan's ranks [CANON Ch6, `codex/locations/bloodhurst.md`].
7. **Shield arts versus Ways.** Ru's shield art is not under any of the five Ways in the codex. I make it an item-granted art (the Albion pattern). OPEN.
8. **Placement of clubs, maces, hammers, whips, daggers, crossbows and slings** inside five Ways is my reading. The ledger once lists "sword, spear, dagger, bow" as the physical-arts weapons. OPEN whether a sixth Way is wanted.
9. **No cloak, quiver, bag or mount slot.** Eleven slots is canon. I used sockets and the stat-bearing-cloak rule. OPEN.
10. **Guard shares, Power floors, Block bands, Edge bands, price index and level bands** are placeholders.
11. **Chapter 11 draft items** are soft until Chapter 11 is rewritten.
12. **Inventory as a pocket versus backpacks.** I kept both: the pocket stores, belt sockets ready, bulky camp kit is placed.

---

## 11. Sources

- D&D weapons, armor and gear (SRD-based): https://dnd5e.wikidot.com/weapons , https://dnd5e.wikidot.com/armor , https://dnd5e.wikidot.com/adventuring-gear , https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment
- D&D class proficiencies and rarity: https://api.open5e.com/v1/classes/ , https://api.open5e.com/v1/magicitems/weapon-1-2-or-3/ , https://dnd-srd-sphinx.readthedocs.io/en/latest/magic-item/armor.html , https://dnd-srd-sphinx.readthedocs.io/en/latest/magic-item/shield.html , https://roll20.net/compendium/dnd5e/Magic%20Items
- Pathfinder shields and the dogslicer: https://www.d20pfsrd.com/equipment---final/armor/ , https://pathfinderwiki.com/wiki/Dogslicer
- Real shields: https://en.wikipedia.org/wiki/Shield , https://en.wikipedia.org/wiki/Pavise
- Albion Online: https://guildorder.com/games/albion/wiki/gear-tier-system , https://heaven-guardian.com/albion-online-gear-guide/
