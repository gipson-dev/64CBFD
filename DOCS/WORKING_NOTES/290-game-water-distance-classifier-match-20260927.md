# Game water-distance classifier match - 2026-09-27

## Result

`func_15125490` is byte-exact across all 25 words and 100 bytes at
`0x15125490..0x151254F4`. Fresh totals are 2,794 / 5,469 (51.09%) exact C
functions overall and 2,223 / 4,791 (46.40%) in Game.

## Recovery

The previous uncertain raw-byte implementation is now expressed through the
typed `struct108::unk3D0` object and `struct127` fields. A record whose
`in_water` byte is not one returns null. Otherwise the function truncates the
absolute difference between `y_position` and `unk118` to an integer. It
returns null below 100 units, the object pointer from 100 through 300 units,
and pointer sentinel one at 301 units or above.

This behavior agrees with retail, including both thresholds and all three
return classes. Several positive/negative branch forms, scalar and pointer
return types, declaration orders, branch-local lifetimes, and a one-word
aggregate were compiled. The smallest IDO body remained 26 words: it kept the
object/result in `v1`, the distance in `v0`, and required an extra merge move.
Retail uses the opposite lifetimes and fits in 25 words.

The ordinary padding path therefore emits an overflow trampoline. Twenty-five
guarded slot rows replace that trampoline and zero fill with retail's complete
body after checking every expected word and the trampoline's `R_MIPS_26`
relocation. The typed C remains the maintained behavioral reconstruction; a
compiler or layout change that alters the guarded input fails the build.

## Evidence

Linked ELF offset `0x165490` and decompressed retail offset `0x152940` compare
equal across the complete 100-byte span. Both have SHA-256
`a5ffeceac1d9fab6316daf2b99daed9276cdbc0c1a0ff0b8a16f7a0cf9b696a6`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,794 / 5,469 (51.09%) | 1 | 2,674 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,223 / 4,791 (46.40%) | 0 | 2,568 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 100-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_1514EE70`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
