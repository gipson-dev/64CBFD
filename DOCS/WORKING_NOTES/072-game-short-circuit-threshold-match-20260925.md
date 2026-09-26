# Game short-circuit threshold match - 2026-09-25

## Result

All 19 tracked words of `func_150DE2C4` now match retail across
`0x150DE2C4..0x150DE310`. The linked matcher reports `2585 / 5484 (47.14%)`
overall and `2017 / 4795 (42.06%)` game, with one address-drift blocker and
2,898 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine subtracts `0x1A` from the signed halfwords at offsets `0x34` and
`0x36`, then clears the halfword at offset `0x38` when either adjusted value
is below ten. Expressing the two equivalent branches as one logical-OR test
restores retail's short-circuit control flow, branch-likely delay-slot clear,
single shared second clear, and two trailing padding words directly from C.

No guarded words were added. The generated object and complete link passed,
and the complete 76-byte linked span at
`conker/build/conker.us.bin+0x10B744` and pristine retail span at
`conker/conker.us.bin+0x10B774` both have SHA-256
`fc341f80de7976c7bcfee30c55345917dd6461764c3c1015adf431f8ad893c4b`.
The patch table remains at 659 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 12-word `func_151318E8`, now the first game row with ten real
differences. Compare its C, compact object, retail words, and relocations
before editing.
