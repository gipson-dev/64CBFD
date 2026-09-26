# Game seven-argument wrapper match - 2026-09-25

## Result

All 19 words of `func_151581D8` now match retail across
`0x151581D8..0x15158224`. The linked matcher reports `2589 / 5484 (47.21%)`
overall and `2021 / 4795 (42.15%)` game, with one address-drift blocker and
2,894 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine forwards seven arguments to `func_151580B0`, inserting zero for
the second and third arguments while narrowing the incoming byte arguments
and forwarding the remaining stack arguments. Its frame, every spill and
reload, outgoing stack slots, call relocation, delay-slot store, and epilogue
were already present in the compact object.

IDO orders ten independent prologue and argument-preparation words
differently from retail. Equivalent local and parameter-reuse source forms
either compiled identically or changed value registers, so they were
rejected. Ten expected-word guards normalize only the existing instruction
schedule. They move no relocation, insert no word, and alter no operand,
stack slot, call target, or control flow.

The complete generated-object rebuild and link passed. The complete 76-byte
linked span at `conker/build/conker.us.bin+0x185658` and pristine retail span
at `conker/conker.us.bin+0x185688` both have SHA-256
`0792b2f5cacd300b78d1eda3584b4422de9d312ba57cc4a943b7be7af3efd4be`.
The patch table has 678 rows, zero duplicate keys, ten target rows, and no
target insertion-bearing rows.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 34-word `func_151D74B0`, now the first game row with ten real
differences. Compare its source model, compact object, retail words, and
relocations before editing.
