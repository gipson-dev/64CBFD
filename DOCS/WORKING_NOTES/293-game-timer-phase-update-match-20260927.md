# Game timer/phase updater match - 2026-09-27

## Result

`func_1517F7B4` is byte-exact across all 24 words and 96 bytes at
`0x1517F7B4..0x1517F814`. Fresh totals are 2,797 / 5,469 (51.14%) exact C
functions overall and 2,226 / 4,791 (46.46%) in Game.

## Recovery

The zero-return placeholder was a global timer and phase updater. If the
unsigned 16-bit timer `D_800DDE08` is nonzero, it subtracts the signed frame
delta `D_800BE9E4` while saturating at zero. It then advances the 8-bit phase
accumulator `D_800DDD89` by the product of speed byte `D_800DDD88` and that
same frame delta; the byte store provides the retail wraparound behavior.

Direct global accesses reproduce the complete retail control flow and
instruction count. They also retain the timer value in `v0`, frame delta in
`v1`, speed in `t8`, multiply ordering, branch delay slots, accumulator load,
and all non-timer address lifetimes.

IDO allocates the timer base to `a0`, while retail uses `a1`. Five guarded
rows normalize only that equivalent base lifetime: the timer's checked
`R_MIPS_HI16`/`R_MIPS_LO16` address pair, initial halfword load, decremented
halfword store, and zero store. A tested unused-parameter theory was rejected
because IDO emitted an argument-home store and overflowed the retail span.

## Evidence

Linked ELF offset `0x1BF7B4` and decompressed retail offset `0x1ACC64` compare
equal across the complete 96-byte span. Both have SHA-256
`e2b43acfdd268d2a26e9aaa278219ebc73751ae9197e6e408b87412c964eef4d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,797 / 5,469 (51.14%) | 1 | 2,671 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,226 / 4,791 (46.46%) | 0 | 2,565 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full clean-equivalent nonmatching
rebuild and link, fresh progress and matcher, independent 96-byte hashes, and
direct byte comparison pass. The replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 25-word `func_151A0950`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
