# Game optional-owner callback match - 2026-09-27

## Result

`func_15141250` is byte-exact across all 27 words and 108 bytes at
`0x15141250..0x151412BC`. Fresh totals are 2,846 / 5,469 (52.04%) overall and
2,274 / 4,791 (47.46%) in Game.

## Recovery

The function optionally passes the owner pointer at object offset `0x154` and
the object itself to `func_1517E134`. It then decrements `D_800DC9F0` and uses
the byte at object offset `0x168` to select a callback from `D_80089FE4`.

The prior semantic C body overflowed its 108-byte slot because the callback
table was incorrectly declared with two arguments, forcing IDO to preserve the
object in `$a2`. Retail prepares only `$a0` for the indexed callback. Correcting
the table to a one-argument callback contract restores the `$a1` object
lifetime. Treating the owner slot as volatile preserves retail's separate null-
test and call-argument loads. All 27 words now compile directly from C without
guards or an overflow trampoline.

## Evidence

The rebuilt span at `build/conker.us.bin+0x16E6D0` and pristine retail span at
`conker.us.bin+0x16E700` compare equal for all 108 bytes. Both have SHA-256
`6f88fbf60af2c237ad6c02abe4a3d6eafe680309efda564ab7cb569e09a6c72a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,846 / 5,469 (52.04%) | 1 | 2,622 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,274 / 4,791 (47.46%) | 0 | 2,517 |
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

Continue with 25-word Game `func_1514ED8C`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
