# Game state-transition wrapper match - 2026-09-27

## Result

`func_15155F3C` is byte-exact across 21 words and 84 bytes at
`0x15155F3C..0x15155F90`. Fresh totals are 2,727 / 5,470 exact C functions
overall and 2,156 / 4,792 in Game.

## Recovery

The function looks up the current record with
`func_15155FD4(D_800C3E78)`. When a record exists, state byte `+0x11` changes
from `2` to `0` or from `3` to `2`; every other state is left unchanged.

A retained state-byte local makes IDO reproduce the complete frame, global
load and call relocations, branch-likely null exit, nested transition branches,
stores, and epilogue. IDO keeps that local in `a0`, while retail keeps it in
`v1`. Three guarded, non-relocating words preserve the retail register in the
state load and two comparisons. The other 18 words compile directly.

## Evidence

Linked ELF offset `0x195F3C` and decompressed retail offset `0x1833EC` compare
equal for all 84 bytes. Both spans have SHA-256
`0119e77d17efbde4d25797a1ebcd4419b5641efec94faf73ec7d9be6bf5fe34d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,727 / 5,470 (49.85%) | 1 | 2,742 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,156 / 4,792 (44.99%) | 0 | 2,636 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and exhaustive full link, fresh progress and matcher,
independent retail/ELF span hashes and `cmp`, replacement build, project tool
checks, all six padding-tool unit tests, outer build, and `git diff --check`
pass.

## Next boundary

Keep `func_15155FD4` parked at its measured owner/end/node allocation boundary.
Continue with 22-word `func_1507A47C`.
