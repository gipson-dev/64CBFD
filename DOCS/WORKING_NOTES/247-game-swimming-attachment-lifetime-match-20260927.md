# Game swimming-attachment lifetime match - 2026-09-27

## Result

`func_15033328` is byte-exact across all 32 words and 128 bytes at
`0x15033328..0x150333A8`. Fresh totals are 2,750 / 5,469 (50.28%) exact C
functions overall and 2,179 / 4,791 (45.48%) in Game.

## Recovery

The existing C already described the swimming-attachment lifetime behavior:
it disables the callback in global state one, resets the lifetime to 30 when
the attachment or height test fails, subtracts `D_800BE9E4` while sufficient
time remains, and returns one when the lifetime expires.

Its original control flow left the zero return value dead until the shared
epilogue. IDO consequently used `v0` for the timing global and emitted a
different subtraction/return schedule. Keeping a zero result live and using it
on the early returns allocates the timing global to `v1`, reuses the dead
second argument register for the counter, and reproduces retail's direct
returns. No expected-word guards are needed.

## Evidence

Linked ELF offset `0x73328` and decompressed retail offset `0x607D8` compare
equal across the complete 128-byte span. Both have SHA-256
`41e163c146a74b2190cd422401cae4e101ac44a0b906369e1e75486b2d3215e8`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,750 / 5,469 (50.28%) | 1 | 2,718 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,179 / 4,791 (45.48%) | 0 | 2,612 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 128-byte span hashes, and `cmp` pass. The repository-wide
padded replacement build, project tool checks, all seven padding-tool unit
tests, outer `NON_MATCHING=1` build, and staged `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_1503378C`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the previously documented
lower-difference rows parked.
