# Game four-resource teardown byte match

Date: 2026-09-29

`func_1519F400` occupies 35 words and 140 bytes at
`0x1519F400..0x1519F48C`. It examines four resource pointers at owner offset
`0x58`. Resources zero and two are released through `func_1519F48C`; resources
one and three each pass through `func_151A0928` and then `func_1516972C`.

A pointer-array view preserves retail's use of `a0` for each conditional call
and emits all 35 words directly from C with no expected-word guards. The full
non-matching link succeeds. The matcher reports `3,039 / 5,463 (55.63%)`
overall and `2,461 / 4,789 (51.39%)` in Game with no drift. Linked Game offset
`0x19F400` and retail ROM offset `0x1CC8B0` share SHA-256
`42485dfa9f8061de584a11197449d96173d89c7f9fd07617b80c36e3d2e45650`.
`make tools-check` and all 10 tool unit tests pass.

Resume with Game `func_151AFC08`, the next ordinary 32-word matcher row. Keep
the four documented special-case rows parked.
