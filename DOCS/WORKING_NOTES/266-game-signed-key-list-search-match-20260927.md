# Game signed-key list search match - 2026-09-27

## Result

`func_1514ECE0` is byte-exact across all 23 words and 92 bytes at
`0x1514ECE0..0x1514ED3C`. Fresh totals are 2,769 / 5,469 (50.63%) exact C
functions overall and 2,198 / 4,791 (45.88%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail walks a linked
list through the pointer at node offset `0x14`, compares the signed halfword at
offset `0x1C` with the requested key, and optionally writes the matching node
through the third argument. It returns one when a match is found and zero when
the list is exhausted.

The neighboring recovered `func_1514ED3C` has the same control flow but
compares the 32-bit field at offset `0x10`. Reusing its structured loop with a
typed `s16` key reproduces retail's argument sign extension, branch-likely
loop, delay slots, and shared return path directly from C. No guarded retail
words are needed.

## Evidence

Linked ELF offset `0x18ECE0` and decompressed retail offset `0x17C190` compare
equal across the complete 92-byte span. Both have SHA-256
`b86fa571f8372f319a0e24df91da420b10ef6e0d1478b06f8741b62923391112`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,769 / 5,469 (50.63%) | 1 | 2,699 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,198 / 4,791 (45.88%) | 0 | 2,593 |
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

Continue with 22-word `func_15159BB0`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
