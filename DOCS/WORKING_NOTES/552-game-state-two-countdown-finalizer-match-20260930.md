# Game state-two countdown finalizer byte match

Date: 2026-09-30

`func_1510D720` occupies 35 words and 140 bytes at
`0x1510D720..0x1510D7AC`. It ignores inactive indices and zero countdowns.
For an active nonzero entry in `D_800D9F68`, it decrements the byte. When that
byte reaches zero, it expands the dirty index range in `D_800D9F58` and
`D_800D9F5C`, then calls `func_1510D608(arg0, 2)`.

The function is the retail structural twin of `func_1510D694`. Preserving its
independent `void` body reproduces the same unsigned-byte lifetime, ordinary
early branches, dirty-range updates, and shared epilogue. The only instruction
difference between the twins is the final state argument. All 35 words emit
directly from semantic C with no guarded retail words.

The matcher advances by exactly one row to `3,055 / 5,462 (55.93%)` overall
and `2,476 / 4,788 (51.71%)` in Game with no address drift. The linked
140-byte Game span has SHA-256
`291ebfdf97818a363db055caf102d3c63d6c9470df7db1bc76e7479705857527`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1511A410`, the next ordinary matcher row.
