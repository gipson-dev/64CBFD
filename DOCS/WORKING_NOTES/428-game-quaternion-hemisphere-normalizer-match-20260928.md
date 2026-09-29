# Game quaternion hemisphere normalizer byte match

Date: 2026-09-28

## Scope

This pass completed `func_15049C40` in
`conker/src/game/generated_770F0.c`. The retail slot spans 30 words and 120
bytes at `0x15049C40..0x15049CB4`.

## Recovered behavior

The routine computes the four-component dot product of two float vectors used
as quaternions. When the dot product is negative, it negates all four
components of the second quaternion in place. This selects the equivalent
quaternion representation in the same hemisphere as the first, allowing the
following interpolation or matrix setup to take the shorter orientation path.

The typed pointer body preserves retail's component-load order, floating-point
accumulation tree, comparison, branch shape, and four stores. IDO emits the
complete retail schedule directly from semantic C. No expected-word guards or
compiler-profile override are required.

## Verification

- The focused `generated_770F0.c.o` build passed under the existing
  `-O2 -g3` profile; all 30 words match retail directly from C.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- `match_progress.py` classifies `func_15049C40` as byte-exact.
- The linked ELF and retail 120-byte spans share SHA-256
  `72c4d1b7cee3dc8bf2561bc11b2cb4068a34014c26038ac1ebf6060fbc9f2951`.
- Fresh matcher totals are `2,930 / 5,466 (53.60%)` overall and
  `2,356 / 4,790 (49.19%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 38-word `func_1506D6B4`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
