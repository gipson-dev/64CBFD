# Game angle normalization match - 2026-09-26

## Result

`func_15144BC8` is byte-exact across all twenty-five words at
`0x15144BC8..0x15144C2C`. The linked matcher reports
`2638 / 5483 (48.11%)` overall and `2070 / 4794 (43.18%)` game, with one
address-drift blocker and 2,844 total differing C functions. Debugger remains
complete at `181 / 181`.

## Source lifetime

The function normalizes an angle into the inclusive 0-to-360 range by
repeatedly subtracting or adding `360.0f`. The previous source mutated incoming
`arg0` directly, keeping the angle in `f12` and loading zero into `f2`.

Introducing `f32 ret = arg0`, applying both loops to `ret`, and returning it
matches the neighboring `func_15144B68` idiom. IDO copies incoming `f12` to
`f2`, reuses `f12` for zero, and emits retail's exact comparisons,
branch-likely delay slots, loop backs, result copies, and return. No guarded
rows are required, and the patch table remains at 903 unique rows.

## Evidence

The final linked and pristine 100-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x172048`
- retail `conker/conker.us.bin+0x172078`
- SHA-256 `4045e24a198fb60bd83d11f5ebef1738e49fe3e58ce02b2824547f86b5a9d441`

The focused object build, nonmatching relink, fresh direct matcher, outer
build, and project tool checks passed.

The `64CBFDOGL` sibling contains generated recompilation calls, a translation,
and a declaration, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 45-word `func_150718E4`, the sole remaining ordinary-C game row
at fourteen real differences. Its branch structure, calls, constants, and
field accesses already agree with retail. The current build places the
`D_80099BB8` random-byte source word at `sp + 0x2C` and `struct17` at
`sp + 0x20`; retail places them at `sp + 0x20` and `sp + 0x24`, respectively.
Reverse the two local declarations first, then compare whether the corrected
stack layout also restores retail's `t0..t5` register sequence before adding
guarded normalization.
