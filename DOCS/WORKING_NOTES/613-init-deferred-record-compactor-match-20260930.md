# Init deferred-record compactor match

Date: 2026-09-30

`func_10011310` occupies 91 words and 364 bytes at
`0x10011310..0x1001147C`. The former zero-return placeholder is replaced with
the recovered deferred-record update and compaction routine.

The routine walks the pending four-byte records in `D_80041F10`. Records with
a nonzero delay byte are decremented and retained. A ready record uses its
resource-slot byte to select `D_800425E0`; when the slot identifier matches,
the routine clears the slot state, releases a non-null allocation through
`func_10017594`, and clears the allocation pointer. Ready records reduce the
survivor count, while the original compaction flag and destination index drive
the retail unaligned `lwl/lwr/swl/swr` copy of retained records.

IDO emits an 81-word semantic body with the exact 64-byte frame, saved-register
lifetime, branches, resource release, and unaligned copy. It strength-reduces
the destination index to a pointer and retains the count-global address,
where retail keeps an integer index and repeatedly rematerializes fixed global
addresses. Twenty-six retail words remain direct compiler output. Fifty-five
replacement guards and ten checked insertions reproduce that closed
allocation and scheduling difference. Every guard validates its compiled
source word; input relocations are checked, while fixed retail address words
remain literal because the partial reconstructed data/function layout resolves
those symbols at non-retail addresses.

The exhaustive stale-guard rebuild compiles and links every padded object
without a guard failure. The authoritative matcher and direct 364-byte
section-span comparison pass. The linked and retail spans share SHA-256
`828a7eefa3237b51cd4f4828947fcfdee4611afc4a363d0e04d2506cbcfc4d9a`.

The matcher advances to `3,112 / 5,457 (57.03%)` overall and
`429 / 488 (87.91%)` in Init, with zero address drift and 59 genuinely
different Init C rows. The corrected `D_80041F10` declaration also preserves
the adjacent byte-exact `func_100112BC` result.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
