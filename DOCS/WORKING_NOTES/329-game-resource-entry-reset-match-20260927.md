# Game resource-entry reset match - 2026-09-27

## Result

`func_15023440` is byte-exact across all 25 words and 100 bytes at
`0x15023440..0x150234A4`. Fresh totals are 2,833 / 5,469 (51.80%) overall and
2,261 / 4,791 (47.19%) in Game.

## Recovery

The helper resets one `struct163` entry. With a nonzero mode, it releases the
resource in `unk34` through `func_1516D2E0` and clears the pointer. With mode
zero and an active `unkC` flag, it refreshes the resource through
`func_1516D328` and retains the pointer. An inactive mode-zero entry clears
the pointer. Every path clears the entry's leading halfword `unk0`.

The structured branches naturally reproduce all 25 retail words: the
branch-likely mode split, saved `a2` object lifetime around each call, release
and refresh relocations, inactive-pointer clear in a likely delay slot, the
compiler's unreachable scheduled clear after the refresh path, and the final
epilogue. No guarded word patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x508C0` and pristine retail span at
`conker.us.bin+0x508F0` compare equal for all 100 bytes. Both have SHA-256
`a8d81a7d4b3a413a1f964ff45762715e657657e89cd4b13c1076393c346bf7a1`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,833 / 5,469 (51.80%) | 1 | 2,635 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,261 / 4,791 (47.19%) | 0 | 2,530 |
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

Continue with 25-word Game `func_1502DB20`, the next unparked C row at 24 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
