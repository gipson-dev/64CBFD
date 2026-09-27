# Game event-bit updater twin match - 2026-09-27

## Result

`func_150D1BD0` is byte-exact across all 24 tracked words and 96 bytes at
`0x150D1BD0..0x150D1C30`. Fresh totals are 2,756 / 5,469 (50.39%) exact C
functions overall and 2,185 / 4,791 (45.61%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. It is the structural
twin of `func_150BB700`: retail queries
`func_1509BE40(1, 0x402C, 6, 0x2000)`. A nonzero result sets bit `0x10` in the
object word at offset `0x84`; zero clears the same bit.

The same typed pointer and direct set/clear expression reproduce the complete
retail body naturally. IDO emits the 0x18-byte frame, call setup and delay
slot, shared object-pointer load in the branch delay slot, both mask paths,
and epilogue without guarded words. Generated-slice padding preserves the two
retail zero words after the function body.

## Evidence

Linked ELF offset `0x111BD0` and decompressed retail offset `0xFF080` compare
equal across the complete 96-byte tracked span. Both have SHA-256
`2f7bbe6a8f54e13aca4d41dc1417f4f6b6f2af1c5181abfec7cfc76302499732`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,756 / 5,469 (50.39%) | 1 | 2,712 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,185 / 4,791 (45.61%) | 0 | 2,606 |
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

Continue with 22-word `func_150E411C`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
