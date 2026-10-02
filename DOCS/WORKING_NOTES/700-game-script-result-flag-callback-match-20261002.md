# Game script-result flag callback match

Date: 2026-10-02

Game `func_150C7350` occupies the 36-word slot at
`0x150C7350..0x150C73E0`. It first sets flags `0x80004000` in the word at
object offset `0x84`. It then calls
`func_1509BE40(3, 0x2000, 0xAC, 0x4002, 0x4003, 0x4004)`. A nonzero result
sets bit `0x00400000`; a zero result clears that bit.

The recovered `void func(u8 *)` contract keeps the object pointer in `s0`
across the variable-argument script query. Expressing the nonzero path as a
set followed by an early return reproduces retail's branch-likely zero path,
its delay-slot flag reload, and the taken-path branch to the shared epilogue.

All 36 words, including the trailing alignment word, emit directly from C
without expected-word guards or a compiler profile override. The 40-byte
frame, `s0` and return-address lifetimes, six call arguments, flag loads and
stores, masks, relocation, branches, delay slots, epilogue, and final padding
match in the focused object and final linked image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,538 / 4,788 (53.01%)`, with
2,250 different C rows; overall byte-exact C progress is
`3,206 / 5,456 (58.76%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 36-word `func_150D1B40`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
