# Game global-gated parameter dispatcher byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150C7870` in
`conker/src/game/generated_F4D20.c` with its semantic Game routine. The retail
slot spans 28 words and 112 bytes.

## Recovered behavior

The function first tests bit `0x08` in the byte at offset `0x0A` of the global
record referenced by `D_800D2E4C`. When that gate is set, the function returns
without dispatching. Otherwise it tests bit `0x04` at offset `0x73` of the
state referenced by `D_800DBEF4`. A clear state bit calls `func_1511650C` with
the incoming first argument and `(1, 0x353, 1000.0f)`; a set bit uses
`(1, 0x43, 400.0f)`.

The initial nested semantic source compiled 24 bytes too large because the
callee lacked a prototype and C's default argument promotions converted each
floating argument to `double`. Recovering the fourth parameter as `f32`
restores retail's register-only call convention and 24-byte frame. IDO then
hoists the common arguments and emits the two call paths exactly. All 28 words
emit directly from C with no expected-word guards or profile changes.

## Verification

- The focused `generated_F4D20.c.o` build passed under the existing `-O2 -g3`
  profile.
- Focused object disassembly matches all 28 retail instruction words and both
  `func_1511650C` call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150C7870` as byte-exact.
- The linked and retail 112-byte spans share SHA-256
  `e0afeec217c6d5c40f909dfb7f902188fd3bf85fd14216569996e8ff29e28cad`.
- Fresh matcher totals are `2,912 / 5,466 (53.27%)` overall and
  `2,338 / 4,790 (48.81%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_150D0134`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
