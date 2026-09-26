# Game nullable callback dispatch match - 2026-09-26

## Result

`func_1509F660` is byte-exact directly from recovered C across all twenty words
at `0x1509F660..0x1509F6B0`. The linked matcher reports
`2643 / 5483 (48.20%)` overall and `2075 / 4794 (43.28%)` game, with one
address-drift blocker and 2,839 total differing C functions. Debugger remains
complete at `181 / 181`.

## Recovered dispatch

The function obtains a nullable pointer from `func_1505EEF4(arg0)`. When the
lookup succeeds, nonzero `arg1` dispatches the pointer to `func_10010A3C` and
zero dispatches it to `func_100109D0`.

Using a local `void *` preserves that pointer-shaped result without widening
the generated slice's current include surface. IDO naturally restores the
retail 24-byte frame, incoming `a1` spill, result null branch with `a0` handoff,
two callback paths, branch-scheduled `ra` reload, and shared epilogue. No
guarded rows are needed, and the patch table remains at 936 unique rows.

## Evidence

The final linked and pristine 80-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0xCCAE0`
- retail `conker/conker.us.bin+0xCCB10`
- SHA-256 `d00d2f837ee5b5fe1d446316d5725177d4b35f4f7df93686a54b2f2cd3df2b6d`

The focused object build, nonmatching relink, fresh direct matcher, outer
build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation translation,
calls, declaration, and symbol metadata for this function, with no separately
maintained host implementation to update. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 19-word `func_151C4510`. Its existing C already expresses three
scaled additions into fields `0x34`, `0x38`, and `0x3C`, but the fresh matcher
reports fifteen real scheduling differences. Establish the compact register
and load/store schedule before adding guarded normalization.
