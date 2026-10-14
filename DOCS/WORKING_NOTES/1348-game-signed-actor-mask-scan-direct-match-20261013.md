# Signed Actor Mask Scan Direct Match

Date: 2026-10-13. Continue
[Note 1347](1347-game-actor-payload-creator-direct-match-20261013.md) with
`func_1506AAE0`: VA `0x1506AAE0..0x1506AB7C`, ROM `0x97F90..0x9802C`,
39 words / 156 bytes, original frame `0x30`. The wider Game goal stays active.

## Baseline And Contract

Consumer baseline `bbcff6cdd966436707328c4a4fb0604800120d30`; tools baseline
`3c7f8cab499603f71a4c95d1079653df6e770fc1`. The production routine was a
zero-return placeholder in `conker/src/game/generated_97AA0.c`.

Recover a void callback with two unused 32-bit incoming arguments. Snapshot
signed `D_800CC260` once and start at the actor array `D_800CC2D0`. For each
set low bit, call `func_15137610(actor, D_800D1560, D_800D1570, 0, 255, 1)`.
Arithmetic-shift the local mask right and advance the actor by `0x32C` for
every bit position, including unset positions. Stop only when the snapshot
reaches zero; callback changes to the global mask do not change this scan.

The retail SRA means negative masks do not reach zero. Do not substitute an
unsigned mask, clamp the bit count, add an actor-count bound, or reload the
global after callbacks. Guest negative tests explicitly stop observation at
callback 64; this is not a claim to have executed an infinite run or qualified
all downstream providers. Native pointer arithmetic is tested only with the
declared 32-bit, sufficiently backed fixture.

The scan does not dereference its unused incoming pointers, actor records or
vectors itself. Its provider may do so. The real callee assembly's byte load
from incoming slot five supports the `u8` flag declaration; its existing
integer result is ignored by this void callback, not replaced with a new
return-value contract.

## Direct Compiler Recovery

New tools:

- `experiments/game_actor_mask_scan_candidates.py`
- `tests/test_game_actor_mask_scan_match.py`

24 source shapes across four existing compiler profiles give 96 measurements.
All 24 O2/g3 shapes match; the installed plain, nonvolatile while loop matches
**all 39 words directly from C**, frame `0x30`, no pool, diagnostics or guards.
No compiler profile or normalizer changes. O2 without g3 still has 11 word
differences; the O1 shapes keep the wrong `0x28` frame and either 37 or 39 words.

The original incoming homes are frame SP+0x30 and SP+0x34. S0..S3 and RA retain
their original saves, lifetime and reloads. The single JAL is at offset 0x68;
all global HI16/LO16 relocations and the branch-delay actor update emit directly.

## Qualification

After correcting fixture setup, all **14 pre-install checks pass in 56.135s**.
The complete installed run passes **15 checks in 67.757s**: twelve target tests,
two protected text/data tests and the preceding creator's direct-shape check.

- 33,688 positive guest cases cover all 4,096 low-12-bit masks, every positive
  single bit and complement through bit 30, independent additional patterns,
  four provider modes and two SP phases. Compare the independent bit-position
  reference, callback arguments, all external storage and full modeled states.
  Every one of the 39 target instructions is reached.
- 64 negative guest cases cover eight masks, four provider modes and two phases,
  each stopped at the actual 64th callback. Sign extension continues beyond bit
  31 even after callbacks clear or overwrite the global mask. Complete prefix
  states and an independent expected callback sequence agree.
- Twelve input/alias cases verify unmapped unused arguments, absence of own
  actor/vector dereferences and the mask global rebased onto each incoming home.
  Preserve prologue writes before the mask load and the captured snapshot after
  home mutation. Private-home aliases are guest evidence, not portable C promises.
- Six compiled semantic controls are effective in guest and actual native code:
  unsigned mask, wrong stride, wrong vector, wrong flag, stepping only selected
  actors and reloading the global mask after a callback.
- Native32 executes the actual typed body under O2 and O0, **262,424 cases per
  profile**, including every low-16-bit mask and signed callback-64 prefixes.
  GCC's builtin nonlocal return bounds the actual callback without adding a
  termination condition to the recovered routine. No 64-bit host acceptance.
- Complete copied-owner compilation and both real padders preserve all fifteen
  neighbors, normalized pools and relative relocations. The preceding creator
  stays byte-exact and the raw target instructions survive padding unchanged.
