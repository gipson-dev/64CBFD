# Init Offset Sum Full Masked CU1 Set Corpus

Date: 2026-10-03. Source baseline: `32a57ec3`; preceding documentation
checkpoint: `994cc87a`.

## Result

All 507 fresh paired retail-page comparisons pass in 814.477 seconds,
with one passed test, no skips and zero exit status. Linked text is 4,736
bytes, maximum observed descent 3,240, minimum SP 0x80031D68 and known-neighbor
clearance 88 bytes. These agree with Note 862's CU1-clear terminal receipt.
The two unchanged-source runs bank 1,014 paired page executions across
both masked CU1 modes for this selected profile, not the other profiles.

This is the companion to [Note 862](862-init-offset-sum-full-masked-cu1-clear-corpus-20261003.md)
for the exact revised Note 861 packed/remaining O2/g3 combination. Decoder,
adapter, compiler and test sources are unchanged between the runs. This
mode sets CU1 while keeping FR set and IE/EXL clear: status 0x2400FF00.
Scratch-FPR comparison stays enabled; CU1-set behavior is not inferred
from CU1-clear restoration.

## Selection And Coverage

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_builder_offset_sum.InitDecompressorBuilderOffsetSumCorpusTests -v -f
```

Setup freshly compiles/links all six shapes, checks empty compiler/link
logs and selects only packed/remaining O2/g3. Live configuration inspection
confirms the same twelve extra flags listed in Note 862, including
`--dynamic-repeat-value` and `--builder-offset-sum`, ABI FPR shadow,
`INIT_DECODE_CORE_OWNS_STATE=1`, `CoreOwnedStateFixture` and scratch-FPR
comparison. The offset loop uses Note 861's reused `available` variable.

The paired comparison is unchanged from Note 862: all 507 real ROM pages
and reference-image outputs, return/output/workspace/frame state, complete
restored GPR/FPR/status/caller context, FPR receipts, poisoned core-owned
initialization, DMA-rounded read bounds and stack/write guards. Executed
compiled core and adapter are required; original-core execution is rejected.
See that note for the detailed active-gate inventory.

Terminal corpus receipt:

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4736 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 814.477s
OK
```

The observed descent matches the Note 861 static bound. The two-mode
qualification is 507 CU1-clear pages from Note 862 plus 507 CU1-set pages
here. It does not reuse the older Notes 856/857 receipts. Elapsed time is
host harness time, not a hardware performance measurement.

## Supporting Checks

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection -v
wsl make tools-check
git diff --check
```

The fifteen helper/selection tests pass in 0.054 seconds with no skips.
Together with this corpus test, sixteen tests pass with no skips. Tool
and diff checks pass.
The selection controls use synthetic orchestration, not additional guest
page runs. The bounded Note 861 suite is prior evidence, not rerun here.
No source/default/production/README aggregate-count change is made; unrelated
Game work remains preserved and excluded from the documentation checkpoint.

## Limits And Next

- [x] Bank all 507 revised-combination masked CU1-set page comparisons.
- [x] Record the paired current-source qualification with Note 862.
- [ ] Continue builder/shared-helper fitting; linked text still exceeds retail.
- [ ] Qualify other profiles and complete ownership/hardware/scheduler-resume gates before promotion.

These model-executed real-data context checks do not establish full stack
reservation, hardware interrupt timing, arbitrary alias equivalence, retail
slot ownership or byte matching. No production build or sibling-port test
is claimed. Prior Notes 856/857 remain scoped to the older source without
the repeat-value/offset-sum changes; they are not reassigned to this build.
