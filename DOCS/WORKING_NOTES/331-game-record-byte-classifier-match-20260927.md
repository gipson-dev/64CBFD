# Game record-byte classifier match - 2026-09-27

## Result

`func_1502EE8C` is byte-exact across all 26 words and 104 bytes at
`0x1502EE8C..0x1502EEF4`. Fresh totals are 2,835 / 5,469 (51.84%) overall and
2,263 / 4,791 (47.23%) in Game.

## Recovery

The helper indexes a `0x32C`-byte record by `arg0`, reads byte `arg1` relative
to `D_800CC33A`, and classifies the value into three outcomes. Values `0..1`
are returned unchanged, values `2..3` are reduced by two, and values `4+`
return `2`.

Typed C reproduces retail's nine-word strength-reduced `arg0 * 0x32C`
calculation, address addition, unsigned byte load, distinct raw-value `v0`
and result `v1` lifetimes, and three-word return tail. IDO rewrites the source
condition into a branch-likely split and duplicates the upper comparison.
Six guarded words at offsets `0x38..0x4C` restore retail's two ordinary
branches, empty comparison delay slot, and separate high-clamp block. No
relocations or instruction insertions are changed.

## Evidence

The rebuilt span at `build/conker.us.bin+0x5C30C` and pristine retail span at
`conker.us.bin+0x5C33C` compare equal for all 104 bytes. Both have SHA-256
`ad2f5842790e41297970334d3fa181230b0a119fb85bfae9eadcf2b0be9afcf3`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,835 / 5,469 (51.84%) | 1 | 2,633 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,263 / 4,791 (47.23%) | 0 | 2,528 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, exhaustive rebuild and link, fresh
matcher, independent linked-span hashes, and direct byte comparison pass. The
replacement build, outer ROM build, project tool checks, all nine unit tests,
guard-table audit, and whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 25-word Game `func_1503F108`, the next unparked C row at 24 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
