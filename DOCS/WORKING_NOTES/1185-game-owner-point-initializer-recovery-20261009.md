# Game Owner Point Initializer Recovery

Date: 2026-10-09

## Result And Boundary

Continue from [Note 1184](1184-game-owner-ribbon-renderer-guarded-c-match-20261009.md)
with complete func_151B3A7C, VA 0x151B3A7C..0x151B3CF0,
ROM 0x1E0F2C..0x1E11A0. Original: 157 words /628 bytes, frame 0x60 /96 bytes.

Recover the entire ten-point initializer, not only a shortened compatible path.
[Candidate driver](../../tools/experiments/game_owner_points_initializer_candidates.py)
contains complete semantic source. Recovered form fits 157 words, but frame
0x58 /88 bytes and private position home differ from retail; 143 real word
differences remain. No installation, new guards or matching/conversion credit.
The production zero-return placeholder remains in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c).

Parent baseline c9359a95, mounted tools 713023c9d50cbe09a66ef5f345a34d2632ab6c8b;
both clean initially. Previous turn made committed renderer progress.
Single Codex writer, zero Claude calls; no OGL/Release/save/editor work or push.
The wider Game matching goal remains active.

## Actual Registration And ABI

The sole aligned retail pointer to 151B3A7C is ROM 0x2345B8,
D_8008FAF8[0] at VA 0x8008FAF8. The already matched 81-word func_151B3184 update
loads a fresh signed actor+0x34 selector, indexes this table, forwards only the
actor pointer in A0, and uses the signed32 success result to gate cleanup.
Reconstruct the interface as s32 func_151B3A7C(u8 *actor).

Three distinct linked input words at D_800AA394 /398 /39C have bits 0x3DE38E39,
binary32 0.1111111119389534. These are independently addressable Game data,
not permission to replace all three with one hard-coded literal or divide by nine.
The original loads them after storing the first complete output record.
Tests preserve that distinction with independent scale values and alias fixtures.

## Complete Contract

- Compute each binary32 endpoint delta from actor+0x20/24/28 minus +0x14/18/1C.
- Copy the initial three coordinate words without canonicalizing their bits.
- Store ten records at actor+0x48, stride 24 bytes, ending before actor+0x138.
  Each record has a copied 12-byte position and a positive-zero 12-byte second
  vector. The candidate labels the latter velocity; its original field meaning
  is not established solely by this routine.
- After the first record, derive three independently scaled increments from the
  retained endpoint deltas and actual linked input words.
- Generate subsequent positions by repeated ordered binary32 additions.
  Do not substitute start + index * step; its rounding differs.
- Retain all ten private position advances, including the last iteration.
- Read actor+0x10 after record generation; clear only bit 2, preserve every
  other flag bit and return 1. There is no early flag gate or external helper call.
- Preserve incoming saved GPR and FP registers; original saves/restores F20/F21.
  Full original/candidate word coverage is measured.

The reference model operates on complete public memory, including input/scale
aliases, with binary32 rounding at each actual arithmetic operation. It is a
bounded low-word instruction model, not a hardware/FCSR emulator. Stack-private
trace and public access order are not currently byte-exact.

## Source And Profile Fitting

Twenty-nine complete source forms pass all eight ordinary contract fixtures each,
232 candidate executions plus 232 original executions. Initial scalar/byte-access
source emits 234 words/frame56/232 differences. Typed record addressing reduces
this to 232/frame56/217, still too large.

Source loop peeling and explicit four-record grouping are experiments containing
all ten records and the same arithmetic. Giving the four-record loop its real
count local avoids a second compiler expansion: 157/frame88/145 differences.
Move scale derivation after the first complete record, preserving actual aliases:
157/frame88/143. This is the selected RECOVERED form, not the initial BASE.

| Form | Words | Frame bytes | Real differences |
| --- | ---: | ---: | ---: |
| Recovered grouped loop, late scales | 157 | 88 | 143 |
| Grouped loop, early scales | 157 | 88 | 145 |
| Grouped typed loop, separate zeros, late scales | 156 | 88 | 152 |
| Grouped byte access, separate zeros, late scales | 158 | 80 | 131 |
| Simple typed loop with count local | 59 | 48 | 155 |
| Grouped count loop with unequal termination | 235 | 88 | 233 |

These are fitting controls, not installation choices based solely on a lower
difference count. Ordinary-case model agreement does not establish every alias
for every form. Only the selected late-scale body receives full alias/native/
dispatch/rebase qualification. No unused padding locals or literal retail words.

Four selected-body profiles: O2/g3 157/frame88/143; O2 157/frame88/127;
O1/g3 and O1 299/frame56/299. None matches. Existing production profile is unchanged.
The local wrapper finds the actual negative SP adjustment in the prologue rather
than assuming it is word zero; O1 can schedule another instruction first.

## Qualification

