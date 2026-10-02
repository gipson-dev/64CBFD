# Game global-position query match

Date: 2026-10-02

Game `func_150FCF1C` occupies the 37-word slot at
`0x150FCF1C..0x150FCFB0`. It reads the signed three-halfword coordinate source
referenced by `D_800D9AA0`. A null source returns `1.0f`. Otherwise, the
routine converts the three coordinates to a local float vector and returns
the result of `func_15165BB0(arg0, position, 0x44FAE000, 0x460CB400,
D_800A1F2C)`.

The recovered `f32 func(u8 *)` contract preserves the floating return in
`f0`. The two hexadecimal call arguments are full-width integer parameters,
not source-level floating constants; this reproduces their `lui`/`ori`
construction in `a2` and `a3`. The three signed-halfword loads, integer-to-float
conversions, global scalar load, call order, null fast path, and branch delay
slots all compile in the retail order.

IDO persistently places the semantic three-float array at `sp+0x24`, while
retail addresses the same 12-byte vector at `sp+0x20` within the unchanged
`0x30`-byte frame. Four expected-word guards normalize the vector address and
three stores by four bytes. The remaining 33 words emit directly from C; no
compiler-profile override is used.

The focused generated-object build, full repository link, and linked matcher
complete with zero address drift. Game advances to
`2,543 / 4,788 (53.11%)`, with 2,245 different C rows; overall byte-exact C
progress is `3,211 / 5,456 (58.85%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object disassembly, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 37-word `func_15142B7C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
