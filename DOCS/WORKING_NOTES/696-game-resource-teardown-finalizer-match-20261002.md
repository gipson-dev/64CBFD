# Game resource-teardown finalizer match

Date: 2026-10-02

Game `func_15080C64` occupies the 36-word slot at
`0x15080C64..0x15080CF4`. It returns immediately when `D_800D1941` is clear or
byte `0x15` of the record referenced by `D_800D1950` is nonzero. Otherwise it
calls `func_15080BE8` to release the owned resources. Outside categories
`0x29` and `0x2E`, it sets bit `0x10` in `D_800D2E60[8]`. If the pending record
at `D_800D199C` exists, the function sets its byte `0x14` to one and clears the
global pointer.

The recovered function has a `void` contract; the retail body establishes no
return value. A first semantic form with a named record pointer had the right
36-word length but used a different closed temporary-register allocation.
Testing byte `0x15` directly from the global pointer recovers retail's `t7` and
`t8` lifetimes as well as the downstream `t9`, `t0`, and `t1` allocation.

All 36 words emit directly from C without expected-word guards or a compiler
profile override. Both branch-likely early exits, the teardown call, category
tests, global bit update, pending-record writes, relocations, and epilogue
match in the focused object and final linked image.

The incremental generated-slice rebuild, full link, and linked matcher
complete with zero address drift. Game advances to
`2,534 / 4,788 (52.92%)`, with 2,254 different C rows; overall byte-exact C
progress is `3,202 / 5,456 (58.69%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_150CBA30`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
