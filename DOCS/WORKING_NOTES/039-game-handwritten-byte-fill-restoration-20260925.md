# Game handwritten byte-fill restoration - 2026-09-25

## Result

`func_150A7770` is restored to its original handwritten eight-word assembly
extent `0x150A7770..0x150A7790`. The fresh C-only matcher reports
`2554 / 5489 (46.53%)` overall and `1986 / 4800 (41.38%)` game. One init
function remains blocked by address drift; 2,934 total and 2,814 game C
functions still differ. The raw-assembly inventory is now 549 total and 518
game functions.

## Classification evidence

The preserved assembly identifies this routine as handwritten. It stores the
first byte before the loop, decrements the count and increments the pointer
with trapping `addi`, then uses `bnel` with the next byte store in its delay
slot. The final `jr`, delay-slot `nop`, and trailing padding word complete the
eight-word extent.

The maintained C modeled the same byte-fill behavior as a `do` loop. IDO did
not reproduce the handwritten branch-likely shape even with loop-unrolling
disabled in earlier experiments; its compiled body exceeded the retail slot
and was redirected through `__retail_overflow_func_150A7770`. Retaining that C
would misclassify handwritten code and leave the linked retail location as a
two-word trampoline.

The false C model is therefore replaced with `GLOBAL_ASM`, and the dedicated
assembly file is now tracked. This is an ownership correction rather than a
new C match.

## Verification

The current checkout passed:

```sh
make build/src/game_D4C20.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all eight retail words and the function is no
longer part of the C-matcher denominator. The patch table remains at 494 rows
with no duplicate filename/function/offset keys. An independent comparison of
the complete 32-byte linked ELF span at file offset `0xE7770` and retail ROM
span at `0xD4C20` produced SHA-256
`5df18a402703136c0a0c99c64eafa3bfe5c65f0f0aade0dcab67f21bed5f0e7c`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol/configuration files. Restoring decomp assembly ownership does not
require a host-source transplant. Its dirty worktree was left untouched, and
its frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is 14-word `func_1515F008` with six real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following game rows `func_1516F8EC`,
`func_1516F91C`, and `func_1516F984` are also in the six-difference tier.
