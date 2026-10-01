# Init controller-pak write transaction match

Date: 2026-09-30

`__osContRamWrite` occupies 140 words and 560 bytes at
`0x10025870..0x10025AA0`. The existing SDK-derived body already handled the
write request, readback validation, controller status check, bounded retries,
and serial-interface ownership, but omitted Conker's preparation before each
readback DMA.

The recovered retry-loop preparation fills all 16 words of the 64-byte
`__osPfsPifRam` with the 32-bit value `0x000000FF`, then clears its status
word. Retail performs this initialization before every readback attempt. The
nonzero channel-error path keeps the value already extracted by `CHNL_ERR`;
removing the redundant `PFS_ERR_NOPACK` assignment eliminates two stores and
the branch needed to skip them, restoring retail's exact control-flow extent.

The complete 140-word routine emits directly from C with its 96-byte frame,
retry loop, early status-error return, and saved-register lifetime intact. No
expected-word guards, relocation rewrites, insertions, or omissions are used.
The adjacent `__osPackRamWriteData` remains byte-exact in the same object.

The focused object build, complete ELF link, authoritative matcher, ten
project tool tests, and direct 560-byte section-span comparison pass. The
linked and retail spans share SHA-256
`dee476f995e4d64d1d057744683116e6245a537352bd0740fc1a74e405c33adc`.

The matcher advances to `3,119 / 5,457 (57.16%)` overall and
`436 / 488 (89.34%)` in Init, with zero address drift and 52 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
