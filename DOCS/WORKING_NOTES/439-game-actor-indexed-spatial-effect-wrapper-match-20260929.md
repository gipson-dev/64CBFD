# Game actor-indexed spatial-effect wrapper byte match

Date: 2026-09-29

## Scope

This pass completed `func_150FFB6C` in
`conker/src/game/generated_12C1E0.c`. The retail slot spans 28 words and 112
bytes at `0x150FFB6C..0x150FFBD8`.

## Recovered behavior

The routine forwards three floating position components to `func_1505D1C4`.
It merges the caller's flags with `0x60000`, derives an actor index by
subtracting `D_800CC2D0` from the actor pointer and dividing by the `0x32C`
actor stride, and reads the unsigned halfword at actor offset `0x7A`. The
remaining arguments are zero and the caller's final word.

Explicit locals for the actor index and halfword expose their independent
lifetimes. IDO then schedules the halfword and three position loads across the
signed division before reading `mflo`, matching retail naturally. All 28 words
emit directly from semantic C; no expected-word guards are used.

## Verification

- The focused `generated_12C1E0.c.o` build matches all 28 retail words and all
  three relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 112-byte spans share SHA-256
  `df92d35779e03d460d880c2851953b934cce41d52f5cd14206ef8158e240a919`.
- Fresh matcher totals are `2,940 / 5,465 (53.80%)` overall and
  `2,366 / 4,789 (49.40%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_15108BC0`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
