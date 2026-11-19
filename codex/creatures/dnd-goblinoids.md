# D&D Goblinoids Adapted to Eryndal

Goblin, Hobgoblin, Bugbear, Warchief, Totem-bearer, Wolfriders, and their relatives (kobold, orc, ogre, gnoll, hill giant).

**Status:** research and proposal file, written for the author's request to ground HGO's baseline in how Dungeons and Dragons works, translated into our system (reworded and reformatted, never copied). Not author-approved. Nothing here is on the page. Everything marked [PROPOSAL] can be changed or dropped.

**Companion files:** `codex/creatures/dnd-bestiary-adaptation.md` (54 further monsters across Classes I to IV and all six regions) and `codex/creatures/dnd-monster-mapping-note.md` (challenge rating, hit dice, types, and the one-line panel).

**Provenance rule (CANON).** `codex/creatures/overview.md` says the creature files are "original to HGO, described functionally only, not modeled on or naming any outside reference". Provenance for borrowed material is kept in one place (`outline/bkc-reuse-map.md` does this for the BKC material). These three `dnd-*` files are that provenance home and name D&D on purpose. When an entry is promoted into `class-1.md` to `class-4.md`, strip the D&D names and the [SRC] tags and keep the in-world text only.

## How to read the tags

- **[SRC Sn]** paraphrased from the source with key Sn in the table below. "fetched" means I read the page this session. "search summary" means the page itself blocked me and the claim rests on a search-result summary, so treat it as lower confidence.
- **[CANON path]** stated in the repo. `ledger` means `outline/canon-ledger.md`. Later ledger entries beat earlier ones.
- **[PROPOSAL]** invented here.
- No em dashes or en dashes anywhere. Ranges are written with "to".

## Source key

