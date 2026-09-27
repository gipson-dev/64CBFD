# Game typed effect-spawn wrapper match - 2026-09-27

## Result

`func_150C1660` is byte-exact across all 24 words and 96 bytes at
`0x150C1660..0x150C16C0`. Fresh totals are 2,812 / 5,469 (51.42%) exact C
functions overall and 2,240 / 4,791 (46.75%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered wrapper forwards
three incoming float coordinates to `func_1514C2F0`, supplies `80.0f` as the
fourth float argument, and passes fixed effect configuration values followed
by the incoming low-byte selector through the eight stack arguments.

The callee's retail stack loads establish those argument types as `u8`, `s8`,
`s16`, `u8`, word, `f32`, word, and `u8`. Expressing that complete prototype
reproduces the 56-byte frame, argument-home spills, constant-store order,
float-zero delay slot, call relocation, and epilogue directly from C. No
guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0xEEAE0` and pristine retail span at
`conker.us.bin+0xEEB10` compare equal for all 96 bytes. Both have SHA-256
`6f7f51e26c1e53fd7518734316f89e63941584f038798f4abac9b9875903ebad`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,812 / 5,469 (51.42%) | 1 | 2,656 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,240 / 4,791 (46.75%) | 0 | 2,551 |
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

Continue with 24-word Game `func_150DF8C0`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
