# Game owner-list matching-node cleanup byte match

Date: 2026-09-30

`func_1514EDF0` occupies 32 words and 128 bytes at
`0x1514EDF0..0x1514EE70`. It walks the list rooted at owner offset `0x2F4`,
repeatedly asks `func_1514ED3C` for the next node whose object key matches the
first argument, preserves that node's successor, and removes the match through
`func_1514ED8C`. The loop continues until the search reports no further match,
so every matching node at or after the original list head is unlinked and
released.

Twenty-nine words emit directly from semantic C. IDO places the scalar result
pointer at `sp+0x38`, while retail uses the otherwise equivalent `sp+0x34`
slot. Three expected-word guards normalize only the initialization, address
materialization, and reload of that local pointer. The frame size, saved
registers, search/removal calls, 8-bit loop result, branch-likely backedge, and
all delay slots emit directly from the recovered source.

The matcher advances by exactly one row to `3,060 / 5,462 (56.02%)` overall
and `2,481 / 4,788 (51.82%)` in Game with no address drift. The linked
128-byte Game span has SHA-256
`318a5ff08113e9167dc286d85f9442ff04d79e5a5c4890cce2a5ebe9d43d6165`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
37-word Game `func_15158B3C`, the next ordinary matcher row.
