# Game two-way type dispatch match - 2026-09-27

## Result

`func_1513BA78` is byte-exact across all 23 words and 92 bytes at
`0x1513BA78..0x1513BAD4`. Fresh totals are 2,766 / 5,469 (50.58%) exact C
functions overall and 2,195 / 4,791 (45.82%) in Game.

## Recovery

The existing C already represented the retail behavior: it reads the type byte
at record offset `0x48`, calls `func_15109064(record, value, byte)` for type
`1`, calls `func_151BA468(record, value, byte)` for type `2`, and otherwise
returns without dispatching.

The mismatch came from missing callee prototypes. With old-style implicit
calls, IDO kept the normalized byte in `a3` and moved it back into `a2` in each
call delay slot. Declaring both callees with their three argument types keeps
the normalized byte in `a2`, moves the argument normalization ahead of the
saved return address, and leaves the call delay slots as retail `nop`s. Every
word then matches directly from C; no guarded retail words are needed.

## Evidence

Linked ELF offset `0x17BA78` and decompressed retail offset `0x168F28` compare
equal across the complete 92-byte span. Both have SHA-256
`151da9e5c2e45abdfc2658142acaddc654729cd22fb97e3cfe3246a6457022fe`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,766 / 5,469 (50.58%) | 1 | 2,702 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,195 / 4,791 (45.82%) | 0 | 2,596 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 92-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 37-word `func_15144598`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
