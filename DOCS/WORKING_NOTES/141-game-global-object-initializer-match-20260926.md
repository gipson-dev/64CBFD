# Game global/object initializer match - 2026-09-26

## Result

`func_150104F0` is byte-exact across all 18 words at
`0x150104F0..0x15010538`. The linked matcher reports 2,653 / 5,483 exact C
functions overall and 2,085 / 4,794 in Game.

## Source correction

The function clears bytes `0..2` of `D_800D9950`, obtains object `0xF6`
through `func_151149AC`, writes `2.0f` at object offset `0x7C`, and clears
`D_80088980`.

The first two byte clears are now expressed as the right-to-left assignment
chain `D_800D9950[0] = D_800D9950[1] = 0`, preserving retail's store order.
IDO still discards the assignment result and keeps the global base in `v0`;
retail retains the result as zero in `v0` and therefore keeps the base in
`v1`. The third byte clear remains a direct zero store.

Six guarded rows restore that shape: two relocation-preserving base-register
words, one unchanged `ra` save with an inserted `v0 = 0`, and three byte-store
register choices. Every later call, float write, global relocation, and
epilogue word then shifts into its exact retail position without further
normalization. The patch table now contains 998 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x3D970` and retail span
`conker.us.bin+0x3D9A0` are both 72 bytes and compare equal. Both hash to:

`4490ec7ef2aa200e85afeb89209471955c5b3bc3713b2e57cd873bfafbf11db1`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all six
project-tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_150104F0` only in generated symbol lists; there is
no separate maintained host implementation to update. Its 1,659 existing
dirty entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`, plus init-owned
`osMapTLBRdb`. Continue with 33-word `func_150492CC`, the first ordinary Game
C row in the fresh 16-difference queue. It stores three input dimensions,
their half values, and two ratios; when the first dimension is zero, it uses
`D_80099080` as the divisor. The linked matcher reports sixteen real
differences.
