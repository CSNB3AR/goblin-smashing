# HGO Ability System: Rules Brief for Sevish and Wyx Thrash

Audit of the Goblin Smashing repo (clone: /tmp/claude-0/-home-user/5e9a200d-a35d-565e-ba33-6840920e721f/scratchpad/gs). All paths below are relative to that clone. "L" means a line number. Labels used throughout:

- CANON = stated in a file or on the page.
- INFERRED = my reading of canon data points, not stated.
- PROPOSAL = a gap the designer must fill; nothing in the repo says it.

Source order rule used: page text (chapters/) beats codex; later ledger entries (outline/canon-ledger.md) beat earlier ones and beat codex files where they conflict.

---

## 1. The two ability categories, and how they are organised

### 1.1 Physical arts vs spells

CANON. Two separate skill trees.

- **Physical Arts.** "A distinct skill tree from spellcasting entirely, Power/Speed-driven rather than Wisdom-gated, fueled by SP rather than MP" (codex/combat/physical-arts-overview.md L3). Default for Orc, Beastfolk and Goblin (same file L3). Northern name: Reinforced Arts, same system (L17).
- **Spells (magic).** Eight "Books" (schools): Embers, Frost, Tempest, Stone, Tides, Radiance, Veil, Arcane (codex/magic/overview.md L27 to L34, L47). Fueled by MP, scales with Wisdom (codex/lore/hp-sp-mp-resource-pools.md L8). Opening any school needs Wisdom 18 (magic/overview.md L7). Goblins are "restricted, not hard-locked" (codex/races/goblin.md L29). Tatsuya's Shaman's Veil is a bond-granted bypass (races/goblin.md L31).
- **Goblin kit skills** (Goblin Gas, Goblin Flare, Toxic Breath, Challenging Howl, Rune Priming) are not Way-of techniques and not Book spells. They show a STAMINA COST on the page (chapters/chapter-05.md L27, L49), so they run on SP. CANON for Gas and Flare; INFERRED for Howl and Toxic Breath (no cost has ever been shown for them).
- **Both Thrash siblings are martial only.** "Both are martial. No magic outside the goblin kit." (codex/characters/thrash-siblings-ability-lists.md L3). Tatsuya's own read on the page: "Not a spell on the list" (chapters/in-progress/now/chapter-10-assembling-the-assault-team.md L133). So any new Sevish or Wyx ability must be a Physical Art or goblin kit skill, never a Book spell. Spells would also hit the Wisdom-18 gate, which a Hobgoblin does not clear by race (Goblin Wisdom base is 2, races/goblin.md L11).

### 1.2 How Physical Arts are organised

CANON (codex/combat/physical-arts-overview.md and the five Way files).

- Five **Ways**, one per weapon category: Fist, Spear, Blade (sword), Axe, Bow. Each file is a "representative tiered move list (not exhaustive, flagged as expandable)" (overview L22).
- Tiers 1 to 7. Tier 7 "is the practical ceiling", one below magic's Tier 8 (overview L7).
  - Tier 1: "a single basic trained technique. Three per weapon category ... as the standard starting kit" (L9).
  - Tier 2 to 3: technique refinement, "small combo chains of 2-3 moves" (L10).
  - Tier 4 to 5: "real multi-technique combos, a fight-defining sequence" (L11).
  - Tier 6: "signature techniques, distinctive enough to be recognized by other players/NPCs on sight" (L12).
  - Tier 7: "battlefield-altering signature moves, rare, most Physical Arts practitioners never get here" (L13).
- Per-Way tables list: three Tier 1 moves, one Tier 3 combo, and **blank placeholders at Tier 5 and Tier 7** for Axe, Blade, Spear, Bow (e.g. codex/combat/way-of-the-axe.md L9 to L14, way-of-the-blade.md L9 to L14). Fist has Silent Three Fang at Tier 2 to 3, Veil-Pierce Gaze at Tier 4 to 5, blanks at 6 and 7 (way-of-the-fist.md L9 to L15).
- Axe Tier 1: Split Strike, Hook Pull, Haft Check. Tier 3: Momentum Chain. Blade Tier 1: Clean Draw, Parry Riposte, Guard Break Swing. Tier 3: Flowing Edge.
- Named heavy-target move: **Upheaval**, "roughly Tier 4-5", "available to any category that can get a weapon or fist under the target", home Way left open (overview L18).
- **Martial-master rule** (overview L32): someone who has "genuinely mastered a weapon category (a real, earned threshold, not a level number alone ...)" can "develop and name their own technique", but it "has to be built the way any Physical Arts technique is, tiered, SP-costed, and consistent with what that weapon category can actually do." This is the strongest in-canon licence for inventing Sevish and Wyx techniques, and also the constraint on them.

### 1.3 How spells are organised

CANON (magic/overview.md L9 to L17, magic/tier-reference.md, each book file).

