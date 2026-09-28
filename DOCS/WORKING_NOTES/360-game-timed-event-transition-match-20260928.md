# Game timed event transition match - 2026-09-28

## Result

`func_151E83E8` is byte-exact across all 50 words and 200 bytes at
`0x151E83E8..0x151E84B0`. Fresh linked totals are 2,863 / 5,468 (52.36%)
overall and 2,291 / 4,790 (47.83%) in Game.

## Recovered behavior

When `D_800E0A80` is zero, the function changes it to `-1` and calls
`func_1501D348(0x1D, 6, 0, 0, 0)`. It then calls `func_151E530C` and clears
`D_800E0A90` whenever `func_1517EFDC` returns false.

Once the signed timer reaches `0x65`, the function calls `func_151E5034`,
clears `D_8008FDA4`, selects mode `1`, resets the timer, clears `D_800D2E40`,
and dispatches `func_1501C730(6, 0x21, 0, 0, 1)`.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its state-update behavior.

## Compiler boundary

The direct nested-condition C reproduces retail's 32-byte frame, cursor test,
five-argument registration call, shared update and predicate calls, signed
timer threshold, byte/global stores, five-argument transition dispatch, and
branch-likely epilogue. IDO emits all 50 retail words directly. No guarded
retail words or relocation substitutions are needed.

The guard table remains at 1,512 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215868` and pristine retail span at
`conker.us.bin+0x215898` compare equal for all 200 bytes. Both have SHA-256:

`c9c159a99c0ca96242f08a223857956bcfa2753dbe34a25d1a0887d5dba4e964`

The focused object build, relink, fresh linked matcher, direct span comparison,
guard-table integrity audit, replacement and outer-ROM builds, project-tool
checks, all unit tests, and whitespace check pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
92-word Game `func_151E84B0`, currently measured at 84 real differences in the
fresh linked queue, before changing its implementation.
