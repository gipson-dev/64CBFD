# Init Dynamic Order O2 Full Masked CU1 Set Corpus

Date: 2026-10-04. Starting HEAD: `8435f687`.

## Scope

Matching CU1-set qualification of Note 904's opt-in dynamic order-table cursor
and countdown, paired with the pointer-owned core and 176-byte tight adapter.
Sources and flags match the CU1-clear run in
[Note 905](905-init-dynamic-order-o2-full-masked-cu1-clear-corpus-20261004.md).
Setup freshly compiles six images, then selects exactly packed O2/g3.
The fixture inherits input/fifth-slot read-before-initialization guards,
live-SP write fencing and pre-adapter-return callee preservation.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorCorpusTests -v -f
```

Every retail DMA-rounded input is paired with reference execution and pristine
image output. Inherited checks cover output/result, architectural context,
final FPR/GPR state and guarded storage, requiring compiled-core execution
without original-core fallback. This is bounded guest/model evidence, not
hardware timing, complete stack ownership or gameplay validation.

## Result

All 507 paired retail pages pass in 836.723 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4528 depth=3248 low=0x80031D60 margin=80
shadow corpus complete: modes=set runs=507
Ran 1 test in 836.723s
OK
```

Together Notes 905/906 qualify 1,014 paired pages across both masked CU1 modes
for the unchanged dynamic-order packed O2 candidate. Executable text 4,528,
descent 3,248, minimum SP `0x80031D60` and known-neighbor margin 80 match both
runs. Observed descent equals the static bound. The neighbor end is
`0x80031D10`; clearance and the write-only live-SP fence do not prove full
reservation ownership or absence of below-SP reads.

The O2 candidate saves 32 executable bytes and costs eight stack bytes versus
the option-omitted candidate in Notes 901/902. Text remains 544 bytes over
retail 3,984. Other profiles, changed options and production placement are
not qualified by these two corpora. O1 remains the documented negative tradeoff.

## Integrity And Supporting Checks

All six SHA256 hashes recorded in Note 905 match before and after this run.
Candidate sources and flags stayed fixed throughout qualification.
Twenty-two supporting ledger, corpus-selection, exception-mask and storage
tests pass in 50.391 seconds, no skips. Compiled masked-context tests in that
selection cover their existing default configuration; the new candidate's
full corpus is the separate result above. Project tool and whitespace checks
pass.

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
make tools-check
git diff --check
```

Note 904's bounded suite/all-count initializer gate and default-text comparison
remain prior evidence, not rerun here.

## Remaining Gates

- [x] All 507 guarded dynamic-order packed O2 masked CU1-clear pages (Note 905).
- [x] All 507 guarded dynamic-order packed O2 masked CU1-set pages.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

Production Init remains 492 C / 47 assembly functions. Production sources,
README totals, word guards, sibling-port artifacts and unrelated Game work
remain unchanged and excluded from staging. No ROM build or hardware run
is claimed. Nothing is pushed.
