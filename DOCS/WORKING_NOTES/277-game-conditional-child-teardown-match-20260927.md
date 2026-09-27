# Game conditional child teardown match - 2026-09-27

## Result

`func_151A09B4` is byte-exact across all 23 words and 92 bytes at
`0x151A09B4..0x151A0A10`. Fresh totals are 2,781 / 5,469 (50.85%) exact C
functions overall and 2,210 / 4,791 (46.13%) in Game.

## Recovery

The false zero-return placeholder now recovers the original conditional child
teardown. The routine narrows its third argument to a byte, follows the object
links at offsets `0x28` and `0x18`, and returns immediately when the byte flag
is nonzero. With a zero flag, it continues when either the child pointer equals
the selector record's first word or child byte `0x3B` equals selector byte 4.
The accepted path calls `func_151A0928` and then `func_1516972C` on the object.

The direct short-circuit C expression reproduces retail's argument home and
narrowing, loaded branch delay slot, pointer comparison, branch-likely return,
object spill/reload, callback relocations, and epilogue. No guarded retail
words are needed.

## Evidence

Linked ELF offset `0x1E09B4` and decompressed retail offset `0x1CDE64` compare
equal across the complete 92-byte span. Both have SHA-256
`93bbe71ba0637f3ea71c346fa823b4f50f42adc38d076a45ae4ffa286dd09e22`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,781 / 5,469 (50.85%) | 1 | 2,687 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,210 / 4,791 (46.13%) | 0 | 2,581 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and relocation-aware disassembly, nonmatching linked
ELF build, fresh progress and matcher, independent 92-byte hashes, and direct
byte comparison pass. The padded replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 22-word `func_151B4E4C`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
