# Color Channel Aggregate Direct Match

Date: 2026-10-17. Completes the aggregate handoff from
[Note 1471](1471-color-progress-accessor-direct-match-20261017.md).
Consumer baseline **92730710**, tools baseline **5298c5e**. Codex is the
single writer; zero Claude calls suffice for this directly resolved match.

## Direct C Recovery

`func_1517EFDC` in `conker/src/game/generated_1AC2F0.c` now contains its
complete semantic C body rather than a zero-return stub. The first complete
candidate matches all **44 words / 176 bytes directly** with the existing
normal O2/g3 profile. Frame **0x30**, VA **0x1517EFDC..0x1517F08C**, ROM
**0x1AC48C..0x1AC53C**. No new guards, insertions, omissions, compiler profile,
private pools or source diagnostics are needed.

The precise interface is `s32 func_1517EFDC(void)`. Start the active tally
at -1 and channel at zero. Visit channels inclusively through the live signed
limit `D_80082FA0`; count a channel when signed progress is strictly positive
or, only otherwise, its `D_800DDDC8` float state is strictly positive.
Compare the tally with the final live limit. Do not substitute a cached
limit, nonzero progress, nonnegative float test or zero-based tally.
In particular, initial limit -1 returns one without any helper call; -2 does
not. Controlled callbacks can change both the remaining loop and final test.

Raw text SHA-256:
**2a218119a8ddf6a48897a341fb0b7b7049a40c0c5661f93342ebc484928f3af6**.
The independently assembled original has identical words and all **five
relative bindings**: two HI16/LO16 pairs and the progress helper's R26 call.
The actual normal padder preserves every word. All **27 raw/padded owner
neighbors** remain unchanged. Existing external caller declarations already
have the correct no-argument signed-return interface.

## Qualification

All **22 post-installation tests pass in 361.799s**: seven target tests,
three installation tests and twelve prior progress/color/scan/setup installed
tests. All seven pre-installation tests passed in **122.641s**.

- **5,142 paired original/C aggregate guest cases**, both stack phases,
  live signed limits, strict float comparisons, NaNs, signed zero, infinities,
  subnormals, bounded callback mutations and three global alias maps.
  Every aggregate word executes. Compare literal full private memory,
  modeled GPR/FPR/HI/LO, condition, calls, events, PC/delay and data accesses.
- **14,924 helper-call snapshots across both sides** check S0 channel,
  S1 tally, S2 limit pointer, S3 float-state pointer, frame 0x30, the saved
  S0/S1/S2/S3/RA homes, zero F20 at the call and the original saved F20/F21
  pair. Normal returns also enforce the existing complete saved-register ABI
  check. Opaque providers clobber caller-saved GPR/FPR/HI/LO and outgoing homes.
- Actual **43-word func_1517EF00** executes in the real-helper cases, with
  entry explicitly fired. It reaches its same 42 natural words; guarded
  BREAK 7 remains unreachable. **54 paired overflow-trap cases** propagate
  the emitted helper BREAK 6 through the aggregate frame.
- Three independently linked original/C rebase pairs match every word across
  global HI16/LO16 carries and changed R26 helper targets. Alias fixtures
  also independently link the original and compiled C with identical bindings.
- **72 positively fired data-access fault prefixes** compare literal state
  through actual aggregate/progress instructions, including the overflow
  prefix. These are emitted-order checks, not portable C faults or CP0 proof.
- Complete **41-word func_151E8214** sequence-phase caller executes with the
  actual **44-word aggregate and 43-word progress helper** in **3,600 paired
  cases**, including **120 propagated overflow-trap pairs**. Every caller
  word executes. Explicitly check fired/skipped aggregate and helper entries,
  stage-8 bypass, signed timer boundaries, timer reset and phase-transition
  fields against an independent reference. This chain has no opaque provider.
- **4,284 native32 cases per O2/O0 profile with UBSan**, compiling the full
  aggregate, progress body and sequence caller in separate units. A test
  dispatcher selects the actual compiled progress body or the bounded
  mutating provider; no LTO/fwrapv. Check full bank/limit/script state,
  padding/canaries, helper counts and channel packets, including word aliases.
- Eight effective native controls all compile and exit **22**, not signals
  or sanitizer traps: exclusive loop, nonzero progress, nonnegative/negative
  float predicates, cached limit, wrong tally origin, reversed equality and
  missing float fallback. Native overflow division is excluded and covered
  by the emitted guest trap cases instead.
