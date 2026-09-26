# Game interpolation register match - 2026-09-26

## Result

All 58 words of `func_15074A94` now match retail across
`0x15074A94..0x15074B7C`. The linked matcher reports `2592 / 5484 (47.26%)`
overall and `2024 / 4795 (42.21%)` game, with one address-drift blocker and
2,891 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine measures distance from `D_800CC2D0`, updates the current object's
lower bound when needed, selects or interpolates a float value, chains that
value through fields `0x158` and `0x154`, and writes the terminal constant to
field `0x15C`.

The frame, call and relocation, global loads, comparisons, branches, chained
field stores, and epilogue already matched. The interpolation was rewritten as
one factor-times-distance expression with explicit numerator and floor
lifetimes. Eleven guarded words then normalize the remaining independent
floating-point register choices. The guards preserve the existing relocations
for `D_8009A0F4`, `D_8009A0F8`, and `D_8009A0FC`; no words or relocations move.

While validating the guards, the hand-maintained padded-object rules were
found to consume `retail_word_patches.us.csv` without declaring it as a Make
prerequisite. Both `RETAIL_PAD_GLOBAL_ASM_O_FILES` and
`RETAIL_PAD_PLAIN_O_FILES` now declare that dependency. A table change therefore
invalidates every object that consumes it instead of permitting a stale object.

The complete dependency-driven rebuild and project tool checks passed. The
linked span at `conker/build/conker.us.bin+0xA1F14` and pristine retail span at
`conker/conker.us.bin+0xA1F44` both have SHA-256
`4b85cc9681ac9d582b3f068553382b892a04d8c7201c789e79347a5ba4cbfc86`.
The patch table has 700 rows with zero duplicate keys.

The `64CBFDOGL` sibling exposes this function only through generated dispatch,
declaration, and symbol-table artifacts. It has no hand-maintained host body
requiring a transplant. Its existing dirty work was left untouched, and frozen
Release was not built, modified, or launched.

## Next boundary

Continue with 15-word `func_1507EEB8`, now the first game row with eleven real
differences. Compare its source model, compact object, retail words, and
relocations before editing.
