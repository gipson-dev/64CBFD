# Game position/effect wrapper match - 2026-09-27

## Result

`func_151B4E4C` is byte-exact across all 22 words and 88 bytes at
`0x151B4E4C..0x151B4EA4`. Fresh totals are 2,782 / 5,469 (50.87%) exact C
functions overall and 2,211 / 4,791 (46.15%) in Game.

## Recovery

The false zero-return placeholder now uses the same established wrapper idiom
as nearby `func_151B50A4`. It stores the first three float arguments in a local
position vector, forwards the next three floats, and supplies bytes `0x58` and
`0x0C` from the final actor record to `func_151B4EA4`.

Typing the six-argument callee restores the correct floating-point and stack
ABI. The direct C emits retail's 48-byte frame, incoming argument homes,
three vector stores, actor-byte loads, stack arguments, call relocation, and
epilogue without guarded retail words. The still-unrecovered callee remains a
separate nonmatching row.

## Evidence

Linked ELF offset `0x1F4E4C` and decompressed retail offset `0x1E22FC` compare
equal across the complete 88-byte span. Both have SHA-256
`9636d4a1dfde42444c22687e8308ebb8e17535d14b38bb150bd9a1628d5d31f3`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,782 / 5,469 (50.87%) | 1 | 2,686 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,211 / 4,791 (46.15%) | 0 | 2,580 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and relocation-aware disassembly, nonmatching linked
ELF build, fresh progress and matcher, independent 88-byte hashes, and direct
byte comparison pass. The padded replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_151EFF94`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
