# Game scaled fixed-point clamp match - 2026-09-27

## Result

`func_1515F040` is byte-exact across all 27 words and 108 bytes at
`0x1515F040..0x1515F0AC`. Fresh totals are 2,825 / 5,469 (51.65%) overall and
2,253 / 4,791 (47.03%) in Game.

## Recovery

The routine clamps its float argument to the inclusive upper bound in
`D_800A6520` and lower bound `-32768.0f`, scales the selected value by
`65536.0f`, truncates it to a signed integer, and stores it in
`D_800DCD10[arg1]`.

The earlier direct expression retained separate multiply and conversion FP
temporaries. Updating `arg0` with the scale reproduces retail's `f12` lifetime
and every downstream instruction. IDO still emits 28 words: it hoists the
independent lower-bound `lui` before the first `c.le.s` and inserts a hazard
`nop` afterward.

The same three-entry guarded pattern already used by sibling `func_1515F0AC`
swaps those two independent words and omits the redundant `nop`. The generated
object consequently contracts from 28 words to the exact 27-word retail span.

## Evidence

The rebuilt span at `build/conker.us.bin+0x18C4C0` and pristine retail span at
`conker.us.bin+0x18C4F0` compare equal for all 108 bytes. Both have SHA-256
`df3794fced13b76134a228cb6d09226fb5de3e875ce14f3d7a43123269755d35`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,825 / 5,469 (51.65%) | 1 | 2,643 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,253 / 4,791 (47.03%) | 0 | 2,538 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full shared-table rebuild and link, fresh
matcher, direct comparison, replacement build, outer ROM build, tool checks,
all seven relocation/omission tests, guard-table validation, and whitespace
check pass. The guard table now has 1,436 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 25-word Game `func_15166204`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
