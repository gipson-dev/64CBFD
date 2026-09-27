# Game indexed callback dispatch match - 2026-09-27

## Result

`func_151A9060` is byte-exact across all 24 words and 96 bytes at
`0x151A9060..0x151A90BC`. Fresh totals are 2,799 / 5,469 (51.18%) exact C
functions overall and 2,228 / 4,791 (46.50%) in Game.

## Recovery

The zero-return placeholder was an object callback dispatcher. It first sets
bit `0x04` in the byte at object offset `0x16`, then reads the signed table
index at offset `0x18`. Negative indices and indices of eight or greater skip
the dispatch and return one. An in-range index selects an entry from
`D_8008F984`; a nonnull entry is called before the function returns one.

The table callback takes both the object and validated index. That second
argument is the key compiler-shape evidence: it keeps the index in `a1` across
the bounds checks and selects `v0` for the callback pointer, exactly matching
retail's indirect call sequence. A one-argument callback model was
behaviorally incomplete and instead allocated the index to `v0` and callback
to `v1`.

The complete function matches directly from C. No guarded instruction rows or
assembly replacements are required.

## Evidence

Linked ELF file offset `0x1E9060` and decompressed retail offset `0x1D6510`
compare equal across the complete 96-byte span. Both have SHA-256
`f1dcb7d5d51145eba852cfa5ddc264f455e842703946e1ae431d42affd7d0c64`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,799 / 5,469 (51.18%) | 1 | 2,669 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,228 / 4,791 (46.50%) | 0 | 2,563 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 96-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
none of its files were changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word `func_151C2E94`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler and assembly cases parked unless new source or
compiler evidence appears.
