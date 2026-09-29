# Game subtype-2 single-byte allocation payload byte match

Date: 2026-09-29

## Scope

This pass completed `func_150D04C4` in
`conker/src/game/generated_FC5F0.c`. The retail slot spans 28 words and 112
bytes at `0x150D04C4..0x150D0530`.

## Recovered behavior

The wrapper forwards a byte selector, record-data pointer, signed halfword,
secondary byte, and final word to `func_150CFF10`. It supplies allocation mode
`8`, subtype `2`, and a zero auxiliary flag. If allocation succeeds, it copies
one zero byte into the destination pointer at offset `0x48` of the returned
record.

The third formal parameter is a signed halfword, causing IDO to canonicalize
the incoming register with retail's left/right shift pair. The local payload
is an eight-byte byte buffer whose first byte is initialized. That shape
reproduces retail's `0x38` frame and payload at `sp+0x30`; a scalar byte had
produced a `0x30` frame and `sp+0x2F`. All 28 words emit directly from semantic
C, with no expected-word guards.

## Verification

- The focused `generated_FC5F0.c.o` build matches all 28 retail words and both
  call relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 112-byte spans share SHA-256
  `245b46b27d2fe98769d605328c6ad1707b46c6e141b43780c8e4dda15ef79688`.
- Fresh matcher totals are `2,935 / 5,465 (53.71%)` overall and
  `2,361 / 4,789 (49.30%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150D13A0`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
