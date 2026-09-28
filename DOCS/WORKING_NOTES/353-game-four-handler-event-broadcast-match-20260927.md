# Game four-handler event broadcast match - 2026-09-27

## Result

`func_151C9ED4` is byte-exact across all 25 words and 100 bytes at
`0x151C9ED4..0x151C9F38`. Fresh linked totals are 2,856 / 5,468 (52.23%)
overall and 2,284 / 4,790 (47.68%) in Game.

## Recovered behavior

The function stores its incoming pointer in a one-word stack record and sends
that record to `func_15160274`, `func_1515572C`, `func_151A561C`, and
`func_151494E0`, each with event code `0x21`. After all four handlers return,
it clears global byte `D_8008CD00`.

The old body was a false zero-return placeholder. The recovered function is
`void`; expressing the stack-record address as a word-sized call argument
retains it in `s0` across all four calls and reproduces retail's call order,
delay slots, and final global store.

## Compiler boundary

IDO reserves a 48-byte frame for the recovered scalar/address pair, while
retail uses a 40-byte frame with the record at stack offset `0x24`. Four
function-scoped guard rows normalize only the frame allocation, record address,
record store, and frame restoration words. All other instructions and every
relocation are emitted directly from C.

The guard table now contains 1,487 rows with zero duplicate
`(filename, function, offset)` keys. Exactly four rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x1F7354` and pristine retail span at
`conker.us.bin+0x1F7384` compare equal for all 100 bytes. Both have SHA-256:

`0a54d1e0755c866e9e47eb8ad4f5481f02d22e423d506a4c40fcb667e2473918`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all unit tests, and the whitespace check
also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Classify 26-word
Game `func_151D13E0`, the next unparked compact Game row in the fresh linked
queue with 24 real differences, before changing its implementation.
