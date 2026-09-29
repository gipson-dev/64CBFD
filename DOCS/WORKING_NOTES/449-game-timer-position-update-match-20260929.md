# Game timer and position updater byte match

Date: 2026-09-29

## Scope

This pass completed `func_15174920` in
`conker/src/game/generated_1A1B40.c`. The tracked retail slot spans 32 words
and 128 bytes at `0x15174920..0x151749A0`; the semantic routine occupies 29
words and is followed by three retail padding words.

## Recovered behavior

The routine reads the remaining byte at owner offset `0x3F` and caps values
above 200. It subtracts the unsigned product of `D_800BE9E4` and the owner word
at offset `0x18`. A negative result clears the halfword at offset `0x38` and
returns.

For a nonnegative result, the signed motion word at offset `0x14` is added to
the halfword at offset `0x34`. Its value shifted left by three and divided by
seven is added to the halfword at offset `0x36`, and the remaining timer is
written back to byte `0x3F`.

The direct C body reproduces retail's byte cap, unsigned multiply, signed
subtraction, branch-likely expiry path, duplicated motion load, constant
division, store order, and return. All 32 tracked words and the `R_MIPS_HI16`
and `R_MIPS_LO16` relocations for `D_800BE9E4` match without expected-word
guards.

## Verification

- The focused `generated_1A1B40.c.o` build matches all 32 tracked retail words
  and retains both relocations for `D_800BE9E4`.
- The incremental `wsl make -C conker NON_MATCHING=1 -j1` relink refreshed the
  ELF and binary successfully.
- The linked ELF and retail 128-byte spans share SHA-256
  `0db30d81a7b896df6df0ca76299e033339c2e26e5c5968b95a95105e84a194d6`.
- Fresh matcher totals are `2,950 / 5,465 (53.98%)` overall and
  `2,376 / 4,789 (49.61%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 61-word `func_15145548`, currently at
27 real differences. Its existing semantic body calls `func_1514563C` with an
optional scalar output, clamps a negative projection to the first input
vector, clamps a projection above one to the first vector plus the direction
vector, and copies the first input when projection fails. Focus on retail's
`0x28` frame, stack argument/local substitution, branch-likely bounds, and
three-word vector-copy paths. Keep 29-word `func_15194320` and
`func_15194394` parked behind generated-slice jump-table and rodata ownership.
Also keep `func_151F3D78` parked behind audio-object layout drift, the tied
Init SDK cache routines in their ownership lane, and address-drift row
`func_10012588` parked.
