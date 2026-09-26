# Game variable-record maximum match - 2026-09-26

## Result

`func_150CFDB8` is byte-exact across all 33 words at
`0x150CFDB8..0x150CFE3C`. The linked matcher reports 2,648 / 5,483 exact C
functions overall and 2,080 / 4,794 in Game.

## Source correction

The recovered algorithm was already correct: find the terminating byte with
`func_150CFD5C`, walk the intervening variable-length records with
`func_150CFD84`, and return the greatest record length. Its redundant local
copy of `arg0` gave IDO an extra saved-pointer lifetime and a 64-byte frame.

The source now initializes `max` before calling `func_150CFD5C`, declares the
out-pointer `next` at function scope, and advances `arg0` directly. IDO then
emits retail's 56-byte frame, spills incoming `a0` at `sp+0x38`, keeps `max`
in `s0`, `&next` in `s1`, and the end pointer in `s2`, and reproduces the
branch-likely maximum update with `next` at `sp+0x2C`. No guarded word-patch
rows were added. `retail_word_patches.us.csv` remains at 958 rows and has zero
duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xFD238` and retail span
`conker.us.bin+0xFD268` are both 132 bytes and compare equal. Both hash to:

`92b34be7efb8d87a2f94db2b9cffc4289391277d9be36a2670640e8065e7cb8e`

The focused object build, exhaustive `make -B -j2 NON_MATCHING=1`, fresh
linked matcher, outer nonmatching build, `make tools-check`, six project-tool
unit tests, and `git diff --check` all pass.

## Sibling audit

`64CBFDOGL` contains `func_150CFDB8` only in generated recompilation outputs
and declarations; there is no separate maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 23-word
`func_150CFE3C`, the first ordinary-C row in the fresh smallest-difference
queue. It copies the active buffer with `memcpy` and terminates the alternate
buffer at its current size; the linked matcher reports fifteen real
differences.
