# Game stack-record forwarder match - 2026-09-27

## Result

`func_150AF738` is byte-exact across all 22 words and 88 bytes at
`0x150AF738..0x150AF790`. Fresh totals are 2,754 / 5,469 (50.36%) exact C
functions overall and 2,183 / 4,791 (45.56%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail instead accepts a
signed halfword, byte, and third argument; builds a seven-byte stack record
containing byte values `1`, `-1`, and `2`, the first argument as a halfword,
and a final zero byte; then calls `func_1515FF74` with that record, zero, the
second argument, and the third argument.

The typed C recovers the complete 0x20-byte frame, narrow-argument handling,
record layout, call contract, halfword-store delay slot, and epilogue. IDO
emits every retail operation but rotates fifteen independent prologue/setup
words. Function-scoped guards restore that schedule. They do not supply a
constant, memory access, argument value, branch, call, relocation, delay-slot
operation, or return behavior.

## Evidence

Linked ELF offset `0xEF738` and decompressed retail offset `0xDCBE8` compare
equal across the complete 88-byte span. Both have SHA-256
`d2d5a6e1f37e723929f923d806d0242d7c073643f4b11c05f093a484cb5c6a7f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,754 / 5,469 (50.36%) | 1 | 2,714 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,183 / 4,791 (45.56%) | 0 | 2,608 |
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

Continue with 24-word `func_150BB700`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
