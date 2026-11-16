# Thornwatch Elixirs

**Status:** New codex entry. Forward material for Book Two (the Thornwatch push, the Kazuhaya brand, the goblin trade group). Author-stated direction: the Thornwatch Forest is a high-level farming zone with mythical beasts and rare elixir drops, and its elixirs are what the king needs and what top guilds pay a lot for. Everything marked **proposal** or **placeholder** is a designed number or name the author has not approved. Nothing here appears on the page yet. See "Open and conflicts" at the end.

## Why this file exists

The only elixir on the page is the **Minor Elixir** (Uncommon, Alchemy-crafted mana restoration, `codex/crafting/food-and-consumables.md`). Tatsuya sold two of them for **21,000 shillings each** (2,100 HGO Coins, 8,400 yen each, 16,800 yen for the pair, see `codex/characters/tatsuya-kazehaya.md` and the Chapter Seven sale in `outline/canon-ledger.md`). That is an early-game trade good. It is far too weak to be something a top guild or a king cares about, and this file does not change it. The Minor Elixir stays exactly as dramatized.

The Thornwatch elixirs sit far above it. They come from a zone with high-level mythical beasts, they cost real money, and a few of them change the outcome of a fight. The top of the line is the **Phoenix Elixir**. In-world, when players or NPCs say "the elixir" about Thornwatch, they mean the Phoenix Elixir. The rest are "Thornwatch elixirs" or by their own names.

**Currency used throughout:** 10 shillings = 1 HGO Coin = 4 yen, so 1 yen = 2.5 shillings. Reference points: Minor Elixir 21,000 shillings (8,400 yen). Ohema's surgery is about 4,000,000 yen, which is 10,000,000 shillings (`codex/subplots/tabuchi-schematics-and-family-debt.md`). The announced Crownfall prize pool is 10,000,000 yen, which is 25,000,000 shillings.

**Rarity names used exactly as in `codex/lore/deck-building-rarity-and-classes.md`:** Common, Uncommon, Rare, Legendary, World. World is reserved for World Quest rewards, so no Thornwatch elixir is World tier. The Phoenix Elixir is **Legendary**.

## The line at a glance

| Elixir | Rarity | What it does in one line | Median price (shillings) | Yen |
|---|---|---|---|---|
| Wispdew Tonic | Uncommon | Fast mana refill for the trek | 60,000 | 24,000 |
| Hoarfrost Ward | Rare | Frost resistance for the boss's cold attacks | 190,000 | 76,000 |
| Clearspring Elixir | Rare | Cleanses poison and one other debuff, short poison immunity | 280,000 | 112,000 |
| Barkhide Elixir | Rare | Big defense and HP buff | 320,000 | 128,000 |
| Redmaw Elixir | Rare | Attack buff with a cost | 380,000 | 152,000 |
| Ironbark Aegis | Legendary | Large damage shield, long cooldown | 1,100,000 | 440,000 |
| **Phoenix Elixir** | **Legendary** | **Massive attack buff, then a one-time "get out" revive** | **3,000,000** | **1,200,000** |

The Phoenix Elixir is the top of the line by price, effect and scarcity. It is not the only item that matters, and a guild that can only afford Rare-tier elixirs still gets real benefit from them.

---

## 1. The Phoenix Elixir (Legendary)

### In one paragraph

A drinkable buff that lasts 10 minutes. While it is active it raises the drinker's damage by a large amount. If the drinker drops close to death, or would die, it triggers once: the drinker is pulled back to a small amount of health and gets a **30-second window** where they cannot be hurt, cannot hurt anyone, make no sound, and have every harmful status effect removed. They can still be seen. It is an escape tool, not a win button. When the 30 seconds end, whether to fight on or leave is the drinker's choice. A second one cannot be used for 24 hours. It is very, very expensive.

### Card (sample format, matches the on-page item card style)

```
[ITEM: PHOENIX ELIXIR - LEGENDARY]
Drink time: 1.5 seconds. Buff duration: 10 minutes.
While active: +40% damage dealt. +10% damage taken.
Rebirth (once): at 10% HP or lower, or on a killing blow, you are held
at 5 HP and enter EMBER VEIL for 30 seconds.
EMBER VEIL: cannot be damaged, cannot deal damage, cannot be heard,
all harmful status effects removed.
After Rebirth: ASHEN MARK for 24 hours. You cannot drink another.
```

### Numbers (all proposal unless noted)

