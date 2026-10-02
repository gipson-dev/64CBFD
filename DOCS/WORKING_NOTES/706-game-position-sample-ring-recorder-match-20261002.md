# Game position-sample ring recorder match

Date: 2026-10-02

Game `func_1515CF9C` occupies the 37-word slot at
`0x1515CF9C..0x1515D030`. While the current sample count at offset `0x2C` is
below capacity minus one, it increments that count and appends a sample to the
16-byte ring record selected by the signed write cursor at offset `0x2E`.
The sample contains the 12-byte position at object offset `0x10` followed by
the float at status-buffer offset `0x8`. The routine then increments and wraps
the write cursor. When no slot remains, it writes signed status `-1` at status
offset `0x39`. Every path returns one.

The prior body had the right broad behavior but cached one byte-addressed slot
for all four stores. IDO consequently repurposed `a1`, copied the status
pointer to `a2`, and emitted 34 real differences. Recovering the signed `s8 *`
status contract produces retail's full-width `-1`, while a 12-byte position
struct assignment reproduces the compact three-word copy. Addressing the
float field separately recovers retail's second signed-index calculation.

The semantic C emits the first 28 words and the final common operations in
retail order. Four expected-word guard entries normalize only the closed
five-word reset/exit schedule: two branch displacements, the reset store, the
unconditional branch, and its return-value delay slot. One guard inserts that
branch, preserving the 37-word retail slot. No compiler-profile override is
used.

The focused object, complete repository rebuild against the guard manifest,
full relink, and linked matcher complete with zero address drift. Game
advances to `2,545 / 4,788 (53.15%)`, with 2,243 different C rows; overall
byte-exact C progress is `3,213 / 5,456 (58.89%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object disassembly, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 37-word `func_1518F7C4`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
