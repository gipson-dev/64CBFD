# Game tagged table-value serializer match - 2026-09-27

## Result

`func_150B58F0` is byte-exact across all 24 words and 96 bytes at
`0x150B58F0..0x150B5950`. Fresh totals are 2,811 / 5,469 (51.40%) exact C
functions overall and 2,239 / 4,791 (46.73%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered routine returns
the output cursor unchanged when global mode byte `D_800C35EA` equals one. In
other modes it writes halfword tag `0x1A`, reads a halfword from global table
`D_800CC34A` at the incoming index's `0x32C`-byte record, writes that value,
and returns the output cursor advanced by four bytes.

The direct typed source reproduces both return schedules and IDO's exact
shift/add/sub strength reduction for multiplication by `0x32C`. It also emits
the retail global relocations, stores, table load, and cursor update without
any guarded words.

## Evidence

The rebuilt span at `build/conker.us.bin+0xE2D70` and pristine retail span at
`conker.us.bin+0xE2DA0` compare equal for all 96 bytes. Both have SHA-256
`f6d93c4607cecde125be160a07313bf365fe1f4ad166045b96596e0b31c52600`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,811 / 5,469 (51.40%) | 1 | 2,657 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,239 / 4,791 (46.73%) | 0 | 2,552 |
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

Continue with 24-word Game `func_150C1660`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
