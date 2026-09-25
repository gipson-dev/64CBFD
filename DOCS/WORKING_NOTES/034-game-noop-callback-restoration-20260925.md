# Game no-op callback restoration - 2026-09-25

## Result

`func_1515FB70` is restored to its original nine-word assembly extent
`0x1515FB70..0x1515FB94`. The fresh C-only matcher reports
`2550 / 5490 (46.45%)` overall and `1982 / 4801 (41.28%)` game. One init
function remains blocked by address drift; 2,939 total and 2,819 game C
functions still differ. The raw-assembly inventory is now 548 total and 517
game functions.

## Classification evidence

The maintained C body modeled two nested conditions with an empty inner body.
IDO removed the conditional `arg1+0x1C` load and negative-value branch,
leaving six compiled words followed by padding. Four of retail's nine words
therefore differed.

An explicit early-return form compiled identically. A `register volatile`
local retained the load but introduced an eight-byte stack frame. Modeling an
integer return retained the branch but loaded into `v1`, added `move v0,v1`,
and produced ten words. Adding `register` did not change that allocation.
These experiments were reverted.

Retail loads the conditional value directly into return register `v0`, tests
it, and reaches the common return without defining a result on every path.
That undefined-return/no-op callback shape cannot be represented faithfully by
the maintained C without either losing instructions or inventing behavior.
The exact assembly extent is therefore retained as the honest source boundary.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_18A8F0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The function is no longer part of the C-matcher denominator. An independent
comparison of the complete 36-byte linked and retail spans produced SHA-256
`02df2d2216918188d8a3fc4af4bd4a1f7249eee66589525958b38236bd4990ad`
for both. The guarded patch table remains at 485 rows because this restoration
does not require word patches.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. Assembly ownership in the decomp does not require a
host-source transplant. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is 117-word `func_1505841C` with five real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following game row is eight-word `func_150F02A0`,
also with five real differences.
