# Game cached-pointer fallback match - 2026-09-27

## Result

`func_1511BDF4` is byte-exact across all 26 words and 104 bytes at
`0x1511BDF4..0x1511BE5C`. Fresh totals are 2,844 / 5,469 (52.00%) overall and
2,272 / 4,791 (47.42%) in Game.

## Recovery

The function first reads a cached pointer from offset `0x80` of its object. If
that pointer is null, it passes the object's byte at offset `0x3F` to
`func_15083E90`. A non-null selected pointer supplies its words at offsets
`0x14` and `0x1C` to `func_1511BB04`, along with two `1.0f` scale arguments.

Giving `func_1511BB04` its five-argument typed signature prevents default float
promotion. Keeping the cached and selected pointers as separate variables then
reproduces retail's `$v0`/`$v1` branch merge, duplicated object reload, fallback
delay slot, and float stack argument. All 26 words compile directly from C
without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x149274` and pristine retail span at
`conker.us.bin+0x1492A4` compare equal for all 104 bytes. Both have SHA-256
`02175db4753159757ba782321d1a0c783f5c21a6323fb0b07ad06382f1c552b5`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,844 / 5,469 (52.00%) | 1 | 2,624 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,272 / 4,791 (47.42%) | 0 | 2,519 |
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

Continue with 24-word Game `func_1511BE5C`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
