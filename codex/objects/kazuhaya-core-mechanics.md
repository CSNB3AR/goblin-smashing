# The Kazuhaya Tech Core: Mechanics, Aging and the Rebuild Plan

**Type:** Object/tech, real-world. Technical reference for the processor core inside the Kazehaya pods (Daichi's line, the old upright full-body pods). Codex only: it gives the author and any agent one consistent set of numbers and terms so the page can stay light.

**Status:** Mixed. Facts the author has stated are tagged **(canon)**. Everything I added to make it work as engineering is tagged **(proposal)** and can be changed freely. Chapter references are to `chapters/chapter-03-new.md` and `chapters/chapter-06-new.md`.

**Naming used here.** The Kazehaya pod (Daichi's line, from Kazuhaya Tech), the Kuroshio capsule (the Tabuchi-backed line, working name) and the Nexus helmet (Kazuku's line). No numbered-generation labels appear below.

**Working name for the core (proposal).** The author's spoken name ("Hidan") is unclear and is not adopted. On the page it stays "the core" or "the Kazehaya core", as Chapters Three and Six already have it. In the codex, a plain name: the **Haya core** (matching the Haya EB and Haya Sedan naming), with Daichi's original called the **Mk 1** and Tatsuya's rebuild the **Mk 2**. See "Open and conflicts" for the garble.

---

## 1. What the core is

Chapter Three gives the plain-language version and it stays the on-page version: "basically a GPU the size of a brick." The mechanic's version is that the core is the whole heart of the pod in one removable module. It does four jobs. If any one of them fails, the pod fails, and the way it fails tells you which one.

| Job | What it does | What Tatsuya can read or smell when it goes wrong |
|---|---|---|
| **Power** | Takes the pod's supply and turns it into clean, steady power for everything else. Holds a small energy reservoir (a bank of cells) that soaks up spikes and keeps the pod alive for a moment if the wall supply hiccups. | Voltage sag under load, rising internal resistance, the pod resetting when the lights flicker. |
| **Compute** | The big parallel processor that builds the world and runs the physics, the sensation model and the damage model. This is the "GPU" part. | Frame stalls, texture pop, rubber-banding, thermal throttling. |
| **Sync** | Drives the nerve interface: reads the diver's motor signals going out, writes sensation coming in, and keeps the two locked to the same clock. The diver's body is paralysed in the shell while this runs, so timing errors are not just lag, they are wrong feeling. | Ghost inputs, a delayed or doubled sensation, a hard drop-out (the "floor yanked out" feeling in Chapter Three). |
| **Thermal** | Moves the heat out: heat spreader, vapor chamber or heat pipes, a fan, thermistors, a thermal fuse. Also runs the temperature protection that throttles or cuts power. | Core temperature that never flattens, a fan dragging with a whine, the scorched-plastic smell, heat rolling off the shell. |

**The aux rail (canon in spirit, specifics proposal).** Daichi never built anything without a 12-volt system (the Haya EB and the Sedan both have one; see `codex/objects/haya-eb.md` and `codex/characters/daichi-kazehaya.md`). The core follows the same rule. A separate 12-volt auxiliary rail, independent of the main bus, runs the supervisor controller, the temperature sensors, the safety lines and, in the Mk 2, the fan. Marked **jump terminals** on the module let a mechanic with a jump pack wake the supervisor and the fan even when the main side is dead. That is how the old core can still be read and logged on the laptop when everything else has given up, and it is the same trick as the EB: you cannot jump the traction side, you can jump the aux.

**Main bus (proposal).** A nominal 48-volt DC bus feeds the compute side from the pod's own supply. This is a placeholder for flavor; the page needs only "the 12-volt aux rail" and, if anything, "the main bus."

**Form factor (canon).** Roughly brick-sized (Chapter Three). A swappable module in a bay in the pod's base, with heavy cable bundles up the side, which matches the arcade picture.

---

## 2. What the percentage measures, and why it only goes one way

**The distinction that makes the rest work (proposal, built on canon).** There are two different numbers, and Tatsuya's habits from the EB already separate them.

- **Charge** is how full the reservoir is right now. It goes up and down. He "has to charge it from the wall for a while first, or he drains the core" (canon): that is topping the reservoir before a bypass run so the core's cells are not the only thing feeding the load.
- **The percentage on the laptop** is health: how much of the as-built capability the core has left. It is the core's own supervisor comparing what it measures today (usable capacity, internal resistance, how fast it heats) against the values stored when it was built. 100 is as built. 0 is the point where the cells will no longer accept a charge. It only goes down. This is the number that reads 20 in Chapter Three and 19 in Chapter Six.

Car comparison for the page: charge is the fuel gauge, health is the cold-cranking rating. You can fill a tired battery to the brim and it still will not turn the engine over on a cold morning.

**Why a dead core cannot be recharged (canon, explained).** At zero, the cells have worn past the point where they accept charge: internal resistance so high that the charger's voltage just becomes heat, or internal shorts. Charging a dead core is pushing current into a wall. This is the second pod's situation (canon): its core is already gone, so the shell is dead no matter how long it sits on a wall plug.

**Why it was already at 20 (proposal).** The arcade pod spent its life on retro titles that never asked much of it, and then sat for stretches. Age and years in the cells did most of it. 20 means it was already near the end before Tatsuya touched it; what he did was ask it for a load it was never rated for.

### Why a hotwired HGO session burns about a point

Canon: 20 at first login, 19 after one session, roughly one point per hotwired login, about 20 logins left. On the page this is Tatsuya's speculation from two readings ("if I'm going off that"), so the codex keeps it as an estimate. Four things stack up to produce it (proposal):

1. **Heat is current squared times resistance.** A worn core has high internal resistance. HGO draws far more current than a retro title, and the waste heat rises with the square of the current. Double the current and the wasted heat is four times as much. The cells cook themselves from the inside.
2. **The hotwire bypasses the soft start.** Tatsuya bridged the feed to the wall (canon, Chapter Three), so the core's own controlled start-up and charge balancing are skipped. Every login hits the worn reservoir with the full inrush and every load spike, with nothing smoothing it.
3. **Heat accelerates wear.** Rule of thumb, borrowed from ordinary electronics: every ten degrees hotter roughly doubles how fast cells and solder joints age. A core that "never flattens" in temperature is aging faster the whole time it is in use.
4. **Each login is a thermal cycle.** Cold to hot to cold stresses solder joints, the thermal interface and the cells. Part of the point per login is just the cycle, regardless of length.

So the cost per login has a fixed part (inrush plus the thermal cycle) and a part that grows with how long and how hot the session runs. One long session therefore probably costs more than a short one, and the cost per login probably rises as health falls. "About twenty logins, maybe fewer" (Chapter Six) is the honest wording and this explains the "maybe fewer."

**Why the fan whines (canon, explained).** On the Mk 1 the fan is on the main side, so when the supply sags it slows down exactly when the core needs it most: the dying whine in the Chapter Three blackout. The Mk 2 puts the fan on the aux rail so cooling survives a main-side fault.

**Why the blackout was the core and the building (canon, reconciled).** Chapter Three has the core overheat and the shop's lights go out (an old building, Leon takes it for a plain power cut and hot-fixes the supply). Mechanically: the worn core pulled a heavy, spiky draw through old wiring, heat built, the supervisor cut the main side, and the building's weak supply dipped at the same moment. The two overlapping fixes in canon (Leon at the breaker, Tatsuya's hardwire) both hold.

---

## 3. HGO's load versus the retro games the pod was built for

The Kazehaya pod was designed (by Daichi, canon) for the early VR titles of its day. HGO is a different kind of customer.

| | Retro title the pod was built for | HGO |
|---|---|---|
| Average draw, share of rated (proposal) | about 20 to 30 percent | about 70 to 90 percent |
| Peak draw (proposal) | about 50 percent, brief | 100 percent and above in fights, for seconds at a time |
| Shape of the load | Low and steady | Bursty: quiet in town, huge in a siege or a crowded zone |
| Sensation model | Coarse. Light touch and sound, little real feeling | Full sensation and real damage feedback, magnified but capped (canon, see `codex/objects/pod-hardware.md`) |
| Sync bandwidth | Low and forgiving | Full rate. Every limb, every sensation, every frame |
| Network | Local or none | Constant online multiplayer, so the pod also runs the netcode and, with an operator, the monitor feed (see `codex/lore/external-monitor-and-full-dive-safety.md`) |
| Session length | Short, arcade length | Long. People live in it for hours |
| Extra strain | None | Streaming on top (canon: streaming adds real strain) |

The comparison for the page: a retro game is idling at a stoplight, HGO is towing a trailer uphill with the air conditioning on. The engine was never rated for it, and the heat shows the difference.

**Second consequence.** A core that can carry HGO has to be designed around the peaks and the hours, not the average. That is why Tatsuya says (Chapter Seven, canon) he cannot just recreate Dad's core: it was made for the old games, so he has to tailor one to last under HGO. It is also why a stopgap built for a different pod fails (section 6).

---

## 4. The drive slot and the wiring (related, not the core)

Canon: the slot built for HGO drives is missing and the drive is forced into an old slot that does not fit; some wiring is needed and is cheap. These are separate from the core but the Mk 2 plan can absorb them: a proper **drive-bay board** with the right connector so the drive seats cleanly, and a new harness. Cheap, a weekend job, and it removes the "override the slot" hack. The hotwire around the slot stays as the emergency method until then. The core itself is the long job.

---

## 5. The build plan, in stages

All class and lab names below are **proposals**: invented to be plausible, rename freely. Re-entry is as a full first-year (canon, `codex/subplots/tochi-academy-return.md`), so the early stages are first-year work. Labs are gated by grades, standing and instructor access (canon), and instructors, not students, hold the real access to the best equipment. The Nexus Enterprises sponsorship Tochi announced about a year ago is a lead only; this plan never assumes the school holds a Nexus core and never uses one (canon, `codex/objects/pod-hardware.md`).

### Stage 0: Measure and autopsy (now, before Tochi)

**Goal:** know the old core better than anyone, and make the percentage a curve instead of a single number.

**What he learns:** how to log. He already does it for the EB. Add a shunt (a current-sense resistor), a pair of thermocouples and a data logger to the laptop he already carries.

**Where:** the arcade, evenings, and his room (Dad's corner, the soldering smell, canon). No Tochi needed.

**Work:**
- Log every session on the live pod: draw, core temperature, percentage. The result is a **load profile**: the real shape of HGO on the pod, to be replayed later on the bench.
- Open the **dead second pod's core** (nothing to lose) and take it apart. Measure what failed. This is the best classroom he has and it is free. (Canon: Chapter Six has him counting on "two pods here to work from.")
- Re-read Daichi's manual against the module: the aux rail, the jump terminals, the core's own notes.

**Parts:** logger, shunt, thermocouples, a dummy-load resistor bank and a bench supply or jump pack (he has the pack). Roughly 30,000 to 60,000 yen (proposal), which fits a Chapter Three wallet that is 47,320 yen.

**Test procedure:** none yet beyond the logging itself, plus one **pulse test** on the dead core's cells to get a baseline internal resistance for "dead."

**Failure mode:** he spends the live core's remaining logins on experiments. Rule: logging is passive, no extra sessions for testing. The countdown (canon, about twenty logins) is not a resource to spend.

### Stage 1: Foundations (first term at Tochi)

**What he learns:** circuits and rails, regulation, energy storage and measurement habit. The theory behind what his hands already know from the EB: why a cell sags, what internal resistance is, how a regulator holds a rail steady.

**Tochi classes (proposals):**
- *Foundations of Electrical Systems* (open to first-years)
- *Instrumentation and Test Practice* (open, supervised bench)
- *Materials and Heat Basics* (open)
- *Applied Mathematics for Engineers* (open; the dull one that pays off later)

**Labs:** the **Instrumentation Bench Room**, open to first-years under supervision. Good grades here are the first rung of the gate.

**Work:** rebuild the aux-rail supervisor on the bench (the simplest piece and the one Daichi's manual already describes). Build a bench **dummy load** that can replay the Stage 0 load profile.

**Parts:** supervisor board, sense amplifiers, a few cells for practice, connectors. Roughly 20,000 to 40,000 yen (proposal) on top of Stage 0.

**Test procedure:** first **bench load test**: step the dummy load through 25, 50, 75 and 100 percent and log the voltage sag at each step. This is the procedure he already knows from the EB, grown up.

**Failure modes:** a bench short (small, loud, teaches respect); standing slipping because the exams or the grades suffer while he is also diving and working. This stage is where "labs are gated by grades and standing" bites hardest.

### Stage 2: The power stage and the thermal stack (second term)

**What he learns:** power electronics (switching regulators, filtering, protection), thermal design (conduction, spreading, airflow) and basic firmware for the protection logic.

**Tochi classes (proposals):**
- *Power Electronics and Energy Storage* (needs a pass in Foundations)
- *Thermal Engineering Lab* (grade gate)
- *Embedded Control and Firmware* (open)

**Labs:** the **Power and Thermal Test Lab**, grade gated. This is the first lab with the thermal chamber and the heavy-current load bank he cannot build himself.

**Work:** design and build the **Mk 2 power stage**: matched reservoir cells, a balance board, the regulator, the fuse chain, and the aux-powered fan with a tachometer. Build the thermal stack as a stand-alone assembly and test it with a heater block as a fake compute die.

**Parts:** high-discharge cells (matched), balance board, power switches and inductors, a regulator controller, sense shunts, thermal fuses, copper spreader and vapor chamber, fan with a tach signal, thermal paste or pads, thermistors, heavy connectors, and the marked jump terminals. Roughly 80,000 to 150,000 yen (proposal) for the first full set.

**Test procedures:**
- **Bench load test** at stepped loads, then the replayed HGO profile.
- **Internal resistance by pulse:** a short current pulse, measure the drop, divide. Compare to the Stage 0 baselines for old and dead.
- **Thermal soak:** hold full load until the temperatures stop climbing, with the ambient set to a hot arcade (proposal: 30 degrees Celsius), and log how long it takes to level off and where. Pass is a flat curve under the thermal limit with margin. The old core's failure was that the curve never flattened.
- **Brownout drop test:** cut the supply mid-load and confirm the supervisor holds up long enough to run a controlled ramp-down. Hold-up time is a design number, a fraction of a second to a couple of seconds (proposal). This is also the item VRSA will care about for the second pod (see `codex/lore/vrsa.md`).

**Failure modes:** thermal runaway in the reservoir cells (the dangerous one; only in the lab, behind the test cage, with an instructor present); regulator ringing that shows up as brownouts; connector heating at the jump terminals.

### Stage 3: Compute and sync (third term onward; the gated stage)

**What he learns:** how to feed a parallel processor, how to build a low-latency link to the nerve interface and how to prove it is safe. This is the part where Tatsuya does the most thinking and the school does the most gatekeeping.

**Tochi classes (proposals):**
- *High-Performance Compute Systems* (needs good standing)
- *Neural Interface Signalling* (restricted; instructor approval)
- *Independent Study in Applied Hardware* (needs an instructor sponsor; this is the course that unlocks the fabrication lab)

**Labs:** the **Fabrication and Prototyping Lab** (standing plus instructor access) for boards, assembly and reflow. The **Interface Lab** for the sync controller (instructor-only equipment, proposal) is the likeliest place a Nexus-sponsored instrument sits, which is exactly why he needs a sponsor and why the paper trail matters (see below).

**Work:** design the **compute module** and the **sync controller**. The compute module can use commodity accelerator hardware from ordinary parts channels (the Akihabara thread in `codex/subplots/technical-arc-leon-and-sakura-arcade.md`), not Kuroshio parts, which keeps the project clean of Tabuchi money. The sync controller is the tricky piece: a small, fast, deterministic controller plus isolation between the core and the diver. Everything routes through the supervisor so any fault drops the link to a safe state.

**Parts:** commodity accelerator or FPGA boards, memory, a microcontroller or FPGA for sync, isolation components, additional heat spreader and cold plate, a custom PCB run, and a shielded enclosure sized to the Kazehaya bay. Roughly 150,000 to 300,000 yen for the first compute and sync set (proposal).

**Test procedures:**
- **Latency test:** measure round-trip time through the sync path with a signal injector in place of the diver. A spec number, set by what the nerve interface needs (proposal: no spike above a small fixed multiple of the average).
- **Soak under replayed HGO load**, with the compute module active.
- **Fault injection:** pull the aux rail, kill the fan, open a thermistor, drop the supply, and confirm each ends in the safe state and not in a ghost input.
- **Tolerance check:** part-to-part variation across a small batch; the core must work with the worst combination of parts, not just the best (see glossary: tolerance).

**Failure modes:** sync dropout (worst: wrong sensation, a flinch that was not the diver's); EMI from the power stage leaking into the interface; firmware watchdog false trips that kick the diver out for no reason; thermal paste pump-out after many cycles.

### Stage 4: Integration, burn-in and the dead pod first

**Plan:** the first Mk 2 goes into the **dead second pod**. That pod has nothing to lose, which makes it the right test bed, and it is the pod Leon wants running for VRSA clearance anyway (canon: Chapter Five, `codex/subplots/technical-arc-leon-and-sakura-arcade.md`). The live pod keeps running on the old core, rationed, until the Mk 2 has proven itself, then gets its own retrofit.

**Work:** install, commission, then **burn-in**: run the core on a bench or in the pod, hot, at full replayed load, for a long fixed time with periodic cycling, to flush out early failures before anyone dives on it. A suggested schedule (proposal): at least 200 hours cumulative with power cycles every few hours. Only then is a human allowed in the shell, with Leon on the monitor (canon: Leon on the booth) and, in practice, the first diver is Tatsuya.

**Tochi class (proposal):** *Systems Verification and Safety* (instructor-run, ties to the VRSA inspection procedure).

**Test procedure for sign-off:** repeat the Stage 2 soak and the Stage 3 fault injection on the installed unit; log the percentage over a week of normal use to confirm it reads steady and does not fall a point a login.

**Failure modes:** infant mortality (the reason for burn-in); a mismatch with the pod's wiring that the bench could not show; a second pod that passes his tests and fails the inspector's.

### The intellectual-property trail (proposal)

The author wants the core never to read as copying Kuroshio or Nexus (canon). Practically: a dated lab notebook, every design choice traced to Daichi's schematics, no Kuroshio parts and no Nexus parts. It matters twice: for Tochi's lab rules, and because Nexus holds patents built on Daichi's work. Tatsuya does not know that on the page (canon, codex only). It also gives Kazuku a clean reason to take Tatsuya seriously later.

### Timeline (proposal)

About 9 to 14 months of calendar time from a Tochi start to a pod running on a Mk 2: one term of foundations, one of power and thermal, a term and a half of compute and sync, then burn-in. Stage 0 starts now. This is far longer than the old core's remaining life. See the stopgap and the open questions.

---

## 6. The stopgap and why it fails

**The stopgap (canon):** buy a Kuroshio capsule core. It is the fast route and the only core Tatsuya can find on the parts marketplace, at 860,000 yen (canon, placeholder price) against a retail price of about 430,000 that he cannot use. He thinks the fix is faster and he refuses it for a second reason too: Tabuchi money is behind Kuroshio and he will not put it in Daichi's machine (canon, never said aloud to Leon).

**Why it fails (author-stated reasoning, plus mechanics):**
- **It was built for a different machine.** A Kuroshio capsule core is made for a lie-down capsule, with different mounting, a different supply, a different sync protocol and an assumption of good cooling and very good internet (canon: needs great cooling or it overheats). In the Kazehaya pod it needs an adapter harness and a firmware shim, and nobody knows what that shim does to the nerve link. (proposal)
- **It carries its own faults** (canon, left vague on the page), which is why people paid extra for the Nexus helmet.
- **HGO is exactly the load it handles worst.** Tatsuya's line to Leon (Chapter Six, canon): "with the traffic you'd get with HGO and VR in the same sentence, a core like that wouldn't last a week, going by what I've tested." Mechanically it drains: cells cooking under sustained load in a pod that does not cool it as the capsule does (proposal).
- **The math (writer logic only, not for the page, canon).** Four cores in a month at 860,000 yen is 3,440,000 yen, more than he can ever recover. "Buying a core is easier, but not if you have to buy four in one month." The ledger records this as background logic, not dialogue.
- **It does not fix the pod, only the symptom.** The wiring, the slot and the bypass habit stay. And he would be paying the Tabuchis' people to keep Daichi's pod alive.

**Other mitigations (proposal, none of which fix it):** pre-charging from the wall before each run; short sessions; an external cooling fan or chilled air at the case; running the live pod only on weekends. These slow the burn without stopping it, and the page should present them as buying days, not saving the pod.

---

## 7. Cost compared with the Kuroshio core

All figures are proposals except the 860,000 and the roughly 430,000 retail, which are canon placeholders.

| Item | Rough cost (yen) |
|---|---|
| Kuroshio capsule core, parts marketplace (canon) | 860,000 each |
| Kuroshio capsule core, retail (canon, unavailable to him) | about 430,000 |
| Stage 0 logging and test gear | 30,000 to 60,000 |
| Stage 1 bench and supervisor parts | 20,000 to 40,000 |
| Stage 2 first full power and thermal set | 80,000 to 150,000 |
| Stage 3 compute and sync set, first spin | 150,000 to 300,000 |
| Scrapped boards and revisions (expect two or three) | 100,000 to 250,000 |
| **Total R&D to a working Mk 2 (mid value about 600,000)** | **about 380,000 to 800,000** |
| **Bill of materials for each further Mk 2 (mid value about 230,000)** | **about 180,000 to 280,000** |

Lab time, instructor help and the fabrication lab are covered by being a Tochi student and are not in the figures.

**The comparison.** For two pods: the Mk 2 route costs roughly 600,000 plus two units at about 230,000, or about 1,060,000 yen at mid values. Two Kuroshio cores cost 1,720,000 and last a week each under HGO. The Mk 2 BOM is about a fifth to a third of a Kuroshio core, and the R&D is a one-time cost that also covers spares. At the Kuroshio rate of four cores a month, the buying route reaches 3,440,000 yen a month, so building wins on the first month.

**Why not simply wait for the money.** The R&D cost is real, and Tatsuya's wallet is 47,320 yen in Chapter Three. That is what the sponsorship is for.

---

## 8. How the core feeds the sponsorship money

Source: `codex/subplots/leon-tatsuya-sponsorship-agreement.md`. The agreement is a neutral 50-50 either side can walk away from (canon). On the page Leon wrote 80-20 in Tatsuya's favor and Tatsuya asked for 50-50 with a renegotiation after six months, because he wants money going into the cores and into getting both pods running (canon, Chapter Eight). Leon's half is split, roughly 25 to the arcade's infrastructure and refurbishing and 25 to the processor cores (canon, ledger and codex only).

**Reading used here and a flag.** The author's brief reads this as "a quarter of Leon's half goes to the cores." The sponsorship file reads as 25 and 25 within Leon's half. Those are not the same. Both are shown, per 100 yen of stream and sponsor income before the split:

| Reading | Cores get per 100 yen | At an illustrative 1,000,000 yen a month |
|---|---|---|
| A: the file's "25 of the 50" (a quarter of the whole) | 25 yen | 250,000 yen a month |
| B: the brief's literal "a quarter of Leon's half" | 12.5 yen | 125,000 yen a month |

No stream income is canon, so the 1,000,000 figure is only for scale. At that figure, reading A funds the mid R&D estimate (600,000) in about two and a half months and reading B in about five, which is what the six-month renegotiation is shaped to catch.

**Other money in the same pot (proposal):** Tatsuya's own half is his to put in as well, and nothing stops him from sending more to the core when a stage needs it. The arcade half is not wasted on cores: infrastructure covers the fused outlet, the dedicated circuit and the cooling the pods need (the building took the hit in the blackout).

**Link to the logo hold-back.** Streaming starts without the arcade tag (canon). The core is why: the arcade has a pod that runs HGO and the core is what keeps it running. Show the logo too early and the crowds arrive before the core can handle them.

**The conflict of interest later (canon).** Once money is flowing Leon asks to bring in Kuroshio pods; Tatsuya refuses and would accept only Nexus pods. This is the same Tabuchi cutoff as the core.

---

## 9. Page voice: technical, not a lecture

The author wants a mechanic who works with an electrician and an engineer. Rules for keeping it from becoming a manual:

- **One term per beat, and the term is the beat.** "Put a load on it" is the action; the number on the screen is the payoff.
- **Explain by the EB or a car, once, in a clause.** He already did it in Chapter Three (the pit stop, the sag, the swapped cell).
- **Prefer a reading to a paragraph.** Give a number, a color or a sound.
- **Let Leon be the non-engineer.** His blank look or an interruption cuts any explanation short.
- **Say the check, not the theory.** "Load test first, then I'll tell you how bad."

Example lines, all in his voice:

- "It's not out of juice. It's out of life. You can fill a worn battery all the way and it still won't crank."
- "Core temp never flattens. A healthy one climbs and settles. This one just keeps going."
- "Aux rail's fine. I can wake the controller. It's the main side that's cooked."
- "Internal resistance is through the roof. Everything it draws turns into heat."
- "I'll jump the aux and pull a log before I touch anything else."
- "Soak it hot for a day and see if the curve flattens. If it doesn't, it's not done."
- "It passes on the bench. The bench doesn't have a goblin in it."

---

## 10. Glossary (what Tatsuya can say, and when)

| Term | Plain meaning | Page use |
|---|---|---|
| **Load test** | Put a known demand on something and watch what its voltage and temperature do. | "Load test says the core's done." |
| **12-volt aux rail** | The small separate supply that keeps the controller, sensors and safety lines alive when the main side is down. | "Aux rail's fine. The main side isn't." |
| **Jump terminals** | The marked points where you inject outside power to wake the aux side. | "Red to red, at the marked terminals." |
| **Internal resistance** | How much a cell fights its own current. High means heat and sag. | "It dropped like a stone under load. Bad internal resistance." |
| **Sag** | The voltage dipping when load arrives. | "The line sagged the second I loaded it." |
| **Thermal soak** | Running hot until the temperature stops climbing, to see where it settles. | "Soak it until the curve flattens." |
| **Burn-in** | Running a new unit hard for a long time before trusting it, to catch early failures. | "Two hundred hours before anyone gets in the shell." |
| **Thermal limit** | The temperature where the supervisor throttles or cuts power. | "It hits the thermal limit and the lights go with it." |
| **Tolerance** | How far a part can differ from its label and still work. A design has to survive the worst case. | "Any one part is fine. Stack the tolerances and it isn't." |
| **Inrush** | The surge when power is first applied. | "The hotwire skips the soft start, so every login eats the inrush." |

---

## Open and conflicts

Where the author's wishes differ from existing files, the author's wish is followed above and the difference is listed here. Nothing in `chapters/` or any existing file was changed.

1. **The core's name.** The author said something that came through as "Hidan." Not adopted. Possibilities, none certain: a garble of a Haya-prefixed name (the Haya EB and Haya Sedan show the pattern), or the word "hidan" (a real Japanese word, roughly "taking a hit"), which would clash with the damage and pass-out vocabulary. Working name here is the Haya core, Mk 1 and Mk 2. Please confirm or give the real name.
2. **Spelling.** The company is Kazuhaya Tech (with a "u"); the pod and the core are "Kazehaya" on the page in Chapters Six and Seven ("Kazehaya cores"), matching the family name. The brief says "Kazuhaya Tech core." This file uses "the core" and "the Kazehaya core" for the page and "Kazuhaya Tech" for the company. Harmonize if the author wants.
3. **The sponsorship quarter.** "A quarter of Leon's half" (brief) versus "25 to the arcade and 25 to the cores" (file and Chapter Eight notes) are different numbers (12.5 versus 25 of every 100). Section 8 shows both. Author to say which.
4. **"The cores are easy to get."** `codex/objects/pod-hardware.md` says the cores are easy to get. Later canon (and Chapter Six) says there are no Kazehaya cores left and Kuroshio cores are the only ones listed. The brief follows the later canon; the earlier line is stale.
5. **The Tochi lab logo.** Chapter Three still says Tatsuya saw the core logo stamped on equipment in Tochi's tech lab. Later canon removed that. Left unchanged; a Chapter Three edit is the author's call (already flagged in the existing files).
6. **A conflict the existing files do not resolve: the clock.** About 20 logins on the old core (canon) cannot last until a self-built core exists. This file's timeline is 9 to 14 months from a Tochi start. Entrance exams are January 4 (`codex/subplots/tochi-academy-return.md`), and Tochi students need permission to leave campus, granted only on weekends (`codex/locations/tochi-academy.md`). Either the page rations his logins (an irony: weekend-only leave stretches twenty logins to maybe ten weekends), or he needs a bridge. The author needs to choose.
7. **"Core building is part of the curriculum" versus gated labs.** The technical-arc file says core building is part of the Tochi curriculum; the author's brief says labs are gated by grades, standing and instructor access. Followed the brief: the early classes are open, the fabrication and interface labs are gated, and he needs an instructor sponsor. The sponsor is unnamed; who would be it (a new instructor, a Daichi-era contact, someone Chiyo knows) is open.
8. **Kuroshio cores as study material.** The technical-arc file says Kuroshio cores can be studied and reworked as parts. Tatsuya will not fund the Tabuchi side. This plan uses no Kuroshio parts and studies the dead core already in the dead pod instead. Flagged in case the author wants him to study one anyway.

### Open questions for the author

- What is the core's real name? (see conflict 1)
- Which sponsorship reading is right, 12.5 or 25 of every 100? (conflict 3)
- How does the page bridge the clock? Options: ration the logins (weekends only); a single reconditioning of the old core's reservoir cells, in the manner of the EB's swap-or-recondition note (this would buy points back, which cuts the countdown stakes, so it is the author's call); a temporary borrowed part; or accept the pod dying and a dramatic gap before the Mk 2.
- Is there a safety floor? A pod might refuse a full dive below some health reading (say five percent), which would make the real number of logins closer to fifteen than twenty. Not used above.
- Does a long session cost more than a point? This file proposes yes (section 2). The page currently says "a point a session."
- Who is the instructor sponsor for the gated labs, and does the Nexus sponsorship of Tochi put Nexus equipment in the Interface Lab?
- How much of the build is shown? A montage of stages with one test per stage, or each stage as a chapter beat? The lecture risk is highest in Stage 3.
- Does the Mk 2 ever get the safety supervisor tied to the external monitor (the operator's booth), or does it replace it for home use like the Nexus helmet's automated shutoff? That decides whether the Mk 2 ever sells.
