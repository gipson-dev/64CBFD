# Init Guest Tag Sweep and Retag Lifetime Contract

Date: 2026-10-03

## Scope and Method

Extend [Note 834](834-init-guest-free-reinsertion-and-resize-coalescing-20261003.md)
using the same fresh big-endian IDO guest fixture. Extract the production bodies
of `func_10004250`, `func_10004308`, and `func_100043B4` verbatim from
`conker/src/init_3C40.c`. Compile and execute each new scenario in both
`-O2 -g3` and `-O1`. No production changes, assembly conversion, or retail
word guards are involved.

The full sweep calls `func_15042D50` before traversing the physical list. The
fixture substitutes a callback recording its call count and current interrupt
mask. This is deliberately not qualification of the real Game callback's
effects. Allocation failure/fatal callbacks also retain their prior stub scope.

## Measured Contract

- `func_10004250`: tag 2 is freed; tags 3 and 4 age to 2 and 3. Tags 1 and
  `0xFF` remain allocated. Three consecutive sweeps release the original tag-3
  and tag-4 allocations despite intervening free-block coalescing. The fixture
  checks lists/mask after each pass and fully reclaims the heap afterward.
- `func_10004308`: tags 1, 2, 3 and 4 are freed. Tags 5 and `0xFF`, including
  their payload sentinels, survive. Adjacent selected allocations and an
  already freed gap do not prevent traversal from reaching later selected
  allocations. The recorded cleanup callback executes once with mask 1;
  the sweep ultimately restores mask `0x1234`. Freeing the surviving blocks
  afterward restores one complete free block.
- `func_100043B4`: retagging a 64-byte allocation from `0xFF` to 4 preserves
  its size. Three aging sweeps take it through 3, 2, and free, with correct
  links and complete final reclamation.

The page-pool and bitmap allocator requests audited in Notes 833/834 use
tag `0xFF`. Under these unchanged sweep bodies they are not selected for
release or aging. Their explicit resize frees remain relevant; the sweep
does not stand in for that release path.

## Verification

```sh
python3 -m unittest tools.tests.test_init_allocator_guest_free tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_page_pool_setup tools.tests.test_init_decompressor_storage_boundaries -v
make tools-check
git diff --check
```

All 25 focused tests pass in 4.058 seconds, including all three new scenarios
in both compiler profiles. The standalone guest suite passes seven tests.
Project tool checks and whitespace validation pass.

## Remaining Work

These checks cover bounded private-heap C behavior, not gameplay or hardware
execution. They do not cover real callback mutations of the captured list,
all heap fragmentations, invalid pointers/double frees, or fatal-handler
non-return behavior. The full sweep captures the initial list head before
calling the Game callback; its real effects must be inspected before extending
the lifetime claim to that call path.

Next audit the actual callback/fatal paths and the static stack/workspace
reservation writers. Complete decoder ownership and fitting remain open.
The last inventory remains 492/539 Init functions in C and 47 assembly
functions (12,252 bytes); this checkpoint changes none of those aggregates.
The qualified experimental decoder still exceeds its retail group by 896
bytes. README totals and unrelated Game work remain untouched.
