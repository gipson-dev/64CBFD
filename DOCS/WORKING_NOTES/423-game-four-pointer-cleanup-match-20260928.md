# Game four-pointer cleanup byte match

Date: 2026-09-28

## Scope

This pass completed `func_151B222C` in
`conker/src/game/generated_1DF510.c`. The retail slot spans 28 words and 112
bytes at `0x151B222C..0x151B2298`.

## Recovered behavior

The routine retains `arg0 + 0x28` as a base and walks the three pointer fields
at base offsets `0x10`, `0x14`, and `0x18`, corresponding to object offsets
`0x38..0x40`. Each non-null pointer is passed to `func_1516972C`. After that
loop, the independent pointer at base offset `0x1C`, or object offset `0x44`,
is also released when non-null.

The retail loop keeps its counter in `s0`, uses `s1` for the retained base,
and narrows the incremented counter to eight bits before the `< 3` test. An
`s32` C counter with the explicit `i = (u8)(i + 1)` assignment reproduces that
shape. A directly declared `u8` counter makes IDO introduce a redundant zero
copy before the first iteration and overrun the retail slot by one word. The
accepted form emits all 28 words directly from semantic C; no expected-word
guards or compiler-profile override are needed.

## Verification

- The focused `generated_1DF510.c.o` build passed under the existing
  `-O2 -g3` profile; all 28 words and two call relocations match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_151B222C` as byte-exact.
- The linked ELF and retail 112-byte spans share SHA-256
  `dc75cd68d4c35a41ea0c10f1c33213c1ede085a635f7c5243bff33d6db63c063`.
- Fresh matcher totals are `2,925 / 5,466 (53.51%)` overall and
  `2,351 / 4,790 (49.08%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 29-word `func_151CB49C`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
