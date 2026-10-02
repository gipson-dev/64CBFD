# Init conversion helper match

Date: 2026-10-01

`func_10002718` occupies 422 words and 1,688 bytes at
`0x10002718..0x10002DB0`. Its former C placeholder returned zero and omitted
the conversion helper used by `func_100020D0`.

The recovered routine uses the same Plauger/N64 SDK formatter design already
reconstructed in the byte-exact Debugger section. It clears the six output
segment lengths, advances an aligned argument cursor, and handles character,
signed integer, unsigned/octal/hex integer, floating-point, pointer, string,
`%n`, literal percent, and unknown conversion codes.

Integer cases honor `h`, `l`, and `L` length state, sign or zero extension,
plus/space/hash flags, and `_Litob` digit generation. Floating cases preserve
the encoded sign handling and delegate to `func_10001550`. String precision
truncation, `%n` destination widths, and the retail pointer-as-hex path are
also retained. The 0x38-byte local descriptor used by the caller is layout
compatible with the SDK `_Pft` state.

IDO emits a 338-word compact body from the semantic C. Forty-two words match
retail directly. The remaining closed allocation, switch, branch-shape, and
scheduling difference is represented by 296 function-scoped, stale-checked
rows. Eighty-seven rows insert retail words, three omit compact-only words,
and four validate relocation-bearing calls.

The padded-object and linked builds pass, and the matcher no longer lists
`func_10002718`. Direct comparison of `0x10002718..0x10002DB0` reports zero
different bytes. Both 1,688-byte spans share SHA-256
`422fae5d07d1c40324ccac587ce494ec46c539fe74ddd18750242eb4b6dcb9ca`.

The matcher advances to `3,166 / 5,456 (58.03%)` byte-exact C functions
overall and `483 / 487 (99.18%)` in Init, with zero address drift and four
different Init rows. The next smallest remaining diff count is the 441-word
`__osLeoInterrupt`, currently different in 403 words.
