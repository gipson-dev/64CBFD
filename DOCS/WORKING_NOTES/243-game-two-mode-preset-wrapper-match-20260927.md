# Game two-mode preset wrapper match - 2026-09-27

## Result

`func_151D4D58` is byte-exact across all 21 words and 84 bytes at
`0x151D4D58..0x151D4DAC`. Fresh totals are 2,746 / 5,469 (50.21%) exact C
functions overall and 2,175 / 4,791 (45.40%) in Game.

## Recovery

The function takes an object pointer and calls `func_151D469C` twice. The first
call selects mode zero and the second selects mode one; both pass the same
constant preset values `0x50`, `0xFF`, and one. Its caller ignores the return
value, and the recovered `void (u8 *)` signature reflects the observed
behavior.

The direct C compiles to the complete retail instruction sequence without any
expected-word guards. This includes the `0x20`-byte frame, argument home slot,
fifth stack argument for each call, both call relocations and delay slots, and
the epilogue.

## Evidence

Linked ELF offset `0x214D58` and decompressed retail offset `0x202208` compare
equal across the complete 84-byte span. Both have SHA-256
`29e2cc5f82d51a75d33b58200a7c9fdd50236cb5e467c21010ba938403e94a61`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,746 / 5,469 (50.21%) | 1 | 2,722 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,175 / 4,791 (45.40%) | 0 | 2,616 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 84-byte span hashes, and `cmp` pass. The repository-wide
padded-object rebuild, project tool checks, all seven padding-tool unit tests,
outer `NON_MATCHING=1` build, and `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word `func_151E7E9C`, the next unparked Game C row in the
fresh queue at 20 real instruction differences. Keep the previously documented
lower-difference rows parked.
