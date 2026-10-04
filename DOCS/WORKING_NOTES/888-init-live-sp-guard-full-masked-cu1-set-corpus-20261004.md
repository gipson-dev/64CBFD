# Init Live SP Guard Full Masked CU1 Set Corpus

Date: 2026-10-04. Source baseline: `43a2cb40` (unchanged Note 886 fixture).

## Selection

This is the matching CU1-set corpus for
[Note 887](887-init-live-sp-guard-full-masked-cu1-clear-corpus-20261004.md).
It uses the direct-load adapter with LiveStackWriteFixture, core-owned state,
callee-preserving core and first-refill lookup. All nine source hashes match
Note 887 before execution. Candidate and oracle sources are unchanged.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_live_stack_writes.InitDecompressorLiveStackWriteCorpusTests -v -f
```

Setup freshly compiles/links all six shapes, checks empty logs and selects
exactly one packed-remaining O2/g3 image. Status is 0x2400FF00: FR/CU1 set,
IE/EXL clear. Adapter body/aligned text is 192/192 bytes, state 116 bytes,
extra stack area 0x98. Core flags and adapter symbols match Note 887.

## Evidence Scope

The live-SP fixture checks each private-stack write after the executed stack
switch against current SP. Callee-return and state-poison/read-before-init
guards remain active. The inherited paired comparison checks output/result
length, return register, scratch/result and final FPRs, final GPR/status,
doubleword FPR receipts, semantic state, physical frame scratch, changed
workspace/output, caller context, rounded DMA read extent, static stack bound
and known-neighbor writes. Executed compiled core/adapter and no original-core
fallback are required; each page uses pristine reference output.

This is architectural-value guest qualification, not full retail stack
reservation, arbitrary alias behavior, hardware timing, scheduler resume,
retail slot ownership or byte-exact C replacement. The live-SP fence is
write-only. Ordered LWC1 word traces are not separately asserted per page.
Previous unguarded Notes 880/881 remain scoped to their original fixture.

## Result

All 507 paired pages pass in 804.839 seconds. Process exit is zero with
one passed test and no skips. Linked text is 4,576 bytes, 592 over retail.
Maximum observed descent is 3,240 bytes, matching the static bound;
minimum SP is 0x80031D68 and known-neighbor clearance is 88 bytes.
These match Note 887's CU1-clear receipt.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4576 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 804.839s
OK
```

Together Notes 887/888 qualify 1,014 paired pages across both masked modes
for the unchanged packed O2/g3 direct-load candidate with live-SP and
callee-return guards. Time is host harness time, not hardware performance.

## Supporting Checks

Twenty-six ledger/selection, FR=1 word-load, live-SP boundary/corruption,
callee-clobber and exception/storage regressions pass in 11.930 seconds,
no skips. Instruction-clobber controls are rejected across six fresh builds;
live-SP injection runs both masked modes. Synthetic controls are not extra
corpus pages. Note 886's whole bounded suite is prior evidence, not rerun here.
With the corpus test, twenty-seven tests pass without skips. All nine source
hashes match Note 887 after completion, with empty scoped diffs. Project
tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 matching live-SP-guarded CU1-clear pages (Note 887).
- [x] All 507 current guarded CU1-set pages.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

No production conversion, ROM build or sibling-port test is claimed.
Candidate/production sources, profiles, word guards and README totals remain
unchanged; unrelated Game source/tests are preserved and excluded from staging.
