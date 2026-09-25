# Game indexed counter byte match - 2026-09-25

## Result

`func_1517F448` is byte-exact across its complete 16-word linked extent
`0x1517F448..0x1517F488`. The fresh C-only matcher reports
`2536 / 5495 (46.15%)` overall and `1968 / 4806 (40.95%)` game. One init
function remains blocked by address drift; 2,958 total and 2,838 game C
functions still differ.

## Mismatch and resolution

The maintained C body already produced the retail array indexing, loads,
comparison, global increment, conditional store, return sequence, and 16-word
extent. Only two independent address calculations were scheduled in the
opposite order:

```text
offset  current   retail    interpretation
0x10    004E1821  01E27821  compute D_800DDE28 element first
0x14    01E27821  004E1821  compute D_800DDDB0 element second
```

Adding an explicit pointer for `D_800DDE28` and reversing the two pointer
declarations both reproduced the original compiler schedule. Those no-op
source experiments were reverted. `retail_word_patches.us.csv` now has two
function- and offset-scoped expected-word guards that exchange only these
independent words and abort if either compiler input changes.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1AC2F0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent disassembly and
ROM read compared linked addresses `0x1517F448..0x1517F488` with
`conker.us.bin+0x1AC8F8`; all 16 words match. The debugger remains complete
at 181 / 181 C rows, plus its independently exact handwritten assembly row.

The `64CBFDOGL` sibling already carries `func_1517F448` as a generated recomp
function with the same 0x40-byte extent. This IDO-only scheduling
normalization does not transfer to host source. Its unrelated dirty worktree
was left untouched, and its frozen Release configuration was not built or
launched.

## Next boundary

Three two-difference game functions remain, each 20 words:
`func_15079F6C`, `func_1516968C`, and `func_151696DC`. Continue with
`func_15079F6C`, auditing its complete linked body before choosing a source
change or guarded normalization.
