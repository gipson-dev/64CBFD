# Game existing-record wrapper twin match - 2026-09-26

## Result

`func_150C6870` is byte-exact across 21 words and 84 bytes at
`0x150C6870..0x150C68C4`. Fresh totals are 2,724 / 5,470 exact C functions
overall and 2,153 / 4,792 in Game.

## Recovery

This function is the `+0x70` structural twin of `func_150C5F40`. It preloads
the owner pointer from wrapper offset `0x18`, activates an existing record's
embedded `+0x58` member through byte `+4`, or calls
`func_150C68C4(owner, wrapper)` and stores the returned record at `+0x70`.

The same typed owner and wrapper lifetimes reproduce all 21 retail words
directly, including the `a1` wrapper lifetime, `a2` owner preload, branch-delay
move into `a0`, call-delay spill, and returned-pointer store. No retail-word
patch is used.

## Evidence

Linked ELF offset `0x106870` and decompressed retail offset `0xF3D20` compare
equal for all 84 bytes. Both spans have SHA-256
`20817a804dc0355c5d9ffea271db0521cd85aac833f0dfa7653ea887b002e5fb`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,724 / 5,470 (49.80%) | 1 | 2,745 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,153 / 4,792 (44.93%) | 0 | 2,639 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and full link, fresh progress and matcher, independent
retail/ELF span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_150C7968`.
