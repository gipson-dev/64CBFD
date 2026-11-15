# Common particle frame, native sequencing and caller qualification

Date: 2026-11-14. Private `func_15175958` now emits the original **0xC8
frame**, saved S0/RA homes, and **956 words** against retail's **961**.
This advances [Note 2451](2451-game-common-particle-update-private-recovery-20261114.md).
**No production installation, new guards or match credit.** Total stays
**4,493 / 5,515 (81.47%)**, Game **3,820 / 4,842 (78.89%)**, zero drift;
**195 more matches** reach 85%. Owner remains **8 / 9 exact**.

VA **0x15175958..0x1517685C**, ROM **0x1A2E08..0x1A3D0C**.
Baseline consumer `c6828e2c`, mounted tools
`1521cf4245a97ef1c0dc787049d177abb8f42bc7`. Qualification is in the five
`game_particle_common_15175958_*` experiment/test modules; ignored artifacts
remain under `conker/build/game-particle-common-15175958-screen/`.

## Frame and typed source recovery

An explicit, signed promoted-byte variant snapshot restores the real opening
index lifetime. Signed promotion also preserves the original shift/add
20-byte indexing rather than the unsigned temporary's multiply form. Separate
offset, trig and motion lifetimes recover frame **0xC8** without array padding,
frame guards or inserted instructions. The selected draft's saved S0 at
SP+0x30 and RA at SP+0x34 agree with retail.

The configuration view now extends the existing 56-byte
`VertexWave1517725C` type with its recovered prefix fields. The common updater
uses a typedef alias to that same type, avoiding a second incompatible struct
view in native C. Its meaningful maximum/minimum speed, turn timers, bank/tilt
limits and switch threshold coexist with the previously recovered wave fields.
All eight neighboring raw functions and owner pools remain unchanged.

The retained raw stream has **128 binding sites**, **876 differing word
positions including the five-word length deficit**, SHA-256
`3e8deef5b52b493afa4cbb2afb794341f4aae6cfa701184aea8df8a32bf78c54`.
Matching frame/length proximity does not qualify the complete instruction stream.

| Private home | Emitted SP offset | Retail SP offset |
| --- | --- | --- |
| Saved S0 / RA | 0x30 / 0x34 | 0x30 / 0x34 |
| Reverse selector | 0x58 | 0x58 |
| Two coordinate offsets | 0x60 / 0x64 | 0x60 / 0x64 |
| Alpha snapshot | 0x6C | 0x68 |
| Model row pointer | 0x70 | 0x6C |
| Configuration pointer | 0x74 | 0x70 |
| Surface output | 0x78 | 0x74 |
| Relative X / Z | 0x7C / 0x84 | 0x78 / 0x80 |
| Trig results | 0xA4 / 0xA8 / 0xAC | 0xA0 / 0xA4 / 0xA8 |
| Angle vector | 0xB0 / 0xB4 / 0xB8 | 0xAC / 0xB0 / 0xB4 |
| Motion vector | 0xBC / 0xC0 / 0xC4 | 0xB8 / 0xBC / 0xC0 |

These are measured allocation differences, not installed remaps. Small clamp,
switch, scalar/aggregate and lifetime probes remain private. The complete CFG,
operation inventory, roles and instruction count still need closure.

## Native sequencing defect found and fixed in the private draft

The first native run rejected the old embedded audio RNG expression. Retail
calls RNG, then reads the current coordinates for `func_10010F88`. C leaves
argument evaluation order unspecified. With a provider changing the record,
one retained O0 counterexample submitted Y **80** instead of retail's **79**.
This is a source sequencing defect, not a reason to weaken packet checking.

The draft now stages audio RNG before coordinate reads. It separately stages
the cooldown RNG before reading the live slot and the height RNG before reading
the live signed-halfword divisor. Those last two statements do not change the
IDO words but make their required C ordering explicit. A reused `soundRandom`
temporary describes the two audio draws. The old embedded-coordinate form is
retained as an effective native negative control at **all three profiles**.

## Completed qualification

