# Game paired matrix wrapper match - 2026-09-27

## Result

`func_151148A8` is byte-exact across all 25 words and 100 bytes at
`0x151148A8..0x1511490C`. Fresh totals are 2,843 / 5,469 (51.98%) overall and
2,271 / 4,791 (47.40%) in Game.

## Recovery

The function builds one matrix directly in the caller-provided destination
from the middle element of a three-float parameter vector. It builds a second
matrix on the stack from the vector's first and third elements, then multiplies
that temporary matrix into the destination in place through `func_150A7A48`.

Typed `f32 [4][4]` matrix parameters and an `f32 [3]` vector are sufficient for
IDO to reproduce the retail frame, floating-zero moves, argument loads, call
delay slots, and in-place multiply. All 25 words compile directly from C
without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x141D28` and pristine retail span at
`conker.us.bin+0x141D58` compare equal for all 100 bytes. Both have SHA-256
`1db33e9c444428eb5b1b54519defbdc5638d3fa048b9f9d332a1c4682915a410`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,843 / 5,469 (51.98%) | 1 | 2,625 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,271 / 4,791 (47.40%) | 0 | 2,520 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent linked-
span hashes, and direct byte comparison pass. The broader replacement,
outer-ROM, tool, unit-test, guard-table, and whitespace checks also pass. All
nine unit tests pass, and the 1,466-row guard table has zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 26-word Game `func_1511BDF4`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
