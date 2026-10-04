# Init Direct FPR Adapter Full Masked CU1 Set Corpus

Date: 2026-10-04. Source baseline: `f8dfe308` (unchanged Note 879 sources).

## Selection

This is the matching CU1-set corpus for
[Note 880](880-init-direct-fpr-adapter-full-masked-cu1-clear-corpus-20261004.md).
The selected adapter uses direct FPR word loads, core-owned state and the
callee-preserving contract; the core retains first-refill lookup.
Adapter body/aligned text is 192/192 bytes, state 116 bytes and extra
stack area 0x98. All eight source blobs match Note 880 before execution.
No decoder, adapter, compiler or oracle changes during this run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_direct_fpr_adapter.InitDecompressorDirectFprAdapterCorpusTests -v -f
```

Status is 0x2400FF00: FR/CU1 set, IE/EXL clear. Setup freshly compiles
and links all six shapes, checks empty logs, and selects exactly one
packed-remaining O2/g3 image. Core flags and adapter symbols match Note 880.
Each paired page uses the 16-byte-rounded DMA extent and reference image.

## Evidence Scope

The inherited checks compare output/result length, return register,
scratch/result and final FPRs, final GPR/status state, doubleword FPR
transfer receipts, semantic state, frame scratch, changed workspace/output,
caller context, DMA input limit, static stack bound and known-neighbor writes.
They require executed compiled core/adapter and no original-core fallback.
Each page checks S0-S7/GP/FP at core return before any later restoration;
core-owned-state poison/read-before-init guards remain active.

Ordered LWC1 word-load traces are separate from the inherited doubleword
receipts and are not separately asserted per corpus page; Note 879's bounded
clean/dirty checks qualify their order. This is architectural-value guest
execution, not hardware timing, full reservation, arbitrary alias behavior,
retail slot ownership, byte-exact matching or scheduler-resume proof.

## Result

All 507 paired pages pass in 790.940 seconds. Process exit is zero with
one passed test and no skips. Linked text is 4,576 bytes, 592 over retail.
Maximum observed descent is 3,240 bytes, matching the static bound;
minimum SP is 0x80031D68 and known-neighbor clearance is 88 bytes.
These match the CU1-clear receipt in Note 880.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4576 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 790.940s
OK
```

Together Notes 880/881 qualify 1,014 paired page executions across both
masked modes for this unchanged direct-load packed O2/g3 combination,
including the per-page callee-return guard. Time is host harness time,
not guest or hardware performance measurement.

## Supporting Checks

Eleven ledger/selection, FR=1 word-load and executed-clobber guard tests pass
in 5.115 seconds, no skips. The S0-clobber injection is rejected across
six freshly compiled builds. Synthetic selection controls are not corpus
pages. Note 879's whole bounded suite is prior evidence, not rerun here.
With the corpus test, twelve tests pass without skips. All eight source
blobs still match Note 880 after completion; scoped source diffs are empty.
Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 matching masked CU1-clear pages (Note 880).
- [x] All 507 current direct-load masked CU1-set pages.
- [ ] Further fitting, entry/frame ownership, hardware/context and reservation.

Notes 877/878 remain scoped to the earlier 256-byte adapter. Production
sources, defaults, progress CSV and README totals remain unchanged; no
production conversion, ROM build or sibling-port test is claimed. Unrelated
Game source/tests are preserved and excluded from staging.
