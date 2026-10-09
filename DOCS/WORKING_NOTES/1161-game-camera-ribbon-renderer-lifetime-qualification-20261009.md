# Game Camera Ribbon Renderer Lifetime Qualification

## Scope And Baseline

Continue the complete `func_1514803C` matching work from
[Note 1160](1160-game-camera-ribbon-renderer-frame-fitting-20261009.md).
Owner `conker/src/game/generated_175250.c`, VA `0x1514803C..0x151488C4`,
ROM `0x1754EC..0x175D74`: retail **546 words / 2,184 bytes / frame 0x120**.
Actual dispatcher `func_15147C4C` has 52 words and uses the protected
`D_8008A2A4[1]` pointer at `0x8008A2A8`.

Parent starts clean at `ec3ab4aaa6f598157ef5d2d75c5932a92a8cbfa2`, mounted
tools clean at `b2c37ee317552b2cfe40054aeb9a5479f48d7753`. The independent
older checkout remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with
74 initial status entries and two dirty tracked files. One Codex writer,
zero Claude calls. "Keep commited" authorizes coherent tools-first banking
and the exact consumer pin; no push or older-checkout commit.

Production remains GLOBAL_ASM. Reuse the immutable Note 1159 baseline and
verify all four hashes: source, entire ELF, guard CSV and progress CSV.
No installation, guards, aggregate credit or root README changes.

## Complete Forms

The new [lifetime driver](../../tools/experiments/game_camera_ribbon_renderer_lifetimes.py)
tests typed actor/payload fields, shared view/texture/stride contexts,
declaration/register hints, scalar/vector grouping and counter schedules.
All candidates contain the complete renderer; none is a replacement leaf.

| Fully Qualified Form | Words | Frame | Raw Differences | Saved FP Pairs |
| --- | ---: | ---: | ---: | --- |
| `selected-typed-1-1` | 547 | 0x130 | 440 | F20..F29 |
| `inline-local-stride` | 545 | 0x120 | 526 | F20..F29 |

Typed actor fields retain unsigned count at 0x25, signed active/start/head
at 0x2C..0x2E, records at 0x94 and payload at 0x98. Typed payload fields
preserve signed mode bytes at 0x44/0x45 and the full 32-bit texture result.
The typed body saves S2/S1/S0/S3 at SP+0x6C/0x68/0x64/0x70, but its
record/payload/view register roles and 0x130 frame still differ from retail.
The actual padder rejects its 0x88C bytes in the 0x888-byte slot.

The stride form retains a shared context through view, texture and stride
20. Its frame fits, but it saves only S1/S0/S2 at SP+0x6C/0x68/0x70 instead
of retail's four saved GPRs. Actual padder acceptance is slot-fit evidence
only: **not byte-exact, not installed, not conversion credit**.

The final compiler catalog contains **73 complete forms / 35 distinct linked
instruction fingerprints**. Each receives three finite guest samples:
nonlinear geometry, bank-one zero-normal geometry and an origin-helper
record-pointer mutation. This checks final public memory/callbacks, not
ordered writes or full qualification for every form. Keep both source and
linked-word SHA-256 receipts to avoid reinvestigating source-only changes
that emit identical instructions.

## Fresh Qualification

[Ten final tests](../../tools/tests/test_game_camera_ribbon_renderer_lifetimes.py)
pass in **220.493s**, including the final saved-GPR assertions, three
effective unsafe-decompiler negatives and all 73 compiler forms.
Each of the two fully qualified forms receives:

- **804 guest cases / 1,608 executions**, ordered public writes, callbacks,
  return value and full public memory. Retail covers 544 reachable words;
  typed covers 545, stride 543. Float/FCSR interpretation is bounded and
  nontrapping, not hardware acceptance.
- **92 mutation cases / 184 executions**, captured versus live actor/payload
  fields, signed views and helper scratch/FP/argument-home clobbers.
- **94 missing-byte pairs**, five record-pointer aliases and two cyclic
  prefix pairs bounded at 200 public writes. No production bounds added;
  sampled emitted fault prefixes are not portable C fault semantics.
