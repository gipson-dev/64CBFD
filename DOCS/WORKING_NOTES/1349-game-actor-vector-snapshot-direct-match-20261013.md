# Actor Vector Snapshot Direct Match

Date: 2026-10-13. Continue
[Note 1348](1348-game-signed-actor-mask-scan-direct-match-20261013.md) with
`func_1506A79C`: VA `0x1506A79C..0x1506A83C`, ROM `0x97C4C..0x97CEC`,
40 words / 160 bytes, original frame `0x38`. The wider Game goal stays active.

## Baseline And Recovered Body

Consumer baseline `ab0d210848b52fffeb87c6ea992a571e510400db`; tools baseline
`3d885558514938441c293596a4163b8dc1a15d7a`. Production was a zero-return
placeholder in `conker/src/game/generated_97AA0.c`.

Recover the void actor callback and unused 32-bit second argument. Copy the
three actor coordinates at offsets 0x14/0x18/0x1C into a private position array.
Compute the three components of `D_800D1570 - D_800D1560` into a second private
array. Submit `func_151D3480(position, difference, NULL, 0, 255, 1)`.

Both arrays contain three f32 values. Preserve the owner's existing byte-array
global declarations and access the aligned float fields explicitly. The callee's
opening confirms two vector pointers, an optional pointer and byte-selected
mode behavior. This callback does not introduce a pointer-return C contract;
the incidental guest v0 residue remains instruction evidence only.

## Direct Compiler Match

New tools:

- `experiments/game_actor_vector_snapshot_candidates.py`
- `tests/test_game_actor_vector_snapshot_match.py`

24 real source shapes across four existing profiles give 96 measurements.
The plain, nonvolatile position-first array body matches **all 40 words directly
from C**, frame `0x38`, no pool/diagnostics and zero guards. The unused-second-
argument qualifier control also matches but is not installed.

Declaration order alone recovers position SP+0x2C and difference SP+0x20.
Reversing the real arrays retains 40 words/frame0x38 but fails eight private
offset words and a guest-private alias witness. Do not normalize those offsets.
Difference-first and interleaved assignments also remain nonmatching. O2 without
g3 emits 39 or 42 words; O1 emits 56. No profile or compiler changes are installed.

The original parameter homes at frame SP+0x38/SP+0x3C, RA at SP+0x1C, nine
floating input reads, all six private stores and call/return schedule emit
directly. The JAL is at offset 0x88; both global HI16/LO16 pairs remain intact.

One rejected profile hoists address/float work ahead of its SP adjustment at
word 11. The old first-word frame hint was therefore misleading, and the initial
eight-word scanner was insufficient. Decode the unique negative SP adjustment
across the complete measured routine in this target's wrapper. The completed
96-profile bank independently reports frame0x38 throughout. This repairs local
measurement, not emitted instructions or shared compiler tooling.

## Qualification

All **14 pre-install checks pass in 31.111s**. The complete installed suite
passes **16 checks in 49.161s**: twelve target tests, two protected text/data
checks and fresh direct-shape checks for the preceding creator and mask scan.

- 11,904 guest cases cover all 1,728 independent three-field actor bit patterns,
  every 16-by-16 finite numeric subtraction pair per axis, three provider modes
  and two SP phases. Compare all raw actor copies, nine ordered input reads,
  private snapshots, callback arguments, external storage and full modeled
  states against the independently written ordered reference. All 40 words
  are reached. Raw copied NaNs are not generalized arithmetic/FCSR acceptance.
- Sixty alias cases cover actors overlapping either global vector, both private
  arrays and incoming homes, plus each global vector rebased onto a private
  array or home. Independent original/source links agree. Preserve the retail
  read/store sequence; private aliases remain guest evidence, not portable C.
  Reuse identical alias links within a run rather than compiling them again
  for each provider mode; source/profile/symbol inputs are fixed in that cache.
- All 72 missing-input-byte prefixes fail before provider submission, with
  complete original/source states equal. There is no synthetic null-actor gate.
  The wrong real array order changes a private-aliased payload, not merely a
  difference count.
- Six compiled negatives are effective in guest and native execution: wrong
  actor coordinate, reversed subtraction, addition, swapped vectors, wrong
  mode and wrong slot.
- Native32 O2/O0 executes the actual typed source, **20,736 cases per profile**,
  including raw actor payloads, the guest-checked numeric grid, four backed
  public aliases, provider mutation and every byte of the three input arenas.
  SSE/RNE and 32-bit backed-pointer boundaries are explicit; no 64-bit port,
  other rounding modes or complete exception-state acceptance is claimed.
