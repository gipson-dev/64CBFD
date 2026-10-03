# Init Retail Loaded Page Table Loop Write Footprint

Date: 2026-10-03

## Scope

Follow-up to [Note 839](839-init-block-local-storage-writers-and-fr1-fixture-correction-20261003.md).
Resolve one concrete loaded-pointer/loop writer excluded from the static
census: the page-table offset decoder in startup `func_10001194`.
Extend `test_init_decompressor_storage_boundaries.py`; no production edits.

The new fixture pins all 19 words in `[0x10001398, 0x100013E4)` against the
original US ROM, using the extracted startup assembly listing. It executes
the original loop through the existing bounded integer/delay-slot model.
It seeds the already transferred table bytes and the two saved count words;
the actual DMA implementation is not executed.

## Measured Retail Footprint

For 507 retail pages, startup passes 508 offset words including the final
end-offset sentinel. The original loop reloads `D_800354FC` each iteration,
reads the table through that pointer plus the cursor, XORs with `0x8039CCCA`,
adds ROM base `0x42450`, and stores in the loop branch's delay slot.

The fixture establishes:

- All 508 decoded values equal the retail page start offsets plus the final
  page-end sentinel from SHA1-validated retail page extraction.
- Exactly 508 ordered four-byte writes occur at `0x80032B30 + i * 4`.
- The published table pointer is loaded 508 times and remains unchanged.
- The loop body and closing branch each execute 508 times; final count/cursor
  are 508/2032, including the final untaken branch's delay-slot store.
- Writes end at exclusive address `0x80033320`, using 2,032 bytes.
- The last 16 bytes of the 2,048-byte table DMA remain unchanged, as do 16
  poisoned bytes at the following input start `0x80033330`.

This connects Note 832's transfer-size arithmetic to actual loaded-pointer
stores. It does not assign a capacity to the input or workspace.

## Additional Cases

Six synthetic fixtures use counts 1, 2 and 17 at both the real table address
and relocated address `0x81000000`. Exact decoded words, ordered write
addresses and untouched trailing guards pass. These establish cursor/pointer
mechanics, not alternate production configurations.

A zero-count fixture skips the table-pointer dereference and all loop writes.
It is a synthetic branch case, not a claim that retail startup uses zero pages.
All guest writes are fenced to the explicitly declared count-word interval.

## Verification

```sh
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_allocator_guest_free tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route tools.tests.test_init_decompressor_storage_boundaries -v
make tools-check
git diff --check
```

All 41 focused tests pass in 7.395 seconds. The standalone storage-boundary
suite passes all seven tests in 0.595 seconds. Project tool and whitespace
checks pass.

## Remaining Work

This is sequential loaded-pointer arithmetic after a seeded table transfer.
It does not model DMA/cache effects, concurrent pointer/count mutation, every
other pointer-based writer, diagnostic-enabled storage, or full reservation
ownership. Next qualify diagnostic-enabled memory placement and other loaded
writers before enlarging or promoting the decoder replacement.

Decoder fitting still exceeds retail by 896 bytes. Production C/assembly,
decoder/adapter, README aggregate totals and unrelated Game work are unchanged;
the prior Init inventory remains 492 C / 539 total, with 47 retained assembly
functions (12,252 bytes).
