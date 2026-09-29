# Game eight-byte allocation payload wrapper byte match

Date: 2026-09-28

## Scope

This pass completed `func_150D02B4` in
`conker/src/game/generated_FC5F0.c`. The retail slot spans 30 words and 120
bytes at `0x150D02B4..0x150D0328`.

## Recovered behavior

The wrapper initializes the first eight bytes of a local record with a
floating zero and a signed-halfword zero. It forwards the byte selector,
record-data pointer, signed halfword, secondary byte, and final word to
`func_150CFF10`, supplying allocation mode `8`, subtype `1`, and a zero
auxiliary flag. If allocation succeeds, it copies the initialized eight-byte
prefix to the destination pointer at offset `0x48` of the returned record.

The third formal parameter is a signed halfword. Recovering that type makes
IDO canonicalize the incoming register with retail's left/right shift pair
instead of reloading a halfword from its stack home. The local record occupies
12 bytes even though only its initialized eight-byte prefix is copied; that
layout places the floating and halfword fields at retail's `sp+0x2C` and
`sp+0x30`. All 30 words emit directly from semantic C, with no expected-word
guards.

## Verification

- The focused `generated_FC5F0.c.o` build matches all 30 retail words and both
  call relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 120-byte spans share SHA-256
  `ce5cfca6e4c29e1436a90a321944d7eb038dcad21ec146b83f59457a56586ee8`.
- Fresh matcher totals are `2,934 / 5,465 (53.69%)` overall and
  `2,360 / 4,789 (49.28%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150D04C4`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
