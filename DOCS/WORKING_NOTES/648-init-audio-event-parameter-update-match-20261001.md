# Init audio-event parameter update match

Date: 2026-10-01

`func_1000F85C` occupies 48 words and 192 bytes at
`0x1000F85C..0x1000F91C`. It rejects handles below `0x10` and handles that no
longer resolve through `func_1000F3D0`. Valid requests address the active
sound-state pointer in `D_800425E0[arg0 & 0xF].unk8`.

The second argument selects the event parameter. Selector `0x10` converts the
signed cents value in the third argument with `alCents2Ratio` and forwards the
resulting floating-point bits as the event payload. Selector `0x11` aliases to
`0x10`; all other selectors and payloads pass through unchanged. The final
update is submitted through `func_10017714`.

Recovering the selector as `s16` reproduces retail's entry sign extension,
32-byte frame, argument-home stores, branch-likely exits, call sequence, and
saved values. Twenty-six of the 48 words emit directly from semantic C.
Twenty-two stale-checked guards normalize one closed scheduling difference:
the compiler places the converted-payload store in an unconditional branch
delay slot, while retail stores it first and begins table indexing in the
delay slot. The guarded tail also moves the `D_800425E0` HI16/LO16 pair and
`func_10017714` call relocation forward by one word; three earlier guards
adjust forward branch distances to the normalized labels.

The focused object build, serial repository-wide stale rebuild, linked ELF,
authoritative matcher, and direct section-span comparison pass. The linked
and pristine 192-byte spans share SHA-256
`1a0eb4cb47c876f07f4200adf31d43e19fcb899941bb5ffe02d34f9df25e0ee3`.

The matcher advances to `3,147 / 5,457 (57.67%)` overall and
`464 / 488 (95.08%)` in Init, with zero address drift and 24 genuinely
different Init C rows. The next smallest Init candidate is `func_1000A03C`,
which occupies 195 words and currently has 191 real differences.
