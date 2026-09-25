# Game call-argument register match - 2026-09-25

## Result

`func_1505D024` is byte-exact across its complete 104-word linked extent
`0x1505D024..0x1505D1C4`. The fresh C-only matcher reports
`2544 / 5493 (46.31%)` overall and `1976 / 4804 (41.13%)` game. One init
function remains blocked by address drift; 2,948 total and 2,828 game C
functions still differ.

## Mismatch and resolution

The maintained C body already matched 101 of 104 words. The first independent
difference reloaded the object pointer from `sp+0x40` into `a1`, while retail
reused the pointer already live in `t0`. The other two differences loaded and
stored the final stack argument constant through `t0`, while retail used `t1`.

Three expected-word-guarded normalizations preserve the source and call
structure while selecting those retail register lifetimes. The guards verify
the compiler output being replaced, and none of the three words carries a
relocation.

## Verification

The current checkout passed:

```sh
make build/src/game_83300.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
469 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 416-byte linked and retail spans produced SHA-256
`3c6867e893203e7c2c598b64917c309c8231ba72698422767fdf42e16d08e468`
for both.

The `64CBFDOGL` sibling contains this function only as a generated recomp entry
sourced from the ROM instruction stream. This IDO register-lifetime
normalization does not transfer to host source. Its worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The three-difference game queue is complete. The next listed game target is
45-word `func_15071A64` with four real differences; 34-word
`func_15087DCC` is the other four-difference game row. Re-establish the chosen
target's linked mismatch and relocation context before editing.
