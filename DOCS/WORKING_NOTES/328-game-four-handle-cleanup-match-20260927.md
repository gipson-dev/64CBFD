# Game four-handle cleanup match - 2026-09-27

## Result

`func_151D5E30` is byte-exact across all 24 words and 96 bytes at
`0x151D5E30..0x151D5E90`. Fresh totals are 2,832 / 5,469 (51.78%) overall and
2,260 / 4,791 (47.17%) in Game.

## Recovery

The helper walks four consecutive 32-bit handles. For every nonzero entry, it
calls `func_100043B4(handle, 3)`. A null entry is skipped, and the loop always
advances through all four slots.

Using an `s32 *` slot array, a retained `s32` entry, and a `u8` loop index
naturally reproduces retail's 32-byte frame, `s0`/`s1` lifetimes, unsigned-
byte increment normalization, call relocation, loop back edge, and epilogue.
IDO otherwise loads the handle directly into `a0` and forms a likely branch.
Three guarded entries retain it in `v0`, select retail's non-likely null
branch, and copy the handle to `a0` in that branch's delay slot.

## Evidence

The rebuilt span at `build/conker.us.bin+0x2032B0` and pristine retail span at
`conker.us.bin+0x2032E0` compare equal for all 96 bytes. Both have SHA-256
`8a7230c21df7247d5bea3fff7fefbe01360547b2e816318b17bc6455f0914653`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,832 / 5,469 (51.78%) | 1 | 2,636 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,260 / 4,791 (47.17%) | 0 | 2,531 |
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

Continue with 25-word Game `func_15023440`, the next unparked C row at 24 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
