# Game timer/position and byte-clamp match

Date: 2026-10-02

Game `func_150CBA30` occupies the 35-word slot at
`0x150CBA30..0x150CBABC`. It subtracts `D_800BE9E4` from the signed halfword
timer at offset `0x128` and stores the truncated result. While the reloaded
timer remains positive, it multiplies the float at `0x12C` by
`D_800BE9A4` and adds that delta to both float fields at `0x2C` and `0x30`.

When bit zero of the word at `0x58` is set, the routine loads the signed
halfword at `0x1C`. Values below `0x20` are shifted left three bits and lower
the unsigned byte at `0x5C` when the shifted result is smaller. The function
returns one on every path.

The first semantic body had the exact 35-word length but only 27 matching
words. Naming the timer local allowed the compiler to reuse its register for
the later clamp value, producing an equivalent but different allocation.
Testing the reloaded timer field directly splits those lifetimes and recovers
all eight remaining retail words.

All 35 words emit directly from C without expected-word guards or a compiler
profile override. The timer subtraction and reload, floating-point updates,
flag test, signed range check, byte comparison/store, relocations, branches,
delay slots, and return value match in the focused object and final linked
image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,535 / 4,788 (52.94%)`, with
2,253 different C rows; overall byte-exact C progress is
`3,203 / 5,456 (58.71%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Continue from [Working Note 698](698-game-vector-argument-forwarder-match-20261002.md),
then resume the ordinary small-Game queue with 35-word `func_150FFC3C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