- Tiers 1 to 8; Tier 8 is the practical ceiling for players.
- 1 to 2 single small effect; 3 to 4 area or duration control; 5 to 6 chained or triggered effects; 7 reshapes the battlefield, rare; 8 reality bending, boss-tier only.
- Each Book is a tier table with one headline spell per band (book-of-embers.md L7 to L13).
- Amplify: spend extra MP to cast above the unlocked tier, "real cost and real risk" (magic/overview.md L42).

### 1.4 Mastery (a separate axis from tier)

CANON (codex/lore/mastery-system.md).

- Scale 1 to 10 (L13). 100 XP per level, 1,000 XP to master (L15). Grown by use, not points.
- Discipline Points and Crafting Points "unlock the tree and set the tier ceiling; Mastery is the separate, slower climb of how well a character actually executes" (L11).
- Mastery gates tier access: "Roughly 25% Mastery in a book unlocks access to about the first half of its tiers ... six and eight specifically, stay locked out entirely below roughly 75% Mastery" (L19). This is written for books; applying it to Ways is INFERRED.
- At master level a character can teach (L23).

### 1.5 What a tier means in practice, and how tier gates to level

CANON data points only (there is no level to tier table anywhere in the repo):

- Arya, level 10 to 11, Elf Spellforger: cannot cast Tier 6; Hushveil reads Tier 3 on the page (codex/characters/arya.md L70; outline/canon-ledger.md L97; chapters/in-progress/now/chapter-11-silence-and-fire.md L517).
- Tatsuya, level 8: Ancient Bone Flame Barrage shows **TIER 5** in the battle report (chapter-11 L521).
- Ru, level 5 Hobgoblin, and Zinka, level 7 Hobgoblin, have Toxic Breath (companion-troop-system.md L24; codex/characters/pk-wraith-raiding-party.md L22).
- Drosh (Hobgoblin lieutenant): Silent Three Fang (Tier 2 to 3) and Veil-Pierce Gaze (Tier 4 to 5) (goblin-squad-companions.md L19; way-of-the-fist.md L12 to L13).
- Tier 6 and 8 need about 75% Mastery (mastery-system.md L19).

INFERRED reading: tier is capped by points and Mastery, not by a hard level number. A level 8 character can touch Tier 5 (with Amplify or setup cost, ABF cost him 25 of 32 MP, call-of-the-bones-necklace.md L44), a level 10 to 11 caster cannot do Tier 6. No source says what tier a level 25 or level 80 fighter reaches.

### 1.6 How many abilities a character typically has

CANON data points, no rule:

- Level 1 Tatsuya: 2 skills (Gas, Flare) plus a mystery-box passive (chapters/chapter-04.md L73 to L110; chapter-05.md L17 to L19).
- Arya, level 10: five spell unlocks plus Hushveil base (codex/characters/arya.md L70).
- Sevish (L80): seven entries; Wyx (L25): six entries on the author-rejected panels (thrash-siblings-ability-lists.md; chapter-10 L99 to L131). Tatsuya's reaction there: "Every single one of them is a way to hit harder" (chapter-10 L133).
- "Level-ups also occasionally grant a new Codex Entry (skill or minor item)" and Codex Entries are "introduced organically, two to four per major arc, never as an upfront catalog dump" (codex/lore/leveling-and-progression.md L8, L10).
- Per Way, 3 Tier 1 techniques are the starting kit (physical-arts-overview.md L9).

INFERRED: a veteran Physical Arts user plausibly holds 3 starter techniques, 1 or 2 combos, and 1 signature per tier band reached. That is 5 to 8 entries for a high-level fighter, so the existing 6 and 7 counts are not unreasonable. The problem with the rejected panels is not the count.

---

## 2. Resources, cooldowns, damage, passives, rarity

### 2.1 Pools

CANON.

- HP: base 50, plus 3 per level (hp-sp-mp-resource-pools.md L7). Check: level 8 shows 65/65 (HP formula note L7; chapter-11 L23 shows HP 65/65, SP 32/32, MP 32/32).
- Level 1: HP 50, SP 25, MP 25 (chapter-04.md L47). Level 3: 25/25 (hp-sp-mp L8). Level 8: SP 32, MP 32.
- The formula is not universal: Arya, level 10 Elf, shows HP 88, SP 44, MP 72 (codex/characters/arya.md L54 to L56). The formula applied to level 10 would give 80, so race and stats change it.
- INFERRED only: applying the player HP formula to Wyx (level 25) gives 125 and Sevish (level 80) gives 290. No canon NPC pool exists. Level 3 Thrash Enforcer shows HEALTH 48/48, Power 5, Speed 3, and the ledger flags those numbers as placeholders (chapter-04 L187 to L191; canon-ledger.md L318).
- "Abilities have real cooldowns and drain these pools. No spamming, no infinite-use items" (hp-sp-mp L9). SP fuels "physical and item-based abilities ... drains faster when the item or weapon carries a magical augment" (L8).
- SP Regen derives from Speed + Energy (secondary-combat-stats.md L52).

