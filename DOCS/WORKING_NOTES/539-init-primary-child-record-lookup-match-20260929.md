# Init primary/child record lookup byte match

Date: 2026-09-29

`func_1000B1FC` occupies 38 words and 152 bytes at
`0x1000B1FC..0x1000B294`. It first searches the three pointers in
`D_800417B0` for a primary record whose identifier at offset four matches the
argument. If no primary matches, it searches each non-null primary record's
optional child pointer at offset `0x60` and compares the child's identifier.
It returns the matching record or null.

The previous semantic C shared a pointer end local between both passes. IDO
hoisted the table addresses, added an entry precheck, and overflowed the retail
slot. Expressing each pass as the same `i < 3` indexed loop used by neighboring
`func_1000B1B0` recovers retail's strength-reduced pointer walks, independent
address setup, `a1` argument lifetime, and branch-likely loop backs. The full
routine emits directly from C without expected-word guards.

The production object, non-matching link, and fresh matcher succeed. The
matcher reports `3,043 / 5,463 (55.70%)` overall and
`398 / 493 (80.73%)` in Init with no address drift. Linked Init offset
`0xA1FC` and retail ROM offset `0xB1FC` share SHA-256
`354ea04ae4d20834968caad5738373e6337461f7cdd7fb391adcd4d0f78d8d48`.
The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Game `func_15106E78`, and Init
`func_1000FF90` parked at their documented ownership/compiler boundaries.
Resume with 33-word Game `func_1501D1D4`, the next ordinary matcher row.
