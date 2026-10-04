# Init Allocation Table Full Masked CU1 Clear Corpus

Date: 2026-10-04. Source baseline: `cf9c1afd` (unchanged Note 867 experiment).

## Selection

This run qualifies the current table-derived allocation combination, not the
older Note 861 source covered by Notes 862/863. It adds reversed-code toggle,
parent-ascent cursor and table-derived allocation to that earlier combination.
Rejected helper inlining and stride capture are absent. No experiment,
adapter, compiler or test source changes during the run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_builder_allocation_table.InitDecompressorBuilderAllocationTableCorpusTests -v -f
```

Selection is packed-remaining O2/g3, exception-masked CU1 clear, status
0x0400FF00: FR set, IE/EXL clear. The setup freshly compiles and links all
six shapes, verifies empty compiler/link logs and then selects exactly one.
Complete retained configuration:

```text
--frame-backed --packed-entry --bounded-builder-shifts --no-unroll
--bounded-length-scan --dynamic-cursor --cache-builder counts-offsets
--builder-symbol-cursor remaining --abi-fpr-shadow --loop-lookup
--builder-histogram-cursor --fixed-length-cursor --stream-masked-dispatch
--stream-byte-rewind --packed-header --stored-shared-lengths
--dynamic-shared-repeats --abi-seed-cursor --builder-simple-operation
--dynamic-repeat-value --builder-offset-sum --builder-code-toggle
--parent-ascent-cursor --builder-allocation-table
```

The adapter defines INIT_DECODE_ABI_FPR_SHADOW=1 and
INIT_DECODE_CORE_OWNS_STATE=1; fixture is CoreOwnedStateFixture with scratch
FPR comparison enabled. The state remains 116 bytes, adapter 296 body /
304 aligned bytes, and adapter extra stack 0x98.

## Evidence Scope

Every page's chunk and expected output are checked against the retail ROM
and reference image, with the caller's 16-byte-rounded DMA extent. Paired
retail-assembly and compiled-C/context-adapter executions compare:

- Expected output bytes, result length and return register.
- Result FPRs 16..19 and scratch FPRs 0..11.
- All final GPRs/FPRs, status/write sequence and FPR save/load receipts.
- Ten semantic state fields and frame scratch through offset 0xA44.
- Changed output/workspace bytes and caller context region.
- Static call-stack bound, neighboring-thread write guard and DMA read limit.
- Executed compiled core/adapter, with no visit to the original core.
- Poisoned core-owned fields initialized before first read.

These checks are guest-model executions on real corpus data. They are not
hardware interrupt timing, full stack reservation, arbitrary aliasing,
retail slot ownership, byte-exact matching or scheduler-resume proof.

## Result

All 507 paired pages pass in 798.099 seconds. The test exits zero with one
passed test, no skips. Linked text is 4,704 bytes, 720 above retail. Maximum
observed descent is 3,240 bytes, minimum SP 0x80031D68, known-neighbor margin
88 bytes. The maximum matches the retained static bound.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4704 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 798.099s
OK
```

This is the first full current-combination CU1-clear receipt. It does not
reassign the older CU1-set receipt to the changed combination. Host elapsed
time is test-harness time, not guest/hardware performance measurement.

## Supporting Checks

Fifteen call-graph, slot-ledger and corpus-selection tests pass in 0.124s
with no skips. Selection tests are synthetic controls, not extra guest pages.
Combined with the corpus test, sixteen tests pass, no skips. Experiment,
compiler, adapter and selected test sources remain unchanged, verified by
scoped `git diff --exit-code`. Tool and whitespace checks pass.
The Note 870 bounded suite is prior evidence and is not rerun here. No
production ROM build or sibling-port test is claimed. Production sources,
defaults and README counts remain unchanged; unrelated Game edits preserved.

## Remaining Gates

- Full current-combination masked CU1-set corpus remains required.
- Size fitting remains required before production promotion.
- Entry ownership, complete stack reservation and hardware/context boundaries
  remain separate requirements, regardless of corpus success.
