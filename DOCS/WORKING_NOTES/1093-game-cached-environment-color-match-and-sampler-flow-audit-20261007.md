# Game Cached Environment Color Match And Sampler Flow Audit

Date: 2026-10-07. Baseline: `d21f5ece`,
[Note 1092](1092-game-oriented-matrix-direct-match-20261007.md).

`func_15142C10`, VA `0x15142C10..0x15142CF0`, ROM
`0x1700C0..0x1701A0`, now emits **all 56 words / 224 bytes directly from C**
under unchanged **O2/g3**, with the original **frame `0x8`** and saved S0.
The former semantic implementation used an early cache-hit return and manual
command words. A positive cache-miss gate plus the actual SDK
`gDPSetEnvColor(output++, ...)` macro recovers retail's packet pointer,
allocation, branches, delay slots, short cache stores and exact epilogue.
No guards, profile/header/padder changes or padding locals are needed.

## Sampler Flow Audit

Resume `func_151432BC` from
[Note 1074](1074-game-area-sampler-qualified-recovery-20261006.md) and the
scalar-lifetime screen in
[Note 1091](1091-game-actor-lookup-byte-abi-direct-match-20261007.md).
The new [flow driver](../../tools/experiments/game_area_sampler_flow_candidates.py)
retains **54 O2/g3 measurements**: 24 switch-source permutations, 12 early-return
if/else chain forms, six single-case/switch splits and twelve real RNG
temporary/type/register controls. Keep the original 48-byte scratch, signed
live descriptor fields and unsigned angle conversion. Full-width signed RNG
temporaries use an explicit unsigned shifted subtraction, avoiding signed
overflow at `INT_MIN` before the byte helper argument is formed.

All forms have frame `0x50`, no new pool and empty diagnostics, but **only one
RA reload versus retail's three**. None is exact. Word counts vary from 250
through 254. The 254-word forms obtain their extra words from changed
dispatch/block placement, not the two missing per-path reloads; do not use
word count alone as an installation gate. Canonical switch `3201` remains
252/109; reversed-circle `3210` is 252/91 but moves the circle blocks.
RNG declarations with `register` do not recover the original store schedule.
These measurements extend the maintained bank to **252 measurements**
(152 original + 30 supplementary + 16 lifetime + 54 flow), not distinct bodies.

[Four flow tests](../../tools/tests/test_game_area_sampler_flow.py) pass in
75.122 seconds before production editing:

- **1,536 input fixtures / 82,944 candidate executions** qualify all 54 forms
  against the independent public reference. Cover four modes/high flag bits,
  signed-halfword extremes, both stack phases, four output/descriptor alias
  arrangements, callback field mutations and three full RNG words including
  `INT_MIN`. Complete external memory, ordered output writes, helper calls
  and saved state agree. Private layout/trace identity and equality of all
  public reads are not claimed.
- **48 unsigned-conversion fixtures / 2,592 candidate executions** cover both
  integer stages, invalid paths and three incoming control words. The bounded
  truncation/invalid-bit model restores control state before helpers/return;
  this is not general FCSR or native invalid-cast/hardware acceptance.
- Compiler receipts pin 54 measurements, one reload each, no exact candidate,
  frame/profile/pool/diagnostic facts and the unchanged production placeholder.

An optional `cc -S` diagnostic died in the local recompiled `ugen` with signal
11; no usable pre-assembler comparison was obtained. Its partial output was
moved into ignored scratch. Do not infer a compiler-stage cause from that
failed diagnostic. Ordinary object compilation and all required tests work.

The sampler remains uninstalled, with no guards or matching increment.

## Environment Color Contract

The [color driver](../../tools/experiments/game_cached_environment_color_candidates.py)
retains twelve gate/cursor/SDK/explicit-packet forms across four SDK profiles,
**48 measurements**. Only `positive1-cursor0-sdk-o2g3` is direct 56/8/zero.

- Compare the four full signed32 channel inputs against signed16 cached
  values, lazily and in RGBA order. Do not narrow inputs before comparison.
  A cache hit returns the original cursor without reading sync or output.
- On a miss, read sync once. Only byte **one**, not any nonzero byte, emits
  `E7000000 / 00000000`, advances the cursor and then clears sync.
- Emit `FB000000 / RRGGBBAA`, packing each input's low byte with the actual
  SDK unsigned shifts. Advance once more, then store the low halfword of
  each channel to its cache, in RGBA order. No calls or allocation occur.
