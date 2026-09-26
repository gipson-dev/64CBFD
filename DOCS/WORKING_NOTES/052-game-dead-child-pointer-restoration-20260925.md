# Game dead child-pointer restoration - 2026-09-25

## Result

`func_150C5EFC` is restored to its original 17-word assembly ownership across
`0x150C5EFC..0x150C5F40`. The fresh C-only matcher reports
`2568 / 5487 (46.80%)` overall and `2000 / 4798 (41.68%)` game. One init
function remains blocked by address drift; 2,918 total and 2,798 game C
functions still differ. Debugger remains complete at `181 / 181`.

This is a classification correction, not a new exact-C match. Raw assembly is
now 551 functions overall and 520 in game.

## Ownership evidence

The former C body loaded the child pointer at `arg0+0xB0`, cleared its `+0x58`
word, cleared the child field, set bit 1 at `arg0+0x18`, and called
`func_1513F6C0(arg0, 0, 0)`. Retail performs all of those operations but also
emits `addiu v0,v0,0x58` after the two clears and discards the result before
the call.

The maintained C already contained `temp_v0 += 0x58`, but IDO eliminated the
dead update. Its removal shifts the call and every trailing instruction by one
word, accounting for all eight measured differences. Guarding those words
would have to insert the missing instruction and move the call relocation,
which would disguise source ownership rather than recover it.

The maintained source now selects the preserved assembly body. It retains the
dead `addiu`, the original `R_MIPS_26` relocation for `func_1513F6C0`, and the
bit-field store in the call delay slot.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_F3270.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 68-byte linked ELF span at file
offset `0x105EFC` and pristine extracted retail span at
`conker/conker.us.bin+0xF33AC` produced SHA-256
`1bc413712b2394519da1ebb337be60f51449e0d6eac95a5fa625362e5f41a426`
for both. The retail-word patch table remains at 557 rows with no duplicate
filename/function/offset keys and contains no row for this function.

The `64CBFDOGL` sibling contains the symbol only in generated recomp output,
backups, and symbol configuration, with no hand-maintained implementation.
This IDO ownership correction does not transfer to host source. Its dirty tree
was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 17-word `func_150C682C` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