| Property | Value |
|---|---|
| Rarity | Legendary |
| Drink time | 1.5 seconds. Cannot be drunk while stunned, immobilized, silenced or asleep, so it must be drunk before the fight turns. |
| Buff duration | 10 minutes, ticks down in real combat time and while logged in |
| Attack buff | +40% damage dealt, all damage types, applies to Physical Arts, spells and item damage (thrown bombs included). Stacks separately from gear and ability bonuses, per the buff rule in `codex/crafting/food-and-consumables.md`. |
| Cost of the buff | +10% damage taken while the buff is active. The potion makes the drinker hit harder and also easier to kill, which is why the Rebirth clause exists. |
| Rebirth trigger | One charge per elixir. Fires when the drinker's HP falls to 10% of max or lower, or when any single hit would reduce HP to 0 or below. Both cases use the same one charge. |
| Rebirth health | **A flat 5 HP** (author decision, latest). It is the same number at every level, so at high level it is a sliver and the Veil is what matters. If the drinker is already above 5 HP when the 10% trigger fires, their HP is left where it is and not lowered. |
| What a lethal hit does | The killing blow is negated. The drinker is not dead, does not go to a Cathedral, takes no 72-hour death lock, and does not roll the death-drop chance. The attacker gets no kill credit, no loot and no Karma change for a kill, because no kill happened. |
| Ember Veil duration | 30 seconds, starts the instant Rebirth fires |
| While in the Veil | Cannot take damage of any kind (direct, area, damage over time, fall, environmental). Cannot deal damage of any kind. Cannot be heard: footsteps, ability sounds, voice and item sounds are silent to everyone in the world. The drinker can still be **seen**. Hostile NPCs drop aggro on the drinker and cannot re-target them until the Veil ends. All harmful status effects are removed at the moment of Rebirth (Poison, Nauseous, Burning, Chilled, Slowed, Stunned, Rooted, Silence, Deafen, Fear, curses). New harmful status effects cannot be applied during the Veil. Beneficial buffs are kept. |
| What the drinker can do in the Veil | Move, use movement skills, use consumables, use non-damaging utility, buff or heal allies, loot, pick up drops, talk on the party channel. Allies can heal the drinker. HP regeneration continues. |
| What the drinker cannot do | Attack, cast damaging spells, throw bombs, trigger gadgets. Any trap, bomb or device the drinker places during the Veil stays inactive until the Veil ends and then arms normally. |
| After the Veil | The Veil ends at 30 seconds with no extension. The drinker is visible, targetable and damageable again at whatever HP they have. The attack buff continues if it has time left. Staying to fight or running is entirely the drinker's call. |
| Cooldown | **Ashen Mark, 24 hours, starts when Rebirth fires.** While the Mark is active the Phoenix Elixir cannot be drunk (the item greys out with "Ember still cooling"). Runs on the same real clock as the death lock and pass-out lock, so logging out does not pause it. If the 10-minute buff ends without Rebirth firing, no Mark is applied, but that bottle is spent. |
| After the buff ends | Cinder Crash: 3 minutes of -25% SP and MP regeneration. |
| Stacking | Only one Rare-or-higher timed elixir can be active at once (proposal, applies to this whole line). Instant elixirs (Wispdew Tonic, Clearspring Elixir) are exempt. |
| Dispel | The buff and the Veil cannot be dispelled or stolen. |
| Tradable | Yes. It is not bound. Bottles stack to 1. |

### Why it is a "get out" potion

The design is deliberate. The Veil cannot win a fight for the drinker: they cannot deal damage, so they cannot finish anything. It can only buy 30 seconds of safety. In those 30 seconds a player can run, be healed by allies, drink a healing consumable, reposition a party, or cross a dangerous stretch. A drinker with a Warden in the party can return from the Veil at far more than 5 HP. A drinker alone returns at 5 HP and has to leave. The 40% attack buff is the reason to drink it before a hard fight, and the Rebirth is the reason a top guild's front line carries one.

### Where it comes from

The Phoenix Elixir has two sources, which fits both the author's "rare elixir drops" and the author's "Tatsuya can farm, craft and sell these."

**Source A, rare drop (proposal).** The adult **Cinderwing** (below) drops a finished Phoenix Elixir at about **0.2%** per kill. This is the rare drop players already know the forest has. It is the forest's biggest drop and it is almost never seen.

**Source B, crafted (proposal).** The adult Cinderwing drops an **Ember Heart** at about **10%** per kill. A crafter with the right profession tier turns it into a Phoenix Elixir.

### The beast and the plant

