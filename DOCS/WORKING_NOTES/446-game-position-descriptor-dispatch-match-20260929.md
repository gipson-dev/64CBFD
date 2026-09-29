# Game position-descriptor dispatch byte match

Date: 2026-09-29

## Scope

This pass completed `func_151C9AC0` in
`conker/src/game/generated_1F4650.c`. The retail slot spans 28 words and 112
bytes at `0x151C9AC0..0x151C9B30`.

## Recovered behavior

The routine accepts an owner pointer, selector byte, and final word. It builds
a three-float source position from the owner's X coordinate at offset `0x14`,
Y reference at offset `0x180` plus `2.0f`, and Z coordinate at offset `0x1C`.
It asks `func_1504715C` to generate the owner's 36-byte descriptor, then calls
`func_151ABE40` with the source position, generated descriptor, fixed mode `2`,
selector, and final word.

The first semantic body produced the exact retail frame, instruction order,
register allocation, and call relocations, but IDO assigned the two locals in
the opposite stack regions. Declaring the 12-byte position before the 36-byte
descriptor gives retail's descriptor at stack offset `0x20` and position at
offset `0x44`. With that declaration order, all 28 words and both call
relocations emit directly from C. No expected-word guards are required.

## Verification

- The focused `generated_1F4650.c.o` build matches all 28 retail words and
  retains `R_MIPS_26` relocations for `func_1504715C` and `func_151ABE40`.
- The incremental `wsl make -C conker NON_MATCHING=1 -j1` relink refreshed
  both the ELF and binary successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `2d6f3976e971d57fc7ab110f7482f6cfff0424a126dd67d0445621e88aeff3fe`.
- Fresh matcher totals are `2,947 / 5,465 (53.92%)` overall and
  `2,373 / 4,789 (49.55%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_151BFB2C`, currently at
27 real differences. Its existing semantic body releases a primary pointer at
offset `0x28` and two indexed pointers at offsets `0x2C` and `0x30`; recover
retail's byte-canonicalized two-entry loop and retained base pointer. Keep
29-word `func_15194320` and `func_15194394` parked: their retail bodies use
embedded jump tables, while C switches in generated slices currently produce
unowned `.rodata` and unresolved links. Also keep `func_151F3D78` parked behind
the existing audio-object layout drift, keep the tied Init SDK cache routines
in their ownership lane, and keep address-drift row `func_10012588` parked.
