# Game Camera Ribbon Renderer Recovery

Verified locally: 2026-10-09. The complete **func_1514803C** is recovered in
an **uninstalled semantic C candidate**. Retail remains GLOBAL_ASM. Ordinary
O2/g3 emits **547 words /2,188 bytes /frame0x130 /443 raw differences**;
retail is **546 words /2,184 bytes /frame0x120**. This is a recovery and
qualification checkpoint, **not a new byte match or conversion credit**.

## Baseline And Scope

Parent **cc234381d6848afcb1c97f82f6ee444ba72be5d4**, mounted tools
**f0818a5c524768cffd883b5e9e3585df1ded20bd**, initially clean. Older standalone
HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a** has70 pre-existing status
lines; preserve them and both dirty tracked-file hashes. One Codex writer,
zero Claude calls. The previous goal turn made verified committed progress;
this turn pursues the queued complete renderer, not a smaller leaf substitute.

Owner [generated_175250.c](../../conker/src/game/generated_175250.c),
[complete original assembly](../../conker/asm/nonmatchings/generated_175250/func_1514803C.s).
VA **0x1514803C..0x151488C4**, ROM **0x1754EC..0x175D74**. Read all546
instructions and the recovered direct helper interfaces. Actual protected
**D_8008A2A4[1] at0x8008A2A8** points here, called through the complete
52-word graphics dispatcher **func_15147C4C**.

Original production fingerprints, captured once in ignored
`conker/build/game-camera-ribbon-renderer-test/baseline.json`:

| Artifact | SHA-256 |
| --- | --- |
| Owner source | 176546c15a2cfbe36d0ff2335c0791ca1be737abc69679d88a232dc7735f8b89 |
| Whole ELF | 9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e |
| Guard CSV | 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030 |
| Progress CSV | 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24 |

All four remain unchanged. No production source, guard, layout, profile,
compiler, shared helper, ROM, OGL, saves or editor changes. Original ELF is
3,261,160 bytes; its entire identity retains every body/address/extent and
protected data/symbol/metadata byte. Do not recapture this baseline.

## Complete Contract

Capture actor+0x98 payload even before the signed active-byte gate<2.
Request `(unsigned count *32)-32` bytes at actor+0x84 with signed16 view,
private Vtx cursor and null optional argument. Failure returns incoming
command pointer. Retain the redundant second cursor-null gate. Nonzero
D_800BE9C0 selects the second vertex bank by `(count*2-2)*16` bytes.

Set private sync byte1, query the live view origin, then capture actor+0x94
records. Resolve the texture with `(NULL,payload[0x19],0,2)`. On cache miss,
reload the live selector to publish D_80091564[index] into D_800915A4[0],
emit the ten-argument texture helper with bit0x80 selecting62 versus3, and
publish the captured texture result to D_800DD1B0. Preserve all14 color
helper arguments, their signed byte mode loads, signed16 results, six-/eight-
argument environment/primitive calls, geometry/combine/render-state helpers
and sync lifetime. The native typed u8 helper modes observe their low bytes;
the emitted MIPS tests separately require retail's full sign-extended words.

Initialize head-1 and its predecessor as full-width signed indices, wrapping
negative values to a live unsigned count-1. Copy both XYZ structures bitwise
from20-byte records. Seed a pair around the previous endpoint using the
cross product of `(previous-current)` with `(previous-origin)`. Each loop
uses the same segment difference with `(current-origin)`. Preserve ordered
float32 subtraction/products/sum/sqrt/division, exact zero-length fallback,
live payload width and live origin loads. Positions truncate to signed32
then narrow into signed16 vertices. Phase is unsigned16+0x4000; transverse
texture coordinate is0x43C0 /0x4000. RGBA are255 and vertex flag0.

Each step emits the SDK four-vertex command and two single-triangle commands
for0/1/2 and1/3/2. Walk backward with live count wrap. Copy previous and next
record XYZ **before** testing the live signed start byte, including the final
unused prefetch. No invented count clamp, empty exit or production loop bound.
The complete command pointer is returned. Setup helpers remain bounded
interfaces, not newly recovered callees or hardware/gameplay proof.

## Fresh Qualification

[Candidate driver](../../tools/experiments/game_camera_ribbon_renderer_candidates.py)
and [nine-test suite](../../tools/tests/test_game_camera_ribbon_renderer_recovery.py)
reuse existing compiler/object parsers, MIPS and float32 oracles, native32,
asm postprocessor and pool helpers. No shared helper changes.

- **804 cases /1,608 executions** cover all active/head/count bytes in finite
  windows, signed view limits/high bits, both banks/cache branches/texture
  modes, zero/collinear/nonzero geometry and zero/negative/tiny/large width.
  Candidate and retail match independent reference public memory, ordered
  writes, callback arguments and result. **544 reachable retail words** and
  545 candidate words execute; retail indices34/35 remain naturally dead.
