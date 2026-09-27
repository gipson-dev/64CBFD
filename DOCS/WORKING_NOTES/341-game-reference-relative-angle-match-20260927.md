# Game reference-relative angle match - 2026-09-27

## Result

`func_1511BE5C` is byte-exact across all 24 words and 96 bytes at
`0x1511BE5C..0x1511BEBC`. Fresh totals are 2,845 / 5,469 (52.02%) overall and
2,273 / 4,791 (47.44%) in Game.

## Recovery

The function converts signed halfword coordinates at object offsets `0x10`
and `0x14` to floats, then subtracts the reference coordinates at offsets
`0x2F8` and `0x300` of `D_800DBFF0`. It passes those differences to
`func_150484A0`, multiplies the returned angle by `D_800A31E0`, and stores the
result at object offset `4`.

A direct typed assignment preserves retail's paired halfword loads, integer-
to-float conversion schedule, global reference loads, argument subtraction,
call delay slot, and final scaled store. All 24 words compile directly from C
without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1492DC` and pristine retail span at
`conker.us.bin+0x14930C` compare equal for all 96 bytes. Both have SHA-256
`9e74ca5f6539068fb711027533d856fa8433fd8c3c3c6057e928c1e374ddca04`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,845 / 5,469 (52.02%) | 1 | 2,623 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,273 / 4,791 (47.44%) | 0 | 2,518 |
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

Continue with 27-word Game `func_15141250`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
