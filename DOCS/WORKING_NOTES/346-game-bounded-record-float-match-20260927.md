# Game bounded record-float match - 2026-09-27

## Result

`func_1518804C` is byte-exact across all 29 words and 116 bytes at
`0x1518804C..0x151880C0`. Fresh totals are 2,850 / 5,469 (52.11%) overall and
2,278 / 4,791 (47.55%) in Game.

## Recovery

The function first requires its signed index to be within
`0 <= index < D_800DF7B4`. It clamps the float argument to the inclusive range
`[0.0f, 1.0f]`, then stores it in the first word of the corresponding 36-byte
record rooted at `D_800DF70C`.

The natural `arg1 > 1.0f` followed by `arg1 < 0.0f` source shape reproduces
retail's floating comparisons, branch-likely zero setup, clamped register
lifetime, and record-address calculation. All 29 words compile directly from C
without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1B54CC` and pristine retail span at
`conker.us.bin+0x1B54FC` compare equal for all 116 bytes. Both have SHA-256
`d102c486f94767caa8adbdc5fc2170ccb56a0e95f6014a82d00a657770ad278c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,850 / 5,469 (52.11%) | 1 | 2,618 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,278 / 4,791 (47.55%) | 0 | 2,513 |
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

Continue with 25-word Game `func_1519F48C`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
