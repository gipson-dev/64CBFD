# Game two-stage forwarder match - 2026-09-27

## Result

`func_150FB1E8` is byte-exact across all 22 words and 88 bytes at
`0x150FB1E8..0x150FB240`. Fresh totals are 2,759 / 5,469 (50.45%) exact C
functions overall and 2,188 / 4,791 (45.67%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail accepts five
arguments and forwards them to `func_151D710C`. It then passes that result as
the first argument to `func_15157F80` while replaying original arguments two
through five.

Assigning the first call result back to the first source argument makes the
cross-call lifetime explicit. IDO naturally emits the 0x20-byte frame,
argument homes and reloads, both fifth-argument stack stores, both calls and
delay slots, and the epilogue without guarded words.

## Evidence

Linked ELF offset `0x13B1E8` and decompressed retail offset `0x128698` compare
equal across the complete 88-byte span. Both have SHA-256
`fbb5d8ad1f5b61fff246fd8f6872d9f64fb94547d8705287f14c163b98474c00`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,759 / 5,469 (50.45%) | 1 | 2,709 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,188 / 4,791 (45.67%) | 0 | 2,603 |
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

Continue with 23-word `func_150FB240`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
