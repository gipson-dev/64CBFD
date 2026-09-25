# Game synthetic-return trampoline - 2026-09-25

## Result

False zero-return C placeholder `func_150A7A00` is restored to its original
five-word assembly body across `0x150A7A00..0x150A7A14`. The fresh C-only
matcher reports `2547 / 5492 (46.38%)` overall and
`1979 / 4803 (41.20%)` game. One init function remains blocked by address
drift; 2,944 total and 2,824 game C functions still differ.

## Classification

Retail saves the incoming return address in `t9`, installs `func_150A7A14` in
`ra`, and jumps to `func_150A7960`. This synthetic-return linkage cannot be
represented by the former `return 0` C placeholder and is deliberate assembly,
not an ordinary five-word compiler near-match.

The restored body follows the established `GLOBAL_ASM` pattern used for other
handwritten or fallthrough boundaries. Its HI16/LO16 relocations target
`func_150A7A14`, and its jump relocation targets `func_150A7960`.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_D4E10.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is now assembly-classified and absent from the C mismatch list. An
independent comparison of the complete 20-byte linked and retail spans
produced SHA-256
`f0dd2393d582d4bfb33254dfda4600180d8c147e5a69dac3f12dbc68bae33199`
for both.

The `64CBFDOGL` sibling contains this function as a generated recomp entry
sourced from the same ROM instructions, so no host-source transplant is
needed. Its worktree was left untouched, and its frozen Release configuration
was not built or launched.

## Next boundary

The next listed game target is 9-word `func_150ADACC` with four real
differences. Re-establish its source ownership and retail words before editing.
