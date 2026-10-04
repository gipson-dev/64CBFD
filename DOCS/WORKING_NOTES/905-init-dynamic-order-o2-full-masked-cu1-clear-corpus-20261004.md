# Init Dynamic Order O2 Full Masked CU1 Clear Corpus

Date: 2026-10-04. Starting HEAD: `f82d73b3`.

## Scope

Full guarded qualification of Note 904's opt-in dynamic order-table cursor
and countdown, paired with the pointer-owned core and 176-byte tight adapter.
Setup freshly compiles six images, then selects exactly packed O2/g3.
The fixture inherits input/fifth-slot read-before-initialization guards,
live-SP write fencing and pre-adapter-return callee preservation.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorCorpusTests -v -f
```

Each retail DMA-rounded input is paired with reference execution and pristine
image output. Inherited checks cover output/result, architectural context,
final FPR/GPR state and guarded storage, requiring compiled-core execution
without original-core fallback. This is bounded guest/model evidence, not a
hardware or gameplay run.

## Result

All 507 paired retail pages pass in 835.460 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4528 depth=3248 low=0x80031D60 margin=80
shadow corpus complete: modes=clear runs=507
Ran 1 test in 835.460s
OK
```

Observed descent equals the 3,248-byte static bound. The new initializer saves
32 executable bytes and costs eight stack bytes versus the option-omitted
candidate in Notes 901/902. Executable text remains 544 bytes over the retail
3,984-byte group. Minimum SP `0x80031D60` leaves 80 bytes above known neighbor
end `0x80031D10`. Clearance and the write-only live-SP fence do not prove full
reservation ownership or absence of below-SP reads. No production placement
or ASM ownership transition is established.

## Integrity And Supporting Checks

The following six SHA256 hashes match before and after the run. Candidate
sources and flags stayed fixed throughout qualification.

```text
D36149FC872B7C44103B963867B1ABA4540BBD3D4A7B559B81EEEF61A5F2270E init_decompressor_semantic.c
A8D2642E81EA3960B0A9CFABDF61BDB04F2F3A951D7E8B2251228B5FE9DC72CB init_decompressor_core_adapter.s
1755CBFFC371BAF10E23EAB7763A6BBDF57743F5EF5B4066B22ABA203CC51735 compile_init_decompressor.py
5D5CC7622A2E8E3AFC4D1AA45E88B39E076D63E4B40DA5E7952D577AB1E9B654 test_init_decompressor_dynamic_order_cursor.py
0760CACC7BC4FD78C19E63D6D0B48B0195E2B7AF342B7CDE7E2139C22642616C test_init_decompressor_live_stack_writes.py
F9ADF06BEC8B674F78FAE7E7FAFA4D79DF62FA575F96A58A78543F90D3828663 test_init_decompressor_shadow_corpus.py
```

Twenty-two supporting ledger, corpus-selection, exception-mask and storage
tests pass in 47.660 seconds, no skips. The compiled masked-context tests in
that selection cover their existing default configuration; the new candidate's
full corpus is the separate result above. Project tool and whitespace checks
pass.

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
make tools-check
git diff --check
```

Note 904's bounded suite/all-count initializer test is prior evidence, not
rerun here. Option-omitted default-text preservation remains scoped to Note 904.

## Remaining Gates

- [x] All 507 guarded dynamic-order packed O2 masked CU1-clear pages.
- [ ] Matching dynamic-order packed O2 masked CU1-set full corpus.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

Previous configurations' CU1-set results do not qualify this changed candidate.
Production Init remains 492 C / 47 assembly functions. Production sources,
README totals, word guards, sibling-port artifacts and unrelated Game work
remain unchanged. No ROM build or hardware run is claimed.
