# Game display-list state-byte match - 2026-09-25

## Result

All 15 words of `func_15096934` now match retail across
`0x15096934..0x15096970`. The linked matcher reports `2583 / 5484 (47.10%)`
overall and `2015 / 4795 (42.02%)` game, with one address-drift blocker and
2,900 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function emits display-list command `0xDE000000` with target
`D_80087408`, advances the cursor by eight bytes, clears byte `D_800D2DAB`,
and returns the advanced cursor. It is a structural relative of
`func_15094F40`, but its symbols and byte-sized clear were verified
independently before applying the established expansion.

Nine expected-word guards preserve the original cursor in `v1`, move the
target-address and state-byte relocations to their retail instructions, store
through `v1`, advance `a0`, and insert the advanced-cursor copy and final
delay-slot word. All four `R_MIPS_HI16`/`R_MIPS_LO16` relocations remain
explicit. The final three retail padding words remain untouched.

The generated object and complete shared-CSV rebuild passed. The complete
60-byte ELF span at `0xD6934` and pristine retail span at
`conker/conker.us.bin+0xC3DE4` both have SHA-256
`0ce9e94a848eba73ef07a221cf21947ea38ba900526bc53580d4a1f9417ea7ed`.
The patch table has 659 rows, zero duplicate keys, nine target rows, and two
target insertion-bearing rows.

The `64CBFDOGL` sibling mentions this routine only in historical port notes;
it has no hand-maintained implementation requiring a transplant. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

Continue with 28-word `func_150CF578`, now the first game row with ten real
differences. Compare its global-coordinate arithmetic C, compact object,
retail words, and relocations before editing.
