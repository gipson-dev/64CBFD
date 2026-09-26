# Game dead-pointer expression restoration - 2026-09-25

## Result

`func_150C7930` is restored to its original 14-word assembly ownership across
`0x150C7930..0x150C7968`. The fresh C-only matcher reports
`2560 / 5488 (46.65%)` overall and `1992 / 4799 (41.51%)` game. One init
function remains blocked by address drift; 2,927 total and 2,807 game C
functions still differ. Debugger remains complete at `181 / 181`.

This is a classification correction, not a new exact-C match. Raw assembly is
now 550 functions overall and 519 in game.

## Ownership evidence

The former C body loaded `D_800DBEF4`, read the word at `+0x21C`, masked its
upper half into `arg0+0x3C`, and called `func_151150BC`. Retail performs those
operations but also emits `addiu v0,v0,0x1E0` after the load and discards the
result before the call.

Plain unused locals, expression statements, self-assignment, `register`, comma
discard, and folding the expression into the adjacent load were tested; IDO
eliminated the dead pointer expression in every case. Address-taken and array
forms retained work only by adding a non-retail stack store. The callee is a
one-argument function and does not provide a legitimate second-argument
lifetime for the value. Keeping the body classified as C would therefore
require patching the missing instruction and relocating the following call,
which would disguise source ownership rather than recover it.

The maintained source now selects the preserved assembly body. It retains the
dead `addiu`, the store in the `jal` delay slot, and the original
`R_MIPS_HI16`/`R_MIPS_LO16` references to `D_800DBEF4` plus the
`R_MIPS_26` call relocation for `func_151150BC`.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_F4D20.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 56-byte linked ELF span at file
offset `0x107930` and pristine extracted retail span at
`conker/conker.us.bin+0xF4DE0` produced SHA-256
`aea09cd04df8f6357dac1d131c53561000dc6cd942a8eb0b1c753bf8a23cd5e1`
for both. The retail-word patch table remains at 526 rows with no duplicate
filename/function/offset keys.

The `64CBFDOGL` sibling contains only generated symbol and recomp-dispatch
references for this routine, not a hand-maintained implementation. No host
source change applies. Its dirty tree was left untouched, and frozen Release
was not built or launched.

## Next boundary

The next listed game target is 17-word `func_150CDB6C` with seven real
differences. Inspect its source, retail words, relocations, and compiler
schedule before choosing a source rewrite or guarded normalization.
