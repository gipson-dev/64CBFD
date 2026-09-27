# Game guarded mode-4 dispatcher match - 2026-09-27

## Result

`func_15044DE8` is byte-exact across all 22 words and 88 bytes at
`0x15044DE8..0x15044E40`. Fresh totals are 2,752 / 5,469 (50.32%) exact C
functions overall and 2,181 / 4,791 (45.52%) in Game.

## Recovery

The function is the guarded mode-4 variant of the neighboring recovered
dispatch helpers. It tests bytes `0x104` and `0x125` in `D_800CC2D0`, then
tests that `D_800C35EA` is not one. When all three conditions pass it calls
`func_1505D024` with the object, mode four, the halfword at offset `0x7A`, and
`-1`; otherwise it returns without action.

The direct nested condition preserves retail's shared object pointer and
short-circuit exits. IDO emits the complete function without expected-word
guards, including both branch-likely epilogues, the global-state relocation,
preloaded mode and sentinel arguments, and the call delay slot.

## Evidence

Linked ELF offset `0x84DE8` and decompressed retail offset `0x72298` compare
equal across the complete 88-byte span. Both have SHA-256
`2e614c823ff7b9d1a357dc862d044a336d070d58962e14ad022382c7e6c3a564`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,752 / 5,469 (50.32%) | 1 | 2,716 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,181 / 4,791 (45.52%) | 0 | 2,610 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 88-byte span hashes, and `cmp` pass. The
repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and staged
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_15088218`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Its arithmetic behavior is
already recovered, but initial pointer-local, argument-rewrite, and
explicit-offset source probes did not reproduce retail's `a1` index / `t6`
offset lifetime. A partial `index * 33` local still allocated the intermediate
to `a1`, while assigning the table base into the incoming argument changed the
null test to a branch-likely. The original C was restored unchanged. Keep the
previously documented lower-difference rows parked.
