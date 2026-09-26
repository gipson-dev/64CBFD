# Game record-stride register match - 2026-09-25

## Result

All 16 words of `func_1512D6B0` now match retail across
`0x1512D6B0..0x1512D6F0`. The fresh linked matcher reports
`2574 / 5484 (46.94%)` overall and `2006 / 4795 (41.84%)` game. One init
function remains blocked by address drift; 2,909 total and 2,789 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Register evidence

The function indexes a 176-byte record through byte field `arg0+0x23D`, then
compares the record words at `+0xA8` and `+0xAC`. The existing C already emits
the correct shift/subtract multiplication sequence, both loads, XOR equality
reduction, return, and padding.

All nine differences were one closed temporary-register rotation. Retail uses
`t7` for the byte index, `t6` for global `D_800DC2B0`, and `t8` for the scaled
offset; IDO selected `t6`, `t8`, and `t7`. Nine expected-word guards restore
those lifetimes. The two global-base rows explicitly assert unchanged
`R_MIPS_HI16` and `R_MIPS_LO16` relocations.

An explicit `index`/`base`/`offset` source experiment moved the values into
`v1`, `a1`, `t6`, and `a2`, increasing differences, so it was reverted.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_15AA10.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 64-byte linked ELF span at file
offset `0x16D6B0` and pristine extracted retail span at
`conker/conker.us.bin+0x15AB60` produced SHA-256
`3266b541de99bd06941b770d4b38988db458dab3e62d8deb16339a6f96df436a`
for both. The retail-word patch table has 599 rows, no duplicate
filename/function/offset keys, and exactly nine rows for this function.

The `64CBFDOGL` sibling has no hand-maintained implementation of
`func_1512D6B0`. This IDO register-lifetime normalization does not require a
host transplant. Its dirty tree was left untouched, and frozen Release was
not built or launched.

## Next boundary

Continue with 14-word `func_15166FD8`, now the first game row with nine real
differences. It emits the same display-list command as `func_1510E634`; reuse
the typed source and guarded-expansion evidence, but verify its distinct span
and compiler output independently.
