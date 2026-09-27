# Game mapped record-active predicate match - 2026-09-27

## Result

`func_150DF8C0` is byte-exact across all 24 words and 96 bytes at
`0x150DF8C0..0x150DF920`. Fresh totals are 2,813 / 5,469 (51.44%) exact C
functions overall and 2,241 / 4,791 (46.78%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered predicate copies
the three-byte rodata map at `D_80088984` onto its local stack object, maps the
incoming index through values `0x3B`, `0x3C`, and `0x3D`, selects the matching
`0x34`-byte record from runtime table pointer `D_800D3098`, and returns whether
record byte `+0x14` is nonzero.

Typing the map as a three-byte object preserves retail's `lwr`/`swr` stack
copy and relocations; a compiler-owned initializer produced the same words in
the focused object but correctly failed the full link because its private data
section is discarded. Typing the destination record reproduces retail's exact
strength reduction and temporary-register lifetimes. No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x10CD40` and pristine retail span at
`conker.us.bin+0x10CD70` compare equal for all 96 bytes. Both have SHA-256
`f561e7c6bf079ec34a150cf8de10d548606801d1bed3893c687a8c0cde77242b`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,813 / 5,469 (51.44%) | 1 | 2,655 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,241 / 4,791 (46.78%) | 0 | 2,550 |
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

Continue with 24-word Game `func_150F1CB0`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
