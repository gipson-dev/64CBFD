# Game two-command record updater byte match

Date: 2026-09-29

## Scope

This pass completed `func_15109064` in
`conker/src/game/generated_135D00.c`. The retail slot spans 30 words and 120
bytes at `0x15109064..0x151090D8`.

## Recovered behavior

The routine locates the same owner-relative record used by the surrounding
slice: owner field `0x50` supplies a signed offset and the fixed record base is
another `0xF8` bytes forward. A byte command selects one of two updates.

Command `0x1D` copies two words and one byte from the caller's nine-byte
payload into record offsets `0x14`, `0x1C`, and `0x18`, respectively. Command
`0x1E` toggles the record byte at offset `0x20` between zero and one. Every
other command returns without modifying the record.

Expressing the dispatch as a `switch`, and spelling the toggle as a nonzero
test followed by explicit zero/one stores, lets IDO emit 26 of the 30 retail
words directly, including both branch-likely paths. Four guarded
normalizations preserve one commutative owner-plus-offset add, retarget the
second command branch across retail's extra delay-slot word, and move the last
payload store before an explicit copy-path return and inserted `nop`.

## Verification

- The focused `generated_135D00.c.o` build matches all 30 retail words; the
  routine has no relocations.
- The shared patch-table change triggered a complete serial object rebuild;
  `wsl make -C conker NON_MATCHING=1 -j1` completed successfully.
- The linked ELF and retail 120-byte spans share SHA-256
  `8072d145681a82314d4e37392823be0e48170fbc1897c198e8d46dd415a6e6f3`.
- Fresh matcher totals are `2,942 / 5,465 (53.83%)` overall and
  `2,368 / 4,789 (49.45%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_151149AC`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
