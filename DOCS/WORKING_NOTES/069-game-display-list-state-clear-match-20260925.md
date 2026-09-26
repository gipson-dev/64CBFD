# Game display-list state clear match - 2026-09-25

## Result

All 12 words of `func_15094F40` now match retail across
`0x15094F40..0x15094F70`. The linked matcher reports `2582 / 5484 (47.08%)`
overall and `2014 / 4795 (42.00%)` game, with one address-drift blocker and
2,901 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function emits display-list command `0xDE000000` with target
`D_800873D0`, advances the cursor by eight bytes, clears `D_800D2CA0`, and
returns the advanced cursor. Its source already expresses that behavior.
IDO folds the original cursor into `a0`, computes the return directly in
`v0`, and emits ten meaningful words instead of retail's twelve.

Nine expected-word guards apply the established generated-slice cursor
expansion. They preserve the original cursor in `v1`, move the target-address
and global-clear relocations to their retail instructions, store through
`v1`, advance `a0`, and insert the advanced-cursor copy and final delay-slot
word. All four `R_MIPS_HI16`/`R_MIPS_LO16` relocations remain explicit.

The generated object and complete shared-CSV rebuild passed. The complete
48-byte ELF span at `0xD4F40` and pristine retail span at
`conker/conker.us.bin+0xC23F0` both have SHA-256
`989b94637e932e7057eebd6fad9b2ef29c52742fc6ad60b41c25aa1e85b783b1`.
The patch table has 650 rows, zero duplicate keys, nine target rows, and two
target insertion-bearing rows.

The `64CBFDOGL` sibling mentions this routine only in historical port notes;
it has no hand-maintained implementation requiring a transplant. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

Continue with 15-word `func_15096934`, now the first game row with ten real
differences. It is another display-list cursor writer in the same generated
slice; compare its exact relocations and state-byte clear before reusing this
expansion pattern.
