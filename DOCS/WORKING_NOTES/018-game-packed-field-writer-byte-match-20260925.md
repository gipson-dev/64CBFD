# Game packed-field writer byte match - 2026-09-25

## Result

`func_15079F6C` is byte-exact across its complete 20-word linked extent
`0x15079F6C..0x15079FBC`. The fresh C-only matcher reports
`2537 / 5495 (46.17%)` overall and `1969 / 4806 (40.97%)` game. One init
function remains blocked by address drift; 2,957 total and 2,837 game C
functions still differ.

## Mismatch and resolution

The maintained C body already produced the retail global loads, packed
halfword construction, field stores, scheduling, return sequence, and 20-word
extent. Only the register holding `D_800D1891` differed:

```text
offset  current   retail    interpretation
0x14    90631891  906E1891  load the byte into t6 instead of v1
0x20    01E3C025  01EEC025  combine the packed halfword from t6
```

The archived July audit classified this function as a resistant scratch-
register artifact after source-level variants did not change IDO's choice.
`retail_word_patches.us.csv` now has two function- and offset-scoped guards
that normalize only this temporary lifetime.

The first focused build correctly rejected an expected linked word at `+0x14`:
the compact object contains `0x90630000` plus
`R_MIPS_LO16:D_800D1891`, not the final linked immediate. The accepted row
therefore expects `0x90630000`, writes `0x906E0000`, and explicitly preserves
the same relocation. This keeps the object relocatable and still verifies the
final `0x1891` address after linking.

## Verification

The current checkout passed:

```sh
make build/src/game_A28B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent disassembly and
ROM read compared linked addresses `0x15079F6C..0x15079FBC` with
`conker.us.bin+0xA741C`; all 20 words match. The debugger remains complete at
181 / 181 C rows, plus its independently exact handwritten assembly row.

The `64CBFDOGL` sibling already carries `func_15079F6C` as a generated recomp
function with the same 0x50-byte extent. This IDO-only register normalization
does not transfer to host source. Its unrelated dirty worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

Two two-difference game functions remain, both 20 words:
`func_1516968C` and `func_151696DC`. Continue with `func_1516968C`, auditing
its complete linked body before choosing a source change or guarded
normalization.
