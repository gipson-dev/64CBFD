# Game Outer Highest Combiner: Direct Match

Date: 2026-10-03. Baseline: `3aec11c`.

## Result

`func_15046D00` replaces its zero-return placeholder with the complete semantic
outer highest-height combiner. All 161 words / 644 bytes match directly under
the existing compiler profile. No new word guards, profiles, shared layouts,
or assembly substitutions were introduced. Converted totals do not change:
the placeholder was already counted as C. One different C row becomes exact.

## Recovered Contract

1. Reject only when `position[1] < threshold`, clear flag bit 2, and return
   zero without either query. Preserve every other result byte.
2. Snapshot both entire 36-byte records before calling
   `func_1504697C(position, selector, threshold, &first)`, then context-3
   non-entity query `func_1504554C(position, threshold, &second)`.
3. Interpret both returns through their low byte. If exactly one is accepted,
   select that result regardless of height order.
4. If both or neither are accepted, choose first only for strict
   `second.height < first.height`. Ties/unordered comparisons choose second.
   Copy the complete record, including padding.
5. Return normalized success when either query is accepted. If neither is
   accepted, clear only bit 2 after copying the selected fallback and return
   zero. Preserve selected state/value; do not add another threshold gate.

The bound remains by value across helper mutations. Both snapshots precede
output mutation; final selection observes first-snapshot changes made during
the second query.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x15046D00..0x15046F84` |
| Retail ROM interval | `0x741B0..0x74434` |
| Slot | 644 bytes / 161 words, no trailing slot padding |
| Differing words | 0 |
| Following symbol | `func_15046F84 = 0x15046F84`, unchanged |
| SHA-256 | `1ca351c95b9a55684cc2f47eb5853c534b4e41ef727e3c67fb45192d2bd2817b` |

Independent ELF-function comparison includes the return delay slot.

## Verification

Twelve source-extracted freestanding 32-bit tests in
`tools/tests/test_game_outer_highest_combiner.py` reuse the established highest
outer-combiner cases with this routine's actual production body. Only its two
callees are mocked. Coverage includes all acceptance combinations, strict/
tied/unordered selection, low-byte return truncation, equal/NaN gates, all 256
early-rejection flags, full-record/state/value/padding preservation, both-failed
flag masking, helper/output/position/bound mutations, late snapshot updates,
all 65,536 selectors, signed-zero bounds, successful selection for every flag,
infinite heights, and signed-zero height ties.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_outer_highest_combiner
python3 -m unittest discover -s tools/tests
make tools-check
```

All 342 repository tool tests pass. Seventeen exact neighboring routines remain
retail-identical. The four entity-query hashes from Notes 765 and 771-773 and
the non-matching terrain highest hash from Note 759 remain unchanged. This
does not claim those five queries are byte-exact. The complete 5,712-byte
collector, 504-byte producer, and 16-byte return closure remain exact. Both
entire Init sections remain retail-identical with the lengths/hashes in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
These are build, instruction, and host-source behavior checks, not gameplay
qualification. No host-port build, guest execution, or compressed-ROM build
was performed.

## Progress / Next

Fresh inventory remains total 5,462 / 6,042 C rows (90.40%), 1,931,264 /
2,256,728 C bytes (85.58%); Game 4,789 / 5,321 C rows (90.00%), 1,759,828 /
2,072,880 C bytes (84.90%). Matcher becomes total 3,267 / 5,462 exact (59.81%)
and Game 2,594 / 4,789 exact (54.17%). Zero drift; 2,195 different C rows
remain. README changes are aggregate-only; detailed updates remain in DOCS.

Next recover `func_1504715C`'s 89-word actor-to-height-result builder. The full
assembly was inspected: it copies height/metadata from actor offsets `0x180`/
`0x184`, uses flag `0x00200000` to choose synthesized versus stored vertices,
and uses the one-based index at `0x1A0` to publish an entity pointer and state.
It calls `func_15145C90` in the entity path and merges normalized truth into
result flags. The zero-index path emits no defined normalized return value;
establish its caller/return contract rather than preserving the placeholder's
invented `s32` signature blindly. Recover packed/unaligned vertex ownership,
truncation and alias-sensitive reloads before implementing. Matching the
remaining terrain/entity queries and gameplay qualification are separate work.
