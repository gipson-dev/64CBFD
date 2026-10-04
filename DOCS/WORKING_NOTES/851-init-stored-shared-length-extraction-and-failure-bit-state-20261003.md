# Init Stored Shared Length Extraction And Failure Bit State

Date: 2026-10-03. Baseline: `57c6ac0`.

## Result

Opt-in `--stored-shared-lengths` uses the existing 16-bit extractor for both
stored length words. On a bad complement it restores 16 to the buffered bit
count before returning failure. This preserves retail's failure state: the
reservoir has shifted, but the complement's bit count has not been dropped.
The original manual second extraction remains the default.

All three O1 linked builds shrink by 32 bytes; frame O2 shrinks by 16.
Packed O2 stored body shrinks one word, but its final padding grows one word,
so best linked text stays 4,800 bytes, 816 above retail capacity. This is
alternate-profile/body fitting progress, not a reduction of the best packed
O2 total or a production conversion.

## Trials And Accounting

Trials add to the packed-header/stream/fixed-cursor/histogram baseline:

| Packed trial | O2 core text | O1 core text |
| --- | ---: | ---: |
| Note 850 baseline | 4,480 | 5,920 |
| Specialized eight-bit stored loop, rejected | 4,512 | 5,968 |
| Shared 16-bit extraction with inverse check, retained | 4,480 | 5,888 |
| Shared extraction with XOR check, rejected | 4,480 | 5,888 |
| Shared extraction with sum check, rejected | 4,480 | 5,888 |
| Arithmetic failure-count restoration, rejected | 4,496 | 5,904 |
| Shared inverse plus arithmetic builder operation, size-only | 4,480 | 5,872 |

The specialized byte loop plus arithmetic builder operation measured
4,512/5,936. All temporary byte/XOR/sum/arithmetic branches and selectors are
removed. The combined arithmetic-builder form has size evidence only here.
No semantic qualification is assigned to rejected or combined variants.

Packed O2 stored body/slot shrinks 55 to 54 words; core body stays 52, while
its slot grows 52 to 53. Packed O1 stored body/slot shrinks 74 to 67; core
body stays 81 and its slot shrinks 84 to 83: eight words / 32 bytes saved.
Stored frames remain 48/O2 and 40/O1; core-call bounds stay 408/344.

Ignored local receipts are under `conker/build/init-stored-byte-*`,
`init-stored-shared-*` and `init-stored-check-*`, suffixed `-20261003`.
A fresh omitted-flag build at `init-stored-shared-default-check-20261003`
reproduces 4,480/408 O2 and 5,920/344 O1 text/frame, with header layout (4,1).
That is not a fresh default full-corpus qualification.

## Qualified Costs

Final builds retain 116-byte state and the unchanged 320-byte adapter:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,032 | 3,280 | 3,280 |
| Frame O1 | 6,400 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,832 | 3,240 | 3,240 |
| Aligned/end O1 | 6,192 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,800 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,208 | 3,192 | 3,192 |

All stack bounds are unchanged. Packed O2 minimum SP remains `0x80031D58`,
72 bytes above the known protected neighbor. Neither this fence nor
successful fixtures prove complete reservation ownership or hardware faults.

## Failure-State Gate And Verification

The inherited domain passes 432 stream/context comparisons, 114 direct
builders, six exact initializers and 48 direct all-alignment/header-format
comparisons. Header layout rejection and actual LWL/LWR checks remain active.
Nested lookup and constructed byte-rewind gates retain their counts.

Twelve additional paired comparisons cover a bad stored complement across
six builds and both masked CU1 modes: 444 bounded stream/context comparisons
for this variant. Separate bad/valid executions in all six builds verify
the restoration instruction is active only on failure. Failure leaves bits
16, reservoir zero, input at the end of the seven-byte supplied chunk and
no output. The valid two-byte payload bypasses restoration, leaves bits zero
and returns `XY`; input/state/output checks pass.

The first active-store probe relied on PC visits and failed six subcases:
IDO had scheduled the store in a branch delay slot, which that counter does
not visit separately. The paired state checks passed. The corrected probe
observes executed instruction words and the actual state-field address/value,
including delay slots, and records pre-store register snapshots. Bad cases
record exactly one restoration to 16; valid cases record none.

The corrected isolated gate passes in 8.378 seconds. The entire finalized
module was then freshly rerun and passes cleanly:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_stored_shared_lengths
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
```

Final module: 23 tests in 201.411 seconds, 22 pass and one intentional
full-corpus skip. All thirteen call-analysis/slot-ledger tests also pass:
35 passed, one skip across these final commands. This supersedes the first
23-test run's delay-slot instrumentation failures (208.970 seconds).
Compiler/linker logs are empty; root `make tools-check` and `git diff --check`
pass. No production build, ordinary full-suite, new full corpus, hardware
replay or sibling-port test is claimed.

The final bit state and input-read sequence are preserved, but intermediate
C-state stores differ on failure: the extractor drops the count and the
failure path restores it. Asynchronous observation of that intermediate
state is not qualified. No prior full-corpus receipt is reassigned here.

## Next

- [x] Measure and remove byte-specialization and equivalent-check variants.
- [x] Retain smaller O1 shared extraction with explicit retail failure state.
- [x] Prove active restoration including delay slots and rerun the full bounded module.
- [ ] Continue structural fitting of builder/shared helpers/adapter; best O2 excess is 816 bytes.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and remaining ownership/hardware/resume gates.

The opt-in corpus class is `InitDecompressorStoredSharedLengthsCorpusTests`
in `tools.tests.test_init_decompressor_stored_shared_lengths`, with the
existing environment selectors. It was not run here. Production Init,
adapter assembly, default flags and README aggregates remain unchanged.
Unrelated Game edits are preserved and excluded from the checkpoint.
