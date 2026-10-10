# Game Owner X-Axis Point Interpolation Byte Match

Date: 2026-10-10

## Baseline And Result

Continue after consumer 823e6aa5345c8f5862a3aaeebe7692a00c4f7bd2 and mounted
tools b4e101ab91697aa1c134e8803e506fbedf27f9ac, both active checkouts clean.
[Note 1203](1203-game-linked-node-endpoint-transform-direct-match-20261010.md)
banked the neighboring endpoint updater. The older standalone tools checkout
remains at ddbdd16b53ce60b054fb6e11bf0649a41f48375a with162 pre-existing dirty
entries. Mirror only the two absent new files, preserving its tracked edits.

func_151B48DC: VA0x151B48DC..0x151B498C, ROM0x1E1D8C..0x1E1E3C,
44 words /176 bytes, leaf with no frame allocation. Replace the false zero-return
C placeholder in [generated_1E0560.c](../../conker/src/game/generated_1E0560.c)
with the complete ten-point X-axis interpolation routine. All44 linked words
match retail through a closed compiler-normalization recipe. This is semantic
C plus46 dependency guards, not a plain-C match. No new pools or padding.

Use the scoped Graphify query and existing compiler/parser/MIPS/native32/padder/
ELF/data helpers. Single Codex writer, zero Claude calls; no bridge, shared
helper/profile changes, OGL/Release/save/editor work or push. Keep the wider Game
matching goal active. Root README receives only aggregate row updates.

## Recovered Contract

Reuse the existing OwnerPoints3A7C /24-byte point record layout. Read only the
start X at owner+0x14 and end X at+0x20. Compute the rounded subtraction
start-end, then its negation; do not replace this with end-start. Two negative
zero endpoints distinguish the expressions: the original preserves negative
zero through the repeated positions.

Store point0 X as the original start bits, and Y/Z as positive zero. Only after
those three stores, read D_800AA3C4: address0x800AA3C4, ROM0x24EE84,
bits0x3DCCCCCD /0.1f. This can alias any first output component. Multiply the
negated difference by the captured factor. Store points1..9 using repeated
rounded addition, not start+i*step. The ten positions use nine increments,
not an altered1/9 factor designed to force the final point onto the endpoint.

Every position Y/Z is zero; every velocity byte stays untouched. Clear flag0x2
only after all position stores and return1. There are no calls or stack accesses.
Unused start/end Y/Z and velocity bytes need not be mapped for guest execution.

The actual registration is D_8008FAF8[4] /0x8008FB08, ROM0x2345C8. The complete
original81-word func_151B3184 dispatches this third-stage updater when owner+0x34
is4 and flags0xC are absent. Its return1 retains the owner; skipped dispatch sets
flag0x2. The dispatcher and table remain unchanged.

## Compiler And Closed Recipe

[Candidate driver](../../tools/experiments/game_owner_points_line_candidates.py)
screens17 complete source forms under the existing O2/g3 profile. Selected
ordinary typed loop emits46 words, frame0, no diagnostics/pools and37 raw word
differences. Indexed raw pointers also emit46/37. Two manually peeled points
emit45 words; explicit four-record work with a local count emits44 but changes
the induction/branch structure and has38 differences. A word-count-equality
form emits88 words. Those alternatives are measured, not installed or claimed
to satisfy the selected scheduling gates.

The recipe consumes the entire expected46-word compiler shape, allowing only
relocated immediate fields at+0x1C/+0x24. It reads no retail words to construct
output. The44 surviving source offsets form a complete closed permutation:

- Remove only the initial NOP at+0x4 and point-one pointer add at+0x2C.
- Fold its three stores into owner-relative+0x60/+0x64/+0x68 accesses; the pointer
  was used only there, then overwritten by loop limit10.
- Rename the end/difference/negative/scale/step/current-X producer roles without
  changing arithmetic operations, operands, rounding or dependencies.
- Schedule input loads before the zero-register transfer, and retain the first
  three stores before the relocated constant read.
- Move point-two Y/Z stores ahead of cursor advancement, folding their negative
  offsets to the same physical addresses. Move the independent final X addition
  into the loop branch delay slot; it still executes on every iteration.

All46 manifest rows guard the actual object:37 changed retained words, seven
unchanged dependencies and two omissions. No inserted instructions. HI16/LO16
relocations follow their original instructions through the permutation. Actual
padder output and original retail assembly agree across four independent symbol
sets, including signed-low carry boundaries.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_owner_points_line_match.py): all nine
tests pass before installation in21.744s and after in21.622s.

