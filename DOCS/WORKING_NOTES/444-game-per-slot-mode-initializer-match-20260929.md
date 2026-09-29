# Game per-slot mode initializer byte match

Date: 2026-09-29

## Scope

This pass completed `func_15181D00` in
`conker/src/game/generated_1AC2F0.c`. The retail slot spans 28 words and 112
bytes at `0x15181D00..0x15181D70`.

## Recovered behavior

The routine accepts a slot index and a mode. Mode zero clears only the indexed
value in `D_800DDDC8`. A nonzero mode clears `D_800DDDD8`, seeds
`D_800DDDC8` from `D_800A72AC`, and clears both floats in the corresponding
`D_800DDDE8` pair. Both paths finish by storing the mode byte in
`D_800DDE1C`.

The full-width `s32` mode parameter is significant even though its final
destination is a byte. It lets retail branch directly on the incoming value
and use the same register for the final `sb`. An initial `u8` signature caused
IDO to emit an entry spill, `andi`, and register move, expanding the body to
31 words. The retail-span guard rejected that object; changing the parameter
to `s32` removed exactly those three words and produced the retail body.

All 28 words and twelve HI/LO relocations emit directly from semantic C. No
expected-word guards are required.

## Verification

- The focused `generated_1AC2F0.c.o` build matches all 28 retail words and all
  twelve data relocations directly from C.
- The incremental full `wsl make -C conker NON_MATCHING=1 -j1` rebuild and
  relink completed successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `90db6f25d42c5e2c18435daace07fbcdebc254eb75f8fd653e55d38191e757f9`.
- Fresh matcher totals are `2,945 / 5,465 (53.89%)` overall and
  `2,371 / 4,789 (49.51%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_1518AB60`, currently at
27 real differences. It is an allocator wrapper that initializes a command
`0x1E` record. Keep the documented lower-difference compiler cases parked.
Also keep `func_151F3D78` parked behind the pre-existing audio-object layout
drift, keep the tied Init SDK cache routines in their ownership lane, and keep
address-drift row `func_10012588` parked.
