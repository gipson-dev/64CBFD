# Game type-result selector match - 2026-09-27

## Result

`func_151928B0` is byte-exact across all 28 words and 112 bytes at
`0x151928B0..0x15192920`. Fresh totals are 2,853 / 5,469 (52.17%) overall and
2,281 / 4,791 (47.61%) in Game.

## Recovery

The function reads the type byte at object offset `0x04`. Types `0..4` return
success and write zero through the output pointer. Type `0x53` returns success
and writes one. Every other type returns zero without modifying the output.

The five low types intentionally retain retail's five-entry jump table even
though all entries share one body. The generated-slice build now retargets the
compiler-produced table references to existing retail symbol
`jtbl_800A8160_game`. Four function-scoped guard rows restore retail's empty
default delay slot, shared-epilogue branch extents, and explicit type-`0x53`
branch/store pair.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1BFD30` and pristine retail span at
`conker.us.bin+0x1BFD60` compare equal for all 112 bytes. Both have SHA-256
`5df09e47be03d532d51cb3be24137de3e4bb65af2be2d7a3b7f6f83212c0fe88`.
The linked relocations resolve against absolute retail symbol
`jtbl_800A8160_game` at `0x800A8160`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,853 / 5,469 (52.17%) | 1 | 2,615 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,281 / 4,791 (47.61%) | 0 | 2,510 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, direct linked-span
comparison, target hash, and jump-table symbol audit pass. The 1,465-row guard
table has zero duplicate `(filename, function, offset)` keys. The broader
replacement and outer-ROM builds, project tool checks, all nine unit tests,
and the whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Classify 25-word Game `func_150ADA68`, the first Game row in the fresh queue
after the documented compiler cases. It belongs to the existing PRNG cluster,
so verify source and handwritten ownership before changing its implementation.
