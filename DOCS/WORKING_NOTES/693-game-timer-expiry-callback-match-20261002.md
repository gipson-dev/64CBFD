# Game timer-expiry callback match

Date: 2026-10-02

Game `func_1503EEC0` occupies the 35-word slot at
`0x1503EEC0..0x1503EF4C`. It first calls `func_1503ECA0(index)`, selects the
corresponding 16-byte entry in `D_800C6660`, and subtracts global tick count
`D_800BE9E4` from the signed halfword at offset `0x0C`. The truncated result is
stored back to that halfword. When the full 32-bit subtraction result is zero
or negative, the function calls `func_15060F28(&D_800CC2D0[index], 1)`.

Keeping the subtraction result as `s32` is significant: declaring it `s16`
introduced two sign-extension words and incorrectly based the expiry branch on
the truncated value. The recovered callback retains its original `s32`
signature because it participates in the callback table, although the retail
body does not establish a meaningful return value.

The semantic body emits the complete 35-word length and 16 retail words
directly. Nineteen stale-checked words normalize one closed compiler register
allocation and instruction-scheduling cycle. Four relocation-aware rows move
the `D_800BE9E4` and `D_800CC2D0` HI/LO pairs with their retail register
allocation; both calls and both branch-delay behaviors already emit directly
from C.

The function-specific object disassembly matches all 35 retail words. The
shared patch-table rebuild, full link, and linked matcher also complete with
zero address drift. Game advances to `2,531 / 4,788 (52.86%)`, with 2,257
different C rows; overall byte-exact C progress is
`3,199 / 5,456 (58.63%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full stale-guard rebuild, full-link, and linked-word comparison evidence.

The next checkpoint completed 36-word `func_150489B0`; see
[Working Note 694](694-game-trigonometric-lookup-match-20261002.md). Resume the
ordinary small-Game queue with 35-word `func_15074664`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
