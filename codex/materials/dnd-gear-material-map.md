# Gear Material Map: the tier ladder, materials and professions (D&D baseline, Albion-style)

**Status:** Research and proposal file, not canon until the author accepts it. It sits on top of `codex/materials/overview.md`, `organic.md`, `inorganic-and-salvage.md`, `magical-and-spirit-tied.md`, `monocrystals-and-mono-steel.md` and `blacksmithing-and-farm-resources-book-one.md` and does not edit any of them. Sibling files: `codex/lore/dnd-gear-baseline.md` (the hub), `codex/lore/dnd-camp-gear-tools-and-mounts.md`, `codex/lore/dnd-class-dress-and-casting-foci.md`, `codex/lore/dnd-racial-gear-sets.md`, `codex/lore/goblin-gear-and-camp-realism.md`.

**Tags used in this file.**
- **[SRC]** taken from an outside source and paraphrased, with the URL on or above the line.
- **[CANON]** already in this repo, file named. Items taken from the Book One materials file are in the repo, but that file calls itself a proposal, so treat them as soft canon.
- **[PAGE]** shown in a chapter on the page.
- **[PROPOSAL]** my invention or adaptation. Nothing marked this way is canon.

**Purpose.** Any item the writer needs (a camp club, a shield, a sabre, a staff, a tent) can be traced to a material, a processing step, a profession and a station, at a stated tier. Wherever the codex already names a material, I use it. Where it has a gap I say so and propose a plain generic term, never a new brand name pretending to be canon.

---

## 1. The scales, kept separate

The codex already has four scales that must not be merged. I add one more, the Gear Tier, which is simply the crafting-tier idea applied to the finished item.

| Scale | Values | What it measures | Source |
|---|---|---|---|
| Rarity ladder | Common, Uncommon, Rare, Legendary, World | The card colour and what the item can carry. World is reserved for World Quest rewards. | [CANON] `codex/lore/deck-building-rarity-and-classes.md` |
| Material grade | Rough, Standard, Refined, Pristine | How good this particular batch of raw material is. | [CANON] `codex/materials/overview.md` |
| Crafting tier | Tier 1 to 8 | How skilled the crafter is. A Tier 1 smith makes basic Common gear. Tier 8 is the domain of a handful of named crafters. | [CANON] `codex/crafting/overview.md` |
| Creature class | I to IV | How dangerous the source creature is. | [CANON] `codex/creatures/overview.md` |
| **Gear Tier (GT)** | **GT1 to GT8** | **What kind of gear it is, matched to the crafting tier that can make it reliably.** | **[PROPOSAL]** |

Rules for how they interact, all [PROPOSAL] except the first, which is [CANON] (`codex/materials/monocrystals-and-mono-steel.md`):
1. Finished gear rarity follows the crafter's tier and the grade of the batch, not the material's own tier alone.
2. A crafter at tier N makes GT N gear reliably. GT N plus 1 is a gamble. Two or more above is almost never a success (the existing success-rate rule in `codex/crafting/overview.md`).
3. Rarity band by material: Common materials feed GT1 and GT2. Uncommon feed GT3 and GT4. Rare feed GT5 and GT6. Legendary feed GT7 and GT8. A Pristine batch of a lower band can lift an item by half a step but never across a band.
4. World rarity is never crafted. It comes from World Quests. GT8 crafted gear tops out at Legendary.

### What Albion does, and what we take from it

Albion Online is a stated inspiration (`style-guide/inspirations-and-borrowing.md`). The facts below are what I could confirm. We take the structure and use our own names.

- [SRC] https://guildorder.com/games/albion/wiki/gear-tier-system : Albion gear runs on numbered tiers (the page covers T2 to T8). Each tier has enchantment sub-levels .0 to .4 and each step adds the same flat amount of item power. Five quality ratings (Normal, Good, Outstanding, Excellent, Masterpiece) add small flat bonuses. From T3 upward, crafting needs refined material from the tier below. Refining happens at dedicated stations (smelter, lumbermill, tanner, weaver, stonemason) and finished gear at a forge, a hunter's lodge or a mage's tower.
- [SRC] https://heaven-guardian.com/albion-online-gear-guide/ : ten slots (main hand, off hand, head, chest, shoes, cape, bag, food, potion, mount). Three armor types, cloth (most output, least defence), leather (balanced), plate (most defence). The weapon sets the core role and abilities, and the chest piece's active ability often matters more than its material. Helmets counter specific effects, boots handle mobility, capes give automatic effects. Tier 4 is a common starting point for full builds, and enchantment can let a lower tier compete with a higher one.

