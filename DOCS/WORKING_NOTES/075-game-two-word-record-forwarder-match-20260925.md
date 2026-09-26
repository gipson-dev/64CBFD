# Game two-word record forwarder match - 2026-09-25

## Result

All 18 words of `func_15133E3C` now match retail across
`0x15133E3C..0x15133E84`. The linked matcher reports `2588 / 5484 (47.19%)`
overall and `2020 / 4795 (42.13%)` game, with one address-drift blocker and
2,895 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine copies the two-word record at `D_800A3860` into an eight-byte
stack local and forwards its address, record count two, `arg0`, and narrowed
byte `arg1` to `func_15169260`. Replacing two scalar array assignments with a
`TwoWord15F680` aggregate initializer restores retail's copy registers and
call-delay store.

Correcting `func_15169260`'s first parameter from `s32` to `void *` removes
the incompatible pointer/integer call model and lets IDO materialize the
local address directly in `a0`. The resulting frame, argument setup, both
`D_800A3860` relocations, copy sequence, call relocation, and epilogue match
without guarded words.

The complete object and link passed. The complete 72-byte linked span at
`conker/build/conker.us.bin+0x1612BC` and pristine retail span at
`conker/conker.us.bin+0x1612EC` both have SHA-256
`edc82dab6f11e3d95b78955ef9d2bb24d4330125fc2decc6f04d9861724ebd28`.
The patch table remains at 668 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 19-word `func_151581D8`, now the first game row with ten real
differences. Compare its source model, compact object, retail words, and
relocations before editing.
