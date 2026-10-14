# Matrix Translation Guarded Byte Match

Date: 2026-10-13. Finish `func_15142314` from
[Note 1095](1095-game-matrix-translation-qualified-recovery-20261007.md), after
[Note 1345](1345-game-matrix-reflection-guarded-byte-match-20261013.md).
VA `0x15142314..0x151423D8`, ROM `0x16F7C4..0x16F888`:49 words /196 bytes,
frame zero. The wider Game matching goal remains active.

## Scope And Source

Consumer baseline `e21e1106a906766d09f025b735ca3c5d7504abba`; tools baseline
`5c4c157b3534695444588e479d67f0d5ed80fb1c`. The recovered C body already lives
at `conker/src/game_16EE20.c:452`. It remains completely unchanged: source
SHA-256 `7acc24c75dc922e9aa72027a030b4c8e43b0d2a2d9bc5f8c2a17fccb3dba7810`.
Retain its single byte flag read, unsigned32 wrapped matrix indexing, separate
signed-halfword conversions, power-of-two scaling and sequential XYZ stores.

The prior152-form source screen and26 typed/backend controls remain unchanged.
Their retained receipts are not reported as newly run tests. A fresh normal
O2/g3/MIPS2 compile still emits49 words/frame0/no pool/34 differences. Original
and selected arithmetic registers already agree; the differences are scheduling.
No source, header, compiler-profile, ABI, layout or conversion-row edit is needed.

New tools:

- `experiments/game_matrix_translation_matching.py`
- `tests/test_game_matrix_translation_match.py`

## Source-Derived Schedule

The complete unrelocated196-byte source payload is pinned to SHA-256
`d18460a4fd940873c915b3896f1dbf3b1f8b5a7220fc65946c8ad55672e3c950`.
Require both exact HI16/LO16 `D_800C3E90` relocations at offsets0/4. Linked
identity canonicalizes only these relocation fields; no relocation moves.

Derive34 expected-word guards solely from emitted source instructions:

- Hoist the existing scale LUI from word10 to word3 and its FP transfer from
  word14 to word6. Preserve the repeated shift/address instructions.
- Convert word4's zero-test branch-likely to an ordinary zero-test branch;
  derive its new displacement from the existing float block. Put the source's
  common address operation in the delay slot on both paths.
- The likely delay load and the unreachable float-block load are identical.
  Retain the latter as the float path's first load instead of performing the
  former in a branch delay. This restores original fault/scratch timing.
- Close the scale-materialization gap, put the last fixed store before JR and
  reuse the emitted no-op as the now-empty return delay.

All49 normalized words match retail. This deliberately changes the likely
branch opcode/displacement and replaces its duplicate load location with the
recovered schedule; it is not merely a register rename. No retail bytes feed
guard generation, no literal instruction template substitutes for the C body,
and no manifest insertion/omission changes the49-word extent. Raw C remains
34 words different: **guarded byte-exactness**, not direct compiler matching.

## Qualification

The initial14-test target/text suite passes in90.851s. Fresh owner-pool/full
parent checks pass separately in3.386s, and image-corruption qualification in
1.507s. The complete installed suite passes **17 tests in91.981s**:13 translation
checks, two protected text/data checks and two focused reflection regressions.

- 65,536 correlated guest tuples cover every signed-halfword pattern in each
  of six fields, all255 nonzero flags, ten wrapped indices and two stack phases.
  Compare independent exact-numerator RNE results, ordered public accesses,
  complete storage and complete normalized modeled return state.
- 20,576 edge/alias cases retain15360 fixed aliases,5120 float aliases and96
  flag/output aliases, including signed zero, subnormal, infinity and NaN bit
  copies. Check raw C storage/access effects as well as normalized full state.
- 66,816 actual native32 cases per profile execute the unchanged C at O2/O0.
  Native little-endian overlap/fence checks and the independent double-numerator
  reference remain separate from guest layouts and undefined legacy C.
- 1,152 connected cases execute all98 original parent words on its null and
  positive/negative-zero point routes, comparing full modeled states and actual
  forwarded inputs. Nonzero parent routes are not newly qualified here.
- All864 access cuts fire over96 domains; normalized states/dispatched words
  equal retail at every cut. Raw schedules differ at320 cuts, an effective
  negative control rather than an absent-output inference.
- Both complete owner padders retain89 functions /88 untouched neighbors,
  identical normalized pools and relocation maps. A pristine addressed owner
  inventory supplies only slice bounds to the strict padder; independent target
  assembly remains the original maintained `.s` file.
- Three independent original/raw/guarded layouts agree completely after
  normalization, including signed LO16 carry. All49 stale source words, all34
  stale expected guards, both missing relocations and every dropped guard are
  effective negatives. Whole-image/header/parent/source/guard corruptions fail.
