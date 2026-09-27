# Game event-bit updater match - 2026-09-27

## Result

`func_150BB700` is byte-exact across all 24 tracked words and 96 bytes at
`0x150BB700..0x150BB760`. Fresh totals are 2,755 / 5,469 (50.37%) exact C
functions overall and 2,184 / 4,791 (45.59%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail queries
`func_1509BE40(1, 0x4047, 6, 0x2000)`. A nonzero result sets bit `0x1000` in
the object word at offset `0x84`; zero clears the same bit.

The typed pointer and direct set/clear expression reproduce the complete
retail body naturally. IDO emits the 0x18-byte frame, four call arguments,
call delay slot, shared object-pointer load in the conditional branch delay
slot, both mask paths, and epilogue without guarded words. The generated-slice
padding also preserves the two retail zero words after the function body.

## Evidence

Linked ELF offset `0xFB700` and decompressed retail offset `0xE8BB0` compare
equal across the complete 96-byte tracked span. Both have SHA-256
`120ebe1a5434d337d45ad6cfdf8bc0db6e532efd860f38b9dee810c45f9b6204`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,755 / 5,469 (50.37%) | 1 | 2,713 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,184 / 4,791 (45.59%) | 0 | 2,607 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 96-byte span hashes, and `cmp` pass. The
repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and staged
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word `func_150D1BD0`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
