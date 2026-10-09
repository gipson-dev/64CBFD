# Game Camera Ribbon Retail Frame And Save Slots

## Scope And Baseline

Continue the complete `func_1514803C` recovery from
[Note 1161](1161-game-camera-ribbon-renderer-lifetime-qualification-20261009.md).
Owner `conker/src/game/generated_175250.c`, VA `0x1514803C..0x151488C4`,
ROM `0x1754EC..0x175D74`: retail **546 words / 2,184 bytes / frame 0x120**.
Protected renderer pointer remains `D_8008A2A4[1]` at `0x8008A2A8`,
called by the actual 52-word `func_15147C4C` dispatcher.

Parent starts clean at `b06fa0c874ed7108a45aff09c8b092b286739867`, mounted
tools clean at `799d9be19c59da595301dec835c93bbde3852dcc`. The independent
older checkout remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with
76 initial status entries and both dirty tracked hashes preserved.
One Codex writer, zero Claude calls. "Keep commited" authorizes local
tools-first banking and the exact consumer pin, not a push or older commit.

Reuse the immutable Note 1159 baseline, not a recaptured production baseline.
Source, entire ELF, guard CSV and progress CSV hashes remain unchanged.
The target remains GLOBAL_ASM; no installation, guards or aggregate credit.

## New Matching Constraint Reached

The new [stack-fitting driver](../../tools/experiments/game_camera_ribbon_renderer_stackfit.py)
retains complete setup, graphics calls, cross products, width, paired vertex
writes, SDK commands, backwards wrap and final XYZ prefetches.
Two new complete forms now have **both retail's 0x120 frame and all four
GPR/five FP save slots**, unlike the previously qualified frame-only forms:

| Fully Qualified Form | Words | Frame | Raw Differences | Padder |
| --- | ---: | ---: | ---: | --- |
| `selected-last-output-scale-deltaX-deltaY-deltaZ` | 547 | 0x120 | 463 | Rejects |
| `outer-active-last-output-scale-deltaX-deltaY-deltaZ` | 545 | 0x120 | 512 | Accepts |

Both save S0/S1/S2/S3 at SP+0x64/0x68/0x6C/0x70 and
F20/F22/F24/F26/F28 pairs at SP+0x38/0x40/0x48/0x50/0x58.
This is a measured frame/save-slot constraint, **not a matching register
lifetime or instruction schedule**. GPR save order still differs.
The selected form remains one word larger than retail; outer padder
acceptance is only slot-fit evidence, not installation or byte matching.
No synthetic padding, extra work or dropped behavior was added to reach
the measured save slots.

Disassembly gives the remaining concrete mismatch: candidate initially
retains view in S2, then records in S2 and payload in S3; retail retains view
in S3, payload in S2, captures records in T5 and spills records across setup,
then reuses S3 for the 32-bit texture result and stride 20. In the selected
form origin is SP+0xF4 rather than 0xF0, cursor 0x11C rather than 0x118,
sync 0x11B rather than 0x117, previous/current positions 0x100/0x10C rather
than 0xFC/0x108, and primitive/environment colors 0xD8..0xDE/0xD0..0xD6
rather than 0xBC..0xC2/0xB4..0xBA. These are emitted layouts, not inferred
original declarations. Do not normalize these unresolved differences with
broad word guards.

## Correct Scale Reuse Boundary

Scale/output overlap is not universally invalid. After all normal components
are computed, the old delta values are dead. Set `deltaZ = width / length`,
then compute output X into deltaX and output Y into deltaY; only the final
`deltaZ = normalZ * deltaZ` overwrites the scale. No remaining multiplication
needs the old scale. The zero-length branch still initializes all outputs.

The earlier failing overlap remains rejected: overwriting scale while
computing X changes Y/Z. A fresh compiled negative performs that early
overwrite and changes public vertex output on deterministic nonlinear
geometry. Refine the blanket wording in Note 1160; its effective negative
receipt remains valid. Do not allow overlap with a still-needed normal
component or any overwrite before the remaining multiplies consume scale.

## Fresh Qualification

[Eleven final tests](../../tools/tests/test_game_camera_ribbon_renderer_stackfit.py)
pass in **221.346s**. Each of the two complete forms receives:

