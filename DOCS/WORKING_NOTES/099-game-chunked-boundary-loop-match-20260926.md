# Game chunked-boundary loop match - 2026-09-26

## Result

All 18 words of `func_15043B70` now match retail across
`0x15043B70..0x15043BB8`. The linked matcher reports `2612 / 5484 (47.63%)`
overall and `2044 / 4795 (42.63%)` game, with one address-drift blocker and
2,871 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine consumes `arg3` in chunks capped by the distance from `arg2` to
`arg1`. It advances `arg2`, subtracts the selected chunk from `arg3`, clears
`arg2` when the boundary is reached, and continues until no count remains.

The original C initialized `tmp = arg3` and conditionally overwrote it. IDO
collapsed that spelling into a one-arm fallthrough, omitting retail's
unconditional branch after the alternate subtraction. The object was one word
short inside the tracked body; its final padding word therefore occupied the
last retail slot and thirteen words differed through shifted branch targets.

Expressing the same value choice as
`tmp = arg1 < arg2 + arg3 ? arg1 - arg2 : arg3` makes IDO emit retail's
two-arm merge exactly: `arg3` enters `v0` in the conditional branch delay
slot, the subtraction enters `v0` in an unconditional branch delay slot, and
both paths join before the counter updates. This restores all branch targets,
the branch-likely loop back, the return, and the complete 18-word extent with
no guarded rows or relocations.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x70FF0` and pristine
retail `conker/conker.us.bin+0x71020` are byte-identical for 72 bytes and share
SHA-256
`ba904403da942b5a2963e724bdcbec9cf4b4ec668ad4072fece06f24f09fefc2`.
The patch table remains at 790 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 16-word `func_1507A3E8`, now the first game row with thirteen
real differences. Inspect its source, retail control flow, and current object
before deciding whether the mismatch is another missing merge word or a
register-allocation problem.
