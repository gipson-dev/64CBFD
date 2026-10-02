# Game counted resource-owner teardown match

Date: 2026-10-02

Game `func_151EDB58` occupies the 33-word slot at
`0x151EDB58..0x151EDBDC`. A null owner returns immediately. Otherwise the
routine releases the auxiliary resource at offset `0x24`, frees the owner
allocation with heap selector 4, and then releases the count-sized pointer
array beginning at offset `0x04`. The loop reloads the unsigned count byte at
offset `0x14` after each release, matching retail's observable memory-access
order.

The recovered local type records the pointer-array, count, and auxiliary
resource offsets. Its semantic C body emits all 33 retail words directly under
the slice's existing compiler profile. The frame, three saved-register
lifetimes, early branch-likely delay slot, release ordering, loop branch-likely
delay slot, and epilogue all match without expected-word guards.

The function-specific object disassembly is exact. A full non-matching link
and linked matcher also complete with zero address drift. Game advances to
`2,528 / 4,788 (52.80%)`, with 2,260 different C rows; overall byte-exact C
progress is `3,196 / 5,456 (58.58%)`. Init remains `487 / 487 (100.00%)` and
Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_150227BC`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
