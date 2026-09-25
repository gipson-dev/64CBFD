# Game motion-scale register match - 2026-09-25

## Result

`func_1505841C` is byte-exact across its complete 117-word linked extent
`0x1505841C..0x150585F0`. The fresh C-only matcher reports
`2551 / 5490 (46.47%)` overall and `1983 / 4801 (41.30%)` game. One init
function remains blocked by address drift; 2,938 total and 2,818 game C
functions still differ.

## Mismatch and resolution

The maintained C body already matched 112 of 117 words. Three differences
were the floating-point registers used for the scaled denominator, quotient,
and following global-offset addition. Two more were the register selected for
the `D_800419A0` HI16/LO16 load pair near the function tail.

Combining the quotient and addition into one source expression changed the
constant's FP register and cascaded through later code. Splitting the
denominator update, division, and sum into three assignments moved the
long-lived result from `f0` to `f2` and produced a larger cascade. Both source
experiments were reverted.

Five expected-word-guarded normalizations preserve the original readable C
body while selecting retail's `f0`/`f16` quotient chain and `t9` global-load
register. The `R_MIPS_HI16:D_800419A0` and
`R_MIPS_LO16:D_800419A0` relocations remain attached to their normalized
instructions.

## Verification

The current checkout passed:

```sh
make build/src/game_83300.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
490 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 468-byte linked and retail spans produced SHA-256
`bedd9ce23e7064232569e930772e0a4a1c0f2a9adb4590814918804e8cc5c0ee`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO register-allocation normalization does not
transfer to host source. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is eight-word `func_150F02A0` with five real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following game row is 12-word `func_151B2FA0`,
also with five real differences.
