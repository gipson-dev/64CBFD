# Game four-word state clear match - 2026-09-25

## Result

All ten words of `func_151E81EC` now match retail across
`0x151E81EC..0x151E8214`. The linked matcher reports `2579 / 5484 (47.03%)`
overall and `2011 / 4795 (41.94%)` game, with one address-drift blocker and
2,904 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine clears four adjacent words at `D_800E0BA0..D_800E0BAC`, then
clears byte `D_8008FD84`. The previous body was a three-word `return 0`
placeholder. Independent scalar assignments and array access both reproduce
the behavior but exceed the fixed ten-word retail extent.

Representing the four words as one struct and using a chained assignment
preserves all five stores, their retail order, and the exact function size.
IDO still materializes one base pointer, while retail uses two shared `$at`
high halves for paired symbol stores. Six function-specific guards replace
only that address form and preserve explicit `R_MIPS_HI16`/`R_MIPS_LO16`
relocations for `D_800E0BA4`, `D_800E0BA0`, `D_800E0BA8`, and `D_800E0BAC`.
The byte clear and two return words are compiler-exact.

The generated object and complete shared-CSV rebuild passed. The complete
40-byte ELF span at `0x2281EC` and pristine retail span at
`conker/conker.us.bin+0x21569C` both have SHA-256
`8ffd94c76c5a73aa7b0eaa0be788a471eb78a68224cc3b6365c6ce6666ddd16d`.
The patch table has 631 rows, zero duplicate keys, and six target rows.

The `64CBFDOGL` sibling has only an investigation note referring to this
routine among hand-maintained sources. Its generated recompilation artifacts
do not require a manual transplant. The dirty sibling tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 17-word `func_1502EA0C`, now the first game row with ten real
differences. Compare its packed-byte writer C, compact object, retail words,
and relocations before editing.
