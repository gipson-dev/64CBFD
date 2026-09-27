# Game paired endpoint update match - 2026-09-27

## Result

`func_1518A360` is byte-exact across all 24 words and 96 bytes at
`0x1518A360..0x1518A3C0`. Fresh totals are 2,776 / 5,469 (50.76%) exact C
functions overall and 2,205 / 4,791 (46.02%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail only acts when
the byte argument is marker `0x2D`. It compares the selected endpoint in the
object word at offset `0x188` against two source words. A match against source
word zero installs source word one and byte nine; a match against source word
one installs source word zero and byte eight. The companion byte is stored at
object offset `0x18D`.

The established paired-record C shape reproduces 23 of the 24 words directly.
IDO reverses the operands of the second commutative equality branch, emitting
`bne a2,t9` where retail uses `bne t9,a2`. One guarded word at function offset
`0x40` checks the compiler's exact input word and selects retail's equivalent
operand order. No relocation or behavioral change is involved.

## Evidence

Linked ELF offset `0x1CA360` and decompressed retail offset `0x1B7810` compare
equal across the complete 96-byte span. Both have SHA-256
`c49fa92800abfcf75e48c6d36597feb3d3c75ae58cb91fb76bb2d503beebd0ed`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,776 / 5,469 (50.76%) | 1 | 2,692 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,205 / 4,791 (46.02%) | 0 | 2,586 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 96-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word `func_151904BC`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
