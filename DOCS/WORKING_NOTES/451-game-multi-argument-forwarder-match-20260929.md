# Game multi-argument forwarder byte match

Date: 2026-09-29

## Scope

This pass completed `func_1503F5B8` in
`conker/src/game/generated_6C960.c`. The tracked retail slot spans 29 words
and 116 bytes at `0x1503F5B8..0x1503F62C`.

## Recovered behavior

The wrapper accepts an object pointer, two word arguments, two floating-point
arguments, and a final stack word. It calls `func_1505E0C4` with twelve
arguments: two leading zero selectors, the object, another zero selector, the
two word arguments, the object's unsigned byte at offset `0x3F5`, both caller
floats, two zero floats, and the final word. Its return value is passed through
unchanged.

Giving both functions complete prototypes is essential. It prevents the
caller floats from undergoing default argument promotion and lets IDO recover
retail's `f12` and stack-float ABI. The direct return expression then emits the
retail `0x38` frame, incoming argument spills, stack argument stores, byte
load, call delay slot, and return sequence without expected-word guards.

## Verification

- The focused `generated_6C960.c.o` comparison matches all 29 retail words and
  the `R_MIPS_26` relocation for `func_1505E0C4`.
- `wsl make -C conker NON_MATCHING=1 -j1` relinked the ELF and binary
  successfully.
- The linked ELF and retail 116-byte spans share SHA-256
  `6398afee78289df1a106eeb809f135089e0481c1fcaa07602fb253bf3c7bea8a`.
- Fresh matcher totals are `2,952 / 5,465 (54.02%)` overall and
  `2,378 / 4,789 (49.66%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 28-word `func_1507C370`,
currently at 28 real differences. It is a zero-return placeholder in
`conker/src/game/generated_A9260.c`; recover its semantics from the retail
`A9260` assembly slice before attempting compiler normalization. Keep
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership, `func_151F3D78` parked behind audio-object layout drift,
the tied Init SDK cache routines in their ownership lane, and
`func_10012588` parked on address drift.
