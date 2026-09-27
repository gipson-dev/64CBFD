# Game display-list state helper match - 2026-09-27

## Result

`func_1517EA4C` is byte-exact across all 24 words and 96 bytes at
`0x1517EA4C..0x1517EAAC`. Fresh totals are 2,827 / 5,469 (51.69%) overall and
2,255 / 4,791 (47.07%) in Game.

## Recovery

The helper accepts a display-list cursor, emits a pipe sync, installs combine
words `0xFCFFB3FF / 0xFF65FEFF`, installs other-mode words
`0xEF002C0F / 0x00504344`, and returns the cursor advanced by three `Gfx`
entries.

The standard `gDPPipeSync`, `gDPSetCombine`, and `gDPSetOtherMode` macros
produce the retail command words directly. Their block-local `_g` temporaries
also reproduce retail's `v1`, `a1`, and `a2` allocation sequence and the exact
constant-load order. No guarded word patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1ABECC` and pristine retail span at
`conker.us.bin+0x1ABEFC` compare equal for all 96 bytes. Both have SHA-256
`12a220ce6dd9bd2e40cbdc7e70533c694b619289159f5ca2f20418b1ddc74acf`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,827 / 5,469 (51.69%) | 1 | 2,641 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,255 / 4,791 (47.07%) | 0 | 2,536 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full shared-table rebuild and link, fresh
matcher, and independent linked-span comparison pass. The complete replacement
build, outer ROM build, tool checks, unit tests, guard-table audit, and
whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 28-word Game `func_1518E298`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