### 2.2 Costs and cooldowns on the page

CANON (the only real examples).

| Ability | Cost | Cooldown | Source |
|---|---|---|---|
| Goblin Gas (radius, poison DoT stacks to 4x, chance to stun) | 10 SP of 25 | 30 seconds | chapters/chapter-05.md L27, L29; ledger L322 (30s replaces 45s) |
| Goblin Flare (signal, 2 damage) | 5 SP | 30 seconds | chapter-05 L49, L51 |
| Rune Priming | mana "on every attempt", "roll required" | 6 seconds between attempts | chapter-10 L159; ledger L1001 |
| Ancient Bone Flame Barrage (Tier 5 on page) | 25 MP of 32 | not stated | chapter-11 L509 |
| Hushveil (Arya, Tier 3) | "a large share" of her MP | 12 s effect (page), 15 s effect and 30 s cooldown (ledger) | chapter-11 L517; ledger L999 |
| Doppelganger's Band | 60 MP to activate (item) | not stated | codex/lore/battle-items-and-battlegear.md L24 |
| Challenging Howl (Sevish) | never shown | never shown | immobilise, 6 s on Tatsuya, 12 s on the kid (chapter-06.md L5 to L9) |

INFERRED scale: the only active stamina skills seen cost 20 to 40 percent of a level 1 pool at a 30 second cooldown; the one Tier 5 spell cost about 78 percent of a pool. Two Gases plus the Flare took Tatsuya from 25 to 0 SP in one fight (chapters/chapter-05.md L87, L113).

Every ability activation shows its skill name on the page (ledger L298). Abilities "must be triggered, by intent, channeling, a named skill or an action tied to a weapon or material"; Physical arts "fire off hits or a drawn arrow plus the intent" (ledger L296).

### 2.3 Damage number scale

CANON where it exists. There is **no canon number for level 25 or level 80**.

- Level 3: Goblin Flare 2 damage (chapter-05 L47); Gas plus Flare explosion shows 96 and 94 on 48 HP enforcers (chapter-05 L103; ledger L322 flags these as placeholders).
- Level 8: Tatsuya thinks he does "maybe six damage with my fists" (chapter-11 L87, his own estimate). Shiv-Touched Flare does 4 damage (ledger L999). Ancient Bone Flame Barrage, a Tier 5 combo burst: BASE 840, CRITICAL x2.19, TOTAL 1,840, killing four level 12 to 14 raiders (chapter-11 L522 to L529; raider levels in ledger L1001).
- Level 10 Arya: Physical AP 13, Magic AP 48 (arya.md L58 to L59).
- Standard potion at Tatsuya's tier heals about 15 HP over ten seconds (chapter-11 L225).
- Rule for the page: from Chapter 9 forward, damage, kills and healing surface as real numbers when a fight is live (five-disciplines-stat-system.md L18). But the ally panels in Chapter 10 were written with a "no numbers" rule (thrash-siblings-ability-lists.md L24). See conflict C5.

PROPOSAL (no canon): whatever number is used for Sevish and Wyx hits must sit visibly above the level 8 spell burst scale for a level 80, and must not exceed what the page needs. The safest approach the canon supports is to leave NPC numbers off the panel and show only text effects.

### 2.4 Passives

CANON precedents:

- Gambler's Gambit (unique passive, costs 1 skill point to equip, permanent, loot only) (chapter-04 L87 to L97; ledger L251).
- Whispers of Shiv: passive, Fortune scaling, recruitment (companion-troop-system.md L16).
- Bone Surge: passive. "Design rule: Bone Surge never hands Tatsuya a borrowed or generic effect. It only ever amplifies or redirects abilities that are already his." Amplify is Fortune-rolled; Reflect "crashes his Energy down to 1" (call-of-the-bones-necklace.md L35 to L38).
- Meditation: common baseline, slow SP and MP restore while stationary, no HP (preserved-misc-mechanics.md L17).
- Momentum Charm: "Brief Speed bump on landing a hit. Passive, no activation cost ... nothing to drain" (battle-items-and-battlegear.md L10).
- Goblin Rally: stat bonus scaling with nearby allied goblins (goblin-squad-companions.md L23).
- Elf passive: spells cost less mana (tatsuya-trap-bomber-brigand-archetype.md L88).

Derived rules (INFERRED from the above plus the no-spam rule):

1. A passive has no activation cost and cannot be spammed, so its power must come from a trigger, a condition, a roll, or a drawback.
2. A passive amplifies or reacts to things the owner already does (hit, kill, take damage). It does not create a new attack.
3. Anything that boosts damage with no ceiling needs a limiter (a cap, a decay, a cost, a drawback), as Reflect has its Energy crash.
4. A passive does not bypass the CC rules in codex/crafting/debuffs-and-resistances.md (L21 Physical row: stun, root, slow are "partially resisted by Power/Courage").
5. Weapon masteries ("War Axe Mastery", "Twin Sabre Mastery") have no canon precedent as named skills. Mastery in canon is a 1 to 10 progress meter on a skill or Way (mastery-system.md L13), not a passive ability. A "Mastery" passive on a panel conflicts with the Mastery system's vocabulary (see C6).

