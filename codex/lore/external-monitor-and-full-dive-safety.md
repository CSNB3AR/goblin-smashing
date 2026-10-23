# External Monitor & Full-Dive Safety

**Type:** Real-world hardware/regulatory mechanic. Introduced on the page in Chapter 6 at Sakura Arcade.

## Full dive means fully locked in

Full dive is total: mind and body both leave the real world the instant a player logs in. There is no partial awareness, no "feeling" the real body, no ability to self-extract if something goes wrong. As far as the diver is concerned, the real world doesn't exist until they log out or are pulled out. This is the reason the external monitor mechanic below exists at all, a diver physically cannot notice or respond to a real-world emergency happening to them.

## The external monitor / operator's booth

A monitor station positioned at a VR pod, staffed by a live human operator, required by VRSA on any pod running an **online or multiplayer-capable** session on first- or second-gen hardware (see `codex/objects/pod-hardware.md`). The operator watches two things in real time: the diver's vitals on a digital chart (brainwaves and equivalent readouts) and a mirrored feed of what the diver is actually doing in-game. If something goes wrong, medically or otherwise, the operator is the only one who can safely extract them.

**Not required for solo/offline sessions.** This is why Tatsuya's very first session on Leon's first pod (already-committed content, the day before Chapter 6's Sakura Arcade scene) ran with nobody actively watching, Leon assumed it was a solo session, so no operator was legally necessary. The moment a session goes online/multiplayer-capable, an operator becomes mandatory.

**Third-gen home hardware substitutes an automated AI safety shutoff for the human operator requirement.** This is part of why third-gen helmets are so expensive and why Kazuku's built real security/protection into them, an automated system watching in place of a person, safe enough to legally sell for home use without requiring a staffed booth. Any large-scale public/commercial event still requires actual VRSA agents on-site regardless of hardware generation, and VRSA agents themselves operate exclusively on third-gen equipment. A given region has a standing VRSA agent or agency responsible for it, monitoring and inspection is an ongoing presence, not a one-time visit.

## Resolves the pass-out / 72-hour death lock question

`codex/objects/pod-hardware.md` previously flagged an open question: how does the pass-out penalty (a lock-out after taking a fight-ending amount of damage, 24 hours by default) relate to the 72-hour death lock for true in-game character death? Resolved: **they are two distinct tiers.** A pass-out is a forced real-world extraction triggered by the monitor/failsafe system (human operator or third-gen AI shutoff) stepping in before things get worse, a shorter, safety-driven penalty. The 72-hour death lock is a separate, harsher penalty tied to actual in-game character death, not a safety intervention at all. This file is the canonical resolution; `codex/objects/pod-hardware.md`'s open flag should be considered closed.

## Overheating under sustained load, established Chapter 7

Leon's external monitor rig is scrappy, jury-rigged first/second-gen equipment (see `codex/subplots/technical-arc-leon-and-sakura-arcade.md` for the Akihabara parts-sourcing thread). **The pod is what overheats** (author-stated), a first-gen pod running HGO under sustained load (see `codex/objects/pod-hardware.md`), and streaming adds real strain on top of it. The VRSA Inspector is a regulator, not a repair technician, for pods (see `codex/lore/vrsa.md`), so pod repair stays Tatsuya's exclusive domain; the monitor station is the regulated equipment the Inspector does service himself. **The real constraint, established Chapter 7:** he won't actually inspect or work on the setup while Tatsuya's still connected and diving, a pod in use doesn't get opened up mid-dive. So in Chapter 7 he can only swing by, confirm Leon's temporary override on the pod is holding, buys time, isn't a real fix. The actual repair has to wait for a window where the pod's powered down and Tatsuya's fully out, which is exactly what forces the longer, ten-to-fifteen-minute shutdown in Chapter 8. A five-to-ten-minute window is what pulls Leon away from the booth in Chapter 7 itself, the direct trigger for the empty-booth window Arya later uses to start watching Tatsuya's gameplay (see `codex/subplots/aryas-loop-discovery-and-reputation.md`).

## The real fix, Chapter 8-9: parts, urgency, and the Tochi lead

The ten-to-fifteen-minute Chapter 8 shutdown gets the override stabilized, not a permanent repair, the pod is still degrading under the combined monitoring/streaming load. In the following real-world stretch, Tatsuya gets an email lead with real, specific part numbers, the actual components that bridge first-gen pod hardware with something closer to third-gen reliability. He doesn't have the technical knowledge to act on it himself yet, a real, felt gap, not a minor inconvenience, and it's what pushes him to seriously consider Tochi Academy's tech program (see `codex/subplots/tochi-academy-return.md`) as the realistic way to actually learn this, faster and cheaper than a university path he doesn't have the time or money for. Ties this file's overheating thread directly into the open Tochi decision rather than leaving them as two separate pressures.

## Avatar state on disconnect, confirmed Chapter 8

When a diver disconnects mid-session (a real-world break, a forced monitor shutdown, anything short of a clean logout), their avatar doesn't vanish from the world. It goes idle exactly where it was, physically present but unresponsive, until they log back in. Confirmed Chapter 8: Tatsuya's avatar sits down in the war tent's chair while he's offline for the monitor check, and he picks back up from that exact position on return.

## Cross-references
- `codex/lore/vrsa.md` — the regulatory body that mandates this, and the Inspector role that certifies it.
- `codex/objects/pod-hardware.md` — hardware generations, the pass-out mechanic this file resolves.
- `codex/subplots/technical-arc-leon-and-sakura-arcade.md` — Leon acting as the operator for Tatsuya's Chapter 6 session, seeding an early coach/sponsor dynamic.