| Key | What | URL | Status |
|---|---|---|---|
| S1 | SRD license page (SRD 5.1 under OGL 1.0a and CC-BY-4.0; SRD 5.2 of April 2025 and 5.2.1 of May 2025 under CC-BY-4.0, attribution the only requirement) | https://www.dndbeyond.com/resources/1781-systems-reference-document-srd | fetched |
| S2 | SRD 5.1 full monster list with CR, type, HP, hit dice (322 entries) | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&limit=400 | fetched |
| S3 | SRD 5.1 goblin, hobgoblin, worg, wolf, dire wolf, kobold, orc, ogre, gnoll, hill giant | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&slug__in=goblin,hobgoblin,worg,wolf,dire-wolf,kobold,orc,ogre,gnoll,hill-giant | fetched |
| S4 | SRD 5.1 bugbear | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&search=bugbear | fetched |
| S5 | SRD 5.2 goblin family (Goblin Warrior, Minion, Boss; Hobgoblin Warrior, Captain) | https://api.open5e.com/v2/creatures/?document__key=srd-2024&name__icontains=goblin | fetched |
| S6 | SRD 5.2 bugbear (Warrior, Stalker) | https://api.open5e.com/v2/creatures/?document__key=srd-2024&name__icontains=bugbear | fetched |
| S7 | SRD 5.2 worg | https://api.open5e.com/v2/creatures/?document__key=srd-2024&name__icontains=worg | fetched |
| S8 | SRD 5.2 full creature list with types (331 entries) | https://api.open5e.com/v2/creatures/?document__key=srd-2024&limit=400 | fetched |
| S9 | SRD 5.1 giant rat, stirge, giant bat, giant spider, animated armor, skeleton, zombie, ghoul, shadow, wight, mimic, gelatinous cube | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&slug__in=zombie,skeleton,ghoul,shadow,wight,mimic,gelatinous-cube,giant-rat,stirge,giant-bat,giant-spider,animated-armor | fetched |
| S10 | SRD 5.1 owlbear, griffon, harpy, basilisk, ankheg, giant scorpion, manticore, minotaur, chimera, bulette, hydra, wyvern | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&slug__in=owlbear,griffon,harpy,basilisk,ankheg,giant-scorpion,manticore,minotaur,chimera,bulette,hydra,wyvern | fetched |
| S11 | Wikipedia, Goblin (D&D): history, tribes, mounts | https://en.wikipedia.org/wiki/Goblin_(Dungeons_%26_Dragons) | fetched |
| S12 | Wikipedia, Hobgoblin: folklore origin and D&D use | https://en.wikipedia.org/wiki/Hobgoblin | fetched |
| S13 | Wikipedia, Bugbear: folklore origin | https://en.wikipedia.org/wiki/Bugbear | fetched |
| S14 | Wikipedia, Kobold: German folklore origin | https://en.wikipedia.org/wiki/Kobold | fetched (folklore half only) |
| S15 | Wikipedia, Ogre: folklore and D&D use | https://en.wikipedia.org/wiki/Ogre | fetched |
| S16 | Gnoll origin (Dunsany's gnoles, 1974 first appearance, hyena look from 1977), Greyhawk wiki | https://greyhawkonline.com/greyhawkwiki/Gnoll | search summary (page blocked) |
| S17 | Pathfinder 1e goblin organisation (gang, warband, tribe, mounts) | https://pathfinder.d20srd.org/bestiary/goblin.html | search summary (page blocked) |
| S18 | Old-school goblin and hobgoblin lair numbers (1-1 HD and 1+1 HD, chief with bodyguards) | https://sites.google.com/view/vile-monsters/monsters/goblin | search summary |
| S19 | 4th edition monster roles (Brute, Soldier, Artillery, Skirmisher, Lurker, Controller, Leader) | https://www.enworld.org/threads/should-explicit-monster-roles-return.704433/latest | fetched (fan thread) |
| S20 | Old-school monster rules (hit dice drive attacks and saves, morale, number appearing, treasure types) | https://digital-gm.pages.dev/docs/ose-rules/monsters/general/ | fetched |
| S21 | Monsters left out of the SRD as Product Identity (beholder, mind flayer, displacer beast, umber hulk, yuan-ti and others) | https://www.enworld.org/goto/post?id=5871683 | search summary |
| S22 | SRD 5.1 damage vulnerabilities, resistances and immunities for the undead, constructs, giants and dragons used in the companion file | https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&slug__in=skeleton,zombie,ghoul,shadow,wight,mummy,wraith,gargoyle,gelatinous-cube,ice-mephit,hell-hound,troll,frost-giant,young-white-dragon,adult-white-dragon,adult-green-dragon,air-elemental,stone-golem,shambling-mound,vampire-spawn,vampire,hydra,mimic,animated-armor | fetched |
| S23 | Open5e goblin search incl. third-party Goblin Boss, Warlock, Alchemist, Hobgoblin Captain and Warlord entries | https://api.open5e.com/v1/monsters/?search=goblin&limit=50 | fetched |

**Licensing note.** [SRC S1] The SRD 5.1 is available under both OGL 1.0a and CC-BY-4.0, and the SRD 5.2 series only under CC-BY-4.0 with attribution as the one requirement. This file paraphrases stat lines and ideas and renames everything, which is what the author asked for. It deliberately avoids the monsters Wizards kept out of the SRD (beholder, mind flayer, displacer beast, umber hulk and the like) [SRC S21], so there is no close reskin of those anywhere in the three files. "Goblin", "hobgoblin", "bugbear", "kobold" and "ogre" are older folklore words [SRC S12, S13, S14, S15], not D&D coinages. "Gnoll" is a D&D-lineage word [SRC S16], so the gnoll relative below is renamed. Suggested attribution line if the author ever publishes the underlying data: "Includes material from the System Reference Document 5.1 and 5.2, by Wizards of the Coast LLC, licensed under CC-BY-4.0" (wording is mine; check the license preamble in the SRD PDF).

## House conventions used in this file

1. **Natural weapons file under a Way.** [PROPOSAL] Beasts and natural-weapon creatures list innate attacks under the Way their motion resembles: bites, claws, grabs and slams under **Fist** (hand to hand, improvised weapons, `codex/combat/way-of-the-fist.md`); thrusts, gores and charges under **Spear**; cleaves and heavy swings under **Axe**; cuts under **Blade**; spat or thrown volleys under **Bow**. This lets every creature art name a Way and a tier 1 to 7, as the author asked.
2. **Art line format.** [PROPOSAL] **Name** (Way Tn, SP cost as a share of the pool, cooldown): effect and limiter. The cost and cooldown ladder is in the mapping note. SP and MP pools for creatures follow 24 plus level, which fits the two canon points (25 at level 1, 32 at level 8) [CANON `codex/lore/hp-sp-mp-resource-pools.md`].
3. **Passives.** No cost. Every passive states a **trigger** and a **limiter** [CANON rule derived in `outline/research/ability-system-audit.md` section 2.4].
4. **Kit skills.** Goblin Gas, Goblin Flare, Toxic Breath and Challenging Howl are goblin kit skills, not Way techniques and not Book spells, and run on SP [CANON ability audit 1.1].
5. **No creature summoning.** Anything D&D calls "summon" becomes a call to creatures already nearby, as the Chitin Warlord's Chitter Call already does [CANON `codex/creatures/class-3.md`, `codex/lore/crafting-and-alchemy.md`].
6. **Hands.** Goblin hands have fingers, never claws, in every description [CANON ledger, "Goblin hands have fingers, not claws"].
7. **Panels.** Every entry carries a one-line placeholder panel in the page style of the Enforcer (`[THRASH CLAN ENFORCER: LV 3] [HEALTH: 48/48] [POWER: 5] [SPEED: 3]`, `chapters/chapter-04.md`). Numbers are placeholders from the mapping note's formulas, exactly as the ledger flags the Enforcer's own numbers as placeholders.

## 1. What D&D does with goblinoids

### 1.1 The stat lines

| Creature | SRD 5.1 (2014 rules) | SRD 5.2 (2024 rules) |
|---|---|---|
| Goblin | Small humanoid (goblinoid), CR 1/4, 7 HP, AC 15, scimitar and shortbow, Nimble Escape (Disengage or Hide as a bonus action) [SRC S3] | Goblin Warrior CR 1/4 (10 HP), Goblin Minion CR 1/8 (7 HP), Goblin Boss CR 1 (21 HP, AC 17, Redirect Attack reaction: swap places with a nearby ally so the ally takes a hit). All three are type **Fey** [SRC S5, S8] |
| Hobgoblin | Medium humanoid (goblinoid), CR 1/2, 11 HP, AC 18, Martial Advantage (extra damage once per turn if an ally is next to the target) [SRC S3] | Hobgoblin Warrior CR 1/2 (Pack Tactics), Hobgoblin Captain CR 3 (58 HP, Aura of Authority: it and nearby allies gain advantage on attacks and saves). Type **Fey** [SRC S5, S8] |
| Bugbear | Medium humanoid, CR 1, 27 HP, AC 16, Brute (one extra damage die on melee weapon hits), Surprise Attack (extra 2d6 against a surprised target in the first round) [SRC S4] | Bugbear Warrior CR 1 (33 HP, 10 ft reach Grab), Bugbear Stalker CR 3 (65 HP, Quick Grapple bonus action, Abduct: moves a grappled target without extra movement cost). Type **Fey** [SRC S6, S8] |
| Worg | Large monstrosity, CR 1/2, 26 HP, speed 50, bite can knock prone [SRC S3] | Large **Fey**, bite gives the next attack on that target advantage [SRC S7] |
| Kobold | Small humanoid, CR 1/8, 5 HP, Sunlight Sensitivity, Pack Tactics [SRC S3] | Kobold Warrior, type **Dragon** [SRC S8] |
| Orc | Medium humanoid, CR 1/2, 15 HP, Aggressive (bonus action to close on a visible enemy) [SRC S3] | no orc in the 331-entry SRD 5.2 creature list [SRC S8] |
| Ogre | Large giant, CR 2, 59 HP, AC 11, greatclub and javelin [SRC S3] | Ogre, giant, 68 HP [SRC S8] |
| Gnoll | Medium humanoid, CR 1/2, 22 HP, Rampage (after dropping a foe in melee, a bonus move and bite) [SRC S3] | Gnoll Warrior, type **Fiend** [SRC S8] |
| Hill giant | Huge giant, CR 5, 105 HP, two greatclub attacks, thrown boulder [SRC S3] | Hill Giant, giant, 105 HP [SRC S8] |

### 1.2 How the family is organised in D&D

- **Three bodies, three jobs.** Goblins are small, cunning and numerous. Hobgoblins are disciplined soldiers who run tribes and legions [SRC S12]. Bugbears are big hairy ambushers [SRC S4 (Surprise Attack, Brute), S13]. The three sit under one "goblinoid" umbrella [SRC S11].
- **Leaders.** A tribe is led by its strongest member, tribes range from small gangs to about 400, leaders are sometimes non-goblins who use goblins as expendable soldiers, and larger tribes ride wolves or dire wolves or ally with worgs [SRC S11]. The 3.5e and Pathfinder organisation is a gang of 4 to 9, a warband of 10 to 16 on goblin dogs, and a tribe of 17 or more with one sergeant per 20 adults, one or two lieutenants, one leader, and 10 to 40 mounts [SRC S17, search summary]. An old-school lair has a chief with bodyguards, with females and young on top [SRC S18, search summary].
- **Old-school yardstick.** Goblins were 1 minus 1 hit dice and hobgoblins 1 plus 1 [SRC S18], and in that rules family hit dice drive attack rolls, saves, XP and the morale rating, with "number appearing" and a treasure type per monster [SRC S20]. The goblin therefore threatens by numbers and morale, not by single-body strength.
- **Boss ranks.** The 2024 rules give each family a minion, a warrior, and a boss or captain tier [SRC S5, S6]. The 4th edition role vocabulary (Brute, Soldier, Skirmisher, Artillery, Controller, Lurker, Leader) fits them cleanly: goblin = skirmisher, hobgoblin = soldier or leader, bugbear = brute or lurker [SRC S19, fan thread, lower confidence].
- **Retyping.** The 2024 rules retype goblinoids from humanoid to fey and kobolds to dragon [SRC S8]. HGO already has its own type word for goblins (see section 2), so the retyping is ignored.
- **Folklore roots.** "Hobgoblin" comes from "hob", an English household goblin, first recorded about 1530 [SRC S12]. "Bugbear" is a Middle English word for a frightening bear-like bogey [SRC S13]. "Kobold" is a German household or mine spirit [SRC S14]. "Ogre" is a French folk monster popularised by Perrault [SRC S15]. "Gnoll" traces to Lord Dunsany's gnoles and took its hyena look in 1977 [SRC S16].

### 1.3 Design takeaways used below [PROPOSAL]

1. A goblin fight is a **numbers and nerve** fight: the pack is the monster, and morale collapses when the leader falls.
2. **Rank is role.** Grunt = skirmisher, hobgoblin = soldier, bugbear = ambusher, boss = buffer and redirector. HGO already has rank as an evolution, so this lines up with canon.
3. A leader's best trick is **making someone else take the hit** (Redirect Attack) or **making allies fight better** (Aura of Authority, Martial Advantage).
4. **Mounts** turn a Class I mob into a Class II mobile threat, and wolves are the mount.

## 2. What canon already fixes

| Fact | Source |
|---|---|
| Thrash Clan Enforcer: recruits, LV 3, panel HEALTH 48/48, POWER 5, SPEED 3 (numbers flagged placeholder), speak in full sentences | `chapters/chapter-04.md`, ledger "Goblin speech and intelligence", "Provoke status panel" |
| Ru: a true runt goblin mob at LV 1 (short broken words, stutter). Shiv's one-time blessing makes him a Hobgoblin at LV 5, evolves Goblin Gas into Toxic Breath, and he speaks in patterns afterwards. Title is Disciple of Elder Nykri | `codex/characters/young-goblin-companion-candidate.md`, `codex/lore/companion-troop-system.md` |
| Zinka: Thrash scout, Hobgoblin, LV 7, has Toxic Breath, full sentences | `codex/characters/pk-wraith-raiding-party.md` |
| Wyx: LV 25 Hobgoblin, gold tag, blade dancer. Sevish: LV 80 Hobgoblin, gold tag, axe berserker. Both are human height, much bigger than camp goblins, and both have Toxic Breath listed but never use it. Gold-tag NPCs do not level unless they become Tatsuya's troops | `codex/characters/thrash-siblings-ability-lists.md`, `codex/lore/companion-troop-system.md`, ledger |
| Drosh: hobgoblin lieutenant with Silent Three Fang (Fist, Tier 2 to 3) and Veil-Pierce Gaze (Fist, Tier 4 to 5) | `codex/characters/goblin-squad-companions.md`, `codex/combat/way-of-the-fist.md` |
| A goblin becomes a hobgoblin only by leveling steadily through combat without dying. Most goblins never live long enough. Only two hobgoblins in the camp (Sevish, Wyx), a third with Tatsuya's Shiv Goblin form, a fourth with Ru. Zinka makes a fifth | `codex/locations/bloodhurst.md`, `codex/characters/pk-wraith-raiding-party.md` |
| The camp holds about 25 goblins in total, "almost everyone is a grunt", recruits arrive on the Thrash ship, and the camp takes about a month to refill, which is why the Goblin March is monthly | `codex/locations/bloodhurst.md`, ledger |
| Goblin race: Courage 4, Power 4, Wisdom 2, Speed 7, Fortune 9, Energy 4. Racials Scavenger's Eye and Nimble Hands. No resistances. Wisdom 2 is far under the Wisdom 18 casting gate | `codex/races/goblin.md` |
| Goblin Gas costs 10 of 25 SP, 30 s cooldown, radius poison that stacks to 4x with a stun chance, and can be ignited. Goblin Flare costs 5 SP, 30 s. Only players start with both. NPC goblins may have gas, flare or both, most never use the flare tree, and none have used the combination | ledger, `codex/lore/preserved-misc-mechanics.md` |
| Only Thrash-clan goblins can enter villages and settlements. Every other clan reads as feral and is barred. Feral clans read red to a Thrash goblin | `codex/lore/goblin-clan-culture-and-feral-stigma.md`, `codex/lore/npc-tag-system.md` |
| Myrrhwood: the Beast Kingdom holds the walled half. The rest is the Black Lands, many small goblin camps fighting each other with no kingdom. Six goblin provinces and seven Thrash-type clans | `codex/locations/eryndal-world-overview.md`, ledger |
| Creature classes I to IV. Ash Wolf is Class I, Frostmaw Direwolf (leads Ash Wolf packs) is Class III, Greyvast is Class III. Chitin Warlord's summon is only a call to nearby hive members | `codex/creatures/class-1.md`, `class-3.md` |
| Orc is a playable race (Sunmarch) with Unbroken, poison resistance, frost weakness | `codex/races/orc.md` |
| Existing creature types for the "creature-type bonus" gear affix: beast, undead, humanoid, demihuman | `codex/lore/secondary-combat-stats.md` |
| NPCs speak in a medieval-fantasy register ("D&D-like") in their own world | ledger "Speech register and sources" |
