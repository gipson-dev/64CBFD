# Game identifier check byte match - 2026-09-25

## Result

`func_1519C910` is byte-exact across its complete 14-word linked extent
`0x1519C910..0x1519C948`. The fresh C-only matcher reports
`2535 / 5495 (46.13%)` overall and `1967 / 4806 (40.93%)` game. One init
function remains blocked by address drift; 2,959 total and 2,839 game C
functions still differ.

## Mismatch and resolution

The maintained C body already produced the retail loads, likely branches,
delay-slot return values, zero return, dead shared-return assignment, and
14-word extent. Only the operands of its two equality branches differed:

```text
offset  current   retail    interpretation
0x10    50AE0007  51C50007  beql a1,t6 -> beql t6,a1
0x1C    50AF0004  51E50004  beql a1,t7 -> beql t7,a1
```

Reversing both equality expressions in C produced the same original words;
IDO canonicalized the commutative comparisons back to `$a1` first. That
no-op source experiment was reverted. `retail_word_patches.us.csv` now has
two function- and offset-scoped expected-word guards that normalize only
these branch operands and abort if either compiler input word changes.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1C2C60.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent disassembly and
ROM read compared linked addresses `0x1519C910..0x1519C948` with
`conker.us.bin+0x1C9DC0`; all 14 words match. The debugger remains complete
at 181 / 181 C rows, plus its independently exact handwritten assembly row.

The `64CBFDOGL` sibling already carries `func_1519C910` as a generated recomp
function with the same 0x38-byte extent. This IDO-only equality normalization
does not transfer to host source. Its unrelated dirty worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The remaining two-difference game queue is `func_1517F448` (16 words),
`func_15079F6C` (20 words), `func_1516968C` (20 words), and
`func_151696DC` (20 words). Continue with `func_1517F448`, auditing its full
linked body before choosing a source change or guarded normalization.
