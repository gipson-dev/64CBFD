# Game two-word aggregate call match - 2026-09-26

## Result

All 17 words of `func_151090DC` now match retail across
`0x151090DC..0x15109120`. The linked matcher reports `2595 / 5484 (47.32%)`
overall and `2027 / 4795 (42.27%)` game, with one address-drift blocker and
2,888 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine copies the two words at `D_80088C58` into an eight-byte stack
object and passes that object to `func_15169260` with arguments `2`, `0`, and
`0x1E`. The former pair of scalar assignments made IDO materialize the global
through `v0`, load both words early, and store them through direct stack
offsets.

Initializing the existing `TwoWord135D00` aggregate from the typed global and
passing its address recovers retail's aggregate-copy sequence directly. IDO
now uses `t6` as the source, `at` and `t9` for the copied words, and `a0` as the
stack-object destination while interleaving the remaining call arguments. The
second store occupies the call delay slot. The frame, saved return address,
relocations, call, epilogue, and all 17 words match without guarded rows.

The complete non-matching link and project tool checks passed. The linked span
at `conker/build/conker.us.bin+0x13655C` and pristine retail span at
`conker/conker.us.bin+0x13658C` both have SHA-256
`55ddb338289c96218fdbd1278286280acc0413a16f923996dfc3be3651ad8e9a`.
The patch table remains at 709 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling exposes this function only through generated symbol
metadata. It has no hand-maintained host body requiring a transplant. Its
1,659 existing dirty entries were left untouched, and frozen Release was not
built, modified, or launched.

## Next boundary

Continue with 28-word `func_15141564`, now the first game row with eleven real
differences. Compare its `arg0 + 0x170` base lifetime, `sinf` position update,
phase accumulation, normalization call, FP registers, and relocations before
editing.
