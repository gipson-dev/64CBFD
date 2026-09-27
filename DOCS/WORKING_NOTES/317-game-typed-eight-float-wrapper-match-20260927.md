# Game typed eight-float wrapper match - 2026-09-27

## Result

`func_15133760` is byte-exact across all 24 words and 96 bytes at
`0x15133760..0x151337C0`. Fresh totals are 2,821 / 5,469 (51.58%) exact C
functions overall and 2,249 / 4,791 (46.94%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered wrapper forwards
its first pointer plus eight single-precision fields from its second pointer to
`func_15142838`, then returns one. The fields are at offsets `+0x18`, `+0x1C`,
`+0x20`, `+0x24`, `+0x28`, `+0x38`, `+0x3C`, and `+0x40`.

Adding the typed nine-argument callee contract prevents default float-to-double
promotion. IDO then emits retail's 56-byte frame, saves the source pointer in
`s0`, passes the first three floats through `a1..a3`, writes the remaining five
floats to outgoing stack slots, and places the last store in the call delay
slot. The return-one epilogue follows directly with no guarded words.

## Evidence

The rebuilt span at `build/conker.us.bin+0x160BE0` and pristine retail span at
`conker.us.bin+0x160C10` compare equal for all 96 bytes. Both have SHA-256
`2f32a09575c94a5c410e4972036f77aa1e3f26d4f43cbe8b57f824663f5b4809`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,821 / 5,469 (51.58%) | 1 | 2,647 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,249 / 4,791 (46.94%) | 0 | 2,542 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,412 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 34-word Game `func_15142FBC`, the next ordinary unparked C row
in the fresh queue at 23 real differences. Keep the documented smaller
compiler, SDK, and ownership rows parked in their existing queues.
