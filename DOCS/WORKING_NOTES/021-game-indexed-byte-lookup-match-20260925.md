# Game indexed-byte lookup match - 2026-09-25

## Result

`func_150849A0` is byte-exact across its complete 11-word linked extent
`0x150849A0..0x150849CC`. The fresh C-only matcher reports
`2540 / 5493 (46.24%)` overall and `1972 / 4804 (41.05%)` game. One init
function remains blocked by address drift; 2,952 total and 2,832 game C
functions still differ.

## Mismatch and resolution

The function reads a byte index at offset `0x1C9`, then returns either the
indexed preceding byte or the first byte of the pointer stored at offset
`0x2C4`. Its control flow, loads, offsets, and return paths already matched.
Only the index register differed across three instructions: current IDO reused
return register `v0`, while retail kept the index in `v1` and used `v0` only
for the returned byte.

Changing the local index type from `u8` to `s32` preserves the value and
behavior of the zero-extended byte load while separating the index and return
lifetimes. IDO then emits the retail `v1` allocation naturally. No guarded
word normalization is needed.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_AEB40.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent extraction of the
linked `.game` section compared all 44 bytes with `conker.us.bin+0xB1E50`;
both slices have SHA-256
`a9c2b556bc04c94bc24acdaab75d2f6c1fb49c949ada74fef06f7b2eb09c7e57`.

The `64CBFDOGL` sibling already carries `func_150849A0` as a generated recomp
entry. This IDO local-allocation fix does not transfer to host source. Its
unrelated worktree was left untouched, and its frozen Release configuration
was not built or launched.

## Next boundary

Four game rows remain at three real differences. Inspect 19-word
`func_150636A4` next, followed by `func_1514672C` (30 words),
`func_15199980` (36 words), and `func_1505D024` (104 words).
