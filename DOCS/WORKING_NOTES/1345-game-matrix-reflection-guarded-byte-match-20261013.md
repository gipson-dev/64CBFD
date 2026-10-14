# Matrix Reflection Guarded Byte Match

Date: 2026-10-13. Finish `func_15034F30` after
[Note 1344](1344-game-matrix-reflection-original-prologue-recovery-20261013.md).
VA `0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`: 486 words / 1,944 bytes,
original frame `0x190`. The wider Game matching goal remains active.

## Baseline And Recovered Source

Consumer baseline `7b6ec48727339df6f9aa37e1eaa5bd772649776d`; tools baseline
`579be6c075871007ec300c8f2e3862729ab28821`. Production had a zero-return
placeholder, not a recovered reflection implementation.

The interrupted loop-setup source survived; the proposed normalization helper
and its receipt did not. Recompile the surviving source rather than claiming
that the interrupted normalization or installation had completed.

The recovered 19-slot interface preserves the unused float slot, live mode,
count and output homes, SDK matrix indexing and four original shifted indices.
Modes 0/1 perform the Y reflection and opacity falloff; mode 2 performs the
rotated X reflection around a pivot and planar-distance falloff. Preserve
fixed/float input and output conversion, in-place aliases, the full-width actor
gate and the temporary actor matrix-pointer replacement around its callback.

Twenty-one complete loop-setup forms retain 486 words/frame0x190. The selected
`secondary-ioc-snapshot1` snapshots the secondary count before output setup,
improving 240 ->238 literal differences while retaining all22 opening words.
Raw return GPR9/13 remain different; the banked240 GPR9/14 negative is retained
separately. Equal extent or public output is not a direct C match.

## Guard Derivation

New tools:

- `experiments/game_matrix_reflection_loop_setup.py`
- `experiments/game_matrix_reflection_matching.py`
- `tests/test_game_matrix_reflection_match.py`

The normalizer reads the emitted source object, not retail bytes. Its complete
1,944-byte unrelocated SHA-256 is
`a904c1c26881f37fbdb461a11a0deb5a9967da4bcad388b5f4ee8c10b086473b`.
All16 R_MIPS_26 call relocations must have their exact names and offsets.
Linked input identity canonicalizes only those call-target fields.

Derive 238 expected-word guards from closed GPR/scratch-FPR lifetime cycles,
dead floating-result coalescing, two integer-add operand commutations and two
single-precision multiply operand commutations. Loop-local s4/s5 cache/offset
roles are normalized without changing their prologue or epilogue stores.
Saved F20..F28, helper argument registers and the original frame remain fixed.
COP1 transfer, compare, unary and branch fields are handled separately; reserved
fields and REGIMM subtype fields are not register operands.

Every opcode, immediate, memory offset, branch displacement and call relocation
stays fixed. No instruction movement, insertion, omission, padding, fixed-register
C binding or retail-word substitution is used. The normalized complete body
matches all486 retail words. This is **guarded byte-exactness**, not direct C
compiler matching: the raw body still differs at238 words.

## Qualification

The pre-install suite passes20 tests in71.600s; the added image-corruption check
passes separately in1.516s. The complete installed suite passes **21 tests
in64.167s**, including the two protected text/data tests.

- 4,800 sampled guest cases compare the raw C body to the independent semantic
  reference and compare complete normalized modeled return states with retail.
- Input/output overlaps, mixed-format provider rejection, live count/output and
  post-callback actor homes, and both authentic19-slot caller windows remain tested.
- Native32 executes the actual typed C body at O2/O0,256 cases per profile;
  all four ramp/gate/restoration/distance-slot negatives remain effective.
- Across192 domains, all10,260 access cuts actually fire and the normalized
  RAM/GPR/FPR/condition/LO/events/raw-call states and dispatched words agree.
- Both complete owner padders preserve all neighbors, pools and relocations.
  Three independently assembled retail/guarded rebased links agree completely.
- Every238 stale expected word is rejected by both padders and the source hash;
  every dropped replacement breaks complete identity. All16 omitted relocations
  are rejected. Invalid cycles, stale arrays and incomplete objects fail closed.
- Banked240 return-register and cut19 negatives, and bare-O2 cut1/profile
  negatives, remain effective. Whole-image/source/guard mutations are detected.

The owned compiler capture fires and exits with complete normal/traced object
identity. Physical locals296/saved88/outgoing16/frame400, optimizer M292/P76 and
matrix offsets -268,-192,-128,-64 remain fixed. These are bounded model/native
checks, not arbitrary-input, hardware PC/BD/full FCSR/HI, complete SDK execution,
complete-parent or host/gameplay acceptance.

