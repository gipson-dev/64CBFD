# Game optional-pointer call match - 2026-09-25

## Result

`func_1509D054` is byte-exact across its complete 14-word linked extent
`0x1509D054..0x1509D08C`. The fresh C-only matcher reports
`2547 / 5493 (46.37%)` overall and `1979 / 4804 (41.19%)` game. One init
function remains blocked by address drift; 2,945 total and 2,825 game C
functions still differ.

## Mismatch and resolution

The function already matched 10 of 14 words. Retail loads `D_800D2FB0` into
`v0`, tests it there, and copies the pointer into `a0` in the call delay slot.
Current IDO coalesces the pointer directly into `a0` and leaves the delay slot
empty. Earlier local-shape and prototype experiments were documented as unable
to retain retail's extra lifetime.

Four expected-word-guarded normalizations reproduce the retail register path.
The first two guards preserve the `R_MIPS_HI16:D_800D2FB0` and
`R_MIPS_LO16:D_800D2FB0` relocations on the global load; the other two update
the null-test register and call delay slot. The maintained C behavior is
unchanged.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_C9EC0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
473 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 56-byte linked and retail spans produced SHA-256
`4ea0830d6b2a5c7a1cd2990ca10be04002e0dff9d255fb790dc16c3bb2935fd2`
for both.

The `64CBFDOGL` sibling contains this function only as a generated recomp entry
sourced from the ROM instruction stream. This IDO register-lifetime
normalization does not transfer to host source. Its worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is 5-word `func_150A7A00` with four real
differences. Re-establish its ownership and retail representation before
editing because a four-difference result across five words may indicate a
wrapper, trampoline, or assembly-classification issue rather than ordinary C
register allocation.
