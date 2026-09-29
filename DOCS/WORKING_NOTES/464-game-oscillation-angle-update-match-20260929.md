# Game oscillation and angle updater byte match

Date: 2026-09-29

## Scope and behavior

`func_151B8BE0` in `conker/src/game/generated_1E5FF0.c` spans 29 words and
116 bytes. It writes `sinf(angle) * amplitude + base` to offset `0x44`,
advances the angle at `0x58` by angular velocity times `D_800BE9A4`,
normalizes that angle through `func_15144B68`, and forwards the object and
second argument to `func_151D9450`.

Adding the correct `f32 func_15144B68(f32)` declaration removed three false
integer/varargs conversion words. Twenty-two words then emitted directly from
C. Seven fail-closed guards preserve one closed, equivalent floating-point
temporary allocation cycle around the two arithmetic expressions.

## Verification

- The focused padded object reproduces all 29 retail instructions.
- The shared guard table passed a complete single-job rebuild and relink.
- Direct comparison passes all 116 linked bytes with SHA-256
  `a78173b8ca18bd598d1836c8e2a37e2cbcc47ad86fe5af291d52c8795aa9afae`.
- Fresh totals are `2,966 / 5,465 (54.27%)` overall and
  `2,392 / 4,789 (49.95%)` in Game, with one address-drift row.

## Resume boundary

Rerun the fresh matcher list and continue the next ordinary Game row after
the previously documented compiler, SDK, and generated-rodata parked cases.
