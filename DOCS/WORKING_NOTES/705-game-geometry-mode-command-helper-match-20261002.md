# Game geometry-mode command helper match

Date: 2026-10-02

Game `func_15142B7C` occupies the 37-word slot at
`0x15142B7C..0x15142C10`. It compares requested clear-mode bits against
`D_800DD200` and requested set-mode bits against `D_800DD1FC`. For each group
containing uncached bits, it appends the corresponding geometry-mode command
to the display list, merges the requested bits into that cache, and returns
the advanced display-list cursor.

The prior semantic body manually expanded both graphics commands into their
two display-list words. Although behaviorally equivalent, that form let IDO
store through `a0` before advancing the cursor and produced 34 real word
differences. Recovering the original `gSPClearGeometryMode(arg0++, arg2)` and
`gSPSetGeometryMode(arg0++, arg1)` expressions restores retail's `v0` command
pointer, pre-store cursor increments, command-store order, cache pointers,
branches, and delay slots.

All 37 words emit directly from semantic C without expected-word guards or a
compiler-profile override. The focused object, final linked image, and both
global-data relocation pairs match retail.

The incremental object build, full link, and linked matcher complete with zero
address drift. Game advances to `2,544 / 4,788 (53.13%)`, with 2,244 different
C rows; overall byte-exact C progress is `3,212 / 5,456 (58.87%)`. Init
remains `487 / 487 (100.00%)` and Debugger remains
`181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object disassembly, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 37-word `func_1515CF9C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
