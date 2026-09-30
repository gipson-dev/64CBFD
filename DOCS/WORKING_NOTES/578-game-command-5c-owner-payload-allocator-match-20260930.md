# Game command-0x5C owner-payload allocator match

Date: 2026-09-30

`func_150F2C8C` occupies 34 words and 136 bytes at
`0x150F2C8C..0x150F2D14`. It constructs a 16-byte payload containing the
incoming owner pointer, the owner's identity byte at offset `0x3B`, two
explicitly cleared byte fields, and a zero float. It calls `func_15149130`
for command `0x5C`, allocator argument `0x44`, payload size 16, and fixed
final arguments `0xFF` and one. A successful allocation receives the payload
at offset `0x28`; allocation failure returns without copying.

The recovered payload type and allocator declaration reproduce the retail
`0x48` frame, incoming argument home, payload stores, nine-argument call,
null branch, and 16-byte `memcpy`. All 34 words and both call relocations emit
directly from semantic C with no expected-word guards.

The focused object, complete relink, authoritative matcher, and direct span
comparison pass. The linked ELF and retail spans share SHA-256
`4c4e9b52574cae5bba65ecb5a0911f8b0ec9895325756631c3dc9a13157fe95b`.
The matcher advances to `3,080 / 5,461 (56.40%)` overall and
`2,501 / 4,788 (52.23%)` in Game, with zero address drift.

Resume with 35-word Game `func_150F7310`, the next ordinary matcher row.
