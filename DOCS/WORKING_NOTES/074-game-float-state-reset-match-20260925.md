# Game float-state reset match - 2026-09-25

## Result

All 17 words of `func_15133A50` now match retail across
`0x15133A50..0x15133A94`. The linked matcher reports `2587 / 5484 (47.17%)`
overall and `2019 / 4795 (42.11%)` game, with one address-drift blocker and
2,896 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine clears float fields `0x44`, `0x48`, `0x4C`, `0x50`, `0x54`, and
`0x58`, stores the original `0x10` value plus stack argument `arg4` at `0x3C`,
and returns one. Naming the pending sum and moving its store between the
`0x54` and `0x58` clears restores retail's load, arithmetic, and store
schedule.

IDO still assigns the pending sum to `f0` and the shared zero to `f2`, while
retail keeps zero in `f0` and the sum in `f8`. Nine expected-word guards
normalize only those FP register fields. They move no relocations, insert no
words, and alter no memory address or control flow.

The complete generated-object rebuild and link passed. The complete 68-byte
linked span at `conker/build/conker.us.bin+0x160ED0` and pristine retail span
at `conker/conker.us.bin+0x160F00` both have SHA-256
`d46c11f94cffe15df0b700b643efd7c5844f60926746c7f45c7fb8c409ef7705`.
The patch table has 668 rows, zero duplicate keys, nine target rows, and no
target insertion-bearing rows.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 18-word `func_15133E3C`, now the first game row with ten real
differences. Compare its source model, compact object, retail words, and
relocations before editing.
