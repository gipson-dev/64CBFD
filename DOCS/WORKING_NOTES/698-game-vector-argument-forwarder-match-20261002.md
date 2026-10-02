# Game vector-argument forwarder match

Date: 2026-10-02

Game `func_150E3340` occupies the 35-word slot at
`0x150E3340..0x150E33CC`. It forwards a three-word vector twice as the first
six arguments to `func_150E3020`, then supplies mode `0x1A`, scale `10.0f`,
and a zero argument. A three-float vector follows, along with the incoming
word and signed-halfword parameters.

The recovered `void func(f32 *, s32 *, s32, s16)` contract explains the retail
incoming-register spills and the signed halfword reload from the low half of
the stored fourth argument. Writing the fourteen-argument call directly also
reproduces the vector loads, duplicate argument placement, constant setup,
stack argument order, and final float store in the call delay slot.

All 35 words emit directly from C without expected-word guards or a compiler
profile override. The 64-byte frame, saved return-address lifetime, argument
spills, loads, stores, call relocation, delay slot, and `void` epilogue match
in the focused object and final linked image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,536 / 4,788 (52.97%)`, with
2,252 different C rows; overall byte-exact C progress is
`3,204 / 5,456 (58.72%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_150FFC3C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
