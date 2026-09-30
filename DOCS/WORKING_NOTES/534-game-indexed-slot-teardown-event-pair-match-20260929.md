# Game indexed slot teardown event pair byte match

Date: 2026-09-29

`func_15172CA8` occupies 32 words and 128 bytes at
`0x15172CA8..0x15172D28`. If signed slot state `D_800DD2B0[index]` is already
`-1`, it returns without work. Otherwise it marks the slot inactive and calls
`func_1517EE40` twice: first with `(0, 0, 0, 0, 1, index)`, then with
`(0, 0, 0, 0x32, 0, index)`.

The recovered indexed byte accesses and direct six-argument calls emit all 32
retail words from C with no expected-word guards. The full non-matching link
succeeds. The matcher reports `3,038 / 5,463 (55.61%)` overall and
`2,460 / 4,789 (51.37%)` in Game with no drift. Linked Game offset `0x172CA8`
and retail ROM offset `0x1A0158` share SHA-256
`85845ebeab1c34c3ccaac89e2f3f6c17cdcc73f798354419eabaa2a1de864a90`.
`make tools-check` and all 10 tool unit tests pass.

Resume with Game `func_1519F400`, the next ordinary matcher row. Keep the four
documented special-case rows parked.
