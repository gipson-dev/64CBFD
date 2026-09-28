# Game paired-record dispatch match - 2026-09-27

## Result

`func_151B3040` is byte-exact across all 28 words and 112 bytes at
`0x151B3040..0x151B30B0`. Fresh linked totals are 2,855 / 5,468 (52.21%)
overall and 2,283 / 4,790 (47.66%) in Game.

## Recovered behavior

The function dispatches the same type byte and object pointer through
`func_15169850` twice. The first call receives embedded fields at object
offsets `0x150` and `0x154`; the second receives the adjacent fields at
`0x164` and `0x168`.

The old body was a false zero-return placeholder. The recovered function is
`void`. Naming the first embedded-record address as a base preserves retail's
reuse of that value for the second pair, while making the incoming byte
argument volatile reproduces retail's stack spill and reload lifetime.

## Compiler boundary

The recovered C compiles to retail's complete instruction schedule directly,
including its 40-byte frame, first-call delay-slot object argument, retained
base stack slot, and second-call address derivation. No generated-slice guard
rows or relocation substitutions are needed.

The guard table remains at 1,483 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x1E04C0` and pristine retail span at
`conker.us.bin+0x1E04F0` compare equal for all 112 bytes. Both have SHA-256:

`06670f0bf180924a64312f13ccee3fc1eb5e2d3887c5bbe550a97d99609e7b87`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all unit tests, and the whitespace check
also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Classify 25-word
Game `func_151C9ED4`, the next unparked compact Game row in the fresh linked
queue with 24 real differences, before changing its implementation.
