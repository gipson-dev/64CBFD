# Game fixed-scale transform copy match - 2026-09-27

## Result

`func_1519EF04` is byte-exact across all 27 words and 108 bytes at
`0x1519EF04..0x1519EF70`. Fresh totals are 2,830 / 5,469 (51.75%) overall and
2,258 / 4,791 (47.13%) in Game.

## Recovery

The helper reads a linked source from destination offset `0x110`. It
multiplies source floats at `0x18` and `0x1C` by `10.0f` into destination
offsets `0x2C` and `0x30`, copies source vector `0x0C..0x14` to destination
`0x40..0x48`, copies source vector `0x00..0x08` to destination `0x34..0x3C`,
and returns `1`.

Typed C naturally reproduces all 27 retail words. IDO emits the `0x41200000`
constant through `lui` and `mtc1`, retains retail's floating-point hazard
`nop`, loads the source into `v1`, initializes `v0`, and assigns the same
floating-point registers through the complete copy. No guarded word patches
are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1CC384` and pristine retail span at
`conker.us.bin+0x1CC3B4` compare equal for all 108 bytes. Both have SHA-256
`538df983afbd767f37e9900031a7f0012a06eb70b77d7523a944083e8f40d98c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,830 / 5,469 (51.75%) | 1 | 2,638 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,258 / 4,791 (47.13%) | 0 | 2,533 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full link, fresh matcher, and independent
linked-span comparison pass. The complete replacement build, outer ROM build,
tool checks, unit tests, guard-table audit, and whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 28-word Game `func_151AE640`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
