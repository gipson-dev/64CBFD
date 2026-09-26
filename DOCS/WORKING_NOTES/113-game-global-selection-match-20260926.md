# Game global-selection match - 2026-09-26

## Result

`func_1502C380` is byte-exact across all fifteen words at
`0x1502C380..0x1502C3BC`. The linked matcher reports
`2625 / 5483 (47.88%)` overall and `2057 / 4794 (42.91%)` game, with one
address-drift blocker and 2,857 total differing C functions. Debugger remains
complete at `181 / 181`.

## Candidate exclusion

The matcher first offered 13-word `func_151F892C` and `func_151F8960`. Their
retail assembly explicitly marks both as handwritten. They consume values in
`t0` and, for `func_151F892C`, `s1` that are not represented by the normal
function ABI. Their padded C placeholders are therefore not conversion
targets and were left unchanged.

## Evidence

`func_1502C380` selects one word from `D_800C3E80` using byte index
`D_800BE9C0`, copies it to `D_800C3E88` and `D_800C3E8C`, then clears
`D_800C3E7A`. The original local-value form expressed the behavior correctly,
but IDO folded the first destination into a direct store and used `v0` for the
source array and value.

Writing the copy as an assignment chain makes the first destination's address
observable to the second expression. IDO then retains `&D_800C3E88` in `v0`
and the selected value in `t8`, reproducing all fifteen retail words directly
without guarded patch rows.

The linked and pristine 60-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x59800`
- retail `conker/conker.us.bin+0x59830`
- SHA-256 `5ac1848a7f9245f00f951fd6a5260b0718bb374820703bff54ae237941375025`

The nonmatching build and link, fresh direct matcher, outer build, and project
tool checks passed. The `64CBFDOGL` sibling has renderer comments describing
this frame-pool cursor reset and generated recompilation output, but no
separately maintained host implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 16-word `func_150A7B80`, the smallest ordinary-C row among the
fourteen-difference candidates. Its current loop exceeds the fixed retail
slot and is redirected to `.game_overflow`; retail uses eight unrolled
64-bit zero stores followed by four diagonal halfword stores.
