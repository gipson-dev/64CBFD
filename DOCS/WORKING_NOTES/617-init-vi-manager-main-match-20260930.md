# Init VI manager thread match

Date: 2026-09-30

`viMgrMain` occupies 102 words and 408 bytes at
`0x10003658..0x100037F0`. The empty placeholder is replaced with the
canonical libultra VI manager thread body.

The thread receives messages from the VI device manager queue. On each
retrace it swaps the active VI context, decrements the retained retrace
counter, and notifies the current client's queue when that counter expires.
It increments `__osViIntrCount`, samples the hardware count register, and
accumulates the elapsed count into the 64-bit `__osCurrentTime`. Counter
messages dispatch `__osTimerInterrupt`.

Keeping `retrace` as the canonical function-local static is important to
IDO's allocation. An external global makes its address long-lived in `s1`,
which adds an `s8` save and grows the frame from retail's `0x50` to `0x58`.
The function-local static restores the exact frame, saved-register lifetime,
branch topology, and complete 102-word instruction schedule.

Generated-slice padding discards the compact object's temporary `.bss`.
Ten stale-checked relocation-only guards therefore retarget the five `%hi` /
`%lo` pairs from `.bss` to retail `D_80037E30`. Every replacement word equals
its expected compiled word, so no opcode, instruction order, insertion, or
omission is normalized.

The exhaustive shared-guard rebuild compiles every padded object and links
the complete ELF without a stale-guard failure. The whole-ROM checksum gate
remains expectedly incomplete, while the authoritative matcher and direct
408-byte section-span comparison pass. The linked and retail spans share
SHA-256
`5856a698d1f28b707e9768ffe365d925abf9bd588699baec40447970e450a7de`.

The matcher advances to `3,116 / 5,457 (57.10%)` overall and
`433 / 488 (88.73%)` in Init, with zero address drift and 55 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
