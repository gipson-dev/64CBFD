# Game active-buffer copy match - 2026-09-26

## Result

`func_150CFE3C` is byte-exact across all 23 words at
`0x150CFE3C..0x150CFE98`. The linked matcher reports 2,649 / 5,483 exact C
functions overall and 2,081 / 4,794 in Game.

## Source correction

The function copies `arg0[0x3C]` bytes from the source pointer at object
offset `0x34` to the active output pointer selected by byte `0x3D` from the
pointer array beginning at offset `0x40`. It then NUL-terminates the active
buffer in the nested state at object offset `0x28`.

A typed `BufferState` records that nested layout: current size and active
index are bytes at nested offsets `0x14` and `0x15`, and the two buffer
pointers begin at nested offset `0x18`. This removes repeated untyped pointer
arithmetic and preserves the recovered behavior.

IDO still folds the nested-state base into the later loads. Six guarded rows
restore retail's object-base add order, retain the explicit `arg0 + 0x28`
calculation after the object reload, and select the nested base and offsets
for the index, size, pointer-array index, and active-pointer load. The patch
table now contains 964 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xFD2BC` and retail span
`conker.us.bin+0xFD2EC` are both 92 bytes and compare equal. Both hash to:

`54f23549a68d0a118376c4e2c6448428d31c37c0cdcd10e1099075a64f5c28a8`

The exhaustive `make -j2 NON_MATCHING=1` rebuild covered every consumer of
the shared patch table and passed. The fresh linked matcher, exact span
comparison, outer nonmatching build, `make tools-check`, and all six project
tool unit tests also pass.

## Sibling audit

`64CBFDOGL` contains `func_150CFE3C` only in generated recompilation outputs
and declarations; there is no separate maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 23-word
`func_15167010`, the first ordinary-C row in the fresh smallest-difference
queue. It walks the fixed `struct115` table from `D_8008B4A8` through
`D_8008B4A8 + 0x1484` and invokes each non-null callback at record offset
`0x18`; the linked matcher reports fifteen real differences.
