# Alignment Framework for Eryndal (the Road, the Hand and the Tree)

**Status:** design proposal, codex only. Nothing here is on the page. It is written to sit on top of the locked Karma, Affiliation, NPC-tag and patron rules without changing any of them. Companion files: `codex/characters/alignment-and-character-trees.md` (who sits where, with a personality block for each), `codex/characters/npc-personality-template.md` (the reusable card), `codex/lore/goblin-code-and-clan-alignments.md` (goblins in depth).

## 0. Conventions

- **[CANON path]** a fact or rule already in the repo, with its file. Where the ledger overrides an older file I follow the ledger (`outline/canon-ledger.md`, later entries win).
- **[PAGE chN]** what the drafted chapters show, using the numbering of the files in `chapters/` (Chapter Four "The Runt's Bowl" is `chapter-04.md`; Chapters Nine to Eleven are the "now" drafts in `chapters/in-progress/now/`, still unreviewed).
- **[SRC Sn]** a paraphrase of an outside source. The key, with URLs and a note on whether I fetched the page or only saw a search summary, is in section 14. Nothing outside is quoted at length.
- **[PROPOSAL]** my invention. Every number is a dial the author can turn.
- The borrowing rule in `style-guide/inspirations-and-borrowing.md` applies throughout: same idea, our names, our numbers, our scene.
- **Terminology trap.** In canon, "Karma/Alignment" is the name of the single global punitive meter (`codex/lore/preserved-misc-mechanics.md`). In this file **Karma** always means that meter, unchanged. The nine-cell frame is called **the Tree**, and "alignment" in lowercase means a reading of conduct that has no meter of its own.

## 1. The one-paragraph version

D&D asks two questions of every character: how do they go after what they want, and what do they want for other people [SRC S3]. Eryndal keeps both questions and gives them in-world names: the **Road** (Straight, Wandering, Wild) and the **Hand** (Open, Level, Cold). Nine combinations make **the Tree**, the same "alignment tree" canon already uses to decide which patron notices a player [CANON codex/lore/patrons-and-world-weapons.md]. The Tree is a way of reading people, not a stat. NPCs carry a hidden Compass Card. Players carry nothing: the world reads them through the meters that already exist (Karma for punishable harm, Affiliation for what each faction values, Fame for reach) plus the attention of the five gods. Alignment shows through behavior and is never printed, and it moves only through witnessed, costly, repeated deeds.

## 2. What canon already fixes

Read this before changing anything. Every row below is locked; the framework works inside it.

| Topic | Locked rule | Where |
|---|---|---|
| Karma | One global meter, purely punitive, never rises on its own. Goblins default about -5 (disliked but tolerated). At about -15 to -20 guards attack or arrest on sight and the nameplate flips white to red, "Blood Tinted". Killing players outside sanctioned PvP, and mistreating NPCs or a region's people, push it down. | `preserved-misc-mechanics.md`, `player-owned-economy-and-living-world-npcs.md` |
| Zones | Red: open PvP, full loot, no Karma penalty. Yellow: PvP possible but costs Karma, guards pursue the negative. Green: safe haven. | `preserved-misc-mechanics.md` |
| Affiliation | Per faction and per individual, 0 to 100. Bands: Hostile below 0, Wary-Neutral 0 to 24, Friendly 25 to 49, Trusted 50 to 79, Allied 80 to 100. Nobody starts below about 20. Goblins start 40 to 50 percent with goblin NPCs and about 20 with humans. It moves because the NPC parses what the player says and does, in a register its world can process. Never a jump straight to Allied. | `affiliation-and-reputation-system.md`, ledger |
| Fame | A third public meter: how widely a player is known. Goblins start infamous. Carries into Node Wars and seasonal standing. | `affiliation-and-reputation-system.md` |
| Tags | White friendly, yellow conditional, red enemy, gold quest-critical (essentially never hostile; if one flips, the whole faction behind it flips), blue always a player. Yellow and below can die permanently, and NPC death is permanent. A role-title nameplate marks a disposable NPC, a proper name marks someone significant. | `npc-tag-system.md` |
| NPC AI | Every NPC reacts individually to what the player does. Gold tags run long memory and real strategic judgment. Metagame slang does not register as input. | `npc-tag-system.md`, `style-guide/race-dialect-and-voice.md` |
| Patrons | Five gods, each with its own personality and beliefs. Gods go by character trait, not good versus evil. No one starts with a blessing: a god grants it for how a player acts and lives, "along an alignment tree" (lawful good, good, chaotic good, down through neutral to the wicked). The race's god notices faster; nothing is locked to race. A PKing player can earn the wicked patron's blessing. Two offers are possible, one accepted. Changing needs a respec (500,000 yen, once). Some patrons are rare with hidden unlocks, and none may feel gatekept. | `patrons-and-world-weapons.md`, ledger "Patrons are earned" |
| Race standing | In Lunarest elves get special treatment under an elven law; Beastfolk, goblins and dwarves carry bad infamy. Orcs and Drakekin carry a wicked-by-reputation label, but individuals can be neutral or shaded. NPCs never show naive surprise about their own race's standing. | `lunarest-royal-court.md`, `races/orc.md`, `style-guide/craft-rules.md` |
| Compass | Tatsuya's morals and moral compass stay; his real-life money worries live in the real-world scenes. | ledger |
| Authors' reads already stated | Tatsuya's voice is "chaotic good". Wyx: the author is unsure of the exact alignment and reads her as chaotic good. Sevish is modeled on a battle-hungry fighter with a strange personal honor; no alignment is stated. | `tatsuya-kazehaya.md`, `wyx-thrash.md`, `sevish-thrash.md` |

## 3. What D&D does, and what we keep

### 3.1 The two-question design

- Mike Mearls describes law and chaos as the *method* of acting and good and evil as the *goals*, and calls alignment a roleplaying shorthand with no mechanical force in 5e [SRC S3].
- The D&D Beyond explainer defines the moral axis as how a character treats others and whether they put others' needs ahead of their own, and the order axis as how they relate to rules, laws, traditions and structure [SRC S2].
- The 2024 free rules say alignment "broadly describes" ethical attitudes, that each summary describes typical behavior and individuals differ, and that evil is assumed to be unusual for player characters and cleared with the DM first [SRC S1].

### 3.2 The nine, in plain words (my paraphrase of S1 and S2)

| D&D label | One-line reading |
|---|---|
| Lawful Good | Does what a community expects as right, often by oath or code, and shields the innocent. |
| Neutral Good | Helps people according to their need; works inside rules without feeling bound by them. |
| Chaotic Good | Conscience before convention; will break a rule to protect someone. |
| Lawful Neutral | Law, tradition or a personal code comes first, even over pleas and temptations. |
| Neutral | Takes no side in moral arguments and does what seems sensible; can be a balancer or just pragmatic. |
| Chaotic Neutral | Freedom first and whims second; not especially kind or cruel. |
| Lawful Evil | Takes what it wants methodically, through order, contract and hierarchy. |
| Neutral Evil | Pursues its wants and is unbothered by the harm. |
| Chaotic Evil | Violence out of hatred, spite or bloodlust. |

