# Game marker-table cursor match - 2026-09-28

## Result

`func_151E82B8` is byte-exact across all 76 words and 304 bytes at
`0x151E82B8..0x151E83E8`. Fresh linked totals are 2,862 / 5,468 (52.34%)
overall and 2,290 / 4,790 (47.81%) in Game.

## Recovered behavior

The function first calls `func_151E530C`. Cursor state `-1` waits for timer
`0x79`; once reached, it selects mode `9`, resets the timer, writes `0xFF` to
`D_8008FDCC`, resets the cursor, and dispatches event `0x1D` through
`func_1501C730(6, 0x1D, 0, 0, 1)` before returning. Cursor state `-2` is
normalized to zero.

Once the timer reaches `0x1BE`, a nonnegative cursor scans the pointer table
at `D_800E0BD8` until its current record begins with marker byte `0x2A`. The
cursor advances past that marker; a following `0x3D` marker changes the cursor
to `-1`. The function then resets the timer.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its state-update behavior.

## Compiler boundary

The scalar cursor lifetime, deliberate global reloads, and direct final table
index reproduce retail's frame, calls, branches, table scan, global stores,
and epilogue. IDO emits every substantive instruction directly. At offset
`0x024`, IDO canonicalizes the equality branch as `bne v0,a1` while retail
uses the equivalent `bne a1,v0`; one guarded word preserves only that operand
order. It changes neither the comparison nor its target.

The guard table has 1,512 rows with zero duplicate
`(filename, function, offset)` keys. Exactly one row belongs to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215738` and pristine retail span at
`conker.us.bin+0x215768` compare equal for all 304 bytes. Both have SHA-256:

`4abd7ddbc182747cbd0d4604e7b7f6050d6e5c094ee70e2d4f30ee7f5cfeb0a7`

The exhaustive guarded-object rebuild, fresh linked matcher, direct span
comparison, guard-table integrity audit, replacement and outer-ROM builds,
project-tool checks, all unit tests, and whitespace check pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
50-word Game `func_151E83E8`, currently measured at 44 real differences in the
fresh linked queue, before changing its implementation.
