# Game mode-dependent area scaler match - 2026-09-27

## Result

`func_15144598` is byte-exact across all 37 words and 148 bytes at
`0x15144598..0x1514462C`. Fresh totals are 2,767 / 5,469 (50.59%) exact C
functions overall and 2,196 / 4,791 (45.84%) in Game.

## Recovery

The existing C described the correct broad calculation but used stale
`struct134` fields. Retail selects a mode from byte offset `0x15`, not `0x16`,
and reads both dimensions at offsets `0x06` and `0x0A` as signed halfwords.
Modes `0` and `1` return the square of the first dimension scaled by
`D_800A5694`; mode `2` returns the product of both dimensions scaled by
`4.0f`; other modes return `1.0f`.

The corrected implementation uses explicit typed offsets locally rather than
changing the shared structure before its other consumers can be audited.
Placing case `2` before the shared `0/1` path reproduces retail's basic-block
layout. IDO evaluates integer multiplication operands right-to-left, so the
commutatively equivalent source order `dimensionA * dimension6` reproduces
retail's offset-`0x06` then offset-`0x0A` load schedule. Every word matches
directly from C; no guarded retail words are needed.

## Evidence

Linked ELF offset `0x184598` and decompressed retail offset `0x171A48` compare
equal across the complete 148-byte span. Both have SHA-256
`d24133a60d99d777e37a1986522ced2d3947226df1bf63479c3b2569cd62e7eb`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,767 / 5,469 (50.59%) | 1 | 2,701 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,196 / 4,791 (45.84%) | 0 | 2,595 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 148-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 25-word `func_15149BF4`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
