# Game PRNG seed setter restoration - 2026-09-25

## Result

`func_150ADACC` is restored from its maintained C equivalent to the original
handwritten assembly across the complete nine-word extent
`0x150ADACC..0x150ADAF0`. The fresh C-only matcher reports
`2547 / 5491 (46.38%)` overall and `1979 / 4802 (41.21%)` game. One init
function remains blocked by address drift; 2,943 total and 2,823 game C
functions still differ.

## Classification

Retail increments the 32-bit argument with MIPS III `daddiu`, writes the
result to 64-bit PRNG seed `D_800885B0`, then emits an otherwise dead
`li a0, 0` before returning. The source already documented this distinctive
sequence as handwritten assembly that IDO C cannot reproduce faithfully.

The prior C body remains behaviorally equivalent, but it used `addiu`, stored
through temporary register `t6`, omitted the dead argument clear, and occupied
only five instructions before padding. Restoring the extracted body preserves
the `R_MIPS_HI16:D_800885B0` and `R_MIPS_LO16:D_800885B0` relocations and the
three trailing alignment words.

## Verification

The current checkout passed:

```sh
make build/src/game_DAE50.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is now assembly-classified and absent from the C mismatch list. An
independent comparison of the complete 36-byte linked and retail spans
produced SHA-256
`701e30e662e4d149927dcdebc520123d68e7008d58a30aaf4cd91d838cf642ac`
for both.

The `64CBFDOGL` sibling contains this function as a generated recomp entry
sourced from the same ROM instructions, so no host-source transplant is
needed. Its worktree was left untouched, and its frozen Release configuration
was not built or launched.

## Next boundary

The next listed game target is 13-word `func_150BDB3C` with four real
differences. Re-establish its source ownership, retail words, and relocation
context before editing.
