# Game parameter preset match - 2026-09-27

## Result

`func_150E411C` is byte-exact across all 22 words and 88 bytes at
`0x150E411C..0x150E4174`. Fresh totals are 2,757 / 5,469 (50.41%) exact C
functions overall and 2,186 / 4,791 (45.63%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail forwards its
incoming object to `func_151C3B0C` with three float parameters encoded as
`0x3EB43959`, `0x3F3374BD`, and `0x3F10E561`, global float `D_800A1054`, and
three trailing `0xFF` values.

The initial short decimal spellings rounded each immediate float one ULP low.
Using the exact single-precision decimal values `0.352000028f`,
`0.701000035f`, and `0.566000044f` reproduces the retail words. IDO then emits
the complete frame, global HI16/LO16 relocation pair, immediate loads,
stack-argument stores, call delay slot, and epilogue without guards.

## Evidence

Linked ELF offset `0x12411C` and decompressed retail offset `0x1115CC` compare
equal across the complete 88-byte span. Both have SHA-256
`7719be748c7a2baa8892764bce224f70933275986384d391a4c0ed4dc0d77167`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,757 / 5,469 (50.41%) | 1 | 2,711 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,186 / 4,791 (45.63%) | 0 | 2,605 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 88-byte span hashes, and `cmp` pass. The
repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and staged
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word `func_150EB030`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
