# HGO Game System — The Glory Codex

This is the mechanical backbone of Hero's Glory Online: stats, leveling, the goblin signature mechanic, and the deck-building layer. It merges the "Voyage Codex" brainstorm (originally drafted under a placeholder title, "Heroes' Voyage Online") into confirmed HGO/Eryndal canon, and folds in the mechanics flagged as worth preserving from `bible/old-draft-chapter-bible.md`. Everything here is Eryndal-branded; no "Voyage Site," "Heroes' Voyage," or other placeholder terminology survives past this document.

For character facts, world facts, and craft rules, defer to `bible/writing-bible.md`. This document is mechanics only.

**House style reminder (see Writing Bible §10 for the full rules):** mechanics are shown sparingly and always filtered through what Tatsuya perceives, small HUD notifications in his vision, brief inner-monologue math, the occasional stat callout at a real milestone. Never a dumped stat block mid-fight. Never narrator-voice exposition of a rule Tatsuya wouldn't be actively thinking about in the moment. Brains-over-brawn: the story rewards game knowledge and tactics (see the Tactical Cartographer title below) over raw numbers, in keeping with the King's Avatar governing principle.

## 1. Core Stats: The Five Disciplines + Energy

Every creature, player character, and named NPC in Eryndal runs on the same six numbers. These are also the stat line printed on any deck-building card representation of a creature or hero (see §4).

- **Courage** — willpower, bravery, leadership, fear resistance, stabilizing risky gambles. Drives "save the skill" checks and some defensive/social challenges.
- **Power** — raw physical strength, damage output, intimidation, breaking things. Primary stat for physical attacks and Power Challenges.
- **Wisdom** — perception, knowledge, cunning, magical affinity, resisting tricks or mental effects. Governs skill-learning speed and Wisdom Challenges.
- **Speed** — agility, reflexes, evasion, movement, initiative in many situations. A goblin favorite for hit-and-run play.
- **Fortune** — luck, probability, critical hits, loot quality, random-event success, and every Gambler-path effect. Higher Fortune makes gambles safer and better, and is the gate for goblin signature mechanics (see §3). Fortune Challenges cover high-variance moments.
- **Energy** — the depletable resource pool: HP plus fuel for big abilities. Damage reduces it; zero means defeated. In the story, this reads as stamina/mana that regenerates between fights or slowly during them.

**Resolving checks in prose:** opposed checks or checks against a difficulty are handled narratively, only surfaced on the page when the tension calls for it. Margin of success can add damage or a bonus effect. Author judgment and narrative weight drive most outcomes; a check is only shown as a number when a gamble is genuinely live.

## 2. Leveling & Progression

- Level starts at 1 (or backstory-appropriate).
- XP comes from quests, fights, exploration, and world events.
- On level up: +1 to all five Disciplines (baseline growth), a handful of stat points to distribute (narrated through action: training, quests, "the bones warmed at his throat"), an Energy increase, and occasionally a new Codex Entry (skill or minor item) from class/race lists or story rewards.
- **Racial/Class growth:** Goblins grow Fortune faster than other races (an extra point or two per level, or a bias in free stat points), consistent with the underdog/luck-based arc the goblin race already carries in the Writing Bible. Other races grow more balanced or lean into their own strengths.
- **Codex Entries** (skills, feats, gear) have tiers, Bronze through Silver, Gold, and beyond as the story and levels advance. New entries are introduced organically, two to four per major arc, never as an upfront catalog dump. Scaling comes from higher tiers and better gear, not bigger numbers pasted onto the page.

## 3. The Goblin Signature Mechanic: The Call of the Bones Necklace

This merges the old draft's central goblin artifact with the Gambler mechanic, rather than inventing a second item. Shiv's Warset stays a 7-piece legendary set (see `bible/old-draft-chapter-bible.md`); the necklace remains piece 1 of 7.

