# Game gated active-object scan byte match

Date: 2026-09-28

## Scope

This pass completed `func_150347E8` in
`conker/src/game/generated_61490.c`. The retail slot spans 30 words and 120
bytes at `0x150347E8..0x1503485C`, including three trailing padding words.

## Recovered behavior

The routine first checks the global disable byte `D_800BEAC0`. When enabled,
it walks the object table from `D_800CC2D0` to the exclusive end marker
`D_800D121C` in `0x32C`-byte increments. Each record whose words at offsets
`0` and `0x9C` are both nonzero is passed to `func_15034728`; inactive records
are skipped.

A record pointer declared before the gate occupies `s0`. Scoping the end
pointer inside the gated block makes IDO materialize its high half in the
gate branch delay slot and retain it in `s1`, reproducing retail's opening
schedule. The `do` loop and short-circuit condition also emit the original
branch-likely increment slots directly. All 30 words match without
expected-word guards or a compiler-profile override.

## Verification

- The focused `generated_61490.c.o` build passed under the existing
  `-O2 -g3` profile; all 30 words, call relocation, and data relocations match.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_150347E8` as byte-exact.
- The linked ELF and retail 120-byte spans share SHA-256
  `a559ebb0f27b18ffd2c9d3b1c9e7e0a43a4525d56175f4a5ba2269920502ad3b`.
- Fresh matcher totals are `2,928 / 5,466 (53.57%)` overall and
  `2,354 / 4,790 (49.14%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_15045714`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
