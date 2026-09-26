# Game flag-gated high-half-mask match - 2026-09-26

## Result

`func_150C78E0` is byte-exact across all twenty words at
`0x150C78E0..0x150C7930`. The linked matcher reports
`2645 / 5483 (48.24%)` overall and `2077 / 4794 (43.32%)` game, with one
address-drift blocker and 2,837 total differing C functions. Debugger remains
complete at `181 / 181`.

## Mask and retained pointer update

The existing C checks object flag `0x04` at offset `0x73`. On the clear path it
reads the word at `D_800DBEF4 + 0x21C`, negates its high half, masks the result
back to the high half, stores it at object offset `0x3C`, and calls
`func_151150BC`.

The compact C body is nineteen words. Retail rotates the global-pointer load
around the flag test and retains a dead `addiu v0, v0, 0x1E0` after reading the
source word. Six guarded replacements restore the load, mask, and branch
schedule; one guarded insertion restores the dead pointer advance. Both moved
`D_800DBEF4` relocations are explicit. The patch table contains 958 unique rows
with no duplicate keys.

## Evidence

The final linked and pristine 80-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0xF4D60`
- retail `conker/conker.us.bin+0xF4D90`
- SHA-256 `2993ebbc71a7fdab44102ff522da92775807b05b01243a07957585f11868530d`

The focused object build, exhaustive nonmatching rebuild, fresh direct matcher,
outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation translation,
declaration, and symbol metadata for this function, with no separately
maintained host implementation to update. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 20-word `func_15130230`. Its existing C reads the callback index
byte at `D_800B0DF0 + 0x0F` and invokes `D_80089670[index]` when nonzero.
Retail also spills incoming `a1`, computes the table index in the null-check
delay slot, and retains three trailing padding words. Establish the compact
register, relocation, and padded extent before normalization.
