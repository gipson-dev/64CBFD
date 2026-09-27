# Game indexed flag predicate match - 2026-09-27

## Result

`func_1503B95C` is byte-exact across all 24 words and 96 bytes at
`0x1503B95C..0x1503B9B8`. Fresh totals are 2,804 / 5,469 (51.27%) exact C
functions overall and 2,232 / 4,791 (46.59%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered function reads the
flag byte at `D_800CC5CB[index * 0x32C]`. Flag bit `0x02` clears byte `0x4E`
of the supplied record and returns zero. Bit `0x01` returns zero without that
mutation. A flag with both low bits clear returns one.

The `0x32C` indexed expression produces retail's complete nine-instruction
shift/add multiplication chain. Declaring the zero-extended flag as an `s32`
temporary keeps it in `v0`, reproducing the two masks, branches, three return
paths, and their delay slots directly. No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x68DDC` and pristine retail span at
`conker.us.bin+0x68E0C` compare equal for all 96 bytes. Both have SHA-256
`65a1b3ed7d8a1c961d3a7383c20d10959fbe356696bf0083283342ae4c56ca85`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,804 / 5,469 (51.27%) | 1 | 2,664 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,232 / 4,791 (46.59%) | 0 | 2,559 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,354 rows with zero duplicate keys.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_1503DA3C`, the first ordinary unparked C row
in the fresh queue at 23 real differences. It is a generated-slice placeholder
with preserved retail assembly. Keep the documented lower-difference ownership
and compiler/callback rows in their separate queues.
