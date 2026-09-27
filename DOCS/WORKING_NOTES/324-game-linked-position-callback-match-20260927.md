# Game linked-position callback match - 2026-09-27

## Result

`func_1518E298` is byte-exact across all 28 words and 112 bytes at
`0x1518E298..0x1518E308`. Fresh totals are 2,828 / 5,469 (51.71%) overall and
2,256 / 4,791 (47.09%) in Game.

## Recovery

The callback receives a destination plus three unused integer arguments. It
loads the linked source at destination offset `0x1C` and returns `1` if either
the link or the source's first word is zero. Otherwise it truncates source
floats at `0x14`, `0x18`, and `0x1C` into destination halfwords at `0x02`,
`0x04`, and `0x06`, then returns `0`.

The explicit four-argument signature reproduces retail's three frameless
argument-home stores. Nesting the two positive tests, returning zero inside
the successful path, and leaving one default return after the tests gives IDO
retail's `v1` source pointer, `v0` return value, non-likely null branches, and
final halfword store in the successful `jr` delay slot. No guarded word
patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1BB718` and pristine retail span at
`conker.us.bin+0x1BB748` compare equal for all 112 bytes. Both have SHA-256
`394557df7bda8712ee5a6684d29ccf265f919731ac1f8b0acf9a200c004bc2da`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,828 / 5,469 (51.71%) | 1 | 2,640 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,256 / 4,791 (47.09%) | 0 | 2,535 |
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

Continue with 24-word Game `func_1519ED24`, the next unparked C row at 23 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
