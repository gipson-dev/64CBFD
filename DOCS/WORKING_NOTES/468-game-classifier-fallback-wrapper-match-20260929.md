# Game classifier fallback wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_1504530C` in `conker/src/game/generated_71820.c` spans 30 words and
120 bytes. It dispatches the result of `func_150470B0(arg0, arg1, arg2)`:
result zero calls and returns `func_15044ED0` with the original arguments,
result one returns zero, and result two returns one.

The switch intentionally has no explicit default return. Retail falls through
with the classifier result still in `v0`, so an unrecognized value is preserved.
A named result plus explicit default return was tested, but IDO copied `v0` to
`v1` and expanded the routine to 32 words. The direct switch reproduces all 30
retail words without guards.

## Verification

- The focused padded object reproduces all 30 retail instructions.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `328e786deff2085910be798eef006116221c3ccb28fe5d7418974696df4439f5`.
- The authoritative matcher reports `2,970 / 5,465 (54.35%)` overall and
  `2,396 / 4,789 (50.03%)` in Game, with one address-drift row.

## Resume boundary

Continue with an ordinary small Game placeholder. Keep `func_150AFBF4` parked
at its documented compiler pointer-lifetime boundary.