### 2.5 Rarity labels

CANON ladder (codex/lore/deck-building-rarity-and-classes.md L23 to L29): Common (white/gray), Uncommon (green), Rare (blue), Legendary (gold), World (purple, World Quest rewards only). The same scale is used for skills and items (L23).

Additional label on the page: **UNIQUE**. Chapter 4 prints "UNIQUE ITEM! GAMBLER'S GAMBIT!" and "GAMBLER'S EARRING" with the tag UNIQUE (chapters/chapter-04.md L85, L103). Unique items "scale with their user, unlike lower rarities, which cap at a level (even Legendary stays capped around level 80+)" (codex/objects/gamblers-earring.md L17). The ladder file does not list Unique and the canon ledger flags "Epic" as a label the ladder does not have (ledger L857). Where Unique sits relative to Legendary and World is not set. The roulette on the page lands on "white-hot" past "common, blue, gold" (chapter-04 L79 to L81).

What makes an ability Rare: **CANON is silent.** Evidence:

- Rarity shows as a color border on cards that "name, rarity-colored border, the stat bonuses it grants, and description text" (deck-building L33).
- Rare items "usually carried by veterans, guards and officers" (battle-items L28).
- Ru's shield technique "unlocks through rare-tier gear" (young-goblin-companion-candidate.md L21).
- Gambler's Gambit rolls for "Rare or higher quality loot" as the prize outcome (chapter-04 L93).
- Two entries in the rejected Chapter 10 panels are tagged RARE: Dance of Blades (Wyx), Earthsplitter and Pain Is Proof (Sevish) (chapter-10 L103, L123, L127). Normal skill panels for Gas and Flare carry no rarity tag at all (chapter-05 L17 to L51).

INFERRED: Rare means a distinctive, build-defining entry, probably Tier 4 or above for a Physical Art, and probably what overview L12 calls a "signature" (Tier 6, recognisable on sight). PROPOSAL: reserve RARE for at most one active per sibling plus at most one passive for Sevish; leave starter techniques unlabelled or Common.

---

## 3. How abilities are learned in canon today

All CANON unless marked.

| Route | Quote or fact | Source |
|---|---|---|
| Starter kit by Way | Three Tier 1 techniques per weapon category "as the standard starting kit" | physical-arts-overview.md L9 |
| Level-up | "Level-ups also occasionally grant a new Codex Entry (skill or minor item) from class/race lists or story rewards" | leveling-and-progression.md L8 |
| Racial or starting | Goblin Gas and Goblin Flare on the starting sheet. "Only players start with both" | chapter-05 L17 to L19; preserved-misc-mechanics.md L24 |
| Mystery box | Newcomer Mystery Box gives "a passive, a skill line, an item or a weapon" | canon-ledger.md L251, L255 |
| Skill points | Equipping Gambler's Gambit "COST: 1 SKILL POINT. PERMANENT." | chapter-04.md L95 |
| Quest and blessing | Shiv's direct blessing evolved Ru Goblin to Hobgoblin and Goblin Gas to Toxic Breath, "Shiv's own one-time act" | companion-troop-system.md L24 |
| Evolution rank-up | Goblin becomes Hobgoblin "only by leveling steadily through combat without dying" | codex/locations/bloodhurst.md L43 |
| Item grants ability | "description text that explicitly names any ability it unlocks"; necklace grants Bone Surge, Shiv-Touched Flare, Rune Priming | deck-building L33; call-of-the-bones-necklace.md L9 |
| Gear or materials unlock | Gadget Belt abilities "LOCKED, REQUIRES CRAFTING MATERIALS"; Ru's shield art through rare gear | chapter-05 L163; young-goblin L21 |
| Manuals | Absorbing "a crafting manual or technique" needs a joint Wisdom plus Speed check | five-disciplines-stat-system.md L7; mastery-system.md L27 |
| Reading | "time spent reading in the library ... can grant Wisdom or skill points" | codex/locations/grand-library-of-lunarest.md L11 |
| Use (Mastery) | "A character who unlocks a skill and never uses it stays at Mastery 1 indefinitely" | mastery-system.md L15 |
| Teachers | "Training with another player or NPC who has already mastered the skill accelerates the climb." Masters "unlock the ability to teach it to others, players included" | mastery-system.md L15, L23 |
| Self-invented | Martial-master custom technique | physical-arts-overview.md L32 |

Teachers and trust gates:

