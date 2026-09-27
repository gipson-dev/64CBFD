# Game conditional submission wrapper match - 2026-09-26

## Result

`func_1502E474` is byte-exact across all 20 words and 80 bytes at
`0x1502E474..0x1502E4C4`. Fresh totals are 2,702 / 5,469 exact C functions
overall and 2,131 / 4,791 in Game.

## Recovery

The function reads the global count at `D_800C3E7A`. When nonzero, it selects
the pointer in `D_800C3E80` indexed by byte `D_800BE9C0` and passes that
pointer plus the count to `func_150A9984`. It then sets the byte completion
flag `D_800C3E90` to one on both paths.

Retail loads the count with `lhu`, establishing `D_800C3E7A` as `u16` rather
than the previous signed declaration. Using the global directly in both the
condition and call lets IDO common-subexpress the value into `a1`, reproducing
retail's shared `lui`/`lhu` register. The unconditional flag assignment then
produces retail's branch-likely delay constant and post-call constant reload.
All 20 words compile directly without guarded retail words.

## Evidence

Linked ELF offset `0x6E474` and decompressed retail offset `0x5B924` compare
equal for 80 bytes, both with SHA-256
`57242216c7ecf9676d6561c4c19d0d06ea0b3e217660676bcd1140454ccaf708`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,702 / 5,469 (49.41%) | 1 | 2,766 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,131 / 4,791 (44.48%) | 0 | 2,660 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` already contains the complete generated body plus
host diagnostics, so no sibling regeneration is needed. The sibling's 1,659
dirty entries and frozen Release executable remain untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with existing 33-word `func_150319CC`, the
next unparked nonblocked Game row at 19 differences. Keep the measured
`func_151A8584`/`func_151A85D4` callback-scheduling pair parked. Init
alternative `func_10001000` remains at 14 differences; keep address-blocked
`func_10012588` parked.
