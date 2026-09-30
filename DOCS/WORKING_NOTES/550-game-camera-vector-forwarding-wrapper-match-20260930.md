# Game camera-vector forwarding wrapper byte match

Date: 2026-09-30

`func_1510B32C` occupies 33 words and 132 bytes at
`0x1510B32C..0x1510B3B0`. It calls `func_1510B128` with the incoming slot and
three float words plus a zero fifth argument. It then indexes the 12-byte
records at `D_800D9AC0`, stores the incoming components in `{arg3, arg1,
arg2}` order, and sets update flag `D_800D9AF0` to one.

The neighboring `func_1510B128` remains an old-style non-matching placeholder.
Passing raw float words preserves the direct `jal` without C's default
float-to-double promotions. One inserted `mtc1` and seven stale-checked word
guards restore retail's floating fifth-argument store and `f6`/`f8`/`f10`
post-call lifetime. The remaining 25 words emit directly from semantic C.

The matcher advances by exactly one row to `3,053 / 5,462 (55.90%)` overall
and `2,474 / 4,788 (51.67%)` in Game with no address drift. Linked Game offset
`0x10B32C` has SHA-256
`1d1156abe599b3f2474a382805b158a19073bd10f6a273c4e72de1927b0bc317`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_1510D694`, the next ordinary matcher row.
