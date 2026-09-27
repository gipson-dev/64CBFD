# Game secondary object-eligibility predicate match - 2026-09-27

## Result

`func_151028AC` is byte-exact across all 29 tracked words and 116 bytes at
`0x151028AC..0x15102920`. Fresh totals are 2,818 / 5,469 (51.53%) exact C
functions overall and 2,246 / 4,791 (46.88%) in Game.

## Recovery

The old source was a zero-return placeholder. This routine is the secondary
form of `func_1510281C`: it reads the object pointer from caller offset
`+0x170` and the final flag from `+0x174`, then applies the same selector,
nested-object, owner-byte `+0x197`, and low-bit eligibility checks.

The established source shape advances the object base by `0x110` and addresses
the selector at relative offset `+0x22`. IDO emits all 26 executable retail
words directly, including the signed halfword parameter narrowing and both
branch-likely delay-slot flag loads. The generated-slice padder retains the
three retail layout nops after the function, so the entire 29-word matcher
extent is exact without guarded retail words.

## Evidence

The rebuilt span at `build/conker.us.bin+0x12FD2C` and pristine retail span at
`conker.us.bin+0x12FD5C` compare equal for all 116 bytes. Both have SHA-256
`46ddfc72dd6c62c3641e2897081b79a165585a68b99e031779e04614fe1b8279`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,818 / 5,469 (51.53%) | 1 | 2,650 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,246 / 4,791 (46.88%) | 0 | 2,545 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 116-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,412 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 28-word Game `func_1510FE30`, the next ordinary unparked C row
in the fresh queue at 23 real differences. Keep the documented smaller
compiler, SDK, and ownership rows parked in their existing queues.
