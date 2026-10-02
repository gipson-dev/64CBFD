# Game randomized event-descriptor match

Date: 2026-10-02

Game `func_150FFC3C` occupies the 35-word slot at
`0x150FFC3C..0x150FFCC8`. It returns immediately when the pointer at object
offset `0x318` is null. Otherwise it constructs a seven-byte descriptor on the
stack: byte zero is one, the signed halfword at bytes two and three is a random
value from `20` through `30`, byte four is a random value of seven or eight,
byte five is a one-hot mask selected by nested byte `0x23D`, and byte six is
the `-1` terminator. It submits the record through
`func_151D8868(descriptor, 0, 0xFF, 1)`.

The recovered `void func(u8 *)` contract and `s8 descriptor[7]` representation
explain the 32-byte frame and mixed halfword/byte stores. Preserving the source
write order reproduces the two random calls, unsigned modulo by eleven, nested
pointer reload, variable shift, and final argument setup exactly.

All 35 words emit directly from C without expected-word guards or a compiler
profile override. The branch-likely early exit, descriptor stores, calls,
relocations, delay slots, saved return-address lifetime, and `void` epilogue
match in the focused object and final linked image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,537 / 4,788 (52.99%)`, with
2,251 different C rows; overall byte-exact C progress is
`3,205 / 5,456 (58.74%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Continue from [Working Note 700](700-game-script-result-flag-callback-match-20261002.md),
then resume the ordinary small-Game queue with 36-word `func_150D1B40`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
