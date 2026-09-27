# Game packed actor-mask clear match - 2026-09-27

## Result

`func_1507A47C` is byte-exact across 22 words and 88 bytes at
`0x1507A47C..0x1507A4D4`. Fresh totals are 2,728 / 5,470 exact C functions
overall and 2,157 / 4,792 in Game.

## Recovery

The function packs bytes `D_800D1890` through `D_800D1893` into a 32-bit
mask, complements that mask, and clears the corresponding bits in the current
actor's `unk94` field. A named packed-mask local preserves the exact retail
extent and makes the recovered behavior explicit.

IDO still schedules the four independent byte loads, actor access, shifts,
OR tree, complement, and final field update differently from retail. Eighteen
guarded rows restore the retail schedule while checking every compiler word
and all five moved relocation pairs. The initial address materialization,
actor-address `lui`, and final return words compile directly. The shared patch
table now contains 1,182 rows with zero duplicate
`(filename,function,offset)` keys.

## Evidence

Linked ELF offset `0xBA47C` and decompressed retail offset `0xA792C` compare
equal for all 88 bytes. Both spans have SHA-256
`45861dbacdfafde2e9941b698382ca182e210932c1f210c4d95ce0388da56e3c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,728 / 5,470 (49.87%) | 1 | 2,741 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,157 / 4,792 (45.01%) | 0 | 2,635 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and exhaustive full link, fresh progress and matcher,
independent 88-byte span hashes and `cmp`, replacement build, project tool
checks, all six padding-tool unit tests, outer build, and `git diff --check`
pass.

## Next boundary

Keep the measured compiler-boundary rows ahead of it parked and continue with
24-word `func_150C5310`, the next ordinary Game C candidate with 20 real
differences.
