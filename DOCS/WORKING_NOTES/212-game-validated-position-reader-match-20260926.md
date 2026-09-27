# Game validated-position reader match - 2026-09-26

## Result

`func_151B7678` is byte-exact across all 21 words and 84 bytes at
`0x151B7678..0x151B76CC`. Fresh totals are 2,715 / 5,469 exact C functions
overall and 2,144 / 4,791 in Game.

## Recovery

The function accepts an object and a three-float output vector. It follows the
pointer at object offset `0x98`, then the pointer at offset `4` of that
container, then the record pointer at offset `0` of the entry. The record is
accepted only when its leading word is nonzero and the entry byte at offset
`4` equals the record byte at offset `0x3B`. On success, floats at record
offsets `0x14`, `0x18`, and `0x1C` are copied to the output and the function
returns one; otherwise it returns zero.

Expressing failure as one short-circuit `empty || tag mismatch` condition gives
IDO retail's layout: an ordinary empty-record branch, branch-likely tag match,
one shared zero-return block, a duplicated scheduled load of the first float,
and the success copy after that block. More obvious nested or separate guard
forms either hoisted the zero result or overflowed the retail span.

## Evidence

Linked ELF offset `0x1F7678` and decompressed retail offset `0x1E4B28` compare
equal for 84 bytes, both with SHA-256
`b6be4112a6bbc89160af04c63a144617a2f1d834e34c138fc78fc2089f63d57b`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,715 / 5,469 (49.64%) | 1 | 2,753 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,144 / 4,791 (44.75%) | 0 | 2,647 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 22-word `func_151B8318`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
