# Game trigonometric lookup match

Date: 2026-10-02

Game `func_150489B0` occupies the 36-word slot at
`0x150489B0..0x15048A40`. It accepts a byte angle and divides its range at
`0x41`, `0x81`, and `0xC1`. The four paths select `D_8009A220[arg0]`,
`-D_8009A420[-arg0]`, `-D_8009A020[arg0]`, or
`D_8009A620[-arg0]`. These reflected table accesses and signs reconstruct the
full periodic result from the four retail table anchors.

The recovered `f32 func_150489B0(u8)` contract is supported by the floating
return register and existing typed callers. The semantic body emits the
complete 36-word length and 31 retail words directly. Five stale-checked,
non-relocation words normalize the compiler's equivalent negate-before-shift
array indexing into retail's shift-before-negate byte-offset schedule. All
branches, four table HI/LO relocation pairs, floating loads/sign changes, and
the return path emit directly from C.

Correcting the callee contract changed adjacent 12-word `func_15048A40` from
its previously exact schedule even though its quarter-turn behavior remained
the same. Seven additional stale-checked words preserve retail's argument
normalization, relocated call position, delay slot, and epilogue. Both coupled
slots are byte-exact in the focused object and final linked image.

The shared patch-table rebuild, full link, and linked matcher complete with
zero address drift. Game advances to `2,532 / 4,788 (52.88%)`, with 2,256
different C rows; overall byte-exact C progress is
`3,200 / 5,456 (58.65%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
coupled-slot object comparison, two complete stale-guard rebuilds, full-link,
and linked-word comparison evidence.

Resume the ordinary small-Game queue with 35-word `func_15074664`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
