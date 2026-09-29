# Game record-mediated dispatch byte match

Date: 2026-09-28

## Scope

This pass completed `func_15173C90` in
`conker/src/game/generated_1A0E60.c`. The retail slot spans 28 words and 112
bytes at `0x15173C90..0x15173CFC`, including the trailing alignment word.

## Recovered behavior

The routine passes the low byte of its third, full-width argument to
`func_151149AC`. A null lookup result returns immediately. For a valid record,
it reads the unsigned halfword at offset `0x54`, clears bit `0x8000`, derives
the record index as `(record - D_800DBEF4) / 0xA0`, and calls
`func_151739B0(masked_flags, 1, arg0, arg1, index)`.

Keeping the third formal as `s32` is part of the recovered ABI: declaring it
as `u8` makes IDO insert prologue canonicalization and overrun the retail
slot. The `u8` prototype on `func_151149AC` instead emits retail's `andi` in
the call delay slot. The semantic body emits 26 of 28 words directly. Two
expected-word guards only exchange the independent masked-flag move and stack
store for the table index at offsets `0x44` and `0x48`; neither guard carries
a relocation or changes data flow.

## Verification

- The focused `generated_1A0E60.c.o` build passed under the existing
  `-O2 -g3` profile; all 28 words, including the trailing alignment word,
  match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_15173C90` as byte-exact.
- The linked ELF and retail 112-byte spans share SHA-256
  `87de100270dfcecc257f5181f12efce8f30d295ee468b3eb7adc258d79683bc0`.
- Fresh matcher totals are `2,921 / 5,466 (53.44%)` overall and
  `2,347 / 4,790 (49.00%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15178DA4`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
