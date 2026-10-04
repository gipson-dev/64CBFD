# Init Distance Operation O2 Full Masked CU1 Clear Corpus

Date: 2026-10-04. Starting HEAD: `0f2bf894`.

## Scope

Full guarded qualification of Note 911's opt-in distance-operation local,
combined with the packed-remaining dynamic-order, pointer-owned core and
176-byte tight adapter configuration. Setup freshly compiles six images,
then selects exactly packed O2/g3. The fixture retains input/fifth-slot
read-before-initialization checks, live-SP write fencing and callee receipt
guards before adapter return. No candidate source or flags changed during the run.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalCorpusTests -v -f
```

Each DMA-rounded retail input is paired with reference execution and pristine
image output. Inherited checks cover result/output, architectural context,
final FPR/GPR state and guarded storage. Compiled core execution is required;
there is no original-core fallback. This is guest/model evidence, not hardware
or gameplay acceptance.

## Result

All 507 paired retail pages pass in 826.726 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4512 depth=3248 low=0x80031D60 margin=80
shadow corpus complete: modes=clear runs=507
Ran 1 test in 826.726s
OK
```

Observed descent equals the 3,248-byte static bound. The sixteen-byte text
saving remains intact at 4,512 executable bytes, still 528 above the retail
3,984-byte group. Minimum SP `0x80031D60` is 80 bytes above known neighbor
end `0x80031D10`. This clearance and write-only live-SP fencing do not prove
full private reservation ownership or absence of below-SP reads. No production
placement or assembly ownership transition is established.

## Integrity And Supporting Checks

All six SHA-256 hashes match before and after the corpus run:

```text
43A3897FE734E8000F4C156CDB3DB69722D25A210B5B518C02EA315BD71CA0C2 init_decompressor_semantic.c
A8D2642E81EA3960B0A9CFABDF61BDB04F2F3A951D7E8B2251228B5FE9DC72CB init_decompressor_core_adapter.s
E5792E1FDB2A12A7273A0BE3B91BD67E557801CBC6EA54896F9A7926BCBA3506 compile_init_decompressor.py
1280377B35F3582B29A2D7FDC4F28A7237E7CF3F9BFBEA35093458A05275BAFD test_init_decompressor_distance_operation_local.py
0760CACC7BC4FD78C19E63D6D0B48B0195E2B7AF342B7CDE7E2139C22642616C test_init_decompressor_live_stack_writes.py
F9ADF06BEC8B674F78FAE7E7FAFA4D79DF62FA575F96A58A78543F90D3828663 test_init_decompressor_shadow_corpus.py
```

Twenty-two supporting ledger, corpus-selection, exception-mask and storage
tests pass in 50.609 seconds, no skips:

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
```

The supporting compiled masked-context tests cover their existing default
configuration; the changed candidate's full corpus is the separate result above.
Note 911's bounded suite, table-stability guard and default-text preservation
are prior evidence, not rerun here. Project tool and whitespace checks pass.

## Remaining Gates

- [x] All 507 guarded distance-operation packed O2 masked CU1-clear pages.
- [ ] Matching distance-operation packed O2 masked CU1-set full corpus.
- [ ] Reduce 528-byte fitting excess and prove full reservation ownership.
- [ ] Establish production entry/frame ownership and hardware/context behavior.

Run the same corpus command with `CONKER_INIT_SHADOW_CORPUS_CU1=set` next,
keeping this candidate fixed and checking the same hashes. Earlier configurations'
CU1-set receipts do not qualify the changed code.

Production Init remains 492 C / 47 assembly functions. Production sources,
README totals, word guards, sibling artifacts and Release are unchanged.
Pending Game and actor/timeline work remains untouched and unstaged. No ROM
build, production promotion, hardware execution or push is claimed.
