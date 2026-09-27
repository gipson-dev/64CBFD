# Game actor-state byte selector match - 2026-09-27

## Result

`func_150F1CB0` is byte-exact across all 24 words and 96 bytes at
`0x150F1CB0..0x150F1D10`. Fresh totals are 2,814 / 5,469 (51.45%) exact C
functions overall and 2,242 / 4,791 (46.80%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered routine writes
actor byte `+0x68` as `0x1B` when halfword `+0x84` equals `0x14`, otherwise as
`0x0C`. It initializes actor byte `+0x69` to `0x13`, changes it to `0x14` when
the low two bits of word `+0x2E4` are both set, and finally overrides it with
`0x17` when bits two and three are both set.

The direct ordered conditionals reproduce retail's constant materialization,
both branch delay slots, and the alias-driven reload of word `+0x2E4` after the
intervening byte store. No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x11F130` and pristine retail span at
`conker.us.bin+0x11F160` compare equal for all 96 bytes. Both have SHA-256
`56494e88f5d715bac816b14d0224f33c4a07cf1ea3a74785482ab275bc80ce51`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,814 / 5,469 (51.45%) | 1 | 2,654 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,242 / 4,791 (46.80%) | 0 | 2,549 |
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

Continue with 24-word Game `func_150F52B0`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