- **Cinderwing** (placeholder name, OPEN). A mythical fire bird, large enough to carry off a person, that nests in ash groves in the Thornwatch Forest's high ground. It is the forest's one fire creature, which is the point: it lives in a cold, frost-kin forest by burning its own nesting ground bare.
  - **Cinderwing Fledgling:** Class III (`codex/creatures/overview.md`), found in the open forest around the burn patches. Needs a party. Drops Cinder Down (Rare material) and low-odds Rare elixirs.
  - **Adult Cinderwing:** top of Class III (not Class IV, which stays reserved for the Crownfall world boss). Needs a full party. Spawns only in the high-ground **ash groves**, which lie on the far side of the fort from the way in. Four groves, about an 8-hour respawn each (placeholders). Fire immune. Weak to frost and to poison stacks. Drops one Ember Heart at 10%, one to three Cinder Plumes always, and the finished Phoenix Elixir at 0.2%.
  - Unlike the three event beasts of the Crownfall raid (defense, cleansing, attack, `codex/pro-scene/crownfall-siege-event.md`), the Cinderwing is not one of the three. It is a normal farmable spawn outside the event.
- **Ashbloom** (placeholder name). A pale plant that only grows in ground the Cinderwing has burned bare. Harvested as a petal. Without it the Ember Heart cannot be bound.

### Recipe (proposal)

**Profession:** Alchemy / Poisoncraft, **Tier 7 of 8** (`codex/crafting/professions.md`). Tier 8 is the domain of a handful of named crafters, so Tier 7 is the highest a normal serious crafter reaches. Station: Clan Workbench or equivalent. The Portable Campfire Kit has a very low success chance on anything Tier 4 or above and is not usable for this.

| Ingredient | Qty | Source | Approx. market value |
|---|---|---|---|
| Ember Heart (Legendary material) | 1 | Adult Cinderwing, 10% | 1,000,000 shillings |
| Wispglass (Rare material) | 2 | Forest floor, from wisps that dissolve on their own | 160,000 total |
| Ashbloom petal | 4 | Burned ground in the ash groves | 80,000 total |
| Flarebloom | 6 | Existing material, ignition base (`codex/materials/organic.md`) | 12,000 total |
| Glacial Marrow | 1 | Existing Valefrost reagent, balances the fire (`codex/materials/overview.md`) | 30,000 |
| Monocrystal vial (cut wind monocrystal) | 1 | Existing material (`codex/materials/monocrystals-and-mono-steel.md`) | 20,000 |

**Total input cost:** about 1,300,000 shillings (520,000 yen) at market prices.

**Success chance (proposal):** about 60% for a Tier 7 crafter at tier. A high-Fortune crafter such as a goblin gets the "Lucky Craft" bonus described in `codex/crafting/crafting-stations-and-process.md`, about +10 points, so about 70%. Failure consumes the Ember Heart and returns about half of the other ingredients. A Lucky Craft success can add a bonus effect: +2 minutes of buff duration. Expected cost per finished bottle at 60% is about 2,200,000 shillings if the crafter bought the Heart, so the crafter's margin at a 3,000,000 shilling sale is thin unless they also farmed the Heart themselves. Farming the Heart is where the real money is, which is why guilds that own the groves are rich.

**Recipe discovery (proposal).** Recipes are learned by doing, per the crafting process. The Phoenix recipe is not a public menu item. The first printed version could be found in the ruined armory of the Thornwatch fort as the king's own expedition notes, which would give the guild holding the fort (London Spire) first access. This is optional and flagged below.

### Supply (placeholder math, so the price makes sense)

- Four groves, about 12 adult spawns a day in total, realistically about 6 killed a day because of contest.
- 6 kills x 10% = about 0.6 Hearts a day, about 4 a week across the whole server.
- At 60% crafting success, about 2 to 3 finished bottles a week, plus almost nothing from the 0.2% direct drop.
- That is what holds the median price at about 3,000,000 shillings and why top guilds treat each bottle as a planned purchase.

### Value and buyers

