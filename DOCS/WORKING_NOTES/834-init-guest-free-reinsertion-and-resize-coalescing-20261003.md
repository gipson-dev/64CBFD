# Init Guest Free, Reinsertion and Resize Coalescing

Date: 2026-10-03

## Scope

Follow-up to [Note 833](833-init-page-pool-retry-and-zero-count-fallback-contract-20261003.md).
Qualify the recovered production C `func_10004074` together with the actual
allocator and heap initializer. No production code, retail-word guards,
decoder experiments, adapter, or conversion ownership changes.

The free routine clears the tag using `*((u8 *)block + 8) = 0`. This is the
high byte of the size/tag word on the N64. Running it unchanged in the existing
little-endian native fixture would clear the low size byte instead. The new
fixture therefore compiles unchanged production bodies with IDO 5.3 to a
fresh big-endian MIPS ELF, without retail patches or padding.

## Method

- Reuse the allocator fixture's exact production function/layout/table extraction,
  now also extracting `func_10004074`.
- Replace only the generated fixture's GNU heap declaration with an external
  fixed-address array, linked at `0x800E9D10`; capacity is a private 2 MiB.
- Remove the fixture's bulk poison loop; lazily poison reads inside that private
  heap instead. Production routines remain unchanged.
- Compile separately with `-O2 -g3` and `-O1`, link text/data at
  `0x10400000`/`0x10500000`, and execute via the bounded guest instruction model.
- Permit writes only to the private heap, bounded stack, or mapped writable ELF
  bytes; reject read-only ELF writes. Interrupt-mask and fatal callbacks are
  instrumented C stubs, not real OS/hardware behavior.
- Locally implement signed `LH`, with a focused sign-extension/endian test.
  Assert preserved O32 saved registers and confirm the actual free entry executes.

## Results

All three compiled scenarios pass in both compiler profiles:

1. Counts 107 through 362: allocate the aligned rear page pool and front bitmap,
   validate the lists, free pool first (the recovered resize order), then bitmap.
   Every cycle restores one physical/free block at the original heap base with
   the original `capacity - 0x14` payload size, correct free head/tail and restored
   interrupt mask. This is 256 cycles per profile, 512 total.
2. Free the middle of three front allocations, then the preceding and following
   blocks: free-list reinsertion and both coalescing directions preserve links
   and fully reclaim the private heap. A null free also returns harmlessly.
3. Free the middle allocation while its neighbors remain live: their allocation
   tags, sizes and distinct byte payloads remain unchanged.

Verification:

```sh
python3 -m unittest tools.tests.test_init_allocator_guest_free tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_page_pool_setup tools.tests.test_init_decompressor_storage_boundaries -v
make tools-check
git diff --check
```

The focused suite passes all 22 tests in 3.915 seconds. Project tool checks pass.

## Boundary and Next Work

This establishes ordinary free/reinsertion/resize behavior for a private heap
under a bounded instruction model. It does not establish hardware execution,
actual game heap fragmentation, arbitrary invalid/double frees, tag-sweep
lifetimes, fatal-handler non-return behavior, or complete static decoder
workspace/stack reservation ownership.

Init remains 492 C functions of 539, with 47 retained assembly functions
(12,252 bytes), per the prior inventory; this test-only checkpoint does not
refresh or change those totals. The decoder replacement still has a smallest
qualified linked text size of 4,880 bytes, 896 over its 3,984-byte retail group.
Do not promote that replacement merely because these allocator checks pass.

Next examine the tag-sweep/free callers and fault lifetime, then the complete
stack/workspace reservation writers. Fitting remains an independent blocker.