**Translation table** [PROPOSAL]:

| Albion idea | Our version |
|---|---|
| Item tier | Gear Tier GT1 to GT8, matched to crafting tier |
| Enchant level .0 to .4 | Insignia seats, 0 to 3 (the existing rule: Common 0 or 1, Uncommon 1, Rare 2, Legendary 3, `codex/materials/blacksmithing-and-farm-resources-book-one.md`) |
| Quality rating | Material grade (Rough to Pristine) plus the Lucky Craft proc (`codex/crafting/crafting-stations-and-process.md`) |
| Refine raw to refined to finished | Gather, process (tan, smelt, carve), craft. The codex already says each is "a real, separately-crafted intermediate step" (`codex/materials/organic.md`) |
| Refined material from the tier below | A GT N piece needs processed stock of GT N, and the processing step itself must be done at tier N minus 1 or better [PROPOSAL] |
| Weapon decides abilities | A Way technique needs a weapon of that Way. See `codex/lore/dnd-gear-baseline.md` section 6 |
| Armor slots grant abilities | Rare and higher armor and shields can unlock one named art, as Ru's shield art already does ([CANON] `codex/characters/young-goblin-companion-candidate.md`) |
| Plate / leather / cloth | Heavy / Light / soft goods, plus our Medium kit. See `codex/lore/dnd-gear-baseline.md` section 5 |

---

## 2. Gear Tier names

The names are mine and are not Albion's. Level bands are [PROPOSAL] and OPEN, because the codex says crafting tiers are "gated by character level bands" but never states the bands (`codex/crafting/overview.md`). The ceiling is level 150 for the first major milestone ([CANON] `codex/lore/leveling-and-progression.md`).

| GT | Name | Wearer level band | Typical rarity | Typical grade | Crafter | D&D feel | What it looks like |
|---|---|---|---|---|---|---|---|
| 1 | **Scrap** | 1 to 10 | Common | Rough | Tier 1 | Starting gear, improvised weapons | Field-made from salvage and raw hide. Patched rags, clubs, stake-spears, hide shields. |
| 2 | **Camp** | 8 to 25 | Common (Uncommon on a Lucky Craft) | Rough to Standard | Tier 2 | Simple weapons, leather armor | Made at a camp bench. Tanned leather, iron-capped tools, plain boots. Where the Common Goblin line lives. |
| 3 | **Shop** | 20 to 45 | Common to Uncommon | Standard | Tier 3 | Studded leather, chain shirt, martial weapons | Made at a proper forge or tannery. Riveted leather, Greywall Iron edges. |
| 4 | **Garrison** | 40 to 70 | Uncommon to Rare | Standard to Refined | Tier 4 | Standard-issue soldier gear (the chain-and-shield soldier) | First steel. What a city guard or legion soldier is issued. |
| 5 | **Guild** | 65 to 100 | Rare | Refined | Tier 5 | Half plate, plus-one gear | Rare stock: Myrrhwood Hide, Hallmarked Steel, Rimeiron. What serious guild members wear. |
| 6 | **Captain** | 95 to 125 | Rare to Legendary | Refined to Pristine | Tier 6 | Plus-two gear | Mono steel, Barrow Bear Hide, Thornback scale. Officer and top-guild gear. |
| 7 | **Marshal** | 120 to 150 | Legendary | Pristine | Tier 7 | Plus-three gear | Fallstone Iron, Legendary catalysts, three seats. |
| 8 | **Crown** | 150 and up | Legendary (World only by quest) | Pristine | Tier 8 | Artifact-adjacent | Named crafters only. Kingdom-defining pieces. |

