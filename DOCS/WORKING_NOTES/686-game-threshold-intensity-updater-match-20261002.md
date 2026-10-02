# Game threshold/intensity updater match

Date: 2026-10-02

Game `func_151A787C` occupies 35 words at
`0x151A787C..0x151A7908`. Its recovered `void` callback reads the signed timer
at object offset `0x38` and the parameter block based at offset `0x50`. Below
the first parameter threshold, it writes the timer-times-scale result to byte
`0x3F`.

Below the second threshold, the callback multiplies the signed step parameter
by `D_800BE9E4`, adds the result to both halfwords at offsets `0x34` and
`0x36`, and reloads the timer. It then always multiplies the current timer by
the parameter at offset `0x52` and writes the low byte to offsets `0x42`,
`0x41`, and `0x40`. The recovered signature is `void`, matching the retail
routine's lack of a defined return value.

Nineteen of the 35 words emit directly from semantic C. Sixteen stale-checked
expected-word rows normalize one commutative multiply operand order and a
closed compiler register-allocation and instruction-scheduling cycle in the
second half. The conditions, elapsed-tick multiplication, two field updates,
timer reload, three output stores, and all control-flow edges remain explicit
in C.

The full non-matching link and whole-tree stale-guard sweep complete with zero
address drift. Game advances to `2,524 / 4,788 (52.72%)`, with 2,264 different
C rows; overall byte-exact C progress is `3,192 / 5,456 (58.50%)`. Init
remains `487 / 487 (100.00%)` and Debugger remains
`181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 34-word `func_151B498C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.

## Superseded resume point

`func_151B498C` was subsequently recovered and byte-matched in
[Working Note 687](687-game-output-default-initializer-match-20261002.md).
Resume the ordinary queue with 39-word `func_151CD224`; the two parked special
cases above remain unchanged.
