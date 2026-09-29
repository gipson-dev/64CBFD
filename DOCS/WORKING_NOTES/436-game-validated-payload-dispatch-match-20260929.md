# Game validated payload dispatcher byte match

Date: 2026-09-29

## Scope

This pass completed `func_150ECB8C` in
`conker/src/game/generated_1199D0.c`. The retail slot spans 29 words and 116
bytes at `0x150ECB8C..0x150ECBFC`.

## Recovered behavior

The routine reads the target pointer stored at owner offset `0x28`. It first
requires the target's opening word to be nonzero, then compares the owner's
byte at offset `0x2C` with the target selector at offset `0x3B`. Either failure
writes `-1` to the owner halfword at offset `0x0E` and returns.

On success, the target pointer and owner bytes at offsets `0x2D..0x31` are
forwarded to `func_1502EA98`, with a zero sixth argument. Expressing the
validation as an early-return failure path reproduces retail's shared store,
branch-likely delay load, duplicated unreachable load word, and direct fall
through from the call to the epilogue. All 29 words emit directly from
semantic C; no expected-word guards are used.

## Verification

- The focused `generated_1199D0.c.o` build matches all 29 retail words and
  the call relocation.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 116-byte spans share SHA-256
  `68df9f722f643d62ec6be026854fd09c8e361cb94615261afd64d54b6cee4240`.
- Fresh matcher totals are `2,937 / 5,465 (53.74%)` overall and
  `2,363 / 4,789 (49.34%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150ECC00`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
