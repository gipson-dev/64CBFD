# Game wrapped timer counter match - 2026-09-27

## Result

`func_151749A0` is byte-exact across all 22 words and 88 bytes at
`0x151749A0..0x151749F8`. Fresh totals are 2,773 / 5,469 (50.70%) exact C
functions overall and 2,202 / 4,791 (45.96%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail adds global frame
delta `D_800BE9E4` to byte timer `D_800DD406`, preserving byte wrapping. When
the wrapped timer exceeds the caller's first limit, byte counter `D_800DD405`
is incremented. The counter resets at the caller's second limit, and the timer
is cleared after every threshold crossing.

Declaring both globals as `u8` makes IDO emit retail's explicit `0xFF` masks
before both signed threshold comparisons. The direct nested C also reproduces
the timer store in the outer branch delay slot and the counter store in the
inner branch delay slot. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x1B49A0` and decompressed retail offset `0x1A1E50` compare
equal across the complete 88-byte span. Both have SHA-256
`1ef04391b9f03b0528bc0f1c4f9d39ed6df05e2f7125a49e456853d8507445cd`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,773 / 5,469 (50.70%) | 1 | 2,695 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,202 / 4,791 (45.96%) | 0 | 2,589 |
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

Continue with 22-word `func_1517F75C`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
