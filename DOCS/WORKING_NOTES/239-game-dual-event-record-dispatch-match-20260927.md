# Game dual event-record dispatch match - 2026-09-27

## Result

`func_151AA17C` is byte-exact across all 21 words and 84 bytes at
`0x151AA17C..0x151AA1D0`. Fresh totals are 2,742 / 5,469 (50.14%) exact C
functions overall and 2,171 / 4,791 (45.31%) in Game.

## Recovery

The function constructs a local record from the target pointer at object
offset `0x18` and code byte at offset `0x1C`. It submits that record to
`func_15147D64` and `func_151494E0`, both with selector `0xA`, then forwards
the original object to `func_1519F3B8`.

A volatile retained pointer expresses the record lifetime across the first
call and keeps the C body at retail's 21-word extent. The source supplies 11
retail words directly. Ten expected-word-guarded entries restore retail's
independent return-address save, incoming-object lifetime, target/code
temporaries, record placement at `sp+0x1C`, and retained-pointer slot at
`sp+0x18`. No relocation is patched: all three call instructions and their
delay slots already match from the recovered C control flow.

## Evidence

Linked ELF offset `0x1EA17C` and decompressed retail offset `0x1D762C`
compare equal across the complete 84-byte span. Both have SHA-256
`504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,742 / 5,469 (50.14%) | 1 | 2,726 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,171 / 4,791 (45.31%) | 0 | 2,620 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
84-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_151AA210`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
