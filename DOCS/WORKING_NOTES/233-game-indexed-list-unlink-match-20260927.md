# Game indexed-list unlink match - 2026-09-27

## Result

`func_15168A9C` is byte-exact across its 29-word, 116-byte tracked span at
`0x15168A9C..0x15168B10`. Fresh totals are 2,735 / 5,468 (50.02%) exact C
functions overall and 2,164 / 4,790 (45.18%) in Game.

## Recovery

The routine removes a `ListNode` from the list selected by its row and index
bytes. It computes the slot in `D_800DCE50`, replaces the slot when the node is
the list head, reconnects the next node's `prev` link, and reconnects the
previous node's `next` link.

The previous raw `void *` implementation already had retail's 29-word control
flow but differed in 20 register words. Merely changing to typed fields did
not recover the allocation. The matching source keeps explicit `u8 row` and
`u8 index` locals before computing the typed `ListNode **slot`, then retains
explicit `next` and `prev` node lifetimes.

That shape reproduces retail directly: row/index in `v0`/`v1`, scaled-row
calculation in `t6`, scaled index in `t7`, combined offset in `t8`, global
base in `t9`, slot pointer in `a1`, and link-update values in `t0` through
`t3`. Both branch-likely link loads and the final null check also match. No
guarded retail-word entries are required.

## Evidence

Linked ELF offset `0x1A8A9C` and decompressed retail offset `0x195F4C` compare
equal for all 116 bytes. Both spans have SHA-256
`3d0eff7bee4097954ec64a6c5026e8fd390df1a7edcd8a26f92c594b4126b538`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 2,735 / 5,468 (50.02%) | 1 | 2,732 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 2,164 / 4,790 (45.18%) | 0 | 2,626 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
116-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 23-word `func_15179AB8`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
