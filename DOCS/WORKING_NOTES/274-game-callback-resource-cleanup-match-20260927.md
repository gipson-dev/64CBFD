# Game callback resource cleanup match - 2026-09-27

## Result

`func_151904BC` is byte-exact across all 23 words and 92 bytes at
`0x151904BC..0x15190518`. Fresh totals are 2,777 / 5,469 (50.78%) exact C
functions overall and 2,206 / 4,791 (46.04%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail conditionally
releases the pointer at object offset `0x84`, unregisters callback
`func_1518E298` for the object and owner value at offset `0x10`, then releases
the resource index reached through object offset `0x78`.

Volatile accesses to the optional pointer preserve retail's separate null-test
and call-argument loads. A volatile derived pointer keeps `arg0 + 0x30` live
across callback unregistration, and declaring the owner local first places
that pointer in retail stack slot `0x18`.

IDO still converts the null branch to a branch-likely and rotates three
independent unregister-call setup instructions. Five guarded words preserve
retail's non-likely branch, empty delay slot, and callback/owner/resource setup
order. The guard checks the exact compiler input words and moves the callback
`HI16` relocation with its instruction; behavior and call targets are
unchanged.

## Evidence

Linked ELF offset `0x1D04BC` and decompressed retail offset `0x1BD96C` compare
equal across the complete 92-byte span. Both have SHA-256
`723d6af129190b4ac047acf1739e7f4abfc79a6eea5f78b62c342f3e6c336ee4`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,777 / 5,469 (50.78%) | 1 | 2,691 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,206 / 4,791 (46.04%) | 0 | 2,585 |
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

Continue with 23-word `func_15197A0C`, the next unparked Game C row in the
fresh ordered queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
