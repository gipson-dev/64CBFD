# Game script-gated high-flag match - 2026-09-27

## Result

`func_150F52B0` is byte-exact across all 24 words and 96 bytes at
`0x150F52B0..0x150F5310`. Fresh totals are 2,815 / 5,469 (51.47%) exact C
functions overall and 2,243 / 4,791 (46.82%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered wrapper calls the
variable-argument script dispatcher as `func_1509BE40(1, 0x401C, 6, 0x9000)`.
A nonzero result sets bit 31 of actor word `+0x84`; a zero result clears it.

The direct branch reproduces retail's 24-byte frame, saved incoming pointer,
four constant arguments, `0x9000` call delay slot, branch-delay pointer reload,
high-bit set/clear materialization, and shared epilogue. No guarded words are
used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x122730` and pristine retail span at
`conker.us.bin+0x122760` compare equal for all 96 bytes. Both have SHA-256
`101a6dbcb8cea8393fd0b05a1b1b5018023f189c8b26d6ef52fcdd77a01a49e1`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,815 / 5,469 (51.47%) | 1 | 2,653 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,243 / 4,791 (46.82%) | 0 | 2,548 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,395 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_150FB188`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
