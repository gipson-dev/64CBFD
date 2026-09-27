# Game resource-size selector match - 2026-09-27

## Result

`func_1502DB20` is byte-exact across all 25 words and 100 bytes at
`0x1502DB20..0x1502DB84`. Fresh totals are 2,834 / 5,469 (51.82%) overall and
2,262 / 4,791 (47.21%) in Game.

## Recovery

The helper reads `D_800C4ED0[arg0]`. IDs 59, 117, 130, 136, 144, 150, 152,
156, 157, 159, 160, 177, 178, and 180 return that unsigned-halfword value
minus four; all other IDs return it unchanged.

A single C switch reproduces retail's complete control flow. IDO separates
the isolated ID 59 comparison from a 64-entry jump table spanning IDs
117 through 180, then emits both table-read return tails with the retail
registers and delay slots. No guarded instruction words are required.

The compact switch table is compiler-generated rodata, while this generated
slice retains the original table at `jtbl_80096DF8_game`. The generated-object
padding tool now accepts the same explicit `--rodata-symbol` retarget used by
plain padded objects. This keeps the C-generated text relocations while
discarding duplicate compact rodata and resolving the linked load to retail
address `0x80096DF8`.

The matcher also needed a correctness fix: restored internal `.L` labels were
being parsed as new functions, truncating the enclosing function. Local labels
now remain address metadata while subsequent words stay attached to the real
function. Regression tests cover both tool paths.

## Evidence

The rebuilt span at `build/conker.us.bin+0x5AFA0` and pristine retail span at
`conker.us.bin+0x5AFD0` compare equal for all 100 bytes. Both have SHA-256
`d84d8b8a9ab78162b67744ee3f461014abf7ef58b7b51b398fb7b45d93819a29`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,834 / 5,469 (51.82%) | 1 | 2,634 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,262 / 4,791 (47.21%) | 0 | 2,529 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, complete rebuild and link, corrected fresh
matcher, linked-span hashes, and direct byte comparison pass. The replacement
build, outer ROM build, project tool checks, unit tests, guard-table audit, and
whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 26-word Game `func_1502EE8C`, the next unparked C row at 24 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
