# Game handwritten two-block word transform restoration

Date: 2026-09-28

## Scope

This pass restored `func_150B1DB0` in
`conker/src/game/generated_DF260.c` to original handwritten assembly
ownership. The retail slot spans 28 words and 112 bytes at
`0x150B1DB0..0x150B1E1C`.

## Ownership evidence

The preserved retail source explicitly marks this routine as handwritten. It
uses MIPS III 64-bit loads, stores, and shifts over two adjacent words,
followed by deliberate trapping `addi` instructions for both the source
pointer and the uncached alias maintained in the loop delay slot. These are
authored instruction choices rather than an IDO-generated schedule.

Each iteration masks a 64-bit word with `D_8009F8D8`, masks a second copy with
`D_8009F8D0`, shifts the latter both left and right by five bits, merges the
three pieces, and stores the result. It performs that transform at offsets
zero and eight, then advances through the caller's half-open range by 16
bytes. The false zero-return C model is therefore replaced with tracked
`GLOBAL_ASM`, not a synthetic semantic C approximation.

## Verification

- The focused `generated_DF260.c.o` build contains all 28 retail words and
  all six expected HI/LO relocation records across the three symbols.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- The linked ELF and retail 112-byte spans share SHA-256
  `dec18e02cec836269f4ceff6550b667ceaaaf0c2fbb06db63767cc62065ffcf2`.
- The C-only matcher correctly removes the function from its denominator:
  totals are `2,932 / 5,465 (53.65%)` overall and
  `2,358 / 4,789 (49.24%)` in Game, with one address-drift row.
- The complete inventory is now 5,465 C functions plus 576 assembly functions
  across 6,041 rows. The Game inventory is 4,789 C plus 532 assembly across
  5,321 rows.

## Resume boundary

Resume the ordinary unparked queue with 35-word `func_150D0034`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
