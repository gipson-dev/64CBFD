# Game bounded callback dispatch match - 2026-09-27

## Result

`func_151A8A20` is byte-exact across all 22 words and 88 bytes at
`0x151A8A20..0x151A8A78`. Fresh totals are 2,740 / 5,469 (50.10%) exact C
functions overall and 2,169 / 4,791 (45.27%) in Game.

## Recovery

The function reads the selector byte at object offset `0x5C`, clamps values
outside the three-entry table to slot zero, and loads the selected callback
from `D_8008F964`. A non-null callback receives the original object, second
argument, and byte-normalized third argument.

A typed callback table, signed local index, and `u8` third parameter reproduce
retail directly. IDO emits the original argument normalization, selector
fallback branch-likely, indexed callback load, null branch-likely, and indirect
call without guarded retail-word scheduling.

## Evidence

Linked ELF offset `0x1E8A20` and decompressed retail offset `0x1D5ED0`
compare equal across the complete 88-byte span. Both have SHA-256
`8b82ac8d37d486ce4aa72a79997287dc4fadcd880adc9881cdd64f877cf34a8d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,740 / 5,469 (50.10%) | 1 | 2,728 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,169 / 4,791 (45.27%) | 0 | 2,622 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
88-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 20-word `func_151A8F1C`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
