# Game damped motion-state integrator byte match

Date: 2026-09-29

## Scope

This pass completed `func_150D13A0` in
`conker/src/game/generated_FE850.c`. The retail slot spans 28 words and 112
bytes at `0x150D13A0..0x150D140C`.

## Recovered behavior

The routine integrates the float at offset `0xBC` into the position-like
field at `0xB8`, then scales that velocity-like field by `D_800A08B0`. It
scales the field at `0x3C` by `D_800A08B4`, integrates the float at `0x148`
into the field at `0xC4`, and scales the `0x148` field by `D_800A08B8`.
Finally it calls `func_15059C84` with the same state pointer.

A minimal offset-accurate `D13A0State` type records the five independently
updated fields. Writing the independent scale update before the lift-position
update gives IDO the retail floating-register lifetimes and schedule while
preserving the same per-field result. All 28 words emit directly from
semantic C; no expected-word guards are used.

## Verification

- The focused `generated_FE850.c.o` build matches all 28 retail words and all
  expected relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 112-byte spans share SHA-256
  `e81264e9e1921d131d19d246e269c70b250ce8bf241825d6f1d6c3040ab3c090`.
- Fresh matcher totals are `2,936 / 5,465 (53.72%)` overall and
  `2,362 / 4,789 (49.32%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 29-word `func_150ECB8C`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