**Call of the Bones Necklace** — legendary bound item, granted by Shiv during the "Call of the Bones" World Quest. In addition to its established effects (negates the goblin INT penalty, unlocks the Shaman's Veil spirit-magic path), it is the vessel for the goblin Gambler path: a small grant of bonus Fortune, and access to the necklace's Facets (three charges per in-game day, "the bones only whisper so much before dawn").

**Gambler's Gambit** (active skill, costs 1 Facet):
- **Draw & Load** — loads a random temporary skill ("Codex Trick") into an open skill slot. Tier is determined by current Fortune and level (Bronze early, Silver mid, Gold+ later). Higher Fortune means a better tier or safer odds. The drawn skill is volatile for one round after loading.
- **Save-if-hit / volatile phase** — if Tatsuya is targeted by an attack while the drawn skill is still volatile, he gets an immediate reaction Fortune Challenge to stabilize it:
  - **Success** (especially high margin): the skill locks in for the rest of the encounter, sometimes empowered. *The bones held.*
  - **Failure**: the skill fizzles, often with a minor self-debuff or small backfire. *The bones bit back.*
- This is the core risk/reward tension of the goblin's signature mechanic: getting hit mid-gamble is dangerous, but surviving the hit while stabilizing the draw upgrades it.

**Sample Bronze-tier draws** (early story, low Fortune/level — expand per tier as the story needs more): a minor self-debuff or backfire; a Speed/evasion buff; a bonus to the next attack; a temporary Wisdom buff or weakness-reveal; on a rare good roll, something stronger, a borrowed trick or a real stat swing.

Goblin Gas, the Goblin Gas + fire = **Goblin Flare** combo, and Ancient Boneflame Barrage (with its toxin-effect bonus) stay exactly as established in the old draft, unaffected by this merge, they belong to the goblin/shaman kit generally, not specifically to the necklace.

## 4. The Deck-Building Layer

Ties directly to Pillar 3 of the Writing Bible: a player's permanent, earned inventory functions as their deck, and what they bring into a competitive match matters as much as their class. Never named as its direct inspiration on the page, described functionally only.

- **Creature/Hero cards** (narrative shorthand, not literally shown to the reader as cards): name, race/class/path, the six Discipline+Energy stats, abilities (innate/activated/triggered), rarity tied to story progression.
- **Battlegear / items:** equipped gear (the Call of the Bones Necklace, later Warset pieces, other earned items) grants stat bonuses and unlocks abilities. Limited equip slots keep loadouts meaningful.
- **Skills:** played for damage, buffs, direct effects, or to trigger a Gamble. Some require winning a Discipline or Fortune Challenge to land.
- Competitive matches (see Writing Bible §7 for the 3v3/5v5 ruleset) are where the deck-building layer is most visible on the page: players bring their earned kit in alongside their base class, and world-level items are nerfed for balance but still matter.

## 5. Preserved Mechanics From the Old Draft

These carry forward unchanged from `bible/old-draft-chapter-bible.md`, flagged there as worth keeping:

- **Skill combo system** — Goblin Gas + fire = Goblin Flare; toxin effects boost Ancient Boneflame Barrage's damage/radius. Reusable and mechanically satisfying, fits the deck-building pillar.
- **Karma/Alignment system** — killing players outside sanctioned PvP shifts alignment and visibly flips the nameplate from white to red ("Blood Tinted"). A strong, visible consequence system for open-world PvP.
- **Seven-day death lock** — dying carries a real week-long penalty, not just a respawn timer.
- **Physical Arts** — a distinct skill category from spells (Drosh's Veil-Pierce Gaze, Silent Three Fang), giving goblins/hobgoblins a combat identity separate from caster classes.
- **Prestige/ranking ladder** — numeric competitive tiers (Platinum 40K, Diamond 75K, Master 120K+), usable as visible LitRPG texture on the ranked ladder.
- **Tactical Cartographer title** — earned for drawing up a battle plan, not just fighting. Rewards the brains-over-brawn playstyle the story leads with.
- **In-game time dilation** — time moves faster inside HGO than in the real world. Flagged as needing pacing care: any quest timer stated in-game (e.g., a three-day ultimatum) needs to be checked against how it lands against Tatsuya's real-world schedule before it's used in a chapter.
- **Live streaming as an organic exposition tool** — chat reactions doing the work of flagging "this is unusual" on-screen, without narration or an announcer stating it outright. A deliberate craft technique, not just a mechanic, reuse it the same way.

## 6. Open Flags

- Bronze/Silver/Gold Codex Trick tables are intentionally left thin here (a handful of samples only). Expand table entries only when a specific chapter needs a specific draw, no upfront full-table authoring.
- The Prestige/ranking ladder numbers above are old-draft placeholders (Platinum 40K, Diamond 75K, Master 120K+). Confirm with Bobby before they appear on the page if a chapter needs Tatsuya's or a rival's rank stated explicitly.
