# Game fixed-point/float record value match - 2026-09-27

## Result

`func_15088218` is byte-exact across all 22 words and 88 bytes at
`0x15088218..0x15088270`. Fresh totals are 2,753 / 5,469 (50.34%) exact C
functions overall and 2,182 / 4,791 (45.54%) in Game.

## Recovery

The function returns zero when `D_800872A0` is null. Otherwise it selects the
`arg0` record from the 0x84-byte table and returns the signed halfword at
offset `0x24`, shifted left four, plus the truncated float at offset `0x08`
multiplied by 16.0.

The refined C makes the incoming index, computed record address, and signed
halfword lifetime explicit. IDO emits the complete arithmetic and memory
behavior, but schedules the opening table-base load ahead of the saved index,
branches before finishing the 132-byte stride, and reverses the final
commutative addition. Nine function-scoped guards restore those equivalent
scheduling words and preserve the `D_800872A0` HI16/LO16 relocations. No guard
supplies a branch condition, behavior constant, memory access, conversion, or
floating-point operation.

## Evidence

Linked ELF offset `0xC8218` and decompressed retail offset `0xB56C8` compare
equal across the complete 88-byte span. Both have SHA-256
`e5d5d321d70aa26986e0693c90892be508a283fd44a0fcebe53249e772f14a7f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,753 / 5,469 (50.34%) | 1 | 2,715 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,182 / 4,791 (45.54%) | 0 | 2,609 |
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

Continue with 22-word `func_150AF738`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
