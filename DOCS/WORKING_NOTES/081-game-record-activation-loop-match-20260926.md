# Game record activation loop match - 2026-09-26

## Result

All 17 words of `func_150B6D34` now match retail across
`0x150B6D34..0x150B6D78`. The linked matcher reports `2594 / 5484 (47.30%)`
overall and `2026 / 4795 (42.25%)` game, with one address-drift blocker and
2,889 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine walks the three four-byte entries from `D_800D9898` through
`D_800D98A4`. Each non-null pointer at entry offset `0x14` receives the active
value `1` at offset `0x20`, after which `D_800D9890` is set to `3`.

Removing the explicit end-pointer and value locals lets IDO recover retail's
`a1` end pointer and `a0` active value directly, reducing the original eleven
real differences to nine. Nine guarded words then normalize the compiler's
remaining `v0`/`v1` cursor and record-pointer allocation. The three guarded
address-setup words declare both expected and replacement relocations for
`D_800D9898` and `D_800D98A4`; the other six rows change registers only. No
word is inserted and the 68-byte extent is unchanged.

The complete dependency-driven non-matching rebuild and project tool checks
passed. The linked span at `conker/build/conker.us.bin+0xE41B4` and pristine
retail span at `conker/conker.us.bin+0xE41E4` both have SHA-256
`03ce6560ee0992ce0939368415ac8387c68e5cac8aa8022d68bc01deea2f1124`.
The patch table contains 709 rows with zero duplicate keys and nine rows for
this function.

The `64CBFDOGL` sibling exposes this function only through generated symbol
metadata. It has no hand-maintained host body requiring a transplant. Its
1,659 existing dirty entries were left untouched, and frozen Release was not
built, modified, or launched.

## Next boundary

Continue with 17-word `func_151090DC`, now the first game row with eleven real
differences. Compare its two-word stack aggregate, compact-object copy
schedule, call relocations, and retail words before editing.
