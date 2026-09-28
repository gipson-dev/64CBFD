# Game actor-position query match - 2026-09-28

## Result

`func_150E36BC` is byte-exact across its complete 31-word, 124-byte retail
span at `0x150E36BC..0x150E3738`.

The fresh linked matcher reports 2,877 / 5,466 (52.63%) exact C functions
overall and 2,303 / 4,790 (48.08%) in Game, with one address-drift blocker and
2,588 genuinely different C rows overall.

## Recovery

The function accepts a one-based actor slot followed by three output pointers.
It decrements the slot, requires the resulting index to be in `[0, 7]`, and
reads the actor pointer from `D_800D99D0`. A valid actor must be non-null and
have type byte `0x27`. Its floating-point coordinates at offsets `0x10`,
`0x14`, and `0x18` are then truncated to signed integers and written to the
three outputs.

A small local actor view captures only the type and coordinate fields needed
by this query. IDO naturally emits retail's range checks, pointer-table lookup,
null and type checks, three `trunc.w.s` conversions, `mfc1` pipeline, and output
stores from direct semantic C. No expected-word guards or compiler-profile
override are used.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x1236BC` and the
pristine retail span at `conker/conker.us.bin` offset `0x110B6C` compare equal
across all 124 bytes. Both have SHA-256:

`2fc9f7a7d84f34d87b35d75ec2dcc7e22bc8f446a100113dc7519f2540ffe8d6`

## Validation

The focused object build, linked matcher, replacement build, outer ROM build,
project tool checks, all nine focused Python tests, direct byte comparison,
and whitespace validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_150F9720`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
