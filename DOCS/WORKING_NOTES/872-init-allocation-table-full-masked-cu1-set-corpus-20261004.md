# Init Allocation Table Full Masked CU1 Set Corpus

Date: 2026-10-04. Source baseline: `7b628fa1` (unchanged Note 867 experiment).

## Selection

This is the matching CU1-set run for [Note 871](871-init-allocation-table-full-masked-cu1-clear-corpus-20261004.md).
The source/options include reversed-code toggle, parent-ascent cursor and
table-derived allocation. Older Notes 862/863 do not qualify this combination.
Rejected helper inlining and stride capture are absent. No compiler, decoder,
adapter or selected test source changes during the run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_builder_allocation_table.InitDecompressorBuilderAllocationTableCorpusTests -v -f
```

Status is 0x2400FF00: FR/CU1 set, IE/EXL clear. Setup freshly compiles and
links all six shapes, verifies empty compiler/link logs, then selects exactly
one packed-remaining O2/g3 image. Complete option set and evidence scope are
listed in Note 871. CoreOwnedStateFixture, scratch-FPR comparison and the
core-owned ABI-shadow adapter are unchanged.

Git blob IDs captured before qualification completes (paths relative to repo):

| Path | Git blob |
| --- | --- |
| tools/experiments/init_decompressor_semantic.c | 33179131122326450f91905eb57d6a19e3327cc8 |
| tools/experiments/init_decompressor_core_adapter.s | 7a6977cca452ac2c20b3bfef6debcb08bf515cc8 |
| tools/experiments/compile_init_decompressor.py | 05e30ee1c766dc0945103d88a96f869b6d472ad3 |
| tools/tests/test_init_decompressor_builder_allocation_table.py | b826ea9380aaf9eb78e2426ac412ff37b47574c3 |
| tools/tests/test_init_decompressor_shadow_corpus.py | d2a3f155672616bbeb3033a9f73e5bdce43a59fa |

## Result

All 507 paired pages pass in 804.532 seconds. The process exits zero with
one passed test and no skips. Linked text is 4,704 bytes, maximum observed
descent 3,240, minimum SP 0x80031D68 and known-neighbor clearance 88 bytes.
These match the CU1-clear run and retained static bound. Together Notes
871/872 qualify 1,014 paired page executions across both masked modes on
the unchanged current combination.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4704 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 804.532s
OK
```

Elapsed time is host test-harness time, not guest/hardware performance.

## Supporting Checks

Fifteen call-graph, slot-ledger and corpus-selection tests pass in 0.059
seconds, no skips. Selection tests are synthetic controls, not extra guest
page executions. Combined with the corpus test, sixteen tests pass without
skips. Source diff checks pass and all five blob IDs above are unchanged
after the terminal result. Project tool and whitespace checks pass.
The Note 870 bounded guest suite is prior evidence, not
rerun here. The corpus compares output, state/frame/memory effects, context,
FPR transfers, DMA bounds, known-neighbor protection and executed compiled
core/adapter without fallback to the original core, as detailed in Note 871.

## Remaining Boundaries

The retained packed O2 object ledger has 1,100 total core words against 996
retail decoder words, a 104-word core excess. The aligned adapter adds 76
words, yielding 180 words / 720 bytes total excess. The builder's 405-word
region includes a 333-word public body plus 22 ABI-capture and 50 lookup
helper words; its 293-word retail slot therefore has 40 public-body excess
words but 112 region excess words. Other named regions and wrapper/helper
accounting offset part of that excess. This is size accounting, not proof
that independent retail entry slots can be reassigned. The receipt inspected
is `conker/build/init-take-drop-restored-20261003/measurements.json` from
the unchanged retained source.

Even successful corpus qualification does not remove the 720-byte linked
text excess or prove retail slot ownership, hardware timing, arbitrary alias
behavior, complete stack reservation or scheduler resume. Size fitting and
those connected-contract requirements remain before production promotion.
No production ROM build or sibling-port test is claimed. Production sources,
defaults, progress CSV and README totals are unchanged; unrelated dirty Game
source/tests are preserved and excluded from staging.
