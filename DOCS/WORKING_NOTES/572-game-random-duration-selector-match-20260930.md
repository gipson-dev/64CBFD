# Game random-duration selector match

Date: 2026-09-30

`func_1507F4C0` occupies 35 words and 140 bytes at
`0x1507F4C0..0x1507F54C`. Mode zero returns a random value in `180..239`.
Mode one returns a random value in `60..119`, while other nonzero modes return
one in `0..29`. All nonzero modes return zero when `D_800BE9F0` is `0x31`.

Reusing the incoming parameter as the selected modulus recovers retail's
control flow, branch-likely delay slots, PRNG call, unsigned remainder, and
addition directly. Twenty-nine words emit from semantic C. Six stale-checked
guards normalize one closed compiler-allocation cycle: the `0x28` frame and
the spill/reload slots for the base and range that remain live across the
PRNG call.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`55ec7967c98d5eabe2b7d0293f09b16178590c39b8639308c777852b2ed1d4d2`.
The matcher advances to `3,074 / 5,461 (56.29%)` overall and
`2,495 / 4,788 (52.11%)` in Game, with zero address drift.

Resume with 34-word Game `func_150B0C58`, the next ordinary matcher row.
