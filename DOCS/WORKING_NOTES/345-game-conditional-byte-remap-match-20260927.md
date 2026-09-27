# Game conditional byte remap match - 2026-09-27

## Result

`func_15182768` is byte-exact across all 26 words and 104 bytes at
`0x15182768..0x151827D0`. Fresh totals are 2,849 / 5,469 (52.09%) overall and
2,277 / 4,791 (47.53%) in Game.

## Recovery

The function compares its signed halfword selector with the byte at record
offset `0x2C`. On a match, it passes the original first argument and five bytes
from the record at offset `0x28` to `func_1517F08C`. The byte order is
`3, 0, 1, 2, 4`; on a mismatch it returns the original first argument.

Assigning the helper result back into the first argument preserves retail's
final `$v0` to `$a0` to `$v0` moves. The explicit `s16` selector reproduces the
entry sign-extension sequence. All 26 words compile directly from C without
guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1AFBE8` and pristine retail span at
`conker.us.bin+0x1AFC18` compare equal for all 104 bytes. Both have SHA-256
`c37eb6ea3bc8d3f98df5b7f4ac3bccdd1305c56f1d5f1d5ee28761720e157638`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,849 / 5,469 (52.09%) | 1 | 2,619 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,277 / 4,791 (47.53%) | 0 | 2,514 |
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

Continue with 29-word Game `func_1518804C`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
