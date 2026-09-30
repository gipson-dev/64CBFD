# Game owner-event dispatcher match

Date: 2026-09-30

`func_150F15F8` occupies 35 words and 140 bytes at
`0x150F15F8..0x150F1684`. For event `0x43`, it compares the incoming owner's
word and identity byte against the object record at offset `0x28`; either
match destroys the object through `func_1516972C`. Other event codes forward
the owner record, code, object fields at `0x28/0x2C`, and object pointer to
`func_15149514`.

Declaring the event byte and incoming owner pointer volatile recovers retail's
incoming argument homes and deliberate repeated loads. Explicit word-owner
and byte-owner identities reproduce the complete branch/call schedule.
Twenty-six words emit directly from semantic C. Nine stale-checked guards
normalize only the closed register-allocation cycle across those identities;
instruction positions, branches, arguments, and both call relocations match.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`3680ee0fd4268a962063b7b48e7d229d1e99000861d24f013ef5f200a18c18e1`.
The matcher advances to `3,078 / 5,461 (56.36%)` overall and
`2,499 / 4,788 (52.19%)` in Game, with zero address drift.

Resume with 34-word Game `func_150F2518`, the next ordinary matcher row.
