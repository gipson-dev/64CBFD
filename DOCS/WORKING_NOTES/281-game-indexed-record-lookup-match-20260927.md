# Game indexed-record lookup match - 2026-09-27

## Result

`func_1508855C` is byte-exact across all 36 words and 144 bytes at
`0x1508855C..0x150885EC`. Fresh totals are 2,785 / 5,469 (50.92%) exact C
functions overall and 2,214 / 4,791 (46.21%) in Game.

## Recovery

The existing C already recovers the original lookup behavior. It rejects a
null record table, derives a record index from `arg0` relative to
`D_800CC2D0` in `0x32C`-byte units, returns zero for the base record, and
rejects tables with fewer than two active entries. It then scans the signed
index byte at offset `0x31` in each `0x84`-byte record from entry one onward,
returning the matching entry number or `-1`.

Direct C reproduces the complete 36-word instruction count and behavior, but
IDO assigns the table, index, count, iterator, and record pointer to different
registers and chooses equivalent branch scheduling. Twenty-two guarded rows
assert the exact compiler output and normalize only those independent register
lifetimes and control-flow words. The guarded `lui`/load pair retains
`R_MIPS_HI16:D_800872A0` and `R_MIPS_LO16:D_800872A0` on both sides; no
relocation is moved or retargeted.

## Evidence

Linked ELF offset `0xC855C` and decompressed retail offset `0xB5A0C` compare
equal across the complete 144-byte span. Both have SHA-256
`8e59eaab129aa398368550fe589cf0991cec44face9740101ec18eb00a61c74d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,785 / 5,469 (50.92%) | 1 | 2,683 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,214 / 4,791 (46.21%) | 0 | 2,577 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, exhaustive all-object nonmatching
ELF rebuild, fresh progress and matcher, independent 144-byte hashes, and
direct byte comparison pass. The replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 26-word `func_150A6500`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
