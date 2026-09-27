# Game float damping threshold match - 2026-09-27

## Result

`func_15149BF4` is byte-exact across all 25 words and 100 bytes at
`0x15149BF4..0x15149C58`. Fresh totals are 2,768 / 5,469 (50.61%) exact C
functions overall and 2,197 / 4,791 (45.86%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail reads the two
float fields at offsets `0x2C` and `0x30` plus a damping factor at offset
`0x150`. Each axis is updated in place to `value - value * damping`. The
routine returns zero if either stored result is below `2.0f`; otherwise it
returns one.

Named arithmetic temporaries initially retained the first result in an FPU
register and produced separate zero-return paths, making the body one word too
long. Expressing both operations as direct in-place updates makes IDO reload
the stored first axis for its comparison. Combining the threshold checks with
a short-circuit OR produces retail's shared return-zero epilogue and exact
interleaving of the second subtraction, first compare, store, and branch.
Every word matches directly from C; no guarded retail words are needed.

## Evidence

Linked ELF offset `0x189BF4` and decompressed retail offset `0x1770A4` compare
equal across the complete 100-byte span. Both have SHA-256
`035239563829978bd71d6f260e062841506d078a1d0c22061d7c40fe8c5c24f4`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,768 / 5,469 (50.61%) | 1 | 2,700 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,197 / 4,791 (45.86%) | 0 | 2,594 |
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

Continue with 23-word `func_1514ECE0`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
