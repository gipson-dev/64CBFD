# Game null-gated event-byte copy match - 2026-09-27

## Result

`func_15023870` is byte-exact across all 24 words and 96 bytes at
`0x15023870..0x150238D0`. Fresh totals are 2,749 / 5,469 (50.27%) exact C
functions overall and 2,178 / 4,791 (45.46%) in Game.

## Recovery

The function handles only event pair `(0xB, 2)`. It passes the fourth argument
to `func_1505EEF4`, returns without mutation when the resolved object is null,
and otherwise copies byte `0x3B` from that object into byte `0x2A` of the
`D_800C35F0` record indexed by the third argument.

The initial direct expression exposed an early source-byte load because it
omitted retail's null gate. Restoring the gate recovered both the actual
behavior and the complete instruction schedule. The final C compiles without
expected-word guards, including the argument spill, branch-likely exit,
resolver call and delay slot, null branch, indexed global lookup, two epilogue
paths, and two alignment words.

## Evidence

Linked ELF offset `0x63870` and decompressed retail offset `0x50D20` compare
equal across the complete 96-byte span. Both have SHA-256
`31b6a4a8e8d8ca077e34240978a92a22b54ac3effa545273e03e30b0386abf36`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,749 / 5,469 (50.27%) | 1 | 2,719 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,178 / 4,791 (45.46%) | 0 | 2,613 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 96-byte span hashes, and `cmp` pass. The repository-wide
padded replacement build, project tool checks, all seven padding-tool unit
tests, outer `NON_MATCHING=1` build, and staged `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 32-word `func_15033328`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the previously documented
lower-difference rows parked.
