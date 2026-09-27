# Game marker-record swap match - 2026-09-27

## Result

`func_150E2FC0` is byte-exact across its 24-word, 96-byte tracked span at
`0x150E2FC0..0x150E3020`. Fresh totals are 2,730 / 5,470 exact C functions
overall and 2,159 / 4,792 in Game.

## Recovery

The routine only acts for marker `0x2D`. It compares the destination word at
offset `0xDC` against the first two words of the source record. A match against
the first word installs the second word and source byte 9; a match against the
second installs the first word and source byte 8. The selected source byte is
stored in the destination byte at offset `0xDA`.

Assigning the first source word before the current destination value recovers
retail's `v0`/`v1` load lifetimes. IDO still emits the final equality branch as
`bne v1,t9`; retail uses the equivalent `bne t9,v1`. One guarded,
non-relocating word preserves that operand order without changing control flow
or data flow.

## Evidence

Linked ELF offset `0x122FC0` and decompressed retail offset `0x110470` compare
equal for all 96 bytes. Both spans have SHA-256
`815e571938eeb39d9ffeae2889c41574f46c2fa15e9b608e8ccc12d0e8dff23f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,730 / 5,470 (49.91%) | 1 | 2,739 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,159 / 4,792 (45.05%) | 0 | 2,633 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and exhaustive full link, fresh progress and matcher,
independent 96-byte span hashes and `cmp`, replacement build, project tool
checks, all six padding-tool unit tests, outer build, and `git diff --check`
pass.

## Next boundary

Keep the documented 17-word `func_150721A4` direct-C register-allocation case
parked. Continue with 26-word `func_15125628`, the next unparked Game C
candidate in the fresh queue, with 16 real differences.
