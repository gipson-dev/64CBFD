# Game flag-gated record update match - 2026-09-26

## Result

`func_150C7968` is byte-exact across 21 words and 84 bytes at
`0x150C7968..0x150C79BC`. Fresh totals are 2,725 / 5,470 exact C functions
overall and 2,154 / 4,792 in Game.

## Recovery

The function first calls `func_15116110(arg0)`. If flag `0x04` is clear in
byte `arg0+0x73`, it reads the signed halfword at `D_800DBEF4+0x21C`, shifts
it right by four, and stores the result in byte `+0x13` of the optional record
at `arg0+0x7C`.

Compact typed C emits 20 words and preserves the behavior, frame, initial
call, flag test, arithmetic, optional store, and epilogue. Retail independently
orders the global-state and record loads, reads the source halfword before the
record null test, and retains an otherwise dead `state + 0x1E0` calculation.
Five guarded entries restore that schedule: one branch adjustment, two
relocation-aware load swaps, one source-load replacement plus dead-word
insertion, and one null-branch replacement. The unchanged compiler-produced
tail shifts into its retail positions.

## Evidence

Linked ELF offset `0x107968` and decompressed retail offset `0xF4E18` compare
equal for all 84 bytes. Both spans have SHA-256
`44bd9f87969d7f78f53c6889bbcefec767a3c726977b9b281e3f9cc353457889`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,725 / 5,470 (49.82%) | 1 | 2,744 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,154 / 4,792 (44.95%) | 0 | 2,638 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and full link, fresh progress and matcher, independent
retail/ELF span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_150EB430`.
