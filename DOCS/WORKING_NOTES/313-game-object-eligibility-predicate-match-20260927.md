# Game object-eligibility predicate match - 2026-09-27

## Result

`func_1510281C` is byte-exact across all 26 words and 104 bytes at
`0x1510281C..0x15102884`. Fresh totals are 2,817 / 5,469 (51.51%) exact C
functions overall and 2,245 / 4,791 (46.86%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered predicate reads
the object pointer at caller offset `+0xD0`, advances it to the embedded record
at `+0x110`, and compares the signed incoming selector against the byte at
original offset `+0x132`. A matching selector returns zero when the embedded
object is null or its owner byte `+0x197` is nonzero. All other surviving paths
return whether bit zero of caller byte `+0xD4` is set.

Expressing the selector as `base + 0x22` after advancing `base` by `0x110`
preserves the retail `v0` pointer lifetime. IDO then emits the complete retail
schedule directly, including the incoming halfword narrowing, both
branch-likely delay-slot loads, the nested `+0x31C` owner lookup, and all three
return paths. No guarded retail words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x12FC9C` and pristine retail span at
`conker.us.bin+0x12FCCC` compare equal for all 104 bytes. Both have SHA-256
`3d65ee6d48fdac7191cf7ff9857fd9e97d6e2fae1a47af955cf3aaa91cd57994`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,817 / 5,469 (51.51%) | 1 | 2,651 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,245 / 4,791 (46.86%) | 0 | 2,546 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 104-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,412 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with adjacent 29-word Game `func_151028AC`, an ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
