# Init bidirectional heap allocator match

Date: 2026-10-01

`func_10003C6C` occupies 258 words and 1,032 bytes at
`0x10003C6C..0x10004074`. Its previous C body returned zero even though the
retail routine is the core Init heap allocator used by `allocate_memory` and
multiple Game callers.

The recovered body records the request diagnostics, applies the selected
alignment class, enforces the optional low-memory gate, and searches the free
list from either its head or tail. It allocates from the requested end of a
candidate block, either splits or consumes that block, repairs the physical
neighbor chain and the independent free-list links, preserves the allocation
type in the high byte, and recomputes the largest-free-block record when the
selected block owned it. Failure restores the interrupt mask and retains the
retail optional fatal-dispatch path.

IDO emits the complete semantic control flow in the exact 258-word extent and
preserves its single saved-register lifetime. Forty-two words emit directly.
Two hundred sixteen function-scoped, stale-checked rows normalize the closed
frame, stack-slot, register-allocation, and scheduling differences; 42 rows
carry relocation changes explicitly. No insertion, omission, padding, or
resolved-address binary patch is used.

A targeted object rebuild accepts every expected word and relocation, and the
full linked ELF completes successfully. Direct comparison of
`0x10003C6C..0x10004074` reports zero different bytes. Both 1,032-byte spans
share SHA-256
`7b188602de53c31d0fc1e07510cee2edd09e91b94dff1e5a1f295a026afdcaea`.

The refreshed matcher reports `3,154 / 5,456 (57.81%)` byte-exact C functions
overall and `471 / 487 (96.71%)` in Init, with zero address drift and 16
different Init C rows. The next smallest measured Init candidate is the
271-word `func_10008F90`, currently different in 266 words.
