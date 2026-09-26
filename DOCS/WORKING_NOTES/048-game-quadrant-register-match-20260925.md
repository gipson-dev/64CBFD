# Game quadrant register match - 2026-09-25

## Result

`func_151423D8` is byte-exact across its complete 27-word linked extent
`0x151423D8..0x15142444`. The fresh C-only matcher reports
`2564 / 5488 (46.72%)` overall and `1996 / 4799 (41.59%)` game. One init
function remains blocked by address drift; 2,923 total and 2,803 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained byte-angle lookup already has retail's argument mask,
reflection around `0x40`, quadrant test, table lookup, sign selection, control
flow, and function length. Both `D_8009A220` HI16/LO16 relocation pairs also
matched before this pass.

Seven words differed as one allocator cascade. IDO kept the quadrant in the
now-dead `a0` register and used `t0`/`t1` for the positive and negative table
index shifts. Retail keeps the quadrant in `t0` and advances the shift
temporaries to `t1`/`t2`. Seven symmetric expected-word-guarded,
non-relocating normalizations select those retail registers without obscuring
the source or moving either relocation pair.

## Verification

The current checkout passed:

```sh
make build/src/game_16EE20.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
make tools-check
```

The focused object contains all 27 retail words and the target is absent from
the non-exact list. The patch table has 550 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
108-byte linked ELF span at file offset `0x1823D8` and pristine extracted
retail span at `conker/conker.us.bin+0x16F888` produced SHA-256
`7d8800bced6a6b54940fa6f014a7a233975aacb0ba279b0bc6d6d021ab6e86c7`
for both.

The `64CBFDOGL` sibling contains this symbol in generated recomp output,
configuration, and host-side test fixtures, but has no hand-maintained
implementation. This IDO register normalization does not transfer to host
source. Its dirty tree was left untouched, and frozen Release was not built
or launched.

## Next boundary

The next listed game target is 17-word `func_15155EF8` with seven real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
