# Game opening-load schedule match - 2026-09-25

## Result

`func_151254F4` is byte-exact across its complete 40-word linked extent
`0x151254F4..0x15125594`. The fresh C-only matcher reports
`2550 / 5491 (46.44%)` overall and `1982 / 4802 (41.27%)` game. One init
function remains blocked by address drift; 2,940 total and 2,820 game C
functions still differ.

## Mismatch and resolution

The maintained C body already matched 36 of 40 words. Current IDO saved `ra`
and the second argument immediately after allocating the frame, then loaded
global scale `D_800A352C`. Retail loaded the scale first and performed the two
frame saves afterward. The rest of the function, including both calls,
floating-point calculations, zeroing stores, and indexed `D_800CC2D0`
address construction, already matched.

Four expected-word-guarded scheduling normalizations reproduce the retail
opening. The `R_MIPS_HI16:D_800A352C` and `R_MIPS_LO16:D_800A352C`
relocations move with their load instructions; the two frame stores remain
unrelocated. The maintained C semantics are unchanged.

## Verification

The current checkout passed:

```sh
make build/src/game_14FF90.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. The generated patch table has
485 rows and no duplicate filename/function/offset keys. An independent
comparison of the complete 160-byte linked and retail spans produced SHA-256
`101b0a798fd62bebff254c4e531cc4ec1ac95ca2718289d59c81c5275f204690`
for both.

The `64CBFDOGL` sibling contains generated recomp and symbol references plus a
behavior test that names this guest function. The change only normalizes the
ordering of equivalent guest instructions, so no host-source or behavior-test
change applies. Its worktree was left untouched, and its frozen Release
configuration was not built or launched.

## Next boundary

The next listed game target is nine-word `func_1515FB70` with four real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following game row is 117-word `func_1505841C`
with five real differences.
