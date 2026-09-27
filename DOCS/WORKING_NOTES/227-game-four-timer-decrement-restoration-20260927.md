# Game four-timer decrement restoration - 2026-09-27

## Result

`func_15125628` is restored from its maintained C equivalent to the original
handwritten assembly across the complete 26-word, 104-byte extent
`0x15125628..0x15125690`. The fresh C-only matcher reports 2,730 / 5,469
(49.92%) overall and 2,159 / 4,791 (45.06%) in Game.

## Classification

The routine independently decrements four nonzero timer bytes at
`D_800DBFF4..D_800DBFF7`. Retail loads every byte through an assembler
self-base symbol expansion and prepares each store with a separate `lui at`.
The four repeated blocks use consecutive result registers `t6..t9` and keep
each decrement in the branch delay slot.

IDO C combines the load and store address within each block. Prior experiments
only reproduced retail by declaring every access as a different single-use
symbol, which would falsify the data model. The behaviorally equivalent C is
retained under `#if 0`, while the existing extracted body now owns the symbol
through `GLOBAL_ASM`.

## Evidence

The linked symbol remains at `0x15125628`. ELF file offset `0x165628` and
decompressed retail offset `0x152AD8` compare equal for all 104 bytes. Both
spans have SHA-256
`ea2a21dfd73b25f4db3c08366068559df6e0985d32ba0a86af22edd3e74542ac`.

| Section | C functions | Raw assembly | C bytes | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,039 (90.56%) | 570 | 1,931,864 / 2,256,728 (85.60%) | 2,730 / 5,469 (49.92%) | 1 | 2,738 |
| Init | 497 / 538 (92.38%) | 41 | 148,600 / 164,048 (90.58%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,319 (90.07%) | 528 | 1,763,624 / 2,072,880 (85.08%) | 2,159 / 4,791 (45.06%) | 0 | 2,632 |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
104-byte span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Keep the documented `func_150721A4` and
`func_151A8584`/`func_151A85D4` compiler-scheduling cases parked. Continue
with 33-word `func_1505DFDC`, the next unparked Game C row in the fresh queue,
with 19 real differences.
