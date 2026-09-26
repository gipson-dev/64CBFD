# Game global-coordinate update match - 2026-09-25

## Result

All 28 words of `func_150CF578` now match retail across
`0x150CF578..0x150CF5E8`. The linked matcher reports `2584 / 5484 (47.12%)`
overall and `2016 / 4795 (42.04%)` game, with one address-drift blocker and
2,899 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine reads `D_800BE9E4`, adds 26 times that value to `D_80088890`,
and subtracts 28 times it from both `D_80088894` and `D_80088898`. Naming the
loaded value as a local before deriving the 28-times temporary restores
retail's `v0` source lifetime, `v1` temporary lifetime, and arithmetic
schedule directly from C.

No guarded words were added. The generated object and complete link passed,
and the complete 112-byte linked span at `conker/build/conker.us.bin+0xFC9F8`
and pristine retail span at `conker/conker.us.bin+0xFCA28` both have SHA-256
`9380ec55443833e5ed9950f30c40317a0bd33d130dbcba4a2a34e2aa36427898`.
The patch table remains at 659 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes only
its generated declaration, symbol-table entry, and dispatch registration.
It has no hand-maintained implementation requiring a transplant. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

Continue with 19-word `func_150DE2C4`, now the first game row with ten real
differences. Compare its C, compact object, retail words, and relocations
before editing.