| Measure | Shillings | HGO Coins | Yen |
|---|---|---|---|
| Typical player-to-player sale | 3,000,000 | 300,000 | 1,200,000 |
| Low end (patient buyer, plentiful week) | 2,200,000 | 220,000 | 880,000 |
| High end (raid week, shortage) | 5,000,000 | 500,000 | 2,000,000 |
| Court standing order (Prince Ilyan's quartermaster, see below) | 5,000,000 | 500,000 | 2,000,000 |
| Ember Heart alone | 1,000,000 | 100,000 | 400,000 |

One typical bottle is about 30% of the 10,000,000 shilling surgery cost, which is the single biggest pacing flag in this file (see Open).

**Who buys:**
- **Top guilds.** Raid leaders, front-line tanks and the person carrying the objective. A guild cannot afford a bottle for every member, so each war or raid it buys a few for the people whose death costs the most. The Veil lets them survive a 72-hour-lock death and extract.
- **Siege-style and Node War leaders** (once those are open).
- **The court**, through the Prince Ilyan side (see section 3).
- **Rich solo players and sponsored pros.** A sponsored player can have a bottle bought for them.
- **Dealers.** Goblin trade groups and auction-house middlemen who hold stock until a raid week.

**How it sells:** Per `codex/crafting/crafting-stations-and-process.md`, Rare-tier and above do not sell through standing buy orders. The Phoenix Elixir moves through private contracts and direct player-to-player trades. The auction board's posting fee and cut of the sale ("that tax eats most of it", `outline/canon-ledger.md`) would take a large share of a 3,000,000 shilling item, so serious sellers avoid it. No tax figure is set.

---

## 2. The other Thornwatch elixirs

All numbers are proposals. Each also exists as a lower-chance drop from its beast, and each is crafted by Alchemy / Poisoncraft.

### 2.1 Wispdew Tonic (Uncommon)

- **Effect:** Restores 50% of max MP over 10 seconds. Shares a 90-second cooldown with other mana potions. No side effect.
- **Source:** Dew gathered from **wispmoss**, a pale moss that grows where wisps drift through the forest (`codex/locations/eryndal-world-overview.md`, wisps are quick, low-HP and drawn to high-mana users). Alchemy Tier 3. Recipe: 3 wispmoss, 1 Spiritmoss (`codex/materials/organic.md`), 1 empty vial.
- **Value:** 60,000 shillings (6,000 coins, 24,000 yen). About 3 times a Minor Elixir. Uncommon, so it sells instantly to standing buy orders like the Minor Elixir does.
- **Buyers:** Everyone crossing the forest. The trek burns through resources, so this is the forest's trade-goods staple, the way Minor Elixirs are Lunarest's.

### 2.2 Hoarfrost Ward (Rare)

- **Effect:** +60% Frost resistance and immunity to Chilled and frost-based Slowed for 5 minutes.
- **Side effect:** -20% Fire resistance for the same 5 minutes.
- **Source:** Frostroot (high-ground plant) plus Glacial Marrow (`codex/materials/overview.md`, normally a Valefrost reagent; the forest sits near Frostborn and Dwarven land). Alchemy Tier 5.
- **Value:** 190,000 shillings (19,000 coins, 76,000 yen).
- **Buyers:** Parties heading for the frost-breathing boss in the high ground (`codex/pro-scene/crownfall-siege-event.md`). Valefrost-bound guilds.

### 2.3 Clearspring Elixir (Rare)

- **Effect:** Instantly removes all Poison and Toxin stacks and Nauseous, plus one other harmful status effect of the drinker's choice. Then 120 seconds of immunity to Poison and Nauseous.
- **Source:** **Hartwater**, the clean water that collects in the antlers of the **Clearwater Hart** (placeholder name, Class III stag, found beside springs). Alchemy Tier 5.
- **Limit:** It does not remove the zone poison that kills late entrants into the Crownfall forest. That is a zone rule, not a status effect.
- **Value:** 280,000 shillings (28,000 coins, 112,000 yen).
- **Buyers:** Any gas or poison user. A goblin gas build can drink it to clear the Nauseous stacks from its own Goblin Gas (`codex/crafting/debuffs-and-resistances.md`). Also guilds fighting toxin-heavy opponents.

### 2.4 Barkhide Elixir (Rare)

- **Effect:** +35% Physical defense and +20% max HP for 5 minutes (the extra HP is temporary and drops off when the buff ends).
- **Side effect:** -15% Speed for the duration.
- **Source:** **Aurochs sap** from the **Barkhide Aurochs** (placeholder name, Class III, a bark-plated bull). Alchemy Tier 5. Recipe: 2 aurochs sap, 3 Spiritmoss, 1 Glacial Marrow.
- **Value:** 320,000 shillings (32,000 coins, 128,000 yen).
- **Buyers:** Tanks (Ironbreakers) and front-line players. It matches the defensive buff the raid's defense beast gives.

### 2.5 Redmaw Elixir (Rare)

- **Effect:** +25% damage dealt for 3 minutes.
- **Side effect:** -10% defense while active, then 20 seconds of "Winded" (-50% SP regeneration).
- **Source:** **Redmaw tusk marrow** from the **Redmaw Direwolf** (placeholder name, Class III, a pack hunter). Alchemy Tier 5. Recipe: 2 marrow, 4 Flarebloom, 1 Cracked Bloodstone (`codex/materials/overview.md`).
- **Value:** 380,000 shillings (38,000 coins, 152,000 yen).
- **Buyers:** Damage dealers (Berserkers, Spellforgers) before a burst window. It is the cheap cousin of the Phoenix attack buff: smaller, shorter, no safety net.

### 2.6 Ironbark Aegis (Legendary)

- **Effect:** A shield worth 50% of max HP for 30 seconds. It cannot be dispelled. While it holds the drinker is not staggered or knocked back.
- **Cooldown:** 6 hours (this item only).
- **Side effect:** Movement speed -10% while the shield is up.
- **Source:** **Heartwood** from the **Elder Aurochs**, a unique spawn that appears roughly once a day in the forest and is a tougher version of the Barkhide Aurochs (placeholder). Alchemy Tier 6. Recipe: 1 Heartwood, 2 aurochs sap, 2 Wispglass, 1 Glacial Marrow.
- **Value:** 1,100,000 shillings (110,000 coins, 440,000 yen).
- **Buyers:** Raid and Node War tanks, objective holders, any guild defending a flag. It is the second-most-wanted item after the Phoenix Elixir, and it is the one a guild can afford to stock for a whole front line.

### Shared notes

- **Raid mirror.** The raid's three beast buffs (defense, cleansing, attack) are the event versions of Barkhide, Clearspring and Redmaw. Outside the event, the same beasts spawn as ordinary farmable targets, and their material makes the elixirs above.
- **Materials list.** New materials in this file: Ember Heart (Legendary), Cinder Plume (Rare), Cinder Down (Rare), Wispglass (Rare), Wispmoss, Frostroot, Ashbloom, Hartwater, Aurochs sap, Heartwood, Redmaw marrow. They are not yet in `codex/materials/`. Material grades (Rough, Standard, Refined, Pristine) apply as usual and are separate from rarity.
- **Elixir limit (proposal).** Only one Rare-or-higher timed elixir is active at a time. Instant elixirs are exempt.

---

## 3. The king, the court and Crownfall

### What existing canon says

- **King Aldemar Vaereth** is about 97, kept alive by elixirs that are failing (`codex/lore/lunarest-royal-court.md`).
- **Corvith** makes the king's elixirs from material he brought out of Azure, and that material is running low (same file). The ledger notes the contradiction with the later "forest drops the elixir" direction as unreconciled (`outline/canon-ledger.md`, the king's illness entry).
- The king has used elixirs for decades to hold something off (a sickness or a curse). They do not cure it, and enough use may kill him, though not other users (ledger).
- The king's own expeditions into the forest failed for lack of anyone strong enough (ledger). He holds the fort but could never hold the forest.
- After Thornwatch, London Spire holds the fort and one land. The entrance to the elixir's materials is the dungeon behind Thornwatch. Every prince must negotiate with London Spire, Ilyan included. He dies at Crownfall regardless (ledger).

