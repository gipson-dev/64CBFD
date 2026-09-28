# Game timed mode transition match - 2026-09-28

## Result

`func_151E8214` is byte-exact across all 41 words and 164 bytes at
`0x151E8214..0x151E82B8`. Fresh linked totals are 2,861 / 5,468 (52.32%)
overall and 2,289 / 4,790 (47.79%) in Game.

## Recovered behavior

Mode `8` returns immediately. In every other mode, the function calls
`func_1517EFDC` and clears `D_800E0A90` while that predicate is false. Once the
signed transition timer reaches `0xA1`, it clears `D_8008FDCC`, selects mode
`8`, sets both input-state bytes to one, clears `D_8008FDA4`, writes `-2` to
`D_800E0A80`, resets the timer, and raises `D_800D2E43`.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its state-update behavior.

## Compiler boundary

The direct nested-condition C reproduces retail's 24-byte frame, branch-likely
early exit, call and timer-reset path, shared `D_800E0A90` address lifetime,
signed threshold check, constant registers, exact-width stores, and epilogue.
IDO emits all 41 retail words directly. No guarded retail words or relocation
substitutions are needed.

The guard table remains at 1,511 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215694` and pristine retail span at
`conker.us.bin+0x2156C4` compare equal for all 164 bytes. Both have SHA-256:

`19b672f8cd503cffe4161a9ce5fab0e0b80c4f7177123ac0e88fa72b12ae2051`

The focused object build, relink, fresh linked matcher, direct span comparison,
guard-table integrity audit, replacement and outer-ROM builds, project-tool
checks, all unit tests, and whitespace check pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
76-word Game `func_151E82B8`, currently measured at 74 real differences in the
fresh linked queue, before changing its implementation.
