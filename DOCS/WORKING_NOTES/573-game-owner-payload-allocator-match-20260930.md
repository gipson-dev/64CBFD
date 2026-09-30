# Game owner-payload allocator match

Date: 2026-09-30

`func_150B0C58` occupies 34 words and 136 bytes at
`0x150B0C58..0x150B0CE0`. It constructs a 12-byte payload containing the
incoming owner pointer, the owner's byte at offset `0x3B`, and a zero float.
It calls `func_15149130` for command `0x58`, subtype `0x43`, payload size 12,
and the caller's final two arguments. A successful allocation receives the
payload at offset `0x28`; allocation failure returns without copying.

The typed payload and allocator declaration recover the retail `0x40` frame,
incoming argument homes, payload stores, nine-argument call, null branch, and
12-byte `memcpy`. All 34 words and both call relocations emit directly from
semantic C with no expected-word guards.

The focused object, complete relink, authoritative matcher, and direct span
comparison pass. The linked ELF and retail spans share SHA-256
`ac0b02a319621df6c63c1acb70a87ca4951000e4a82f9cd3b68178ad0abe2ba2`.
The matcher advances to `3,075 / 5,461 (56.31%)` overall and
`2,496 / 4,788 (52.13%)` in Game, with zero address drift.

Resume with 37-word Game `func_150B73F0`, the next ordinary matcher row.
