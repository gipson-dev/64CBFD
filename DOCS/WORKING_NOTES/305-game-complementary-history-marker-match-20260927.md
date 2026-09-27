# Game complementary history-marker match - 2026-09-27

## Result

`func_1507EE58` is byte-exact across all 24 words and 96 bytes at
`0x1507EE58..0x1507EEB8`. Fresh totals are 2,809 / 5,469 (51.36%) exact C
functions overall and 2,237 / 4,791 (46.69%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered wrapper first
passes the incoming marker byte and five-byte history pointer to
`func_1507EEB8`, which shifts the existing history and inserts the marker. If
the marker is `0x11`, the wrapper inserts complementary marker `0x12`; if it is
`0x12`, the wrapper inserts complementary marker `0x11`.

Correcting the signature to `void (u8, u8 *)` reproduces retail's incoming
argument spill and low-byte reload. The direct `if`/`else if` source shape emits
both branch-likely comparisons, all three calls and delay slots, and the shared
epilogue exactly. No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0xAC2D8` and pristine retail span at
`conker.us.bin+0xAC308` compare equal for all 96 bytes. Both have SHA-256
`1d32e38706b456f78bb80f1980911262f13dc972b5e4ed4fd73191b10743c01f`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,809 / 5,469 (51.36%) | 1 | 2,659 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,237 / 4,791 (46.69%) | 0 | 2,554 |
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

Continue with 24-word Game `func_1508434C`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