### What this file adds (proposal)

**Why he needs the Phoenix Elixir.** For about **ten or eleven years of story time**, the king has been fighting age, not only the sickness. The sickness has been held off for decades by lesser elixirs of the kinds above (Aegis-grade shielding and mana and cleansing draughts). Around age 86 the age problem began killing him outright, and the court moved to the Phoenix Elixir. He has died and been brought back repeatedly since then. The exact count stays off the page (placeholder: nine).

**How the court brings him back (court dose).** Players use the Phoenix Elixir as a 10-minute combat buff. For an aged NPC like the king, Corvith cuts one bottle into a slower **court dose** that arms Rebirth for 12 hours and carries no attack buff. When the king's heart stops during those 12 hours, Rebirth fires like it does for a player: he is held at 5 HP. The court's need is then about two bottles a day to keep him continuously covered, a supply no one can meet, which is the supply crisis the court story already describes.

**Why he cannot regain full strength.** The 24-hour rule for players does not apply to him, because the court re-doses constantly. What limits him is age. Each Rebirth lowers his **vigor ceiling**, the most HP he can recover to, by a few points, and his HP regeneration slows. For a young player Rebirth is a clean reset. For him it is a smaller man each time. Internal bookkeeping only, never stated on the page.

**Why he can no longer use it effectively.** By Crownfall his ceiling is so low that even a full recovery is almost nothing, and he regains almost no regeneration afterward. A dose arms, he dies, he is held at 5 HP, and he drops again within minutes. He cannot use the 30-second Veil to get away because he cannot walk. The potion still triggers, but it no longer gets him anywhere. This is also why the "elixirs fail" line in the court file stays true: the doses still work, but they no longer help him.

