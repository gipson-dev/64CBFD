# Game existing-record wrapper match - 2026-09-26

## Result

`func_150C5F40` is byte-exact across 21 words and 84 bytes at
`0x150C5F40..0x150C5F94`. Fresh totals are 2,723 / 5,470 exact C functions
overall and 2,152 / 4,792 in Game.

## Recovery

The function preloads the owner pointer from wrapper offset `0x18`. When the
record at wrapper offset `0x5C` already exists, it advances to the embedded
record at `+0x58` and sets byte `+4` to one. Otherwise it calls
`func_150C5F94(owner, wrapper)` and stores the returned record at `+0x5C`.

The typed owner and wrapper lifetimes make IDO reproduce all 21 retail words
directly. This includes retaining the wrapper in `a1`, preloading the owner in
`a2`, moving it to `a0` in the conditional branch delay slot, spilling `a1`
in the call delay slot, and restoring it for the returned-pointer store. No
retail-word patch is used.

## Evidence

Linked ELF offset `0x105F40` and decompressed retail offset `0xF33F0` compare
equal for all 84 bytes. Both spans have SHA-256
`5809aac14fd7051e9acbf5960f6c29c0e8557a442bacb5c54804f44d028b1d93`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,723 / 5,470 (49.78%) | 1 | 2,746 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,152 / 4,792 (44.91%) | 0 | 2,640 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and full link, fresh progress and matcher, independent
retail/ELF span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with structural twin `func_150C6870`.
