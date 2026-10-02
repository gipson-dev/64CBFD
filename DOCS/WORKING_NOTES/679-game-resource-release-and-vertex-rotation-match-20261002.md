# Game resource release and vertex rotation match

Date: 2026-10-02

`func_151325C8` occupies 33 words at `0x151325C8..0x1513264C`. Its former
zero-return placeholder omitted an object resource-release pass. The recovered
body scans entries beginning at object offset `0x154` through the inclusive
global limit `D_80082FA0`, calls `func_100043B4(entry, 4)` for each nonzero
entry, and then applies the same release to the trailing slot at offset
`0x164`. The integer storage declaration follows the established sibling
layout in `func_1513C92C` and preserves retail's register allocation and
branch-delay moves. All 33 words emit directly from semantic C.

`func_151436B4` occupies 34 words at `0x151436B4..0x1514373C`. Its existing
rotation math was semantically correct, but the inline fourth `sinf` let IDO
store the first output before making the call and expanded the compact body
beyond the retail slot. Naming the fourth trigonometric result makes all four
calls occur before the vertex arithmetic and stores, reproducing retail's
frame, call order, floating-point schedule, and epilogue across all 34 words.

Neither function needs expected-word guards or a compiler-profile override.
The full linked matcher reports zero address drift and advances Game to
`2,514 / 4,788 (52.51%)`, with 2,274 different C rows. Overall byte-exact C
progress is `3,182 / 5,456 (58.32%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

Resume the ordinary small-Game queue with 33-word `func_1514795C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.

Superseded resume: [Working Note 680](680-game-resource-release-family-and-height-predicate-match-20261002.md)
completed `func_1514795C` and continued through the related release family and
height predicate.
