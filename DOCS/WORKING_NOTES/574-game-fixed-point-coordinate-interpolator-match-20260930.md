# Game fixed-point coordinate interpolator match

Date: 2026-09-30

`func_150B73F0` occupies 37 words and 148 bytes at
`0x150B73F0..0x150B7484`. It divides the signed 16.16 progress value at offset
`0x24` by the duration at `0x1C`, interpolates the signed halfword X endpoints
at `0x18/0x20` and Y endpoints at `0x1A/0x22`, and writes float coordinates at
`0x2C/0x30`.

The direct arithmetic C recovers the complete instruction schedule: endpoint
loads, signed divide and both hardware trap checks, two fixed-point multiplies,
arithmetic shifts, integer-to-float conversions, stores, and return. Thirteen
words emit directly. The remaining 24 words differ only in register fields and
form one closed compiler-allocation cycle. Scoped stale-checked guards normalize
that cycle without changing opcodes, immediates, instruction order, control
flow, or relocations.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`5ff8bb8bebad3257d3ce7d34f41d03f4517bd0b6c4e0cf9afd7692eeb9c41e18`.
The matcher advances to `3,076 / 5,461 (56.33%)` overall and
`2,497 / 4,788 (52.15%)` in Game, with zero address drift.

Resume with 34-word Game `func_150D5440`, the next ordinary matcher row.
