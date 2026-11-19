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

<!-- PART1 END -->

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

<!-- PART2 END -->
