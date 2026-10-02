# Game render-parameter wrapper family match

Date: 2026-10-02

`func_1510E7A4`, `func_1510E82C`, and `func_1510E8BC` occupy 34, 36, and 37
words at `0x1510E7A4..0x1510E82C`, `0x1510E82C..0x1510E8BC`, and
`0x1510E8BC..0x1510E950`. Their former zero-return placeholders omitted three
closely related argument adapters around `func_1510E950`.

The recovered signatures preserve the first two coordinate-like values as raw
32-bit words, which keeps them in `$a2` and `$a3` instead of floating-point
argument registers. The wrappers insert a zero third argument, shift the
remaining mixed integer and floating-point parameters, and supply the final
three parameters in distinct ways. `func_1510E7A4` forwards caller-provided
bounds and appends zero. `func_1510E82C` supplies the retail `-10000.0f` and
`20000.0f` bounds and appends zero. `func_1510E8BC` supplies its corresponding
bound symbols and forwards the caller's final mode word.

IDO emits each complete retail slot directly from semantic C, including the
0x48-byte frame, raw argument spills, mixed `lw`/`lhu`/`lwc1` loads, outgoing
stack stores, call relocation and delay slot, and epilogue. No expected-word
guards, inserted or omitted instructions, or compiler-profile override is
required.

The full linked matcher reports zero address drift and advances Game to
`2,509 / 4,788 (52.40%)`, with 2,279 different C rows. Overall byte-exact C
progress is `3,177 / 5,456 (58.23%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

The next motion-update recovery is recorded in
[Working Note 678](678-game-angular-motion-update-family-match-20261002.md).
Resume the ordinary small-Game queue with 33-word `func_151325C8`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
