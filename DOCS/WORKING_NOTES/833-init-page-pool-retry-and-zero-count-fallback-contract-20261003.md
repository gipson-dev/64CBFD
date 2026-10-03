# Init Page Pool Retry And Zero Count Fallback Contract

Date: 2026-10-03. Baseline: `4923bd5`.

## Result

The page-pool setup's complete 55-word retail slot is pinned and its retry
control flow is executed with explicit allocator return stubs. A new native
production-C allocator test independently proves zero-size page/bitmap requests
can allocate nonzero storage from the valid test heap. Together these narrow
the ownership precondition: positive requested count and nonzero allocation
returns alone do not establish a positive count after fallback.

All 26 focused tests pass in 2.483 seconds. No production function, word guard,
decoder/adapter, compiler default or README aggregate changes. This is failure
contract recovery, not a new conversion, hardware failure observation or fix.

## Original Setup And Retry

`func_10005B04` occupies 0x10005B04..0x10005BE0. The fixture checks all 55 words
against the SHA-1-qualified US retail ROM. It records the Context/Wired CP0
writes without emulating CP0/TLB behavior, and substitutes synthetic allocator
stubs outside the original slot. The callee stubs provide chosen return values
and record arguments; they do not execute the real allocator.

The routine saves the old signed halfword count in s0, publishes the new count,
then requests a pool with (count<<12, 0xFF, 4, 1, 2). A zero result jumps to
the interior entry `func_10005B3C`, with old s0 copied to a0 in the delay slot.
It requests a new allocation at the old count, not an old allocation pointer.
Repeated failures retry that same saved old count, without another prologue.

On a nonzero result, the pointer is masked with 0x0FFFFFFF into D_8003BE74.
The current signed count then determines the bitmap request `(count + 7) >> 3`.
Its returned pointer is published to D_8003BE70; the inclusive endpoint is
start + requested_bitmap_bytes - 1. There is no local bitmap-null branch.
Saved registers, SP and RA are restored on the tested returning paths.

The resize wrapper `func_100014C4` disables interrupts, resets mappings, frees
the old pool and bitmap if nonzero, then calls setup and clears the bitmap.
Consequently fallback is reallocation using an old size, not preservation of
the previous live allocation. That wrapper ordering is inspected production C,
not a newly executed wrapper/allocator/free integration test.

## Tested Outcomes

| Input / stub outcome | Measured setup behavior |
| --- | --- |
| Request 235, pool succeeds | 235-page request, bitmap request 30, published count 235 |
| Request 362 fails, previous 235 succeeds | Requests 362 then 235 pages; bitmap request 30; count 235 |
| Every pool result zero | No return within 256-instruction budget; retries old count after first request |
| Request 235 fails, previous 0 succeeds | Pool requests 235 pages then zero bytes; bitmap request zero; count 0, end=start-1 |
| Bitmap callee returns zero for count 235 | Publishes start=0, end=29 and returns |
| Artificial old count 0xFFFF | Signed old -1 produces pool argument 0xFFFFF000 and bitmap request zero |

The negative old-count case is outside the established ordinary caller domain;
it protects signed-load fidelity, not a gameplay reachability claim. The
repeated-failure budget result is not proof of an infinite real-machine loop.
The bitmap-null result is conditional on the callee returning: the actual
fatal callback may not return and is not newly qualified here.

In the zero-previous-count fixture, execution continues into the actual
`func_10005BE0` leaf. It immediately stores 0xFF at start and does not return
within a 128-instruction budget with end=start-1. This connects the setup's
conditional fallback geometry to the already documented zero-count leaf
contract. No arbitrary address-space/fault behavior is modeled.

Startup clears BSS containing the previous-count global and requests 235 pages.
This makes zero a relevant initial previous value to investigate; it does not
prove the first real allocation ever fails or that gameplay reaches this edge.
The direct resize caller's positive 107..362 requested domain from Note 788
remains valid. It must not be broadened into a proof that setup always publishes
a positive count after allocator failure.

## Native Allocator Evidence And Boundaries

The existing production-C allocator harness from
[Note 789](789-init-bitmap-allocator-provenance-and-rear-bound-correction-20261003.md)
already covers successful positive-count allocation bounds and valid list state.
This checkpoint reuses it rather than repeating that audit as new evidence.

The new case calls real recovered `func_10003C6C(0, 0xFF, 4, 1, 2)` and
`allocate_memory(0, 0xFF, 0, 0)` in its freestanding 32-bit two-MiB heap at
0x800E9D10. Both return nonzero; the page pointer has class-four alignment and
at least eight bounded payload bytes, the bitmap payload is eight bytes, and
the physical/free lists and instrumented interrupt mask remain valid.

This does not integrate the native allocator with the MIPS setup fixture or
prove a particular real out-of-memory trajectory. It demonstrates that the
zero-size success premise is not excluded by the recovered allocator's
minimum-eight-byte rule. Storage allocation success does not repair setup's
zero-count endpoint arithmetic.

Do not introduce a defensive early return into a matching decomp based on
this edge characterization. A deliberate behavior fix would be a separate
decision; this checkpoint preserves original semantics.

## Verification And Next

```powershell
wsl python3 -m unittest tools.tests.test_init_page_pool_setup tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_bitmap_assembly tools.tests.test_init_decompressor_storage_boundaries -v -f
```

- 26 tests pass in 2.483 seconds: seven setup tests, seven production-C
  allocator tests, eight bitmap tests and four storage-boundary tests.
- Setup uses bounded retail-word execution with allocator/CP0 stubs; allocator
  tests use native production C with instrumented mask/fatal callbacks. Neither
  substitutes for actual hardware, full exception replay or gameplay.
- No new compiled shadow corpus, full production build or full project suite.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- Pending Game changes and sibling repositories remain untouched.

Next qualify real free/reinsertion/coalescing writers and resize lifetime,
including allocation failure/fatal callback behavior. Keep complete exception
stack/workspace reservation and synchronous-fault bounds separate. The
decompressor's 896-byte fitting excess and remaining full-corpus profiles also
stay open before production replacement.
