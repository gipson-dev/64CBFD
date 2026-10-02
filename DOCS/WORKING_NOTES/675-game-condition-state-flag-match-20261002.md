# Game condition state-flag match

Date: 2026-10-02

`func_150F9A20` occupies a 36-word, 144-byte retail slot at
`0x150F9A20..0x150F9AB0`. Its former C placeholder returned zero and omitted
the complete condition-driven state update.

The recovered routine queries `func_1509BE40(1, 0x4025, 6, 0x2000)`. A true
result enables state flag `0x80`, clears flag `0x08`, and writes `85.0f` to
field `0x190`. A false result clears `0x80`, enables `0x08`, and zeros that
field.

IDO emits the retail frame, branch-likely path, repeated flag stores, floating
constants, epilogue, and complete padded slot directly from semantic C. No
expected-word guards, insertions, omissions, relocation normalization, or
object-profile override is required.

The linked matcher advances Game to `2,505 / 4,788 (52.32%)`, with 2,283
different C rows. Overall byte-exact C progress is
`3,173 / 5,456 (58.16%)` at this checkpoint.

The following owner-event callback recovery is recorded in
[Working Note 676](676-game-owner-event-callback-match-20261002.md).
