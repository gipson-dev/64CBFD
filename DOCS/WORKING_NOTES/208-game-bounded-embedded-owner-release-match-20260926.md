# Game bounded embedded-owner release match - 2026-09-26

## Result

`func_151A73EC` is byte-exact across all 20 words and 80 bytes at
`0x151A73EC..0x151A743C`. Fresh totals are 2,711 / 5,469 exact C functions
overall and 2,140 / 4,791 in Game.

## Recovery

The function accepts an object pointer and forms an interior entry pointer at
offset `0x170`. When the signed halfword at object offset `0x64` is below
`0x20`, it reads the owned pointer at entry offset `+4` (`object + 0x174`). A
non-null pointer is passed to `func_1516972C` and then cleared. Every path
returns one.

The nested conditions reproduce retail's two branch-likely early returns,
each with the constant-one result in its taken delay slot. Keeping the entry
as a separate initialized interior pointer makes IDO spill it at `sp + 0x18`
in the release call's delay slot, reload it after the call, and clear the same
field. The resulting C matches all 20 retail words directly.

## Evidence

Linked ELF offset `0x1E73EC` and decompressed retail offset `0x1D489C` compare
equal for 80 bytes, both with SHA-256
`019efff64d8d7ce0f17f9f3d54d94649404be7cb4852b79daa15023147b58f6d`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,711 / 5,469 (49.57%) | 1 | 2,757 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,140 / 4,791 (44.67%) | 0 | 2,651 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `func_151AF338`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
