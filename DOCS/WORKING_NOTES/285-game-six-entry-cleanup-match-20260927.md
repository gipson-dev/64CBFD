# Game six-entry cleanup match - 2026-09-27

## Result

`func_150D2054` is byte-exact across all 23 words and 92 bytes at
`0x150D2054..0x150D20B0`. Fresh totals are 2,789 / 5,469 (51.00%) exact C
functions overall and 2,218 / 4,791 (46.30%) in Game.

## Recovery

The false zero-return placeholder now walks six pointer slots at object
offsets `0x4C..0x60`. Every non-null entry is passed to `func_1516972C` before
the loop advances.

The counter remains a signed working value but is narrowed to `u8` after each
increment, reproducing retail's `andi`, comparison, and branch-delay update.
Writing the address as indexed array access keeps IDO's base-before-index
`addu` operand order. Together these source shapes recover the complete loop,
including the branch-likely null path, without guarded retail words.

## Evidence

Linked ELF offset `0x112054` and decompressed retail offset `0xFF504` compare
equal across the complete 92-byte span. Both have SHA-256
`eeac0c230700015d8097afd16b38ab2414d2e649eff75b81f111f9843feccfaa`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,789 / 5,469 (51.00%) | 1 | 2,679 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,218 / 4,791 (46.30%) | 0 | 2,573 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching ELF relink, fresh
progress and matcher, independent 92-byte hashes, and direct byte comparison
pass. The replacement build, project tool checks, padding-tool unit tests,
outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 25-word `func_150D32FC`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
