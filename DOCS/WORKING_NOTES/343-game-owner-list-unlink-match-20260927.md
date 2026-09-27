# Game owner-list unlink match - 2026-09-27

## Result

`func_1514ED8C` is byte-exact across all 25 words and 100 bytes at
`0x1514ED8C..0x1514EDF0`. Fresh totals are 2,847 / 5,469 (52.06%) overall and
2,275 / 4,791 (47.48%) in Game.

## Recovery

The function removes a node from the owner list rooted at offset `0x2F4`. It
updates the owner head when removing the first node, repairs both directions of
the node's `next` and `prev` links, saves the word at node offset `0x10`,
releases the node through `func_1516972C`, and returns the saved word.

The first draft incorrectly passed the saved word to the release helper. That
forced IDO to preserve the node in `$a2` and overflowed the retail slot by one
word. Retail keeps the node in `$a0`, calls the release helper with that node,
and uses the offset-`0x10` word only as the return value. Direct repeated field
expressions preserve all three branch-likely delay-slot loads. All 25 words
compile directly from C without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x17C20C` and pristine retail span at
`conker.us.bin+0x17C23C` compare equal for all 100 bytes. Both have SHA-256
`020ffa1b0ba6edd6dccd51c81dab466b8783efb6fd5e85ea7be8d6d0b47339be`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,847 / 5,469 (52.06%) | 1 | 2,621 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,275 / 4,791 (47.48%) | 0 | 2,516 |
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

Continue with 26-word Game `func_15178C34`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