- **92 mutation/failure cases /184 executions** cover nine live mutations
  plus baseline, two stack phases, captured payload versus later record
  capture, texture/cache and color reloads, head/start changes, origin/width
  changes, caller-scratch/FP and first eight argument-home clobbers.
- **Eight effective compiled negatives**, each compared over five samples:
  unsigned active/head, wrong bank/phase/normal/triangle/cache and early
  records capture. Use head128/count4/start1 to distinguish unsigned head;
  head128/count128/start126 was an ineffective sample and was replaced.
- **94 missing-public-byte pairs**, five public record-pointer aliases,
  four compiler profiles. The production O2/g3 ordered-write test stays
  strict; other profiles are final-memory/callback controls, not claims that
  their differently scheduled writes match retail fault order.
- **536 actual native32 defined cases** check complete vertex fields, GPU
  commands/pointers, typed helper arguments, output tails and full actor256 /
  payload128 /records7,720-byte canaries. All active/count bytes tested.
  Independent Python float32 geometry supplies expected results. Native
  little-endian untouched Vtx halfwords are initialized explicitly; no
  native aliases, live mutations, cyclic inputs or invalid float casts claimed.
- Ten actual postprocessed owner neighbors, pools and relative relocations
  are unchanged, with zero diagnostics. The actual padder rejects installation:
  **`patched func_1514803C is 0x88C bytes but its retail span is only 0x888`**.
  No filler, broad normalization or dropped instructions are used.
- **16 cases /32 executions** connect the complete52-word dispatcher and
  full547-word candidate /546-word retail leaf through the actual protected
  table. Signed view and optional transform argument are checked. Transform
  and graphics helpers are bounded hooks, not complete callee acceptance.
- **18 complete source forms**, three finite samples each, and two cyclic
  emitted-prefix pairs bounded at200 public writes. These are screening and
  invalid-prefix evidence, not full qualification of every form or a C
  termination guarantee. No bound is added to production.

The initial vertex discrepancy was a fixture defect: camera origin had been
placed at the oracle stack base and overwritten by incoming arguments. Move
the origin to a disjoint region; retain an explicit non-overlap assertion.
Do not attribute that failed fixture to retail or candidate arithmetic.

## Fitting Evidence And Next Action

| Profile /form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Selected O2/g3 | 547 | 0x130 | 443 |
| Selected O2 | 546 | 0x130 | 459 |
| Selected O1/g3 | 687 | 0xE8 | 674 |
| Selected O1 | 687 | 0xE8 | 674 |
| Indexed seed O2/g3 | 547 | 0x128 | 442 |
| Single cursor gate O2/g3 | 546 | 0x130 | 467 |

Outer-active, byte-record, shift-stride and ray-lifetime forms also screen,
but none has the retail0x120 frame. The chosen complete body remains the
fully qualified source baseline; do not install a shorter form just because
its word count fits. Next fit **both position/private-local layout and the
record-pointer lifetime across setup calls**. Retail spills captured records
and uses S2 for payload/S3 for view then stride; the candidate keeps records
in S2 and payload in S3. Recover that lifetime before register/scheduling
normalization. Independently rebased linking, full native alias/mutation
qualification and installed whole-ELF audit remain future matching gates.

Nine final tests pass in **106.260s**. Both tools checks pass. Prior35 shared
tests from Note1158 are explicitly reused, not rerun: no shared helper/profile/
production input changes and the whole ELF/guard/progress hashes are unchanged.
Documentation validation passes: **145 documents /4,261 relative links /
zero broken**. All37 mounted/mirrored tool files parse and have exact bytes.
The older standalone keeps all70 initial status lines, both dirty tracked
hashes and its HEAD; only two absent new paths are added, total72 status lines.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_candidates
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_recovery -v
wsl --exec make tools-check
```

Graphify finds no target node; manual refresh refuses17,027 nodes over retained
38,815 and keeps19,398 nodes from2,972 excluded files still on disk. Existing
version/zero-node warnings persist. Do not force or reinstall. Check the fresh
post-commit hook before closing the checkpoint.

## Banking Boundary

Per "Keep commited", bank the two new mounted tools first, then docs and
exact parent pin. Mirror only these absent tool paths into the independently
dirty older checkout; do not commit/reset it. No push. Keep ignored candidate,
baseline, execution/native/owner/form receipts out of commits. Production
counts stay **5,489 converted /3,406 exact**, Game **4,816 /2,733**, zero
drift,2,083 different,11,510 guards. The root README does not change because
no aggregate credit changes. Keep the complete Game matching goal open.

Mounted tools **8c7bd4a6c49187566ddf8af3026e86bce2a3ce4c** is banked first
with exactly the two candidate/test files; parent pins that revision second.
