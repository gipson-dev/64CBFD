# Game mode-flag toggle match - 2026-09-27

## Result

`func_150C5310` is byte-exact across its 24-word, 96-byte tracked span at
`0x150C5310..0x150C5370`. Fresh totals are 2,729 / 5,470 exact C functions
overall and 2,158 / 4,792 in Game.

## Recovery

The routine calls `func_150C5280` and updates bit `0x20000` in the caller's
word at offset `0x60`. A true result sets the bit; a false result clears it.
The routine returns `1` in either case.

A typed `u32 *` argument and direct indexed update reproduce retail's stack
frame, saved argument, call and delay slot, two branch bodies, shared return,
and epilogue without guarded retail-word replacement. The function body uses
21 instructions; the tracked retail extent also includes three trailing zero
padding words, which the generated-slice padding tool preserves exactly.

## Evidence

Linked ELF offset `0x105310` and decompressed retail offset `0xF27C0` compare
equal for all 96 bytes. Both spans have SHA-256
`0179e738632a005405b2a6cbec57c8da5a8f6b66f9707772bf19f68c884fcdf7`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,729 / 5,470 (49.89%) | 1 | 2,740 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,158 / 4,792 (45.03%) | 0 | 2,634 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
96-byte span hashes and `cmp`, replacement build, project tool checks, all six
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 24-word `func_150E2FC0`, the next ordinary Game C candidate
with 20 real differences.
