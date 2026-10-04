# Init Callee Adapter Full Masked CU1 Clear Corpus

Date: 2026-10-04. Source baseline: `59d050ea` (unchanged Notes 873/875).

Follow-up: [Note 878](878-init-callee-adapter-full-masked-cu1-set-corpus-20261004.md)
passes the matching CU1-set corpus with unchanged source. Together these
receipts cover 1,014 paired pages across both masked modes for the current
packed-remaining O2/g3 core/adapter combination.

## Selection

This qualifies the retained first-refill lookup core plus callee-preserving
adapter, not the earlier Notes 871/872 combination. Discarded exit-predicate
and pointer-ownership trials are absent. No decoder, adapter, compiler or
test source changes during the run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_callee_preserving_adapter.InitDecompressorCalleePreservingAdapterCorpusTests -v -f
```

The status is 0x0400FF00, FR set with CU1/IE/EXL clear. Setup freshly
compiles/links all six shapes, requires empty compiler/link logs, then selects
exactly one packed-remaining O2/g3 image. The full core configuration from
Note 871 additionally selects `--lookup-first-refill` from Note 873.
Adapter symbols are INIT_DECODE_ABI_FPR_SHADOW=1,
INIT_DECODE_CORE_OWNS_STATE=1 and INIT_DECODE_CORE_PRESERVES_CALLEE=1.
State is 116 bytes, adapter body/aligned text 256/256, extra stack area 0x98.

Git blob IDs captured before completion (paths relative to repository):

| Path | Git blob |
| --- | --- |
| tools/experiments/init_decompressor_semantic.c | bdc96bf5835c86bdd67a495e60f8a5b63cbe9071 |
| tools/experiments/init_decompressor_core_adapter.s | cdaa455b5ce7e7476afa7cefbc0ca16d50209358 |
| tools/experiments/compile_init_decompressor.py | 172d1b0e2db511d1f9702dd391e07114e4af3c83 |
| tools/tests/test_init_decompressor_lookup_first_refill.py | a42e4efe7debfe27b4198eaf10d72a29371c678d |
| tools/tests/test_init_decompressor_callee_preserving_adapter.py | cb293757461878a03db110ef7d631b0fe89221e9 |
| tools/tests/test_init_decompressor_shadow_corpus.py | d2a3f155672616bbeb3033a9f73e5bdce43a59fa |

## Evidence Scope

Each of the 507 ROM chunks and expected decompressed pages is verified against
the reference image. Paired retail and freshly compiled executions use the
caller's 16-byte-rounded DMA input extent. The comparison checks output and
length, return register, result/scratch/all final FPRs and GPRs, status/write
traces, FPR save/load receipts, ten state fields, frame through offset A44,
changed output/workspace bytes and caller context, DMA read limit, static
stack bound and neighboring-thread write protection. It requires executed
compiled core/adapter and forbids fallback to the original core.

CalleePreservingFixture additionally compares S0-S7, GP and FP at the
compiled core's return PC (unique adapter JAL + 8) against adapter-entry
values, before any later restoration can hide a clobber. It retains the
core-owned state poison/read-before-initialization guard. This fixture is
selected for every corpus page, not only the standalone negative test.

These are guest-model/context checks on real corpus data, not hardware
interrupt timing, full stack reservation, arbitrary alias behavior, retail
slot ownership, byte-exact matching or scheduler-resume proof.

## Result

All 507 paired pages pass in 839.425 seconds. The process exits zero with
one passed test and no skips. Linked text is 4,640 bytes, 656 over retail.
Maximum observed descent is 3,240 bytes, matching the retained static bound;
minimum SP is 0x80031D68 and known-neighbor clearance 88 bytes.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4640 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 839.425s
OK
```

This is the first full CU1-clear receipt for the current first-refill and
callee-preserving adapter combination. It does not assign older CU1-set
receipts to this source. Elapsed time is host test-harness time, not guest
or hardware performance measurement.

## Supporting Checks

Sixteen helper/ledger/selection and executed-clobber guard tests pass in
4.831s, no skips. The negative guard injects an S0 clobber into the verified
compiled-core return delay-slot NOP and rejects it across six builds.
Selection tests are synthetic controls, not extra corpus pages. Note 875's
whole bounded suite remains prior evidence, not rerun here.
Together with the corpus test, seventeen tests pass without skips. Scoped
source diff checks pass and all six recorded blob IDs are unchanged after
the terminal result. Project tool and whitespace checks pass.

## Remaining Gates

- [x] Finish all 507 current-combination masked CU1-clear pages.
- [x] Qualify the matching current-combination masked CU1-set corpus (Note 878).
- [ ] Continue size fitting and entry ownership/hardware/context/reservation gates.

No production ROM build or sibling-port test is claimed. Production sources,
defaults, progress CSV and README totals remain unchanged; unrelated Game
source/tests are preserved and excluded from staging.
