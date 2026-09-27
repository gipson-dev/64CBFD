# Game paired state-clear callback match - 2026-09-27

## Result

`func_1519F108` and adjacent structural twin `func_1519F168` are independently
byte-exact across all 24 words and 96 bytes at `0x1519F108..0x1519F168` and
`0x1519F168..0x1519F1C8`. Fresh totals are 2,780 / 5,469 (50.83%) exact C
functions overall and 2,209 / 4,791 (46.11%) in Game.

## Recovery

Both false zero-return placeholders now recover the original null-gated
record update. The routine follows the link at object offset `0x98`; when the
record exists, state 6 clears the first word at record offset `0x58`, and
state 7 clears the third word at offset `0x60`. The functions differ only in
their final callback: `func_1519F108` calls `func_151478F4`, while
`func_1519F168` calls `func_15147928`.

IDO preserves the frame, pointer loads, control flow, call delay slot, and
epilogue, but folds the shared `record + 0x58` base into two stores and assigns
the state lifetime to `a0`. Explicit and volatile pointer variants emit the
same 23-word body. Eight independent guarded rows per function therefore
assert that exact compiler output, insert the missing base calculation, and
normalize seven scheduling/register words. Neither callback relocation is
replaced.

## Evidence

Linked ELF offsets `0x1DF108` and `0x1DF168` compare equal to decompressed
retail offsets `0x1CC5B8` and `0x1CC618` across their complete 96-byte spans.
Their respective SHA-256 values are
`c30604a30fce7acfc9c4508dc25d815ae938bc8fb15c221b8351c2fe3f46b2c1` and
`15a54430576641fbb8f849e8250fb8f39c1527d06c5829a84d6c89597d227412`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,780 / 5,469 (50.83%) | 1 | 2,688 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,209 / 4,791 (46.11%) | 0 | 2,582 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, exhaustive all-object nonmatching
ELF rebuild, fresh progress and matcher, independent 96-byte span hashes, and
direct byte comparisons pass. The repository-wide padded replacement build,
project tool checks, padding-tool unit tests, outer nonmatching build, and
working-tree whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_151A09B4`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
