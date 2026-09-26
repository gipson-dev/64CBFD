# Game chained global clear match - 2026-09-25

## Result

All ten words of `func_15080200` now match retail across
`0x15080200..0x15080228`. The fresh linked matcher reports
`2572 / 5484 (46.90%)` overall and `2004 / 4795 (41.79%)` game. One init
function remains blocked by address drift; 2,911 total and 2,791 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Source evidence

The routine clears `D_800D192C`, `D_800D1928`, and `D_800D1930`. Three
independent C assignments compile to eight instructions: IDO uses direct
symbol stores and the retail slot ends with two padding words. Explicit local
pointers are optimized into the same shape.

Writing the operation as
`D_800D1930 = D_800D1928 = D_800D192C = 0` recovers the original ten-word
body. IDO retains the first two addresses in `v0` and `v1`, stores through
those registers in retail order, then emits the final direct symbol store.
The change needs no guarded normalization.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_AD6B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 40-byte linked ELF span at file
offset `0xC0200` and pristine extracted retail span at
`conker/conker.us.bin+0xAD6B0` produced SHA-256
`5fe7f7f6c8dc160faba47b5b2a363a0d7a7ca5dadc9982da1e3fe41d9141e7b6`
for both. The retail-word patch table remains at 582 rows with no duplicate
filename/function/offset keys and contains no row for this function.

The `64CBFDOGL` sibling has no hand-maintained implementation of
`func_15080200`. This source-level compiler-shape correction does not require
a host transplant. Its dirty tree was left untouched, and frozen Release was
not built or launched.

## Next boundary

Continue with 15-word `func_1510E634`, now the first game row with nine real
differences. Compare its C body, compact object, retail words, and relocations
before editing.
