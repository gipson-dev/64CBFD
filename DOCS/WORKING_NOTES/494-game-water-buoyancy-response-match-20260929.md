# Game water-buoyancy response byte match

Date: 2026-09-29

## Scope and behavior

`func_15058F24` in `conker/src/game_83300.c` occupies 135 words and 540 bytes
at `0x15058F24..0x15059140`. It derives a blend value and its complement,
reads the water surface from actor field `unk118 + 9.0f`, and handles initial
water entry, buoyancy correction, the near-surface settle case, separate
rising and sinking damping, and terminal downward velocity.

Retail preserves the original second float argument before conditionally
subtracting `0.5f` from the working blend. The initial `y_velocity` scale uses
that preserved value. The previous C body used the modified blend instead;
assigning the incoming value to `temp_f12` before the split restores the
retail behavior while leaving the later complement and branch logic intact.

## Compiler shape

The corrected `-O2 -g3` body emits the exact 135-word retail extent. Its
control flow, arithmetic, field accesses, constants, and branch targets are
present without inserted or omitted instructions. IDO leaves six independent
opening schedule/debug-home differences, five integer temporary-register
choices, and nineteen floating-point temporary-register choices.

Thirty stale-checked guards normalize those compiler artifacts. None carries
a relocation, changes control flow, or substitutes behavior. The opening
guards also restore retail's branch-likely surface-load schedule after the
blend-complement calculation.

## Verification

- The focused `game_83300` object rebuild accepts all thirty new stale checks.
- A complete guarded-object rebuild and ELF relink pass.
- The authoritative matcher reports `2,998 / 5,463 (54.88%)` overall and
  `2,421 / 4,789 (50.55%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 540 bytes.
- Both spans share SHA-256
  `cc8850f8e8a135673446e62d2e2970372482b610029b53414e54706f610376d4`.
- Project tool checks and all 10 tool unit tests pass.

## Resume boundary

Continue with the next ordinary small C candidate from the authoritative
matcher queue. Keep `func_15015F40` parked behind its unresolved indirect-table
ownership and keep handwritten `func_150A76F0` in the assembly lane.
