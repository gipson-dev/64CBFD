# Game line-projection match - 2026-09-27

## Result

`func_1514563C` is byte-exact across all 65 words and 260 bytes at
`0x1514563C..0x15145740`. Fresh linked totals are 2,854 / 5,468 (52.19%)
overall and 2,282 / 4,790 (47.64%) in Game.

## Recovered behavior

The function projects `arg2` onto the directed line beginning at `arg0` with
direction `arg1`. It rejects a zero-length direction, computes the projection
amount from two dot products, optionally returns that amount through `arg4`,
and writes `arg0 + amount * arg1` through `arg3`. A null amount pointer uses a
stack-local fallback.

The existing behavior was correct. Expressing the six commutative dot-product
multiplications in retail operand order removes six mismatches directly from
C while retaining the compiler's stable control-flow and FP schedule.

## Compiler boundary

Eighteen function-scoped guard rows retain retail's independent IDO choices:
nine words select its 32-byte leaf frame and stack offsets, while nine words
select operand order and temporary FP registers for the three output
components. None changes a branch target, relocation, or recovered behavior.

The guard table now contains 1,483 rows with zero duplicate
`(filename, function, offset)` keys. Exactly 18 rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x172ABC` and pristine retail span at
`conker.us.bin+0x172AEC` compare equal for all 260 bytes. Both have SHA-256:

`19c6f8f57853c7b7d404c4ba8fe718d0c7cad42955a1b1ec2ea13d27680c730f`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all nine unit tests, and the whitespace
check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler cases parked. Classify 28-word Game
`func_151B3040`, the next unparked compact Game row in the fresh linked queue
with 24 real differences, before changing its implementation.
