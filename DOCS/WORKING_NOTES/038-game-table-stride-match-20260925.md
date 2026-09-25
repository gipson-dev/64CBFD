# Game table-stride match - 2026-09-25

## Result

`func_150770E4` is byte-exact across its complete 36-word linked extent
`0x150770E4..0x15077174`. The fresh C-only matcher reports
`2554 / 5490 (46.52%)` overall and `1986 / 4801 (41.37%)` game. One init
function remains blocked by address drift; 2,935 total and 2,815 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The original C indexed a float table with
`D_800D154C->unk222 * 203`. IDO calculated the 203-element index in `t8`, then
put the implicit four-byte element scaling in `t9`. That consumed `t9` and
forced the independently loaded threshold byte into `t0`. Retail instead
keeps the entire byte-offset chain in `t8` and loads the threshold through
`t9`, producing six register-only differences.

An explicit element-index local was tested and rejected. It preserved the
original index in `v0`, moved the multiplication chain to `t7`, and increased
the mismatch. Expressing the equivalent access through a byte pointer with
the combined `203 * sizeof(f32) = 812` stride let IDO strength-reduce the
whole offset as one lifetime. The resulting object matches retail naturally,
including all three global relocations and the unsigned-byte-to-float
conversion path.

This is a source-level expression recovery. It adds no guarded word patches.

## Verification

The current checkout passed:

```sh
make build/src/game_A28B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 36 retail words and the target is absent from
the non-exact list. The patch table remains at 494 rows with no duplicate
filename/function/offset keys. An independent comparison of the complete
144-byte linked ELF span at file offset `0xB70E4` and retail ROM span at
`0xA4594` produced SHA-256
`7d295305c79d2c334bf958b7ca9a4d50402bb1c8c0ded4d1a797ec923610ec08`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO expression recovery does not transfer to
hand-maintained host source. Its dirty worktree was left untouched, and its
frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is eight-word `func_150A7770` with six real
differences. Earlier experiments identify it as a likely synthetic overflow
trampoline whose apparent C loop does not fit the retail extent; classify its
original ownership before attempting another C rewrite.
