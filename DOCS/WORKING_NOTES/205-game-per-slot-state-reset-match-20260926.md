# Game per-slot state reset match - 2026-09-26

## Result

`func_15181DC8` is byte-exact across all 20 words and 80 bytes at
`0x15181DC8..0x15181E18`. Fresh totals are 2,708 / 5,469 exact C functions
overall and 2,137 / 4,791 in Game.

## Recovery

The function accepts a slot index and clears five pieces of per-slot state:
`D_800DDDD8[index]`, `D_800DDDC8[index]`, both float components in
`D_800DDDE8[index]`, and byte `D_800DDE20[index]`. Declaring the first two
globals as float arrays, the paired storage as a two-float row array, and the
last storage as a byte array reproduces retail's two index scales, address
formation, store order, and return sequence.

Direct C emits the full behavior in 19 words and common-subexpression reduces
all four floating zero stores to `$f0`. Retail instead materializes zero a
second time in `$f4`, uses `$f4` for the first store only, and then uses `$f0`
for the other three stores. A guarded insertion retains the redundant
`mtc1 zero,$f4`; a guarded replacement changes only the first store's source
register. The low relocation on that store remains attached to
`D_800DDDD8`.

## Evidence

Linked ELF offset `0x1C1DC8` and decompressed retail offset `0x1AF278` compare
equal for 80 bytes, both with SHA-256
`46a4fcb449b8f5cab466a5e009ace1fafb9aec11abd05a64d76dc5db6496b189`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,708 / 5,469 (49.52%) | 1 | 2,760 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,137 / 4,791 (44.60%) | 0 | 2,654 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and LIST
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. The first guarded entry
inserts word `0x44802000` after the unchanged index scale at function offset
`0x04`. The second expects relocated word `0xE4200000` at compact offset
`0x10` and replaces it with `0xE4240000`, retaining the
`R_MIPS_LO16:D_800DDDD8` relocation.

## Parked boundary and next step

`func_15155FD4` is behaviorally recovered as a two-owner linked-list lookup.
The closest 21-word direct-C form still rotates retail's owner, end, and node
registers and schedules the owner increment differently; alternate top-load
forms add an argument move. Its source is restored to the placeholder until
new compiler-shape evidence appears. Continue with 21-word `func_1518F108`.
