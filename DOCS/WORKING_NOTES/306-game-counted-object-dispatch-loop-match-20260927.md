# Game counted object-dispatch loop match - 2026-09-27

## Result

`func_1508434C` is byte-exact across all 24 words and 96 bytes at
`0x1508434C..0x150843AC`. Fresh totals are 2,810 / 5,469 (51.38%) exact C
functions overall and 2,238 / 4,791 (46.71%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered routine reads the
unsigned count byte at object offset `0x2C9`, substitutes one when the stored
count is zero, and calls `func_150843AC(object, index)` once for each index from
zero through count minus one.

The direct source loop reproduces retail's 40-byte frame, retained object,
count, and index registers, zero-to-one normalization, empty-loop guard, call
delay slot, increment, branch-likely post-test, object reload, and epilogue.
No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0xB17CC` and pristine retail span at
`conker.us.bin+0xB17FC` compare equal for all 96 bytes. Both have SHA-256
`83fcda040d8f514bb3346c5db1daf2b45d2f74d998f6dd88fca5175461716227`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,810 / 5,469 (51.38%) | 1 | 2,658 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,238 / 4,791 (46.71%) | 0 | 2,553 |
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

Continue with 24-word Game `func_150B58F0`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