- [x] **1,483 guest cases** compare retail and emitted C, all public memory,
  helper packets and complete 248-byte record snapshots at every helper entry.
  Cases now visit **881 / 961 retail words**. Added steering NaNs/infinities
  stay separate from portable native coverage. Late provider mutations include
  slot and divisor changes, with a directed zero-cooldown case ensuring that
  the sound path actually runs after the slot changes.
- [x] **24 pre-division zero-divisor cases** stop before the actual DIVU in
  both streams. They compare public memory, packets and snapshots, including
  the preceding -1 timer store and RNG call. They do not execute C modulo zero
  or claim a hardware division-fault result.
- [x] **1,315 native32 cases at O0/O2/O3**, using undefined-behavior traps,
  compare all 248 record bytes, **616 configuration bytes**, 55 model words,
  eleven control words, step, scene gate, marker, helper packets/snapshots and
  the complete 28-byte live/active flag backing. Valid native variants are
  0..10; mutation-selected slots remain 0..11. Finite FP inputs and distinct
  record/config storage bound this native contract.
- [x] The native flag backing preserves the real overlap: live at +0,
  cooldown at +4 and active at +12. GNU symbol aliases reference one bounded
  byte object; a changed late slot can write into either live or active bytes.
  Native conversion also handles the A4/A6 and sound halfwords explicitly.
- [x] **Six effective native controls** reject active marker, fade direction,
  speed floor, cooldown, unsigned-height correction and the old embedded audio
  RNG expression. SSE `sqrtss` supplies the original single-precision square
  root boundary. Expected results come from independently executed retail
  instructions, not the candidate's C expressions.
- [x] All **three authentic direct JAL windows** execute **120 cases** and all
  **four authentic registry entries** execute **160 cases**, each with retail
  and emitted C. The real dispatcher pointer transport, saved roles and
  nontrivial bookkeeping are checked. Removing the bookkeeping store fails.
  These are bounded caller windows, not full parent/gameplay execution.
- [x] Mounted and isolated sibling-overlay focused suites pass; source, data,
  guard CSV, progress, Makefile and production ELF are not modified by them.

Five guest emitted controls continue to reject marker, fade, speed floor,
cooldown and unsigned-height changes. The native coordinate-order regression
is additional coverage. The former C0 private draft and its unchanged-word
screens are superseded; they were never installed or credited.

Reproduce with the prepared consumer:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_common_15175958_recovery -v
```

The sibling overlay copies **five byte-identical task files** and uses sibling
dependencies with mounted fallback. Sibling HEAD remains
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439 dirty paths** and
before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are preserved. No sibling file is replaced. Shared tools remain unchanged;
the Note 2450 `make tools-check` receipt is reused, not presented as fresh.

All **807 frozen production inputs**, including **82 headers / 698 objects**,
stay fixed. The production ELF remains
`73b2aa1dbe44da28872317ece93d57e1b1a1f3a4f321f8d1af67513e8b31fbf6`.
The previous actual-ELF recount therefore remains applicable. Root README
receives no figure change for this private work.

Scoped Graphify AST refresh covers five tools files, retaining all **61,004
old IDs**, zero lost nodes: **61,010 nodes / 114,688 links**. This is a scoped
merge, not full-corpus re-extraction. Routine Claude calls: zero. Tools commit
`635058a13192e74c31f5cacdb7c2022d61b29957` precedes the consumer pin/documentation commit. No push;
host Release remains frozen.

## Remaining acceptance and resume point

The original **961-word layout**, private homes, complete CFG/register/operation
inventory and any eventual normalization proof remain open. Keep the new native
sequencing regressions while refining source; do not restore the old embedded
RNG to improve compiler shape. Explore the named-home placement around alpha,
the audio temporary and the configuration pointer before introducing remaps.

Guest record/global aliases, a broader independent semantic model and full
instruction-memory prefixes still need qualification. Bounded provider behavior
does not establish helper internals, full FCSR exceptions or hardware parity.
Both padders, independent rebases, strict whole-image prediction, actual Make,
installation/audit and a fresh recount follow only after exact source/word gates
pass. No exact match is claimed here.
