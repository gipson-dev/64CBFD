# Game callback-gated record-state update byte match

Date: 2026-09-28

## Scope

This pass completed `func_150D0034` in
`conker/src/game/generated_FC5F0.c`. The retail slot spans 35 words and 140
bytes at `0x150D0034..0x150D00BC`.

## Recovered behavior

The routine examines the signed callback selector at record offset `0x4C`.
A selector of `-1` bypasses callback dispatch. Otherwise, it indexes
`D_800888A0` and calls the selected function with the record. A zero callback
result writes `-1` to the halfword at offset `0x0E` and returns the caller's
first pointer immediately. The bypass and successful callback paths both
clear bit zero of the status byte at offset `0x30` before returning that same
pointer.

The selector is modeled as volatile because retail performs two independent
signed-byte reads: one for the sentinel test and another for callback-table
indexing. That type information lets IDO emit retail's branch-likely and
taken delay-slot pointer calculation. Expressing the status update as `&=
~1` preserves the byte result while recovering retail's promoted `0xFFFE`
immediate. All 35 words emit directly from semantic C; no expected-word
guards are used.

## Verification

- The focused `generated_FC5F0.c.o` build matches all 35 retail words and
  both callback-table relocations.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 140-byte spans share SHA-256
  `b7054a84fa9bb16c0971dd8874a53f7a6db60c6d57bad0ef1d65f8dc43239799`.
- Fresh matcher totals are `2,933 / 5,465 (53.67%)` overall and
  `2,359 / 4,789 (49.26%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_150D02B4`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
