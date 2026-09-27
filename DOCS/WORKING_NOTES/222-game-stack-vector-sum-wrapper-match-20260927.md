# Game stack-vector sum wrapper match - 2026-09-27

## Result

`func_150EB430` is byte-exact across 21 words and 84 bytes at
`0x150EB430..0x150EB484`. Fresh totals are 2,726 / 5,470 exact C functions
overall and 2,155 / 4,792 in Game.

## Recovery

The function adds two three-component float vectors into a local stack vector,
then calls `func_150EB484(arg0, sum)`. The 40-byte frame, local vector at
`sp+0x1C`, three additions, final store in the call delay slot, and epilogue
all compile directly from that typed shape.

IDO evaluates each addition right-to-left. Writing the equivalent commutative
expressions as `arg1[i] + arg0[i]` reproduces retail's six load choices and all
floating-register lifetimes. The remaining difference is one allocator choice:
IDO retains the second vector in `a2`, while retail uses `a3`. Four guarded,
non-relocating words preserve the initial `a3` move and its three component
loads. The other 17 words remain direct compiler output.

## Evidence

Linked ELF offset `0x12B430` and decompressed retail offset `0x1188E0` compare
equal for all 84 bytes. Both spans have SHA-256
`bb57799e7e106d77a3a3c05e720507b9841d7179ad06170cde91cf5dccc1a7ee`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,726 / 5,470 (49.84%) | 1 | 2,743 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,155 / 4,792 (44.97%) | 0 | 2,637 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and exhaustive full link, fresh progress and matcher,
independent retail/ELF span hashes and `cmp`, replacement build, project tool
checks, all six padding-tool unit tests, outer build, and `git diff --check`
pass.

## Next boundary

Continue with 21-word `func_15155F3C`.
