# Game accelerated-motion integrator byte match

Date: 2026-09-29

## Scope

This pass completed `func_1515B994` in
`conker/src/game/generated_188440.c`. Its tracked retail slot spans 31 words
and 124 bytes at `0x1515B994..0x1515BA10`.

## Recovered behavior

The former zero-return placeholder now reads an object's old velocity from
offset `0x78`, acceleration from `0x74`, and the global timestep
`D_800BE9A4`. It advances the value at `0x14` by
`velocity * timestep + 0.5f * acceleration * timestep`, then stores the new
velocity as `velocity + acceleration * timestep`.

The routine next adds the old and new velocities, scales that sum by the
object value at `0x80` and `0.5f`, and accumulates the result at offset
`0x1C`. It returns one.

An initial direct expression produced the correct 31-word extent with 19
compiler-only differences. Retaining the old velocity, acceleration,
timestep, and velocity sum as explicit semantic lifetimes reduced that to 14.
A more explicit position/scale/accumulator experiment introduced a stack
frame and expanded to 35 words, so it was rejected and removed.

Fourteen fail-closed expected-word guards preserve retail's equivalent
floating-point register choices and independent load/store schedule. They do
not replace the recovered arithmetic, branches, constants, or return value.

## Verification

- The focused generated object reproduces all 31 retail instructions after
  guarded normalization.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt every padded object and
  linked the complete ELF and binary successfully.
- Direct linked-span comparison passes all 124 bytes. The linked and pristine
  retail spans share SHA-256
  `f22fcf8d8bea13e9b9dd8fb27fdbba4edc7b3382187883b96a8b59006e502b09`.
- Fresh matcher totals are `2,964 / 5,465 (54.24%)` overall and
  `2,390 / 4,789 (49.91%)` in Game, with one address-drift row.

## Resume boundary

Resume ordinary Game matching with 29-word `func_1518E308`, at 28 real
differences. Keep the lower-difference compiler-scheduling cases and the
generated-slice jump-table/rodata cases at their documented parked boundaries.
Keep the tied Init SDK cache routines in their ownership lane and
`func_10012588` parked on address drift.
