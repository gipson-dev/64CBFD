# Init Pointer Owned O2 Full Masked CU1 Set Corpus

Date: 2026-10-04. Starting HEAD: `e3caf0d6`.

## Scope

Matching CU1-set qualification of Note 900's combined pointer-owned core and
176-byte tight adapter. Sources and flags match the CU1-clear run in
[Note 901](901-init-pointer-owned-o2-full-masked-cu1-clear-corpus-20261004.md).
Setup freshly compiles six images, then selects exactly packed O2/g3.
The fixture retains input/fifth-slot read-before-initialization guards,
live-SP write fencing and pre-adapter-return callee preservation.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_pointer_owned_adapter.InitDecompressorPointerOwnedAdapterCorpusTests -v -f
```

All retail DMA-rounded inputs are paired with reference execution and pristine
image output. Inherited checks cover output/result, architectural context,
final FPR/GPR state and guarded storage, requiring compiled-core execution
without original-core fallback. This is guest/model evidence, not hardware
timing, complete stack ownership or gameplay validation.

## Result

All 507 paired retail pages pass in 823.148 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4560 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 823.148s
OK
```

Together Notes 901/902 qualify 1,014 paired pages across both masked CU1 modes
for the unchanged combined packed O2 candidate. Executable text 4,560,
descent 3,240, minimum SP `0x80031D68` and known-neighbor margin 88 match both
runs. Observed descent equals the static bound. The neighbor end is
`0x80031D10`; clearance and the write-only live-SP fence do not prove full
reservation ownership or absence of below-SP reads.

Executable text remains 576 bytes over the retail 3,984-byte group. Note 900's
sixteen-byte isolated text-plus-rodata span saving is not production placement.
These corpora do not qualify other shapes, profiles or future option changes.

## Integrity And Supporting Checks

All six SHA256 hashes recorded in Note 901 match before and after this run.
No candidate source or configuration edits occurred during qualification.
Twenty-two supporting ledger, corpus-selection, exception-mask and storage
tests pass in 46.715 seconds, no skips. Compiled masked-context tests in that
selection cover their existing default configuration; the new candidate's
full corpus is the separate result above. Project tool and whitespace checks
pass. Note 900's whole bounded suite remains prior evidence, not rerun here.

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
make tools-check
git diff --check
```

## Remaining Gates

- [x] All 507 guarded combined packed O2 masked CU1-clear pages (Note 901).
- [x] All 507 guarded combined packed O2 masked CU1-set pages.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

No production conversion, ROM build or sibling-port test is claimed.
Production Init totals, README, word guards and unrelated Game work remain
unchanged and excluded from staging. Nothing is pushed.
