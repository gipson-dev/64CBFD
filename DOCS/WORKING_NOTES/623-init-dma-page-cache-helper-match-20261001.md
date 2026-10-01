# Init DMA page-cache helper match

Date: 2026-10-01

`func_100097CC` occupies 109 words and 436 bytes at
`0x100097CC..0x10009980`. Its former zero-return placeholder bypassed the
Init audio loader's 0x800-byte DMA page cache.

The restored function scans the active `struct54` list beginning at
`D_80040F78.unk4`. A request that lies wholly within an existing page refreshes
that node's `unkC` timestamp from `D_8002AE44` and returns the physical address
of the requested offset within the page. The scan retains the insertion point
for a miss.

On a miss, the function rejects an empty free list or all 32 DMA message slots
being occupied. Otherwise it removes the first node from the free list,
repairs both neighboring links, and inserts the node after the retained active
node or at the active-list head. It retains an odd device-address low bit,
aligns the page address, records the page start and current frame, claims the
next `D_80040F98` message slot, and starts an 0x800-byte `osPiStartDma` into the
node's DRAM buffer through `D_80041298`. The return value is that buffer's
physical address with the retained low bit restored. Retail does not otherwise
use the third incoming argument.

The semantic C has retail's exact 109-word extent and 0x38-byte frame. IDO
nevertheless assigns the list cursors, address temporaries, DMA slot, and call
setup differently and schedules independent global-address construction at
different points. Seventy-four relocation-aware, stale-checked guard rows
normalize those compiler-only differences. The remaining 35 words emit
directly from semantic C.

The exhaustive padded-object rebuild and complete ELF link passed. The
authoritative matcher no longer lists `func_100097CC`; a direct comparison of
all 436 bytes reports zero differences, and the linked and retail spans share
SHA-256
`64c77129d302ef6d7adfd48564394809ef11918a2c59289cadfe7a162ba5b0c5`.
The project test suite also passes all 10 tests, with 8 expected skips.

The matcher advances to `3,122 / 5,457 (57.21%)` overall and
`439 / 488 (89.96%)` in Init, with zero address drift and 49 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
