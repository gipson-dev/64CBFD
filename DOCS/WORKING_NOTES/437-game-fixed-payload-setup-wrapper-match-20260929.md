# Game fixed payload-setup wrapper byte match

Date: 2026-09-29

## Scope

This pass completed `func_150ECC00` in
`conker/src/game/generated_1199D0.c`. The retail slot spans 28 words and 112
bytes at `0x150ECC00..0x150ECC6C`.

## Recovered behavior

The wrapper first forwards its owner pointer, selector byte, and final word to
`func_151C9AC0`. It then calls `func_150ECA68` with the same owner and the
fixed argument tuple `0, 0xFF, 0, 0xFF, 4, -1`, followed by the original
selector byte and final word.

The selector is modeled as a volatile byte formal because retail stores the
incoming word unchanged and performs two independent low-byte reads from its
stack home, one before each call. A nonvolatile byte or explicit cast lets IDO
cache that conversion, enlarging the frame and changing the schedule. The
volatile form recovers retail's `0x30` frame and both byte loads naturally.
All 28 words emit directly from semantic C; no expected-word guards are used.

## Verification

- The focused `generated_1199D0.c.o` build matches all 28 retail words and
  both call relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 112-byte spans share SHA-256
  `5af0f6f5ba18580c81f2287f4d54cfd6f25fcdea88f33ff5853d1733759c1c0b`.
- Fresh matcher totals are `2,938 / 5,465 (53.76%)` overall and
  `2,364 / 4,789 (49.36%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150F739C`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
