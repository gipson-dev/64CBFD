# Game owned-state teardown match - 2026-09-27

## Result

`func_151D13E0` is byte-exact across all 26 words and 104 bytes at
`0x151D13E0..0x151D1448`. Fresh linked totals are 2,857 / 5,468 (52.25%)
overall and 2,285 / 4,790 (47.70%) in Game.

## Recovered behavior

The function checks the object pointer stored at owner offset `0x30`. If it is
non-null, the function follows that object's offset-`0x98` link, clears object
byte `0x30`, clears flag `0x2`, sets flags `0x8` and `0x1` through distinct
read-modify-write operations, and writes `0x28` to halfword `0x1C`. It then
clears the first word of the linked record and nulls the owner slot.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its wrapper and teardown-only behavior.

## Compiler boundary

Expressing each object-field access through the owner slot preserves retail's
repeated `lw` instructions and alias boundary. IDO then emits the complete
26-word leaf routine directly, including the null branch, early constant load,
three independent flag updates, final stores, and return schedule. No guarded
retail words or relocation substitutions are needed.

The guard table remains at 1,487 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x1FE860` and pristine retail span at
`conker.us.bin+0x1FE890` compare equal for all 104 bytes. Both have SHA-256:

`0244d7b415296c133f4e777a20a9f3de1c752d82b13a12814a4e4a39beff5bec`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all unit tests, and the whitespace check
also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Classify 25-word
Game `func_151E4E00`, the next unparked compact Game row in the fresh linked
queue with 24 real differences, before changing its implementation.
