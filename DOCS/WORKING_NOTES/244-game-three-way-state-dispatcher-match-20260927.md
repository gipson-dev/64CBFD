# Game three-way state dispatcher match - 2026-09-27

## Result

`func_151E7E9C` is byte-exact across all 23 words and 92 bytes at
`0x151E7E9C..0x151E7EF8`. Fresh totals are 2,747 / 5,469 (50.23%) exact C
functions overall and 2,176 / 4,791 (45.42%) in Game.

## Recovery

The function reads signed state byte `D_800E0BE9` once and dispatches one of
three values to `func_10017870`. State two sends one, state zero sends two, and
all other states send four. The recovered `void (void)` signature agrees with
both known callers, which ignore a return value.

Two explicit conditions with early returns reproduce retail's control flow
directly. IDO retains the first global load in `v0` for both comparisons and
emits the complete sequence without expected-word guards, including the two
global relocations, three call relocations, branch delays, early epilogues,
and shared return.

## Evidence

Linked ELF offset `0x227E9C` and decompressed retail offset `0x21534C` compare
equal across the complete 92-byte span. Both have SHA-256
`9e1f4c78ce7ec52e9380fa7c74c7e84150751076fb47ad086646a1af136cbe05`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,747 / 5,469 (50.23%) | 1 | 2,721 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,176 / 4,791 (45.42%) | 0 | 2,615 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full link, fresh progress and
matcher, independent 92-byte span hashes, and `cmp` pass. The repository-wide
padded-object rebuild, project tool checks, all seven padding-tool unit tests,
outer `NON_MATCHING=1` build, and `git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_15022190`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the previously documented
lower-difference rows parked.
