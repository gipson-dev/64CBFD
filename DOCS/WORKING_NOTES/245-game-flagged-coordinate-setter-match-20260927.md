# Game flagged coordinate setter match - 2026-09-27

## Result

`func_15022190` is byte-exact across all 22 words and 88 bytes at
`0x15022190..0x150221E8`. Fresh totals are 2,748 / 5,469 (50.25%) exact C
functions overall and 2,177 / 4,791 (45.44%) in Game.

## Recovery

The function is the flagged twin of the adjacent recovered `func_150221E8`.
It stores three signed 16-bit arguments in `D_800C358C`, stores the float
fourth argument in `D_800C3594`, and sets byte `D_800C3663` to one.

The direct `void (s16, s16, s16, f32)` C signature reproduces retail's
incoming argument home stores and explicit sign-extension sequence. IDO emits
the complete function without expected-word guards, including all four global
relocation pairs and the flag write.

## Evidence

Linked ELF offset `0x62190` and decompressed retail offset `0x4F640` compare
equal across the complete 88-byte span. Both have SHA-256
`4313640b5a0c843e78e6ee6bbc03b7a274102f6275f51c7d3d02c499b485783a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,748 / 5,469 (50.25%) | 1 | 2,720 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,177 / 4,791 (45.44%) | 0 | 2,614 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 88-byte span hashes, and `cmp` pass. The combined closing
replacement build, project tool checks, all seven padding-tool unit tests,
outer `NON_MATCHING=1` build, and staged `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word `func_15023870`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the previously documented
lower-difference rows parked.