- Teaching is a real systemic mechanic, tied to Mastery 10 ("master level") (mastery-system.md L23). Book of the Veil explicitly bottlenecks on teachers (book-of-the-veil.md L5). Crafting apprenticeship gives a "Trainer bonus to Mastery" (merchant-license-auction-and-jobs.md L95, a proposal document).
- Tatsuya's own future arc is "training disciples" once he masters Shaman's Veil (mastery-system.md L23).
- Affiliation bands: Trusted (50 to 79) "real requests get taken seriously, some restricted access opens"; Allied (80 to 100) "treats the player as one of their own" (affiliation-and-reputation-system.md L17 to L18). Current numbers: Thrash clan 45 to 47 (chapter-10 L67); Wyx personally 45 to 52 in Chapter 6, 52 to 56 in Chapter 11 (wyx-thrash.md L21).
- **No file says a Thrash master teaches a technique, or sets an Affiliation threshold for learning one.** The Affiliation file only says Allied unlocks the "earned" elder status (L41). Any "Sevish or Wyx teaches Tatsuya" beat is a PROPOSAL (see section 6, G6).
- NPC levels are frozen: non-troops "cannot gain levels and stay at the level they are held at until they become troops of the player" (companion-troop-system.md L41; sevish-thrash.md L21; wyx-thrash.md L19). That is a level rule, not a learning rule, but it means their kits are fixed unless they join.

---

## 4. Gold-tag NPCs and how their power is bounded

CANON (codex/lore/npc-tag-system.md).

- Gold = "world-boss-tier or otherwise quest-critical/important NPC. Sevish and Wyx Thrash both carry gold tags." (L10).
- "Gold tags essentially never go hostile, except under real provocation ... If a gold tag does flip hostile, it's never just that one NPC, it's whatever faction stands behind them" (L10).
- Death is permanent for yellow and below; NPCs generally do not respawn (L11, L28). Sevish and Wyx cannot die in the monthly Goblin March: "at about 20% HP they go into a rage and retreat" (ledger L376).
- A proper name plus gold tag marks the significant NPC; "Thrash Clan Enforcer" is the mob read (npc-tag-system.md L12).
- Gold NPCs run "the most sophisticated" reactive AI: long memory, strategic reasoning (L20).
- **Levels are fixed.** Sevish L80, Wyx L25, both Hobgoblin; both "cannot level" (companion-troop L41; sevish-thrash L11, L21; wyx-thrash L11, L19). Their tags show level on the page (ledger L330 to L332; chapter-05 L187 to L189).
- **Panels.** Tatsuya got question marks in Chapters 5 and 6 "because he is too far below their level" (ledger L384; chapter-06 L9). From Chapter 10 he can inspect them because he is "now an ally of Thrash" (thrash-siblings-ability-lists.md L3).
- **Page rule for the ally panels:** "names with a short effect line for the martial ones; no numbers" (thrash-siblings-ability-lists.md L24). This is the rule the rejected draft followed.
- **Why Sevish stays off the field:** a level 80 "would send them home to bring more" (ledger L1034); the siblings are the camp's walls, "Like two level bosses" (ledger L1052; page line chapter-10 L93).
- **Credit rule:** if an NPC finishes a fight and Tatsuya lands no damage he "gets nothing (no experience, no drops, less than zero)" (ledger L1053). So any ability must not make the siblings a shortcut around Tatsuya's contribution, and must be consistent with them not wiping raiders.
- Power gap rule: "Large level gaps can bypass normal CC resistance" (debuffs-and-resistances.md L29). That is why Sevish (L80) can immobilise a level 3 for 6 seconds and a weaker NPC for 12.

Bounding rule that follows (INFERRED, anchored on the above): a gold-tag ability should be strong enough to read as boss tier against a party of level 8 to 14, while having a clear counter or cost, because (a) NPCs run cooldown-and-pool rules like everyone, (b) the story needs Tatsuya's party to contribute, (c) the siblings are described as walls, not killers.

---

## 5. What canon already says, topic by topic, with conflicts resolved

### 5.1 Challenging Howl

