# Game object-entry matrix builder match

Date: 2026-09-30

`func_150F2518` occupies 34 words and 136 bytes at
`0x150F2518..0x150F25A0`. It selects an entry through the object-relative
offset at `0x50`, builds a rotation matrix from entry fields `0x24/0x28`,
writes translation fields `0x18/0x1C/0x20` into the final matrix row, and
converts the result into the `D_800BE9C0`-selected matrix slot at object
offset `0x78`. It returns one.

The semantic C recovers the `0x60` frame, entry-address lifetime, matrix call,
three translation stores, `guMtxF2L` call, and return. Twenty-seven words emit
directly. Seven stale-checked guards normalize one closed address-register
cycle; the HI16/LO16 guards retain their `D_800BE9C0` relocations explicitly.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`0cc68b8a90190392cd5688cf29f8ef05a9496b0b10e7a79980b34d6efdfee906`.
The matcher advances to `3,079 / 5,461 (56.38%)` overall and
`2,500 / 4,788 (52.21%)` in Game, with zero address drift.

Resume with 34-word Game `func_150F2C8C`, the next ordinary matcher row.
