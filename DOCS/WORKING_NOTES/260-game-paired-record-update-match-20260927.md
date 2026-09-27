# Game paired-record update match - 2026-09-27

## Result

`func_1510A870` is byte-exact across all 23 words and 92 bytes at
`0x1510A870..0x1510A8CC`. Fresh totals are 2,763 / 5,469 (50.52%) exact C
functions overall and 2,192 / 4,791 (45.75%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail only acts when
the byte argument is `0x2D`. The destination record starts at `arg0 + 0x28`
and contains a selected word followed by its companion byte. The source
contains two candidate words at offsets `0` and `4`, with companion bytes at
offsets `8` and `9`.

When source word zero matches the destination word, retail selects source word
one and byte nine. Otherwise, when source word one matches, it selects source
word zero and byte eight. If neither word matches, the destination is left
unchanged.

IDO emits every semantic and scheduling word from the recovered C except the
operand order of the second equality branch. A plain comparison produces
`bne a2,t9`; retail uses the commutatively equivalent `bne t9,a2`. Subtraction
and XOR comparison experiments selected retail's branch operands but changed
the later byte-load temporary from `t0` to `t1`. An explicit early return
restored that lifetime but IDO canonicalized the branch operands again. The
single guarded word at function offset `0x40` therefore selects retail's
operand order without changing behavior or branch displacement.

## Evidence

Linked ELF offset `0x14A870` and decompressed retail offset `0x137D20` compare
equal across the complete 92-byte span. Both have SHA-256
`fd478fda75bdea9e1b7e81f5eff7d3c810f4609bb7f137f6a493be6fde6e5a48`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,763 / 5,469 (50.52%) | 1 | 2,705 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,192 / 4,791 (45.75%) | 0 | 2,599 |
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

Continue with 25-word `func_1510A8CC`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
