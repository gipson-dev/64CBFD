# Game nested-state flag match - 2026-09-26

## Result

`func_151C9B64` is byte-exact across all fifteen words at
`0x151C9B64..0x151C9BA0`. The linked matcher reports
`2624 / 5483 (47.86%)` overall and `2056 / 4794 (42.89%)` game, with one
address-drift blocker and 2,858 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

Retail loads the nested pointer at object offset `0x188` and checks its byte
at offset `0x6F`. A nonzero byte clears bit 1 in the object word at offset
`0x58` and writes zero through `arg1`; a zero byte writes one through `arg1`.
The generated C had those outcomes reversed.

Flipping only the comparison corrected behavior but produced a duplicated
one-byte store and a different control-flow schedule. Expressing the zero path
first recovered retail's branch-likely layout, including its duplicated
unreachable word before the nonzero label. Naming the nested pointer then
restored its initial `v0` lifetime, the return-value reuse of `v0`, and the
exact `t6` through `t9` allocation. All fifteen words match directly from C;
no patch-table rows are required.

The linked and pristine 60-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1F6FE4`
- retail `conker/conker.us.bin+0x1F7014`
- SHA-256 `858ab5572befd445453963a3e2f71e301e601166088a9fbfd54a0da147819bbc`

The nonmatching build and link, fresh matcher, outer build, and project tool
checks passed. The ordinary `make match-progress` verification prerequisite
still rejects the intentionally nonmatching whole-ROM checksum, so the fresh
scan was run directly with `tools/match_progress.py` against the linked ELF.

The `64CBFDOGL` sibling references this address in recompilation metadata and
generated declarations, but has no maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

The tied 13-word game rows `func_151F892C` and `func_151F8960` were inspected
and excluded: both are explicitly handwritten and consume non-ABI live
registers. Continue the C-restoration queue at `func_1502C380`.
