# Init Scan Deficit O1 Full Masked CU1 Set Corpus

Date: 2026-10-04. Starting HEAD: `d7df5452`.

## Scope

Matching CU1-set qualification for the Note 892 opt-in scan-deficit candidate.
Source/configuration match the CU1-clear run in
[Note 893](893-init-scan-deficit-o1-full-masked-cu1-clear-corpus-20261004.md).
Setup freshly compiles six shapes, then selects exactly packed O1. The fixture
retains the live-SP write fence and pre-adapter-return callee-register guard.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o1 python3 -m unittest tools.tests.test_init_decompressor_builder_scan_deficit.InitDecompressorBuilderScanDeficitCorpusTests -v -f
```

All 507 retail DMA-rounded pages are paired with reference execution and
pristine-image output. Inherited comparisons require compiled-core execution
without original-core fallback and check output/result, architectural context,
final FPR/GPR state and guarded storage/callee preservation. This is bounded
guest/model evidence, not hardware timing, complete stack ownership or gameplay.

## Result

All 507 paired pages pass in 971.161 seconds, no skips, process exit zero.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o1 cu1=set pages=507 text=5984 depth=3200 low=0x80031D90 margin=128
shadow corpus complete: modes=set runs=507
Ran 1 test in 971.161s
OK
```

Linked text 5,984, descent 3,200, minimum SP `0x80031D90` and known-neighbor
clearance 128 match Note 893. Observed descent equals the static packed O1
bound. The neighbor boundary is `0x80031D10`; margin and the write-only live-SP
fence do not prove reservation ownership or absence of below-SP reads.

Together Notes 893/894 qualify 1,014 paired pages across both masked CU1 modes
for unchanged scan-deficit packed O1. They do not qualify changed-option O2.
The prior default O2 evidence remains scoped to its default configuration.

## Supporting Checks And Integrity

Twenty-six ledger/selection, FR=1 word-load, scan-domain/branch/dependency and
exception/storage tests pass in 5.760 seconds, no skips. With the corpus,
twenty-seven tests pass without skips. The whole bounded suite in Note 892
is prior evidence, not rerun here.

All six source hashes recorded in Note 893 match before and after this run;
scoped source diffs are empty. No source or configuration edits occurred during
qualification. Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 guarded packed O1 masked CU1-clear pages (Note 893).
- [x] All 507 guarded packed O1 masked CU1-set pages.
- [ ] Changed-option O2 qualification if selected for further fitting.
- [ ] Best-profile fitting, full reservation, entry/frame ownership and hardware/context.

No production conversion, ROM build or sibling-port test is claimed. Best
default O2 remains 4,576 / 592 excess. Production Init, README totals and
unrelated Game source/tests remain unchanged and excluded from staging.
