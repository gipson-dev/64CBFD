# Common particle update private recovery

Date: 2026-11-14. The complete retail `func_15175958` has been read and a
typed semantic C candidate is retained in
`tools/experiments/game_particle_common_15175958_candidates.py`.
**This candidate is private, uninstalled and uncredited.** Production remains
**4,493 / 5,515 exact C functions (81.47%)**, with **195 more** needed for 85%.
The owner remains **8 / 9 exact**; its production common-updater stub is intact.

Target: **961 words / 3,844 bytes**, VA **0x15175958..0x1517685C**, ROM
**0x1A2E08..0x1A3D0C**, frame **0xC8**. Original saved homes are S0 at
SP+0x30 and RA at SP+0x34. The recovered interface is one particle pointer,
returning void. The alternative source's `void(f32,f32)` signature and many
word-sized field accesses contradict retail and were not imported.

Baseline consumer `60b5647e`, mounted tools
`76987f788cb3c07b715613a9ca599d21ac7b7698`. The preceding callback adoption
is `c7c29d87`; the follow-up documentation commit preserves all old UTF-8
index bytes, leaving only the intended new entry relative to its parent.
Ignored artifacts: `conker/build/game-particle-common-15175958-screen/`.

## Recovered contract

The opening model/control gate frees disabled variants. Alpha is snapshotted
before the special variant 8/9 path, which can clear flags and transition to
radial motion under the original scene/mode/timer conditions. The inner scene
checks remain after the flag write; they cannot simply be removed as repeated
tests when record/global aliases are possible. Fade-in and fade-out preserve
32-bit wrapping step arithmetic and the original signed clamps.

The active marker is written before loading the 56-byte configuration row and
optional sound handle. Sound validation either submits the ten-word position
update packet or clears the handle. Steering flag 4 uses signed distance and
optional inner-radius reversal, computes a heading through the real X/Z vector
interface, then runs the turn/idle state machine and turn-rate clamp.

Flag 0x80 refreshes ground height and maps the returned surface pointer into
the original attribute table. Flag 0x40 controls a signed halfword timer and
vertical target selection. RNG uses an unsigned remainder with the late signed
halfword divisor transported to unsigned 32 bits; source spells out the signed
float32 conversion followed by the 2^32 correction for high-bit remainders.
The zero-divisor hardware boundary has not yet been qualified for this target.

The ordinary motion path integrates and clamps tilt, wraps heading, changes
bank, and updates/clamps the signed halfword at A4 using A6. In this routine
A4/A6 act as speed/acceleration; their shared view currently retains the earlier
`lifetime`/`mode` names. Any final rename must preserve all neighbors. Model
switching depends on tilt sign and the configuration wave threshold. Flag
0x200 instead advances radial position and descent with the original live
trig-provider reads and scene-dependent retirement.

Record type 19 can emit a randomized sound and write a fresh slot cooldown.
Flag 2 performs one or two visibility queries, retiring the particle according
to the original short-circuit outcomes. The ten-word packets and full record
snapshots are compared at all modeled helper entries.

Three direct JAL sites are **0x15176AF8**, **0x15176B58**, **0x15176DD4**,
ROM **0x1A3FA8**, **0x1A4008**, **0x1A4284**. Four registry entries point to
the common updater:

| Descriptor | Pointer ROM | Pointer VA |
| --- | --- | --- |
| 10 | 0x230170 | 0x8008B6B0 |
| 20 | 0x230378 | 0x8008B8B8 |
| 68 | 0x230D38 | 0x8008C278 |
| 69 | 0x230D6C | 0x8008C2AC |

These are static discoveries. Connected execution of these callers/registry
entries belongs to the remaining qualification; this screen does not claim it.

## Measured private result

