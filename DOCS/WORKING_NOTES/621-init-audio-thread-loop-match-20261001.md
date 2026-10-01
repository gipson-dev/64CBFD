# Init audio thread loop match

Date: 2026-10-01

`func_10009400` occupies 104 words and 416 bytes at
`0x10009400..0x100095A0`. Its former empty placeholder discarded the main
Init audio thread, while a commented draft retained enough structure to
recover the retail routine.

The restored thread initializes the audio state through `func_100051C8`, then
blocks on `D_8003E5D0`. Message type 1 drives a two-frame cycle. On the first
successful `func_100095A0` submission after startup, the thread receives a
completion message from `D_8003E608` and retains its audio token for the next
submission. Message types 4 and 10 terminate the active loop. A global
shutdown request rewrites the current message to type 4 before dispatch.

After termination, the thread calls `n_alClose` for `D_8003E640` and enters
retail's permanent receive loop. Recovering the `switch` statement restores
the exact branch topology, including the duplicated completion assignments
for the two terminal cases. The frame size, saved-register lifetime, call
sequence, two-frame counter update, and all branch extents compile with the
retail shape.

IDO still chooses different stack homes for three locals, swaps the closed
lifetimes of `s3` and `s4`, copies the constant one from `fp` in three delay
slots, and schedules the close setup differently. Twenty-two stale-checked
replacement rows normalize those words; one also carries a relocation-aware
insertion that retains retail's close-address completion after preparing the
terminal message pointer. Five checked omission rows remove one dead counter
clear, one dead message-type clear, and three trailing alignment nops. The
total is 27 guarded rows; none changes the recovered behavior.

The focused object build, complete ELF link, authoritative matcher, project
tool tests, and direct 416-byte section-span comparison pass. The linked and
retail spans share SHA-256
`2a41b5bdbbeefb67b41d391642d2911785132b61f5f7be1a10bc9d3dda894e94`.

The matcher advances to `3,120 / 5,457 (57.17%)` overall and
`437 / 488 (89.55%)` in Init, with zero address drift and 51 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
