# Game Oriented Matrix Original Frame Recovery

Date:2026-10-06. Baseline:`851a0f93`
([Note1069](1069-game-row-matrix-match-and-oriented-layout-20261006.md)).
This checkpoint advances `func_15142600` recovery and qualification tools,
**not production matching**. Its zero-return placeholder remains unchanged.
No new guards, frame rewriting, profile/shared-header changes or installed caller.

## Original Frame Recovered

Retail:142 words/568 bytes, frame0xB8, VA15142600..15142838,
ROM16FAB0..16FCE8. The twelve-input ABI and oriented-basis contract are unchanged
from [Note1068](1068-game-oriented-matrix-recovery-20261006.md).

[Maintained driver](../../tools/experiments/game_oriented_matrix_candidates.py)
now adds sixteen source forms across four actual SDK profiles:horizontal
two-component/three-component struct, separate/in-place direction normalization,
expression/in-place up normalization, and direct/captured start point.
Total128 controls:prior32 base,32 layout and64 in-place controls.
All standalone diagnostics empty; no complete exact candidate.

The best form `inplace0100` subtracts the points into direction's reversed
three-field struct, then normalizes that struct in place. This removes the
separate dx/dy/dz group while preserving every arithmetic instruction.
Under unchanged O2/g3 it emits **142 words, frame0xB8,27 differences**.
All input-home, saved-state, early temporary, arithmetic, helper-call and
branch-delay words match; every differing word changes only an SP immediate.

| Qualified O2/g3 Candidate | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Initial frame-fitting array-up |142|0xB8|84|
| Prior reversed struct-up |142|0xC8|57|
| Ordered/reversed direction |142|0xC8|47|
| Ordered/reversed direction/captured start |142|0xD0|44|
| In-place direction normalization |142|0xB8|27|

The remaining differences have two exact relationships:

- Ten normalized-direction loads/stores use SP64/68/6C instead of retail68/6C/70.
- Seventeen matrix references, including its pointer setup at offset58, use
  SP70..AC instead of retail78..B4.

The tests check these relationships and equality of every other word.
They do **not** normalize offsets or patch the frame. The raw142-word symbol
contains its complete return/delay pair; actual padding retains all568 bytes.
guMtxF2L's sole R_MIPS_26 remains at offset21C.

## Qualification

[Thirteen maintained tests](../../tools/tests/test_game_oriented_matrix_recovery.py)
pass in120.279s, no skips/errors/failures:

- 128 compiler controls; exact frame/length and private-only assertions for
  the new body, alongside the previous controls and layout assertions.
- 2448 six-body guest cases:five C candidates plus retail; known matrix fields,
  destination, all external bytes, source/output aliases, helper source mutation,
  two stack phases, signed/degenerate points and special float bits.
  All142 instructions covered in every body, saved GPR/FPR/SP/RA state preserved.
- 1224 actual freestanding32-bit native typed-caller cases per candidate,
  five candidates/6120 total. Complete external-byte comparison; converter is
  a bounded float-payload capture and arithmetic NaNs are classification-compared.
- 144 connected cases per body execute every original30-word caller,
  142-word builder and115-word converter instruction. Cardinal directions and
  asymmetric scales stay in the finite exactly integral signed32-bit domain
  after multiplication by65536.
- Eighteen compiled semantic negatives:the same nine wrong-call/direction/cross/
  normalization/scale/translation/output mutations applied to both the initial
  array body and the new in-place body. Each changes known behavior on valid
  mapped storage; missing mapped memory and native integer-load rejection remain.
- Actual padder exercised for both frame-fitting bodies, preserving568 bytes
  and retargeting only the converter call under alternate link addresses.
- Five copied builder owners preserve all92 other raw functions/relocations,
  private pools and two existing warnings; target equals its standalone object.
  Typed caller copy preserves all eight raw owner functions/pools/relocations,
  zero warnings and all30 retail caller words. Caller correction remains copy-only.

No original sqrt hardware/FCSR exception-mode acceptance, general fixed
conversion rounding/NaN/out-of-range behavior, native NaN payload parity or
private trace identity across different layouts is claimed. Gameplay and host
integration remain outside these bounded guest/native gates.

## Rejected Explorations

Ignored receipts under `conker/build/game-oriented-matrix/`:

- `left_orders.py`:96 declaration-order/delta/matrix-aggregate controls.
  All remain142/frameC8/44, so declaration permutation is not the remaining fix.
- `in_place_vectors.py`:sixteen O2/g3 scratch forms, now represented by the
  maintained generator. Best142/frameB8/27; three-component horizontal variant
  grows to frameC0/47. Up in-place normalization alone does not improve layout.
- `homogeneous_vectors.py`:sixteen meaningful homogeneous-component forms.
  Four-component direction and up, with zero w forwarded to the corresponding
  matrix fields, recover every private offset but retain frameC0/17 differences.
  Those17 words are frame/input-home displacements, not an eligible exact match.
- `consumed_normalizer.py`:six ex/ey/ez reciprocal-storage controls; lengths
  141..148, framesB0..D8 and132..141 differences. Reject changed scheduling.
- `vector_normalizer.py`:eight vector-w reciprocal/reset forms;142/frameC0/30.
- `partial_up.py`:32 component-normalization/homogeneous controls; no exact
  candidate. Best private-exact forms still142/frameC0/17.
- `vector_storage.py`:sixteen struct/array and three/four-component forms.
  Best still142/frameB8/27 or142/frameC0/17; arrays change the instruction stream.

None of those additional homogeneous/consumed-normalizer/storage scratch bodies
is installed or behavior-qualified by the maintained five-candidate fixtures.
Do not claim their small difference counts as acceptance.

## Production And Next Step

Audit against the Note1069 manifest:all6059 function slots, addresses/extents,
protected init/init_data/debugger/game_data and10809 guard rows unchanged.
All720 Game-data owners/189088 bytes remain exact. Production-source diff
against851a0f93 is empty. Current progress report confirms unchanged totals:
3343/5464 total exact (61.18%), Game2670/4791 (55.73%),2121 different, zero drift.
Converted counts/bytes and root README remain unchanged; no new match is counted.

All41 focused neighboring regression tests pass in185.411s, zero skips/errors/
failures:11 row matrix,13 oriented matrix,12 scaled matrix and5 padder tests.
Project tools, scoped Python compilation and git whitespace checks pass.
Documentation verification covers52 documents/3585 relative links, zero broken.

Next:recover direction68/6C/70 and matrix78..B4 from legitimate C while keeping
the now-correct frame0xB8. The private-exact homogeneous form is useful allocation
evidence, not authority to shrink its frame. Do not replace the placeholder or
install private-offset guards merely to report a match.
After a full candidate matches, install builder and typed caller together,
then repeat owner, production, neighboring regression and progress gates.

Ignored audit/regression receipts:`conker/build/game-oriented-frame-test/`;
maintained test receipts:`conker/build/game-oriented-matrix-test/`.
No sibling source/build/save/runtime, frozen Release, host adoption or push.
The full Game matching goal remains active.
