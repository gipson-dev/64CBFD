# Game mode-driven slot updater match - 2026-09-27

## Result

`func_151AE640` is byte-exact across all 28 words and 112 bytes at
`0x151AE640..0x151AE6B0`. Fresh totals are 2,831 / 5,469 (51.76%) overall and
2,259 / 4,791 (47.15%) in Game.

## Recovery

The callback receives an object, a two-word pair, and an unsigned byte mode.
In mode zero, it clears the object's tracked slot at `0x44` when that slot
matches the pair's first word. In mode `0x2D`, it replaces a matching first
word with the second, or a matching second word with the first. Other modes
and nonmatching pairs leave the slot unchanged.

Declaring the mode as `u8`, retaining the pair's first word in a local, and
using explicit early returns reproduces retail's argument-home store, byte
normalization, register lifetimes, branch-likely path, and successful-swap
delay-slot store. IDO schedules the zero-mode clear into `jr`'s delay slot,
while retail emits `store; jr; nop`. Four guarded entries restore that three-
word sequence and retarget the two earlier local branches across the inserted
word. No data relocations are involved.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1DBAC0` and pristine retail span at
`conker.us.bin+0x1DBAF0` compare equal for all 112 bytes. Both have SHA-256
`290f1de7726975b100bdf3b023d45174364d7fda0e0a2060cef19eeb052d4328`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,831 / 5,469 (51.76%) | 1 | 2,637 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,259 / 4,791 (47.15%) | 0 | 2,532 |
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

Continue with 24-word Game `func_151D5E30`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
