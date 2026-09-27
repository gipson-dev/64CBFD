# Game optional record release match - 2026-09-26

## Result

`func_151B8318` is byte-exact across all 22 words and 88 bytes at
`0x151B8318..0x151B8370`. Fresh totals are 2,716 / 5,469 exact C functions
overall and 2,145 / 4,791 in Game.

## Recovery

The function accepts an object pointer, a supplied record pointer, and a byte
flag. It follows the object pointer at offset `0x98` and the entry pointer at
container offset `4`. When the normalized flag is zero, it compares the first
word of the supplied record with the first word of the current entry. If those
words differ, it compares their bytes at offset `4`. Either match releases the
original object through `func_1516972C`; a nonzero flag or two mismatches exits
without releasing it.

The typed byte parameter reproduces retail's incoming `$a2` home, mask, and
normalized lifetime. Keeping the supplied record word as an explicit local
lets IDO reuse `$v0` after the container lookup and restores the retail
`$v0/$t7/$t8/$t9` comparison allocation. The pointer-word equality branches
directly to the call, while the byte mismatch uses retail's branch-likely
epilogue load.

## Evidence

Linked ELF offset `0x1F8318` and decompressed retail offset `0x1E57C8` compare
equal for 88 bytes, both with SHA-256
`9943dcd929ed73f90c0a377ed615475e599d1ae6b60e9243438c146009649cb7`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,716 / 5,469 (49.66%) | 1 | 2,752 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,145 / 4,791 (44.77%) | 0 | 2,646 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 22-word `func_151D8D5C`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
