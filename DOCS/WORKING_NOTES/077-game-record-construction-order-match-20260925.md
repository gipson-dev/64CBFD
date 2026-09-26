# Game record-construction order match - 2026-09-25

## Result

All 34 words of `func_151D74B0` now match retail across
`0x151D74B0..0x151D7538`. The linked matcher reports `2590 / 5484 (47.23%)`
overall and `2022 / 4795 (42.17%)` game, with one address-drift blocker and
2,893 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine constructs an eight-byte record from the source pointer and three
byte values, calls `func_151D71B0`, and copies the record to offset `0x40` of
the returned object when allocation succeeds. The frame, record contents,
seven call arguments, both call relocations, conditional branch, `memcpy`,
and epilogue were already correct.

Moving `rec.word0 = arg0` ahead of the three byte-field assignments restores
retail's pointer store before the remaining byte and stack-argument loads.
That single source-order correction accounts for all ten differing schedule
words without guarded rows.

The complete object and link passed. The complete 136-byte linked span at
`conker/build/conker.us.bin+0x204930` and pristine retail span at
`conker/conker.us.bin+0x204960` both have SHA-256
`002a8c708dffc31c8235fae006313e893a65b893b7ffcc3e730a65a2ec243d01`.
The patch table remains at 678 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

The ten-difference game tier is complete. Continue with 20-word
`func_150717E0`, now the first game row with eleven real differences. Compare
its source model, compact object, retail words, and relocations before editing.