- **536 actual native32 cases**, compiled from each new complete body,
  with complete vertex/command fields, callback arguments, output tails
  and actor/payload/record canaries checked independently.
- **128 additional deterministic nonlinear geometry cases**, seed
  `0x1514803C`, alternating banks, finite float32 positions/origin/width:
  256 guest executions and 128 actual native32 cases per form. Full public
  vertices, command words/pointers and canaries agree. These native tests
  do not claim alias, mutation, invalid-cast or cyclic acceptance.
- **16 cases / 32 executions** through the actual complete 52-word
  dispatcher and protected pointer. Graphics/transform helpers remain
  bounded hooks, not newly recovered complete callees or gameplay.
- Ten unchanged copied-owner neighbors, pools and relative relocations,
  zero diagnostics and explicitly different padder acceptance boundaries.

No shared helper, profile or production input changes. Earlier broader
suites are retained evidence, not reported as fresh runs this checkpoint.

## Decompiler Audit

Run the existing local `conker/tools/mips_to_c/m2c.py` on the complete
retail body with recovered structures/helper prototypes in an ignored
context file. Retain ordinary and register-hinted outputs for comparison;
do not install their raw text. Three compiled negative controls prove
observable errors in tempting inferred transformations:

- Capturing `actor->records` before `func_15144B34` loses the origin-helper
  mutation of the records pointer (mode 2).
- Reading `actor->head` before `func_15142FBC` loses the final render-helper
  mutation of head/start (mode 7).
- Narrowing the texture result to `s16` loses the full 32-bit cache value.

The decompiler also leaves unresolved position types/byte arithmetic and
nested helper evaluation order. Its inferred private layout is a useful
constraint, not proven original declarations: records SP+0xEC, origin
SP+0xF0, previous XYZ SP+0xFC/0x100/0x104, current XYZ
SP+0x108/0x10C/0x110, sync SP+0x117 and cursor SP+0x118.
Original environment colors are SP+0xB4..0xBA and primitive colors
SP+0xBC..0xC2. Register/declaration/vector variants frequently emit the
same words; changing debug homes alone is not a layout recovery.

## Next Matching Step

Provide correct 12-byte position and origin-view types to the isolated
decompiler context, then explicitly preserve origin-before-record capture,
render-before-head read and full-width texture lifetime. Fit the measured
private slots and retail S3 view-to-texture-to-stride lifetime without
meaningless padding, synthetic work, dropped prefetches or broad guards.
Retail FP roles constrain the scalar schedule: ray F22/F24/F26,
delta Y/Z/X F18/F20/F2, normals F12/F14/F16, length F0, scale F2,
and outputs F18/F20/F22.

After recovering the complete raw body/register schedule, qualify independent
rebases and remaining alias/mutation domains before production installation,
whole-ELF audit and fresh progress. The Game matching goal remains active.
Totals stay **5,489 converted / 3,406 exact**, Game **4,816 / 2,733**,
zero drift, 2,083 different and 11,510 guards.

## Banking

Mounted tools **799d9be19c59da595301dec835c93bbde3852dcc** banks exactly
the new lifetime driver and tests first. Commit this note, short indexes and
the exact parent gitlink separately. Preserve all 74 initial older-checkout
status entries, its HEAD and both dirty tracked hashes; mirror only the two
absent new paths byte-for-byte, yielding 76 entries. Both project tools
checks pass. Syntax and exact mirrors pass for all 41 retained tool-file
pairs; documentation validation passes **147 documents / 4,277 relative
links / zero broken**. No push, standalone commit, pause,
OGL/Release/save/editor work.

Manual Graphify update refuses 17,045 nodes over the retained 38,833,
keeping 19,398 nodes from 2,972 excluded files still on disk. Existing
package/skill version and zero-node warnings persist. Do not force or
reinstall; inspect the fresh post-commit hook separately.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_lifetimes --form inline-local-stride
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_lifetimes -v
wsl --exec make tools-check
```
