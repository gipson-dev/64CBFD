# Init Diagnostic Overlay Placement and Positive Pool Bounds

Date: 2026-10-03

## Scope

Follow-up to [Note 840](840-init-retail-loaded-page-table-loop-write-footprint-20261003.md).
Qualify the enabled diagnostic path's placement arithmetic, without executing
the complete debugger loader, DMA, TLB effects or hardware exception handling.

Add `test_init_diagnostic_storage.py` and one native allocator contract test.
All diagnostic instruction slices are pinned against the SHA1-validated US
ROM using `func_10007DAC`'s extracted words. The existing bounded integer
model gains a local signed ADD with overflow rejection; no general CPU model
changes or production edits.

## Retail Placement

`D_8003BE74` is the page pool's physical-address value: the setup routine
masks allocation results with `0x0FFFFFFF` before publishing it.

The diagnostic code at `0x10007ED8..0x10007F00` computes:

```text
overlay_cached = (pool_physical & 0xFFFF0000) + 0x80010000
initial_sp     = overlay_cached + 0x5958
```

Thus the debugger starts at the next 64 KiB boundary, not in a separate
allocation or the static decoder workspace. For an 8 KiB-aligned pool, its
offset within the pool is 8 KiB through 64 KiB. The fixture executes all eight
alignment residues and checks the original register results.

The pinned DMA-argument slice produces direction 0, ROM source `0x19EA88`,
destination `overlay_cached`, and length `0x4960` (`0x1A33E8 - 0x19EA88`).
The image ends `0xFF8` bytes below the initial SP. This checks arguments only;
it does not perform or validate DMA/cache effects.

The pinned TLB-argument slice produces index 15, page mask `0x1E000`, virtual
base `0x16000000`, physical halves at `overlay_physical` and
`overlay_physical + 0x10000`, and final argument `-1`. The two argument stores
occur in the 0x18-byte call frame below the relocated SP. This records a
128 KiB mapping span, not proof that the mapping or debugger execution succeeds.

## Allocation Bounds

The new allocator test compiles unchanged recovered allocator/initializer C
in the existing freestanding native fixture. For every direct count 107..362,
it allocates the real aligned rear pool and verifies that the overlay image,
initial SP and entire 128 KiB mapping span lie inside the requested pool and
private heap. All eight low-16-bit alignment residues occur in these 256
allocations. The formula checked there is separately established by executing
the original diagnostic words.

These positive-count extents are backed by the page-pool allocation, but are
not separate ownership: debugger loading reuses/overwrites that pool's storage.
This does not prove live game pages remain valid during diagnostics.

Zero/tiny cases are explicitly separate. With published pool zero, placement
is `0x80010000`, below the ordinary heap base. With physical pool `0x0012E000`,
SP needs `0x7958` bytes from the pool base, exceeding both an eight-byte
zero-request allocation and a one-page pool. These are bounded arithmetic
counterexamples, not observed failure reachability. Note 833's zero-count
fallback cannot inherit the positive-count diagnostic bound.

## Verification

```sh
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_allocator_guest_free tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_diagnostic_storage tools.tests.test_init_bitmap_allocator_contract
make tools-check
git diff --check
```

All 54 focused tests pass in 8.080 seconds. The diagnostic/native allocator
subset passes 13 tests in 2.523 seconds. Project tool and whitespace checks pass.

## Remaining Work

Next inspect debugger entry/stack and post-diagnostic mapping/page-state cleanup,
or return to decoder fitting with these lifetime constraints preserved. Full
enabled-path effects, actual fallback reachability and complete static decoder
reservation ownership remain open. Decoder fitting is still 896 bytes over
retail; do not promote or enlarge buffers on these placement results alone.

Production C/assembly, decoder/adapter, README totals and unrelated Game edits
remain unchanged. Prior Init inventory remains 492 C / 539 total, with 47
retained assembly functions (12,252 bytes).
