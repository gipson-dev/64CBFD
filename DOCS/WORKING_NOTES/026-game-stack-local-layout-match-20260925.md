# Game stack-local layout match - 2026-09-25

## Result

`func_15071A64` is byte-exact across its complete 45-word linked extent
`0x15071A64..0x15071B18`. The fresh C-only matcher reports
`2545 / 5493 (46.33%)` overall and `1977 / 4804 (41.15%)` game. One init
function remains blocked by address drift; 2,947 total and 2,827 game C
functions still differ.

## Mismatch and resolution

The function already matched 41 of 45 words. All four differences were stack
addresses passed to three calls: current IDO placed the 36-byte `sp28` array
at `sp+0x34` and `struct17 sp4C` at `sp+0x28`, while retail placed them at
their recovered `sp+0x28` and `sp+0x4C` locations.

Declaring `sp4C` before `sp28` makes IDO allocate the locals in the retail
order. The function then matches naturally from C; no guarded word patch is
needed, and none of the changed stack-address instructions has a relocation.

## Verification

The current checkout passed:

```sh
make build/src/game_981E0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent comparison of the
complete 180-byte linked and retail spans produced SHA-256
`d75ebb203277ef22dbc4f7618afc9da108c33e675cd95d8d2ed3f22ca8c2a28b`
for both.

The `64CBFDOGL` sibling contains this function only as a generated recomp entry
sourced from the ROM instruction stream. This IDO declaration-order fix does
not transfer to host source. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is 34-word `func_15087DCC` with four real
differences. Re-establish its linked mismatch and relocation context before
editing; later four-difference rows include 14-word `func_1509D054`, 5-word
`func_150A7A00`, and 9-word `func_150ADACC`.
