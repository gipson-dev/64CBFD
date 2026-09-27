# Game paired-record update twin match - 2026-09-27

## Result

`func_1510A8CC` is byte-exact across its complete 25-word / 100-byte tracked
layout at `0x1510A8CC..0x1510A930`. The function contains 23 executable words
followed by two retail layout-padding words. Fresh totals are 2,764 / 5,469
(50.54%) exact C functions overall and 2,193 / 4,791 (45.77%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail is an executable
twin of adjacent `func_1510A870`: it only acts for event `0x2D`, compares the
destination word at `arg0 + 0x28` against two source words, and replaces a
matching selection with the opposite source word and its companion byte.

The same recovered C emits all semantic and scheduling words except the
operand order of the second equality branch. The one guarded word at function
offset `0x40` changes IDO's `bne a2,t9` to retail's commutatively equivalent
`bne t9,a2` without changing behavior or branch displacement. The padding
tool preserves the two zero words at offsets `0x5C` and `0x60` that complete
this twin's longer tracked layout.

## Evidence

Linked ELF offset `0x14A8CC` and decompressed retail offset `0x137D7C` compare
equal across the complete 100-byte span. Both have SHA-256
`f637c9f80def4be39e6e23fbc94349b62bb30814b7e22c6ffc593287695455ef`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,764 / 5,469 (50.54%) | 1 | 2,704 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,193 / 4,791 (45.77%) | 0 | 2,598 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 100-byte span hashes, and `cmp` pass.
The repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and working-tree
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_1512D6F0`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
