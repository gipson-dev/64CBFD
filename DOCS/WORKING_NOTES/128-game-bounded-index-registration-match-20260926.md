# Game bounded-index registration match - 2026-09-26

## Result

`func_150142AC` is byte-exact across all sixteen words at
`0x150142AC..0x150142EC`. The linked matcher reports
`2640 / 5483 (48.15%)` overall and `2072 / 4794 (43.22%)` game, with one
address-drift blocker and 2,842 total differing C functions. Debugger remains
complete at `181 / 181`.

## Bound and exit recovery

The function sets object flag `0x04`, reads the index byte at offset `0x1B`,
and registers the object in `D_800D9AA0` only for indices zero through two.
The previous source used `u8 idx` and only expressed the upper bound, producing
a shorter single-exit body.

Recovering `s32 idx`, assigning it after the flag update, and spelling the
invalid path as `idx < 0 || idx >= 3` restores retail's load order, `v1`
lifetime, `bltz`, upper-bound branch into the store, and distinct early and
final return sequences. The lower-bound branch is retained by IDO even though
the source byte is loaded unsigned. No guarded rows are required, and the
patch table remains at 913 unique rows.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x4172C`
- retail `conker/conker.us.bin+0x4175C`
- SHA-256 `1fdcdcd00fe78afae49fed648e7f3b6598a9f0f8cf9503eeb0c969e401d833ea`

The focused object build, nonmatching relink, fresh direct matcher, outer
build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation translations and
declarations, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 16-word `func_15088270`, now the smallest ordinary-C game row
among the fifteen-difference candidates. Retail copies incoming `arg0` into
`a1`, computes the `0x84` record stride from `a1`, and reuses `a0` for the
record pointer before converting the float at offset `0x14` to an integer. The
current source computes directly from `arg0`, leaving the stride in `a0` and
the pointer in `t7`. Mirror neighboring `func_150882B0` with an explicit
`s32 idx = arg0` before considering guarded normalization.
