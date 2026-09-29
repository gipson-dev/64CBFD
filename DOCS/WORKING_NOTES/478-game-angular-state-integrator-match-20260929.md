# Game angular state integrator byte match

Date: 2026-09-29

## Scope and behavior

`func_150AFBF4` in `conker/src/game/generated_DC6B0.c` spans 29 words and
116 bytes at `0x150AFBF4..0x150AFC68`. It advances float field `0x78` by
field `0x7C` times the global timestep `D_800BE9A4`, normalizes the result
through `func_15144B68`, and passes that angle to the existing `sinf` routine
at `0x15047D60`. The sine is scaled by field `0x74`, offset by field `0x70`,
and stored at `0x10`. The routine returns one.

## Compiler shape

The four floats at `0x70..0x7C` are represented as an embedded typed block.
A reassigned scratch parameter expresses retail's derived-pointer lifetime
across the `sinf` call and recovers the complete arithmetic, call order,
32-byte frame, floating-register allocation, and return schedule.

Twenty-six words emit directly from semantic C. Three expected-word guards
remove IDO's unused incoming scratch-parameter home and move the corresponding
derived-pointer spill and reload from `sp+0x1C` to retail's `sp+0x18` slot.
The guards do not alter behavior, call targets, arithmetic, or field access.

## Verification

- The focused generated-slice object builds with the complete 29-word retail
  instruction sequence after the three guarded scheduling normalizations.
- The complete ELF relink passes.
- Direct comparison passes all 116 linked bytes. Both spans share SHA-256
  `72132aa45284c9b660a8e383d7676ed19df6d95609f2cd27d5eb49be8defcfb2`.
- The authoritative matcher reports `2,981 / 5,465 (54.55%)` overall and
  `2,406 / 4,789 (50.24%)` in Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Preserve the existing
parks for unresolved jump-table ownership, handwritten live-register
fragments, and the documented low-difference compiler-scheduling cases.