- First use: Chapter 5. A "war roar" out of the big tent; panel lines `SKILL: CHALLENGING HOWL` and `STATUS EFFECT: IMMOBILIZED` (chapter-05.md L175 to L177).
- Effect: Immobilize, whole body, sound-based, **not a root** (preserved-misc-mechanics.md L22; ledger L384). Duration 6 seconds on Tatsuya, 12 on the kid, "double his" (chapter-06 L5 to L9; Tatsuya's guess: weaker body or NPCs hit harder). It freezes the watchers and the kid, not Wyx (chapter-05).
- Name: the ledger calls "CHALLENGING HOWL" "the author's working name (OPEN)" (ledger L324), later used consistently on the page.
- Wyx: "a Howl, a smaller one than Sevish's ... hers freezes no one, it turns enemies on her. Every time a caster tries to reach past the wall at the archers she howls and the spell comes to her; they cannot pick another target" (ledger L1044).
- **Conflict C1.** Sevish's Howl is a stun (immobilise); Wyx's is a taunt (forced targeting). The rejected panel gave Wyx the line "ENEMIES WITHIN EARSHOT ARE FORCED TO FIGHT THE USER" (chapter-10 L109) and left Sevish's blank. The ability list's gloss calls Wyx's "the same roar on a shorter leash" (thrash-siblings L10). The author-dictated ledger entry L1044 is more precise: different effect, not just a shorter range. **Winner: ledger L1044 (latest, author-stated).** Treat it as a related family skill with two different effects, one immobilise and one taunt. The panel shorthand "shorter leash" is flavor only.
- Gap: no cost, cooldown, range or tier has ever been shown.

### 5.2 Goblin Gas and Toxic Breath

- Goblin Gas: radius poison, stacks to 4x, chance to stun, user not immune, can be ignited (chapter-05 L25). Toxic Breath is "his own baseline Goblin Gas evolving into a gut-charged toxic cloud" (young-goblin-companion-candidate.md L27). Granted to Ru by Shiv's blessing at the Hobgoblin evolution (companion-troop L24); Zinka also has it, a young Hobgoblin, source unexplained (pk-wraith-raiding-party.md L22 to L24).
- Wyx: "has Toxic Breath but never uses it because she thinks it is not ladylike" (wyx-thrash.md L27). Sevish: "Probably has not used Goblin Gas or Goblin Flare in a very long time; he was built on war" (sevish-thrash.md L27). Toxic Breath on Sevish's panel is "long unused" (thrash-siblings L24).
- **No conflict between files**, but a **design trap**: both siblings listing Toxic Breath on a panel contradicts nothing, yet it is the one entry on both panels with no effect text, and it makes the Hobgoblin tier look like a rank-up that grants Toxic Breath (consistent with Ru, Zinka). Keep it as a deliberately unused, low-key entry. Do not build either sibling's combat identity on it.
- NPCs may copy the gas plus flare combo "potentially" (preserved-misc-mechanics.md L24).

### 5.3 Thrash clan techniques and "advanced physical arts"

- The only statements are the two author notes: Sevish "uses advanced physical arts and Thrash clan techniques he rarely shows" (sevish-thrash.md L27); Wyx "fights with advanced physical arts and rarely used Thrash clan techniques" (wyx-thrash.md L27). Same phrase in preserved-misc-mechanics.md L24.
- **No clan technique is named anywhere in the repo.** "Advanced" is not defined; INFERRED: it means higher-tier Physical Arts, Tier 4 and above. "Rarely shows or uses" is a story constraint: they do not open a fight with their best moves.
- Searched for `Thrash clan technique`, `advanced physical`, `clan art` across codex, outline, chapters, archive, bible: only those three hits. The Way-of tables list nothing for Thrash.
- Thrash's identity facts to anchor any clan technique to: ranks are earned, hobgoblins run "on a system" (ledger L492, tent), clan law is no fighting among their own (ledger L362), they hold camps as "the walls" (ch10 L93), faith in Shiv.

### 5.4 Weapons and class of each sibling (conflict C2, C3)

- Sevish: two-handed battle axe, "always has" (sevish-thrash.md L11). Berserker (thrash-siblings L14; ch10 L117). Way of the Axe is the home Way. Kenpachi Zaraki model (sevish-thrash L23).
- Wyx: **dual sabres, Blade Dancer** (ledger L1060; chapter-10 L99, L113; thrash-siblings L5 to L6).
- **Conflict C2.** codex/objects/call-of-the-bones-necklace.md L21 says "Wyx uses dual daggers plus Physical Arts". Ledger L1060 and the Chapter 10 page say sabres. **Winner: ledger L1060 plus page (later, author-stated). Dual sabres.** The necklace file is stale.
- **Conflict C3.** codex/combat/way-of-the-bow.md L3 says the Bow Way is "Wyx's category". wyx-thrash.md L7 says "a fighter and not a ranger". **Winner: wyx-thrash.md and ledger L1060. Wyx is Way of the Blade (sabres), not Bow.** way-of-the-bow.md L3 is stale; flag for the author.
- Stray line: ledger L1034 (earlier formation plan, later held back to Chapter 11) says Wyx "shows the axe". Treat as an early slip, not a weapon change.
- Sevish and Wyx share the Hobgoblin tag; "Hobgoblin" has no race file (no codex/races entry). Facts: human height and build, evolved by levelling steadily (bloodhurst.md L43; ledger L354).

### 5.5 The author-rejected Chapter 10 panels

Provisional lists (thrash-siblings-ability-lists.md; chapter-10 L99 to L131). Problems measured against the system:

1. **No tier, no cost, no cooldown, no Way.** The Gas and Flare panels show cost and cooldown (chapter-05). Physical Art entries are supposed to be tiered and SP-costed (overview L32).
2. **Names not in the Way tables.** Rending Cleave, Earthsplitter, Whirling Edge, Winding Step, Dance of Blades appear in none of the Way files. Way of the Axe lists Split Strike, Hook Pull, Haft Check, Momentum Chain; Way of the Blade lists Clean Draw, Parry Riposte, Guard Break Swing, Flowing Edge.
3. **Mastery misused as a passive.** "War Axe Mastery" and "Twin Sabre Mastery" collide with the Mastery system (1 to 10 meter).
4. **Rarity tags inconsistent.** RARE sits on an active, a passive, and (for Sevish) two entries; the standard panels carry no rarity.
5. **Bloodlust and Pain Is Proof have no limiter.** Damage rising per kill and per wound, with no cap, no decay, no cost. Pools and cooldowns rule the system (hp-sp-mp L9).
6. **Earthsplitter and Rending Cleave overlap.** Both are big axe area hits; no Tier or cost separates them. Whirling Edge (Wyx) is the same shape as Rending Cleave (Sevish).
7. **Challenging Howl on Wyx's panel** repeats the same text as the ability name for the system effect, and the Toxic Breath lines are bare.
8. **"No numbers" rule** conflicts with the Chapter 9 forward rule for live numeric stats (five-disciplines L18). Ally inspection is not a live fight, so INFERRED: static numbers are optional.

Winner on conflicts C5 and C6: system rules above beat the provisional lists; the lists are author-rejected.

### 5.6 Other conflict notes

- **C4. Wyx level.** The author once said level 60; the ledger corrects it: "Wyx is canon level 25, so the author's "60" was not used" (ledger L1034). Winner: level 25.
- **C7. ABF tier.** The Veil file puts Ancient Bone Flame Barrage at Tier 1 to 2 start (book-of-the-veil.md L17) and the necklace file says it is "capped well below its full potential" (call-of-the-bones-necklace.md L44); the page prints TIER 5 at level 8 (chapter-11 L521). Winner: page. It matters for this brief because it shows a level 8 character can use a Tier 5 effect through setup cost and Amplify, so an NPC "ceiling by level" cannot be derived tightly from level.
- **C8. Rarity ladder vs "Unique".** See 2.5. Winner: page text (UNIQUE exists); ordering unset.

---

## 6. Constraints a new ability must satisfy, and gaps

### 6.1 Constraints (CANON or direct INFERRED from CANON)

A new Sevish or Wyx ability fits the system only if it:

1. **Is a Physical Art or goblin kit skill.** Not a spell, no Book, no MP (no magic outside the goblin kit, thrash-siblings L3; hp-sp-mp L8).
2. **Names its Way** (Axe for Sevish, Blade for Wyx; Fist and others only if the story needs a different weapon) or is explicitly a Thrash clan technique (see G1). (overview L20 to L28)
3. **States a tier from 1 to 7.** Not 8 (magic ceiling). Tier 7 "most Physical Arts practitioners never get here" (overview L13).
4. **Is consistent with the weapon.** "Consistent with what that weapon category can actually do" (overview L32): an axe move swings an axe, a sabre move cuts with sabres, no free-form powers.
5. **Has an SP cost and a cooldown** (hp-sp-mp L9; ch5 L27 to L29, L49 to L51) unless it is a passive.
6. **Does not duplicate or replace an existing named move.** Reuse Way names where they exist (Split Strike, Momentum Chain, Flowing Edge) before inventing new ones, unless the ability is a martial-master custom technique (overview L32), which is the licence for new names.
7. **Respects CC and resistance rules.** Stun, immobilise, root are Physical CC, partly resisted by Power and Courage; the level gap can bypass resistance (debuffs-and-resistances L21, L29). Silence locks Physical Arts for anyone without a melee weapon drawn (L19). Poison stacks cap at 4x (L18).
8. **Passive rules** (2.4): no activation cost, a trigger or condition, an in-built limiter, amplify or react only.
9. **Stays inside the stat model.** Scales off Power, Speed (Physical AP, Ranged AP), Fortune for crits, Courage and Power for CC resist. No new stat (tatsuya-trap-bomber-brigand-archetype.md L66; secondary-combat-stats.md).
10. **Is level-appropriate and fixed.** Sevish L80 and Wyx L25 do not level (companion-troop L41). Ability tier must match the level they are held at and must not imply growth.
11. **Respects the "rarely shows" framing.** Their advanced arts and clan techniques are "rarely used" (sevish-thrash L27; wyx-thrash L27). The ability appears at a high-stakes moment, not as an opening move.
12. **Does not trivialise the plot.** The siblings are walls, not solvers: Tatsuya needs the kills, and a level 80 would scare the raiders away (ledger L1034, L1052, L1053).
13. **Fits the page format.** Bold bracketed skill line, skill name shown on activation (ledger L298), cost and cooldown on the description panel (chapter-05 L23 to L29), rarity only when it applies (deck-building L33), NPC panels short text without numbers (thrash-siblings L24) unless the author overrides.
14. **Fits the people.** Sevish: berserker, takes pain as proof, honour code (no killing the helpless, fair one-on-one) (sevish-thrash L19). Wyx: dignified, warm, "not ladylike" aversions, brains, protects her people (wyx-thrash L15 to L29). Abilities that need cruelty to the helpless or low-class behaviour contradict them.
15. **Is gold-tag consistent.** A gold-tag NPC is boss-tier or quest-critical; they do not flip hostile except under real provocation (npc-tag L10); an ability needs to read as "boss tier but fair".

### 6.2 Gaps (PROPOSAL territory; the designer must decide, and flag to the author)

All items below are PROPOSALS, not canon.

- **G1. Thrash clan techniques.** No named technique, no definition. Proposal: treat them as Physical Arts that need no Way (or a "Thrash" tag on a Tier 4 to 6 move), built on clan themes: holding a line, shield-wall, bait and counter, rally. Keep them few (one each) and ritual ("rarely used").
- **G2. Level to tier map.** None. Proposal: Wyx (L25) top tier 5 with one Tier 5 at most, rest Tier 1 to 4. Sevish (L80) top tier 6 for signatures, at most one Tier 7 held back as the "never shown" reveal. Rationale: Tier 6 is "recognised on sight" (overview L12), Tier 7 is rare. Page precedent: a level 8 reached Tier 5, so Wyx at Tier 5 is not extreme.
- **G3. SP cost by tier.** Only Tier 1 style numbers exist (10 SP, 5 SP of 25). Proposal as fractions of pool: Tier 1 about 10 to 20 percent, Tier 2 to 3 about 20 to 35, Tier 4 to 5 about 40 to 80 (ABF is 78 percent), Tier 6 to 7 about 80 to 100 percent or a charge or cost in HP. Pools proposal: use 50 + 3 per level HP (125 and 290) for the siblings unless the author says otherwise, and say pools are not shown on panels.
- **G4. Cooldown by tier.** Only 30 s (Gas, Flare), 6 s (rune), 30 s (Hushveil) and 24 h (Phoenix Elixir) exist. Proposal: Tier 1 to 2 about 10 to 20 s, Tier 3 to 4 about 30 to 60 s, Tier 5 to 6 about 90 to 180 s, Tier 7 once per fight or per day.
- **G5. Damage at level 25 and 80.** Absent. Proposal: do not print numbers (matches thrash-siblings L24). If printed, anchor to level 8 ABF (840 base, a combo burst) as the "spell tier 5 burst", and keep NPC physical hits below that unless it is a signature.
- **G6. Learning and teachers from Sevish or Wyx.** No canon. Proposal: a technique is taught only by a character at Mastery 10 in that Way; learning requires Affiliation Trusted (50+) with the teacher personally, a Wisdom plus Speed check (five-disciplines L7), a use grind (Mastery 1 to 10 at 100 XP per level), and probably a Way match (Tatsuya has no weapon and is hand-to-hand, equipment-and-gear-slots.md L11, so Way of the Fist or a taught Thrash technique). Keep it future (Act Three expedition). Do not make it a chapter reward now.
- **G7. What makes an ability Rare.** Not defined. Proposal (above, 2.5): Rare equals a signature, Tier 5 or above, or a unique mechanic; limit the count; label only on the panel where the rarity matters.
- **G8. Unique vs Legendary vs World ordering.** Not defined. Do not use Unique or Legendary for an NPC ability unless the author wants to open that question; Rare is safe.
- **G9. Passive scaling and drawbacks.** No NPC passive precedent. Proposal: a Rare passive for Sevish that grows with damage taken must show a clear cap (for example a per-fight stack ceiling) and a downside (guard drops, which the draft already half-did with Bloodlust).
- **G10. Howl numbers.** Range, cost, cooldown, tier. Proposal: Sevish's Howl a Tier 5 to 6 area Immobilize (a few seconds, shorter on equal levels, long on large level gaps), one use per fight window; Wyx's Howl a Tier 3 to 4 forced-target taunt, 30 to 60 s cooldown, range limited to "earshot" of the wall, no damage. Proposal only.
- **G11. Hobgoblin as a race.** No codex entry. If abilities hang off "Hobgoblin" evolution (Toxic Breath at the rank-up), the designer should say so but not invent more.
- **G12. Rare or Common label on gold NPC panels.** Not set whether NPC panels show rarity at all.
- **G13. Stat lines for the siblings.** None exist. Needed only if a number is shown.
- **G14. Gas plus flare for Hobgoblins.** NPC use is "potentially" copyable (preserved-misc L24); no rules.

---

## 7. Quick verification checklist for the designer

For each proposed ability, answer:

1. Which Way or "Thrash" tag? What weapon does it use?
2. What tier (1 to 7)? Does the tier match the NPC's level (Wyx 25, Sevish 80) and the "rarely shown" rule?
3. What SP cost (fraction of pool) and cooldown?
4. Active or passive? If passive, what trigger and what limiter?
5. Is any CC resisted by Power/Courage, and does the level gap override?
6. Does it clash with or duplicate an existing named move?
7. Rarity (if any) justified?
8. Does it make the siblings solve the fight that Tatsuya is meant to solve?
9. Does it fit the character (Sevish: pain, honour, fair fights; Wyx: poise, intelligence, protective)?
10. What does the panel line look like on the page (name, short effect, optional cost and cooldown)?
