# Game nested state classifier match - 2026-09-27

## Result

`func_150EB030` is byte-exact across all 24 words and 96 bytes at
`0x150EB030..0x150EB090`. Fresh totals are 2,758 / 5,469 (50.43%) exact C
functions overall and 2,187 / 4,791 (45.65%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail returns `-1`
unless the first argument is mode one and `D_800BE9F0` is state four. In that
case it calls `func_151420F8` with the second argument and returns six for a
nonzero callback result or three for zero.

Straight nested conditions or early returns preserve the behavior but IDO
folds the default paths into branch-likely forms. Nested switches retain the
two independent default cases visible in retail. That source emits both `-1`
assignments, every branch and delay slot, callback call, result path, and the
epilogue directly, without guarded words.

## Evidence

Linked ELF offset `0x12B030` and decompressed retail offset `0x1184E0` compare
equal across the complete 96-byte span. Both have SHA-256
`a34d5679b8a478511f46b1d6f21549808b5c1acf81b6a79448e9440a81bb660b`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,758 / 5,469 (50.43%) | 1 | 2,710 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,187 / 4,791 (45.65%) | 0 | 2,604 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 96-byte span hashes, and `cmp` pass. The
repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and staged
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_150FB1E8`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
