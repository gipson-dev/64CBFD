# Game scalar-temporary match - 2026-09-25

## Result

`func_150BDB3C` is byte-exact across its complete 13-word linked extent
`0x150BDB3C..0x150BDB70`. The fresh C-only matcher reports
`2548 / 5491 (46.40%)` overall and `1980 / 4802 (41.23%)` game. One init
function remains blocked by address drift; 2,942 total and 2,822 game C
functions still differ.

## Mismatch and resolution

The maintained C body already matched nine of 13 words. Current IDO kept the
shifted signed value in `a1` and loaded the existing byte into `t6`; retail
kept the shifted value in `t6` and the existing byte in `t7`. The four
differences were the byte load, shift destination, comparison operands, and
conditional byte store.

Naming the existing byte as a local, with and without `register`, moved it to
`a2` and worsened the allocation, so that experiment was reverted. Four
expected-word-guarded normalizations preserve the maintained C body while
selecting the retail temporary registers. None of the normalized words carries
a relocation.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_E8C10.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
477 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 52-byte linked and retail spans produced SHA-256
`99c50deb57fa911977f650f3a87b020e2222bad7067a40ca4bd42bf7c94a5249`
for both.

The `64CBFDOGL` sibling contains this function only as a generated recomp entry
sourced from the ROM instruction stream. This IDO register-allocation
normalization does not transfer to host source. Its worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is 18-word `func_150F33B0` with four real
differences. Re-establish its source ownership, linked words, and relocation
context before editing.
