# Game shifted motion-decay update match - 2026-09-26

## Result

`func_1518F108` is byte-exact across all 21 words and 84 bytes at
`0x1518F108..0x1518F15C`. Fresh totals are 2,709 / 5,469 exact C functions
overall and 2,138 / 4,791 in Game.

## Recovery

The function is a shifted-field structural twin of `func_1514A498`. It reads
float components at object offsets `0x30` and `0x2C` and a factor at `0x154`,
then replaces each component with `value - value * factor`. It reads a signed
timer at `0x1C`; when that timer is below the signed limit at `0x158`, it
multiplies the timer by the signed halfword at `0x15A` and stores the low byte
at `0x5C`. The function returns one on both paths.

The same local declaration and expression order used for `func_1514A498`
reproduces retail's floating-point register allocation, paired operations,
comparison schedule, branch delay-slot store, and integer lifetimes. IDO again
canonicalizes the commutative multiply as `multu t7,v0`, while retail uses
`multu v0,t7`. A guarded non-relocating patch changes only that equivalent
operand order.

## Evidence

Linked ELF offset `0x1CF108` and decompressed retail offset `0x1BC5B8` compare
equal for 84 bytes, both with SHA-256
`3ffe7494afd5ff6f15b2c609f15b61cf689c756363214ebc03ea988c4bb71059`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,709 / 5,469 (49.53%) | 1 | 2,759 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,138 / 4,791 (44.63%) | 0 | 2,653 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. The guarded patch expects
compiler word `0x01E20019` and replaces it with retail word `0x004F0019` at
function offset `0x38`; it carries no relocation.

## Next boundary

Continue with 20-word `func_15192308`. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