[Nine-test recovery suite](../../tools/tests/test_game_owner_points_initializer_recovery.py)
passes in 35.481s, zero skips, after the final local prologue-measurement correction.
Earlier nine-test run passed 39.376s; report the final run as current.

- Guest: 2,048 cases /4,096 original/candidate executions, all 256 flag bytes,
  four geometry bit-pattern sets and two incoming stack phases. Both complete
  157-word bodies reached; saved GPR/FP lifetime checks pass.
- Independent scales and first-output constant aliases: 44 cases /88 executions.
  The three first-record aliases exercise overwritten position/zero words before
  scale loads. Public memory and return agree with the independent reference.
- Six effective compiled negatives reject wrong flags, failure return, missing
  last four records, reversed X increment, collapsed Z scale and nonzero second
  vector. These run emitted instructions, not only source-text comparisons.
- Actual complete native32 C: 8,192 cases, all flag bytes, finite binary32
  geometry/independent scale values and every actor/canary byte checked.
  Native fixtures qualify public results; no FCSR exception claim.
- Actual complete original 81-word update and registered callback:
  32 cases /64 executions, lazy skipped first callbacks, signed selector 0,
  live timer update and success return. No cleanup hook is needed for these
  paths; wider cleanup/walker behavior is outside this suite.
- Four independent symbol sets /eight original/candidate links:
  32 cases /64 executions, all six original HI16/LO16 relocation uses retained.
  Original canonical assembly equals all 157 ROM words. Rebases qualify full
  semantics; candidate is not falsely reported byte-exact at any set.
- Actual copied owner and padder: 16 neighbors/pools/relative relocations
  preserved, zero existing/new warnings; target equals isolated raw body.
  Padder accepts the 628-byte slot without new guards, but does not establish
  frame/private-home equivalence. Explicitly reject installation on that basis.
- Four missing-byte faults /eight executions compare public memory prefixes:
  endpoint input, first output, first scale and final flags. Two removed unused
  bytes /four executions still return normally. No general read-order,
  portable-C fault-order or hardware exception equivalence claim.
- Production source/ELF/guards/progress hashes, actual callback pointer and
  189,088 protected Game bytes /720 owners are unchanged and exact.

The first suite run exposed a local inheritance error while reusing the signed-byte
instruction override. Make PointOracle an actual ActorOracle subtype and initialize
its complete TriangleOracle state explicitly; rerun the full suite. No production
defect or weakened assertion is inferred from the fixture error.

Project make tools-check passes. No new linked rebuild is needed because
production source/profile/guards/data are byte-identical; the prior successful
Note 1184 build is reused explicitly, not reported as freshly rerun.
No hardware/emulator/live rendering/gameplay was exercised.

## Preservation And Checkpoint

Unchanged SHA-256:
source 2cd9fbac1a68ad325b9e644abdedb867f42f777fdb4cff4cb058856cb82ad50c;
ELF 4867fdd672d1e50e18345bcdc0f8a2d50c8774e443863e7d13cbffa0554a14b9;
guards 431d3bb33607126440e2a13829f599c27bdf25851767e25d05097911a49c7913;
progress 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.
Protected data 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh matching report remains total 3,416 /5,489 (62.23%) and Game 2,743 /4,816
(56.96%), zero address drift /2,073 different. Init492/492 and Debugger181/181
remain exact. Root README aggregate rows are unchanged.

Mounted tools b3a58e3e547051d49c4b909330d2e68b2fd8de7a commits the driver and
suite before consumer documentation/tools pin. No push requested/performed.
Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a, both tracked
dirty-file hashes and all 122 original dirty entries are verified unchanged.
Mirror only two absent authored files, yielding 124; no older commit/reset/push.

Ignored receipts: conker/build/game-owner-points-initializer/ and
conker/build/game-owner-points-initializer-test/.
Explicit graphify update . exits1, refusing 39,063-to-17,282 node shrink while
preserving the graph. Retain version/zero-node/scan-corpus warnings; no force,
purge or install. Wait for the separate consumer incremental commit-hook receipt.
Documentation validation passes: 171 documents /4,541 relative links /zero broken;
all 89 authored tooling files parse and have identical mounted/older mirror bytes.
Scoped Git whitespace checks pass. Independently dirty older checkout retains all
122 previous entries and both tracked dirty-file hashes; only the two intended
new files raise its count to 124.

## Continue This Function

Recover the complete actual workspace/private position home and loop-pointer
shape directly from real semantic locals. Original frame is0x60 and position
home SP+0x44; current frame is0x58 and position home SP+0x34.
Do not patch the frame alone or add unused padding to make metadata look right.

Retain late independent scale loads, full ten-record arithmetic/flag contract,
all six relocation uses and current native/guest/alias/dispatch qualification.
Then fit induction, zero-store order, register allocation and scheduling. Any
residual normalization needs closed lifetime/memory/control proofs, effective
negatives and complete independent linked qualification before guards.
Install only after full frame/slot/word/owner/ELF/data/guard-history checks pass.