Page anchors, all [PAGE]: Tatsuya at level 8 wears Common gear (Common Goblin Leather Chest, Common Goblin Boots, the Common Goblin Gadget Belt), which is GT1 to GT2. The raiders at levels 12 to 14 in the codex (5 and 6 on the page) carry **Rare** legacy pieces (Ironhide Chestplate, Vanguard's Greaves) in the draft of Chapter 11. That is not a contradiction: legacy-account gear is old high-grade gear on a low-level body, so rarity can run ahead of level for legacy pieces ([CANON] `codex/lore/preserved-misc-mechanics.md` on legacy accounts, and `codex/characters/pk-wraith-raiding-party.md`).

---

## 3. The master ladder (material by tier and family)

Read down a column to see one material family climb. Read across a row to see what a character at that tier is plausibly wearing. Every material name is [CANON] unless tagged. Rarity in brackets is the material's own rarity.

| GT | Hide and leather | Bone, horn, tusk, scale | Wood and plant | Iron, steel, mono steel | Cloth and cord | Crystal, reagent | Magic and spirit |
|---|---|---|---|---|---|---|---|
| **1 Scrap** | Raw Beast Hide, patched rag-leather [Common, Rough] | Bone Shards [Common, Rough] | Scrap Wood, fire-hardened poles, tent poles | Copper and Iron Scrap, salvaged edges, Clanmark Ore [Common, Rough] | Sinew, plant twine, canvas scraps | Common Spirit Dust [Common, Rough] | none |
| **2 Camp** | Tanned Beast Leather (Ash Wolf, plain boar) [Common, Standard] | Sturdy Beast Bone, carved bone [Common] | Scrap Planks, Pine Pitch (glue), Hollowreed Stalk | Clanmark and Ironvein Ore ingots, Bloodhurst Slag as flux (plain iron) [Common] | Canvas, sinew thread, leather thong | Common Spirit Dust [Standard] | none |
| **3 Shop** | Boarhide **[PROPOSAL generic name]** from Ironback and Thornwood Boar [Uncommon] | Marrowhound Rib, Thornwood Boar Tusk [Uncommon] | Thornwood Bark, Bonewood (Myrrhwood timber) [Uncommon] | **Iron:** Greywall Iron, Old Kingdom Rivets [Uncommon], Mountain Coal as fuel [Common] | Skitterling Silk, Hookvine Cord [Uncommon] | Clearquartz, Cinderflint, Wind Monocrystal (Rough) [Uncommon] | Rune Stone Fragments [Uncommon] |
| **4 Garrison** | Boarhide (Refined) with Thornwood Bark backing | Marrowhound Rib and Boar Tusk (Refined) | Bonewood (Refined), Thornwood Bark staves | **Steel:** plain Garrison Steel **[PROPOSAL generic name]**, smelted from Greywall Iron with Mountain Coal | Skitterling Silk (Refined), Enchanted Thread (processed) | Wind Monocrystal (Standard), Clearquartz (Refined) | Rune Stone Fragments (Refined) |
| **5 Guild** | Myrrhwood Hide [Rare, poison-resistant] | Ancient Bone Shards (Rare end) | Hollow Heartwood [Rare] | **Steel:** Hallmarked Steel Bar [Rare]. **Alloys:** Fort Bronze Plate, Rimeiron (frost), Sunforged Iron (fire) **[PROPOSAL tier]**, Skyglass Ore (arcane) **[PROPOSAL tier]** | Enchanted Thread (Refined) | Prism Dust, Echostone, Blue Pearls | Whispering Ash [Rare] |
| **6 Captain** | Barrow Bear Hide [Rare, Toxin ward], Thornback Scale, Warlord Chitin [Rare] | Glassfang, Mistantler [Rare], Ancient Bone Shards (Pristine) | Hollow Heartwood (Pristine) | **Mono Steel** [Rare ingredient, Refined alloy], Mountain Silver inlay | Enchanted Thread (Pristine), Spirit-Infused Oil (processed) | Prism Dust (Pristine), Monocrystal (Rare cluster) | Whispering Ash (Refined) |
| **7 Marshal** | Pristine Rare hides with a Legendary catalyst. **Gap: no Legendary hide is named in the codex** | Pristine Rare bone with a Legendary catalyst. **Same gap** | Hollow Heartwood with an Elderbeast Marrow seat | **Fallstone Iron** [Legendary], Mono Steel (Pristine) | Spirit-woven thread **[PROPOSAL]** | Pristine monocrystal from a Class IV beast (OPEN) | Spirit Shards, Cursed Ash, Elderbeast Marrow [Legendary] |
| **8 Crown** | Same stock at its best, by a named Tier 8 crafter | same | same | Fallstone with Mono Steel fittings | same | Legacy Crystals, Ancient Relics | Shivbone Fragments **[World, World Quest chain only, never crafted for sale]** |

---

## 4. Family tables

Columns: the profession that does the work and the station. Stations are [CANON] (`codex/crafting/crafting-stations-and-process.md`): the **Portable Campfire Kit** (basic recipes anywhere, low success above Tier 4), the **Clan Workbench / Forge** (full Smithing and Bonecrafting/Leatherworking), the **Shamanic Altar / Spirit Circle** and the later **Portable Shaman Kit** (spirit-binding). The six professions are [CANON] (`codex/crafting/professions.md`).

### 4A. Hide and leather

| GT | Material | Source | Profession (station) | Typical gear |
|---|---|---|---|---|
| 1 | Raw Beast Hide, patched | Ash Wolf, Bog Croaker and similar Class I (`codex/creatures/class-1.md`) | Bonecrafting/Leatherworking T1 (Campfire Kit) | Spawn rags with mismatched leather patches [PAGE Ch4], wraps, thongs, rag-vests |
| 2 | Tanned Beast Leather | Same, processed ("Tanned Leather", `codex/materials/organic.md`) | Leatherworking T2 (Clan Workbench) | **Common Goblin Leather Chest, Common Goblin Boots** [PAGE Ch10], belts, pouches, quivers, waterskins, hide shields |
| 3 | Boarhide (generic) | Ironback Boar, Thornwood Boar (Class II) | Leatherworking T3 (Clan Workbench) | Riveted leather, hide-and-bark jerkins, saddles |
| 4 | Boarhide Refined plus Thornwood Bark backing | Same | Leatherworking T4 | Garrison leather, Thickhide coats (the D&D "hide armor" slot) |
| 5 | Myrrhwood Hide | Myrrhwood, "tougher and poison-resistant" [CANON organic.md] | Leatherworking T5 | Scout and ranger sets for Myrrhwood and goblin elites |
| 6 | Barrow Bear Hide, Thornback Scale, Warlord Chitin | Class III beasts (Book One file) | Leatherworking T6 with Smithing for rivets | Thornhide sets, scale coats, chitin gauntlets and helmets |
| 7 to 8 | Pristine Rare hide plus Legendary catalyst | Class III and IV, OPEN | Tier 7 to 8 named crafters plus Enchanting | Marshal and Crown sets (the Thornhide Skirmisher Set Pattern is the codex's existing top light set) |

### 4B. Bone, horn, tusk, scale and chitin

| GT | Material | Source | Profession (station) | Typical gear |
|---|---|---|---|---|
| 1 | Bone Shards | Any beast | Bonecrafting T1 | Knobs, needles, toggles, bone totems for poles |
| 2 | Sturdy Beast Bone | Same | Bonecrafting T2 | Bone daggers, bone clasps, fang necklaces, spiked bone guards (Wyx's look) |
| 3 | Marrowhound Rib, Thornwood Boar Tusk | Class II | Bonecrafting T3 | Bonewire frames for light armor, bow limbs, trap spikes, blade edges, pommels |
| 5 | Ancient Bone Shards | Ruins, Grand Library restricted floors | Bonecrafting T5, Enchanting | Spirit-affinity pieces, Shivbone-line wands (the codex recipe uses three) |
| 6 | Glassfang, Mistantler | Glassfang Lynx, Mist Stag (proposed beasts in the Book One file) | Bonecrafting T6 | Light dagger edges, wand and staff heads |
| 8 | Shivbone Fragments | World Quest chain only | Runecrafting/Spirit-Binding | The Call of the Bones line. Not for sale |

### 4C. Wood and plant

The codex lists only Scrap Wood and Planks, Bonewood, Thornwood Bark, Hollow Heartwood and Pine Pitch. It names no woodworking profession. **[PROPOSAL, OPEN]:** wood is shaped by the profession that owns the finished item. Bonecrafting/Leatherworking takes bows, staves, wands, wicker and shield faces. Smithing takes hafts, shafts, frames, stakes and anything metal-fitted. No seventh profession is added.

| GT | Material | Profession | Typical gear |
|---|---|---|---|
| 1 | Scrap Wood, green poles | Smithing T1 or Bonecrafting T1 | Clubs, stake-spears, tent poles, stakes, hurdle uprights |
| 2 | Scrap Planks, Pine Pitch, Hollowreed Stalk | Smithing T2 | Shield boards, spear shafts, hafts, crate and cart boards |
| 3 | Thornwood Bark, Bonewood | Bonecrafting T3 | Bow staves, staves, stiff backing under armor |
| 5 to 6 | Hollow Heartwood | Bonecrafting T5, Enchanting | Reusable rune staves and wands (holds a rune seat well) |

**Note on "ironwood".** The brief asked for goblin gear built from hide, bone, sinew, ironwood and scrap iron. Ironwood is **not a codex material**. The nearest are Bonewood (Myrrhwood, dense and dark), Thornwood Bark and Hollow Heartwood. I use "ironwood" in lowercase only as a generic craft word for any very hard timber and never as a node name. See conflicts.

### 4D. Iron, steel and mono steel

| GT | Metal | Source | Profession (station) | Typical gear |
|---|---|---|---|---|
| 1 | Scrap iron, Copper and Iron Scrap | Salvage from ruins and camps | Smithing T1 (Campfire Kit) | Nails, spikes, caltrops, knife blanks, cressets |
| 2 | Clanmark Ore, Ironvein Ore (base-tier smithing metal) | Bloodhurst belt, Lunarest | Smithing T2 (Clan Forge) | Axe and spear heads, plain blades, shield rims, pots |
| 3 | Greywall Iron, Old Kingdom Rivets | High ground mines, fort ruins | Smithing T3 | Rivets, riveted armor, good heads, mail rings |
| 4 | Garrison Steel (generic, needs Mountain Coal) | Smelted Greywall plus coal | Smithing T4 | Mail shirts, soldier blades, helmets |
| 5 | Hallmarked Steel Bar | Dwarven house standing | Smithing T5 | High-end plate, mail hauberks, guild weapons |
| 6 | **Mono Steel** | Rimeiron plus wind monocrystal, refined by dwarven houses | Smithing T6 | Blades and armor that **hold a Physical Arts augment** and resist magic better than iron |
| 7 | Fallstone Iron | Storm falls on the high ground | Smithing T7 plus Enchanting | The best Book One edge (Fallstone Edge Pattern) |

### 4E. Special-affinity metals and alloys

| Metal | GT (proposed) | Effect | Source |
|---|---|---|---|
| Rimeiron | 5 | Innate minor Frost resistance in any piece | [CANON] `codex/materials/overview.md` |
| Sunforged Iron | 5 | High heat tolerance, holds a burn enchant, Fire resistance | [CANON] overview and `codex/crafting/debuffs-and-resistances.md` |
| Skyglass Ore | 5 | Light, Wisdom-friendly, favored for staves | [CANON] overview |
| Fort Bronze Plate | 5 | Holds rune priming without cracking | [CANON] Book One file |
| Mountain Silver | 6 | Inlay wire, carries a rune charge, holds a ward | [CANON] Book One file |
| Mono Steel | 6 | Frost resistance kept, holds the augment | [CANON] `codex/materials/monocrystals-and-mono-steel.md` |

### 4F. Cloth and cord

Only Skitterling Silk, Hookvine Cord, Enchanted Thread and sinew exist in the codex. Canvas is on the page in the tents. Linen, wool and cotton are real trade goods in D&D [SRC] https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment (canvas, cotton and linen are priced by the square yard). **[PROPOSAL, OPEN]:** soft goods (robes, wraps, bedrolls, canvas, banners, hurdle ties) belong to Bonecrafting/Leatherworking, with Enchanting adding Enchanted Thread for caster robes.

### 4G. Crystals, reagents and inks (Enchanting)

| Material | GT | Use in gear |
|---|---|---|
| Common Spirit Dust | 1 to 4 | Seats a Common insignia |
| Wind Monocrystal | 3 to 6 | Tempest foci, mono steel feedstock |
| Clearquartz | 3 to 4 | Mask lenses, focus lenses |
| Cinderflint | 3 | Spark triggers on gadgets |
| Prism Dust, Echostone, Blue Pearls | 5 to 6 | Serious enchanting, competitive-gear flavor (Echostone), Tides foci (Blue Pearls) |
| Elderbeast Marrow | 7 | The only catalyst that seats a Legendary insignia |

### 4H. Magical and spirit materials (Runecrafting/Spirit-Binding, gated)

Gated behind an open Spirit Magic path or Tatsuya's necklace bypass, and needs the Shamanic Altar or Portable Shaman Kit ([CANON] `codex/crafting/professions.md`, `crafting-stations-and-process.md`).

| Material | Rarity | GT | Use |
|---|---|---|---|
| Rune Stone Fragments | Uncommon up | 3 to 6 | Inscription, channeling |
| Whispering Ash, Cursed Ash | Rare to Legendary | 5 to 7 | Spirit-binding, anti-curse items, Spirit Ward Totem |
| Spirit Shards | "Epic to World", read here as Legendary (see conflicts) | 7 | Magic weapon cores, activating catalysts |
| Legacy Crystals, Ancient Relics | "Epic and up", read as Legendary | 7 to 8 | Hybrid human-elf-goblin tech |
| Shivbone Fragments | World | 8 | True Shiv-descendant gear, World Quest only |

---

## 5. Refinement chain and "hold"

[PROPOSAL] chain, built on the codex's own intermediate list ("Tanned Leather, Carved Bone Runes, Distilled Poison, Enchanted Thread, Spirit-Infused Oil, Flare Cores", `codex/materials/organic.md`):

| Step | Hide | Metal | Bone | Wood | Cloth |
|---|---|---|---|---|---|
| 1 Gather | Skin from a kill | Ore or scrap | Harvest | Cut trunk, strip bark | Gather fibre or salvage canvas |
| 2 Process | Scrape and tan (Leatherworking) | Smelt to ingot (Smithing, slag as flux) | Clean and carve | Season and split into planks and billets | Spin and weave |
| 3 Work | Cut, stitch, rivet | Forge and temper | Carve, wire | Shape | Sew |
| 4 Finish | Oil, harden, line | Edge, fit, grip | Polish, bind | Bind, fit, lacquer | Hem |
| 5 Seat (optional) | Enchanting seats an insignia | same | same | same | same |

**Hold.** A material's hold is how well it keeps an enchant instead of bleeding it. This is a concept already written into the Book One file ([CANON], `codex/materials/blacksmithing-and-farm-resources-book-one.md`): iron and most hides hold poorly, Fort Bronze Plate, Mountain Silver, Hollow Heartwood and Mistantler hold well, mono steel and Fallstone hold best. I use four steps, Low, Mid, High, Top, and I place plain Garrison Steel and Hallmarked Steel at **Mid** [PROPOSAL]. This is why a dwarf can forge the best base but "cannot seat a rune" (same file, from `codex/races/dwarf.md`), and why a goblin enchanter is a partner and not a customer.

---

## 6. Item trace: from the thing the writer needs back to material and profession

Every row is [PROPOSAL] mapping. Material names are [CANON] unless marked.

| Item | GT | Primary material | Processed form | Profession | Station | Notes |
|---|---|---|---|---|---|---|
| Camp club | 1 | Scrap Wood, bone knob | shaped billet | Smithing T1 or Bonecrafting T1 | Campfire Kit | The club seen at belts [PAGE Ch6]. Improvised weapon |
| Stake-spear | 1 | fire-hardened pole | pointed, charred | Smithing T1 | none | The poorest spear |
| Thrash spear | 2 | Scrap Planks shaft, Ironvein head | forged head | Smithing T2 | Clan Forge | The standard camp spear |
| Hatchet / fighting axe | 2 to 3 | Clanmark or Greywall head, plank haft | forged head | Smithing T2 to T3 | Clan Forge | |
| Camp sabre (curved short blade) | 3 to 4 | Greywall or Garrison Steel, leather grip | forged blade | Smithing T3 to T4 | Clan Forge | Wyx's dual sabres are far above this, see goblin file |
| War axe (two-handed) | 4 to 6 | Garrison or Hallmarked Steel, Bonewood haft | forged head | Smithing T4 to T6 | Clan Forge | Sevish's weapon class |
| Horn shortbow | 2 to 4 | Thornwood Bark or Bonewood stave, sinew string | stave plus string | Bonecrafting T2 to T4 | Clan Workbench | |
| Arrow | 1 to 5 | plank or reed shaft, bone or iron head, feather | head plus fletch | Bonecrafting plus Smithing | Campfire Kit | Stack item, consumed [PROPOSAL] |
| Herder's sling | 1 | leather thong, pouch | cut leather | Leatherworking T1 | Campfire Kit | |
| Reed dart-tube | 2 | Hollowreed Stalk, Nightveil needles | cut reed, distilled poison | Bonecrafting T2 plus Poisoncraft | Campfire Kit | The goblin silent weapon |
| Common Goblin Leather Chest | 1 to 2 | Tanned Beast Leather, thong straps | tanned hide | Leatherworking T1 to T2 | Clan Workbench | [PAGE Ch10], +1 Energy, Common |
| Common Goblin Boots | 1 to 2 | Tanned Beast Leather | tanned hide | Leatherworking T1 to T2 | Clan Workbench | [PAGE Ch10] |
| Goblin Gadget Belt | 2 | Beast Leather, tin buckles | tanned leather | Leatherworking T2 plus Alchemy gadget line | Clan Workbench | [PAGE Ch5], Common, slots locked until materials gathered |
| Riveted leather | 3 | Boarhide, Old Kingdom Rivets | tanned, rivets | Leatherworking T3 plus Smithing | Clan Workbench | |
| Spiked bone pauldron | 3 to 4 | Marrowhound Rib, Sturdy Beast Bone | carved | Bonecrafting T3 | Clan Workbench | Wyx's guard, as seen [PAGE Ch5] |
| Mail shirt | 4 | Garrison Steel rings | wire, rings | Smithing T4 | Clan Forge | |
| Scale coat | 5 to 6 | Thornback Scale, Hallmarked rivets | scales | Bonecrafting T5 plus Smithing | Clan Forge | |
| Plate harness | 6 to 7 | Hallmarked Steel or Mono Steel plates | plates | Smithing T6 to T7 | Clan Forge | Needs a dwarven contact for the bar |
| Bone cap or helm | 2 to 4 | Sturdy Beast Bone, hide lining | carved | Bonecrafting T2 to T4 | Clan Workbench | |
| Iron cap | 2 to 3 | Ironvein plate | forged | Smithing T2 to T3 | Clan Forge | |
| Wicker-and-hide shield | 1 to 2 | green willow or reed, rawhide face | woven frame, wet rawhide | Leatherworking T1 | Campfire Kit | See camp sheet |
| Plank shield | 1 to 2 | Scrap Planks, battens, rope grip | cut boards | Smithing T1 to T2 | Campfire Kit | |
| Iron-rimmed round board | 3 to 4 | Planks, Greywall rim and boss | forged rim | Smithing T3 to T4 | Clan Forge | |
| Fang-and-claw necklace | 2 to 3 | fangs, claws, sinew | cleaned | Bonecrafting T2 | Campfire Kit | Jewelry [CANON] |
| Bone totem (pole cap) | 2 | Sturdy Beast Bone | carved | Bonecrafting T2 | Campfire Kit | On the war tent poles [PAGE Ch6] |
| Staff, plain | 2 to 3 | Bonewood or Thornwood | shaped | Bonecrafting T2 to T3 | Clan Workbench | "A staff makes channeling easier" [CANON ledger] |
| Rune staff, reusable | 5 to 6 | Hollow Heartwood, Mountain Silver wire | shaped, wired | Bonecrafting T5 plus Enchanting | Clan Workbench | Hollow Heart Foci Pattern |
| Burnable bone-and-wire wand | 2 to 3 | Marrowhound Rib, copper wire | carved | Bonecrafting T3 plus Enchanting | Campfire Kit | Tatsuya's cheap wands |
| Hide A-frame tent cover | 2 | Tanned Beast Leather panels | sewn | Leatherworking T2 | Clan Workbench | The camp's tents [PAGE Ch4] |
| Canvas tent | 2 to 3 | canvas, rope | sewn | Leatherworking (soft goods) T2 | Clan Workbench | The round war tent [PAGE Ch6] |
| Timber tent frame and ribs | 2 | Scrap Planks, poles | cut, lashed | Smithing T2 | Campfire Kit | |
| Sharpened stake | 1 | green pole | pointed | Smithing T1 | none | The line along the clearing [PAGE Ch4] |
| Hurdle panel | 1 | hazel or willow, hide ties | woven | Leatherworking (soft goods) T1 | none | Proposal, see camp sheet |
| Iron stew pot | 2 | Ironvein plate | forged | Smithing T2 | Clan Forge | [PAGE Ch4] |
| Iron cresset | 2 | Ironvein | forged | Smithing T2 | Clan Forge | The torch holders along the stakes [PAGE Ch10] |
| Rope | 1 to 3 | sinew, hide thong, Hookvine Cord | twisted | Leatherworking T1 to T3 | Campfire Kit | Nab carries a coil [PAGE Ch10] |
| Quiver, pouch, satchel | 1 to 2 | Tanned Beast Leather | cut | Leatherworking T1 | Campfire Kit | |
| Bedroll | 1 | hide, straw stuffing | sewn | Leatherworking T1 | none | The holding tent has one with straw [PAGE Ch6] |
| Caltrops | 1 | scrap iron | forged spikes | Smithing T1 | Campfire Kit | |
| Smoke or gas bomb | 2 to 3 | Beast Leather pouch, herbs, Gas Sac | assembled | Alchemy/Poisoncraft gadget line | Campfire Kit | [CANON] recipes-gadget-line |
| Charged Ward | 5 | Monocrystal, leather pouch, Spirit Dust | charged token | Alchemy gadget line plus Enchanting | Clan Workbench | [CANON] stub recipe |
| Rune circle chalk or ink | 3 | Rune Stone Fragments, Spirit Dust | ground | Runecrafting | Shamanic Altar or Shaman Kit | Gated |
| Portable Spirit Ward Totem | 6 | carved bone, Whispering Ash | carved | Runecrafting/Spirit-Binding | Shamanic Altar | [CANON] recipes-spirit-line |

---

## 7. Who crafts what, in one view

| Profession [CANON] | Owns in this ladder |
|---|---|
| Smithing | Every metal part, weapon heads, hafts and frames, mail, plate, shield rims, pots, cressets, stakes and caltrops (the physical gear layer) |
| Bonecrafting / Leatherworking | Hide and leather armor, boots, belts, pouches, bone and horn pieces, jewelry, bows, staves, wands, soft goods and wicker **[PROPOSAL placement for bows, wands, wicker, soft goods]** |
| Alchemy / Poisoncraft | Gadget line, poison coatings, needles, fire-ward and hide-preserving washes [PROPOSAL for the washes] |
| Enchanting | Insignia seats, enchanted thread, charged tokens |
| Cooking | Trail rations for camp kits |
| Runecrafting / Spirit-Binding | Rune work and spirit-bound gear, gated |

The hard cap of two active professions per character (`codex/crafting/overview.md`) means a camp armorer is not also a smith. A camp therefore needs a **named trade roster**: one smith at the Clan Forge, one leatherworker-bonecrafter, and everyone else does Tier 1 work with no recipe at all [PROPOSAL, it explains why scrap-grade gear is everywhere].

---

## 8. Regional and racial material traditions (short; full sets in `codex/lore/dnd-racial-gear-sets.md`)

| Region and people | Signature materials ([CANON] `codex/materials/overview.md`) | Gear tradition [PROPOSAL] |
|---|---|---|
| Lunarest, humans | Ironvein Ore, Hearthroot, Common Spirit Dust | Garrison leather and mail, guild-stamped steel, the baseline everyone else is compared against |
| Valefrost, dwarves and frostborn | Rimeiron, Glacial Marrow, Frostbloom, monocrystals, mono steel | Heavy mail and plate, hallmarked bars, fur-lined cold kit |
| Myrrhwood, beastfolk and goblins | Bonewood, Ashroot Fungus, Clanmark Ore, Myrrhwood Hide | Bone-and-hide, scrap iron, poison and gas, "cheap to acquire, quietly useful" |
| Sunmarch, orcs | Sunforged Iron, Redroot Pepper, Cracked Bloodstone | Heavy forged edges, fire-tolerant gear, big hides |
| Azure Expanse, elves | Skyglass Ore, Moonpetal, Prism Dust | Light, Wisdom-friendly foci, fine cloth |
| Wraith Isles | Echostone | Competitive gear flavor |

---

## 9. Conflicts with canon, and open items

Where the codex and the proposal disagree, canon wins and the proposal bends.

1. **"Epic" is not on the rarity ladder.** `organic.md`, `inorganic-and-salvage.md`, `magical-and-spirit-tied.md` and `recipes-spirit-line.md` use "Epic". The ladder is Common, Uncommon, Rare, Legendary, World. I read every "Epic" as Legendary, as the Book One file already does. A sweep should fix the four files.
2. **Ironwood is not a codex material.** Use Bonewood, Thornwood Bark or Hollow Heartwood, or approve a new node.
3. **No woodworking, tailoring or wicker profession exists.** Six professions, two active per character. I placed them inside Bonecrafting/Leatherworking and Smithing and flagged it OPEN.
4. **No Legendary hide, bone or cloth is named.** GT7 and GT8 leather and bone sets need either Pristine Rare stock plus a Legendary catalyst (my reading) or new Legendary beasts. The Book One file keeps Fallstone Iron and Elderbeast Marrow as the only Legendary farmed materials.
5. **Sunforged Iron and Skyglass Ore have no stated rarity.** I placed them at GT5, Rare. OPEN.
6. **Scrap iron, Clanmark Ore and Ironvein Ore overlap.** The codex calls Ironvein the default starting metal and Clanmark "low-grade but stubbornly common" and "most other regions treat as junk". I treat Clanmark as the goblin-camp scrap-grade metal and Ironvein as the Lunarest standard. They smelt together at the camp forge (Bloodhurst Slag, Book One file).
7. **Plain steel is not a named material.** The Book One file says Mountain Coal is needed "to smelt steel" and names Hallmarked Steel Bar. "Garrison Steel" is my generic term for undistinguished steel.
8. **Gear levels versus legacy gear.** Legacy pieces run ahead of level. Not a conflict, but the writer should not read GT bands as hard walls.
9. **GT level bands** are placeholders and need the author.
10. **The chapter-11 draft** uses Common and Rare items (Ironhide Chestplate, Vanguard's Greaves, PK Raiding Crest). Chapter 11 is flagged for rewriting, so these are treated as soft.

---

## 10. Sources

- D&D 5e equipment (SRD-based Basic Rules text, trade goods): https://www.dndbeyond.com/sources/dnd/basic-rules-2014/equipment
- Albion Online gear tiers: https://guildorder.com/games/albion/wiki/gear-tier-system and https://heaven-guardian.com/albion-online-gear-guide/ (both are community write-ups, not the official wiki, which returned an access error; verify names against the client before relying on them).
- Repo files named inline.
