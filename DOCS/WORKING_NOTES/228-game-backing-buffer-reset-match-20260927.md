# Game backing-buffer reset match - 2026-09-27

## Result

`func_1505DFDC` is byte-exact across its 33-word, 132-byte tracked span at
`0x1505DFDC..0x1505E060`. Fresh totals are 2,731 / 5,469 exact C functions
overall and 2,160 / 4,791 in Game.

## Recovery

The routine first writes `0xFFFF` to the owner halfword at offset `0x84`. If
the backing pointer at offset `0x2D0` is nonnull, it clears the word at backing
offset `0x28`, zeroes the `0x3A0` bytes beginning at offset `0x40`, clears the
words at offsets `0x30` and `0x34`, and writes the selected
`D_800C4ED0[index] + 1` byte at offsets `0x41` and `0x211`.

The prior `u8` index spilled as a byte and a cached `u16 value` collapsed
retail's two table reads, producing a 30-word body. Keeping the index as `s32`
and spelling both table expressions directly restores the 33-word extent.
Declaring the index before the backing pointer assigns retail's stack slots;
placing both source-level selector writes before the two zero-word stores lets
IDO reproduce retail's interleaved schedule exactly. No guarded retail words
or compiler-steering expressions are needed.

## Evidence

Linked ELF offset `0x9DFDC` and decompressed retail offset `0x8B48C` compare
equal for all 132 bytes. Both spans have SHA-256
`715ebfa81ced3911f6b4616b912c1f45f7373229d091f13f28d99674fcc05eff`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,039 (90.56%) | 2,731 / 5,469 (49.94%) | 1 | 2,737 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,319 (90.07%) | 2,160 / 4,791 (45.08%) | 0 | 2,631 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
132-byte span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Keep the documented `func_150721A4`, `func_151A8584`/`func_151A85D4`,
`func_1506EF5C`, `func_1507A4D4`, `guMtxIdentF`, `func_150F1684`, and
`func_15155FD4` compiler cases parked. Review 60-word zero-return placeholder
`func_150AD8B0`, the next unparked Game C row in the fresh queue, with 19 real
differences.
