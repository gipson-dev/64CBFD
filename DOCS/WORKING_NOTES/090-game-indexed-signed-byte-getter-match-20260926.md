# Game indexed signed-byte getter match - 2026-09-26

## Result

All 13 words of `func_150882B0` now match retail across
`0x150882B0..0x150882E4`. The linked matcher reports `2603 / 5484 (47.47%)`
overall and `2035 / 4795 (42.44%)` game, with one address-drift blocker and
2,880 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine returns signed byte `0x27` from a 132-byte record selected through
`D_800872A0`, or zero when the global record table is null. The former C body
declared the index before the pointer and returned through a separate pointer
local. IDO optimized away the index copy, emitted a 12-word body plus slot
padding, and formed the final pointer in `t7`.

Declaring the global pointer before the retained index and assigning the final
record address back to `arg0` gives a meaningful 13-word C body. IDO preserves
the original index and uses the intended final argument lifetime, but still
schedules the global load before the index copy and splits the stride around
the branch. Explicit precomputed-offset and assignment-order probes either
coalesced away the copy or reversed the `a1`/`v1` allocation.

Ten expected-word guards finish the schedule. Three explicitly move the
`D_800872A0` HI16/LO16 relocation pair after retail's opening `move a1,a0`;
five place the complete 132-byte stride before and in the null-branch delay
slot; two form and load through the final pointer in `a0`. No word is inserted,
and the branch target, return paths, and 13-word extent remain unchanged.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0xB5730` and pristine
retail `conker/conker.us.bin+0xB5760` are byte-identical for 52 bytes and share
SHA-256 `7c3ea120c159b30ba557ad53b2e8ab7720ec13bb50a7daebf4f56f9d93ed63c4`.
The patch table contains 745 rows, zero duplicate keys, and ten rows for this
function.

The `64CBFDOGL` sibling has no hit for this function in its maintained source,
headers, tools, scripts, or documentation. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains its 2026-09-23 timestamp.

## Next boundary

Continue with 16-word `func_1508B194`, now the first game row with twelve real
differences. It bounds-checks `arg0` against signed byte `D_8008FD90`, then
returns halfword `0x70` from a 12-byte record selected through `D_8008FDD4`.
Retail uses a positive branch to a separate load path and an explicit
zero-return path; current C emits a negative branch with zero in its delay slot
and places the halfword load in the final return delay slot. Both global
HI16/LO16 pairs also differ in schedule. Test positive-branch source shapes
and retained base/index lifetimes before adding guards.
