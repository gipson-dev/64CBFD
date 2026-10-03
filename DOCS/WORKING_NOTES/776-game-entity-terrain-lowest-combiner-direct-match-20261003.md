# Game Entity/Terrain Lowest Combiner: Direct Match

Date: 2026-10-03. Baseline: `50b5056`.

## Result

`func_150466F8` converts retained assembly ownership to its complete semantic
entity/terrain lowest-height combiner. All 161 words / 644 bytes match retail
directly under the existing compiler profile. No new word guards, profile
changes, shared layouts, or assembly substitutions were introduced.

## Recovered Contract

1. Reject only when `threshold < position[1]`, clear flag bit 2, and return
   zero without either query. Preserve every other result byte.
2. Snapshot both entire 36-byte result records before either helper call.
   Call entity combiner `func_150461D0(position, selector, threshold, &first)`,
   then terrain query `func_15044ED0(position, threshold, &second)`.
3. Interpret each query return through its low byte, not raw integer truth.
   If exactly one succeeds, select it regardless of the two heights.
4. If both succeed or neither succeeds, choose first only for strict
   `first.height < second.height`. Ties and unordered comparisons choose the
   terrain record. Copy all result bytes, including padding.
5. Return normalized success when either query is accepted. If neither is
   accepted, clear only bit 2 after copying the selected fallback and return
   zero. Do not clear state/value on either failure path.

The threshold remains by value even if a helper mutates its caller's storage.
Both snapshots precede mutation of the original output. The final height
comparison observes updates to the first snapshot made during the terrain
query. No second gate after a helper changes position Y is invented.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x150466F8..0x1504697C` |
| Retail ROM interval | `0x73BA8..0x73E2C` |
| Slot | 644 bytes / 161 words, no trailing slot padding |
| Differing words | 0 |
| Following symbol | `func_1504697C = 0x1504697C`, unchanged |
| SHA-256 | `265f938bf2380bfc30dd552bee2265c77d0a5888616f4491fe1d079d43a9675d` |

Independent ELF-function comparison includes the return delay slot.

## Verification

Twelve source-extracted freestanding 32-bit tests in
`tools/tests/test_game_entity_terrain_lowest_combiner.py` reuse the established
lowest-combiner behavioral cases with the actual two-call production body.
Only the entity and terrain callees are mocked. Checks include all acceptance
combinations, strict/tied/unordered heights, low-byte return truncation,
equal/NaN gates, all 256 early-rejection flags, full-record copies and failure
masking, snapshot/output and position/bound mutations, late first-snapshot
updates, all 65,536 selectors, signed-zero bounds, successful selection for
all flags, infinite heights, and signed-zero height ties.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_entity_terrain_lowest_combiner
python3 -m unittest discover -s tools/tests
make tools-check
```

All 318 repository tool tests pass. Fifteen prior neighboring routines remain
retail-identical, including both entity combiners and the retained terrain
query. All four semantic entity-query slot hashes remain unchanged from Notes
765 and 771-773. The complete 5,712-byte collector, 504-byte producer, and
16-byte return closure remain exact. Both whole Init sections remain retail-
identical, with the lengths/hashes recorded in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
These are build, instruction, and host-source behavior checks, not guest
gameplay qualification. No host-port build, guest execution, or compressed-ROM
build was performed.

## Progress / Next

Fresh inventory: total 5,462 / 6,042 C rows (90.40%), 1,931,264 / 2,256,728
C bytes (85.58%); Game 4,789 / 5,321 C rows (90.00%), 1,759,828 / 2,072,880
C bytes (84.90%). Matcher: total 3,265 / 5,462 exact (59.78%); Game
2,592 / 4,789 exact (54.12%). Zero drift; 2,197 different C rows remain.
Remaining raw assembly is 580 total rows, including 532 Game rows. README
changes are aggregate-only; detailed recovery updates remain in DOCS.

Next recover the highest entity/terrain placeholder `func_1504697C`. Its
inspected opening rejects when `position[1] < threshold`, clearing only flag
bit 2, snapshots both records, then calls `func_15046460` and `func_150450CC`.
Inspect its full selection/failure paths before implementing. Do not copy the
inner highest combiner's early state/value reset into this outer routine.
Entity-query byte matching and gameplay qualification remain separate work.
