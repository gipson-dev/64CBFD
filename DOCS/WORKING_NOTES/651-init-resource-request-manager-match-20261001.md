# Init resource-request manager match

Date: 2026-10-01

`func_10009CBC` occupies 208 words and 832 bytes at
`0x10009CBC..0x10009FFC`. An odd caller value is an encoded resource request;
an even value is an existing manager-node handle. For a new request, the
routine decodes the resource identifier and transfer size, then takes a node
from the free list or evicts the last inactive eligible node from the active
list. The selected node is unlinked from its old list and inserted at the head
of the active list.

The new-request path allocates a rounded transfer buffer, clears it, performs
the required data-cache writeback and invalidation, and records the request
metadata. It preserves the retail ordering that saves the old DMA-message
index, advances the global index before the transfer call, and uses the old
index to select `D_80041330`. The PI transfer is submitted with
`OS_MESG_PRI_HIGH`, and the caller's encoded value is replaced with the
selected node. The existing-handle path updates node state and reference
tracking before returning the resource pointer.

The recovered semantic C emits the retail 88-byte frame and 205 words. One
hundred seven function-scoped, stale-checked rows normalize the remaining
closed IDO register-allocation and instruction-scheduling cycle. Three checked
insertions expand the result to the 208-word retail slot. Unlike the preceding
Init matches, this schedule requires explicit relocation-aware rows: address
pairs for `D_8002AE50`, `D_80041330`, and `D_800416F0`, together with affected
calls, are moved or retargeted to their retail words without changing the
recovered behavior.

The focused build, full serial stale-check rebuild, final ELF link,
authoritative matcher, direct section-span comparison, and all 11 repository
tool unit tests pass. The clean build reaches the expected whole-ROM SHA-1
failure because other functions still differ. The linked and pristine spans
share SHA-256
`aa485f43fb54b12658083b22b286f6e3c97cf462aa1e1e6f7637cc2bbaec7131`.

The matcher advances to `3,150 / 5,457 (57.72%)` overall and
`467 / 488 (95.70%)` in Init, with zero address drift and 21 genuinely
different Init C rows.