- **804 guest cases / 1,608 executions**, ordered public writes, callbacks,
  return value and full public memory. Retail covers all 544 reachable words;
  selected covers 545, outer 543. Nontrapping float/FCSR model is bounded,
  not hardware acceptance.
- **92 setup-mutation cases / 184 executions**, signed views, live versus
  captured actor/payload fields, scratch/FP and argument-home clobbers.
- **94 missing-byte pairs**, five public record-pointer aliases and two
  cyclic prefix pairs bounded at 200 public writes. No production loop
  bound; emitted fault prefixes do not establish portable C fault semantics.
- **536 actual native32 cases**, compiled from each new complete body:
  complete vertex bytes, commands/pointers, typed callback arguments,
  output tails and actor/payload/record canaries.
- **128 additional deterministic nonlinear geometry cases**, seed
  `0x1514803C`, alternating banks, finite float32 positions/origin/width:
  256 guest executions plus 128 actual native32 cases per form. No native
  alias, mutation, cyclic or invalid-cast acceptance is claimed.
- **16 cases / 32 executions** through the actual complete 52-word
  dispatcher/protected pointer. Graphics/transform callees remain bounded
  hooks, not complete recovered callees or gameplay evidence.
- Ten unchanged actual postprocessed owner neighbors, pools and relative
  relocations; zero diagnostics; explicit selected padder rejection versus
  outer acceptance. Neither is byte-exact or installed.

The compiler catalog contains **61 complete forms / 46 distinct instruction
fingerprints**, each with three finite final-memory/callback controls,
including an origin-helper records-pointer mutation. It covers color
structs/arrays, grouped or field-wise XYZ copies, scoped/private color calls
and safe last-output scale reuse. This is sampled screening, not full
qualification or ordered-write acceptance for every form. Grouping the
stride form's positions changes its frame to 0x118; it does not supply
retail's fourth saved GPR. Keep emitted hashes to identify duplicates.

## Typed Decompiler Evidence

Generate a reproducible context for the existing local m2c with a complete
0x120 stack type and real 12-byte positions. Native32 GCC compiles static
size/offset assertions for all ten named private slots. The typed decompiler
now resolves Y/Z position and origin fields, but still emits invalid
`(bitwise f32)` first-field casts and pointer increments in incorrect typed
units. Its captured-record/head/texture ambiguities from Note 1161 remain
unsafe. The raw output is **not compiled or installed**. Context types are
analysis constraints, not recovered original source or SDK/hardware proof.

## Next Matching Step

Use the newly qualified same-frame/save-slot selected form as a complete
reference. Recover the view-to-texture-to-stride lifetime so payload occupies
S2 and records use retail's setup spills; recover the measured color,
position, origin, sync and cursor private slots. Then resolve the complete
raw body/schedule. Do not claim matching from frame/save-slot counts or a
shorter body. Independently rebased links, remaining alias/mutation domains,
production installation and whole-ELF/progress audit remain required.

No shared profile/helper or production input changes. Previous broader
suite receipts are reused, not reported as fresh this checkpoint. Root
README aggregates remain unchanged: total **5,489 converted / 3,406 exact**,
Game **4,816 / 2,733**, zero drift, 2,083 different and 11,510 guards.
The full Game matching goal stays active.

## Banking

Mounted tools **df3bbd1319bf9b60746a0a7d7bfd04c4abd84699** banks exactly
the new driver and tests first. This note, the corrected prior wording,
short indexes and exact parent gitlink follow separately. Preserve all 76
initial older-checkout status entries, both dirty tracked hashes and HEAD;
mirror only the two absent new paths byte-for-byte, yielding 78 entries.
Both project tools checks pass. Syntax/exact mirrors pass for all 43
retained tool-file pairs; documentation validation passes **148 documents /
4,286 relative links / zero broken**. No push, older commit, pause or
OGL/Release/save/editor work.

Graphify query has no exact function node. Manual update refuses 17,055
nodes over the retained 38,843, keeping 19,398 nodes from 2,972 excluded
files still on disk. Existing package/skill version and zero-node warnings
persist. Do not force/reinstall; inspect the fresh post-commit hook separately.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_stackfit --decompiler
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_stackfit --form selected-last-output-scale-deltaX-deltaY-deltaZ
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_stackfit -v
wsl --exec make tools-check
```
