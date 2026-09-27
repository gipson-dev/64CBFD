# Game event-key forwarder match - 2026-09-27

## Result

`func_150D32FC` is byte-exact across its tracked 25 words and 100 bytes at
`0x150D32FC..0x150D3360`. Fresh totals are 2,790 / 5,469 (51.01%) exact C
functions overall and 2,219 / 4,791 (46.32%) in Game.

## Recovery

The false zero-return placeholder now accepts only event byte `0x34`, derives
the record at object offset `0x28`, and compares the incoming key byte against
record byte `0x51` (object offset `0x79`). On a match it calls
`func_150D278C` with the record's first word, the address at record offset
`0x10`, and object bytes `0x0C` and `0x01`.

Initializing the derived record pointer before a short-circuit `&&` condition
gives IDO the original register lifetimes and schedule: the object reload in
the event branch delay slot, retained `v0` record base, object and incoming
key loads, branch-likely return path, and four call arguments. The generated
slice padder retains the two original layout nops after the 23-word function
body. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x1132FC` and decompressed retail offset `0x1007AC` compare
equal across the complete 100-byte span. Both have SHA-256
`33eb62e07e9e46c86be7d1d80a40c3465c16c01b981521dbeef75de32cf2af44`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,790 / 5,469 (51.01%) | 1 | 2,678 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,219 / 4,791 (46.32%) | 0 | 2,572 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching ELF relink, fresh
progress and matcher, independent 100-byte hashes, and direct byte comparison
pass. The replacement build, project tool checks, padding-tool unit tests,
outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 26-word `func_150DEC28`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
