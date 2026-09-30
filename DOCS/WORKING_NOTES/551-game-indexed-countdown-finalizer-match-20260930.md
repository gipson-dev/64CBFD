# Game indexed countdown finalizer byte match

Date: 2026-09-30

`func_1510D694` occupies 35 words and 140 bytes at
`0x1510D694..0x1510D720`. It ignores inactive indices and zero countdowns.
For an active nonzero entry in `D_800D9F68`, it decrements the byte. When that
byte reaches zero, it expands the dirty index range in `D_800D9F58` and
`D_800D9F5C`, then calls `func_1510D608(arg0, 3)`.

The recovered `void` signature permits retail's `v0` pointer lifetime. An
unsigned-byte temporary followed by a post-store zero check emits retail's
`addiu` and `andi` normalization, ordinary early branches, and exact shared
epilogue. All 35 words emit directly from semantic C with no guarded retail
words.

The matcher advances by exactly one row to `3,054 / 5,462 (55.91%)` overall
and `2,475 / 4,788 (51.69%)` in Game with no address drift. The linked
140-byte Game span has SHA-256
`14b2c699b48bf4376cc3f16817191178ab21579419ba72f7755cf4ee0895d309`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_1510D720`, the next ordinary matcher row.
