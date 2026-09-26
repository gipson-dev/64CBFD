# Game position and phase update match - 2026-09-26

## Result

All 28 words of `func_15141564` now match retail across
`0x15141564..0x151415D4`. The linked matcher reports `2596 / 5484 (47.34%)`
overall and `2028 / 4795 (42.29%)` game, with one address-drift blocker and
2,887 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine computes an output position from the `arg0 + 0x170` base value,
amplitude, and sine of the angle at `arg0 + 0x178`. It then advances the phase
at base offset eight by the offset-`0xC` rate scaled by `D_800BE9A4`, normalizes
that phase through `func_15144B68`, stores the result, and returns one.

Writing the position expression in multiplication-first order recovers nine of
the original eleven differing words directly from C. IDO emits retail's
`0x28` frame and incoming-argument slot, loads the amplitude into `f6` and the
base value into `f4`, forms the product in `f8`, and also recovers the complete
`f4`/`f6` phase-update pipeline and final stack restore. The only residual
compiler choice is whether the `arg0 + 0x170` base pointer is preserved at
`sp+0x1C` or retail's `sp+0x18`; two expected-word guards normalize that
spill/reload pair. No relocation or instruction position changes.

The complete dependency-driven non-matching rebuild and project tool checks
passed. The linked span at `conker/build/conker.us.bin+0x16E9E4` and pristine
retail span at `conker/conker.us.bin+0x16EA14` both have SHA-256
`364192b03df56b95681c27fb0a27b22cdeacb071d6a9a462c1b4a07bcb72364b`.
The patch table contains 711 rows with zero duplicate keys and two rows for
this function.

The `64CBFDOGL` sibling exposes this function only through generated symbol
metadata. It has no hand-maintained host body requiring a transplant. Its
1,659 existing dirty entries were left untouched, and frozen Release was not
built, modified, or launched.

## Next boundary

Continue with 15-word `func_15178E14`, now the first game row with eleven real
differences. Compare its K&R `u8` argument normalization, frame, incoming
argument spill, nested `func_15178B98`/`func_15178DA4` calls, delay slots, and
call relocations before editing.
