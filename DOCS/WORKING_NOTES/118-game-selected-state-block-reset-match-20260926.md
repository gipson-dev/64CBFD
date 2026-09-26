# Game selected state-block reset match - 2026-09-26

## Result

`func_1508F060` is byte-exact across all seventeen words at
`0x1508F060..0x1508F0A4`. The linked matcher reports
`2630 / 5483 (47.97%)` overall and `2062 / 4794 (43.01%)` game, with one
address-drift blocker and 2,852 total differing C functions. Debugger remains
complete at `181 / 181`.

## Corrected behavior

The function clears standalone state bytes `D_800D246D` and `D_800D247D`,
selects row two from the 16-byte-stride `D_800D2460` state block, clears four
bytes relative to that selected row, then clears word `D_800D24C0`.

The previous C accessed `D_800D2460[1][13]`, `[2][13]`, `[3][13]`, and
`[0][13]` from the unshifted base. Retail first adds `2 * 16`, so those stores
were targeting the wrong bytes. The source now forms `&D_800D2460[2]` and
performs the four row-relative clears through that pointer.

IDO constant-folds the selected pointer into direct offsets and emits only
fourteen instructions. Retail retains the index in `v0`, table base in `t7`,
scaled index in `t6`, and selected pointer in `v1`. Nine stale-guarded rows
restore the global-address order and the index setup; insertions after compact
offsets `0x1C`, `0x20`, and `0x24` add the base sum and two otherwise folded
stores. The existing `D_800D24C0` relocation pair and return then slide into
their retail positions naturally.

## Evidence

The final linked and pristine 68-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0xBC4E0`
- retail `conker/conker.us.bin+0xBC510`
- SHA-256 `5a6bee06d54645060055d96fea8a8d6bd8253996ea416f5e385bc7133ed93ebe`

The patch table contains 867 rows, nine for this function, and no duplicate
`(filename, function, offset)` keys. The focused object build, exhaustive
nonmatching rebuild and no-op confirmation, fresh direct matcher, outer build,
and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation copies of this
function, with no separately maintained host implementation to update. Its
1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 17-word `func_1518F89C`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It samples `func_150ADA68`, updates
the float at object offset `0x30` from fields at `0x3C` and `0x40`, then calls
`func_1518F8E0`. Its current body has the right frame and calls but does not
retain retail's object pointer and floating-point operation schedule.
