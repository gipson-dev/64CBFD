# Game attachment-state updater match

Date: 2026-10-02

Game `func_150333A8` occupies the 38-word slot at
`0x150333A8..0x15033440`. Global mode `D_800C35EA == 1` returns zero without
changes. When byte `0xAD` on the second argument is nonzero, the callback
clears byte `0x11A` on its optional attached object at offset `0x31C` and
returns one. Otherwise it compares the reference float at offset `0x118`
against `D_80097B68`; exact equality or failure of the position-at-`0x18`
less-than-reference-plus-`300.0f` test writes `0xFF` to byte `3` of the first
argument, while the remaining case writes zero. These paths return zero.

The semantic body emits the complete 38-word length and 31 retail words
directly. Seven stale-checked words normalize one commutative floating-point
equality operand order and its closed equivalent branch-likely/store layout.
The guarded stores preserve the same three path results and do not modify any
relocation-bearing instruction.

The function-specific object disassembly matches all 38 retail words. The
shared patch-table rebuild, full link, and linked matcher also complete with
zero address drift. Game advances to `2,530 / 4,788 (52.84%)`, with 2,258
different C rows; overall byte-exact C progress is
`3,198 / 5,456 (58.61%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full stale-guard rebuild, full-link, and linked-word comparison evidence.

The next checkpoint completed 35-word `func_1503EEC0`; see
[Working Note 693](693-game-timer-expiry-callback-match-20261002.md). Resume the
ordinary small-Game queue with 36-word `func_150489B0`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
