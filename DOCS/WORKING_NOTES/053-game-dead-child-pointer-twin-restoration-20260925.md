# Game dead child-pointer twin restoration - 2026-09-25

## Result

`func_150C682C` is restored to its original 17-word assembly ownership across
`0x150C682C..0x150C6870`. The fresh C-only matcher reports
`2568 / 5486 (46.81%)` overall and `2000 / 4797 (41.69%)` game. One init
function remains blocked by address drift; 2,917 total and 2,797 game C
functions still differ. Debugger remains complete at `181 / 181`.

This is a classification correction, not a new exact-C match. Raw assembly is
now 552 functions overall and 521 in game.

## Ownership evidence

This routine is a structural twin of restored `func_150C5EFC`. It loads the
child pointer at `arg0+0xB0`, clears the child's `+0x6C` word rather than
`+0x58`, clears the child field, sets bit 1 at `arg0+0x18`, and calls
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
make build/src/game/generated_F3BA0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 68-byte linked ELF span at file
offset `0x10682C` and pristine extracted retail span at
`conker/conker.us.bin+0xF3CDC` produced SHA-256
`55653ae91d16b26d46b4fa3f6132f078d6ee1f494d18ee7f3b349f4c645e49be`
for both. The retail-word patch table remains at 557 rows with no duplicate
filename/function/offset keys and contains no row for this function.

The `64CBFDOGL` sibling contains the symbol only in generated recomp output,
backups, and symbol configuration, with no hand-maintained implementation.
This IDO ownership correction does not transfer to host source. Its dirty tree
was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 16-word `func_150EA904` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
