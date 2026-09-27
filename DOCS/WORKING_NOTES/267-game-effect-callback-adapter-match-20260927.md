# Game effect callback adapter match - 2026-09-27

## Result

`func_15159BB0` is byte-exact across all 22 words and 88 bytes at
`0x15159BB0..0x15159C08`. Fresh totals are 2,770 / 5,469 (50.65%) exact C
functions overall and 2,199 / 4,791 (45.90%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail receives a
seven-slot effect callback signature. Its first three float arguments become a
three-component position vector, while a second local vector is initialized to
zero. The seventh argument is an effect record whose bytes at offsets `0x0C`
and `0x01` are forwarded with those vectors to `func_15159890`.

Typing the leading coordinates as `f32` places them in `f12`, `f14`, and `a2`
under the o32 ABI. Keeping the three unused callback slots before the record
pointer places that pointer at retail's seventh-argument stack location. The
straight-line vector construction reproduces all frame, home-slot, zero-store,
byte-load, call-delay, and epilogue scheduling directly from C. No guarded
retail words are needed.

## Evidence

Linked ELF offset `0x199BB0` and decompressed retail offset `0x187060` compare
equal across the complete 88-byte span. Both have SHA-256
`4ca84258ab41695df242af9177bdc89d911377839c1cc187058020c2c4d30d88`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,770 / 5,469 (50.65%) | 1 | 2,698 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,199 / 4,791 (45.90%) | 0 | 2,592 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 88-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_15172C50`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
