# Game set-bit temporary match - 2026-09-25

## Result

`func_150F33B0` is byte-exact across its complete 18-word linked extent
`0x150F33B0..0x150F33F8`. The fresh C-only matcher reports
`2549 / 5491 (46.42%)` overall and `1981 / 4802 (41.25%)` game. One init
function remains blocked by address drift; 2,941 total and 2,821 game C
functions still differ.

## Mismatch and resolution

The maintained C body already matched 14 of 18 words, including the
`D_800DBFF0` relocation pair, floating-point comparison, branch-likely shape,
clear-bit arm, and returns. Current IDO used `t9` for the set-arm byte and
`t0` for the OR result; retail used `t0` and `t1`. The four differences were
the branch-delay load, its unreachable scheduled duplicate, the OR, and the
store.

An explicit byte value temporary moved the pair backward to `v0` and `t9`.
A named pointer increased the function from `0x48` to `0x50` bytes. Expanding
the compound assignment emitted the original `t9`/`t0` pair. Those source
experiments were reverted. Four expected-word-guarded normalizations preserve
the concise maintained C body while selecting the retail temporary registers.
None of the normalized words carries a relocation.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_11FF10.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
481 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 72-byte linked and retail spans produced SHA-256
`a35053910df25a072d547261fc3c16e1dc5897daa93353b7e12381787cf1c7fa`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO register-allocation normalization does not
transfer to host source. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is 40-word `func_151254F4` with four real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following game row is nine-word `func_1515FB70`,
also with four real differences.