**How this squares with the Azure material (proposal).** Corvith's Azure stock is **Wispglass**, the one ingredient above that is hard to get. Azure is the elves' continent, wisps are drawn to elves and high-mana users, and rumor puts Corvith's origin in the high-magic forest (`codex/locations/eryndal-world-overview.md`). So the king's elixir always needed both halves: a Thornwatch base (the Ember Heart) and Azure Wispglass to bind it. The court had both for years: old Thornwatch stock from before the forest closed to the king's expeditions, and Corvith's Azure supply. Both are now nearly gone. That keeps the court file's claim (Azure material running low) and the ledger's claim (the forest is the source) both true.

**Why Crownfall is a big deal.** The king's Rebirth is what has kept the crown from changing hands for about ten years. When it stops working, the realm loses the only thing keeping him in place, and the ledger's civil war starts. The Crownfall raid is the one event that gathers the Thornwatch forest's materials at scale, and the court watches who controls them.

**Leverage on the princes (proposal for the story):**
- **Ilyan** runs the king's army under Corvith and needs the supply for his father. He has to bargain with London Spire.
- **Dorrin**, the outcast the king doubts is his son, backs London Spire's guild and sits next to the supply. That is an irony the court file already supports.
- **Maldren** wants a new order. A supply that stays out of the court's hands suits him, so he has a motive to see the forest locked or contested.
- **London Spire** is big on raids and PvP and asks what is in it for them, per the ledger. They can sell, hold back, or tie the price to land.

**After the king.** Once he is dead and the funeral truce ends, the elixir stops being a medicine and becomes a weapon: the princes' guilds buy it for their own front lines. Demand does not drop with his death. It rises.

---

## 4. How a goblin trapper-bomber uses and sells them

Tatsuya is a trap and bomb player, a goblin with a low HP base (`codex/lore/hp-sp-mp-resource-pools.md`: 50 HP plus 3 per level) and a build that wins through setup (`codex/subplots/tatsuya-trap-bomber-brigand-archetype.md`). Phoenix-line items suit him in specific ways.

### Using them

- **The Veil as a setup window.** In the 30 seconds he cannot deal damage, but he can place traps, bombs and snares, and under the proposed rule they stay inactive until the Veil ends and then arm normally. A bomber who retreats and re-lays a trap field in 30 seconds comes back with the ground already his. That fits his "setup over raw output" style and the control, stack, ignite, finish loop.
- **Quiet exit.** Cannot be heard is natural for a goblin who works from cover. It is the one part of the Veil that suits him exactly.
- **Low HP makes it a real lifeline.** At 5 HP minimum, even a single stray tick hurts after the Veil. Rebirth alone does not save him. It buys the 30 seconds to get out or be healed.
- **Clearspring Elixir.** His own Goblin Gas stacks Nauseous (fumble chance, lower stamina regeneration, `codex/crafting/debuffs-and-resistances.md`). A bottle clears it and gives 120 seconds of immunity. This is the cheapest useful Thornwatch item for him.
- **Redmaw Elixir before a burst window.** A bomber's damage is multiplied by stacked debuffs. A 25% boost to a combo that already ends fights is worth its cost.

### Farming

- Adult Cinderwings are fire immune. His fire-based Goblin Gas plus Goblin Flare combo does almost nothing to them. He needs poison stacks, Chain Root and frost (a bomb made with Glacial Marrow). That is a good fight-design hook, not only a limit.
- A solo goblin cannot kill an adult Cinderwing. He needs a party or his own guild. Troops count in the guild's side (`codex/lore/companion-troop-system.md`).
- The ash groves lie behind the fort, so he needs London Spire's permission, a way past them, or a slip through a narrow route. A stealthy goblin crew can reach a grove when guilds cannot. That is also a reason for his guild to have a relationship with the fort's holders.

### Crafting

- **Luck helps him.** Goblins get a real edge from Fortune and the Lucky Craft proc (`codex/crafting/crafting-stations-and-process.md`).
- **Tier gap.** Alchemy Tier 7 is a big investment. A character can run only two professions and each point spent on crafting is not spent on combat (`codex/crafting/overview.md`). He either reaches Tier 7 late, or hires a Tier 7 alchemist, or sells Hearts and Wispglass raw and lets someone else craft. The third option is the realistic first step.
- **Failure cost.** An Ember Heart is about 1,000,000 shillings. A failed craft destroys it. That is a real, felt risk, not a vending machine.

