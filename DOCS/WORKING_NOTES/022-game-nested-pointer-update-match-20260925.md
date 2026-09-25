# Game nested-pointer update match - 2026-09-25

## Result

`func_150636A4` is byte-exact across its complete 19-word linked extent
`0x150636A4..0x150636F0`. The fresh C-only matcher reports
`2541 / 5493 (46.26%)` overall and `1973 / 4804 (41.07%)` game. One init
function remains blocked by address drift; 2,951 total and 2,831 game C
functions still differ.

## Mismatch and resolution

The function follows two guarded pointers rooted at the object passed in
`arg0`, writes `0x1E` at nested offset `0x195`, and stores the source-object
index at offset `0x196`. Its compact 19-word body, branches, arithmetic, and
relocations already matched. Only three words differed: current IDO held the
nested pointer in `v1`, while retail held it in `a1` for the load, null test,
and first byte store.

Two source-only experiments added a second pointer parameter, once normally
and once with an explicit `register` qualifier. Both made IDO spill `a1` to
`4(sp)`, retained `v1` for the nested pointer, and expanded the body from
`0x4C` to `0x50`; the generated-slice size guard rejected both forms. The
one-argument source was restored. Three expected-word-guarded normalizations
now encode the retail `a1` lifetime without changing control flow or any
relocation-bearing instruction.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_90840.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent extraction of the
linked `.game` section compared all 76 bytes with `conker.us.bin+0x90B54`;
both slices have SHA-256
`fdf526a66f30745672a5e08113fde82311f0eb1c645547788fd70e41be77a9d6`.

The `64CBFDOGL` sibling contains this function only as a generated recomp
entry sourced from the ROM instruction stream. This IDO register-allocation
normalization does not transfer to host source. Its worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

Three game rows remain at three real differences. Inspect 30-word
`func_1514672C` next, followed by `func_15199980` (36 words) and
`func_1505D024` (104 words). Prior source-shape work on `func_1514672C` found
an independent-load ordering difference feeding a float comparison; an
explicit temporary compiled identically and more invasive variants worsened
the result, so begin from the restored source and current linked evidence.
