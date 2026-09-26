# Game global PRNG step restoration - 2026-09-25

## Result

`func_151EF610` is restored to its original 12-word assembly ownership across
`0x151EF610..0x151EF640`. The fresh C-only matcher reports
`2570 / 5484 (46.86%)` overall and `2002 / 4795 (41.75%)` game. One init
function remains blocked by address drift; 2,913 total and 2,793 game C
functions still differ. Debugger remains complete at `181 / 181`.

This is a classification correction, not a new exact-C match. Raw assembly is
now 554 functions overall and 523 in game.

## Ownership evidence

The routine advances global `D_80091970` with the recurrence
`((value * 4 + 2) * (value * 4 + 3)) / 4` and returns the new value. The C
model has the correct arithmetic and return value, but IDO materializes one
global address, reuses it for the load and store, and performs the store before
the return. Retail instead uses a direct symbol load, a second `%hi` for the
store, and places the `%lo` store in the `jr ra` delay slot.

An explicit assignment-expression return and a volatile declaration did not
recover the retail lifetime. Removing the explicit return grew the body from
12 to 13 words and left the wrong value in `v0`; that experiment was rejected.
Original assembly ownership preserves both symbol relocation pairs and the
caller-visible result without disguising this routine as matched C.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_21CAC0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 48-byte linked ELF span at file
offset `0x22F610` and pristine extracted retail span at
`conker/conker.us.bin+0x21CAC0` produced SHA-256
`7fa144078d7821335feae3ad8e5f7953424f200288ed27731c1764cd45f04606`
for both. The retail-word patch table remains at 573 rows with no duplicate
filename/function/offset keys and contains no row for this function.

The `64CBFDOGL` sibling contains the symbol in generated recomp output,
configuration, and test fixtures, but no hand-maintained host implementation
of this routine. This IDO ownership correction does not transfer to host
source. Its dirty tree was left untouched, and frozen Release was not built or
launched.

## Next boundary

The eight-difference game tier is complete. The next listed game targets each
have nine real differences:

1. `func_150771F0` - 41 words
2. `func_15080200` - 10 words
3. `func_1510E634` - 15 words
4. `func_1512D6B0` - 16 words
5. `func_15166FD8` - 14 words
6. `func_15196330` - 33 words
7. `func_151963B4` - 33 words
8. `func_151E5F64` - 18 words
9. `func_151E81EC` - 10 words

Start with `func_150771F0` by comparing source, compact object, retail words,
and relocations before editing.
