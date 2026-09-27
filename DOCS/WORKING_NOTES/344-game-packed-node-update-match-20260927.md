# Game packed node update match - 2026-09-27

## Result

`func_15178C34` is byte-exact across all 26 words and 104 bytes at
`0x15178C34..0x15178C9C`. Fresh totals are 2,848 / 5,469 (52.08%) overall and
2,276 / 4,791 (47.51%) in Game.

## Recovery

The function looks up a node through `func_15178B98` using a byte ID. For a
successful lookup, it packs the low halves of its second and third arguments
into the word at node offset `0x10`, shifts the fourth argument into the high
half of the word at offset `0x14`, and stores the signed fifth argument at
offset `0x30`.

The initial typed body matched 25 of 26 words. Retail's `lh 0x2A(sp)` for the
fifth stack argument establishes that parameter as `s16`; the prior declaration
used `s32` and emitted `lw 0x28(sp)`. Correcting both the definition and its
cross-file declaration reproduces all 26 words directly from C without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1A60B4` and pristine retail span at
`conker.us.bin+0x1A60E4` compare equal for all 104 bytes. Both have SHA-256
`d95e4bc7333312ac17d400f54e3868d3bb50f56992bf5da1252ddabd00477356`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,848 / 5,469 (52.08%) | 1 | 2,620 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,276 / 4,791 (47.51%) | 0 | 2,515 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent linked-
span hashes, and direct byte comparison pass. The broader replacement,
outer-ROM, tool, unit-test, guard-table, and whitespace checks also pass. All
nine unit tests pass, and the 1,466-row guard table has zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 26-word Game `func_15182768`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