- 7,680 guest cases /23,040 executions cover every flag byte, fifteen finite/
  signed-zero/subnormal/overflow/infinity/NaN endpoint pairs and both stack phases.
  All44 original,46 raw and44 normalized words execute. Entire final memory,
  return and saved GP/FP/SP agree with an independent rounded reference; private
  stack and every velocity byte remain untouched.
- Raw ordered reads and write multisets match original. Normalized full ordered
  read/write events match original, including the unrolled stores and delay-slot
  update. Raw reordered-store fault prefixes are not claimed equivalent.
- 78 positive constant-alias/independent-factor cases include input X, the first
  three outputs, untouched velocity, and later outputs. Six effective complete
  compiled negatives cover reversed subtraction/negative zero, premature constant
  read, nine points, direct formula/repeated rounding, velocity clear and wrong flag.
- 34 paired normalized fault prefixes and unmapped unused Y/Z/velocity fields
  qualify emitted guest order, not portable C faults or hardware trap behavior.
- Actual native32 selected C passes8,192 finite full-memory cases,288 constant
  aliases and196 special-float pairs. Record size0x138/stride24 and existing offsets
  qualify. First X raw bits and all Y/Z zeros are exact; arithmetic NaNs are
  classified, not a host/N64 payload or FCSR-equivalence claim.
- Twelve independent links/four entry-global symbol sets and32 guest rebase cases
  qualify relocation propagation. Twelve complete original dispatcher cases retain
  table registration, dispatch/skip flags and no-removal contract.
- Actual copied owner preserves all16 neighbors, raw bodies, relative relocations
  and pools. Actual padder preserves every other byte, emits176 bytes with no
  padding and keeps func_151B498C at its original address. The production padded
  target is independently identical to the qualified normalized object/relocations.
- Actual padder rejects each of46 individually stale source words at its exact
  offset, including both omitted instructions; a stale HI16 relocation spec is
  independently rejected. No stale-layout bypasses.

Reuse prior unchanged endpoint/arc receipts from Note1203/Note1196 explicitly as
prior evidence. Fresh copied-owner and whole-ELF comparison prove their bodies
unchanged; do not rerun unrelated suites whose historical baselines intentionally
record the earlier whole owner/ELF. No live game, emulator, hardware or FCSR tests.

## Linked Installation And Bank

Fresh build/progress and make tools-check pass. Changing the shared guard manifest
triggers the normal wider rebuild; existing duplicate generated_12D630 recipe,
legacy pointer/long-double and old compiler fullwarn warnings persist. Isolated
and copied target-owner compiles are clean; do not call the full build warning-free.

The rebuilt entire ELF equals the baseline after replacing only the176-byte target
slot and symbol extent. Symbol/string ordering is normalized; decoded metadata
agrees. Old guard bytes remain an exact prefix and the only new rows are the46
qualified target dependencies. Conversion CSV is byte-identical. Protected data
189,088 bytes /720 owners stays exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The registered pointer and protected0.1f constant remain unchanged.

Fresh matcher: Game2,748/4,816 (57.06%), total3,421/5,489 (62.32%),
Init492/492 and Debugger181/181 exact. Zero address drift /2,068 different.
Converted counts/bytes remain unchanged because the prior placeholder was C.
Bank mounted tools d9f391de8b05357a66910c14c1cb3153f570c183 first, then consumer
source/guards/docs/aggregate rows/pin. Both new files are exact older mirrors;
its HEAD/tracked dirty fingerprints remain unchanged. No push requested/performed.

Manual graphify update exits1 and refuses to overwrite39,242 nodes with a17,462-node
scan. Fail-closed retention keeps19,398 nodes from2,972 excluded-but-present files.
Existing0.9.20/0.9.26 and zero-node devcontainer.json warnings remain. No force,
purge, install or policy changes; report any fresh hook receipt separately.

## Next Target

func_151B4B78:41 words /164 bytes, leaf, VA0x151B4B78..0x151B4C1C,
ROM0x1E2028..0x1E20CC. Complete retail body uses start bits0xC47A0000 /-1000.0f
and D_800AA3C8's0x435E38E4 /222.222229f before any point store. It is registered
at D_8008FAF8[5]. Recover its ten-point fixed-span sequence, early constant-read
aliases and exact unrolled operation order while preserving velocities.

Preserve the uninstalled curve's
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
frame/private/slot gates. Any future curve harness must record a fresh isolated
baseline for these authorized neighbor changes without overwriting old receipts.
The wider Game matching goal and actual hardware/FCSR/gameplay acceptance remain open.
