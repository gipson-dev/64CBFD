# Game linked-record event callback match - 2026-09-27

## Result

`func_151A0950` is byte-exact across all 25 words and 100 bytes at
`0x151A0950..0x151A09B4`. Fresh totals are 2,798 / 5,469 (51.16%) exact C
functions overall and 2,227 / 4,791 (46.48%) in Game.

## Recovery

The zero-return placeholder was a three-argument event callback with an 8-bit
third parameter. Only event `0xA` is handled. The callback follows the link
pointer stored at object offset `0x98` and stops if the resulting record is
null. A record is accepted when either its 32-bit owner at offset `0x18`
matches the descriptor's first word or its ID byte at offset `0x1C` matches
the descriptor byte at offset 4. Accepted records call `func_1519F48C` with
the original object.

An initial nested short-circuit form was behaviorally correct but made IDO
emit a branch-likely outer exit and one extra return-address load. Materializing
the link before the event check places its load in retail's ordinary branch
delay slot and restores the 25-word extent. Naming the record owner separately
then reuses the dead link register `v1`, aligning all four comparison
temporaries with retail.

The complete function matches directly from C. No guarded instruction rows or
assembly replacements are required.

## Evidence

Linked ELF offset `0x1E0950` and decompressed retail offset `0x1CDE00` compare
equal across the complete 100-byte span. Both have SHA-256
`33dcd9647ac0531f73903a0cf150dfec1dea4c1f0047fadccf54342cc478efbb`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,798 / 5,469 (51.16%) | 1 | 2,670 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,227 / 4,791 (46.48%) | 0 | 2,564 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 100-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 24-word `func_151A9060`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
