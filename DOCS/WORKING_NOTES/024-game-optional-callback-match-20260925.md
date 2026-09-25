# Game optional-callback match - 2026-09-25

## Result

`func_15199980` is byte-exact across its complete 36-word linked extent
`0x15199980..0x15199A10`. The fresh C-only matcher reports
`2543 / 5493 (46.30%)` overall and `1975 / 4804 (41.11%)` game. One init
function remains blocked by address drift; 2,949 total and 2,829 game C
functions still differ.

## Mismatch and resolution

The function dispatches two optional indexed callbacks and then releases an
optional object at record offset `0x148`. Its first 27 and final six words
already matched. In the remaining three words, current IDO loaded the optional
pointer into `t8`, tested `t8`, then reloaded the pointer into `a0` in the
call delay slot. Retail loaded the pointer directly into `a0`, tested `a0`,
and left the call delay slot empty.

Naming the loaded callback argument as a local `void *` gives it the intended
lifetime. IDO then selects `a0` naturally and emits the retail sequence with
no guarded word normalization.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1C2C60.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent extraction of the
linked `.game` section compared all 144 bytes with
`conker.us.bin+0x1C6E30`; both slices have SHA-256
`e119eadc3db707c279dbacd15731434df6ee0e48cfe9361e3c71add7774989e5`.

The `64CBFDOGL` sibling contains this function as a generated recomp entry
sourced from the ROM instruction stream. This IDO source-lifetime fix does not
transfer to host source. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

`func_1505D024` is the final game row with three real differences. It is 104
words and has prior failed source-shape experiments recorded in the historical
update log; re-establish its current linked mismatch before editing.
