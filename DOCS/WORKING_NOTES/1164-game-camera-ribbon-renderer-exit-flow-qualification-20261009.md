# Game Camera Ribbon Exit Flow Qualification

## Scope And Baseline

Continue complete `func_1514803C` matching from
[Note 1163](1163-game-camera-ribbon-renderer-private-slots-view-staging-20261009.md).
Owner `conker/src/game/generated_175250.c`, VA `0x1514803C..0x151488C4`,
ROM `0x1754EC..0x175D74`: retail **546 words / 2,184 bytes / frame 0x120**.
Actual dispatcher remains the complete 52-word `func_15147C4C` and protected
`D_8008A2A4[1]` entry at `0x8008A2A8`.

Previous goal turn made progress: five measured private slots and the
16-bit-input reference were qualified and committed, not installed. Start
this turn with clean parent `79eeb45ae8aeb5e01ed30c630b0e7f4290568c87` and
clean mounted tools `d940c7e9dcb028002cba435888b02696840ca88d`. Independent
older checkout stays at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all
80 initial status entries and both dirty tracked hashes preserved. One
Codex writer, zero Claude calls. "Keep commited" authorizes tools-first
local banking and the consumer pin, not push/reset/older-checkout commits.

Reuse the immutable Note 1159 source/whole-ELF/guard/progress baseline,
never recapture it. Production still uses GLOBAL_ASM. No guard, source,
profile or progress changes; root README aggregate rows are unchanged.

## Measured Exit-Flow Constraint

The [complete control-flow driver](../../tools/experiments/game_camera_ribbon_renderer_controlflow.py)
changes the signed active gate from an early return to an outer active
block. Preserve the explicit cursor-null return and redundant cursor-nonnull
gate. The entire setup, geometry, SDK commands, backwards wrap and final
XYZ prefetch remain present; no replacement loop, fake work or added bound.

| Complete Reference | Words | Frame | Raw Differences | Actual Padder |
| --- | ---: | ---: | ---: | --- |
| Prior short-input local-view | 547 | 0x120 | 433 | Rejects |
| New `selected-outer` | 545 | 0x120 | 509 | Accepts |

The new form keeps the recovered caller's 16-bit input and all five measured
private slots: cursor SP+0x118, sync 0x117, origin 0xF0, previous XYZ 0xFC
and current XYZ 0x108. All four GPR save slots and five FP save pairs remain
retail-shaped. Unlike the prior early-return form, the backend call lands at
the retail instruction index and the active branch goes directly to the
shared result move. The explicit null return and second cursor gate retain
their retail branch/delay-slot shape.

This removes the oversize and extra active-exit branch constraints; it does
**not** improve the fixed-address raw difference count or prove the full
CFG/schedule exact. Branch displacements still differ. Payload remains S3,
records S2 and view initially S2, rather than retail S2 payload, T5 records
with setup spills and S3 view/texture/stride. Color homes and FP allocation
also differ. Slot fitting alone earns no matching/conversion credit.

## Discriminating Catalog

The final catalog contains **62 complete source forms / 39 instruction
streams**. Outer/goto active
gates, explicit versus empty cursor-null blocks, phase/stride reuse,
registered phase, scalar declaration orders and six independent scale
assignment orders are measured rather than inferred from decompiler prose.

- An empty null block emits a branch-likely instead of retail's explicit
  null-return branch sequence. Its smaller word count is not the right
  matching direction.
- Explicit phase/stride reuse does not recover the retail S3 lifetime. Some
  forms reach exactly 546 words but change the frame to 0x118 or add an FP
  save pair. Do not compensate with unused locals or frame padding.
- Scalar declaration permutations do not recover the FP roles. The grouped
  versus separately declared form can change some instruction choices;
  fingerprints distinguish that from permutations that are identical.
- Six independent scaled-output assignment orders retain the same shape
  metrics but emit six distinct instruction streams for each index schedule.
  Moving the two loop index updates between ray assignments changes register
  pressure, but the resulting 546-word body has frame0x128, three GPR saves
  and six FP pairs. Exact word count alone is insufficient.

The catalog receives three bounded finite controls per form: nonlinear
geometry, banked zero geometry and origin-helper record-pointer mutation,
including raw view0x18000. Final memory/callback checks are not the primary
form's full ordered-write/alias/fault qualification. Retain source and
instruction SHA-256 fingerprints to avoid repeating duplicate schedules.
Phase reuse also changes color and texture spill homes despite unchanged
length/frame/raw-difference counts. Do not treat matching shape metrics as
byte identity. An earlier catalog assertion made that mistake; correct the
fixture using actual linked-word fingerprints. This is not a renderer defect
or a passing full-suite receipt.

## Qualification

