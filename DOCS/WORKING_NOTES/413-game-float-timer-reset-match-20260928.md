# Game float timer reset byte match

Date: 2026-09-28

## Scope

This pass completed `func_150E88C0` in
`conker/src/game/generated_113D60.c`. The retail slot spans 28 words and 112
bytes.

## Recovered behavior

The routine subtracts the global frame delta `D_800BE9A4` from the float timer
at offset `0x28` of its input record. A nonnegative timer returns immediately.
When the timer becomes negative, the routine calls `func_150ADA68`, scales the
random result by `D_800A1378`, adds `201.0f`, stores the new timer, and calls
`func_150E8930` for the same record.

The direct pointer-based C expression reproduces retail's `0x18` frame,
floating-point register allocation, likely-branch layout, saved argument,
random call, reseed arithmetic, delay-slot store, and epilogue. All 28 words
emit directly from semantic C. No expected-word guards or compiler-profile
changes are required.

## Verification

- The focused `generated_113D60.c.o` build passed under the existing
  `-O2 -g3` profile.
- Focused object disassembly matches all 28 retail instruction words and both
  call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150E88C0` as byte-exact.
- The linked and retail 112-byte spans share SHA-256
  `94893d3fec01a0867260d976a9d1cdfd0153235d3a20289e838f3e3cffc7c4e5`.
- Fresh matcher totals are `2,915 / 5,466 (53.33%)` overall and
  `2,341 / 4,790 (48.87%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 29-word `func_15114050`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
