# Init Post-Diagnostic Page State Cleanup and Continuation

Date: 2026-10-03

## Scope

Follow-up to [Note 841](841-init-diagnostic-overlay-placement-and-positive-pool-bounds-20261003.md).
Add `test_init_diagnostic_cleanup.py` to execute the retail diagnostic return
tail, actual software page-table clear and actual bitmap reset. No production
C/assembly or conversion ownership changes.

Pin all modeled original instructions against the SHA1-validated US ROM:
`0x10008078..0x10008114`, `func_10005BE0`'s complete 19-word slot and the
nine-word `func_10001420` slot. Seed the debugger return values, saved SP/RA,
page-pool pointer, positive bitmap count/bounds and surrounding guards.

The guest fixture instruments three external calls: `osUnmapTLB`, diagnostic
formatter `func_10007CC4`, and `osWritebackDCacheAll`. Explicit synthetic
BREAK markers record calls and return; these are not their actual bodies.
CACHE records operands only. The page-table and bitmap writes are executed
from original retail instructions, not supplied by stubs.

## Measured Tail

- A zero debugger result preserves seeded continuation `0x100077A4`, the
  normal post-diagnostic fault path. Any tested nonzero result (1 or
  `0xFFFFFFFF`) replaces it with `0x10007760`, the thread-requeue path.
- The tail captures seeded v1 in s2, then issues exactly 30 unmap calls with
  indices 2 through 31 in order.
- `func_10001420` writes exactly 1,016 four-byte zeros to
  `[0x80043B40, 0x80044B20)`, the `0xFE0` software page table.
- `func_10005BE0` resets the bitmap to FF bytes, masking the final byte to
  `(1 << (count & 7)) - 1` when count is not divisible by eight.
- The instruction-cache sweep records 513 operands, operation 0, from
  `0x80000000` through inclusive endpoint `0x80004000`, stride 32.
- Formatter offset `0x300` precedes the writeback call. The diagnostic cursor
  `D_8002AE34` becomes zero, saved SP restores to `0x80032A10`, and RA loads
  the selected continuation.
- Pool pointer `D_8003BE74` remains unchanged. The table/bitmap guards and
  entire static decoder interval `[0x80031AE0, 0x80035504)` remain unchanged
  by modeled CPU stores. Write fences reject that static interval and guards.

Tests execute six count/result combinations for counts 107, 235 and 362,
one all-bits-set nonzero result at count 112, and eight bitmap remainder cases
112..119: 15 bounded cleanup runs. A separate test checks write-fence rejection.

## Verification

```sh
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_allocator_guest_free tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_diagnostic_storage tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_diagnostic_cleanup
make tools-check
git diff --check
```

All 58 focused tests pass in 8.216 seconds. Project tool checks and whitespace
validation pass.

## Boundaries and Next Work

Execution stops before final JR RA; the test verifies its loaded continuation,
not thread requeue, scheduler selection or resumed execution. It does not
execute the debugger UI/entry, actual unmap/cache operations, DMA, formatter
writes, concurrent state mutation or zero/tiny fallback cleanup. Thus it proves
the sequential CPU-store footprint under explicit stubs, not complete enabled
diagnostic behavior or full decoder reservation ownership.

The real tail clears software page state after reusing pool storage. No new
private allocation is shown here. Next inspect debugger entry/stack use and
the continuation contracts, or pursue decoder fitting while preserving these
constraints. The experimental decoder remains 896 bytes over retail.

Production, decoder/adapter, README aggregates and unrelated Game work remain
unchanged. Prior Init inventory stays 492 C / 539 total, with 47 retained
assembly functions (12,252 bytes).
