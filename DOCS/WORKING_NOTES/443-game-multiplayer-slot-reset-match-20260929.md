# Game multiplayer-slot reset byte match

Date: 2026-09-29

## Scope

This pass completed `func_151298C0` in
`conker/src/game/generated_156160.c`. The retail slot spans 29 words and 116
bytes at `0x151298C0..0x15129934`.

## Recovered behavior

The routine accepts a player-state pointer and first checks the global
multiplayer count `D_80089550`. When multiplayer state is active, it uses the
player index at offset `0x23D` to select a `0x24`-byte record in
`D_800DC028`. It clears the halfword at record offset `2`, writes `-1.0f` at
offset `4`, and copies `D_800A3610` to offset `8`. An inactive multiplayer
count leaves the table unchanged.

A local record type captures the table stride and three written fields. The
semantic field assignments naturally preserve retail's repeated player-index
loads and multiplications, as well as its integer and floating-point constant
schedule. The unused second integer parameter reproduces retail's entry spill.
All 29 words and six HI/LO relocations emit directly from C; no expected-word
guards are required.

## Verification

- The focused `generated_156160.c.o` build matches all 29 retail words and all
  six data relocations directly from C.
- The incremental full `wsl make -C conker NON_MATCHING=1 -j1` rebuild and
  relink completed successfully.
- The linked ELF and retail 116-byte spans share SHA-256
  `8fff14e7c9b648c89670a714b6e49fbbab7cecd3e055020618b33a3650abb410`.
- Fresh matcher totals are `2,944 / 5,465 (53.87%)` overall and
  `2,370 / 4,789 (49.49%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15181D00`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
