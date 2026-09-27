# Game actor parameter initializer match - 2026-09-27

## Result

`func_150FB188` is byte-exact across all 24 words and 96 bytes at
`0x150FB188..0x150FB1E8`. Fresh totals are 2,816 / 5,469 (51.49%) exact C
functions overall and 2,244 / 4,791 (46.84%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered routine writes
`-95.0f`, `-80.0f`, and `0.0f` to actor offsets `+0x54`, `+0x58`, and `+0x5C`.
It builds a five-float stack record containing three zeros followed by two
copies of `D_800A1DC0`, passes that record to `func_15157DEC`, and returns one.

Typed C reproduces retail's 48-byte frame, saved return address, two actor
constants, five stack fields, call, delay-slot parameter pointer, and return
sequence in the exact 24-word extent. Seventeen guarded words normalize only
the compiler's independent instruction schedule, `f0`/`f2` lifetimes, and the
relocation-preserving movement of the `D_800A1DC0` address pair.

## Evidence

The rebuilt span at `build/conker.us.bin+0x128608` and pristine retail span at
`conker.us.bin+0x128638` compare equal for all 96 bytes. Both have SHA-256
`01144cdde22851e6ac89ae165b93f105ed789a3d297fd0e77e9773a11973a827`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,816 / 5,469 (51.49%) | 1 | 2,652 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,244 / 4,791 (46.84%) | 0 | 2,547 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table now has
1,412 rows with zero duplicate keys; seventeen belong to this function.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 26-word Game `func_1510281C`, the next ordinary unparked C row in
the fresh 23-real-difference queue. Keep the documented smaller compiler, SDK,
and ownership rows parked in their existing queues.
