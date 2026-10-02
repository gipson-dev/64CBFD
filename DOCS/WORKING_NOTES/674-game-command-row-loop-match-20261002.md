# Game command-row loop match

Date: 2026-10-02

`func_150413FC` occupies 33 words and 132 bytes at
`0x150413FC..0x15041480`. Its former C placeholder returned zero and omitted
the complete command-processing loop.

The recovered routine walks a zero-terminated stream of command bytes. For
each entry it translates the command through `func_15041480`, passes that
value and the current eight-byte row to `func_15041508`, retains the returned
state, advances both streams, and repeats until the command terminator.

IDO emits the complete 33-word extent with the retail frame, saved-register
lifetimes, two calls, loop updates, and epilogue. Nine stale-checked expected
words normalize only the independent prologue schedule. They do not replace
loop semantics, calls, relocations, or control flow.

The full linked matcher reports zero address drift and advances Game to
`2,504 / 4,788 (52.30%)`, with 2,284 different C rows. Overall byte-exact C
progress is `3,172 / 5,456 (58.14%)`. Init remains `487 / 487 (100.00%)` and
Debugger remains `181 / 181 (100.00%)`.

The next two recoveries are recorded in
[Working Note 675](675-game-condition-state-flag-match-20261002.md) and
[Working Note 676](676-game-owner-event-callback-match-20261002.md). Resume
the ordinary small-Game queue with 34-word `func_1510E7A4`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
