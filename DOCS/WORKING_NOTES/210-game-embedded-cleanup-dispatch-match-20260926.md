# Game embedded cleanup dispatch match - 2026-09-26

## Result

`func_151B4C1C` is byte-exact across all 20 words and 80 bytes at
`0x151B4C1C..0x151B4C6C`. Fresh totals are 2,713 / 5,469 exact C functions
overall and 2,142 / 4,791 in Game.

## Recovery

The function accepts an object pointer and first passes its embedded region at
offset `0x140` to `func_151D5E30`. It then reads the object's byte at offset
`0x44`, uses it to select a one-argument callback from `D_8008FB70`, and calls
the callback with the original object when the entry is non-null.

A typed callback local reproduces retail's single table load into `$v0`.
Keeping the object as a pointer parameter gives IDO the original `$a1`
lifetime across the cleanup call, including the call-delay spill and reload.
The null check compiles to retail's branch-likely epilogue, while the callback
receives the retained object in the indirect-call delay slot. The neighboring
`func_151B4C6C` and `func_151B4C98` signatures were corrected to pointer and
void types; their already-exact code remains unchanged.

## Evidence

Linked ELF offset `0x1F4C1C` and decompressed retail offset `0x1E20CC` compare
equal for 80 bytes, both with SHA-256
`a08bf8588f3eb11ac0c886027a1db252f1fe639ea88ad592cff9cebea2a533ab`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,713 / 5,469 (49.61%) | 1 | 2,755 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,142 / 4,791 (44.71%) | 0 | 2,649 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `func_151B50A4`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
