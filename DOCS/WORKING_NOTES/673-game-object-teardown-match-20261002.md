# Game object teardown match

Date: 2026-10-02

`func_15106E78` occupies 32 words and 128 bytes at
`0x15106E78..0x15106EF8`. Its former C placeholder returned zero and omitted
the complete object teardown sequence.

The recovered routine indexes `D_80088C18` with the object's type byte at
offset `0x5C` and invokes the optional destructor callback. It then releases
the optional child objects at offsets `0x6C` and `0x70` through
`func_1516972C`, before passing the embedded record at offset `0x74` to
`func_151D5E30`.

IDO emits all 32 retail words directly from the semantic C body. No expected
word guards, insertions, omissions, object-profile override, or relocation
normalization is required. The adjacent `func_15106EF8` and `func_15106F24`
wrappers now use the recovered pointer argument type and remain byte-exact.

The linked matcher reports zero address drift and advances Game to
`2,503 / 4,788 (52.28%)`, with 2,285 different C rows. Overall byte-exact C
progress is `3,171 / 5,456 (58.12%)`. Init remains `487 / 487 (100.00%)` and
Debugger remains `181 / 181 (100.00%)`.

The next recovery, 33-word `func_150413FC`, is recorded in
[Working Note 674](674-game-command-row-loop-match-20261002.md). Resume the
ordinary small-Game queue with 36-word `func_150F9A20`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
