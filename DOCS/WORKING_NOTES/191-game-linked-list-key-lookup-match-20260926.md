# Game linked-list key lookup match - 2026-09-26

## Result

`func_1514ED3C` is byte-exact across all 20 words and 80 bytes at
`0x1514ED3C..0x1514ED8C`. Fresh totals are 2,694 / 5,469 exact C functions
overall and 2,123 / 4,791 in Game.

## Recovery

The function walks a doubly linked game node list, compares each node's
32-bit key at offset `0x10`, and returns one when it finds a match. When its
third argument is non-null, it also writes the matched node, or null after an
unsuccessful search.

A local typed node header records the key, next/previous links, and adjacent
16-bit key used by neighboring routines. Keeping `current` separate from the
prefetched next `node` reproduces retail's `$v0`/`$a0` lifetimes. Declaring the
found flag before `current` places its zeroing before the opening null test and
moves the current-pointer initialization into the branch delay slot. All words
compile directly with no guarded patches or compiler-steering expressions.

## Evidence

Linked ELF offset `0x18ED3C` and decompressed retail offset `0x17C1EC` compare
equal for 80 bytes, both with SHA-256
`10caa2bb84bec91148134f5ebee3b7856aad744979f985e503f3860cc03b5d65`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,694 / 5,469 (49.26%) | 1 | 2,774 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,123 / 4,791 (44.31%) | 0 | 2,668 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` already contains the complete generated retail body,
so no sibling regeneration is needed. Its 1,659 dirty entries and frozen
Release executable remain untouched.

The focused object, full replacement link, fresh progress and matcher scans,
independent span comparison, tool checks, all six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with 20-word `func_15178BE4`, the next
nonblocked Game row at 18 differences. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
