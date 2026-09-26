# Game duplicate masked-field store match - 2026-09-26

## Result

All 40 words of `func_151355B8` now match retail across
`0x151355B8..0x15135658`. The linked matcher reports `2607 / 5484 (47.54%)`
overall and `2039 / 4795 (42.52%)` game, with one address-drift blocker and
2,876 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function handles event selectors zero and three. Both paths compare a
word or byte identifier. Selector zero calls `func_1516972C` on a match;
selector three clears bit zero in the word at offset `0x10` and writes the
same result twice. The previous ordinary C assignments let IDO eliminate the
second identical store. That shortened the body by one instruction, changed
three exit-branch offsets, and left a padding word after the return.

Qualifying only the offset-`0x10` read and writes as volatile makes the two
stores observable. IDO then emits both stores and directly restores all branch
targets, the return placement, and the complete 40-word extent. A chained
assignment still collapsed to one store. Splitting the load and mask into two
locals selected `v1` and `v0`, which was worse. A retained volatile pointer
local folded to the same object as the simpler direct volatile accesses.

Five expected-word guards cover the remaining register-allocation cluster at
relative offsets `0x68`, `0x7C`, and `0x84..0x8C`. They select retail's `t5`
loaded field and `t6` masked result in both duplicate stores. No relocation,
branch, call, frame, or other control-flow word is guarded.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x162A38` and pristine
retail `conker/conker.us.bin+0x162A68` are byte-identical for 160 bytes and
share SHA-256
`905987a8e0bd8c6da95744f53d6707165b266566a5e67456208c2d84e35d4f97`.
The patch table contains 767 rows, zero duplicate keys, and five rows for this
function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 28-word `func_15168800`, now the first game row with twelve real
differences. It allocates a record with `func_15167A68`, copies 168 bytes from
`arg0` to the allocated record at offset `0x10`, and returns the allocation.
The first fourteen words through the allocation call are already exact.
Retail branches positively into the copy path and explicitly returns null on
allocation failure; current C branches around the copy and joins through a
final `v1` result. Express the failure as an early null return before testing
any guarded scheduling changes; preserve both call relocations and the
28-word extent.
