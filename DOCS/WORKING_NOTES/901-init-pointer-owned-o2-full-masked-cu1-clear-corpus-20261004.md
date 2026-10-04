# Init Pointer Owned O2 Full Masked CU1 Clear Corpus

Date: 2026-10-04. Starting HEAD: `4bf3a333`.

## Scope

Full guarded qualification of Note 900's combined pointer-owned core and
176-byte tight adapter, selected packed O2/g3, exception-masked CU1 clear.
Setup freshly compiles six images before selecting exactly one profile.
The fixture retains input/fifth-slot read-before-initialization guards,
live-SP write fencing and pre-adapter-return callee preservation.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_pointer_owned_adapter.InitDecompressorPointerOwnedAdapterCorpusTests -v -f
```

Each retail DMA-rounded input is paired with reference execution and pristine
image output. Inherited comparisons check output/result, architectural context,
final FPR/GPR state and guarded storage, requiring compiled-core execution
without original-core fallback. This is guest/model evidence, not a hardware
or gameplay run.

## Result

All 507 paired retail pages pass in 819.113 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4560 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 819.113s
OK
```

Observed descent equals the 3,240-byte static bound. The 88-byte margin above
known neighbor end `0x80031D10` and write-only live-SP fence do not establish
full reservation ownership or absence of below-SP reads. Executable text is
still 576 bytes above the retail 3,984-byte group. Note 900's sixteen-byte
isolated text-plus-rodata span reduction is prior layout evidence, not a
production ROM placement result.

## Integrity

These SHA256 hashes match before and after the run. No candidate source or
configuration edits occurred during qualification.

```text
B9CB79406AF409EE107AF800A4B06D446A2B002EDC4E87129E8B403CDCC92198 init_decompressor_semantic.c
A8D2642E81EA3960B0A9CFABDF61BDB04F2F3A951D7E8B2251228B5FE9DC72CB init_decompressor_core_adapter.s
6EAC52AC58FE53D060DBC643CA30C93B320B08F48C9D7659D08C1CEA26249B7C compile_init_decompressor.py
B4782710085321F96032458BFB9D507C9BC684A63FDD2CE158E97D4EF15F3484 test_init_decompressor_pointer_owned_adapter.py
0760CACC7BC4FD78C19E63D6D0B48B0195E2B7AF342B7CDE7E2139C22642616C test_init_decompressor_live_stack_writes.py
F9ADF06BEC8B674F78FAE7E7FAFA4D79DF62FA575F96A58A78543F90D3828663 test_init_decompressor_shadow_corpus.py
```

Twenty-two supporting ledger, corpus-selection, exception-mask and storage
tests pass in 47.790 seconds, no skips. The compiled masked-context tests in
that selection cover their existing default configuration; the new candidate's
full corpus is the separate result above. Project tool and whitespace checks
pass. Note 900's bounded suite is prior evidence, not rerun here.

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
make tools-check
git diff --check
```

## Remaining Gates

- [x] All 507 guarded combined-candidate packed O2 masked CU1-clear pages.
- [ ] Matching combined-candidate packed O2 masked CU1-set corpus.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

Previous configurations' CU1-set results do not qualify this combination.
Production sources, Init conversion totals, README, word guards, sibling-port
artifacts and unrelated Game work remain unchanged. No ROM build or hardware
run is claimed.
