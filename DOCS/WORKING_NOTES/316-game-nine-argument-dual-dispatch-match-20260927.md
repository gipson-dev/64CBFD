# Game nine-argument dual dispatch match - 2026-09-27

## Result

`func_1513164C` is byte-exact across all 24 words and 96 bytes at
`0x1513164C..0x151316AC`. Fresh totals are 2,820 / 5,469 (51.56%) exact C
functions overall and 2,248 / 4,791 (46.92%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered nine-argument
routine dispatches two five-argument calls. It first forwards arguments 5
through 9 to `func_15131514`. It then forwards arguments 1 through 4 plus the
shared ninth argument to `func_1513137C` and returns that second call's result.

The explicit nine-argument ABI is the compiler-shape fix. IDO emits retail's
32-byte frame, saves the first four incoming registers in their caller home
slots, loads arguments 5 through 8 into `a0..a3`, and writes argument 9 to the
outgoing stack slot in the first call's delay slot. It then reloads argument 9
and the original register arguments for the second call, using the same
delay-slot stack store. The epilogue follows directly with no guarded words.

## Evidence

The rebuilt span at `build/conker.us.bin+0x15EACC` and pristine retail span at
`conker.us.bin+0x15EAFC` compare equal for all 96 bytes. Both have SHA-256
`d1f2ddb2fc806b978707ae893df837c78ef338cc51db51e04be4c5441ab7e941`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,820 / 5,469 (51.56%) | 1 | 2,648 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,248 / 4,791 (46.92%) | 0 | 2,543 |
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

Continue with 24-word Game `func_15133760`, the next ordinary unparked C row
in the fresh queue at 23 real differences. Keep the documented smaller
compiler, SDK, and ownership rows parked in their existing queues.
