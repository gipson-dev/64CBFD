# Game lifetime updater match - 2026-09-27

## Result

`func_15166204` is byte-exact across all 25 words and 100 bytes at
`0x15166204..0x15166268`. Fresh totals are 2,826 / 5,469 (51.67%) overall and
2,254 / 4,791 (47.05%) in Game.

## Recovery

The routine adds the signed rate at `+0x96`, scaled by `D_800BE9E4`, to the
signed accumulator at `+0x9E`. It then subtracts the same frame delta from the
unsigned byte lifetime at `+0x92`. A still-positive lifetime is stored back;
an expired lifetime instead passes the object to `func_1516972C` for removal.

Initializing the lifetime temporary before the accumulator statement keeps it
in retail's `v0`. Spelling expiry as the primary `if` path makes IDO produce
the retail `bgtzl` and its delay-slot store. IDO also naturally retains the
unreachable duplicate store after the unconditional branch. No guarded word
patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x193684` and pristine retail span at
`conker.us.bin+0x1936B4` compare equal for all 100 bytes. Both have SHA-256
`1a61744e11c39328ddee4adaaf1d193d7b88382e326b16990c76e93d61b2a689`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,826 / 5,469 (51.67%) | 1 | 2,642 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,254 / 4,791 (47.05%) | 0 | 2,537 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full shared-table rebuild and link, fresh
matcher, and independent linked-span comparison pass. The complete replacement
build, outer ROM build, tool checks, unit tests, guard-table audit, and
whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 24-word Game `func_1517EA4C`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
