# Init allocator free coalescing match

Date: 2026-10-01

`func_10004074` occupies 119 words and 476 bytes at
`0x10004074..0x10004250`. Its former zero-return placeholder discarded the
allocator's complete free and coalescing path.

The restored function accepts a payload pointer and recovers its 12-byte block
header. A null payload returns without changing allocator state. Otherwise it
saves the caller's interrupt mask, marks the block free, and inspects the
adjacent physical blocks. A free predecessor absorbs the current block, and a
free successor is then absorbed into the resulting block. Both paths repair
the physical predecessor/successor links.

Successor coalescing also removes the absorbed block from the doubly linked
free list and repairs the list head when necessary. When no physical merge is
possible, the block is inserted into the free list in address order, including
the empty-list and new-head cases. The final path updates the free-list tail,
refreshes the cached largest free size and block when required, and restores
the saved interrupt mask.

The semantic C recovers the complete retail extent and control flow. A byte
store clears only the high allocation-status byte while preserving the packed
size. Explicit predecessor and successor lifetimes preserve the two distinct
physical and free-list link domains. IDO still chooses a different frame,
register allocation, branch layout, and schedule across most of the routine.
Ninety-five relocation-aware, stale-checked guard rows normalize those
compiler-only words, including both `osSetIntMask` calls and the allocator
global references. Twenty-four words emit directly from semantic C.

The exhaustive padded-object rebuild and complete ELF link passed. The
authoritative matcher no longer lists `func_10004074`; a direct comparison of
all 476 bytes reports zero differences, and the linked and retail spans share
SHA-256
`f1baa8fbaeb74356ce2ff072fab39380ec3e2f06dab02e7ef33269f8eb04567c`.
The 95 guard offsets are unique. Project tool checks pass. The focused unit
suite passes all 10 tests, with 8 expected skips.

The matcher advances to `3,125 / 5,457 (57.27%)` overall and
`442 / 488 (90.57%)` in Init, with zero address drift and 46 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