## Installed Image And Progress

Replace only the target placeholder in `conker/src/game/generated_61D10.c`,
add its five required helper declarations and append exactly238 guard rows.
The historical manifest is an exact byte prefix: 14,770 ->15,008 rows.
The original assembly, layout, compiler profile and conversion CSV stay fixed.

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds. The shared guard
dependency rebuilds many owners and emits existing unrelated compiler/recipe
warnings; this is not a warning-free build. No ROM or host executable is built.

The entire ELF equals the archived image with only the target slot replaced and
that named function's four-byte size field changed from12 to1944. Exactly1,465
bytes differ:1,463 inside the slot and two at size-field bytes0x2BBE1A/0x2BBE1B.
There is no blanket metadata exclusion. Header, addresses, all other symbol
fields, neighboring functions and protected data remain fixed. All189,088 Game
data bytes /720 owners are exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `03c09d4eb4d2a7631759b1f73fd26bc11e6989bd358a09406e55d2ec5c959f5a` |
| ELF | `fd188cd74393988f34b462987b50082856707d02e5b729e7a119ba3f100890ee` |
| Guards | `586bbe75d4b9fbee2fb3429e15ca8bf9822449177fb53bdb2e1ca786d435f110` |

Fresh matching totals: Game2,825/4,823 (58.57%), total3,498/5,496 (63.65%),
different1,998, drift0. Conversion totals remain5,496/6,044: this replaces a
previously counted false-C placeholder, not an additional conversion row.
Root README changes aggregate rows only; detailed recovery remains here.

After the exact image proof, archive all nine protected text-fixture snapshots
and their manifest under `matrix-reflection-before-rebase/`. Advance only its
ELF/guard snapshots and two corresponding source pins; preserve the other seven
inputs and every corruption gate. Both immutable text tests pass after rebasing.

## Banking And Next Work

Tools **5c4c157b3534695444588e479d67f0d5ed80fb1c** banks the three helpers/tests
and the two-line text-pin update first. The consumer records this exact pin.
The older mirror retains HEAD ddbdd16 and441 of442 initial fingerprints; its
only changed initial file receives the same two verified text pins. Three
previously absent files are copied byte-identically, giving445 dirty paths.
No mirror commit, reset, push, dependency install, real-save or Release change.
ROM-free wrapper and Windows byte-compilation checks pass in both tools copies.

Direct Graphify update refuses18,787 proposed versus40,556 retained nodes.
Preserve19,398 nodes from2,972 excluded-but-existing files; do not force shrink
or install a new version. Record the incremental hook/post-bank receipts below.

Next, inspect the fresh remaining list and the complete caller/owner of
`func_15142314` (49 words,34 real differences, `game_16EE20`). The preceding
32-word `func_150A76F0` candidate is handwritten and returns through v0 with
nonstandard live registers; it needs assembly-boundary review, not ordinary
C-ABI conversion. Do not infer its convertibility from the sorted score alone.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m unittest tools.tests.test_game_matrix_reflection_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Post-Bank Verification

Consumer **23fa40a6425e15b6fd9afaf974f599d93abdb6a3** banks the installed
source/guards, aggregate-only README changes, documentation and exact tools
**5c4c157b3534695444588e479d67f0d5ed80fb1c** pin. Both active checkouts are clean.
Six fresh post-bank checks pass **in4.209s**: complete shape/word identity,
literal whole-image accounting, full private return state, effective whole-image
corruptions and both protected text/data tests. The full21-check receipt stays
separate. Guard history, conversion CSV and all protected Game data remain fixed.

The first incremental hook completes **40,565 nodes /81,053 edges** with no
remaining worker at observation. It preserves the excluded-but-existing history,
direct shrink refusal and oversized-HTML limitation rather than bypassing them.
All five new index links resolve. No push or frozen host Release work.

The next routine is the fixed/float translation accessor at
`conker/src/game_16EE20.c:452`; original assembly is
`conker/asm/nonmatchings/game_16EE20/func_15142314.s`, not a generated whole-slice
assembly file. Before any next-function edits, current source SHA-256 is
`7acc24c75dc922e9aa72027a030b4c8e43b0d2a2d9bc5f8c2a17fccb3dba7810`;
assembly SHA-256 is
`8f81a8658a1d949078601a100688508a5c52b329afdded05c59821b77bba3f53`.
Inspect signed halfword conversion order, output aliases and its real callers
before changing the body. No next-function source modification is banked here.
The full Game goal remains active with1,998 still-different converted functions.
