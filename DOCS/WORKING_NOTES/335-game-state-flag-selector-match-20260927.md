# Game state-flag selector match - 2026-09-27

## Result

`func_150829D8` is byte-exact across all 27 words and 108 bytes at
`0x150829D8..0x15082A44`. Fresh totals are 2,839 / 5,469 (51.91%) overall and
2,267 / 4,791 (47.32%) in Game.

## Recovery

The helper clears bits `0x08000002` in the object's word at offset `0xF8`,
then sets bit `0x4`. If the object at offset `0x31C` exists and its byte at
offset `0x56` is zero, the current `D_800BE9F0` state selects whether bit
`0x2` is also set.

States 0, 10, 14, 18, 19, 25, 27, 44, 60, 61, 66, 67, and 68 leave bit
`0x2` clear. Every other state, including values outside the table's
0-through-68 range, sets it. A direct C switch reproduces retail's complete
instruction schedule and 69-entry dispatch table without guarded words.

This generated slice previously could not link switch-generated rodata. The
generated-object padding path now supports an explicit retained-rodata symbol,
so the compact object's switch relocations are retargeted to the original
`jtbl_8009CC40_game` table at `0x8009CC40`.

## Evidence

The rebuilt span at `build/conker.us.bin+0xAFE58` and pristine retail span at
`conker.us.bin+0xAFE88` compare equal for all 108 bytes. Both have SHA-256
`77cdd4a69fb33b7fdbb9dff3a70e358f52fb924ad779f1e9d75c84743e46813d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,839 / 5,469 (51.91%) | 1 | 2,629 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,267 / 4,791 (47.32%) | 0 | 2,524 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, exhaustive rebuild and relink, fresh matcher,
independent linked-span hashes, and direct byte comparison pass. The broader
replacement, outer-ROM, tool, unit-test, guard-table, and whitespace checks
also pass. All nine unit tests pass, and the 1,460-row guard table has zero
duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with the next ordinary unparked Game row in the fresh 24-real-
difference queue. Keep the documented smaller SDK/compiler-special rows
parked.
