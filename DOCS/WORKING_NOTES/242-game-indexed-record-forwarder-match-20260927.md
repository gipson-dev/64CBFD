# Game indexed record forwarder match - 2026-09-27

## Result

`func_151D10E4` is byte-exact across all 21 words and 84 bytes at
`0x151D10E4..0x151D1138`. Fresh totals are 2,745 / 5,469 (50.19%) exact C
functions overall and 2,174 / 4,791 (45.38%) in Game.

## Recovery

The function narrows its third argument to a byte, reads the optional target
at object offset `0x1D4`, and returns zero when that target is null. Otherwise
it selects one 12-byte entry from `D_800AAF9C`, calls `func_15143134` with the
entry, incoming second argument, and target, then returns one.

The recovered C compiles to the correct 21-word size, frame, call, return
values, and null-gated behavior. IDO nevertheless homes and reloads the byte
argument, allocates the target to `a3`, and speculatively materializes the
table base before the null test. Source probes using a typed 12-byte table,
full-width argument with casts or masks, positive and early-return branches,
typed owner fields, locals, and direct repeated field expressions did not
produce retail's schedule.

Twelve expected-word guards restore retail's equivalent byte normalization,
target and stride register lifetimes, null-path branch schedule, and table
load. The `D_800AAF9C` HI16 relocation moves from source offset `0x14` to
`0x2C`; its LO16 relocation remains at `0x30` with the retail register. The
`func_15143134` call relocation at `0x38` and the epilogue are not patched.

## Evidence

Linked ELF offset `0x2110E4` and decompressed retail offset `0x1FE594`
compare equal across the complete 84-byte span. Both have SHA-256
`be6f6bade86c0c2f86c7f70e65b0555e2d868b0a1a06e05aba5523cde2bffff9`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,745 / 5,469 (50.19%) | 1 | 2,723 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,174 / 4,791 (45.38%) | 0 | 2,617 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object, repository-wide padded-object rebuild, full link, fresh
progress and matcher, independent 84-byte span hashes, `cmp`, and
`git diff --check` pass. The replacement build, project tool checks, all seven
padding-tool unit tests, and outer `NON_MATCHING=1` build also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 21-word `func_151D4D58`, the next unparked Game C row in the
fresh queue. Keep the previously documented lower-difference rows parked.
