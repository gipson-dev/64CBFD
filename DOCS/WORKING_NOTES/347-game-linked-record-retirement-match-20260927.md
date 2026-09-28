# Game linked-record retirement match - 2026-09-27

## Result

`func_1519F48C` is byte-exact across all 25 words and 100 bytes at
`0x1519F48C..0x1519F4F0`. Fresh totals are 2,851 / 5,469 (52.13%) overall and
2,279 / 4,791 (47.57%) in Game.

## Recovery

The function follows the actor's link slot at offset `0x98`. For a live linked
record, state 6 clears the first word at record offset `0x58`, state 7 clears
the third word at offset `0x60`, and every state retires the link. It then
clears byte `0x30`, removes flag `0x2` from halfword `0x1E`, and sets the link
slot's byte-4 active flag.

Typed C recovers the complete behavior and 21 of the 25 retail words directly.
IDO folds the shared `record + 0x58` base into each store, unlike retail's
retained `a1` base. Four function-scoped guard rows preserve the null-branch
extent, shared-base materialization, and the two field stores. This is the
same measured compiler boundary already documented for the adjacent linked-
record helpers `func_1519F108` and `func_1519F168`.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1CC90C` and pristine retail span at
`conker.us.bin+0x1CC93C` compare equal for all 100 bytes. Both have SHA-256
`9f3cf4224facdf4f49be4bf99dc0f87c954f2ef38c2ac71c9b79044638c714e9`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,851 / 5,469 (52.13%) | 1 | 2,617 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,279 / 4,791 (47.57%) | 0 | 2,512 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent linked-
span hashes, and direct byte comparison pass. The 1,470-row guard table has
zero duplicate `(filename, function, offset)` keys. The broader replacement,
outer-ROM, tool, unit-test, and whitespace checks are run before the commit.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 29-word Game `func_151A931C`, the first ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller SDK and
compiler-special rows parked.
