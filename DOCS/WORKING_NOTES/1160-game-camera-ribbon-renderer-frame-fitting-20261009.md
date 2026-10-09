# Game Camera Ribbon Renderer Frame Fitting

## Scope And Baseline

Continue the complete `func_1514803C` recovery from
[Note 1159](1159-game-camera-ribbon-renderer-recovery-20261009.md), not a
smaller replacement leaf. Owner `conker/src/game/generated_175250.c`,
VA `0x1514803C..0x151488C4`, ROM `0x1754EC..0x175D74`:
retail **546 words / 2,184 bytes / frame 0x120**. The actual protected
renderer pointer is `D_8008A2A4[1]` at `0x8008A2A8`.

Parent starts at `ec0cddd3b61057feec4744a073034e0916ae1a96`, mounted tools
at `8c7bd4a6c49187566ddf8af3026e86bce2a3ce4c`; both clean. Older standalone
remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with 72 initial
status entries and two preserved dirty tracked hashes. One Codex writer,
zero Claude calls. "Keep commited" authorizes coherent tools-first local
banking and the exact parent pin, not a push or standalone commit.

Production remains GLOBAL_ASM. The immutable Note 1159 baseline is reused:
source/entire ELF/guard CSV/progress CSV SHA-256 values are verified unchanged.
No source installation, filler-based conversion, guard additions or progress
credit. The root README aggregate rows remain unchanged.

## Complete Fitting Forms

The new [fitting driver](../../tools/experiments/game_camera_ribbon_renderer_fitting.py)
defines 124 complete forms: private offset/scale lifetime reuse, context and
record-pointer forms, and inlined camera-ray expressions. This is a catalog,
not a claim that all 124 are fully qualified. The corrected mixed screen
freshly compiles 32 forms; other earlier screens remain isolated compiler
measurements. None changes the production source.

| Form | Words | Frame | Raw Differences | Saved FP Pairs |
| --- | ---: | ---: | ---: | --- |
| Prior selected complete body | 547 | 0x130 | 443 | F20..F29 |
| `selected-inline-rays` | 543 | 0x120 | 544 | F20..F29 |
| `outer-indexed-mixed-normalX-normalY-normalZ-deltaX` | 546 | 0x120 | 513 | F20..F31 |

The inline-ray form uses S2 for payload, but saves only S0..S2 at
SP+0x68/0x6C/0x70. Retail saves S0..S3 at SP+0x64/0x68/0x6C/0x70.
The new form spills view in the incoming argument area instead of retaining
retail's S3 lifetime, and spills records from RA across setup calls.
Cursor is SP+0x11C, sync SP+0x11B, primitive colors SP+0xD8..0xDE,
environment colors SP+0xD0..0xD6, previous position SP+0x100..0x108 and
current position SP+0x10C..0x114. These are measured emitted layouts,
not recovered original local declarations.

The 546-word mixed form saves four GPRs but has an extra F30/F31 pair and
shifted save slots. Equal word/frame counts are insufficient for matching.
The actual padder accepts both copied-owner objects, unlike the prior
oversized selected form; this is slot-fit evidence only. Neither candidate
is byte-exact or installed, and no padding-based recovery is claimed.

Exclude scale/offset reuse mappings where the scale variable is one of the
three output targets: the first multiply overwrites the scale needed by
later multiplies. A compiled negative control demonstrates changed public
vertex output on ordinary finite geometry. Invalid earlier screen results
are not accepted candidates or evidence of correctness.

## Fresh Qualification

[Eight fitting tests](../../tools/tests/test_game_camera_ribbon_renderer_fitting.py)
pass in **138.152s**. After adding explicit saved-GPR layout assertions,
the shape/baseline test passes again in **1.589s**; the unchanged behavioral
tests' receipts are retained, not mislabeled as rerun after that assertion edit.
Each of the two forms receives:

- **804 guest cases / 1,608 executions**, ordered public writes, helper calls,
  return value and full public memory. Retail covers all 544 reachable words;
  inline covers 541, mixed 544. Width, signed active/head and unsigned count
  domains, cache, bank, zero normals and finite geometric patterns retained.
- **92 setup-mutation cases / 184 executions**, captured versus live pointer
  and payload fields, signed views, stack phases and helper scratch-register,
  FP-register and argument-home clobbers.
- **94 missing-public-byte pairs**, five public record-pointer aliases and
  two cyclic emitted-prefix pairs bounded at 200 public writes. No production
  loop bound. These qualify sampled emitted prefixes, not portable C fault
  semantics or a guarantee for every alias.
- **536 actual native32 cases**, compiled from each new complete body, not
  from the prior selected body. Complete vertex fields, command words/pointers,
  typed callback arguments, output tails and actor/payload/record canaries
  agree with independent Python float32 expectations. No native cyclic,
  invalid-cast, alias or mutation acceptance is claimed.
- Ten unchanged actual postprocessed owner neighbors, pools and relative
  relocations; zero diagnostics and actual padder acceptance.
- **16 cases / 32 executions** through the complete 52-word graphics
  dispatcher and protected renderer table, with full candidate/retail leaf.
  Graphics/transform helpers remain bounded hooks, not recovered complete
  callees or hardware/gameplay acceptance.

The Note 1159 connected receipt also says **16 cases / 32 executions**.
Its previous prose and roadmap doubled that number; correct those historical
descriptions. No tests or stored receipts are changed to inflate coverage.

Both project tools checks pass. Preserve all 72 older standalone status
entries, both tracked dirty hashes and HEAD; mirror only the two absent new
files byte-for-byte, yielding 74 entries. Python syntax and exact mirrors
pass for all 39 retained tool-file pairs; documentation validation passes
**146 documents / 4,269 relative links / zero broken**. Shared helper/profile/production
inputs are unchanged, so prior broader suites are reused, not called fresh.

Graphify query locates the prior camera-ribbon note/roadmap, but no exact
function node. Manual update refuses 17,036 nodes over the retained 38,824,
keeping 19,398 nodes from 2,972 excluded files still on disk. Existing
version/zero-node warnings remain. Do not force or reinstall; inspect the
fresh post-commit hook separately.

## Concrete Next Step

Continue from the fully tested `selected-inline-rays` form, preserving the
prior selected body as an independent semantic reference. Recover retail's
fourth saved-GPR/view lifetime and original color/position private layout
before trying scheduling normalization. In particular, retail initially
retains view in S3, then reuses S3 for stride 20; records are captured and
spilled across setup, not held as the view. Do not add meaningless source
work, empty exits, loop limits or drop final prefetches just to reach 546.

Resolve the complete raw body/register schedule, then independently rebased
links and remaining alias/mutation domains before production installation
and whole-ELF/progress audit. The wider Game matching goal stays active.
Totals remain **5,489 converted / 3,406 exact**, Game **4,816 / 2,733**,
zero drift, 2,083 different and 11,510 guards.

## Banking

Mounted tools **b2c37ee317552b2cfe40054aeb9a5479f48d7753** banks exactly
the new fitting driver and tests first. Parent documentation and exact gitlink
follow in a separate local commit. No push, standalone commit, pause or
OGL/Release/save/editor work.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_fitting --mixed
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_fitting -v
wsl --exec make tools-check
```
