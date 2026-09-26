# Game bounds-checked halfword getter match - 2026-09-26

## Result

All 16 words of `func_1508B194` now match retail across
`0x1508B194..0x1508B1D4`. The linked matcher reports `2604 / 5484 (47.48%)`
overall and `2036 / 4795 (42.46%)` game, with one address-drift blocker and
2,879 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine checks `arg0` against signed byte `D_8008FD90`, then returns the
halfword at offset `0x70` from a 12-byte record selected through
`D_8008FDD4`. The former source put the successful load inside
`if (arg0 < limit)` and returned zero afterward. IDO emitted a negative branch,
zero in its delay slot, and the halfword load in the final return delay slot.

Expressing the same behavior as `if (arg0 >= limit) return 0` directly restores
retail's positive branch, empty branch delay slot, explicit zero-return path,
load-before-return sequence, and complete 16-word extent. That source change
reduces the mismatch from twelve words to five.

The remaining five words are one register-allocation cluster. Retail keeps the
record-table base in `t7` and the 12-byte offset in `t8`; IDO chooses the
reverse. Five expected-word guards select retail's registers. They explicitly
move the `D_8008FDD4` HI16 relocation from offset `0x0C` to `0x08` and retain
its LO16 relocation at offset `0x24` with the corrected register. The
`D_8008FD90` HI16/LO16 pair, branch, return paths, and all other words remain
untouched. An explicit base/offset-local probe was rejected because IDO loaded
the full base into `v1` before the branch.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0xB8614` and pristine
retail `conker/conker.us.bin+0xB8644` are byte-identical for 64 bytes and share
SHA-256 `3b86be0e704bd4067e9efad6096d883a46966c5626da1fb6476ed2dafbb9b1ee`.
The patch table contains 750 rows, zero duplicate keys, and five rows for this
function.

The `64CBFDOGL` sibling has no hit for this function in its maintained source,
headers, tools, scripts, or documentation. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains its 2026-09-23 timestamp.

## Next boundary

Continue with 18-word `func_150E33CC`, now the first game row with twelve real
differences. It loads `*arg2`, returns one when that value is null, otherwise
calls `func_1000E7A0(2, value)` and returns zero. Retail keeps the value in
`v0`, materializes constant two in `a0` before testing it, and moves `v0` to
`a1` in the call delay slot. Current C keeps the value in `a1` and materializes
constant two in the call delay slot. Test argument/local lifetime and call
expression ordering before adding guards; preserve the call relocation and
18-word frame exactly.
