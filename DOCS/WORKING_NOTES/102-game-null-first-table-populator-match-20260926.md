# Game null-first table populator match - 2026-09-26

## Result

All 30 words of `func_15085B70` now match retail across
`0x15085B70..0x15085BE8`. The linked matcher reports `2615 / 5484 (47.68%)`
overall and `2047 / 4795 (42.69%)` game, with one address-drift blocker and
2,868 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine asks `func_1502B5C8` for a table. On failure it clears
`D_80087290`, `D_80087294`, and `D_800D2350`; on success it copies two
halfwords and points `D_800D2350` four bytes past the returned header. It then
tail-calls the common setup through `func_15085BE8` and returns its result.

The original C tested `temp_v0 != 0`, laying out the populated path first and
branching to the zeroing path. Retail instead uses `bnez` to skip a compact
fallthrough zeroing path and then executes the populated path. Reversing the C
condition to `temp_v0 == 0` reproduces retail's physical path order exactly.
That single source change restores all thirteen differing words without
changing behavior or adding guarded patches.

The frame, allocator call and delay slot, six global HI16/LO16 relocation
pairs, populated loads and stores, zeroing stores, final call, and epilogue are
all source-emitted and exact. The exhaustive non-matching link, linked matcher,
outer build, and project tool checks passed. Linked
`conker/build/conker.us.bin+0xB2FF0` and pristine retail
`conker/conker.us.bin+0xB3020` are byte-identical for 120 bytes and share
SHA-256
`420680f426f2b1f2b80d4d03a344b7ca8de125e0cc9067820c2464ec5e5d5a19`.
The patch table remains at 808 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling has three symbol-map metadata hits and historical
documentation that previously described this donor routine as a zeroed ROM
stub, but no maintained host implementation was found to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 13-word `func_150A7A14`, now the first game row with thirteen
real differences. Because every tracked word currently differs, first confirm
whether the C body has the correct extent and behavior or represents another
false placeholder before attempting source scheduling or guarded words.
