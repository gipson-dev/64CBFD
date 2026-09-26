# Game destination-pointer schedule match - 2026-09-25

## Result

`func_150CDB6C` is byte-exact across its complete 17-word linked extent
`0x150CDB6C..0x150CDBB0`. The fresh C-only matcher reports
`2561 / 5488 (46.67%)` overall and `1993 / 4799 (41.53%)` game. One init
function remains blocked by address drift; 2,926 total and 2,806 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained C already had the correct signed range checks, global pointer
load, null guard, integer-to-float conversion, multiplier, and destination
field. IDO folded the explicit `temp_v0 + 0x28` pointer into a direct
`0x2C(temp_v0)` store. Retail instead materializes that address in `v1`
between the conversion and multiply, then stores at `4(v1)`.

Adding `register` to the destination-pointer local was tested and was inert.
The generated-slice padder intentionally does not insert words, but this
compiled symbol is one word shorter than its retail slot and is already
followed by zero padding. Seven expected-word-guarded, non-relocating
normalizations therefore restore the three branch displacements, destination
pointer materialization, multiply/store schedule, and return position. The
existing zero-filled final word becomes retail's `jr` delay-slot `nop`.

The `D_80088870` and `D_800A07A4` HI16/LO16 relocation pairs remain on their
original compiled words and are not touched by the normalization.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_FA360.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 17 retail words and the target is absent from
the non-exact list. The patch table has 533 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
68-byte linked ELF span at file offset `0x10DB6C` and pristine extracted
retail span at `conker/conker.us.bin+0xFB01C` produced SHA-256
`fcfdce01e41617b0521a8bb8a86985f675eff73c41145a5436b3ea2e10922d4f`
for both.

The `64CBFDOGL` sibling contains this symbol only in generated recomp output
and symbol configuration, with no hand-maintained implementation. This IDO
schedule normalization therefore does not transfer to host source. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 16-word `func_15108B80` with seven real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
