# Game partial-zero payload allocator byte match

Date: 2026-09-28

## Scope

This pass completed `func_1514DA38` in
`conker/src/game/generated_179F30.c`. The retail slot spans 27 words and 108
bytes.

## Recovered behavior

The routine prepares a 28-byte local payload, requests a same-sized record
from `func_15158BD0` with mode `1`, and returns without further work when the
allocation fails. On success it copies the local payload into offset `0x58` of
the returned record and submits that record with the original object and type
`0x13` through `func_1514EC1C`.

Retail zeroes payload words 5, 6, and 0 through 3, but deliberately leaves
word 4 untouched. The recovered C preserves that partial initialization rather
than replacing it with a fully zeroed aggregate. Declaring the saved result
before the seven-word payload makes IDO place the payload at `sp+0x18` and the
result at `sp+0x34`, reproducing retail's complete stack map and store order.
All 27 words emit directly from semantic C. No expected-word guards or
compiler-profile changes are required.

## Verification

- The focused `generated_179F30.c.o` build passed under the existing
  `-O2 -g3` profile; its warnings are pre-existing neighboring pointer/integer
  prototype warnings.
- Focused object disassembly matches all 27 retail instruction words and all
  three call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_1514DA38` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `c742e2358884d79f9ae480d50e5725e72b6e7e7c5afe4ca285c9249045270546`.
- Fresh matcher totals are `2,918 / 5,466 (53.38%)` overall and
  `2,344 / 4,790 (48.94%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 34-word `func_15159230`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
