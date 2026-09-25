# Game float-bound load-order match - 2026-09-25

## Result

`func_1514672C` is byte-exact across its complete 30-word linked extent
`0x1514672C..0x151467A4`. The fresh C-only matcher reports
`2542 / 5493 (46.28%)` overall and `1974 / 4804 (41.09%)` game. One init
function remains blocked by address drift; 2,950 total and 2,830 game C
functions still differ.

## Mismatch and resolution

The function accepts a three-float vector only when its components remain
inside two global bounds. Its comparisons, branches, return paths, and final
27 words already matched. The three opening words were independently ordered:
current IDO loaded `arg0->unk0` before materializing `D_800A56C4`, while
retail materialized and loaded the threshold first.

Earlier source-shape experiments are recorded in the historical update log.
An explicit threshold temporary compiled identically, and more invasive
variants worsened the result, so the maintained expression was preserved.
Three expected-word-guarded scheduling normalizations now reproduce retail's
opening order. The `R_MIPS_HI16:D_800A56C4` and
`R_MIPS_LO16:D_800A56C4` relocations move with the reordered instructions;
the third load remains unrelocated.

## Verification

The current checkout passed:

```sh
make build/src/game_16EE20.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent extraction of the
linked `.game` section compared all 120 bytes with
`conker.us.bin+0x173BDC`; both slices have SHA-256
`2a6b49ba77569140aa629c98b4ac6251438b3471cc787a709f0bd4aeca47a2f3`.

The `64CBFDOGL` sibling contains this function as a generated recomp entry
sourced from the ROM instruction stream. This IDO scheduling normalization
does not transfer to host source. Its worktree was left untouched, and its
frozen Release configuration was not built or launched.

## Next boundary

Two game rows remain at three real differences. Inspect 36-word
`func_15199980` next, followed by 104-word `func_1505D024`.