The first scalar/struct draft emitted **944 words**, frame **0xC0**. Array
forms retain more of the original aggregate work. A bounded **16-shape**
screen compares offset/sine/vector aggregate forms and two equivalent opening
model views. It produces four distinct raw streams at 952, 953, 955 and 956
words, all with frame 0xC0. The retained **956-word** form uses the two-float
offset array, two three-float direction/angle arrays and separate trig results.
No frame padding, new guards, inserted instructions or omitted instructions
are installed to hide the remaining mismatch.

Retained raw SHA-256:
`d7f17a9c5f17cfcd6dfe7c439d751aa5523b809bdbee92331d91b87079a8be39`.
It has **124 binding sites** and **894 differing word positions**, counting
the five-word length deficit. A five-word deficit does not mean only five
independent scheduling differences remain. All eight neighboring raw functions
and owner pools are unchanged. The frame, homes, complete instruction stream
and any eventual normalization still require recovery/proof.

The focused suite passes **1,314 differential guest cases** comparing retail
and the emitted C, full public memory, helper packets and all 248 record bytes
at every helper entry. It visits **867 / 961 retail instruction words**.
Cases cover gates, fade directions, signed halfword/wrapping speed updates,
distance/angle boundaries, positive/negative/zero steering and bank, special
variants, finite trig providers, live record/global/flag mutations, and high
unsigned RNG remainders with negative signed divisors. Providers clobber all
caller GPR/FPR roles, outgoing homes, HI/LO and the FP condition boolean.

Five effective emitted controls reject changes to the active marker, fade
direction, speed floor, sound cooldown and unsigned-height correction.
Constants come from their primary `24BC30.rodata.s` words, with the primary
assembly, constant owner and retail input hashes pinned. A preliminary scratch
fixture used the wrong constant-owner mapping; its result is discarded. All
reported passing results use the corrected primary constants.

This is a two-stream differential screen, not an independent full semantic
model, portable native validation, all-input equivalence or instruction-fault
proof. Guest aliases, nonfinite inputs, zero-divisor prefixes, full FCSR,
native32 O0/O2/O3, connected callers, padders/rebases and actual Make/image
qualification remain open. The larger helpers are bounded models. Hardware
and host gameplay are not validated. Routine Claude calls: zero.

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_common_15175958_recovery -v
```

Mounted and isolated sibling-overlay suites pass. The overlay uses three
byte-identical task files with sibling dependencies and mounted fallback,
preserving sibling HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all
**2,439 dirty paths**, and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.
Shared compiler/parser code is unchanged; the preceding Note 2450 shared
`make tools-check` receipt is reused, not claimed as a new run here.

All **807 frozen production inputs**, including **82 headers / 698 objects**,
remain unchanged. No source, guard CSV, conversion row, production object or
ELF is installed by this experiment. ELF SHA-256 remains
`73b2aa1dbe44da28872317ece93d57e1b1a1f3a4f321f8d1af67513e8b31fbf6`.
The preceding exact progress recount remains applicable to that identical ELF.

Scoped Graphify AST refresh covers the three new tools files, retaining all
**60,980 old IDs**, zero lost nodes: **60,999 nodes / 114,674 links**. This is
not full-corpus re-extraction. Tools commit `1521cf4245a97ef1c0dc787049d177abb8f42bc7` precedes
the consumer pin/documentation commit. No push; host Release remains frozen.

## Resume steps

1. Recover the original **0xC8 frame** and the model/config/offset lifetimes,
   including SP+0x6C models, SP+0x70 configuration and SP+0x60/0x64 offsets.
   Keep the aggregate dead-store differences separate from useful operations.
2. Close the remaining CFG/operation differences with complete raw/retail
   inventories. Do not treat equal length or a finite behavior pass as permission
   for a broad instruction replacement table.
3. Extend the independent model, aliases, nonfinite and zero-divisor boundaries;
   qualify native32 and the real three-call/four-registry caller interfaces.
4. Only after source/ABI/normalization gates pass, run both padders and rebases,
   strict independent whole-image prediction, actual Make, production audit and
   fresh recount. Install and credit only after every required gate passes.
