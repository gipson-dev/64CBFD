# Game linked-list append match - 2026-09-26

## Result

`func_15188A58` is byte-exact across all seventeen words at
`0x15188A58..0x15188A9C`. The linked matcher reports
`2642 / 5483 (48.19%)` overall and `2074 / 4794 (43.26%)` game, with one
address-drift blocker and 2,840 total differing C functions. Debugger remains
complete at `181 / 181`.

## Recovered append behavior

The function clears the new node's pointer at offset `0x0C`, reads the list
head through the caller's second argument, and either installs the first node
or walks the existing offset-`0x0C` chain before appending at the tail. Its
caller passes a freshly initialized record in `a0` and `D_800DF7CC`'s address
in `a1`.

A minimal typed node recovers the exact 17-word size, incoming `a1` reused as
the next-node cursor, `v1` retained as the previous node, the unrolled first
link, and the loop's branch-delay cursor update. Thirteen guarded words restore
retail's alternate branch-likely layout and duplicated null-head assignment.
No words are inserted and no relocations move. The patch table contains 936
unique rows with no duplicate keys.

## Evidence

The final linked and pristine 68-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1B5ED8`
- retail `conker/conker.us.bin+0x1B5F08`
- SHA-256 `19b3fb64f266d1f692e047d4077fd6b9a74d5cbdd737ee500b73fd07a8fae183`

The focused object build, exhaustive nonmatching rebuild, fresh direct matcher,
outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains generated recompilation declarations and
symbol metadata only, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

The matcher's two smaller 13-word rows, `func_151F892C` and `func_151F8960`,
are explicitly handwritten bitstream helpers and remain assembly by design.
Continue with 20-word ordinary-C placeholder `func_1509F660`. Retail calls
`func_1505EEF4(arg0)`, then dispatches the returned pointer to `func_10010A3C`
when `arg1` is nonzero or `func_100109D0` when it is zero.
