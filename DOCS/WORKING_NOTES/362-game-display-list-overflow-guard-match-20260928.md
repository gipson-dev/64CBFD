# Game display-list overflow guard match - 2026-09-28

## Result

`func_151E8620` is byte-exact across all 49 words and 196 bytes at
`0x151E8620..0x151E86E4`. Fresh linked totals are 2,865 / 5,468 (52.40%)
overall and 2,293 / 4,790 (47.87%) in Game.

## Recovered behavior

The function selects the callback for the current `D_800E0B94` mode from
`D_8008FFC0`, preserves the original incoming `Gfx *`, and sets the active
display-list marker `D_8003C8E0` to `0x09000000`. A nonnull callback transforms
the display-list pointer and causes the mode to be reloaded.

When the resulting mode is nonzero, the function clears `D_80090058` and
`D_800E0C78`. It then clears the active marker and subtracts the current
display-list-buffer base from the result as `Gfx *` values, naturally
reproducing retail's byte subtraction followed by division by eight. If that
command count exceeds `D_800BEBA4`, the original pointer is returned;
otherwise the transformed pointer is returned.

## Compiler boundary

The recovered C reproduces the full control flow, exact 49-word extent,
32-byte frame, original-pointer stack spill, mode-dependent stores, explicit
zero/one overflow materialization, and display-list pointer arithmetic.

Fourteen relocation-aware guard rows normalize only IDO's independent choices
for callback and original-pointer register lifetimes, the active-marker
temporary, and three post-callback reload/move words. They preserve every
branch target, call, delay slot, arithmetic operation, memory access, and
relocation. No frame guard is needed.

The guard table has 1,528 rows with zero duplicate
`(filename, function, offset)` keys. Exactly 14 rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215AA0` and pristine retail span at
`conker.us.bin+0x215AD0` compare equal for all 196 bytes. Both have SHA-256:

`d830d34cd5e00f4d8d151f71bdd967086b13b71bfa9af6d7ac67f5ab76d41572`

The focused/exhaustive guarded rebuild, fresh linked matcher, replacement and
outer builds, direct span comparison, guard-table integrity audit, project
tool checks, unit tests, and whitespace check pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
175-word Game `func_151E86E4`, currently measured at 165 real differences in
the fresh linked queue, before changing its implementation.