### Selling

- **The board is a trap.** The auction tax eats most of the margin on a 3,000,000 shilling item. He avoids the board for Rare and above. This is consistent with Tatsuya noticing the tax in Chapter 3.
- **Private contracts through the goblin trade group.** Under the black-market trade group the author describes (`codex/subplots/tabuchi-takedown-and-kazuhaya-brand.md`, `codex/subplots/goblin-trade-company-forward-plot.md`), rare gear and elixirs move through goblin runners under the guild's goblin name. Arya's trading idea and Jiro Amano's auction connections are the existing bridges (`codex/subplots/aryas-loop-discovery-and-reputation.md`).
- **The court as a buyer is a way in.** A standing order from Ilyan's quartermaster at 5,000,000 shillings is the highest price on the map, and it is also access to nobles, which a guild does not get just by being a guild (`codex/lore/lunarest-royal-court.md`). But goblins carry bad infamy in Lunarest and the court's story makes them the state's enemy, so he cannot walk in. He sells through a human or elven front with a merchant license (Book Two).
- **PK_Wraith's blacklist.** His informal blacklist freezes Nykri out of normal channels (`codex/subplots/goblin-trade-company-forward-plot.md`). The goblin trade group is the workaround.
- **Carrying risk.** In open-world red zones death drops one item at a chance skewed toward better items (`codex/lore/deck-building-rarity-and-classes.md`). A Legendary elixir worth 1,200,000 yen is the most likely thing to drop. Holding bottles in a guild vault and moving them in a single quick run is safer than carrying stock.
- **Kazuhaya brand angle.** A bottle sold under the Kazuhaya Tech name would tie the brand to a top-guild item, which fits the plan of selling by being seen using it.

---

## Open and conflicts

Conflicts are listed where the author's direction and an existing file disagree. In each case this file follows the author.

### Conflicts with existing files

1. **Corvith as the maker versus the forest as the source.** `codex/lore/lunarest-royal-court.md` says Corvith makes the king's elixirs from material he brought out of Azure, and that material is running low. The author and the ledger say the forest drops the elixirs and the king needs them. The ledger itself marks this unreconciled. This file reconciles it with Wispglass as the Azure half (section 3). The court file still reads as written, so a later sweep should add a line pointing here.
2. **"Decades" versus "ten or eleven years".** The ledger says the king has used elixirs for decades. The author now says he has been fighting age for ten or eleven years. This file splits them: lesser elixirs for decades against the sickness, the Phoenix Elixir only for the last ten or eleven years.
3. **"May kill him after enough use, though not other users" (ledger) versus "he cannot regain full strength because he is old" (author).** This file keeps both. The sickness is held off by the old elixirs. The age problem is what shrinks his vigor ceiling.
4. **Rarity names.** `codex/materials/organic.md` and `codex/materials/magical-and-spirit-tied.md` use "Epic" as a rarity word, which is not on the ladder in `codex/lore/deck-building-rarity-and-classes.md`. This file uses only Common, Uncommon, Rare, Legendary and World. The Epic uses are left alone.
5. **Crafting failure rule.** `codex/crafting/overview.md` says a failed craft consumes the materials. `codex/crafting/crafting-stations-and-process.md` says failure returns a portion or a degraded item. This file uses the stations-file version (about half of non-key ingredients returned, the Ember Heart lost).
6. **The 72-hour death lock.** Rebirth bypasses the death lock and the death-drop roll (`codex/lore/preserved-misc-mechanics.md`). That is the author's stated purpose ("get out"), but it affects every war and raid. Details in Open question 3 below.
7. **Crownfall's forest.** Existing files describe Crownfall as a 7-man raid with a late-entry poison clock and an event version of the forest. This file assumes Phoenix Elixirs work inside the raid unless the author says otherwise. Clearspring does not cure the entry poison.
8. **Where the materials are.** The ledger puts the entrance to the elixir's materials in a dungeon behind Thornwatch, and also says players already know the forest drops elixirs as a rare drop. This file makes both true: finished Rare elixirs and the Phoenix at 0.2% drop in the open forest, and the Ember Heart comes from the ash groves behind the fort.
9. **Existing file inconsistency not touched.** `codex/lore/hearthfire-expansion-and-seasons.md` still describes Thornwatch as a fortress city in places despite the direction banner. Not edited here.

### Author's wishes that I had to interpret

