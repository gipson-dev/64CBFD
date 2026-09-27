# Game event-flag handler match - 2026-09-26

## Result

`func_151087FC` is byte-exact across its complete 21-word, 84-byte tracked
span at `0x151087FC..0x15108850`. Fresh totals are 2,704 / 5,469 exact C
functions overall and 2,133 / 4,791 in Game.

## Recovery

The function accepts a `struct126` pointer, an unused second argument, and a
byte event code. Event `0x2B` sets bit zero in the byte at offset `0x30`, while
event `0x2C` clears that bit. Other event values leave the record unchanged.

Offset `0x30` is eight bytes into the state beginning at `struct126::unk28`.
Retail materializes that offset-`0x28` interior pointer separately on both
event paths. Defining one initialized `EventFlags` pointer before the branch
lets IDO sink and duplicate its address calculation into those exact paths;
the first store then occupies the early return's delay slot as in retail.

## Evidence

Linked ELF offset `0x1487FC` and decompressed retail offset `0x135CAC` compare
equal for 84 bytes, both with SHA-256
`79a176792d390d8b8fb0b0b77f55b7e2d332e2be6bbce79269abc52aafe01ea1`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,704 / 5,469 (49.44%) | 1 | 2,764 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,133 / 4,791 (44.52%) | 0 | 2,658 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Keep `func_150721A4` parked at its verified three-word direct-C overflow and
`func_15125628` in its documented handwritten-assembly category. Continue
ordinary Game restoration with 21-word `func_150EC45C`, the compact constant
argument wrapper among the remaining 19-difference rows.
