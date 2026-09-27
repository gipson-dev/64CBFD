# Game six-ID type predicate match - 2026-09-27

## Result

`func_1503378C` is byte-exact across all 22 words and 88 bytes at
`0x1503378C..0x150337E4`. Fresh totals are 2,751 / 5,469 (50.30%) exact C
functions overall and 2,180 / 4,791 (45.50%) in Game.

## Recovery

The function reads the type byte at object offset `0x01` and an unsigned
halfword at context offset `0x84`. It returns zero only when the type is
`0x11` and the halfword is one of `0x3E`, `0x3D`, `0x41`, `0xD9`, `0x138`,
or `0x139`; all other combinations return one.

A direct nested predicate preserves retail's early halfword load and chained
equality tests. IDO emits the complete function without expected-word guards,
including each compare value in the preceding branch delay slot, the final
branch-likely result setup, and both return paths.

## Evidence

Linked ELF offset `0x7378C` and decompressed retail offset `0x60C3C` compare
equal across the complete 88-byte span. Both have SHA-256
`aaec9a5cbe36b7e1038be5629099576d751350b6e0d8617a4a68bf92f1300564`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,751 / 5,469 (50.30%) | 1 | 2,717 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,180 / 4,791 (45.50%) | 0 | 2,611 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 88-byte span hashes, and `cmp` pass. The combined closing
replacement build, project tool checks, all seven padding-tool unit tests,
outer `NON_MATCHING=1` build, and staged `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_15044DE8`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the previously documented
lower-difference rows parked.