- Complete copied-owner compilation and both real padders preserve fifteen
  neighboring bodies, normalized pools and relative relocations. The earlier
  creator/mask remain direct matches. Target raw instructions survive padding.
- Twenty-four connected cases execute the original 38-word dispatcher, its
  actual vector setup and table index4. Verify all41 parent words against ROM,
  including the 12-byte alignment tail, plus the table word at `0x80086120` /
  ROM `0x22ABE0`. Both forwarded arguments and complete target coverage agree.
  The downstream 564-word vector provider is bounded, not emulated or qualified.
- Three independent original/source layouts qualify real HI/LO carry boundaries
  and the JAL with 72 semantic cases, full words and complete modeled states.
- All **792 own-instruction fault pairs /36 domains** actually fire and agree.
  The routine has 22 encoded accesses; provider reads/writes are not counted
  as encoded instructions. The wrong layout fails the cut8 state witness.
  Hardware PC/BD and complete FCSR remain outside this proof.
- Header, target, previous mask scan, image tail, source and guard corruption
  controls all trigger the literal-image gate.

The first native O2 fixture crashed. A read-only GDB run of that owned fixture
observed `movaps` at `0x08049348` with its stack destination misaligned by four
bytes. Archive the failed binary/source as `native-O2-before-stack-fix*` in the
ignored target directory. Apply the existing native-fixture `-mstackrealign`
convention, keeping SSE, warnings and all semantic gates enabled. Both O2/O0
and all six native negatives then pass. This is fixture-entry ABI repair, not
a production defect or a qualified receipt from the failed attempt.

Routine work uses zero Claude calls. No REA setup, dependency installation,
emulator, real gameplay or host Release work is performed.

## Installed Image And Counts

Install only the complete body and its required helper declaration. Preserve
original assembly, existing globals/types, all neighbors, ordinary O2/g3/MIPS2,
layouts and guard history. The normal linked ELF/progress build succeeds with
no new target diagnostics; the existing duplicate-recipe warning remains.
No ROM or host executable is built or launched.

The complete ELF equals the archived image with only the 160-byte target slot
replaced and its named size changed 12 ->160. Exactly **123 bytes differ**:
122 target code bytes and one size byte. Every other byte is fixed, without
blanket metadata exclusions. All 189,088 Game data bytes /720 owners remain
exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `5eabc37b7142d9d137ad5ffd5ba1be01f8dadd4f97bc4a0ae07a86a5c1fcf23b` |
| ELF | `15efd3983e27e174640763a68c61373320bc891173593bf619eea5a6d60fe14b` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

All 15,042 historical guard rows remain byte-identical; the target has none.
Fresh totals: Game **2,829/4,823 (58.66%)**, total **3,502/5,496 (63.72%)**,
different **1,994**, drift **0**. Converted functions/bytes remain fixed because
the false-C placeholder was already counted. Root README changes aggregate
rows only; function recovery belongs here.

After the independent literal image/corruption gates pass, archive all nine
protected text snapshots plus their manifest under
`actor-vector-snapshot-before-rebase/`. Advance only its ELF snapshot and the
single verified ELF pin in both tools copies. All other inputs, the guard pin
and every effective corruption control remain unchanged.

## Banking And Next Work

Tools **7222bfa6bc27df6e407d703422596b66f329f693** banks the two new files and
one-line text ELF-pin update first; the consumer records that exact pin.
Older tools keeps HEAD ddbdd16 and450 of451 initial fingerprints. Only its
protected text test gets the verified pin; two absent, byte-identical files
bring the dirty count to453. No mirror commit/reset or push. Both copies pass
ROM-free wrapper checks and Windows byte-compilation.

Direct Graphify update refuses18,819 proposed versus40,597 retained nodes,
preserving19,398 nodes from2,972 excluded-but-existing files. Do not force
shrink or install a different package. Record incremental hook/post-bank
receipts separately below.

Next `func_1506A864`: VA `0x1506A864..0x1506A968`, ROM `0x97D14..0x97E18`,
65 words /260 bytes, frame `0x60`, still a placeholder in the same owner.
It truncates actor coordinates, adds50 to Y before truncation, builds a compact
descriptor and eleven-slot `func_151602C0` call, then conditionally copies a
16-byte float block to result+0x18. Recover signed conversion bounds, descriptor
padding, the 0/80/0/global float block and allocation-failure/access behavior
before matching. This next body remains unmodified.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_vector_snapshot_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_vector_snapshot_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_actor_mask_scan_match.GameActorMaskScanMatchTests.test_01_direct_complete_slot_and_source_profile_bank \
  tools.tests.test_game_actor_payload_creator_match.GameActorPayloadCreatorMatchTests.test_01_complete_direct_slot_and_all_real_source_profiles -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
