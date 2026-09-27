# Game object state transition match - 2026-09-27

## Result

`func_15172D28` is byte-exact across all 22 words and 88 bytes at
`0x15172D28..0x15172D80`. Fresh totals are 2,772 / 5,469 (50.69%) exact C
functions overall and 2,201 / 4,791 (45.94%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail first calls
`func_15085430` with the object, caller-provided state, and constant one. It
then clears bit `0x10` from the halfword at object offset `0x2F8`. When global
mode byte `D_800BE9B4` is zero, it follows the pointer at object offset `0x31C`
and writes state `3` to byte offset `0x56` when that pointer is non-null.

The direct offset-based C reproduces retail's unsigned halfword mask, global
byte test, nested pointer test, both branch-likely early-return paths, repeated
return-address loads, and epilogue directly. No guarded retail words are
needed.

## Evidence

Linked ELF offset `0x1B2D28` and decompressed retail offset `0x1A01D8` compare
equal across the complete 88-byte span. Both have SHA-256
`f285d4661242ecf09be7ab29f754180e339c667a1036330afba8d6c07bd7473a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,772 / 5,469 (50.69%) | 1 | 2,696 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,201 / 4,791 (45.94%) | 0 | 2,590 |
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

Continue with 22-word `func_151749A0`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