The final complete [twelve-test suite](../../tools/tests/test_game_camera_ribbon_renderer_controlflow.py)
passes in **145.688s**. Hard emitted-opcode assertions verify the active and
cursor branch shapes, retail backend-call index, frame/save slots and all
five private slots. The new primary form receives fresh qualification:

- **804 guest cases / 1,608 executions**, complete public memory, ordered
  writes and callbacks. Retail's infeasible second-cursor-zero exit remains
  unexecuted (words34/35); no claim that every retail word was executed.
- **92 setup mutation cases / 184 executions**, captured/live field
  distinctions and scratch GPR/FP/first-eight-argument-home clobbers.
- **94 missing-byte pairs**, five record-pointer aliases and two cyclic
  prefixes bounded at 200 public writes. No production bounds; emitted
  access/fault-prefix evidence, not portable C fault semantics.
- **536 actual native32 cases**, full vertices/commands/pointers, typed
  helper arguments and actor/payload/record canaries.
- **128 additional nonlinear guest/native32 cases**, seed0x1514803C,
  256 guest executions and full native output checks.
- **14 raw view values**, 56 guest cases/112 executions across both banks
  and stack phases, plus14 native32 cases; both view-taking helpers receive
  the expected signed low halfword. Native caller conversion and raw guest
  register clipping are separate checks.
- **16 cases / 32 executions** through the complete actual dispatcher and
  protected table entry. Transform/graphics callees remain bounded hooks.
- Ten copied-owner neighbors unchanged, including pools and relative
  relocations; zero compiler diagnostics and actual padder acceptance.
- Two effective compiled negatives: unsigned active gate and records
  captured before the origin helper. Both change observable behavior.

Four independently linked original/candidate symbol sets exercise **eight
links / 25 relocation uses / 184 cases / 368 guest executions**. Includes
HI16 carry, signed LO16 values, entry/JAL region changes, both banks/stack
phases, raw views, setup mutations, inactive/backend-failure exits and
nonlinear geometry. Original assembly is independently assembled and linked;
default linked words match the retail input and isolated candidate exactly.
Public memory, ordered writes, callback arguments and returns match the
reference under each symbol set. This is bounded guest relocation evidence,
not complete hardware/FCSR or native whole-caller acceptance.

An initial generator rejected the wrong scale-block indentation before
compilation; correct its exact replacement range. The earlier 11-test run
finished in223.730s with one fingerprint-assumption failure, not a passing
suite. All primary semantic tests passed there; final twelve-test results
above are a fresh complete run after correcting the catalog assertions.
The standalone independent-link test also passed in4.871s before that run.

The exact recovered callback signature remains an integration gate:
`u8 *(*[])(u8 *, u8 *, s16)`. The current candidate's typed Gfx pointer
interface is not installed. Do not claim complete native caller, recovered
callees, FCSR trapping, hardware or gameplay acceptance from bounded hooks.
Native alias, mutation, cyclic and invalid-float-cast domains remain outside
the native fixture. Primary guest coverage does not qualify every catalog
form in those domains. Prior broader receipts are reused, not called fresh.

## Next Matching Step

Use `selected-outer` for the explicit retail-shaped exit flow while retaining
the prior 547-word/433-difference source as a lower-raw-difference reference.
Recover S3 phase lifetime, S2 payload/T5 spills, color homes and FP roles
without losing the five exact private slots or signed input. Settle the full
546-word raw schedule and callback interface before remaining alias/mutation
domains, final-source independent rebases, installation and whole-ELF/progress
audit. Reuse current rebase evidence only while its source/profile/symbol-set
fingerprints remain unchanged.
The wider Game matching goal stays active.

## Banking And Validation

Tools **8a71e515744bb8f515f0d2885e178e55c63b4b14** banks exactly the new
driver/test pair first; this note, short indexes and exact parent pin follow.
Copy only the two absent authored tool files, yielding82 older-checkout
entries while preserving all80 initial entries, its HEAD and dirty hashes.
Both project tools checks pass. Syntax/exact-mirror validation passes all47
retained tool-file pairs; documentation checks pass 150 documents / 4,302
relative links / zero broken. No shared helper/build/profile changes, root README narrative,
OGL/Release/save/editor actions, push or goal pause.

All four immutable production hashes stay unchanged. Totals remain5,489
converted/3,406 exact, Game4,816/2,733, zero drift,2,083 different and11,510
guards. No installation or matching/conversion credit this turn.

The query surfaces generic compiler/register nodes, not an exact function
node. Keep the previous post-commit hook's terminal 38,865-node receipt
separate from this manual graph update: it refuses17,077 nodes over38,865,
retaining19,398 nodes from2,972 excluded files still on disk. Existing
package/skill-version and devcontainer zero-node warnings remain; no force
or reinstall. Inspect the fresh post-commit hook independently.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_controlflow --form selected-outer
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_controlflow -v
wsl --exec make tools-check
```
