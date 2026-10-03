# Init Retail Cleanup Callback Null Path and Fatal Slot

Follow-up correction: [Note 839](839-init-block-local-storage-writers-and-fr1-fixture-correction-20261003.md)
replaces this checkpoint's local even/odd FPR pair-transfer model with FR=1
independent high/low FPR words and requalifies the callback in both IDO profiles.
The original null-list/heap findings remain; pair-transfer semantics are superseded.

Date: 2026-10-03

## Findings

Follow-up to [Note 835](835-init-guest-tag-sweep-and-retag-lifetime-contract-20261003.md).
The real `func_15042D50` is in `conker/src/game_70200.c`, not `src/game`.
It clears `D_800CBD64` and calls `func_15043384(0)`. The latter's C body is
still a zero-return placeholder, so it cannot qualify the real callback.

Retail `func_15043384` loads that cleared pointer at `0x150433C4`, branches
at `0x150433D0` to `0x1504393C`, and increments `D_80085CD0` in the branch
delay slot. That path resets presentation globals and returns. It bypasses
the nonempty-list renderer, its external calls, and its record free at
`0x15043918`. Thus, on this sequential null-list path, the callback does not
invalidate the physical heap head captured by `func_10004308`.

The actual allocator fatal callback `func_150AD770` is a handwritten four-word
slot: `syscall 0`, then three NOPs. It is not a returning C function. Earlier
failure tests deliberately use returning stubs; they do not establish retail
exception-handler control flow, failure reachability, or resumed behavior.
Do not convert this trap to an ordinary C no-op or infer that it never resumes.

## Executable Evidence

Extend `test_init_allocator_guest_free.py` with a mixed guest scenario:

- Compile the actual Init allocator/free/full sweep C without retail guards in
  both O2/g3 and O1 IDO profiles.
- Recover Game bytes independently from the SHA1-validated retail ROM's
  compressed pages, and compare the callback/renderer range against the local
  decompressed image. Pin the ten wrapper words and all 415 renderer words
  against the extracted assembly listing.
- Redirect only the generated fixture callback stub through a guest jump to
  the retail wrapper; retain its original linked address for the compiled caller.
  This is test scaffolding, not a production patch or matching claim.
- Seed the render-list global nonzero to demonstrate that the wrapper actually
  clears it. Execute the original null-list path with bounded global writes.
- Assert visits to the null-list branch/reset epilogue and absence of visits to
  the nonempty-list body/free call. Check counter 41->42, reset colors/positions/
  scale, FPR20/21 preservation, heap/list integrity and saved O32 registers.
- The full sweep releases the selected tag-2 block while preserving the tag-FF
  block and payload; explicit release afterward completely reclaims the heap.
- Locally model FPR pair save/restore and SWC1 bit stores, with an independent
  endian/round-trip test. No floating arithmetic or CP0/exception behavior is
  modeled on this callback path.
- Independently pin the fatal four-word slot from SHA1-validated retail pages.

## Verification

```sh
python3 -m unittest tools.tests.test_init_allocator_guest_free tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_page_pool_setup tools.tests.test_init_decompressor_storage_boundaries -v
make tools-check
git diff --check
```

All 28 focused tests pass in 5.397 seconds. Project tool and whitespace checks
pass. The new real callback scenario passes in both IDO profiles.

## Remaining Boundaries

This is sequential bounded guest execution, not hardware/gameplay acceptance.
It does not qualify asynchronous writes to the render-list global, the renderer's
nonempty path, the real interrupt-mask implementation, or syscall dispatch/resume.
The null callback path removes one specific heap-lifetime concern; it does not
prove complete decoder storage ownership.

Next inspect the static stack/workspace reservation writers and relevant
exception handling before making broader ownership/fault claims. Decoder
fitting remains 896 bytes over retail. No production files, README totals,
decoder/adapter or unrelated Game work changed; Init inventory remains at
the prior 492 C / 539 total, with 47 assembly functions (12,252 bytes).
