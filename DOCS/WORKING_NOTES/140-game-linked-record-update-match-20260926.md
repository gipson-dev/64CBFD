# Game linked-record update match - 2026-09-26

## Result

`func_151D2E5C` is byte-exact across all 41 words at
`0x151D2E5C..0x151D2F00`. The linked matcher reports 2,652 / 5,483 exact C
functions overall and 2,084 / 4,794 in Game.

## Source correction

Selector `0` compares the linked record's pointer and byte identifiers. Retail
passes the owning `struct16 *arg0` to `func_1516972C` when either identifier
matches. The previous C incorrectly passed the byte at `arg0->unk14`, changing
the call ABI and forcing the surrounding values into different registers.

The call now forwards `arg0`. Explicit `temp_v0`, `temp_v1`, `temp_a2`, and
`temp_a3` locals recover retail's `v0`/`v1` and `a2`/`a3` lifetimes for the
selector-0 comparisons, while reuse of the two word locals restores the
entire selector-`0x2D` endpoint-rewiring schedule. Reversing the two
commutative source equalities recovers retail's operand order except for the
second branch, which IDO canonicalizes back to `v1,t9`.

One guarded row at function offset `0x80` changes only that commutative branch
operand order to retail's `t9,v1`; no instruction is inserted and no
relocation moves. The patch table now contains 992 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x2002DC` and retail span
`conker.us.bin+0x20030C` are both 164 bytes and compare equal. Both hash to:

`381b3f7b4eb91412a7c92dff5af51baab45b2fbb64fcd786d0629d9d68fdd063`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all six
project-tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_151D2E5C` only in generated symbol lists; there is
no separate maintained host implementation to update. Its 1,659 existing
dirty entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`, plus init-owned
`osMapTLBRdb`. Continue with 18-word `func_150104F0`, the first ordinary Game
C row in the fresh 16-difference queue. It clears `D_800D9950[0..2]`, obtains
object `0xF6` through `func_151149AC`, writes `2.0f` at object offset `0x7C`,
and clears `D_80088980`; the linked matcher reports sixteen real differences.