- All **44 raw words**, five bindings plus an unexpected binding, and all
  **148 protected production inputs** reject unknown changes.

Native loops stay in the four-entry fixture domain, including large initial
limits immediately reduced by controlled callbacks. This does not establish
arbitrary unbounded array indices as valid. FP comparisons use the existing
nontrapping model/native environment; NaN/subnormal fixtures are not hardware
FCSR, exception-enable, denormal-trap or CP0 qualification. Full sequence-engine,
rendering and gameplay acceptance remain separate. Broader unchanged semantic
suites remain prior receipts, not newly run suites; their twelve installed
checkpoint tests are freshly run through the new exact-successor adapter.

## Complete Installation

Before production edits, reproduce the predecessor ELF from captured normal
link inputs and freeze the first complete image/source prediction. The normal
build recompiles/pads only the affected owner and regenerates progress. Its
entire ELF equals that first prediction:
**a94062b3a07a3d0c03571a2e8e4f647d6a4ad4e9325db9309e9adc0c61862a4d**.

Of **130 changed ELF bytes**, **129** are target instructions and **one** is
the symbol-size update **12 -> 176**. Every other ELF byte is identical,
with no symbol/string reordering and **zero metadata exclusions**. All
canonical definitions are unchanged except this size. The full guard
manifest is byte-identical. Existing duplicate Makefile recipe warnings
remain; this is not a warning-free build or fresh whole-ROM checksum claim.

Installed source owner:
**f3b7927450fa6f9f6f768346eeacdac837dece59e8ff69c177d10670d4c70cf8**.
Protect **148 inputs / 146 unchanged inputs**, both before/after fixture
pairs, and **189,088 Game-data bytes / 720 owners / zero differences**.
The prior progress checkpoint recognizes only this pinned successor before
its original inverse. Unknown images, sources and fixtures remain rejected.

## Progress And Bank

Fresh official matching: Game **2,944/4,828 (60.98%)**, total **3,617/5,501
(65.75%)**, still different **1,884**, zero address drift. Init remains
**492/492**, Debugger **181/181**. Conversion stays **5,501/6,044 functions /
86.04% bytes**; the previous stub already counted as C. Conversion CSV bytes
are unchanged. Root README changes only its two aggregate matching rows.

Tools **83a87d2** banks nine files before the consumer pin. Both local copies
have nine identical pairs and **18 ASCII/AST checks**. Eleven standalone padder
tests pass per copy: active **0.031s + 0.021s**, mirror **0.029s + 0.018s**;
tools-check passes. The two pre-existing task files were explicitly checked
against the committed tools baseline before copying. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and all **992 unrelated initial
dirty-file hashes**. Two existing task files are updated, seven added:
**1,001 final dirty paths**. No mirror commit/reset, push, Claude call,
dependency/configuration change, host-port build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_color_channel_aggregate_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_color_channel_aggregate \
  tools.tests.test_game_color_channel_aggregate_installed \
  tools.tests.test_game_color_progress_installed \
  tools.tests.test_game_color_state_submit_installed \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the complete live-limit/signed-progress/strict-float aggregate directly from C.
- [x] Preserve all 44 words/five bindings, frame/saved F20 lifetime, 27 neighbors and every guard byte.
- [x] Qualify real progress/sequence chains, mutable callbacks, FP/alias cases, native controls, rebases and faults.
- [x] Freeze the first whole image/source before edits, build and pass target plus predecessor installed tests.
- [x] Measure fresh progress, update aggregate rows/indexes/roadmap and bank tools first.

Next: **func_1517F08C**, the adjacent still-stubbed display-list overlay leaf:
**197 words / 788 bytes**, no frame, VA **0x1517F08C..0x1517F3A0**, ROM
**0x1AC53C..0x1AC850**. Recover its full six-argument interface and five
commands / 40-byte cursor advance using the existing SDK graphics macros.
Qualify packed RGBA, the 0x180-byte viewport stride/bounds, four unsigned
float conversions and FCSR restoration, plus the base-pointer reload after
the first rectangle-word store. The leaf always emits even for zero alpha;
do not move the caller's zero-progress gate into it. Use existing graphics/FP
oracles and audit its real wrappers. Wider Game/additional-source matching,
the query engine, timing's 141 differences and full gameplay stay open.

Follow-through: the adjacent overlay leaf is now installed as a full direct
197-word C match in [Note 1473](1473-color-overlay-draw-direct-match-20261017.md),
with all five caller interfaces qualified and the first complete image audit.
