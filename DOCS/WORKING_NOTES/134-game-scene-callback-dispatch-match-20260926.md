# Game scene callback dispatch match - 2026-09-26

## Result

`func_15130230` is byte-exact across all twenty words at
`0x15130230..0x15130280`. The linked matcher reports
`2646 / 5483 (48.26%)` overall and `2078 / 4794 (43.35%)` game, with one
address-drift blocker and 2,836 total differing C functions. Debugger remains
complete at `181 / 181`.

## Explicit callback argument

The function reads the callback selector byte at `D_800B0DF0 + 0x0F`. A zero
selector returns immediately; a nonzero selector indexes `D_80089670` and
calls that scene-specific callback.

The previous placeholder invoked the unprototyped callback without spelling
out an argument. Although incoming `a0` survived to the indirect call, IDO
treated the named `arg0` as unused and spilled it beside `arg1`, making the
compact body one word too long. Passing `arg0` explicitly keeps it live in
place. IDO then naturally emits retail's 24-byte frame, sole incoming `a1`
spill, selector load, null branch with the index shift in its delay slot,
indirect call, shared epilogue, and 17-word body. The generated-slice padding
step supplies the three trailing zero words required by the 20-word extent.
No guarded word patches are needed, and the patch table remains at 958 unique
rows with no duplicate keys.

## Evidence

The final linked and pristine 80-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x15D6B0`
- retail `conker/conker.us.bin+0x15D6E0`
- SHA-256 `7989f751808c1c44c0cfe110f6f1b79f394e3da439b4ce5666479ed702f0cf23`

The focused object build, exhaustive nonmatching rebuild, fresh linked matcher,
outer build, six project-tool unit tests, and project tool checks passed.

The `64CBFDOGL` sibling contains generated recompilation translation,
declaration, and call-site metadata for this function, with no separately
maintained host implementation to update. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 59-word
`func_1506C32C`, the first ordinary-C row in the fresh smallest-difference
queue. Its recovered animation sound-choice behavior is already present in
`game_981E0.c`; the linked matcher reports fifteen real instruction
differences, so establish its current register and scheduling delta before
changing semantics.