- **"Revive with 5": RESOLVED by the author, a flat 5 HP.** The percent and hybrid readings above are dropped.
- **"For players, 24 hours."** Read as a revive cooldown on the player (the Ashen Mark), not the item. The king is exempt because he is an NPC and the court doses him continuously. Decision needed: is the 24 hours real time or in-game time (`codex/lore/preserved-misc-mechanics.md` notes time moves faster in HGO)? This file uses the real clock, same as the death lock and pass-out lock.
- **"Invisibility cloak" and "can be seen".** These two phrases conflict. This file follows the explicit rule (visible) and gives the effect an invisibility-like function by clearing aggro and blocking sound. The item name uses "Ember Veil" so the page does not call it an invisibility cloak. Decision needed: should the drinker be visible or hidden?
- **"Cannot be heard".** Read as in-world sound only. Party voice chat and the party channel still work. Not in the author's words.
- **"All status effects are removed."** Read as all harmful status effects, with beneficial buffs kept, and zone rules, karma markers and quest timers excluded. Not in the author's words.
- **"Brought back every time he died."** The mechanism (a 12-hour court dose) is a proposal. The author did not say how the court revives him.

### Placeholders and flags

- **All names:** Cinderwing, Clearwater Hart, Barkhide Aurochs, Redmaw Direwolf, Elder Aurochs, Wispglass, Wispmoss, Ashbloom, Ember Veil, Ashen Mark, Cinder Crash, Ironbark Aegis, Wispdew Tonic, Hoarfrost Ward, Clearspring Elixir, Barkhide Elixir, Redmaw Elixir, court dose, vigor ceiling.
- **All numbers:** percentages, durations, drop rates, respawn times, creature classes, ingredient quantities, crafting success rates, the king's revive count (nine).
- **Price and pacing.** The median Phoenix price (1,200,000 yen) is about 30% of the surgery cost. It was set so one bottle is meaningful but not enough, and it is held up by a supply of about 2 to 3 per week. If the author wants the surgery to need more than a handful of sales, raise the price or cut the supply. If the author wants Tatsuya to afford the surgery from a single run, cut the price.
- **Creature levels.** No level bands are set for the forest or its beasts. Leveling lists level 150 as the first major milestone and the beta characters are far below it.
- **Recipe discovery.** The king's expedition notes in the ruined fort armory are optional.
- **Elixir limit** (only one Rare-or-higher timed elixir at a time) is a proposal for the whole line.
- **Not decided:** auction tax figures, merchant license rules, whether the royal court can legally buy from a goblin (Book Two).
- **Not edited:** chapters, `codex/crafting/food-and-consumables.md` (which still lists only the Minor Elixir), `codex/materials/`, and the court file. A later sweep could add this file to their cross-references.

## Cross-references

- `codex/crafting/food-and-consumables.md`, `codex/crafting/professions.md`, `codex/crafting/crafting-stations-and-process.md`, `codex/crafting/overview.md`, `codex/crafting/debuffs-and-resistances.md`
- `codex/lore/lunarest-royal-court.md`, `codex/locations/eryndal-world-overview.md`, `codex/lore/hearthfire-expansion-and-seasons.md`
- `codex/pro-scene/crownfall-siege-event.md`
- `codex/lore/preserved-misc-mechanics.md` (death lock), `codex/lore/hp-sp-mp-resource-pools.md`
- `codex/subplots/tabuchi-takedown-and-kazuhaya-brand.md`, `codex/subplots/goblin-trade-company-forward-plot.md`, `codex/subplots/tatsuya-trap-bomber-brigand-archetype.md`
- `outline/canon-ledger.md` (the king's illness, Thornwatch fort and forest, Crownfall entries)


## Author decisions applied after this document was written (latest)

- **Revive amount: a flat 5 HP.** Every earlier mention of 5 percent or a 5 HP floor now reads as a flat 5 HP.
- **Still open for the author** (the agent's questions, not yet decided): whether the 24-hour limit is real time or in-game time; whether the revive skips the 72-hour death lock and the death-drop roll, and whether it works inside the Crownfall raid; "invisibility cloak" versus "can be seen" (the agent made the drinker visible and clears aggro, named Ember Veil); whether "cannot be heard" covers party chat; the court-dose mechanism and a placeholder revive count kept off the page; the price pacing (a typical bottle is about 30 percent of the 10,000,000-shilling surgery cost); the invented names and numbers; where the Cinderwing lives and who controls access; where the Phoenix recipe is found; and whether only one timed elixir may be active at a time.
