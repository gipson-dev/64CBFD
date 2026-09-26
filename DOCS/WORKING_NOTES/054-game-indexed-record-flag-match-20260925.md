# Game indexed-record flag match - 2026-09-25

## Result

`func_150EA904` is byte-exact across its complete 16-word linked extent
`0x150EA904..0x150EA944`. The fresh C-only matcher reports
`2569 / 5486 (46.83%)` overall and `2001 / 4797 (41.71%)` game. One init
function remains blocked by address drift; 2,916 total and 2,796 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained function already has retail's unused first-argument spill,
`0xA0` record stride, `D_800DBEF4` base, `0xE0` tag test, flag update, branch,
and relocations. Eight words differed only in temporary-register allocation.
IDO kept the scaled index in `t6` and the global base in `t7`; retail uses
`t7` for the index and `t6` for the base. That allocation also advances the
final flag load/update/store from current `t9`/`t0` to retail `t0`/`t1`.

Splitting the global base and scaled index into explicit locals extended their
lifetimes and moved the result away from `v0`. Reversing the commutative
initializer operands compiled identically to the original. Both experiments
were reverted. Eight expected-word-guarded normalizations select retail's
register lifetimes while retaining the original `R_MIPS_HI16` and
`R_MIPS_LO16` references to `D_800DBEF4` at the same offsets.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_117490.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 16 retail words and the target is absent from
the non-exact list. The patch table has 565 rows with no duplicate
filename/function/offset keys and exactly eight rows for this function. An
independent comparison of the complete 64-byte linked ELF span at file offset
`0x12A904` and pristine extracted retail span at
`conker/conker.us.bin+0x117DB4` produced SHA-256
`e5d74fd6f5bb8c46aa7f23be8b07a96782be90cce7e8e3922e07128af750406f`
for both.

The `64CBFDOGL` sibling contains the symbol only in generated recomp output,
backups, and symbol configuration, with no hand-maintained implementation.
This IDO register normalization does not transfer to host source. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 21-word `func_1515D480` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
