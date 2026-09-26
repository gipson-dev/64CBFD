# Game allocation-wrapper frame match - 2026-09-25

## Result

`func_1515D480` is byte-exact across its complete 21-word linked extent
`0x1515D480..0x1515D4D4`. The fresh C-only matcher reports
`2570 / 5486 (46.85%)` overall and `2002 / 4797 (41.73%)` game. One init
function remains blocked by address drift; 2,915 total and 2,795 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained allocation wrapper already has retail's `arg0*0x60` size,
`allocate_memory(size, 1, 2, 0)` call, `bzero` call, result, instruction order,
and both call relocations. Eight words differed only in stack layout. IDO
selected a 40-byte frame, spilled the incoming count at `sp+0x28`, and placed
the size/result locals at `sp+0x1C` and `sp+0x20`. Retail uses a 32-byte frame,
the incoming spill at `sp+0x20`, and packed locals at `sp+0x18` and `sp+0x1C`.

Separating the local declarations from their assignments compiled to the same
40-byte frame and was reverted. Eight expected-word-guarded normalizations
select retail's frame and local-slot offsets without moving either
`R_MIPS_26` relocation or changing the maintained C behavior.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_18A8F0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 21 retail words and the target is absent from
the non-exact list. The patch table has 573 rows with no duplicate
filename/function/offset keys and exactly eight rows for this function. An
independent comparison of the complete 84-byte linked ELF span at file offset
`0x19D480` and pristine extracted retail span at
`conker/conker.us.bin+0x18A930` produced SHA-256
`6f3d5b75cb02b75945cfc755ed68078a976130c815f221dd9df5c8f4ed1a1316`
for both.

The `64CBFDOGL` sibling contains the symbol only in generated recomp output,
backups, and symbol configuration, with no hand-maintained implementation.
This IDO frame normalization does not transfer to host source. Its dirty tree
was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 17-word `func_151AB180` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
