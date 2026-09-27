# Game second float ABI adapter match - 2026-09-26

## Result

`func_151B50A4` is byte-exact across all 20 words and 80 bytes at
`0x151B50A4..0x151B50F4`. Fresh totals are 2,714 / 5,469 exact C functions
overall and 2,143 / 4,791 in Game.

## Recovery

The function is a structural twin of byte-exact `func_151AF338`. It accepts
six scalar floats followed by a pointer, builds a three-float local vector
from the first three values, and calls `func_151B50F4` with that vector, the
remaining three floats, and the byte at offset `0xC` of the final pointer.

Reusing the typed seven-argument wrapper reproduces the mixed o32 hard-float
ABI exactly: `$f12`/`$f14` argument stores, `$a2`/`$a3` homes, local-vector
layout, stack scalar loads, final-pointer byte extraction, call-delay store,
and epilogue all match retail. The `func_151B50F4` body remains a placeholder;
only its declaration and definition signature were corrected to describe the
recovered call boundary.

## Evidence

Linked ELF offset `0x1F50A4` and decompressed retail offset `0x1E2554` compare
equal for 80 bytes, both with SHA-256
`480b14e5919e75a4efab526e78c6895aa7d95e3090cd7d1a868dd32d37a20dfe`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,714 / 5,469 (49.63%) | 1 | 2,754 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,143 / 4,791 (44.73%) | 0 | 2,648 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 21-word `func_151B7678`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
