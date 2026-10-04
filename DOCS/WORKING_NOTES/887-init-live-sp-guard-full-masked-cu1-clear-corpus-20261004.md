# Init Live SP Guard Full Masked CU1 Clear Corpus

Date: 2026-10-04. Source baseline: `f14e6c8a` (Note 886).

## Selection

This is the full masked CU1-clear corpus for the direct-load adapter with
the separate LiveStackWriteFixture from
[Note 886](886-init-live-sp-write-fence-and-negative-qualification-20261004.md).
Candidate code and options remain unchanged; only the stronger fixture is
selected. Setup freshly compiles and links all six shapes, checks empty
logs, then selects exactly packed-remaining O2/g3.

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_live_stack_writes.InitDecompressorLiveStackWriteCorpusTests -v -f
```

Status is 0x0400FF00: FR set, CU1/IE/EXL clear. Adapter body/aligned text
is 192/192 bytes, state is 116 bytes and extra stack area 0x98. First-refill
lookup, table-derived allocation and callee-preserving core remain selected.

## Evidence Scope

The live-SP fence arms after the executed retail private-stack switch and
checks each write intersecting the modeled stack interval against current
SP. The inherited comparison also checks output/result length, scratch/result
and final FPRs, final GPR/status, doubleword FPR transfer receipts, semantic
state, physical frame scratch, changed workspace/output, caller context,
DMA read limit, static stack bound and known-neighbor writes. Callee-return
and core-state poison/read-before-init guards remain active on every page.
Executed compiled core/adapter and no original-core fallback are required.
Each page uses its rounded DMA extent and pristine output reference.

This is architectural-value guest execution. It does not establish the
complete retail stack reservation, general aliasing, hardware timing,
scheduler resume, retail entry/slot ownership or byte-exact C replacement.
The new guard fences writes only; below-SP reads are not checked by it.
Ordered LWC1 word traces remain separate from the doubleword receipts and
are not independently asserted per corpus page.

## Source Blobs

| Source | Git blob |
| --- | --- |
| `init_decompressor_semantic.c` | `bdc96bf5835c86bdd67a495e60f8a5b63cbe9071` |
| `init_decompressor_core_adapter.s` | `68f9ede617a36aebe706b6b30feed89dcfef7b4f` |
| `compile_init_decompressor.py` | `172d1b0e2db511d1f9702dd391e07114e4af3c83` |
| `test_init_decompressor_live_stack_writes.py` | `b78e5e609ed103ae51e6f0db0a0c7e2f17ac946c` |
| `test_init_decompressor_direct_fpr_adapter.py` | `96e59d42e9f37c97b896fab9a4d971b7a425ba28` |
| `test_init_decompressor_callee_preserving_adapter.py` | `cb293757461878a03db110ef7d631b0fe89221e9` |
| `test_init_decompressor_exception.py` | `f97bbcb5f67fc4a99e0073635ea35b26153a9597` |
| `test_init_decompressor_guest_adapter.py` | `4e73863ec88a6630e0ca7908276873240aa6bdcf` |
| `test_init_decompressor_shadow_corpus.py` | `d2a3f155672616bbeb3033a9f73e5bdce43a59fa` |

## Result

All 507 paired pages pass in 806.976 seconds. Process exit is zero with
one passed test and no skips. Linked text is 4,576 bytes, 592 over retail.
Maximum observed descent is 3,240 bytes, matching the static bound;
minimum SP is 0x80031D68 and known-neighbor clearance is 88 bytes.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4576 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 806.976s
OK
```

This is the first complete live-SP-guarded CU1-clear receipt. Matching
guarded CU1-set remains open. Time is host harness time, not guest or
hardware performance measurement.

## Supporting Checks

Twenty-six ledger/selection, FR=1 word-load, live-SP boundary/corruption,
callee-clobber and exception/storage tests pass in 12.349 seconds, no skips.
Negative instruction injections are rejected across all six builds; live-SP
corruption runs both masked modes. Synthetic controls are not extra corpus
pages. Note 886's whole bounded suite is prior evidence, not rerun here.
With the corpus test, twenty-seven tests pass without skips. All nine
recorded source blobs still match after completion, with empty scoped
diffs. Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 live-SP-guarded masked CU1-clear pages.
- [ ] All 507 matching guarded CU1-set pages.
- [ ] Further fitting: linked candidate remains 592 bytes over retail.
- [ ] Complete reservation, entry/frame ownership and hardware/context gates.

Notes 880/881's paired corpus receipts remain scoped to the old fixture
without this guard. No production conversion, ROM build or sibling-port
test is claimed. Candidate code, production sources, profiles, word guards
and README totals remain unchanged; unrelated Game edits are preserved.
