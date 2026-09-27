# Game player timer decay match - 2026-09-27

## Result

`func_1517F75C` is byte-exact across all 22 words and 88 bytes at
`0x1517F75C..0x1517F7B4`. Fresh totals are 2,774 / 5,469 (50.72%) exact C
functions overall and 2,203 / 4,791 (45.98%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail iterates from
player index zero through `D_80082FA0`, inclusive, over unsigned halfword timer
array `D_800DDE10`. Each timer is reduced by global frame delta `D_800BE9E4`
when it is larger than the delta; otherwise it is clamped to zero.

The natural indexed C loop makes IDO convert the inclusive index bound into a
pointer to the final halfword. It reproduces retail's negative-player-count
early exit, unsigned halfword load, subtract-or-zero branch, unsigned end
pointer comparison, and branch-likely next-element load directly. No guarded
retail words are needed.

## Evidence

Linked ELF offset `0x1BF75C` and decompressed retail offset `0x1ACC0C` compare
equal across the complete 88-byte span. Both have SHA-256
`4c14539ad1ebebefc3d10023afc401e7b495ec1001efaf6d0ef4ad5cbc26c7c3`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,774 / 5,469 (50.72%) | 1 | 2,694 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,203 / 4,791 (45.98%) | 0 | 2,588 |
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

Continue with 22-word `func_15181D70`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
