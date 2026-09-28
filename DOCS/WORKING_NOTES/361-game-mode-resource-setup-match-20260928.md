# Game mode-resource setup match - 2026-09-28

## Result

`func_151E84B0` is byte-exact across all 92 words and 368 bytes at
`0x151E84B0..0x151E8620`. Fresh linked totals are 2,864 / 5,468 (52.38%)
overall and 2,292 / 4,790 (47.85%) in Game.

## Recovered behavior

The function marks `D_8003C8E0` with `0x09000001`, obtains a result from
`func_151ED1E0`, and passes that result through the callback selected by
`D_800E0B94` from `D_8008FFF4` when the callback is nonnull.

When `D_80000300` is nonzero, the state flags select an optional resource
index. With `D_800BE616` set and `D_8008FD90` at least two, a clear low nibble
of `D_800BE740` maps state one or two to index `0x33` or `0x16`. Otherwise, a
clear low bit maps those states to `0x32` or `0x15`.

A selected index first calls `func_1504332C(0xFF, 0xFF, 0xFF, 0xFF)`, then
calls `func_15042D94(0x94, 0xC8, 0x81, D_800E0BD8[index])`. The function
finally clears `D_8003C8E0` and returns the possibly transformed result.

## Compiler boundary

The recovered C reproduces all substantive instructions, branches, callback
and direct calls, registers, stack slots, global accesses, delay slots, and
return-value handling. A declaration-only local preserves retail's gap before
the index and result slots under IDO's debug layout. IDO then rounds the frame
to 40 bytes while retail uses 32 bytes; two guarded words restore only the
matching prologue and epilogue frame adjustments.

The guard table has 1,514 rows with zero duplicate
`(filename, function, offset)` keys. Exactly two rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215930` and pristine retail span at
`conker.us.bin+0x215960` compare equal for all 368 bytes. Both have SHA-256:

`dcce149dab839960d8e6ba7fec108cac61da0328fbf0f2d218fb53fbe974a341`

The focused object build, exhaustive guarded-object rebuild, relink, fresh
linked matcher, direct span comparison, guard-table integrity audit,
replacement and outer-ROM builds, project-tool checks, all unit tests, and
whitespace check pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
49-word Game `func_151E8620`, currently measured at 49 real differences in the
fresh linked queue, before changing its implementation.
