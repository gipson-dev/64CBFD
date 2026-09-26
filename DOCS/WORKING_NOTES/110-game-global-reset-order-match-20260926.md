# Game global reset order match - 2026-09-26

## Result

`func_1519582C` is byte-exact across all fifteen words at
`0x1519582C..0x15195868`. The linked matcher reports
`2622 / 5483 (47.82%)` overall and `2054 / 4794 (42.85%)` game, with one
address-drift blocker and 2,860 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The function clears `D_800E08E4`, `D_800E08E0`, `D_800E08EC`, and
`D_800E08E8`, then writes `-2` to `D_800E08F0`. The original generated C had
the correct values and statement order, but IDO emitted four direct
`%hi/%lo` stores and left two padded words in the retail span.

Ordinary and register-qualified pointer locals folded back to those direct
stores. Volatile target pointers recovered the two missing address-completion
instructions and exact fifteen-word size, but IDO formed each address
immediately before its store in `t6` and `t7`. Grouping both declarations did
not alter that stable schedule.

The accepted source keeps the clear volatile-pointer intent and uses eight
expected-word and expected-relocation guards for the opening prefix. Retail
preloads `D_800E08E4` into `v0` and `D_800E08EC` into `v1`, completes `v1`
before `v0`, then interleaves the direct `D_800E08E0` store. The final seven
words, from the `D_800E08E8` address through return, match directly.

The exhaustive non-matching rebuild, link, fresh matcher, outer build, and
project tool checks passed. Linked `conker/build/conker.us.bin+0x1C2CAC` and
pristine retail `conker/conker.us.bin+0x1C2CDC` are byte-identical for 60 bytes
and share SHA-256
`ad45cf74ef6a44637dde894db55c1018e023ef7fd224566b94df67081155c95a`.
The patch table contains 831 rows, zero duplicate keys, and eight rows for this
function.

The `64CBFDOGL` sibling contains recompilation metadata and a stub declaration
for this address, but no maintained host implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 15-word `func_151A9024`, now the first game row with thirteen
real differences. Its generated C conditionally calls `func_151A931C` when
byte `0x4C` equals one. Retail additionally stores the third argument in its
home area, narrows and copies it back into `a2`, and uses a `bnel` early
epilogue with the `$ra` restore in the delay slot.
