# Game indexed-record reset match - 2026-09-27

## Result

`func_1512D6F0` is byte-exact across all 22 words and 88 bytes at
`0x1512D6F0..0x1512D748`. Fresh totals are 2,765 / 5,469 (50.56%) exact C
functions overall and 2,194 / 4,791 (45.79%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail reads the actor's
record index byte at offset `0x23D` and selects a 104-byte entry from table
`D_800DC2C0`. It writes state `5` at record offset `0x50`, clears the float
fields at offsets `0x54`, `0x58`, `0x5C`, `0x60`, and `0x2C`, then writes
`-1.0f` at offset `0x28`.

A file-local record definition captures the known field layout and complete
104-byte stride. Direct array indexing reproduces retail's shift/subtract
multiply-by-104 sequence, while ordered field assignments reproduce the float
constant materialization and all stores. Every instruction matches directly
from C; no guarded retail words are needed.

## Evidence

Linked ELF offset `0x16D6F0` and decompressed retail offset `0x15ABA0` compare
equal across the complete 88-byte span. Both have SHA-256
`de1fcbdbd7ec11e4aabe92c6ce6a332173b326d729cafdc4d5e2978c56a0c6cc`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,765 / 5,469 (50.56%) | 1 | 2,703 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,194 / 4,791 (45.79%) | 0 | 2,597 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 88-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word `func_1513BA78`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
