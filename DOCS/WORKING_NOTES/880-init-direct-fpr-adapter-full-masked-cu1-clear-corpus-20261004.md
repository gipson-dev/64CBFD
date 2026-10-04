# Init Direct FPR Adapter Full Masked CU1 Clear Corpus

Date: 2026-10-04. Source baseline: `96a41088` (Note 879).

## Selection

This qualifies the opt-in direct-load adapter introduced in
[Note 879](879-init-direct-fpr-load-adapter-fitting-20261004.md), retaining
first-refill lookup, core-owned state and the callee-preserving core contract.
The new assembler symbol is `INIT_DECODE_DIRECT_FPR_LOADS=1`; the adapter
body/aligned text is 192/192 bytes, state 116 bytes, extra stack area 0x98.
No decoder, adapter, compiler or oracle source changes during the run.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_direct_fpr_adapter.InitDecompressorDirectFprAdapterCorpusTests -v -f
```

Setup freshly compiles and links all six shapes, checks empty logs and
selects exactly the packed-remaining O2/g3 image. Status is 0x0400FF00:
FR set, CU1/IE/EXL clear. Every page supplies the 16-byte-rounded DMA extent
and is compared against its corresponding reference image output.

## Evidence Scope

The inherited comparison checks output/result length, return register,
scratch/result and final FPRs, final GPRs/status, doubleword FPR transfer
receipts, semantic state, physical frame scratch, changed workspace/output,
caller context, DMA read limit, static stack bound and known-neighbor writes.
Executed compiled core/adapter and absence of original-core fallback are
required. The CalleePreservingFixture checks S0-S7/GP/FP at core return before
any later restoration; core-owned state poison/read-before-init guards remain.

These are architectural-value guest-model checks, not hardware timing,
full stack reservation, arbitrary alias behavior, byte-exact matching,
entry/retail slot ownership or scheduler-resume proof. New LWC1 word-load
traces are separate from the inherited doubleword receipt comparison;
their clean/dirty ordering was qualified in Note 879's bounded suite.
The full corpus does not assert those ordered word traces separately.

## Source Blobs

| Source | Git blob |
| --- | --- |
| `init_decompressor_semantic.c` | `bdc96bf5835c86bdd67a495e60f8a5b63cbe9071` |
| `init_decompressor_core_adapter.s` | `68f9ede617a36aebe706b6b30feed89dcfef7b4f` |
| `compile_init_decompressor.py` | `172d1b0e2db511d1f9702dd391e07114e4af3c83` |
| `test_init_decompressor_direct_fpr_adapter.py` | `96e59d42e9f37c97b896fab9a4d971b7a425ba28` |
| `test_init_decompressor_callee_preserving_adapter.py` | `cb293757461878a03db110ef7d631b0fe89221e9` |
| `test_init_decompressor_exception.py` | `f97bbcb5f67fc4a99e0073635ea35b26153a9597` |
| `test_init_decompressor_guest_adapter.py` | `4e73863ec88a6630e0ca7908276873240aa6bdcf` |
| `test_init_decompressor_shadow_corpus.py` | `d2a3f155672616bbeb3033a9f73e5bdce43a59fa` |

## Result

All 507 paired pages pass in 808.272 seconds. Process exit is zero with
one passed test and no skips. Linked text is 4,576 bytes, 592 over retail.
Maximum observed descent is 3,240 bytes, matching the static bound;
minimum SP is 0x80031D68 and known-neighbor clearance is 88 bytes.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4576 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 808.272s
OK
```

This is the first complete CU1-clear receipt for the smaller direct-load
adapter. Its matching CU1-set run remains open. Time is host harness time,
not a guest or hardware performance measurement.

## Supporting Checks

Eleven ledger/selection, FR=1 word-load and executed-clobber guard tests pass
in 5.275 seconds, no skips. The clobber gate rejects a modified compiled-core
return delay slot across all six fresh builds. Synthetic selection controls
are not additional corpus pages. Note 879's complete bounded suite remains
prior evidence, not rerun here.
Together with the corpus test, twelve tests pass without skips. All eight
recorded source blob IDs match after completion, with empty scoped source
diffs. Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 direct-load packed O2/g3 masked CU1-clear pages.
- [ ] All 507 matching masked CU1-set pages.
- [ ] Further fitting: linked decoder remains 592 bytes over retail.
- [ ] Entry/frame ownership, full reservation and hardware/context gates.

Notes 877/878 qualify the earlier 256-byte adapter only. No production
conversion, ROM build or sibling-port test is claimed. Production sources,
defaults, progress CSV and README totals are unchanged. Unrelated Game
source/tests are preserved and excluded from staging.
