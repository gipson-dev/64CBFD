# Game handwritten floating PRNG restoration - 2026-09-27

## Result

`func_150ADA68` is restored from its maintained behavioral C equivalent to the
original handwritten assembly across the complete 25-word, 100-byte extent
`0x150ADA68..0x150ADACC`. This is an ownership correction, not a new exact-C
match: the exact numerator remains 2,853 while the C denominator decreases by
one.

Fresh conversion accounting is 5,468 / 6,041 C functions and
1,931,476 / 2,256,728 C bytes overall. Game is 4,790 / 5,321 functions and
1,763,236 / 2,072,880 bytes. The linked matcher reports
2,853 / 5,468 (52.18%) overall and 2,281 / 4,790 (47.62%) in Game.

## Recovered behavior

The routine advances the 64-bit seed at `D_800885B0` with the same compact
xorshift-style transform as adjacent `func_150ADA20`. It stores the new seed,
extracts the low 16 bits as a nonnegative integer, converts that value to
single precision, and multiplies it by `D_8009F740` to return a scaled random
floating-point value.

The verified behavioral C remains under `#if 0` beside the active
`GLOBAL_ASM`, preserving its readable semantics without misclassifying the
retail routine as compiler-generated C.

## Ownership evidence

The first 15 retail instructions are identical to the corresponding seed
transform and store in handwritten `func_150ADA20`, including direct assembler
`ld`/`sd` symbol expansions, strict source-order shifts, and compact
`a0`/`a1`/`a2` reuse. Retail then uses `v0`, `f2`, and `f4` for the conversion
and leaves the return delay slot empty.

IDO compiles the equivalent C to 26 words, one word beyond the 25-word retail
slot. It retains the seed address in `a0`, spreads the transform across `v1`
and `t0..t9`, schedules the floating constant load before conversion, and adds
an extra nop before the return. The padding tool therefore placed it in
`.game_overflow` behind a trampoline. Combined with both adjacent routines'
proven assembly ownership, this establishes the retail body as handwritten.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0xDAEE8` and pristine retail span at
`conker.us.bin+0xDAF18` compare equal for all 100 bytes. Both have SHA-256:

`65a5f1c67d8297c015c78583648d7a7e45bff89f98a13fe724ff0bdffe3ebe46`

The focused object build, complete relink, fresh progress generation, direct
linked matcher, and exact span comparison pass. The broader replacement and
outer-ROM builds, project-tool checks, all nine unit tests, and the whitespace
check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler cases parked. Classify 65-word Game
`func_1514563C`, the first unparked Game row in the fresh linked queue with 24
real differences, before changing its implementation.
