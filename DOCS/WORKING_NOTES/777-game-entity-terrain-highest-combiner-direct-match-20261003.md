# Game Entity/Terrain Highest Combiner: Direct Match

Date: 2026-10-03. Baseline: `2cec54c`.

## Result

`func_1504697C` replaces its zero-return placeholder with the complete semantic
highest entity/terrain combiner. All 161 words / 644 bytes match retail directly
under the existing compiler profile. No new guards, profiles, shared layouts,
or assembly substitutions were introduced. Converted totals do not change:
the placeholder was already counted as C. One different C row becomes exact.

## Recovered Contract

1. Reject only when `position[1] < threshold`, clear flag bit 2, and return
   zero without either query. Preserve all other result bytes, including state
   and value; do not import the inner highest combiner's reset behavior.
2. Snapshot both entire 36-byte result records before calling highest entity
   combiner `func_15046460(position, selector, threshold, &first)`, then terrain
   query `func_150450CC(position, threshold, &second)`.
3. Interpret each query return through its low byte. With exactly one accepted
   result, select it regardless of height order.
4. With both accepted or neither accepted, select first only for strict
   `second.height < first.height`. Ties and unordered comparisons select the
   terrain record. Copy the entire selected record, including padding.
5. Return normalized success when either query is accepted. If neither is
   accepted, clear only bit 2 after copying the selected fallback and return
   zero. Preserve selected state/value and do not add another threshold gate.

The threshold remains by value across helper mutations. Snapshots precede
mutation of the original output; final selection observes first-snapshot
updates made during the terrain query.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x1504697C..0x15046C00` |
| Retail ROM interval | `0x73E2C..0x740B0` |
| Slot | 644 bytes / 161 words, no trailing slot padding |
| Differing words | 0 |
| Following symbol | `func_15046C00 = 0x15046C00`, unchanged |
| SHA-256 | `6f7a5d95530508c588246e3b4d3459ca49a3ac94f15bddf08ccbe24971daf886` |

Independent ELF-function comparison includes the return delay slot.

## Verification

Twelve source-extracted freestanding 32-bit tests in
`tools/tests/test_game_entity_terrain_highest_combiner.py` reuse the highest
combiner's behavioral cases with the actual two-call production body. The
early-rejection case is replaced because this outer routine preserves state
and value. Only the entity and terrain callees are mocked.

Coverage includes all acceptance combinations, strict/tied/unordered heights,
low-byte return truncation, equal/NaN gates, all 256 early-rejection flags,
full-record copies and failure masking, state/value/padding preservation,
snapshot/output and position/bound mutations, late first-snapshot updates,
all 65,536 selectors, signed-zero bounds, successful selection for all flags,
infinite heights, and signed-zero height ties.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_entity_terrain_highest_combiner
python3 -m unittest discover -s tools/tests
make tools-check
```

All 330 repository tool tests pass. Sixteen exact neighboring routines remain
retail-identical. All four semantic entity-query slot hashes remain unchanged
from Notes 765 and 771-773. The complete 5,712-byte collector, 504-byte producer,
and 16-byte return closure remain exact. Both entire Init sections remain
retail-identical with the lengths/hashes recorded in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).

The terrain highest callee `func_150450CC` is not byte-exact: its 576-byte slot
retains the documented 76 differences and SHA-256
`64640310ebe9fdbfb77fbdd8c9a4794d7a53897feb86f643d838cc449b78ca34`
from [Note 759](759-game-highest-height-query-semantic-recovery-20261002.md).
The initial neighbor check incorrectly included it in the exact group; the
corrected check separates its unchanged non-matching hash from the sixteen
exact neighbors. This is not a new code regression or a claimed callee match.

These are build, instruction, and host-source behavior checks, not gameplay
qualification. No host-port build, guest execution, or compressed-ROM build
was performed.

## Progress / Next

Fresh inventory remains total 5,462 / 6,042 C rows (90.40%), 1,931,264 /
2,256,728 C bytes (85.58%); Game 4,789 / 5,321 C rows (90.00%), 1,759,828 /
2,072,880 C bytes (84.90%). Matcher becomes total 3,266 / 5,462 exact (59.79%)
and Game 2,593 / 4,789 exact (54.14%). Zero drift; 2,196 different C rows
remain. README updates are aggregate-only; detailed updates stay in DOCS.

Next recover outer highest combiner placeholder `func_15046D00`. Its inspected
opening rejects when `position[1] < threshold`, clearing only bit 2, snapshots
both records, and calls `func_1504697C` followed by context-3 non-entity query
`func_1504554C`. Inspect the full selection/failure paths before implementing.
Terrain/entity query byte matching and runtime qualification remain open work.
