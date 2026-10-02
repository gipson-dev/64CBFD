# Game mode-offset adjuster match

Date: 2026-10-02

Game `func_151CD224` occupies the 39-word slot at
`0x151CD224..0x151CD2BC`. It first calls `func_151CC1D4` to sample the current
control value. The recovered body then uses the embedded record at object
offset `0x70` to calculate
`(1.0f - (sampled - offset) * scale) * 75.0f`. Record mode 5 writes
`92.0f + adjustment` to object offset `0x14`; mode 4 writes
`-92.0f - adjustment`; other modes leave the output unchanged.

The compact semantic body emits 35 instructions. Retail retains a shared
record base in `v0`, while IDO folds its three accesses into the object base
and uses `v0` rather than `v1` for the mode. Six stale-checked patch rows
normalize only that compiler decision: one checked instruction insertion,
three dependent record accesses, and two branch-register operands. The
generated-object layout tool retains the final three retail padding nops, so
all 39 words match. No relocation-bearing instruction is changed.

The full non-matching rebuild and linked matcher complete with zero address
drift. Game advances to `2,526 / 4,788 (52.76%)`, with 2,262 different C
rows; overall byte-exact C progress is `3,194 / 5,456 (58.54%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full-link, stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_151D7538`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
