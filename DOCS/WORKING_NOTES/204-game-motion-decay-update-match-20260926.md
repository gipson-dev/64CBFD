# Game motion-decay update match - 2026-09-26

## Result

`func_1514A498` is byte-exact across all 21 words and 84 bytes at
`0x1514A498..0x1514A4EC`. Fresh totals are 2,707 / 5,469 exact C functions
overall and 2,136 / 4,791 in Game.

## Recovery

The function reads float components at object offsets `0x30` and `0x2C` and a
scale at `0x144`, then replaces each component with `value - value * scale`.
It reads a signed index at `0x1C`; when that index is below the signed limit at
`0x156`, it multiplies the index by the signed halfword at `0x158` and stores
the low byte at `0x5C`. The function returns one on both paths.

Local declaration order reproduces retail's paired floating-point operations,
comparison scheduling, branch delay-slot store, and integer register
lifetimes. IDO consistently canonicalizes the commutative integer multiply as
`multu t7,v0`, while retail uses `multu v0,t7`. Tested source-only forms either
retain that one-word difference or perturb the `mflo` result register and
store. A guarded non-relocating patch changes only that equivalent operand
order.

## Evidence

Linked ELF offset `0x18A498` and decompressed retail offset `0x177948` compare
equal for 84 bytes, both with SHA-256
`4325a1e4fbe15bca49875d5f4799d57884826a356ff97ae78ad0b22b03e21939`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,707 / 5,469 (49.50%) | 1 | 2,761 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,136 / 4,791 (44.58%) | 0 | 2,655 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. The guarded patch expects
compiler word `0x01E20019` and replaces it with retail word `0x004F0019` at
function offset `0x38`; it carries no relocation.

## Next boundary

Continue with 21-word `func_15155FD4`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
