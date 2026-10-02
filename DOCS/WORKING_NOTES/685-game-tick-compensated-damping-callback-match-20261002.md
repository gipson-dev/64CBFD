# Game tick-compensated damping callback match

Date: 2026-10-02

Game `func_1519C4E4` occupies 34 words at
`0x1519C4E4..0x1519C56C`. Its recovered C reads the elapsed-tick count from
`D_800BE9E4` and, when positive, applies the parameter factor at object offset
`0x134` once per tick to the floating-point values at offsets `0x2C` and
`0x30`. This preserves the retail routine's repeated factor loads and its
branch-likely loop structure.

After damping, the callback compares the signed timer at offset `0x1C` with
the parameter limit at `0x138`. When the timer is below the limit, it forms the
timer-times-scale candidate using the signed halfwords and retail's unsigned
multiply instruction. It stores the low byte at offset `0x5C` only when that
candidate is smaller than the current unsigned byte. The function always
returns one.

The typed parameter view is based at object offset `0x110`, separate from the
older record view used elsewhere in the slice. The complete function emits
directly from semantic C without expected-word guards or a compiler-profile
override and matches all 34 retail words.

The full non-matching link and matcher complete with zero address drift. Game
advances to `2,523 / 4,788 (52.69%)`, with 2,265 different C rows; overall
byte-exact C progress is `3,191 / 5,456 (58.49%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_151A787C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
