# Game event state/teardown handler match - 2026-09-27

## Result

`func_150F4CFC` is byte-exact across all 24 words and 96 bytes at
`0x150F4CFC..0x150F4D5C`. Fresh totals are 2,792 / 5,469 (51.05%) exact C
functions overall and 2,221 / 4,791 (46.36%) in Game.

## Recovery

The false zero-return placeholder now handles two event bytes. Event `0x4E`
clears object byte `0x71`, derives the embedded state record at object offset
`0x170`, and ORs bits `0` and `2` into its flag byte at record offset `0x24`
(object offset `0x194`). Event `0x4F` passes the object to `func_1516972C` for
teardown. Other events return without changing the object.

Raw byte-pointer source let IDO flatten both flag accesses to object offset
`0x194`, shortened the body, and moved the load ahead of the clear. A minimal
typed embedded-state record preserves retail's separate `arg0 + 0x170` base,
the `+0x24` member access, clear/load/store order, branch-delay flag store, and
alternate teardown path. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x134CFC` and decompressed retail offset `0x1221AC` compare
equal across the complete 96-byte span. Both have SHA-256
`5bb7259de0c805b8e28072d2011a451b4ec747eae9f5a5a69e5aacd1dc61f8c7`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,792 / 5,469 (51.05%) | 1 | 2,676 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,221 / 4,791 (46.36%) | 0 | 2,570 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching ELF relink, fresh
progress and matcher, independent 96-byte hashes, and direct byte comparison
pass. The replacement build, project tool checks, padding-tool unit tests,
outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 29-word `func_151002BC`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
