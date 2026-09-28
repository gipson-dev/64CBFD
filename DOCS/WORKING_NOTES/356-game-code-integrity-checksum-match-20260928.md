# Game code-integrity checksum match - 2026-09-28

## Result

`func_151E7EF8` is byte-exact across all 26 words and 104 bytes at
`0x151E7EF8..0x151E7F60`. Fresh linked totals are 2,859 / 5,468 (52.29%)
overall and 2,287 / 4,790 (47.75%) in Game.

## Recovered behavior

The function first calls `func_151E7E9C`, the preceding three-way state
dispatcher. It then sums each signed 32-bit word from the start of
`func_151DDC20` up to, but not including, `func_151DE7D4`. If that checksum is
not `0xBFC924E3`, it clears the first instruction word of `osSpTaskLoad`.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its call-and-integrity-check behavior.

## Compiler boundary

Separating the checksum start and end into explicit pointer locals reproduces
retail's `a1` and `a2` address-base lifetimes. Initializing the accumulator
after the dispatcher call preserves the 24-byte frame and register-only loop.
IDO emits all 26 retail words directly, including the loop delay-slot sum and
the conditional `osSpTaskLoad` store. No guarded retail words or relocation
substitutions are needed.

The guard table remains at 1,487 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215378` and pristine retail span at
`conker.us.bin+0x2153A8` compare equal for all 104 bytes. Both have SHA-256:

`e921d7cef916745ba7736417867809da191c952fad73becbf514d6f5f81be152`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all unit tests, and the whitespace check
also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
163-word Game `func_151E7F60`, currently measured at 162 real differences in
the fresh linked queue, before changing its implementation.
