# Game mode-gated table-value updater byte match

Date: 2026-09-29

## Scope

This pass completed `func_15108BC0` in
`conker/src/game/generated_135D00.c`. The retail slot spans 30 words and 120
bytes at `0x15108BC0..0x15108C34`.

## Recovered behavior

The routine locates a record at the caller's signed offset from owner field
`0x50`, then reads the record index at effective owner-relative offset
`0x10C`. Index `0x3E7` writes the fallback value `226.0f` to record offset
`0x10`. Otherwise, global mode byte `D_800C35EA` selects between the same
fallback and a floating value at offset `4` in index-sized `0x44`-byte rows
under the table pointer `D_800C3958`.

The semantic C emits 19 retail words directly. Eleven guarded normalizations
preserve one commutative address-add order, move the independent table-pointer
load ahead of the mode branch with relocation ownership intact, retain
retail's `t8`/`t9`/`a0` table-address lifetimes, and insert the explicit `nop`
after the table path's return. The guarded insertion restores the compiler's
29-word form to the original 30-word slot without changing the C behavior.

## Verification

- The focused `generated_135D00.c.o` build matches all 30 retail words and
  all four data relocations after the eleven guarded normalizations.
- The shared patch-table change triggered a complete serial object rebuild;
  `wsl make -C conker NON_MATCHING=1 -j1` completed successfully.
- The linked ELF and retail 120-byte spans share SHA-256
  `87330ef5ce608175b955cbf82685645a8fc86b7a62ac1ca2c510672233bd943e`.
- Fresh matcher totals are `2,941 / 5,465 (53.82%)` overall and
  `2,367 / 4,789 (49.43%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_15109064`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
