# Game conditional stack-record wrapper match - 2026-09-26

## Result

`func_150F2390` is byte-exact across all 20 words and 80 bytes at
`0x150F2390..0x150F23E0`. Fresh totals are 2,706 / 5,469 exact C functions
overall and 2,135 / 4,791 in Game.

## Recovery

The function accepts an owner pointer and two scalar arguments. When the
owner's pointer at offset `0x1D4` is non-null, it creates a 12-byte `struct17`
on the stack. `func_150F22D0` initializes that record using the low byte of the
second argument, then `func_151C329C` submits it with arguments `0xFF` and
zero. A null owner field skips both calls.

The typed stack local establishes retail's `sp + 0x1C` address. Keeping the
second argument scalar and casting it to `u8` makes IDO home the word at
`sp + 0x2C` and reload its low byte from `sp + 0x2F` in the first call's delay
slot. The null path uses retail's branch-likely return-address restore, and the
second call receives zero in its delay slot.

## Evidence

Linked ELF offset `0x132390` and decompressed retail offset `0x11F840` compare
equal for 80 bytes, both with SHA-256
`7990c285682c470388437b0da8386a307ca4e58dce971a9b1b16819b8e0c3abb`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,706 / 5,469 (49.48%) | 1 | 2,762 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,135 / 4,791 (44.56%) | 0 | 2,656 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

`func_150F1684` behavior is recovered, but tested direct-C forms still assign
its incoming key and interior identity pointer to the opposite `v0`/`v1`
registers from retail. Keep it parked at that measured boundary. Continue with
21-word `func_1514A498`, a self-contained motion-decay and byte-update routine.
