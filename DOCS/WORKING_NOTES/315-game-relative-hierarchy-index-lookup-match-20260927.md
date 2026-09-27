# Game relative hierarchy-index lookup match - 2026-09-27

## Result

`func_1510FE30` is byte-exact across all 28 tracked words and 112 bytes at
`0x1510FE30..0x1510FEA0`. Fresh totals are 2,819 / 5,469 (51.55%) exact C
functions overall and 2,247 / 4,791 (46.90%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered routine traverses
a relative-offset hierarchy rooted at `D_800DBE48`. It returns the current
index when it finds the requested node. A signed halfword at node offset
`+0xC` descends to another node without changing that index. When no child is
present, the signed halfword at `+0x4` advances to a sibling and increments the
index. A zero sibling offset terminates the search, which returns zero.

Using a post-tested pointer loop reproduces retail's early target return and
both branch-likely offset loads. Applying the sibling offset before testing it
lets IDO schedule the pointer addition in the zero-test delay slot, followed by
the sibling increment in the unconditional-branch delay slot. The resulting C
emits all 25 executable words directly, while generated-slice padding preserves
the three trailing layout nops. No guarded retail words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x13D2B0` and pristine retail span at
`conker.us.bin+0x13D2E0` compare equal for all 112 bytes. Both have SHA-256
`3c50f9175be4aac89031574212071c25c6da4d7a2c0fb0759961dc2ad1761d74`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,819 / 5,469 (51.55%) | 1 | 2,649 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,247 / 4,791 (46.90%) | 0 | 2,544 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 112-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,412 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_1513164C`, the next ordinary unparked C row
in the fresh queue at 23 real differences. Keep the documented smaller
compiler, SDK, and ownership rows parked in their existing queues.