- Eighty connected cases execute the original 38-word indirect dispatcher,
  its real vector setup and table index 10. Verify the frozen ELF and ROM table
  word at `0x80086138` / ROM `0x22ABF8`, both forwarded arguments, target coverage
  and complete modeled states. The vector-dispatch provider remains bounded.
- Three independently assembled original/source links qualify actual HI/LO
  carry boundaries and the JAL, with 120 semantic cases and complete word/state
  agreement, independent of the production ELF.
- All **1,200 own-instruction fault pairs over 48 domains** fire and agree.
  Completed access counts are 13 + twice the selected-bit count. Provider reads
  and writes are excluded from encoded accesses. The wrong O1 frame is an
  effective private-state negative. Hardware PC/BD/full FCSR are not claimed.
- Header, target, preceding creator, image tail, source and guard corruptions
  all trigger the literal immutable-image gate.

The first connected fixture compared 38 executed parent words with a linked
extent containing three more alignment no-ops. Correct the fixture to compare
all 41 words against ROM, including the exact 12-byte tail, while executing the
38-word body. Add the caller's actual actor/global vector setup and independently
verify the table word. These failed setup attempts are not production defects
or qualified passing receipts. A test keyword typo is likewise corrected before
interpreting any suite result. No warning or acceptance gate is disabled.

Routine work uses zero Claude calls and no additional REA setup, dependency
installation, emulator, host build or gameplay claim.

## Installed Image And Progress

Install only this body and its three required global/helper declarations.
Preserve the original assembly, callback table, all neighboring source, existing
O2/g3/MIPS2 profile, layout and guard manifest. The standard linked ELF/progress
build succeeds with no new target diagnostics; the existing duplicate-recipe
warning remains. No ROM or host executable is built or launched.

The complete ELF equals the frozen image with only the 156-byte target slot
replaced and its named function size changed 12 -> 156. Exactly **132 bytes**
differ: 131 target code bytes and one size-field byte. No blanket metadata
exclusions. All 189,088 Game data bytes / 720 owners remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `026132cc793e9a4c00c612958f706583f14ef65fd8452481aee7dbfed0a66c68` |
| ELF | `79f140332385316ef3a26372c7d231a89bf02c37a398f151ac03ac79568949a0` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

All 15,042 historical guard rows stay byte-identical; the target has zero guards.
Fresh totals: Game **2,828 / 4,823 (58.64%)**, total **3,501 / 5,496 (63.70%)**,
different **1,995**, drift **0**. Converted functions/bytes do not change because
the false-C placeholder was already counted. Root README changes aggregate rows
only; detailed recovery remains in this note.

Only after the literal image and effective corruption gates pass, archive all
nine text-fixture snapshots plus their manifest under
`actor-mask-scan-before-rebase/`. Advance only its ELF snapshot and the single
verified ELF pin in both tools copies. Guard pin, all other protected inputs
and every corruption test remain fixed.

## Banking And Next Work

Tools **3d885558514938441c293596a4163b8dc1a15d7a** banks the two new files and
one-line text ELF pin first. The consumer records that exact pin. The older
tools mirror keeps HEAD ddbdd16 and 448 of 449 initial fingerprints. Only its
protected text test gets the verified pin; two absent, byte-identical files
bring the dirty count to 451. No mirror commit/reset or push. Both copies pass
ROM-free wrapper checks and Windows byte-compilation.

Direct Graphify update refuses 18,809 proposed versus 40,587 retained nodes,
preserving 19,398 nodes from 2,972 excluded-but-existing files. Do not force
shrink or install a different package. Record incremental hook/post-bank
results separately below.

Next `func_1506A79C`: VA `0x1506A79C..0x1506A83C`, ROM `0x97C4C..0x97CEC`,
40 words / 160 bytes, frame `0x38`, still a placeholder in the same owner.
It snapshots actor coordinates at offsets 0x14/0x18/0x1C and computes the three
global-vector differences before calling `func_151D3480`. Recover both live
private vectors, exact floating subtraction/access order and the six-slot ABI
before claiming a match. This next body remains unmodified.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_mask_scan_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_mask_scan_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_actor_payload_creator_match.GameActorPayloadCreatorMatchTests.test_01_complete_direct_slot_and_all_real_source_profiles -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
