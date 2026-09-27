# Game variadic formatting wrapper match - 2026-09-27

## Result

`func_151EFF94` is byte-exact across all 23 words and 92 bytes at
`0x151EFF94..0x151EFFF0`. Fresh totals are 2,783 / 5,469 (50.89%) exact C
functions overall and 2,212 / 4,791 (46.17%) in Game.

## Recovery

The false zero-return placeholder now recovers the original two-fixed-argument
variadic formatting wrapper. It calls `func_100020D0` with `func_151EFF70` as
the output callback, the destination and format pointers, and the first
variadic argument address. A nonnegative formatted length causes a trailing
zero byte at `destination[length]`; the formatter result is returned unchanged.

The key source shape is the actual two-fixed-argument signature and the
existing project idiom `&arg1 + 1` for the variadic cursor. Naming a third
fixed argument made IDO home it too early and forward the format pointer with
a register move. The corrected shape reproduces retail's four argument homes,
callback address relocation pair, stack reloads, call delay slot, result
lifetime, null termination, and epilogue without guarded words.

## Evidence

Linked ELF offset `0x22FF94` and decompressed retail offset `0x21D444` compare
equal across the complete 92-byte span. Both have SHA-256
`21bed0d95f6457b0e0ebf8ba8b78072ed1f6f7883ef19bf31c9a327fbe457102`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,783 / 5,469 (50.89%) | 1 | 2,685 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,212 / 4,791 (46.17%) | 0 | 2,579 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and relocation-aware disassembly, nonmatching linked
ELF build, fresh progress and matcher, independent 92-byte hashes, and direct
byte comparison pass. The padded replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_15044CE4`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
