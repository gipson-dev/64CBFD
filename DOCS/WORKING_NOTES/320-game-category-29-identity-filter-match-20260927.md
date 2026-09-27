# Game category-29 identity filter match - 2026-09-27

## Result

`func_151640C0` is byte-exact across all 29 words and 116 bytes at
`0x151640C0..0x15164134`. Fresh totals are 2,824 / 5,469 (51.64%) overall and
2,252 / 4,791 (47.00%) in Game.

## Recovery

The previous C captured the predicate but kept both pointer arguments live in
registers and re-read object fields directly. Retail homes both parameters in
their ABI stack slots, captures the record and object pointers separately, and
uses stable owner and identifier values across three short-circuit checks.

Declaring the parameter slots volatile, retaining nonvolatile record/object
pointers, advancing the object pointer to its `+0x18` owner field, and naming
both identifiers restores the exact frame, category gate, branch targets,
delay-slot loads, call site, and 29-word extent.

Nine guarded words preserve retail's independent local-register allocation.
The guarded words change only register encodings; no relocation, address, or
control-flow instruction is synthesized.

## Evidence

The rebuilt span at `build/conker.us.bin+0x191540` and pristine retail span at
`conker.us.bin+0x191570` compare equal for all 116 bytes. Both have SHA-256
`5c7f07b4183a17f6647dd6ac0b115f58ff60fa10d84f4c0c4e04f8ec6800c8b9`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,824 / 5,469 (51.64%) | 1 | 2,644 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,252 / 4,791 (47.00%) | 0 | 2,539 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused build/disassembly, required full guard-table rebuild, linked
matcher, direct comparison, replacement build, outer ROM build, tool checks,
all seven relocation tests, guard-table validation, and whitespace check pass.
The guard table now has 1,433 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659 pre-existing status entries. Frozen
Release was not built, modified, or launched; `conker_pc.exe` remains
13,712,896 bytes with timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 27-word Game `func_1515F040`, currently at 23 real differences.
Its earlier correct-looking float-clamp source emitted 28 words because IDO
inserted one FP hazard `nop`; retain that measured boundary while revisiting
the source and schedule.
