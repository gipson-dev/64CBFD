# Game output-default initializer match

Date: 2026-10-02

Game `func_151B498C` occupies 34 words at
`0x151B498C..0x151B4A14`. It receives an unused object pointer followed by
thirteen caller-owned output pointers. The recovered C writes packed values
`0x220005` and `0x40600` to the first two outputs, writes `0xFF` to the next
eight 32-bit outputs, clears the following 32-bit output, and writes byte
selectors `5` and `0x2B` to the final two outputs. It returns one to report
success.

The full signature is significant: the first unused pointer produces retail's
argument-home store, while the last two pointers preserve byte-width stores.
The assignment order reproduces retail's constant-load and stack-argument
schedule. The complete function emits directly from semantic C without
expected-word guards or a compiler-profile override and matches all 34 retail
words.

The full non-matching link and matcher complete with zero address drift. Game
advances to `2,525 / 4,788 (52.74%)`, with 2,263 different C rows; overall
byte-exact C progress is `3,193 / 5,456 (58.52%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 39-word `func_151CD224`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
