# Game attachment-state transition match

Date: 2026-10-02

Game `func_15074664` occupies the 35-word slot at
`0x15074664..0x150746F0`. If the current object has an attachment at offset
`0x31C`, requested state `D_800D1580 == 1` calls `func_10011FDC(5)`. For other
requested states, a prior attachment state byte of one calls
`func_10011FDC(0)`. Each call is followed by the retail attachment/global
reloads before the requested state is written to byte `0x94`.

The existing semantic body compiled to 37 words and therefore selected the
layout tool's retail-overflow fallback. It duplicated the final state store
between branches and compared signed `struct126::unk94`, producing `lb` rather
than retail's `lbu`. Casting the comparison to `u8` and joining both branches
at one final assignment produces the complete retail control flow and exact
35-word length.

All 35 words emit directly from C without expected-word guards or a compiler
profile override. The frame, branch-likely exits and delay-slot stores, both
calls, global and attachment reloads, shared state store, and epilogue match in
the raw object and final linked image.

The incremental object rebuild, full link, and linked matcher complete with
zero address drift. Game advances to `2,533 / 4,788 (52.90%)`, with 2,255
different C rows; overall byte-exact C progress is
`3,201 / 5,456 (58.67%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is source-shape
recovery, raw-object comparison, full-link, and linked-word comparison
evidence.

The next checkpoint completed 36-word `func_15080C64`; see
[Working Note 696](696-game-resource-teardown-finalizer-match-20261002.md).
Resume the ordinary small-Game queue with 35-word `func_150CBA30`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
