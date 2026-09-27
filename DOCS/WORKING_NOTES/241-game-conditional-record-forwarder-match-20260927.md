# Game conditional record forwarder match - 2026-09-27

## Result

`func_151CF844` is byte-exact across all 21 words and 84 bytes at
`0x151CF844..0x151CF898`. Fresh totals are 2,744 / 5,469 (50.17%) exact C
functions overall and 2,173 / 4,791 (45.36%) in Game.

## Recovery

The function loads the record pointer at object offset `0x98`. When the
record's first word is nonzero, it calls `func_15169850` with the incoming
selector, narrowed byte argument, record pointer, adjacent `record + 4`
pointer, and original object. A zero first word returns immediately.

Typing the wrapper as `void (u8 *, s32, u8)` and retaining the local record
pointer reproduces retail directly. IDO emits the original three incoming
argument spills, big-endian byte reload, record-pointer spill, branch-likely
early return, fifth stack argument, call relocation, delay slot, and shared
frame teardown. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x20F844` and decompressed retail offset `0x1FCCF4`
compare equal across the complete 84-byte span. Both have SHA-256
`63e2de29d6ff3c9de2f9df2244a8c564c82f5d4a7a354bfda47b93ce08cf6b4e`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,744 / 5,469 (50.17%) | 1 | 2,724 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,173 / 4,791 (45.36%) | 0 | 2,618 |
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

Continue with 21-word `func_151D10E4`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
