# Game volatile callback-table dispatch match - 2026-09-27

## Result

`func_151076A4` is byte-exact across all 23 words and 92 bytes at
`0x151076A4..0x15107700`. Fresh totals are 2,762 / 5,469 (50.50%) exact C
functions overall and 2,191 / 4,791 (45.73%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail indexes callback
table `D_80088C38` with the byte at record offset `0x68`. A non-null entry is
called with the original record, scalar argument, and normalized byte
argument; a null entry returns without dispatching.

Unlike the nearby retained-callback dispatcher, retail reads both the index
byte and callback-table entry again for the call. Declaring the callback
entries volatile and reading the index through a volatile byte pointer gives
those accesses their observed source-level meaning. A local table-base pointer
then reproduces retail's `v0` lifetime and all instruction scheduling directly
from C without guarded words.

## Evidence

Linked ELF offset `0x1476A4` and decompressed retail offset `0x134B54` compare
equal across the complete 92-byte span. Both have SHA-256
`c4ea7c4b5b4970d6a3c01f5e3a1695c86e46f09cf002f4750c56d9d6024a18db`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,762 / 5,469 (50.50%) | 1 | 2,706 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,191 / 4,791 (45.73%) | 0 | 2,600 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 92-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word `func_1510A870`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
