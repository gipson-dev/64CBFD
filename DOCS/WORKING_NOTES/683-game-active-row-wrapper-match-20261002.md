# Game active-row wrapper match

Date: 2026-10-02

Game `func_1517F4D8` occupies 35 words at
`0x1517F4D8..0x1517F564`. Its recovered C first checks the indexed timer in
`D_800DDE10` and mapped mode in `D_800DDD9C`. If either is zero, it returns the
incoming handle unchanged. For an active row, it indexes the three-byte entry
in `D_800DDD90` and calls `func_1517F08C` with the handle, mapped mode, all
three row bytes, and the original row index.

The direct indexed expressions reproduce retail's early table-address
calculations, two shared unchanged-handle exits, multiply-by-three row address,
byte-load ordering, stack arguments, call delay slot, and common epilogue. The
complete routine emits directly from semantic C without expected-word guards
or a compiler-profile override and matches all 35 retail words.

The full non-matching link and matcher complete with zero address drift. Game
advances to `2,521 / 4,788 (52.65%)`, with 2,267 different C rows; overall
byte-exact C progress is `3,189 / 5,456 (58.45%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_1518B1D8`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.

## Superseded resume point

`func_1518B1D8` was subsequently recovered and byte-matched in
[Working Note 684](684-game-clamped-height-byte-match-20261002.md). Resume the
ordinary queue with 34-word `func_1519C4E4`; the two parked special cases above
remain unchanged.
