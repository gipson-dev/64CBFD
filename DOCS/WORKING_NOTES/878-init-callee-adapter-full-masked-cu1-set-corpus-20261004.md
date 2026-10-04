# Init Callee Adapter Full Masked CU1 Set Corpus

Date: 2026-10-04. Source baseline: `777c6e8d` (unchanged Notes 873/875).

## Selection

This is the matching CU1-set corpus for
[Note 877](877-init-callee-adapter-full-masked-cu1-clear-corpus-20261004.md).
The retained core uses first-refill lookup and the adapter omits duplicate
callee reloads. Exit-predicate and pointer-ownership trials remain absent.
No decoder, adapter, compiler or test source changes during this run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_callee_preserving_adapter.InitDecompressorCalleePreservingAdapterCorpusTests -v -f
```

Status is 0x2400FF00: FR/CU1 set, IE/EXL clear. Setup freshly compiles and
links all six shapes, checks empty compiler/link logs, then selects exactly
one packed-remaining O2/g3 image. Core flags, adapter symbols and all six
recorded source blob IDs match Note 877. Adapter body/aligned text is 256/256,
state is 116 bytes and extra stack area remains 0x98.

## Evidence Scope

The unchanged CalleePreservingFixture checks S0-S7, GP and FP at the
compiled core return boundary on every page, before any later restoration
could hide a clobber. It retains core-owned state poison/read-before-init
guards. Paired retail and compiled-context executions compare each page
against the reference image, using the 16-byte-rounded DMA input extent.

The inherited comparison checks output/result length, return register,
scratch/result/all final FPRs and GPRs, status and FPR transfer receipts,
semantic state, physical frame scratch, changed workspace/output and caller
context, DMA read limit, static stack bound and known-neighbor write guard.
It requires executed compiled core/adapter and no original-core fallback.

These are guest-model executions on real corpus data. Hardware timing, full
stack reservation, arbitrary alias behavior, retail slot ownership,
byte-exact matching and scheduler resume are not established by this run.

## Result

All 507 paired pages pass in 792.002 seconds. The process exits zero with
one passed test and no skips. Linked text remains 4,640 bytes, 656 over
retail. Maximum observed descent is 3,240 bytes, matching the retained
static bound, minimum SP 0x80031D68 and known-neighbor clearance 88 bytes.
These match Note 877's CU1-clear run.

Together Notes 877/878 qualify 1,014 paired page executions across both
masked modes for the unchanged current packed-remaining O2/g3 combination,
including the per-page callee-return guard. Earlier Notes 871/872 remain
scoped to their previous core/adapter baseline.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4640 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 792.002s
OK
```

Elapsed time is host test-harness time, not guest/hardware performance.

## Supporting Checks

Sixteen helper/ledger/selection and executed-clobber guard tests pass in
5.219s, no skips. The S0-clobber injection is rejected across six fresh
builds. Selection tests are synthetic controls, not additional corpus pages.
Note 875's whole bounded suite is prior evidence and is not rerun here.
With the corpus test, seventeen tests pass without skips. Scoped source
diff checks pass and all six source blob IDs still match Note 877 after
completion. Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 current-combination masked CU1-clear pages (Note 877).
- [x] Finish all 507 matching masked CU1-set pages.
- [ ] Continue size fitting, entry ownership and hardware/context/reservation gates.

No production ROM build or sibling-port test is claimed. Production sources,
defaults, progress CSV and README totals remain unchanged; unrelated Game
source/tests are preserved and excluded from staging.
