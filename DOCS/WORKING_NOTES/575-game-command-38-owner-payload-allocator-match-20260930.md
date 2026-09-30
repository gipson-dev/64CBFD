# Game command-0x38 owner-payload allocator match

Date: 2026-09-30

`func_150D5440` occupies 34 words and 136 bytes at
`0x150D5440..0x150D54C8`. It constructs a 12-byte payload containing the
incoming owner pointer, the owner's byte at offset `0x3B`, and a zero float.
It calls `func_15149130` for command `0x38`, subtype `0x28`, payload size 12,
and the caller's final two arguments. A successful allocation receives the
payload at offset `0x28`; allocation failure returns without copying.

This routine is a structural twin of `func_150B0C58`. The same typed payload
and allocator declaration recover the retail `0x40` frame, incoming argument
homes, payload stores, nine-argument call, null branch, and 12-byte `memcpy`.
All 34 words and both call relocations emit directly from semantic C with no
expected-word guards.

The focused object, complete relink, authoritative matcher, and direct span
comparison pass. The linked ELF and retail spans share SHA-256
`797214ab3db1016376fa9239eb154a0fe954d86f45ae7fbe845a7ba3e71f34fa`.
The matcher advances to `3,077 / 5,461 (56.34%)` overall and
`2,498 / 4,788 (52.17%)` in Game, with zero address drift.

Resume with 35-word Game `func_150F15F8`, the next ordinary matcher row.