### 3.3 What DMs are warned about

- **Alignment describes, it does not forbid.** No 5e rule mandates an alignment or restricts a class by it; it describes inclinations, like flaws and bonds [SRC S5]. Actions should inform alignment, not the reverse [SRC S24, quoting Matt Mercer].
- **It is not fixed.** Characters drift and can act against type [SRC S2]. NPC alignments can be changed by what the players do [SRC S2].
- **Evil can cooperate with good, and evil is not cartoonish.** Evil NPCs can be charming and complex [SRC S2]. Mearls adds: do not write evil factions as simply insane; give them coherent motives and social structures [SRC S3].
- **Neutral is not apathy.** A neutral character can be focused and purposeful [SRC S2]. A chaotic neutral person is a self-focused free spirit, not someone seeking harm [SRC S3].
- **Lawful is not "follows any rule".** The "lawful stupid" failure is rigid rule-following with no concern for the rule's purpose [SRC S22].
- **Labels turn vague or become an excuse.** Critics say the definitions blur and the terms get relativized until they tell nobody anything [SRC S23]. Players pick Chaotic to excuse careless behavior and avoid Evil, leaving DMs nothing to build drama on [SRC S24]. The fix on offer: present alignment as beliefs a character holds, and define it by acts.
- **Evil at the table needs boundaries.** Set limits before play, and treat alignment as a story tool, for example a cleric who strays and must atone [SRC S25].

### 3.4 Monsters, groups, personality tools, renown

- **Monsters.** A stat-block alignment is a default the DM may change; some creatures are "any alignment"; low-intelligence creatures that act on instinct are unaligned [SRC S4]. Crawford called the default a suggestion and said benevolent dragons and gentle werewolves are fair game [SRC S5]. The 3.5 books tagged monsters "Always", "Usually" or "Often" with an alignment, and fans read "Always" as "almost never an exception" [SRC S21]. Monsters of the Multiverse reportedly dropped predetermined alignments for most monsters [SRC S20, search summary only], and a Volo's errata removed the Alignment trait from the goblin, bugbear and hobgoblin racial entries [SRC S19].
- **Organizations.** An organization's ethos can be given an alignment, but it does not set the alignment of members or even leaders, and a gap between ethos and leadership is good adventure material [SRC S6, search summary only]. Lawful groups lean on written procedure, chaotic groups treat tradition as disposable, neutral groups deliberate and compromise; evil groups expect cruelty and loyalty with strings, good groups expect selflessness and allow redemption; inverting one trait is a quick way to find a weakness [SRC S7].
- **Personality tools.** The SRD gives each character two traits, one ideal (five of the six ideals follow alignment themes: order, freedom, benevolence, malice, balance), one bond and one flaw, with inspiration as the reward for playing to them [SRC S8]. The 2024 free rules pair each alignment component with suggested traits: chaotic is boastful, impulsive, rebellious or self-absorbed; good is compassionate, helpful, honest or kind; evil is dishonest, vengeful, cruel or greedy; lawful is cooperative, loyal, judgmental or methodical; neutral is selfish, disinterested, laconic or pragmatic [SRC S1]. A critic notes the entries are often vague, bonds name a motive without saying what it means in practice, flaws are too mild to bite, and players ignore them; his fix is a short note on how the NPC will treat the party now [SRC S9]. The Two-Note NPC method needs only a game purpose and one humanizing trait, adding more as the NPC earns screen time [SRC S10].
- **Renown.** The DMG's optional rule tracks standing per faction, earned by advancing the faction's goals, with ranks and benefits [SRC S11, S14]. Tables adapt it with negative renown, hidden numbers described only as liked, trusted or hated, recognition checks for fame, or a plain record of conduct such as bold or cowardly, honorable or treacherous [SRC S13]. Ranks feel empty unless each one grants something concrete [SRC S11].

### 3.5 Supporting references from other games

- **Baldur's Gate 3 approval.** Each companion holds a separate value for the player, from the point where they leave (about -50) up to 100. Typical events move it by 1, 5 or 10. The companion must be present when it happens. Bands shape dialogue tone, persuasion difficulty, romance and personal quests, and the number is shown to the player [SRC S26].
- **Fallout: New Vegas.** Faction reputation is separate from Karma. Each faction tracks fame and infamy as two hidden values that only rise, so standing can be mixed. Infamy comes from being seen attacking or stealing, and killing discreetly avoids it [SRC S27].
- **Pillars of Eternity II.** Dispositions describe how the world sees you (ten labels such as Cruel, Honest, Rational, none called good or bad), and faction reputations notify on every change [SRC S28].
- **Pathfinder: Kingmaker.** Nine alignments on two axes [SRC S29]. Tagged dialogue choices shift alignment slowly over many decisions, and a few options are locked behind alignment [SRC S29, forum summary]. The designers argue companions need personal ties that explain why they stay, and that a mixed-alignment party needs a reason to stay together [SRC S29, GameBanshee].
- **Blades in the Dark.** Faction status runs from -3 to +3 with war at the bottom, and an operation can hurt some factions while helping others [SRC S16, search summary only].
- **Albion Online.** Zones run blue, yellow, red and black; attacking in red zones costs reputation and black zones carry none [SRC S30].
- **Ultima IV.** Eight virtues rest on three principles; what you do in the world shapes them and NPCs treat you accordingly [SRC S31, search summary only].

### 3.6 Borrow table: what we take and how we reword it

| Source idea | HGO version (reworded) | Fit with canon |
|---|---|---|
| Two axes, method and goal [S3] | The Road and the Hand | Works with the existing "alignment tree" wording |
| NPC alignment as starting attitude [S2] | First test and first assumption (section 8) | Fits the reactive-AI rule |
| Alignment from actions [S24] | The Conduct Ledger, deeds not declarations | Fits "register matters" and gold-tag memory |
| Ethos is not membership [S6, S7] | Ethos Card with a Practice and a Gap | Fits the Thrash camp, where the creed and the camp differ |
| Unaligned instinct creatures [S4] | Temperament, no cell | Fits creature classes I to IV |
| "Always/Usually/Often" [S21] | Bound, Inclined, Common, for Persons only | Gives the wicked patron real servants without an evil race |
| Ideals tied to alignment themes [S8] | Six Creeds: Order, Freedom, Mercy, Hunger, Balance, Calling | New names, same job |
| Vague bonds and flaws [S9] | Every card needs a Line and a Trust Key that say what happens on the page | Builds on the martial proposal's Values sheet |
| Renown ranks [S11, S13] | Bands stay as they are; titles only at Allied; tracked per faction | Fits the locked bands |
| Approval ticks of 1, 5, 10 [S26] | Small 1 to 2, Notable 3 to 4, Landmark 5 to 8 | Already used in the martial proposal and the page ticks |
| Fame and infamy as separate values [S27, S28] | Optional split of Fame into reach and flavor (section 7.4) | Marked OPEN, canon has one Fame meter |
| Presence rule [S26, S27] | Witness rule | Fits NPCs reacting to what is in front of them |

## 4. The Road, the Hand and the Tree (the nine, in HGO terms)

