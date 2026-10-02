# Game mode dispatcher match

Date: 2026-10-02

Game `func_15170EC4` occupies 34 words at
`0x15170EC4..0x15170F4C`. Its recovered C dispatches on global mode
`D_800BE9F0`. Mode 2 calls `func_15170B90` with parameters `(1, 1, 1)`;
mode `0x10` uses `(0xA9, 8, 0)`. Both paths forward the low byte of the
caller's second argument and the complete third argument as the two stack
arguments. Other modes return without calling the worker.

Declaring the selector as `u8` reproduces retail's ABI-word home followed by
the least-significant-byte reload. Expressing the control flow as a sparse
`switch` reproduces the two forward equality branches, explicit default exit,
case ordering, call delay slots, and shared epilogue. The complete routine
emits directly from semantic C without expected-word guards or a compiler
profile override and matches all 34 retail words.

The full non-matching link and matcher complete with zero address drift. Game
advances to `2,520 / 4,788 (52.63%)`, with 2,268 different C rows; overall
byte-exact C progress is `3,188 / 5,456 (58.43%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_1517F4D8`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
