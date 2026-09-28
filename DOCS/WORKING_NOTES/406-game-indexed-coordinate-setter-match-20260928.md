# Game indexed coordinate setter byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150A3444` in
`conker/src/game/generated_CDE80.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function accepts a record index and three signed 16-bit coordinates. It
indexes the dynamically allocated table referenced by `D_800D3098`, whose
records are 52 bytes each, and stores the coordinates at offsets zero, two,
and four.

Typing the three coordinate parameters as `s16` reproduces retail's incoming
argument spills and ordered sign extensions. Keeping the writes as three
direct member assignments retains the repeated loads of the global table
pointer between stores, preserving the compiler's alias assumptions. The
complete routine emits directly from semantic C with no expected-word guards
or compiler-profile changes.

## Verification

- The focused `generated_CDE80.c.o` build passed under the existing `-O2 -g3`
  profile.
- Focused object disassembly matches all 27 retail instruction words and both
  `D_800D3098` relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150A3444` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `ddbe910de039f583be412b8888b86891c0a3358c0585d2df05c2c3eccb302182`.
- Fresh matcher totals are `2,908 / 5,466 (53.20%)` overall and
  `2,334 / 4,790 (48.73%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_150B71A8`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
