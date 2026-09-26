# Game allocation/copy wrapper match - 2026-09-26

## Result

All 28 words of `func_15168800` now match retail across
`0x15168800..0x15168870`. The linked matcher reports `2608 / 5484 (47.56%)`
overall and `2040 / 4795 (42.54%)` game, with one address-drift blocker and
2,875 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function allocates a record through `func_15167A68`, copies 168 bytes from
`arg0` to offset `0x10` in that record, and returns the allocation. Its first
fourteen words through the allocation call and delay slot were already exact.
The previous `if (tmp != NULL)` form branched around the copy and merged both
outcomes through a final `v1` result.

Expressing allocation failure as `if (tmp == NULL) return NULL` makes IDO emit
retail's positive branch into the copy path, explicit zero-return branch delay
slot, retained allocation in `v1`, `v1 + 0x10` destination, stack spill across
`bcopy`, and direct result reload. Both call relocations, the 40-byte frame,
and the complete 28-word extent match directly from source. No expected-word
guards were needed.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x195C80` and pristine
retail `conker/conker.us.bin+0x195CB0` are byte-identical for 112 bytes and
share SHA-256
`163d065da4eac9216fff364ccc3d94c87935a63389ba18289abde3a2eef4f5f7`.
The patch table remains at 767 rows with zero duplicate keys.

The `64CBFDOGL` sibling has three symbol-map metadata hits and historical
documentation references describing this guest routine, but no maintained
implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 18-word `func_151E5FAC`, the final game row with twelve real
differences. It returns `D_8008FD8C` when `D_800E0BEB` is set and that signed
byte is below five; otherwise it returns signed byte `D_8008FD90`. Current C
merges both fallback cases into one tail and leaves three padding words.
Retail preloads the default-value address before the flag branch, rematerializes
it before the threshold test, places one default-value load in a return delay
slot, and retains a separate flag-false fallback. Test duplicated explicit
fallback returns and positive threshold control flow before adding guards.
