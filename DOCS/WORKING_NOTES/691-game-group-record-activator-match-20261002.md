# Game group-record activator match

Date: 2026-10-02

Game `func_150227BC` occupies the 35-word slot at
`0x150227BC..0x15022848`. It selects one 30-byte row from `D_800C3550`, uses
the corresponding byte in `D_800C354A` as the active count, resolves each row
ID through `func_151149AC`, and sets byte `0x6E` on every returned record to
one. The loop deliberately reloads the count after every call.

The recovered semantic body exposes the count pointer, row offset, row cursor,
and index lifetime. Thirty-three words emit directly under the slice's
existing no-unroll compiler profile. IDO schedules the independent `i = 0`
before the opening count branch and leaves the final row-offset subtraction in
its delay slot; retail uses the opposite safe order. Two stale-checked rows
normalize only that exchange. No relocation-bearing instruction is modified.

The function-specific object disassembly matches all 35 retail words. The
shared patch-table rebuild, full link, and linked matcher also complete with
zero address drift. Game advances to `2,529 / 4,788 (52.82%)`, with 2,259
different C rows; overall byte-exact C progress is
`3,197 / 5,456 (58.60%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full stale-guard rebuild, full-link, and linked-word comparison evidence.

The next queued function, 38-word `func_150333A8`, is now complete; see
[Working Note 692](692-game-attachment-state-updater-match-20261002.md). Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
