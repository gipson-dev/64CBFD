# Game local-record pointer schedule match - 2026-09-26

## Result

All 20 words of `func_150717E0` now match retail across
`0x150717E0..0x15071830`. The linked matcher reports `2591 / 5484 (47.25%)`
overall and `2023 / 4795 (42.19%)` game, with one address-drift blocker and
2,892 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The existing C already models the routine correctly: allocate object type
`0x12`, construct an eight-byte local record containing the object pointer and
its unique identifier, then forward that record to `func_15131D4C` and
`func_151494E0` with tag `0x43`.

Retail forms the local-record address once in `a0`, saves it at `sp+0x18`
across the first call, and reloads it for the second call. IDO instead
rematerializes `sp+0x20`, producing the same behavior with an eleven-word
schedule difference. Eleven guarded rows restore retail's branch displacement,
pointer spill/reload, both call positions and relocations, delay slots, and
epilogue position. No word is inserted and the 80-byte extent is unchanged.

The complete non-matching rebuild and project tool checks passed. The linked
span at `conker/build/conker.us.bin+0x9EC60` and pristine retail span at
`conker/conker.us.bin+0x9EC90` both have SHA-256
`6cb1079ed02c68652e32fb90cad0f0e18cc65a1ed4deec89e7af75b236fe2d7a`.
The patch table has 689 rows with zero duplicate keys.

The `64CBFDOGL` sibling exposes this guest routine through generated/reference
artifacts and has no hand-maintained host implementation requiring a
transplant. Its existing dirty work was left untouched, and frozen Release was
not built, modified, or launched.

## Next boundary

Continue with 58-word `func_15074A94`, now the first game row with eleven real
differences. Compare its source, compact object, retail words, control flow,
and relocations before editing.
