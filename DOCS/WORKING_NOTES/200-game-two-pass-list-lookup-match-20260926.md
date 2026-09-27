# Game two-pass list lookup match - 2026-09-26

## Result

`func_150319CC` is byte-exact across all 33 words and 132 bytes at
`0x150319CC..0x15031A50`. Fresh totals are 2,703 / 5,469 exact C functions
overall and 2,132 / 4,791 in Game.

## Recovery

The function first searches the list rooted at `D_800C3EE0` for a node whose
type byte at offset zero matches `arg1[0x3B]` and whose key byte at offset six
matches `arg0`. If that typed search is unavailable or misses, it searches the
same list again using only the key byte.

Retail keeps the current node in `v1` and loads its next pointer from offset
`0x54` into `v0` before testing either key. The previous C updated `node`
directly at the bottom of each loop, allowing IDO to fold the next-pointer
loads into branch-likely delay slots. A shared `next` local preserves retail's
two-register lifetime in both passes and reproduces all 33 words directly.

## Evidence

Linked ELF offset `0x719CC` and decompressed retail offset `0x5EE7C` compare
equal for 132 bytes, both with SHA-256
`f8a247eb9795d103d7ccdfbf5fcf438e8d563b2164901157b401e44b4d611c4c`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,703 / 5,469 (49.42%) | 1 | 2,765 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,132 / 4,791 (44.50%) | 0 | 2,659 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, six padding-tool
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue ordinary Game matching with 17-word `func_150721A4`, now the smallest
unparked nonblocked Game row at 16 differences. Keep the measured
`func_151A8584`/`func_151A85D4` callback-scheduling pair parked. Init
alternative `func_10001000` remains at 14 differences; keep address-blocked
`func_10012588` parked.
