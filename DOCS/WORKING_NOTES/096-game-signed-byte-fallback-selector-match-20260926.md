# Game signed-byte fallback selector match - 2026-09-26

## Result

All 18 words of `func_151E5FAC` now match retail across
`0x151E5FAC..0x151E5FF4`. The linked matcher reports `2609 / 5484 (47.57%)`
overall and `2041 / 4795 (42.57%)` game, with one address-drift blocker and
2,874 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function returns signed byte `D_8008FD8C` when flag `D_800E0BEB` is set
and the candidate is below five; otherwise it returns signed byte
`D_8008FD90`. The previous source merged both fallback cases into one tail,
emitting only fifteen active words followed by three padding words.

Adding an explicit fallback return inside the flag block restores the separate
18-word control-flow extent. Reversing the nested condition to `temp_v1 >= 5`
restores retail's positive branch into the candidate-return path. Pointer-local
and `register` pointer probes did not make IDO preload the flag-false fallback
address and were removed.

Twelve expected-word guards cover relative offsets `0x0C..0x38`. They preload
the flag-false `D_8008FD90` address, move the flag branch and candidate load,
rematerialize `D_8008FD90` for the threshold-failure path, and restore both
return-delay loads. The guards explicitly move the `D_8008FD8C` LO16
relocation and both `D_8008FD90` HI16/LO16 pairs. The initial flag relocation,
candidate-address HI16, final fallback LO16, and final return remain exact and
unguarded.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x21342C` and pristine
retail `conker/conker.us.bin+0x21345C` are byte-identical for 72 bytes and
share SHA-256
`6b4a87b0141da6aebe6c6d4e3a60eefa444d170d0fdf07689f40e48da5d1f7ff`.
The patch table contains 779 rows, zero duplicate keys, and twelve rows for
this function.

The `64CBFDOGL` sibling has three symbol-map metadata hits and one historical
interpreter note that calls this guest routine, but no maintained
implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 39-word `func_15002560`, now the first game row with thirteen
real differences. It walks a relative-offset tree, fills a missing sibling
offset from `arg1`, descends through child offset `0x0C`, recursively repairs
siblings, and advances until a zero child offset ends the walk. Compare the
current and retail loop/recursive-call schedules before changing source; keep
the recursion call relocation, early return, and 39-word extent intact.
