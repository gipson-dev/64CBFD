# Game constant preset wrapper match - 2026-09-26

## Result

`func_150EC45C` is byte-exact across its complete 21-word, 84-byte tracked
span at `0x150EC45C..0x150EC4B0`. Fresh totals are 2,705 / 5,469 exact C
functions overall and 2,134 / 4,791 in Game.

## Recovery

The wrapper forwards its incoming object to `func_151C3B0C` with three
`1.0f` values, one `0.0f` value, and three integer `0xFF` values. The callee's
typed eight-argument declaration establishes the intended mixed integer and
floating-point ABI.

IDO loads `1.0f` once into `f0`, copies its bits into `a1` through `a3`, and
loads zero into `f4`. The three channel constants are stored to stack slots in
reverse order, while the zero float occupies the call delay slot. This direct
C call reproduces the complete retail sequence without guarded words.

## Evidence

Linked ELF offset `0x12C45C` and decompressed retail offset `0x11990C` compare
equal for 84 bytes, both with SHA-256
`286cfe5e6e7390c73018d14668a98f0ca33576873782a1ea1b5ce26dac6ab473`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,705 / 5,469 (49.46%) | 1 | 2,763 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,134 / 4,791 (44.54%) | 0 | 2,657 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue ordinary Game restoration with 22-word `func_150F1684`, whose retail
handler compares event byte `0x43`, checks the two-part record identity, and
conditionally calls `func_1516972C`. Keep the previously measured compiler
and handwritten-assembly boundaries parked.
