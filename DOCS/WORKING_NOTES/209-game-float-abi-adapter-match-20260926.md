# Game float ABI adapter match - 2026-09-26

## Result

`func_151AF338` is byte-exact across all 20 words and 80 bytes at
`0x151AF338..0x151AF388`. Fresh totals are 2,712 / 5,469 exact C functions
overall and 2,141 / 4,791 in Game.

## Recovery

The function accepts six scalar floats followed by a pointer. It builds a
three-float local vector from the first three values, then calls
`func_151AF388` with that vector, the remaining three floats, and the byte at
offset `0xC` of the final pointer argument.

The typed seven-argument signature reproduces the mixed o32 hard-float ABI:
the first two floats arrive in `$f12` and `$f14`, the next two are homed from
`$a2` and `$a3`, and the final three arguments arrive on the caller's stack.
IDO emits retail's local-vector stores, final-pointer load, byte extraction,
stack argument forwarding, call-delay store, and epilogue directly. The
`func_151AF388` placeholder remains unconverted; only its declaration and
definition signature were corrected to describe the recovered call boundary.

## Evidence

Linked ELF offset `0x1EF338` and decompressed retail offset `0x1DC7E8` compare
equal for 80 bytes, both with SHA-256
`6d681cd9d26d447146cef46aef99e2567bb2edbf0a3833b27aa03352edde2b87`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,712 / 5,469 (49.59%) | 1 | 2,756 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,141 / 4,791 (44.69%) | 0 | 2,650 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `func_151B4C1C`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