- Preserve write order when sync, cache or command storage alias. A clear
  may overwrite a just-emitted command byte; no alias guard is invented.

## Color Qualification

[Seven color tests](../../tools/tests/test_game_cached_environment_color_match.py)
bind the complete direct body and original assembly reference:

- **62,400 guest fixtures** cover every byte value in each channel (not every
  Cartesian RGBA combination), signed16 boundaries/full signed32 extremes,
  all first-miss/cache-hit positions, four sync bytes, two destination and
  three sync alias locations, and two stack phases. The independent reference
  checks complete external storage, returned cursor and every ordered public
  read/write. Raw C/retail additionally agree on all memory bytes, events,
  GPR/FPR values, calls and visits. All 56 target words execute.
- **5,200 freestanding native 32-bit fixtures** run the actual SDK macros,
  full channel inputs, signed cache comparisons, lazy hits, exact sync states,
  cache updates and unused-command fences. Native storage is disjoint; guest
  alias tests are not native alias/hardware/rendering acceptance.
- Cache-hit probes leave sync/output unmapped and still succeed. Required
  cache/sync/output bytes fail closed. Six compiled negatives change public
  results or lazy traces: unconditional emission, nonzero sync gate, wrong
  opcode, swapped channels, missing clear and unsigned cache declarations.
- The production-preprocessed/postprocessed copied owner retains **89
  functions / 88 neighbors**, relative relocations, normalized pools and the
  same **two warnings**. The selected raw 224-byte target equals the isolated
  object. The real padder emits the full slot, without overflow. Independently
  rebase each of the four cache symbols by `0x18000`; only its actual
  HI16/LO16 relocations change, including signed-low carry handling.
- Installed source, linked exact slot/address and all guard history are pinned.

Five pre-install behavior/owner/padder gates pass in **51.549 seconds**.
Repeated fixture runs are not additional distinct behavioral cases.

```sh
python3 -m unittest tools.tests.test_game_cached_environment_color_match \
  tools.tests.test_game_area_sampler_flow tools.tests.test_game_area_sampler_recovery \
  tools.tests.test_game_oriented_matrix_match tools.tests.test_game_actor_lookup_match \
  tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
```

The combined regression passes **50 tests in 336.828 seconds**. Final
`make tools-check`, Python syntax and `git diff --check` gates pass; the scoped
documentation gate checks **75 documents / 3,874 relative links**, zero broken.

## Build And Audit

`make -C conker build/conker.us.elf -j2` succeeds with the existing duplicate
recipe warning and the same two owner pointer warnings. Fresh pre-edit and
post-link audit retains **6,058 linked symbols**: **6,042 retail slots** plus
16 compiler overflows. Every address/extent is fixed; only `func_15142C10`
changes. All **6,041 other retail bodies**, including the sampler and primitive
color neighbor, and all overflow symbols remain identical.

Protected Init/Init-data/Debugger/Game-data sections, **720 Game-data owners /
189,088 bytes**, and all **11,006 guards** remain unchanged and exact. Neither
color target nor sampler has a guard. Converted functions/bytes do not change;
the color routine already had semantic C.

Exact total advances to **3,359 / 5,466 (61.45%)**, Game to
**2,686 / 4,793 (56.04%)**, **2,107 different**, zero drift. Init492/492 and
Debugger181/181 C functions remain exact. Main README changes only the two
aggregate matching rows; detailed updates stay under DOCS.

## Resume

Bank this direct color match and the qualified sampler flow bank. Next ordinary
neighbor is **77-word `func_15142CF0`**, the cached primitive-color emitter:
recover its positive cache-miss gate and actual SDK macro, then qualify all six
cache fields, sync/order/alias behavior and owner/padder/install gates before
claiming a match. It still has its old manual body and remains nonmatching.

The sampler still needs its two legitimate per-path RA loads and circle RNG-byte
store schedule. Do not repeat this source-order/register sweep as new evidence,
install the short body, insert instructions, or patch private/frame offsets.
No sibling/frozen Release, save/runtime, rendering/hardware acceptance or push.

Ignored receipts: `conker/build/game-area-sampler-flow/`,
`conker/build/game-area-sampler-flow-test/`,
`conker/build/game-cached-environment-color/` and
`conker/build/game-cached-environment-color-test/`.