### 4.1 Two questions [PROPOSAL, built on S3]

- **The Road:** how does this person go after what they want? (D&D's law axis, the method.)
- **The Hand:** what do they want for other people? (D&D's good axis, the goal.)

Six quick tests that place anyone in a minute [PROPOSAL]:

1. An order is wrong and the one giving it can punish you. Obey, bend it, or refuse? (Road)
2. A stranger is helpless and helping would cost you. (Hand)
3. A promise has turned expensive. (Road)
4. Nobody will ever know. (Hand; and Road, if they keep the code anyway)
5. Their own people are hurt. What do they do to whoever did it? (Hand)
6. Someone offers a shortcut that skips the proper door. (Road)

### 4.2 The Road [PROPOSAL]

| Road | D&D axis | Lives by | At its best | At its worst | What NPCs say |
|---|---|---|---|---|---|
| **Straight** | Lawful | Oath, law, rank, clan code, contract | Reliable; protects through order; keeps the count | Puts the letter above the person; hides cruelty behind a form (the "lawful stupid" failure [SRC S22]) | "Word-true." "Keeps the count." "Stands on the letter." |
| **Wandering** | Neutral | What the day asks | Fair, practical, adaptable | Drifts; lets harm pass because it is not their business | "Goes where the day goes." "Keeps his own counsel." |
| **Wild** | Chaotic | Conscience, instinct, personal loyalty, freedom | Breaks an unjust rule; loyal to people, not paper | Cannot be relied on; calls recklessness freedom [SRC S24] | "Answers to no banner." "Wild-hearted." "No one's dog." |

**Wild is not feral.** In canon, "feral" is an outsider's word for uncivilized, animalistic behavior, a stigma laid on goblins and demi-humans [CANON `codex/lore/goblin-clan-culture-and-feral-stigma.md`]. A Wild-Road goblin can be gentle, reasoned and free. "Feral" is a judgment on conduct (a clan that has dropped both a code and a table), and it is also a prejudice. It never means a Road. Details in `goblin-code-and-clan-alignments.md`.

### 4.3 The Hand [PROPOSAL]

| Hand | D&D axis | What it does for others | Counts only when | What NPCs say |
|---|---|---|---|---|
| **Open** | Good | Gives, shields, spares | It cost the giver something real: risk, goods, time or standing. Free kindness is polite, not Open. | "Kind-handed." "Keeps a fire for strangers." |
| **Level** | Neutral | Is fair, tends its own, rarely reaches beyond them | It is a choice and not a shrug; neutral is not apathy [SRC S2] | "Even-handed." "Neither flame nor frost." |
| **Cold** | Evil | Takes, uses, or hurts for gain, order or pleasure | The harm was foreseen and the actor was unbothered by it [SRC S1] | "Cold-handed." "Counts you as coin." |

### 4.4 The nine [PROPOSAL]

Bynames are what an NPC might call a person. "Anchor" shows a cast member who sits there; the reasons are in `alignment-and-character-trees.md`.

| D&D label | HGO byname | Road and Hand | What an NPC might say | In play | Anchor |
|---|---|---|---|---|---|
| Lawful Good | **Oathkeeper** | Straight + Open | "Word-true, and he stands between you and the blade." | Keeps promises at personal cost; protects the weak through law and code; fights an unjust order from inside | Shiv, Ru, Prince Dorrin |
| Neutral Good | **Hearthkeeper** | Wandering + Open | "Her door is never barred and she asks no price." | Helps whoever is in front of them; bends rules for kindness without making a creed of it | Leon, Yuna |
| Chaotic Good | **Freeheart** | Wild + Open | "Wild as a gale and warm as a hearth." | Conscience over convention; breaks rules to protect; loyal to people before paper | Tatsuya, Wyx (author's read), Arya |
| Lawful Neutral | **Warden** | Straight + Level | "By the letter, and fair to all alike." | Law, duty or craft first; does not weigh whether the law is kind | Zinka, Kesh, London Spire, Kazuku |
| Neutral | **Wayfarer** | Wandering + Level | "Goes where the day goes." | Pragmatic; keeps out of it; guards their own and their time; may be a balancer | Haruto (for now) |
| Chaotic Neutral | **Unbound** | Wild + Level | "No man's dog, and no one's enemy until crossed." | Freedom first and whim second; kindness and cruelty are both incidental | Sevish (with a good code) |
| Lawful Evil | **Ironhand** | Straight + Cold | "The law is in his fist and the debt is in his ledger." | Takes methodically through order, contract and hierarchy; keeps bargains that bind others | King Aldemar, Corvith, Maldren, Kazuto |
| Neutral Evil | **Taker** | Wandering + Cold | "Smiles while he empties your purse." | Takes what it can get away with; loyal only to its appetite | PK_Wraith, Eren (young, unsettled) |
| Chaotic Evil | **Ravager** | Wild + Cold | "A burning wolf: no bargain, no end." | Violence out of hatred, spite or bloodlust | No named cast member, on purpose |

### 4.5 The Tree

| | Straight Road | Wandering Road | Wild Road |
|---|---|---|---|
| **Bright Limb (Open Hand)** | Oathkeeper | Hearthkeeper | Freeheart |
| **Middle Limb (Level Hand)** | Warden | Wayfarer | Unbound |
| **Wicked Limb (Cold Hand)** | Ironhand | Taker | Ravager |

- The reading order is the canon phrase: lawful good, good, chaotic good, then down through neutral to the wicked [CANON `patrons-and-world-weapons.md`, ledger "Patrons are earned"].
- **It is a tree, not a ladder.** The Bright Limb is not "better" in the world's eyes. Lunarest's law is Straight and rotten; the Church of Seranis is Straight and kind; the same goblin can be thanked in one village and hunted in the next. A limb says what a deed is, not whether a given faction welcomes it.
- **Gods go by trait, not by good versus evil** [CANON]. A god's notice attaches to a pattern of deeds on the Tree, and a god can prize a deed that sits on another limb than its own cell (a stern, lawful craft god can approve a hard punishment). See section 11.
- The Tree is never drawn in the UI. It is an author's map.

### 4.6 The in-world phrasebook [PROPOSAL]

NPCs speak in a medieval-fantasy register with no modern idioms, no real-world similes and no gamer slang [CANON `style-guide/race-dialect-and-voice.md`]. So no NPC ever says "chaotic good". They talk about deeds, roads and hands.

- Do: "He is true to his word." "She has a free hand and a warm one." "That one counts you as coin."
- Do not: "He's chaotic good." "She's lawful neutral." "Alignment check."
- Goblin speech keeps its own clipped pattern; a low-Wisdom goblin refers to himself by name ("Kesh bring news") [CANON race-dialect-and-voice.md].
- "Feral" is an insult about kind and conduct. It is never a synonym for Wild.

## 5. Who carries a cell, and who does not

| Subject | Has a Tree cell? | Where it lives | Seen by the player? |
|---|---|---|---|
| Player characters | No cell is stored. The world reads the Conduct Ledger (6.2). | Karma, Affiliation, Fame, patron notices | Only through those and through what NPCs say |
| Gold-tag NPCs | Yes, a full Compass Card | Codex and NPC AI | Never printed; learned through behavior and inspect-panel lines |
| Named white and yellow NPCs | Yes, a two-line card | Codex | Never printed |
| Mob-tier, role-title NPCs ("Thrash Clan Enforcer") | No individual cell. They inherit the faction's Practice and a Hand set by rank. | Faction Ethos Card | Never printed |
| Beasts and mindless things | No cell. A Temperament (9.1). | Creature entry | Behavior and tag color |
| Persons among the creatures (anything that bargains, swears or spares) | Yes | Creature entry or Compass Card | Behavior |
| Races | Never. A race is a Prior (5.1), not a nature. | Race file | Starting offsets only |
| Clans, guilds, kingdoms | An Ethos Card with a Practice and a Gap | Codex | Rank, banner, reputation |
| Gods | A favored cell plus listed traits | `patrons-and-world-weapons.md` | Through notices and relics |

Rule of thumb: **if it can swear an oath, it has a Road; if it can spare a life, it has a Hand.**

### 5.1 Priors and Conduct

- A **Prior** is what the world assumes before you do anything: race, a mark such as Shiv's necklace, starting Fame. It sets starting Affiliation offsets and first reactions. Canon already works this way: goblins start about 20 percent with humans and 40 to 50 with goblin NPCs, start infamous, and default to about -5 Karma [CANON `affiliation-and-reputation-system.md`, `preserved-misc-mechanics.md`].
- **Conduct** is what the Ledger records. Only conduct moves a standing for the long term.
- This is exactly the difference canon draws between Tatsuya's **unearned** elder title (a Prior granted by the necklace's mark) and the **earned** elder title that arrives when the Thrash clan's collective Affiliation reaches Allied (Conduct) [CANON `affiliation-and-reputation-system.md`, `outline/act-three-myrrhwood-expedition.md`]. Same word, two states.

## 6. What the system shows

| Surface | What it shows | Source |
|---|---|---|
| Nameplate color | White, yellow, red, gold for NPCs, blue for players | CANON `npc-tag-system.md` |
| Blood Tinted | White flips to red at about -15 to -20 Karma | CANON `preserved-misc-mechanics.md` |
| Affiliation tick | A one-line notice such as `[AFFILIATION: WYX THRASH - 45% → 48%]`, and felt prices and access | CANON; PAGE ch6, ch10, ch11 |
| Inspect panel | Fills only with what the NPC has shown the player; unknown rows stay question marks | PAGE ch5, ch10 |
| Patron notice | A HUD line when a god takes interest (the Sylthara hook) | CANON `patrons-and-world-weapons.md` |
| NPC speech | Deeds and idioms, never a label | PROPOSAL, section 4.6 |
| Nothing | No alignment screen, no good-evil bar, no Tree on any menu | PROPOSAL |

### 6.1 Why nothing prints a label [PROPOSAL]

1. NPCs have no modern vocabulary and no category called "alignment" in their world [CANON register rule].
2. Labels blur and get argued over [SRC S23], and players hide behind them [SRC S24]. Behavior cannot be argued with.
3. A visible good-evil readout would turn gold-tag NPCs into vending machines. The martial proposal already says the Affiliation number is the shadow of a gold NPC's judgment and never a lever on it [`outline/research/martial-teaching-and-mastery-proposal.md`].
4. A printed label invites prescriptive play ("my character is lawful, so..."), which is the misuse the D&D designers warn about [SRC S5, S24].
5. Open question, not proposed: a detection ability. If the author ever wants one, it should read intent in the moment (is this person about to harm me) and never a lasting cell.

### 6.2 The Conduct Ledger (author-facing, never a meter) [PROPOSAL]

A running record, per player and per significant NPC, of notable deeds. Each entry notes: the act, its Road tag, its Hand tag, what it cost the actor, who witnessed it, the zone it happened in, and whom it touched. Three readers use it:

- **The gods** read it for patterns in their key (section 11).
- **NPC AI** reads it through each faction's values to move Affiliation (section 7).
- **The author** reads it with one question: what would the world conclude about this person?

It is a drafting aid and an explanation of how existing meters stay consistent. It adds no new number to the page.

## 7. How alignment moves

### 7.1 Rules of the Ledger [PROPOSAL]

1. **Deeds, not declarations.** NPCs process in-world speech and action. A claim of virtue with no deed behind it does nothing, and gamer slang does nothing [CANON `style-guide/race-dialect-and-voice.md`].
2. **Witness rule.** A deed counts for those who saw it, heard of it from a source they trust, or found the evidence. Reports travel along clan, guild and city lines and arrive weaker. Baldur's Gate 3 requires the companion to be present [SRC S26] and New Vegas counts only what is seen [SRC S27].
3. **Cost test.** An Open Hand deed counts only if it cost the actor something. Gifts alone cannot carry a meter past Friendly; shared risk and shared cost carry it to Trusted [consistent with `martial-teaching-and-mastery-proposal.md`, section 1.4].
4. **Pattern rule.** One deed is a deed. Three consistent deeds before different witnesses is a nature. A god's notice and a gold NPC's revised read both need a pattern. Slow movement also matches the Kingmaker model, where alignment shifts over many decisions [SRC S29].
5. **Diminishing returns.** The same kind of act earns less each time, because gold NPCs remember [same proposal, section 1.4].
6. **Intent and outcome both count.** A mercy that gets innocents killed still reads Open for the one who forgave, and costs standing with whoever paid.
7. **Who started it is recorded.** The page already flags the aggressor (`THRASH CLAN ENFORCERS HAVE INITIATED COMBAT`) [PAGE ch4]. A death in answer to an attack is not a Cold Hand deed.
8. **Courage is delivery.** Canon gives Courage a social half: how convincingly a character talks to NPCs. It does not decide whether the in-character thing lands, which the register rule does [CANON `five-disciplines-stat-system.md`]. So a low-Courage player who says the right thing in-world still moves the meter, only with less force (at most one tick size).

### 7.2 Scales [CANON anchors, PROPOSAL sizes]

| Meter | Small | Notable | Landmark | Betrayal |
|---|---|---|---|---|
| Affiliation (a given faction or individual) | 1 to 2 | 3 to 4 | 5 to 8 | About twice a Landmark, and the offer closes until repaired |

- Page ticks so far are 2 to 4 points (45 to 47, 47 to 50, 45 to 48, 48 to 52, 52 to 56) [CANON ledger; PAGE ch6, ch10, ch11]. The tiers above come from the martial proposal's section 4.1. Baldur's Gate 3 uses events of about 1, 5 and 10 [SRC S26].
- **Karma sizes** [PROPOSAL, dials]. Anchors: a petty market strike costs 1 [`codex/lore/merchant-license-auction-and-jobs.md`, a proposal], goblins start about -5, arrest and Blood Tinted begin about -15 to -20 [CANON]. Suggested sizes: petty offense -1; serious offense (Nimble Hands theft from an NPC, assault, vandalism) -2 to -3; killing an unflagged player outside sanctioned PvP, or a protected NPC outside a war, -5; massacre or a repeated pattern -8 or worse. Each also costs Affiliation with the faction harmed.
- Goblin Karma starts at -5 as a Prior, so a goblin has about 10 to 15 points of room before arrest where a human has about 15 to 20 [CANON `preserved-misc-mechanics.md`; the market file notes the same].

### 7.3 One deed, three readings [PROPOSAL]

Affiliation is never a moral score. Each faction ticks a deed by its own values.

| Deed | Church of Seranis (Straight + Open) | Thrash leaders (Wild-leaning, Open to their own) | PK_Wraith's crew (Wandering + Cold) |
|---|---|---|---|
| Spare a beaten enemy who yields, at a personal cost | Notable up | Notable up if the foe fought fair; no tick if the foe was a farmer who killed clan goblins | Small down (weakness), and the player is marked as soft |
| Break a signed contract because it is unjust | Small down, unless it harmed the helpless | Small up for nerve, but a Landmark down if the contract was a clan vow | No care; they use the broken contract as leverage |
| Stand in front of a bullied runt when nobody else will | Notable up | Landmark up with Wyx and the quest opens [PAGE ch4, ch6] | They laugh; Small down |

### 7.4 How Karma, Affiliation, Fame and the gods share the work [PROPOSAL, on canon meters]

| Meter | What it measures | Direction | Reads which deeds |
|---|---|---|---|
| Karma | Punishable harm outside the sanctioned rules | Down only, never rises on its own [CANON] | Cold Hand deeds the law can punish: killing players outside sanctioned PvP, mistreating NPCs or a region's people, Nimble Hands theft |
| Affiliation | One faction's or person's trust | Both ways, from 100 down below zero | Any deed that faction's values touch |
| Fame | How widely a player is known | Reach, not direction | Any deed that travels: a stream, a world quest, a massacre |
| Patron notice | Which god is paying attention | An event, not a meter | A pattern in that god's key (section 11) |
| "Known for" | What NPCs say about you | Spoken, never stored as a number | A few repeated deeds |

- **Karma sees only the Wicked Limb, and only the slice the law can punish.** It never measures goodness. A player at 0 may be saintly or merely unseen. A player at -18 is certainly Cold toward the helpless.
- **Good is rewarded with doors, not points.** Canon already says players who treat NPCs as people gain access to places, and Yuna reached NPC locations as a beloved idol [CANON ledger, Chapter Six notes]. Open Hand conduct opens access, hidden quests, patron notice, Affiliation discounts and masters willing to teach. Cold Hand conduct opens other doors: the wicked patron, black-market contacts, fear. Both are playable, and neither needs a good-evil bar.
- **Fame.** Canon has one Fame meter. [OPEN] I recommend keeping one number for reach and letting the Ledger supply its flavor by region (famed in Myrrhwood, infamous in Lunarest). The richer alternative is the split used by New Vegas and Pillars of Eternity, where positive and negative standing are tracked separately and can coexist [SRC S27, S28]. It costs more tracking, and the author decides.

### 7.5 Zones change the law, not the deed [PROPOSAL, on canon zones]

| Zone | Karma | The Ledger | Who still reacts |
|---|---|---|---|
| Green | Strong; wardens and guards act, and Affiliation falls too | Records it | Everyone nearby, the city's faction |
| Yellow | Costs Karma; guards pursue the negative | Records it | The same |
| Red | No Karma penalty for killing [CANON] | Still records Cold Hand when the victim was weak or unwary | The victim's clan and guild (Affiliation), the wicked patron's notice, Fame |

- This is how canon's two statements fit together: red zones carry no Karma penalty, and a PKing player can still earn the wicked patron's blessing [CANON `preserved-misc-mechanics.md`, `patrons-and-world-weapons.md`].
- Worked case: PK_Wraith's crew killing Thrash goblins on the Lunarest outskirts. No Karma debt. Affiliation with Thrash is Hostile, the story spreads as Fame, and the crew may even gain standing with Lunarest, because goblins are the state's enemy [CANON `lunarest-royal-court.md`]. Karma is not conscience.
- Albion Online charges reputation for attacks in its red zones and not its black zones [SRC S30]. HGO's red zones carry no penalty by canon, so I keep canon.

### 7.6 Deeds from the page, read through the framework [PROPOSAL]

| Deed on the page | Road | Hand | Who reads it | What follows |
|---|---|---|---|---|
| Tatsuya steps between two enforcers and the runt when nobody else will [PAGE ch4] | Wild (against camp custom) | Open (risk, no reward) | Wyx, Sevish, the quest AI | Wyx 45 to 48 percent, "I like him"; the quest answers the echo of Shiv's creed [PAGE ch6; CANON ledger on the quest trigger] |
| He kills the two enforcers who started the fight [PAGE ch5] | Wandering | Level (self-defense; the system flags who initiated) | Sevish | Sevish treats it as a favor owed and not a crime [PAGE ch6]; no Karma expected |
| He tells Sevish the truth but leaves out his own provocation [PAGE ch6] | Wandering | Level | Tatsuya himself | A hidden risk if it surfaces; no tick |
| He agrees to Shiv's offer and vouches for Ru [PAGE ch9] | Straight (a vouch is a bond) | Open (takes on a burden) | Shiv, the clan | The clan treats him as an elder, unearned [PAGE ch9] |
| He refuses to send more goblins down the road, and calls Sevish's law "a good floor" [PAGE ch10] | Straight | Open | Sevish, Wyx | Thrash 45 to 47 [PAGE ch10] |
| He answers Sevish's anger with a blunt question [PAGE ch11] | Wild | Level | Sevish | Sevish approves; Thrash 47 to 50, Wyx 52 to 56 when Shiv is named [PAGE ch11] |
| He traps the raiders who were farming the clan [PAGE ch11] | Wandering | Level (red zone, retaliation) | Thrash, the raiders' guild | No Karma in a red zone; Thrash up; PK_Wraith's vendetta begins [CANON `pk-wraith.md`] |

### 7.7 Redress [PROPOSAL, [OPEN] for the author]

Canon says Karma "never goes up on its own". That leaves room for deliberate repair. Three routes:

- **Restitution.** Pay or return what was taken to the wronged region's office.
- **Witnessed service.** A penance quest set by a faction that values mercy. The Church of Seranis is the natural home: it heals, wards and restores [CANON `patrons-and-world-weapons.md`].
- **Blood-price.** A debt of service in the goblin manner. Sevish treats two dead clansmen as a favor owed, not a death sentence [PAGE ch6].

Rules: repair always costs at least twice the effort the harm took; it never lifts Blood Tinted until the number is back above the threshold; it never brings back the dead (NPC death is permanent [CANON]). If the author wants Karma strictly one-way, drop this section; nothing else depends on it.

### 7.8 How NPCs drift [PROPOSAL]

- D&D allows NPC alignments to change in response to player choices [SRC S2]. In HGO a gold NPC drifts only through an arc: a pattern plus a Landmark. **Hold** sets the resistance: a Firm NPC needs two Landmarks, a Settled NPC one, a Wavering NPC a pattern.
- Mob-tier NPCs never drift. Their faction does, when its leadership changes or its Gap closes.
- Candidates worth watching: Eren (Wavering), Haruto, Ilyan, Ru (growing into Settled), and Sevish, if Tatsuya's counsel keeps cutting the number of recruits he spends. Detail in `alignment-and-character-trees.md`.

## 8. NPCs: the Compass Card, and how a cell sets the first words

### 8.1 The card [PROPOSAL]

Every gold NPC, and any named NPC who matters, carries a hidden **Compass Card**: Placement (a cell), Hold, two Traits, an Ideal (a Creed), a Bond, a Flaw, a Line, a Trust Key, a Break, a Tell, and a Drift note. It extends the Values sheet from the martial proposal (three Values, likes and dislikes, one Line) [`outline/research/martial-teaching-and-mastery-proposal.md`, section 4.1]: that sheet is the card's lower half. The full template is `codex/characters/npc-personality-template.md`.

- **Hold** says how tightly they keep their lean under pressure: **Firm** (acts in line even at cost), **Settled** (usually in line, can be moved outside it for a good reason), **Wavering** (young, wounded or conflicted).
- **The Line** is the one thing they will not do, or will not forgive. It is not always a virtue: a villain's Line can be "never be seen to lose".
- The six **Creeds** (my renaming of the SRD's ideal categories [SRC S8]): **Order** (the group holds if the rules hold), **Freedom** (nobody should be owned), **Mercy** (spare and mend), **Hunger** (power, wealth, vengeance, or cruelty for its own sake), **Balance** (do not tip the scales), **Calling** (a craft, a faith or a cause that outranks the person).

### 8.2 First test and first assumption [PROPOSAL, from "alignment as starting attitude", SRC S2]

| By Road: how they test a stranger | By Hand: what they assume about one |
|---|---|
| **Straight** tests your word: asks for a name, a sponsor, a pledge | **Open** assumes need: "what ails you?" |
| **Wandering** tests your use: what can you do, what will it cost | **Level** assumes nothing and waits |
| **Wild** tests your nerve: provokes, jokes, dares | **Cold** assumes an angle: "what do you want from me?" |

Page check: Sevish demands words chosen with care, then laughs at frankness [PAGE ch5, ch6, ch10]; Wyx answers a quick tongue with interest [PAGE ch6]; Zinka corrects a miscount in front of the chief [PAGE ch10]. These start the same way the table predicts, which is some evidence that the cells in `alignment-and-character-trees.md` fit.

## 9. Creatures and races

### 9.1 Three kinds of creature [PROPOSAL]

- **Unaligned (instinct).** Most beasts, swarms and constructs. They have no cell and cannot make a moral choice, so they get a Temperament instead. This is D&D's own rule: low-intelligence creatures that act on instinct are unaligned [SRC S4].
- **Persons.** Anything that bargains, swears, lies or spares: the sentient races, intelligent monsters, spirits with motives. They carry a Compass Card (gold) or a two-line card (named white or yellow).
- **Bound.** A rare class for beings whose nature is sworn to a god's creed, such as the wicked patron's servants. See 9.2. Only Persons can be Bound, and never a whole race.

| Temperament | What it does | Tag at first sight | Parley? |
|---|---|---|---|
| Predator | Hunts anything it can beat | Red toward the weaker, yellow toward the clearly stronger | No |
| Territorial | Attacks inside its range | Yellow until you cross the line | No, but it can be steered around |
| Skittish | Flees unless cornered | Yellow | No |
| Guardian | Defends a nest, ward or place | White or yellow until the ward is touched | Sometimes |
| Swarm | Acts as one by numbers | Red when the numbers favor it | No |
| Mindless | Constructs and simple undead | Red or inert | No |

Creature classes I to IV measure threat, not temperament and not alignment [CANON `codex/creatures/overview.md`]. [PROPOSAL] Class IV, the world-boss tier that is "rare, named, remembered", always carries a Compass Card, and a Class III named regional threat may.

### 9.2 Binding, for Persons only [PROPOSAL, from the 3.5 qualifiers in SRC S21]

- **Bound:** born to it, with almost no exceptions (a spirit sworn to the wicked patron).
- **Inclined:** a strong culture or training pushes this way (a hobgoblin legion trains Straight [SRC S18]).
- **Common:** a tendency among many.

Fans read the old "Always" as "exceptions are rare but exist" [SRC S21], so even a Bound being can in principle break. This gives the wicked patron real servants without making any race evil.

### 9.3 Races are Priors, not natures [CANON plus PROPOSAL]

| Race | Prior already in canon | Source |
|---|---|---|
| Elf | Special treatment under elven law in Lunarest | `lunarest-royal-court.md` |
| Beastfolk, goblin, dwarf | Bad infamy in Lunarest | `lunarest-royal-court.md` |
| Goblin | Starts infamous; Karma about -5; about 20 percent with humans, 40 to 50 with goblin NPCs | `affiliation-and-reputation-system.md`, `preserved-misc-mechanics.md` |
| Orc, Drakekin | A wicked-by-reputation label, individuals may be neutral or shaded; mechanical effect OPEN | `patrons-and-world-weapons.md`, `races/orc.md` |

- [PROPOSAL] The label sets first reactions with frightened NPCs and a small Fame flavor. It never sets a Karma value, because Karma is for conduct.
- **No species is a cell.** D&D itself has moved this way: the stat-block alignment is a suggestion [SRC S5], the goblinoid alignment trait was removed in errata [SRC S19], and Monsters of the Multiverse reportedly dropped default alignments [SRC S20, search summary only].
- NPCs never act surprised about their own race's standing [CANON `craft-rules.md`]. They may be bitter, resigned or defiant.
- If the author ever needs a truly wicked people, make it a culture with a creed and a history, not a species. Commenters on Mearls's piece argue evil societies should read as functioning cultures [SRC S3].

### 9.4 Goblinoids: D&D versus HGO

- D&D history. Goblins were neutral evil, hobgoblins lawful evil soldiers whose code prizes obedience, battlefield glory and no cowardice, and bugbears chaotic evil ambushers [SRC S17, S18; the lines are fan-sourced and the official trait was later removed, SRC S19]. A fan reading calls goblinoids a tragedy: a conquered people reshaped by a conqueror god and rejected by everyone else [SRC S17].
- HGO's choice. The same types with the premise reversed. Shiv's story is that a court branded a people feral and a hunted noble spent his life proving it wrong [CANON `shiv.md`]. Hobgoblins are the code-keepers ("the hobgoblins run on a system, the goblins on whatever works" [CANON `bloodhurst.md`]), and "feral" is a stigma, not a nature. The full treatment is in `codex/lore/goblin-code-and-clan-alignments.md`.

## 10. Clans and factions: the Ethos Card

### 10.1 Fields [PROPOSAL, from SRC S7, S12, S15, S16]

- **Ethos** (a cell): what the group says it is.
- **Practice** (a cell): what it actually does.
- **Gap:** the difference between them. This is the engine of scenes; D&D treats an ethos-versus-leadership gap as good adventure material [SRC S6].
- **Creed:** one sentence in the group's own words.
- **Methods, Resources, Fear:** how it pursues its goal, what it holds (land, people, knowledge, coin), and what could end it [SRC S12, S15].
- **Ranks:** earned tiers if any. The Thrash clan says ranks exist and are earned [PAGE ch6].
- **Prior table:** starting Affiliation by race.
- **Trust Keys and Breaks:** what ticks Affiliation up and down.
- **Tell:** banner, dress, the text above a nameplate (a goblin's clan name sits above the word Goblin [CANON ledger]).
- **Allies, enemies, and a current clock:** what the group is trying to do this season [SRC S15, S16].

### 10.2 Rules of thumb

- An ethos does not decide its members' cells, or even its leaders' [SRC S6, S7].
- Lawful groups lean on written procedure and reward members who master it; chaotic groups treat tradition as disposable and shed leaders who lose the room; neutral groups deliberate and compromise [SRC S7].
- Invert one trait to find a weakness: an evil army whose real problem is that nobody follows its own regulations [SRC S7].
- A faction outlives any one member, so killing a villain does not end its plan [SRC S12]. Let factions advance in the background [SRC S12].
- Players should be able to learn what a faction values before they commit to it [SRC S11].

### 10.3 Main factions at a glance [PROPOSAL]

| Faction | Ethos | Practice | Gap |
|---|---|---|---|
| Lunarest crown and court | Ironhand (order, lineage, the realm's good) | Ironhand (a lie told as law, goblins made the state's enemy) | The rot Shiv names: the kingdom rotted long before he gave it an excuse [CANON `shiv.md`] |
| Church of Seranis | Oathkeeper (life, mending, resurrection) | Oathkeeper to Warden (doctrine-bound healing that costs the caster) | A Straight institution serving a Wild goddess [CANON `patrons-and-world-weapons.md`] |
| Thrash clan | Oathkeeper (Shiv's law: no blood among our own) | Warden (rank-and-file bully and look away) | The engine of the whole quest |
| London Spire | Warden (disciplined, patient, professional) | Warden (guerrilla kill zone; no antidote for a dying rival) | A "Knights" name over mercenary conduct |
| PK_Wraith's group | Taker (farm the weak) | Taker, with a darker wing reaching real-world crime | None needed; the gap is Wraith's own wish to be respected |
| Beast Kingdom (goblin rumor only) | Warden (order inside a wall) | Unknown; the goblin account is oral history, not fact | Whether the "peaceful kingdom" name and the goblin fear are both true |

Full placements, with reasons, are in `codex/characters/alignment-and-character-trees.md`.

## 11. Patrons and the Tree

### 11.1 What each god notices [CANON table, PROPOSAL key]

| Patron | Favored cell (CANON, names are proposals) | What it notices (PROPOSAL) | Pattern that earns notice |
|---|---|---|---|
| Seranis (goblins, beastfolk, drakekin) | Chaotic good, Freeheart | Second chances, mending the broken, loyalty to the despised | Three costly mercies toward the misjudged, before different witnesses. She picks odd bearers for her own reasons [CANON], so notice can arrive early and unexplained. |
| Sylthara (elves) | Lawful neutral, Warden | Patient preservation, harmony with old places, disciplined study | Sustained care of something old or fragile, or deep magic practice |
| Aurenor (humans) | Neutral good, Hearthkeeper | Promises kept and things built for others | Three built-and-kept deeds that served more than the builder |
| Khazren (dwarves, frostborn) | Lawful, second axis open | A hard day's work finished, loyalty to a crew | Finished work and kept contracts; open to both Oathkeeper and Warden |
| Morvaine (any evil entity) | Neutral to evil, Taker edging toward Ironhand | Bargains, strength that refuses to beg, a price paid | Predatory or transactional conduct, PKing included [CANON] |

### 11.2 Rules [PROPOSAL, inside the canon rules]

- **Offer rule.** When a pattern matches a god's key, that god offers a blessing. The race-affinity god "notices faster" [CANON], so its threshold is lower: two matching deeds instead of three.
- **Two offers, one acceptance.** A pattern that straddles two keys can draw two offers; the canon example is a PKing dwarf deeply tied to dwarf religion, offered the wicked patron and the dwarf patron. Changing later needs the one-time 500,000 yen respec [CANON].
- **Two keys: Conduct and Craft.** Sylthara's interest in Tatsuya is "because he does magic" [CANON]. So gods notice what a player practices as well as how they treat people. The Conduct key reads the Ledger; the Craft key reads what the player does with their hands, voice or mind.
- **Not gatekept.** No notice depends on race or class [CANON]. If the author makes some patrons rare with hidden unlocks, put the unlock behind the Craft key so players can find it by doing.
- **A notice is a response, not a rewrite.** It never changes the player's cell.

## 12. Author checklist: misunderstandings that would break the world

1. **Alignment describes, it does not leash.** A Freeheart can obey a bad order once; an Ironhand can be kind to a child [SRC S2, S5].
2. **Neutral is not apathy.** A Wayfarer may be the most purposeful person in the room [SRC S2].
3. **Wild is neither random nor feral.** It is conscience and loyalty over rules [SRC S3; CANON for "feral"].
4. **Straight is not "obeys every rule".** Do not write the lawful-stupid knight [SRC S22].
5. **Cold is not cartoonish.** Give the wicked a creed, a structure and a coherent motive [SRC S2, S3].
6. **Opposed cells can work together.** Friction between a Straight and a Wild ally is a scene, not a split [SRC S2, S29 GameBanshee].
7. **No race is a cell** [SRC S5, S19].
8. **A group is not its members.** Check ethos, practice and leaders separately [SRC S6, S7].
9. **Never print a label.** Show deeds [SRC S23, S24].
10. **A placement is a start, not a cage.** Every card needs a Line and a Trust Key that say what happens on the page [SRC S9].
11. **Karma is law, not conscience.** No Karma means no crime, not no guilt [CANON zones].
12. **Tone.** Heroic settings suit clear good and evil, grittier settings suit moral grey [SRC S12]. Eryndal is a grey world where individuals draw clear lines.

## 13. Conflicts with canon, and open questions

Where my proposals touch canon, canon wins.

**Conflicts and how I resolved them**

1. **Name collision.** Canon calls the global punitive meter "Karma/Alignment"; patron canon uses "alignment tree". I kept the meter exactly as locked and named the nine-cell frame "the Tree".
2. **Redress versus "never goes up on its own".** Section 7.7 is an open proposal. If the author wants Karma strictly one-way, delete 7.7 and nothing else breaks.
3. **One Fame meter versus a split.** Canon has one. I kept one and marked the split [OPEN].
4. **Patron table gives ranges, not cells.** "Lawful" for Khazren and "neutral to evil" for Morvaine have no second axis or fixed cell; I kept them as ranges.
5. **"Gods go by trait, not good versus evil" versus an "alignment favored" column.** Reconciled by treating the cell as a measuring frame and giving each god a separate key of deeds and crafts.
6. **Orc and Drakekin reputation label.** Kept as a Prior; canon leaves its mechanical effect open, so my proposal is limited to first reactions and Fame flavor.
7. **Superseded patron lines.** The older "default and switch" rule and "Orc defaults to Morvaine" are superseded in the ledger and I ignored them.
8. **Wyx's alignment.** The author is unsure and reads her as chaotic good; I keep that and note a lawful lean in `alignment-and-character-trees.md`.
9. **Rank wording.** Wyx says there are earned ranks [PAGE ch6]; a later ledger entry says goblins have no formal ranks and the page uses only "co-leader" [CANON ledger]. I treat ranks as informal earned tiers with no rank labels on the page. Details in the goblin file.

**Open questions, ranked**

1. Should Karma ever be repaired (7.7)? Recommendation: yes, slowly, through service.
2. One Fame or two (7.4)? Recommendation: one number, regional flavor.
3. Should any player ever see the Tree? Recommendation: no. If the Church of Seranis ever offers a "reading", make it one in-world sentence.
4. Which patrons are rare, and how do hidden unlocks work? Canon leaves this open (11.2 offers the Craft key).
5. Is Lunarest's elven law written down and enforced by wardens? It would give the Prior a concrete face.
6. May an inspect panel ever show a "known for" line? Recommendation: only as the NPC's own words, once earned.

## 14. Source key

"Fetched" means I read the page; "search summary" means I saw only a search result's text and did not open the page, so treat those claims as softer. Everything is paraphrased.

| Key | Source | URL | Status |
|---|---|---|---|
| S1 | D&D Beyond, Free Rules (2024), Creating a Character (alignment, alignment and personality, evil characters) | https://www.dndbeyond.com/sources/dnd/free-rules/creating-a-character | fetched |
| S2 | D&D Beyond, "Breaking Down Alignment in D&D" | https://www.dndbeyond.com/posts/1869-breaking-down-alignment-in-d-d | fetched |
| S3 | D&D Beyond, Mike Mearls, "Alignment and Your Place in the D&D Multiverse" | https://www.dndbeyond.com/posts/44-alignment-and-your-place-in-the-d-d-multiverse | fetched |
| S4 | D&D Beyond, Basic Rules, Monsters (alignment as a default, unaligned creatures) | https://www.dndbeyond.com/sources/basic-rules/monsters | fetched |
| S5 | ENWorld thread quoting Jeremy Crawford on alignment | https://www.enworld.org/goto/post?id=8038276 | fetched, secondhand |
| S6 | Roll20 compendium, Alignment (organization ethos does not set members' alignment) | https://roll20.net/compendium/dnd5e/Rules:Alignment?expansion=33359 | search summary |
| S7 | Kismetrose, "Developing Nuanced NPC Groups via Alignment and Government" | https://fantasy.kismetrose.com/DMNuancedGroups.html | fetched |
| S8 | SRD, Personality and Background (aidedd mirror) | https://www.aidedd.org/en/rules/background/ | fetched |
| S9 | BJ Keeton, critique of traits, ideals, bonds and flaws | https://bjkeeton.substack.com/p/bonds-flaws-traits-and-ideals-oh | fetched |
| S10 | The Angry GM, "Two-Note NPC" | https://theangrygm.com/angrys-two-note-npc/ | fetched |
| S11 | Tribality, "Factions, Renown and How to Make Your Players Care" | https://www.tribality.com/2019/08/20/factions-renown-and-how-to-make-your-players-care-about-them/ | fetched |
| S12 | Tribality, "Using Factions in Your Campaign" | https://www.tribality.com/2017/03/10/using-factions-in-your-campaign/ | fetched |
| S13 | ENWorld, "Renown: Have You Used This Optional Rule?" | https://www.enworld.org/threads/renown-have-you-used-this-optional-rule.687821/ | fetched |
| S14 | Nerdarchy, "D&D Ideas: Renown" | https://nerdarchy.com/dd-ideas-renown | fetched |
| S15 | ENWorld, "Really good structure for Factions (system agnostic)" | https://www.enworld.org/threads/really-good-structure-for-factions-system-agnostic.714766/ | fetched |
| S16 | Roll20 compendium, Blades in the Dark, The Faction Game | https://roll20.net/compendium/BITD/The%20Faction%20Game | search summary |
| S17 | ENWorld, "Goblinoids in D&D 5e: Their Origin, Story, and Tragedy" | https://www.enworld.org/threads/goblinoids-in-d-d-5e-their-origin-story-and-tragedy.685683/ | fetched, fan analysis |
| S18 | Arcane Eye, Hobgoblin 5e guide (summarizing Volo's) | https://arcaneeye.com/players/dnd-5e-races/hobgoblin-5e/ | fetched |
| S19 | D&D Beyond, Volo's Guide to Monsters errata (alignment trait removed from goblinoid entries) | https://www.dndbeyond.com/sources/dnd/sae/volos-guide-to-monsters | fetched |
| S20 | Monsters of the Multiverse and default alignments (search-result text; exact page not identified) | https://www.belloflostsouls.net/?p=389840 and https://belloflostsouls.net/?p=433995 | search summary, unverified |
| S21 | ENWorld thread on what "Always" means in 3.5 monster alignments; Paizo thread on the qualifiers | https://www.enworld.org/goto/post?id=4726230 ; https://paizo.com/threads/rzs2qijt | first fetched, second search summary |
| S22 | Tropedia, "Lawful Stupid Chaotic Stupid" | https://tropedia.fandom.com/wiki/Lawful_Stupid_Chaotic_Stupid | search summary |
| S23 | Dungeon Chatter, "Why No One Understands Alignment" | https://dungeonchatter.substack.com/p/why-no-one-understands-alignment | fetched |
| S24 | The Dice Society, "Towards better alignment" (quotes Matt Mercer) | https://thedicesociety.substack.com/better-alignment | fetched |
| S25 | Gnome Stew, "Good, Evil, Chaos, Lawful, which direction does your character go?" | https://gnomestew.com/playing-alignments-in-rpg-good-or-not-so-good/ | fetched |
| S26 | Baldur's Gate 3 wiki, Approval | https://bg3.wiki/wiki/Approval | fetched |
| S27 | UHS Hints, Fallout: New Vegas faction reputation | https://www.uhs-hints.com/uhsweb/hints/fallout-newvegas/2625 | fetched |
| S28 | Magic Game World, Pillars of Eternity II dispositions and reputations; Obsidian forum thread on reputations | https://www.magicgameworld.com/pillars-of-eternity-ii-deadfire-dispositions-reputations/ ; https://forums.obsidian.net/topic/96154-reputations-and-factions | first fetched, second search summary |
| S29 | Pathfinder: Kingmaker alignment (Fextralife wiki; GameBanshee Update 40; Steam forum thread) | https://pathfinderkingmaker.wiki.fextralife.com/Alignments ; http://www.gamebanshee.com/kd464 ; https://steamcommunity.com/app/640820/discussions/0/3463849349659688485 | first two fetched, third search summary |
| S30 | Guildorder, Albion Online zone color system | https://guildorder.com/games/albion/wiki/zone-color-system | fetched |
| S31 | Ultima IV virtues (Ultima Codex; Wikipedia) | https://wiki.ultimacodex.com/wiki/Axiom ; https://en.wikipedia.org/wiki/Ultima_IV:_Quest_of_the_Avatar | search summary |
