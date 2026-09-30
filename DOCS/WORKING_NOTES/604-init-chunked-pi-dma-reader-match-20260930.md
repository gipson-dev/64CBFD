# Init chunked PI DMA reader match

Date: 2026-09-30

`func_100046E4` occupies 74 words and 296 bytes at
`0x100046E4..0x1000480C`. The former zero-return placeholder and obsolete
commented reconstruction are replaced with the recovered synchronous,
chunked PI DMA reader.

The routine maps running-thread IDs three through six onto the corresponding
`gMessageQueue` entry, falling back to queue zero outside that range. It
invalidates the complete destination cache range, then transfers a nonzero
request in chunks no larger than `0x14000` bytes. Each chunk submits a PI DMA
request and blocks on its message queue before advancing the ROM address,
destination pointer, and byte count.

The recovered C uses a typed local aggregate containing the receive message
and complete 24-byte `OSIoMesg`. This documents the actual stack storage and
replaces the previous pointer-local guesses. IDO places that aggregate four
bytes above retail and rounds the frame from `0x80` to `0x88`, while emitting
the rest of the function exactly.

Seventy of 74 words emit directly from semantic C, including the saved
register lifetimes, thread-index clamp, unsigned chunk selection, all three
call relocations, loop updates, and branch delays. Four function- and
offset-scoped guards normalize only the frame allocation, two local-address
constants, and frame release. No words are inserted or removed.

The exhaustive stale-guard rebuild, authoritative matcher, and direct
section-span comparison pass. The linked Init section and pristine image
share SHA-256
`3e86429dbeb207960589ce8b2f3305a853d406b5fc5e3643be4ad4e4c0b95e40`
for the complete function.

The matcher advances to `3,103 / 5,457 (56.86%)` overall and
`420 / 488 (86.07%)` in Init, with zero address drift and 68 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
