# Game scaled query wrapper match - 2026-09-27

## Result

`func_15197A0C` is byte-exact across all 23 words and 92 bytes at
`0x15197A0C..0x15197A68`. Fresh totals are 2,778 / 5,469 (50.80%) exact C
functions overall and 2,207 / 4,791 (46.07%) in Game.

## Recovery

The maintained computation was already correct: it calls `func_151422C0`
with the retail constants and data addresses, converts the integer result to
float, and scales it by `D_800A8AA8`. The signature incorrectly declared no
arguments, so IDO omitted retail's incoming `a0` home at `sp + 0x20` and every
following instruction appeared shifted by one word.

Restoring the unused `s32 arg0` parameter emits that home and makes the entire
function exact directly from C. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x1D7A0C` and decompressed retail offset `0x1C4EBC` compare
equal across the complete 92-byte span. Both have SHA-256
`79e00b19930e3d83d5baf14d43868c3332e63a76de73d420b1f301259a31d872`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,778 / 5,469 (50.80%) | 1 | 2,690 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,207 / 4,791 (46.07%) | 0 | 2,584 |
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

Continue with 24-word `func_1519F108`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
