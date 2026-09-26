# Game dead child-pointer third restoration - 2026-09-25

## Result

`func_151AB180` is restored to its original 17-word assembly ownership across
`0x151AB180..0x151AB1C4`. The fresh C-only matcher reports
`2570 / 5485 (46.86%)` overall and `2002 / 4796 (41.74%)` game. One init
function remains blocked by address drift; 2,914 total and 2,794 game C
functions still differ. Debugger remains complete at `181 / 181`.

This is a classification correction, not a new exact-C match. Raw assembly is
now 553 functions overall and 522 in game.

## Ownership evidence

This routine is the third measured member of the dead child-pointer family.
It loads the child pointer at `arg0+0xB0`, clears the child's `+0x70` word,
clears the child field, sets bit 1 at `arg0+0x18`, and calls
`func_1513F6C0(arg0, 0, 0)`. Retail also emits and discards
`addiu v0,v0,0x58` before the call.

The maintained C included the pointer update, but IDO removed it. That shifts
the call relocation and every trailing instruction by one word, producing all
eight measured differences. Preserving the original assembly body retains the
dead update, the `R_MIPS_26 func_1513F6C0` relocation, and the bit-field store
in the call delay slot without disguising the function as matched C.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1D6E80.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 68-byte linked ELF span at file
offset `0x1EB180` and pristine extracted retail span at
`conker/conker.us.bin+0x1D8630` produced SHA-256
`4f98b42bf797016c7e59eee9047f9777c22dbeb51ca0946889bd3b450758683f`
for both. The retail-word patch table remains at 573 rows with no duplicate
filename/function/offset keys and contains no row for this function.

The `64CBFDOGL` sibling contains the symbol only in generated recomp output,
backups, and symbol configuration, with no hand-maintained implementation.
This IDO ownership correction does not transfer to host source. Its dirty tree
was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 12-word `func_151EF610`, the final game row
with eight real differences. Inspect its source, retail words, relocations,
and compiler schedule before editing.
