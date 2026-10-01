# Init audio request allocator match

Date: 2026-10-01

`func_1000FA64` occupies 109 words and 436 bytes at
`0x1000FA64..0x1000FC18`. Its former zero-return placeholder discarded the
construction and submission of an Init audio request.

The restored function rejects allocation when all 32 request records are in
use, reserves the next `D_80041FE0` record, and derives its flags from the
callback and caller-supplied mode. Flag `0x40` replaces the vertical coordinate
through `func_15083E0C` and aborts when that lookup returns `-1`.

The successful path stores the packed identifier, coordinates, volume and
range fields; records the callback, owner, identifier and request metadata;
clears the runtime-owned status fields; and converts the pitch value through
`alCents2Ratio`. It then submits the allocated range through `func_10011624`.
If submission changes the global count, the function returns zero. Otherwise
it sets committed flag `0x1000` and returns the request handle.

The semantic C recovers the complete retail extent and control flow. Taking
the address of the narrow vertical-coordinate argument keeps it in its ABI
stack home, matching the retail halfword update while freeing `a2` for the
queue index. One aligned 32-bit clear expresses the adjacent status-halfword
initialization without exceeding the fixed slot. IDO still chooses a larger
frame and retains `index + 1` across both calls, displacing most integer
allocation and scheduling. One hundred relocation-aware, stale-checked guard
rows normalize those compiler-only words, including movement of both calls
and the `D_80042760` and `D_80041FE0` address pairs. Nine words emit directly
from semantic C.

The exhaustive padded-object rebuild and complete ELF link passed. The
authoritative matcher no longer lists `func_1000FA64`; a direct comparison of
all 436 bytes reports zero differences, and the linked and retail spans share
SHA-256
`d8f6e2f920e541908664a49316ed5a4d01e494969639bdb3023beedc2b706e30`.
Project tool checks pass. The focused unit suite passes all 10 tests, with 8
expected skips.

The matcher advances to `3,124 / 5,457 (57.25%)` overall and
`441 / 488 (90.37%)` in Init, with zero address drift and 47 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
