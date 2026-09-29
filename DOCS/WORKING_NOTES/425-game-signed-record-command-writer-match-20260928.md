# Game signed record-command writer byte match

Date: 2026-09-28

## Scope

This pass completed `func_15034340` in
`conker/src/game/generated_61490.c`. The retail slot spans 28 words and 112
bytes at `0x15034340..0x150343AC`.

## Recovered behavior

The routine indexes `D_800CC2D0` with a `0x32C`-byte record stride and reads
the signed control byte at record offset `0x1D1`. A zero control byte returns
the original output cursor. A nonzero byte writes signed halfword command `6`
at the cursor, advances the cursor by four bytes, rereads the signed control
byte, scales it by 200, and writes that signed halfword in the command's
second slot before returning the advanced cursor.

The direct array-index expression reproduces retail's shift/add multiplication
by `0x32C`. Keeping the value access in the store expression preserves the
retail routine's deliberate second signed-byte read, while updating the
cursor before that store produces the original `-2` displacement. All 28
words emit directly from semantic C. No expected-word guards or
compiler-profile override are required.

## Verification

- The focused `generated_61490.c.o` build passed under the existing
  `-O2 -g3` profile; all 28 words and both data relocations match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_15034340` as byte-exact.
- The linked ELF and retail 112-byte spans share SHA-256
  `529ddd228334416cf0838ce6bf9a03ff9cb7ec638c76c9ed12e5975534320d47`.
- Fresh matcher totals are `2,927 / 5,466 (53.55%)` overall and
  `2,353 / 4,790 (49.12%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_150347E8`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
