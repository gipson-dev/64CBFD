# Game enabled player state initializer match - 2026-09-27

## Result

`func_15181D70` is byte-exact across all 22 words and 88 bytes at
`0x15181D70..0x15181DC8`. Fresh totals are 2,775 / 5,469 (50.74%) exact C
functions overall and 2,204 / 4,791 (46.00%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail initializes the
selected player's state by storing float constant `D_800A72B0` into
`D_800DDDD8`, clearing the matching `D_800DDDC8` scalar and both components of
`D_800DDDE8`, and setting `D_800DDE20` to one.

The neighboring recovered `func_15181DC8` clears the same fields and disables
the entry. Mirroring its indexed field order while substituting the constant
and enable value reproduces retail's floating-point zero lifetime, address
calculations, stores, and epilogue directly from C. No guarded retail words are
needed.

## Evidence

Linked ELF offset `0x1C1D70` and decompressed retail offset `0x1AF220` compare
equal across the complete 88-byte span. Both have SHA-256
`9bc443d34ee264cb7c11bf0e6e84c6c9ca2dbd088fbb4005afd2514acd0ab072`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,775 / 5,469 (50.74%) | 1 | 2,693 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,204 / 4,791 (46.00%) | 0 | 2,587 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 88-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word `func_1518A360`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
