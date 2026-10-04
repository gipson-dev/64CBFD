# Init Offset Sum Full Masked CU1 Clear Corpus

Date: 2026-10-03. Source baseline: `32a57ec3`.

Follow-up: [Note 863](863-init-offset-sum-full-masked-cu1-set-corpus-20261003.md)
banks the matching CU1-set run with unchanged source. Together they cover
1,014 paired pages across both masked modes for packed/remaining O2/g3.

## Result

All 507 fresh packed/remaining O2/g3 paired retail-page comparisons pass
with exception-masked CU1 clear in 790.137 seconds. The test exits zero,
with one passed test and no skips. Linked text remains 4,736 bytes, 752
over retail. Maximum observed descent is 3,240 bytes, minimum SP
0x80031D68 and known-neighbor clearance 88 bytes.

This checkpoint qualifies the revised Note 861 packed/remaining O2/g3
combination, including dynamic repeat-value fill, running offset sum and
the reused `available` accumulator. Notes 856/857's older corpus receipts
do not cover these changes. The run selects exception-masked CU1 clear,
status 0x0400FF00, with FR set and IE/EXL clear. It is not a CU1-set receipt.
Production, defaults and README aggregate counts remain unchanged.

## Exact Selection

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_builder_offset_sum.InitDecompressorBuilderOffsetSumCorpusTests -v -f
```

The corpus setup freshly compiles/links all six shapes, verifies empty
compiler/link logs and then selects exactly one packed/remaining O2/g3
image. The packed base profile uses frame-backed, packed/aligned entries,
bounded builder shifts/length scan, no unroll, dynamic cursor, cached
counts/offsets and remaining-symbol cursor. Setup adds ABI FPR shadow;
the live inherited extra flags are:

```text
--loop-lookup --builder-histogram-cursor --fixed-length-cursor
--stream-masked-dispatch --stream-byte-rewind --packed-header
--stored-shared-lengths --dynamic-shared-repeats --abi-seed-cursor
--builder-simple-operation --dynamic-repeat-value --builder-offset-sum
```

Adapter setup also defines `INIT_DECODE_CORE_OWNS_STATE=1`, besides ABI FPR
shadow. The selected fixture is `CoreOwnedStateFixture`, and scratch-FPR
comparison is enabled. These configuration values were inspected live.
No compiler, experiment, adapter or test source changed during this run.

## Evidence Scope

For each of all 507 retail pages, the harness verifies the ROM chunk and
expected decompressed bytes against the reference image, then compares
retail assembly and the freshly compiled C core through the context adapter.
Each page uses the caller's 16-byte-rounded DMA input extent.

The active paired comparison checks:

- Expected output bytes and result length against the reference image.
- Return register, FPR results 16..19 and scratch FPRs 0..11.
- All final GPRs/FPRs, status, status-write sequence and FPR save/load receipts.
- Ten semantic state fields and frame scratch through offset 0xA44.
- Every changed output/workspace byte and the caller context region.
- Static call-stack bound, known-neighbor write guard and DMA read limit.
- Executed adapter and compiled-core entries, with no original-core visit.
- Poisoned core-owned fields initialized before their first read.

These are model-executed guest/context and real-data checks. They do not
prove hardware interrupt timing, the complete stack reservation, arbitrary
aliasing, retail slot ownership, byte-exact matching or scheduler resume.

Terminal corpus receipt:

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4736 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 790.137s
OK
```

The observed maximum equals the Note 861 static bound. The elapsed time
is host test-harness time, not a guest/hardware performance measurement.

## Supporting Checks

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection -v
wsl make tools-check
git diff --check
```

The fifteen helper/selection tests pass in 0.062 seconds with no skips.
Together with the full-corpus test, sixteen tests pass with no skips.
Tool and diff checks pass.
Corpus-selection orchestration tests are synthetic controls, not additional
MIPS page executions. The Note 861 bounded suite is prior evidence and is
not presented as rerun here. No production build or sibling-port test is
claimed; unrelated Game edits remain preserved and excluded.

## Next

- [x] Bank all 507 revised-combination masked CU1-clear page comparisons.
- [x] Run all 507 pages for the same source/profile with masked CU1 set (Note 863).
- [ ] Return to builder/shared-helper fitting; revised linked text remains over retail.
- [ ] Complete other-profile, ownership, hardware and scheduler-resume gates before promotion.
