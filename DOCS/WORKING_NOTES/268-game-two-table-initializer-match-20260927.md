# Game two-table initializer match - 2026-09-27

## Result

`func_15172C50` is byte-exact across all 22 words and 88 bytes at
`0x15172C50..0x15172CA8`. Fresh totals are 2,771 / 5,469 (50.67%) exact C
functions overall and 2,200 / 4,791 (45.92%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail initializes 16
corresponding bytes in two global tables: each `D_800DD2B0` entry becomes
`-1`, and each `D_800DD2C0` entry becomes zero. It then writes the caller's
value to `D_800DD2C0[0]`.

The apparent four-byte record loop in retail is IDO's four-way unroll of a
simple 16-entry source loop. Expressing four assignments in the C body causes
IDO to unroll that body again, while a pointer-bounded byte loop adds a generic
remainder peel. The fixed 16-entry indexed loop gives the compiler the exact
trip count and reproduces retail's pointer induction, deferred offset-zero
stores, endpoint address, and branch delay slot directly from C. No guarded
retail words are needed.

## Evidence

Linked ELF offset `0x1B2C50` and decompressed retail offset `0x1A0100` compare
equal across the complete 88-byte span. Both have SHA-256
`276590b6fd1af72abb45e1b76d352b988397165f8e9a5e69598a41a213e8465a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,771 / 5,469 (50.67%) | 1 | 2,697 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,200 / 4,791 (45.92%) | 0 | 2,591 |
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

Continue with 22-word `func_15172D28`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
