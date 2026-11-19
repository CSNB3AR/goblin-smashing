# Martial Teaching and Mastery Layer (design, Goblin Smashing)

Status: design proposal, codex only, nothing here is on the page. Read-only research against the repo; no repo file was edited.
Convention: **CANON** means a rule I rely on, with its file path. **PROPOSAL** means an invented rule. Every number marked PROPOSAL is a dial the author can turn.

## 0. The one-paragraph version

Rare physical arts are not items and not level grants. They are **transmitted** by someone who has mastered them. A gold-tag master NPC will teach a Rare art only after four things line up: **standing** (affiliation with that individual), a **Proof** (a trust test built from the master's own values), a **floor** (level plus a stat plus a prerequisite art), and a **token** (something that costs the student). Once taught, an art grows by use through the existing 1 to 10 Mastery scale, and rank only buys small, bounded gains (a rider, a cost trim, a side-grade variant, the right to teach). Levels stay the only source of raw power. No cultivation, no breakthroughs, no stat gain from rank.

## 0.1 Canon I am relying on

- CANON, `codex/lore/mastery-system.md`: Mastery runs 1 to 10, 100 XP per rank, 1,000 total; earned by actually using the skill; training with an NPC or player who has mastered it accelerates the climb; a character at master level can teach, "a real, systemic mechanic"; roughly 25 percent Mastery in a book opens about the first half of its tiers and the top tiers stay locked below roughly 75 percent; Mastery is "what you can actually do", Affiliation is "who trusts you", and the two must not be conflated.
- CANON, `codex/combat/physical-arts-overview.md`: Tiers 1 to 7, Tier 7 is the practical ceiling, Tier 1 is three techniques per weapon, Tier 6 is a signature "recognized on sight", Tier 7 is rare. The martial-master rule lets a true master name a custom technique built inside the Way's limits.
- CANON, `codex/lore/affiliation-and-reputation-system.md`: bands Wary-Neutral 0 to 24, Friendly 25 to 49 (minor favors), Trusted 50 to 79 (real requests, some restricted access), Allied 80 to 100. Per faction and per individual. The meter moves because the NPC parses what the player says and does, in a register its world can process. Never a jump straight to Allied.
- CANON, `codex/lore/npc-tag-system.md`: gold tag means quest-critical and essentially never hostile; gold NPCs run the deepest reactive AI with long memory; yellow and below can die permanently; a generic role-title nameplate marks a disposable NPC and a proper name marks someone significant; NPC death is permanent.
- CANON, `codex/lore/leveling-and-progression.md`: 2 stat points per level, cap 75 per stat, specialization forced by scarcity; level-ups occasionally grant a Codex Entry from class and race lists.
- CANON, `codex/crafting/overview.md`, `professions.md`, `crafting-stations-and-process.md`: CP currency, two active professions maximum, Tier 1 to 8 gated by level bands, success roll with "muscle memory" floor, recipes learned by doing or by clan lore, Shamanic Altar unlocked by Thrash standing.
- CANON, `codex/materials/blacksmithing-and-farm-resources-book-one.md`: Hallmarked Steel Bar is bought or earned through dwarven house standing; dwarves cannot cast so a dwarf smith needs an enchanter; a Legendary schematic is a physical, found object whose reading binds the recipe to the reader; the dwarfling smith is a named OPEN.
- CANON, `codex/characters/sevish-thrash.md`, `wyx-thrash.md`, `thrash-siblings-ability-lists.md`: both use "advanced physical arts and Thrash clan techniques he rarely shows". That sentence is the license for a hidden teachable library. Wyx is a dual-sabre Blade Dancer (L25), Sevish an axe Berserker (L80); neither levels until they become Tatsuya's troops.
- CANON, page state in `chapters/in-progress/now/chapter-11-silence-and-fire.md`: Thrash clan 47 to 50 percent, Wyx 52 to 56 percent. Your brief said 47 and 52, which was the Chapter 10 state; I design from 50 and 56 because they are on the page now. Tatsuya (level 8): Courage 4, Power 4, Wisdom 8 (13), Speed 9, Fortune 15 (18).
- CANON, Chapter 10 page: Sevish, "You may call it a bargain, Nykri. I will call it a debt." A debt exists and has not been paid.

## 1. THE TEACHING SYSTEM

### 1.1 The rule (PROPOSAL)

**Every art has a lineage.** An art enters a character's kit by exactly one of five routes:

| Route | What it gives | Limit |
|---|---|---|
| Origin | Race and class kit (Goblin Gas, Gambler's Gambit) | Fixed at creation. CANON. |
| Level grant | Common and Uncommon Codex Entries from class and race lists | CANON, `leveling-and-progression.md`. Stays as written. Never a signature art. |
| Blessing | World Quest or patron grants (Shiv's Flare, Rune Priming, Call of Command) | Unique, bound, one-off. This is why Tatsuya's four are legitimate: they are a Blessing, not a lesson. Shiv had "little time" (CANON, `call-of-the-bones-necklace.md`), so he transmitted by Blessing. It cannot be reused as a shortcut. |
| Instructor | Tier 1 to 3 arts from a white or yellow NPC with a role title | Cheap, no Proof. Raises you to Rank 5 at most. |
| Master's Transmission | Tier 4 and up (Rare and Legendary arts) | The gated path below. |

A **Treatise** (a written or carved source, such as Shiv's notebook) counts as a master's voice in a bottle. It teaches the form only: the art sits at **Rank 3 maximum, tagged Unset**, until a master watches it performed and sets it. This keeps "you cannot learn it from nobody" true, because a Treatise is someone's teaching.

Rarity mapping (PROPOSAL, uses the CANON rarity ladder Common to World): Tier 1 to 2 Common, Tier 3 Uncommon, Tier 4 to 5 Rare, Tier 6 to 7 Legendary. World is reserved for World Quest rewards and is never taught. Existing tags already agree: Dance of Blades and Earthsplitter are marked RARE in `thrash-siblings-ability-lists.md`.

### 1.2 Who teaches what (PROPOSAL)

| Teacher | How you spot them | Teaches | Can raise you to | Cost of failing them |
|---|---|---|---|---|
| Instructor | White or yellow tag, role-title nameplate ("Thrash Clan Enforcer") | Tier 1 to 3 | Rank 5 | None. Mortal, replaceable. |
| Master | Gold tag, proper name | Tier 4 to 5 | Rank 10 | Long memory. A broken trust closes the offer until repaired. |
| Lineage-holder | Gold tag, last known holder of a Tier 6 to 7 art | Tier 6 to 7 | Rank 10 | Same, and the art may die with them. |

A master must be at Mastery 10 in the art (CANON rule: master level unlocks teaching). The panel shows a `MASTER` flag next to the art.

### 1.3 The gates (PROPOSAL, thresholds tied to CANON bands)

A Master's Transmission needs **all six**:

1. **Standing.** Affiliation with the individual at or above that master's personal threshold, which always sits inside Trusted (50 to 79) for Rare arts and inside Allied (80 plus) for Legendary arts. Clan-bound arts (a clan's own technique) also need the **clan meter** above a set line, because the clan must consent. A Friendly meter (25 to 49) only earns an Instructor.
2. **Proof.** A quest the master designs from their own values (Section 4). The master's AI judges it, not a script, which fits the CANON statement that gold NPCs "recognize an unusual player choice for what it is". Proofs are flagged non-lethal: a loss is a yield, no 72-hour death lock.
3. **Floor.** A level floor, one stat floor, and a prerequisite art. Level floor by tier: T1 3, T2 6, T3 10, T4 15, T5 22, T6 35, T7 50. Stat floors use the six Disciplines so build choices cost something (a Power art is closed to a Power 4 goblin, which is the point). Prerequisite: a lower art at Rank 5 plus Way Mastery at the right percent (Section 2.3).
4. **Token.** Something that costs. For an Instructor, shillings. For a Master, shillings are an insult; the token is an object, a made thing, or a service that means something to that master. Crafting tokens use CP and materials, tying the system to the economy.
5. **Time.** A lesson takes real play time, about one session-hour per tier of the art, splittable. Tatsuya's play hours are limited by the arcade (CANON, ledger), so a lesson is a real choice about where his hours go.
6. **A seat.** Each master holds a small number of seats per art (PROPOSAL: 3). When a master dies with no student, the art is gone from the world (CANON: NPC death is permanent). Codex only; the page never states it.

**The Debt shortcut (PROPOSAL, uses a CANON hook).** An owed debt, such as Sevish's, can buy an Audience (the master sees you) or waive the **token**. It never waives standing, Proof or floor. A debt opens the door; it does not hand over the key.

### 1.4 Why a gold-tag NPC can teach but cannot just hand it over (PROPOSAL)

- **The gold tag is the judge, not a vending machine.** CANON says gold tags run the most sophisticated reactive AI. Affiliation is the shadow of their judgment, not a lever on it. The number is necessary and never sufficient.
- **Arts are not items.** A learned art is bound to the learner; it cannot be dropped, traded, auctioned or looted (the same exemption the CANON necklace and earring have). So there is nothing to "give"; the master can only make the student able.
- **Teaching spends the master.** Seats are finite and a name rides on each pupil. Wyx has "massive pride in her name and abilities" and Sevish keeps "a strict personal honor system" (CANON). Handing a Rare art to someone untested stains the name. They would refuse in character.
- **Technique is a body, not a file.** The master demonstrates and corrects; the art "sets" only after the student performs it under their eye. That is why a Treatise is capped at Unset.
- **Gift-farming is closed.** Repeating the same kind of act earns diminishing ticks because a gold NPC remembers. Gifts alone cannot carry a meter past Friendly. Shared risk and shared cost carry it to Trusted.

### 1.5 What it looks like in the UI (PROPOSAL, two lines)

Inspect panel, after the master has offered it (before then the row shows question marks, as the Chapter 6 panels did, CANON):
`[WYX THRASH | MASTER OF THE BLADE]  Teaches: [DANCE OF BLADES, RARE]  Status: NOT YET TAUGHT`

On success:
`[LESSON COMPLETE: WINDING STEP | TAUGHT BY WYX THRASH | MASTERY 1]`

Thresholds, floors and seats are never shown. The student learns them as spoken conditions and refusals. Affiliation ticks stay in the CANON format, `[AFFILIATION: WYX THRASH - 56% → 60%]`.

## 2. THE MASTERY LAYER (extends `mastery-system.md`, does not replace it)

### 2.1 Division of labor (PROPOSAL)

- **Levels and stat points** are raw power: HP, SP, MP, damage scaling, who can be immobilised.
- **Mastery** is fluency: how reliably, cheaply and variedly you perform what you already have.
- A rank never adds a Discipline point, never adds a level, and never raises the damage multiplier of an art.

### 2.2 Two numbers, reconciled (PROPOSAL)

CANON uses both a 1 to 10 rank and a "percent of a book". I read them as two views of one thing:
- **Art Rank, 1 to 10.** Per art. 100 XP per rank (CANON).
- **Way Mastery percent.** Per Way (Blade, Axe, Fist, Spear, Bow), equal to the average rank of your three best arts in that Way times 10. Three arts at Rank 10 is 100 percent. A Way is to Physical Arts what a Book is to magic.

Tier access (extending CANON's 25 and 75 anchors): 25 percent opens Tiers 1 to 3, **50 percent opens Tiers 4 to 5** (my interpolation), 75 percent opens Tiers 6 and 7. Level floors and stat floors apply on top; mastery alone never opens a tier.

### 2.3 How it is earned (PROPOSAL numbers)

- **By use.** CANON. 1 XP per meaningful use, meaning against a target that can actually threaten you (within about five levels). Training dummies and trivial mobs count only up to Rank 3. Daily cap about 25 XP per art.
- **By drill with a master.** CANON says training with a master accelerates the climb. PROPOSAL: a Drill session adds up to 25 more XP per art that day, once per day, and the master sees your form, so Unset arts can be set.
- **By teaching.** When a student you taught reaches Rank 5 in the art, you gain a one-time 50 XP, for at most three students per art. Teaching cannot be farmed. Its main reward is social: the student carries your **Lineage tag**, and NPCs of your school read you as kin (a small, capped affiliation bump with that school).
- **Crafting.** The same ranks apply to recipes. A recipe's Rank is the CANON "muscle memory" success floor, made visible.

### 2.4 What a rank changes (PROPOSAL, deliberately small)

| Rank | Effect | Notes |
|---|---|---|
| 1 | Base art. | |
| 2 | One more line of description reveals an unlisted use. | CANON: descriptions undersell; the player works out what it can do. No numbers change. |
| 3 | **Rider.** One minor extra effect. | Works in any Way. |
| 5 | **Efficiency.** Cooldown down up to 10 percent, or one step less SP. | Focus Ways only (see 2.5). |
| 7 | **Variant.** Choose one of two side-grades, swappable out of combat. | Focus Ways only. A side-grade changes shape, not size. |
| 10 | **Master.** May teach. Lineage line on the art. Eligible for the martial-master naming rule. | No extra power over Rank 7. |

Illustrative only, not canon: Goblin Gas (30 second cooldown, CANON) at Rank 3 lingers one extra tick on targets who leave the cloud; Rank 5 trims the cooldown to about 27 seconds; Rank 7 offers Dense Gas (fewer, harder stacks) or Wide Gas (bigger, softer). Winding Step at Rank 3 leaves a one-second faint afterimage that draws a swing; Rank 7 offers a longer step or a step that ends in a free parry.

Martial-master naming rule (CANON, extended): naming a custom technique needs Way Mastery 75 percent and Rank 10 in three arts of Tier 3 or higher. That makes it truly rare and keeps the CANON "not a free-form ability" wording.

### 2.5 Keeping it from becoming a second treadmill (PROPOSAL)

1. **Hard ceiling.** One rider, one trim of at most 10 percent, one variant, one teaching right. No rank multiplies damage. Rank 10 adds no power over Rank 7.
2. **Sideways, not upward.** Variants trade, they do not stack.
3. **Two Ways in Focus.** Rank 5 and Rank 7 effects work only in your **Primary Way** and one **Secondary Way**. Other Ways keep Rank 3 riders only. This echoes the CANON scarcity rule that "nobody reaches a fully maxed tree".
4. **Use quality and daily caps.** No dummy grinding past Rank 3, no spamming for XP.
5. **Levels still gate.** A Rank 10 art is not a license to fight above your level; levels set raw output and who a Howl can stop.
6. **No stat from mastery, no mastery from points.** CANON already says Mastery is not Discipline Points under another name. I keep it.
7. **Quiet display.** Rank-up notices appear only at Rank 3, 5, 7 and 10, and only as one line.

## 3. CRAFT MASTERS (same pattern, short)

**Rule (PROPOSAL):** a found schematic gives the **pattern**; a master gives the **hand**. This keeps the CANON found-schematic rule (a physical object, reading binds it, `blacksmithing-and-farm-resources-book-one.md`) intact and adds a reason to seek masters.

- A **found** Rare or Legendary schematic works as written, at its base success floor, with no variant.
- A **taught** one carries the master's **Hallmark** in its lineage, raises the success floor, and reveals one variant. A master can also open a Rare technique that exists in no schematic.
- All crafting teaching still spends **CP** and respects the **two active professions** cap and the level-band tier gate (CANON). A master cannot give a third profession.

| Master | Teaches | Standing gate | Proof | Token |
|---|---|---|---|---|
| **Dwarven house smith** (the Zone E contact, the "dwarfling" OPEN) | Hallmarked refining, augment-holding hafts, Rare blade and armor work | House standing, the same one that sells Hallmarked Steel Bars (CANON) | A piece to the house's standard; poor work wastes good stock (CANON: crafter tier and batch grade decide quality) | Mountain Coal, Greywall Iron, a finished piece with the house's mark |
| **Clan forge-keeper** (unnamed, Bloodhurst Clan Workbench, CANON station) | Bonecrafting and light-armor lines, Thornhide work | Thrash clan meter at Trusted | A kit made from camp salvage | Hides, bone, a day at the forge |
| **Schematic keeper** (an archivist or an enclave elder) | Legendary patterns, such as the Hollow Heart Foci given "for a favor, not a drop" (CANON) | Favor quests, not shillings | A favor that costs the student | A rare reagent or a surrendered pattern |

Two craft-specific hooks:
- **Dwarves cannot cast** (CANON), so the dwarf smith needs Tatsuya's Rune Priming to seat anything. That makes it a **trade of teaching**: he teaches the forge, Tatsuya brings the page in Daichi's manual only a goblin enchanter could use. Mutual need beats a one-way gift.
- **Maker's mark and lineage.** When Tatsuya masters a pattern he can teach it; his own line (CANON blank manual pages) becomes his school. This is the craft-side payoff of the CANON statement that Tatsuya will eventually teach.

## 4. KINGMAKER-STYLE TRUST

### 4.1 How approval is built (PROPOSAL)

Each gold-tag master has a hidden **Values sheet**: three Values, a list of likes and dislikes, and one **Line** they will not forgive crossing. Every choice is parsed (CANON: in-world register or it does not register) and tagged against the sheet.

- **Ticks.** On-page ticks so far are 2 to 4 points (CANON: 45 to 47, 47 to 50, 45 to 48, 48 to 52, 52 to 56). So: Small 1 to 2, Notable 3 to 4, Landmark 5 to 8, kept for Proofs and costly choices.
- **Memory and diminishing returns.** Repeating the same kind of act earns less. Gold NPCs remember.
- **Betrayal costs double.** Crossing the Line subtracts roughly twice what a Landmark adds, and closes the teaching offer until repaired.
- **Multi-faction weights.** Sevish weighs Wyx's read heavily (CANON: "trusts her line of reason"). A Wyx meter above 60 adds a small multiplier to Sevish's ticks. She is the lever, not the key.
- **Voice, not a pop-up.** Kingmaker flags approval with an icon. HGO uses the NPC's own reaction line (a laugh, a pause, a raised eyebrow) and, only sometimes, the tick.
- **No romance mechanic.** Wyx's interest stays narrative texture and the relationship shape is a CANON OPEN. Her ticks come from respect.

### 4.2 Wyx Thrash (L25 Blade Dancer, now 56 percent)

**What she wants, from her codex file:**
- People who are treated as family. She "treats the people under her like family" and "despises cruelty".
- **Character and effort over status and species.** She "judges people by character and effort", so she dislikes him leaning on the unearned "elder" title.
- **A worthy rival.** Massive pride, highly competitive, unwilling to back down. She likes being challenged and likes dry wit answered with dry wit.
- **Reasoned plans.** She is "the brains". She respects a well-argued plan more than bravado.
- A firm believer in Shiv's cause she will not go against.

**Likes (ticks):** carrying the names of the dead; refusing to spend goblins as fodder; sticking to a rule in a spar and winning anyway; making something with his own hands; asking her opinion before a gamble; honest talk about his mother's surgery clock (Chapter 11 already lands this tone).
**Dislikes:** boasting; gamer slang; lording the elder title; mocking her squeamishness about gas ("not ladylike", CANON); gambling with her people's lives (Gambler's Gambit and his Fortune build make this a real temptation).
**The Line:** cruelty to the helpless, or using the clan's dead as a bargaining chip.

**Teachable signature arts (PROPOSAL):**

| Art | Tier / rarity | Why it fits Tatsuya | Floors | Token | Proof |
|---|---|---|---|---|---|
| **Winding Step** (CANON, her list: a sidestep that slips out of melee) | T3 Uncommon, Way of the Blade | Hit-and-run, Speed 9, low Power | Level 10, Speed 10, trust at least 60 | A matched pair of blades **he makes himself** (Bonecrafting or Smithing, Rank-1 quality is enough) | **The Edge Test.** She spars him under a rule: no gas, no flare. Best outcome, win by wit inside her rule (Landmark). Next, lose with grit and take the lesson (Notable). Worst, cheat with gas (a tick loss). |
| **Dance of Blades** (CANON, her RARE chain) | T5 Rare, Way of the Blade | Conjured arcane daggers and the belt sword make a pair; chain quickens per hit | Level 22, Speed 14, Winding Step at Rank 5, Blade Way 50 percent, trust at least 70 | The same pair, now inscribed with his own Rune Priming (a made thing plus craft) | **Hold the Hill.** A defensive trial where he protects goblins under her eye without sacrificing any of them for the win. |

**Milestone bands:**
- Winding Step: **Chapters 13 to 16**, the aftermath of the Hill and before the clan leaves. At 56 percent she needs about 4 more points from notable choices (the funeral names, the spar). If he is not Level 10 yet, she teaches the stance but the art "will not set" until he is.
- Dance of Blades: **Book Two, Act Three (Myrrhwood)**, after the rally succeeds. In Book One, plant it as the closing hook (Chapter 38 to 41 farewell at the dock): she sets the Proof and says what to bring.
- Option for Shiv's notebook: CANON says she hands it over "only when Tatsuya becomes a Shiv Goblin" and I found no handover on the page after Chapter 9. Recommend placing it **in the Winding Step scene** as her trust gift, with her teaching him how to read the Thrash notes (a Treatise route for a hidden Thrash technique).

### 4.3 Sevish Thrash (L80 Berserker, clan 50 percent)

**What he wants, from his codex file:**
- **Frankness.** He laughs and respects people who say it to his face (CANON on the page: "Hah. He says it to my face."). Zero interest in titles, rules, bureaucracy.
- **A fair fight.** Demands fair one-on-one, will not kill the helpless, respects anyone strong enough to challenge him.
- **Care for his own dead.** NPCs do not respawn, so he takes every death seriously and told Tatsuya "when a goblin of mine falls out there, he does not get up".
- **Faith in Shiv and Myrrhwood reunified.** The real driver.
- Wyx's approval (his sister's reasoning weighs on him).

**Likes:** standing his ground when Sevish pushes (CANON on the page); owning mistakes bluntly; fighting beside the clan; honoring Shiv; wounds taken honestly.
**Dislikes:** flattery; hiding behind rules; sneaking a trap into a fair duel; flaunting "elder"; wasting his goblins.
**The Line:** harming the helpless; abandoning the camp; mocking Shiv.

**Teachable signature art (PROPOSAL): the Thrash Howl.** His **Challenging Howl** (CANON, the Chapter 5 roar that immobilised Tatsuya), taught as a clan technique. Tatsuya learns the **taunt-and-steady** form, not the immobilise. Reason: the immobilise is level-bound, so a Howl from Tatsuya stops only targets far below his level, and it stays within the archetype's CANON no-hard-CC rule. Rank 7 variants (PROPOSAL): **Challenging** (draws foes, shorter leash like Wyx's) or **Rallying** (steadies allies and troops against fear and stun, tied to Call of Command and Whispers of Shiv).

| | |
|---|---|
| Tier / rarity | T4 Rare (the list does not tag it, so rarity is PROPOSAL), clan-bound |
| Floors | Level 15, **Courage 12** (Tatsuya has 4, so eight points: a real, felt build cost), Call of Command used in real fights |
| Standing | Individual at least 65, **and the Thrash clan meter at Allied (80)**, since it is a clan technique |
| Token | A **Bone Tally**: the names of the goblins lost to the raids, carved by his own hand (Bonecrafting). Costs time, not shillings |
| Proof | **The Standing.** A fair one-on-one. He does not have to win (impossible at L80). He must **stand through one Howl** without yielding, and land one honest blow (a palm Shiv-Touched Flare counts), with no allies and no traps. Sevish permits his own Rune Priming (preparing is not a trick). |

**Milestone band:** **Book Two, Act Three, after the rally succeeds and the clan crosses into Allied** (CANON, `outline/act-three-myrrhwood-expedition.md`, the "earned elder" payoff). This makes the teaching the on-page proof that "elder" is now earned. In Book One, plant it only: around Chapters 13 to 16 Sevish says "Ask me again when you have stood a Howl". Seed, not a lesson. His debt can buy the Standing an audience, not a pass.

## 5. WHAT GOES ON THE PAGE vs WHAT STAYS IN THE CODEX

**Rule of thumb: the page carries one cost, one reaction, one line of lore. The codex carries the table.**

On the page:
1. **One line of master lore per scene.** A lineage clause in dialogue ("She learned that step from the ones who held the Hill before her") or a panel tag. Names only on panels.
2. **One condition per master, in their own words.** "Bring me two blades you made." The gate becomes a goal, not a rule.
3. **Show the refusal, not the threshold.** "Not yet. You would only hurt yourself." The level floor and stat floor are felt, never printed.
4. **The Proof is the scene.** It must pay off something already on the page (the dead, the Hill, the debt, the gas ban), so a lesson is cause and effect, never a tutorial.
5. **Two UI lines at most.** The inspect row and the lesson-complete notice. Affiliation ticks stay in the canon format.
6. **Mastery shows by doing.** Tatsuya notices the afterimage on Rank 3; the page never says "rider".
7. **No gold-tag talk in narration.** The ledger told us to show their intelligence through behavior; Chapter 11 lets Tatsuya say "gold tags" once in speech, so keep it as a gamer's word at most.
8. **NPC register stays in-world.** They say "your hands have it" or "it has set", never "rank". No gamer slang in an NPC mouth.
9. **Lineage tells.** A stance or a stitch pattern shows who taught whom. It is the cheapest way to make the world feel detailed.

Codex only: seats, the lineage registry, XP caps, Way percents, token and floor tables, craft master tables, thresholds.

## 6. OPEN QUESTIONS (ranked, with recommended answers)

1. **Do Wyx and Sevish stay near Bloodhurst long enough for a lesson in Chapters 13 to 16?** Outlines disagree: `arc-one-open-beta-to-crownfall.md` says the group splits right after Thrash Hill and the clan heads for the boat, while the same file and the Act Three outline say they sail around the start of Season One. Recommend: they stay through Crownfall, so lessons start in 13 to 16, with the farewell at the dock near Book One's close.
2. **May Tatsuya learn martial arts at all, given Arcane Bomber and Power 4?** Recommend: yes, but only arts that fit his stats (Speed or Courage arts), never Power arts. That keeps the build fresh and uses real stat cost.
3. **Confirm Wyx's weapon.** `way-of-the-bow.md` calls her a bow user, `call-of-the-bones-necklace.md` says dual daggers; the latest ledger and ability list say dual sabres. Recommend: dual sabres, and fix the other two files.
4. **Hide thresholds on the page?** Recommend: yes, ticks only.
5. **Is the Thrash Howl the right Sevish art?** Recommend: yes. It fits Courage, Call of Command, and the earned-elder payoff, and avoids a Power art Tatsuya cannot use.
6. **Shiv's notebook handover: when?** Recommend: Wyx's Winding Step scene, as her trust gift.
7. **Master death and lost lineages.** Recommend: yes, codex-only, a quiet consequence of permadeath.
8. **Dwarfling smith:** troop, player or master? A troop cannot also be a gold master. Recommend: a named NPC master first, and he can become a retainer later.
9. **Can players teach?** Recommend: yes at Rank 10, which matches the CANON plan for Tatsuya's Shaman's Veil disciples.
