# Game animation sound-choice match - 2026-09-26

## Result

`func_1506C32C` is byte-exact across all 59 words at
`0x1506C32C..0x1506C418`. The linked matcher reports
`2647 / 5483 (48.28%)` overall and `2079 / 4794 (43.37%)` game, with one
address-drift blocker and 2,835 total differing C functions. Debugger remains
complete at `181 / 181`.

## Shared selection lifetime

The recovered function handles animation command `0x0A`. It decrements the
pending packed sound state, unpacks as many as four 11-bit authored choices,
uses `func_1000F568` to select one when alternatives exist, merges that choice
back into the packed state, and calls `func_1506BF5C` when the result is
nonzero. This behavior was preserved.

The previous source represented the alternative count and selected index as
separate locals. IDO consequently kept the count in `a1`, created a separate
`v1` lifetime for the selected index, and emitted a 64-byte frame. Reusing one
`selected` local across both phases restores retail's `a1` lifetime, its
branch-likely null-count path with the index shift in the delay slot, and the
56-byte frame. IDO assigns debug homes in reverse declaration order; placing
the four-word `choices` array between `packed` and `selected` lands it at the
retail `sp+0x24..0x30` range. All 59 words then match directly from C. No
guarded word patches are needed, and the patch table remains at 958 unique
rows with no duplicate keys.

## Evidence

The final linked and pristine 236-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x997AC`
- retail `conker/conker.us.bin+0x997DC`
- SHA-256 `e069a7bd0b07961da1280aefd0541d6fea6883e891c1cd3815211165b5fbe20d`

The focused object build, exhaustive nonmatching rebuild, fresh linked matcher,
outer build, six project-tool unit tests, and project tool checks passed.

The `64CBFDOGL` sibling contains generated recompilation translation and
declaration metadata for this function, with no separately maintained host
implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 33-word
`func_150CFDB8`, the first ordinary-C row in the fresh smallest-difference
queue. Its existing C scans variable-length records from `arg0` to the end
returned by `func_150CFD5C`, tracking the greatest length returned by
`func_150CFD84`; the linked matcher reports fifteen real differences.
