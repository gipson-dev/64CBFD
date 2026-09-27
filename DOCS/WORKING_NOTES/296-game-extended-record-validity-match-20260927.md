# Game extended record validity match - 2026-09-27

## Result

`func_151C2E94` is byte-exact across all 23 words and 92 bytes at
`0x151C2E94..0x151C2EEC`. Fresh totals are 2,800 / 5,469 (51.20%) exact C
functions overall and 2,229 / 4,791 (46.52%) in Game.

## Recovery

The zero-return placeholder was a two-pointer record validity predicate. It
returns zero when the candidate and comparison pointers are equal, when the
candidate's leading 32-bit word is zero, when its ID byte at offset 4 is
`0xFF`, or when its extended ID byte at offset `0x127` is `0xFF`. A candidate
that passes all four checks returns one.

This is the neighboring `func_151C2E4C` predicate with the final extended-ID
sentinel check added. The same sequence of source-level early returns makes
IDO reproduce retail's branch-likely chain, duplicated loads in the branch
delay/fallthrough slots, shared `0xFF` value in `v0`, and final return path.

The complete function matches directly from C. No guarded instruction rows or
assembly replacements are required.

## Evidence

Linked ELF file offset `0x202E94` and decompressed retail offset `0x1F0344`
compare equal across the complete 92-byte span. Both have SHA-256
`3d887e9020b87ba223d5866416343f7fee5008bd84f8b0cfd34f972166b65edb`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,800 / 5,469 (51.20%) | 1 | 2,668 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,229 / 4,791 (46.52%) | 0 | 2,562 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 92-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
none of its files were changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 34-word `func_151DADA0`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Its current C already
models the byte phase update and two scaled floating-point fields, so begin by
comparing its linked register schedule and expression lifetimes against retail.
