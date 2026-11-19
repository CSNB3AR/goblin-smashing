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
