# Game dimension/ratio setup match - 2026-09-26

## Result

`func_150492CC` is byte-exact across all 33 words at
`0x150492CC..0x15049350`. The linked matcher reports 2,654 / 5,483 exact C
functions overall and 2,086 / 4,794 in Game.

## Recovered behavior

The existing C behavior is correct. The function stores its three float inputs
in `D_800CC220..D_800CC228`, stores each input divided by `2.0f` in
`D_800CC22C..D_800CC234`, and writes the second and third inputs divided by
the first to `D_800CC238` and `D_800CC23C`. If the first input is zero,
`D_80099080` supplies the ratio divisor.

IDO strength-reduces each direct division by `2.0f` to multiplication by a
shared `0.5f` constant. A named local divisor is also constant-propagated to
the same output, so the source remains in its clear direct-division form.

Sixteen guarded rows restore retail's `2.0f` constant, all three `div.s`
operations, the interleaved input/half-value stores, and their address
materialization schedule. The moved `D_800CC220`, `D_800CC224`, `D_800CC228`,
`D_800CC22C`, and `D_800CC230` relocation pairs are declared explicitly;
the later `D_800CC234`, fallback, ratio, and return words already match. The
patch table now contains 1,014 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x7674C` and retail span
`conker.us.bin+0x7677C` are both 132 bytes and compare equal. Both hash to:

`448c8fe7e5a9c01b83513bdec305fb3a25c03b2242ea84b80e7d981696d5666a`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all six
project-tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_150492CC` in generated symbol lists, two generated
multiplayer-collision call sites, and a focused test stub. There is no separate
maintained host implementation to update. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`, plus init-owned
`osMapTLBRdb`. Continue with 17-word `func_150721A4`, the first Game C row in
the remaining 16-difference queue. Its live C unpacks three bytes from
`D_800D1580` and forwards them with `D_800D154C` to `func_1506160C`; an
assembly reference is retained because IDO stages the packed-byte arguments
differently. The linked matcher reports sixteen real differences.
