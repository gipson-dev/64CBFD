# Game actor-position query wrapper match - 2026-09-27

## Result

`func_1503F904` is byte-exact across all 24 words and 96 bytes at
`0x1503F904..0x1503F964`. Fresh totals are 2,806 / 5,469 (51.31%) exact C
functions overall and 2,234 / 4,791 (46.63%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered three-argument
wrapper reads actor floats at offsets `0x14` and `0x1C`, truncates each through
a signed 16-bit value, and calls `func_1503F800` with the actor's embedded
query data at offset `0x320`. The second incoming argument is forwarded in
`a3`, and constant `1` is supplied as the fifth stack argument.

The third incoming argument is behaviorally unused but remains part of the
typed signature. IDO consequently preserves retail's `a2` home-slot spill at
`sp+0x28`. The `QueryActor` layout and direct five-argument return expression
reproduce the complete retail frame, two FP truncations, sign extensions,
call delay slot, and return path without guarded words.

## Evidence

The rebuilt span at `build/conker.us.bin+0x6CD84` and pristine retail span at
`conker.us.bin+0x6CDB4` compare equal for all 96 bytes. Both have SHA-256
`69d25b286871e4066bd8dd2c0d9860c569f2f74a0e75e5cdd729956128995a62`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,806 / 5,469 (51.31%) | 1 | 2,662 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,234 / 4,791 (46.63%) | 0 | 2,557 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,354 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_15044D40`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