- Preserve the seven compiled public-storage negatives for signed underflow,
  unsigned low halves, stride, exact-one gate, scale, snapshots and missing Z.

These are bounded RNE/model/native proofs, not the Cartesian six-field domain,
general FCSR/PC/BD/hardware timing, all parent routes or host/gameplay acceptance.
No extra Claude call, compiler installation, dependency update or REA setup.

## Installed Image And Counts

Append only34 rows to `conker/retail_word_patches.us.csv`:15,008 ->15,042,
with the historical manifest an exact byte prefix. Both source and original
assembly stay fixed; original assembly SHA-256 is
`8f81a8658a1d949078601a100688508a5c52b329afdded05c59821b77bba3f53`.

The standard linked ELF/progress build succeeds, recompiling shared guard
dependents with existing unrelated compiler/recipe warnings. The actual owner
retains its two existing pointer warnings. No ROM or host executable is built.

The complete ELF equals the archived image with only its196-byte target slot
replaced. Exactly **104 bytes change**, all inside that slot. Every symbol field,
address/extent, other body, pool, protected section and conversion CSV is fixed;
there is no metadata exclusion. All189,088 Game data bytes /720 owners remain
exact with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | `3ce90848e52416e7cfdf8ee344df140963443f82c84c46621ca42663acd2bf27` |
| Guards | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

Fresh totals: Game2,826/4,823 (58.59%), total3,499/5,496 (63.66%), different1,997,
drift0. Converted functions/bytes remain unchanged. Root README updates aggregate
rows only. After exact image proof, archive all nine text-fixture snapshots plus
their manifest under `matrix-translation-before-rebase/`; advance only ELF/guard
snapshots and two corresponding pins, preserving all other inputs/corruption gates.

## Banking And Next Work

Tools **4e3cd4c544ad79d2991faf30be37e3cad03c5912** banks the two new files and
verified two-line text-pin update first. The consumer records its exact pin.
Older tools retains HEAD ddbdd16 and444 of445 initial fingerprints; only its
protected text test receives the same two verified pins. Two absent files are
copied byte-identically, giving447 dirty paths, without mirror commits/reset.
ROM-free wrapper checks and Windows byte-compilation pass in both tools copies.
No push, save/configuration changes or frozen host Release work.

Direct Graphify update refuses18,788 proposed versus40,566 retained nodes.
Preserve19,398 nodes from2,972 excluded-but-existing files; do not force shrink
or update dependencies. Record incremental hook/post-bank results below.

Next `func_1506AA48`:VA `0x1506AA48..0x1506AAE0`, ROM `0x97EF8..0x97F90`,
38 words /152 bytes, original frame0x48, still a zero-return placeholder in
`conker/src/game/generated_97AA0.c:50`. Original assembly shows a16-byte actor/
selector/eight-byte payload packet, nine-slot creator call and conditional copy.
Inspect real argument widths, padding/home lifetimes and allocation-failure/alias
behavior before conversion. This next body is not edited in this checkpoint.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m unittest tools.tests.test_game_matrix_translation_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_matrix_reflection_match.GameMatrixReflectionMatchTests.test_01_shape_is_not_exact_matching \
  tools.tests.test_game_matrix_reflection_match.GameMatrixReflectionMatchTests.test_09_public_agreement_is_not_literal_private_frame_identity -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Post-Bank Verification

Consumer **ff5a124407474ca5cb359d69e1b0747a11f40f00** banks the34 guards,
aggregate-only README rows, documentation and exact tools
**4e3cd4c544ad79d2991faf30be37e3cad03c5912** pin. Both active checkouts are clean.
Six fresh post-bank checks pass **in4.434s**: complete shape/word identity,
literal whole-image/source accounting, all864 fired cuts, effective image
corruptions and both protected text/data checks. The full17-check receipt is
separate; source, all symbol fields and conversion rows stay unchanged.

The first incremental hook completes **40,575 nodes /81,062 edges** with no
remaining worker at observation. Retained history, direct shrink refusal and
oversized-HTML limits are preserved. All five new index links resolve.
No push, dependency install, real-save or frozen host Release work.

Next-function baseline fingerprints: `conker/src/game/generated_97AA0.c`
SHA-256 `23b0c8294804b32d6cafef604dc9fe48d366b19c5effbe831be2b53c8a0f6541`;
`conker/asm/97AA0.s`
SHA-256 `875b01a1301468f097ce947456ebee3e669675903aa2bd324ba1675883820109`.
Keep the next38-word creator/copy routine unmodified until its complete actor/
selector/payload/padding contract is qualified. The wider Game goal remains
active with1,997 still-different converted functions.
