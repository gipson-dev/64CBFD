# Game type-and-flag dispatcher match - 2026-09-27

## Result

`func_150FFD2C` is byte-exact across all 22 words and 88 bytes at
`0x150FFD2C..0x150FFD84`. Fresh totals are 2,761 / 5,469 (50.48%) exact C
functions overall and 2,190 / 4,791 (45.71%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail treats the second
argument as a byte-addressed record. Types `0x9F` and `0xA0` are eligible; if
bit `0x80` in the word at offset `0x94` is clear, the routine calls
`func_15081E0C(record, 4, 0)`. All other cases return without dispatching.

The three-argument `void` signature preserves retail's homes for unused
`arg0` and `arg2`. A cached type byte and the direct compound condition emit
the original single load, type tests, flag test, branch-likely epilogues, and
call delay slot without guarded words.

## Evidence

Linked ELF offset `0x13FD2C` and decompressed retail offset `0x12D1DC` compare
equal across the complete 88-byte span. Both have SHA-256
`c113b829b96bfe97ffb7840abe7e9089b81c411b9dd423f97da89628aeb6300c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,761 / 5,469 (50.48%) | 1 | 2,707 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,190 / 4,791 (45.71%) | 0 | 2,601 |
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

Continue with 23-word `func_151076A4`, the first unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
