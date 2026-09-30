# Game object-position forwarding adapter byte match

Date: 2026-09-30

`func_1509F77C` occupies 33 words and 132 bytes at
`0x1509F77C..0x1509F800`. It resolves the object identified by `arg1`, reads
the three position floats at offsets `0x14`, `0x18`, and `0x1C`, truncates
them to signed integers, and calls `func_1000F91C` with the caller's identifier,
signed field, trailing values, fixed `0x7FFF`, and two zero parameters.

Writing the three coordinate conversions as explicit local temporaries
recovers retail's 48-byte frame, incoming argument spills, grouped float
loads, conversion-register lifetimes, ten-argument stack layout, call delay
slot, and epilogue. All 33 words emit directly from C with no guarded rows.

The matcher advances by exactly one row to `3,049 / 5,463 (55.81%)` overall
and `2,470 / 4,789 (51.58%)` in Game with no address drift. Linked Game offset
`0x9F77C` has SHA-256
`7f7016927ccef67069847fbfce123b4a612f7c2c321e445b26dc058627757d9b`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
32-word Game `func_150AD9A0`, the next ordinary matcher row.
