# Game embedded-address setup wrapper match - 2026-09-26

## Result

`func_15192308` is byte-exact across all 20 words and 80 bytes at
`0x15192308..0x15192358`. Fresh totals are 2,710 / 5,469 exact C functions
overall and 2,139 / 4,791 in Game.

## Recovery

The function accepts an object pointer and a second scalar argument. It calls
`func_15131C84` with six values derived from the object: embedded addresses at
offsets `0xAC`, `0xAE`, and `0xB0`; the word stored at `0xA8`; and two stack
arguments pointing to offsets `0x38` and `0x3C`. It then returns one.

Giving `func_15131C84` a typed six-argument declaration lets IDO retain the
object in `s0`, home the otherwise unused second incoming argument at
`sp + 0x2C`, form both stack arguments before the register arguments, and put
the final `arg0 + 0xB0` calculation in the call delay slot. The resulting C
matches all 20 retail words directly and uses no guarded retail-word patch.

## Evidence

Linked ELF offset `0x1D2308` and decompressed retail offset `0x1BF7B8` compare
equal for 80 bytes, both with SHA-256
`8376d022e1edf5b1dd28744f7ee1198c93438ac0a7acea02d3b09240cf2f60a1`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,710 / 5,469 (49.55%) | 1 | 2,758 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,139 / 4,791 (44.65%) | 0 | 2,652 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `func_151A73EC`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
