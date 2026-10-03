# Game Highest-Height Combiner: Direct Match

Date: 2026-10-03. Baseline: `d7496b1`.

## Result

`func_15046460` replaces its zero-return placeholder with the complete semantic
highest-height combiner. All 166 words / 664 bytes match retail directly under
the existing compiler profile. No new word guards, profiles, shared layouts,
or assembly substitutions were introduced. This was already counted as C;
converted function/byte totals are unchanged, while one different row becomes
byte-exact.

## Recovered Contract

1. Reject only when `position[1] < threshold`. Zero result state and value,
   clear flag bit 2, and return zero without preparing counts or querying.
2. Snapshot both complete 36-byte result records before `func_15045714`
   prepares adjacent primary/secondary counts.
3. Call context-2 highest query `func_15045AE4` with the primary count and
   first snapshot, then context-3 query `func_15045F8C` with the secondary
   count and second snapshot. Interpret both returns through their low byte.
4. With one accepted result, publish that result regardless of height order.
   With both accepted or neither accepted, select first only when
   `second.height < first.height`. Ties and unordered comparisons select second.
5. Copy the entire selected record, including padding, and return normalized
   success when either query is accepted. When neither succeeds, clear only
   bit 2 after the copy and return zero; do not zero selected state/value.

The threshold remains by value across helper mutations. No second gate is
invented after preparation. Snapshot comparison observes mutations made during
the second query, including updates to the previously exposed first snapshot.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x15046460..0x150466F8` |
| Retail ROM interval | `0x73910..0x73BA8` |
| Slot | 664 bytes / 166 words, no trailing slot padding |
| Differing words | 0 |
| Following symbol | `func_150466F8 = 0x150466F8`, unchanged |
| SHA-256 | `6be38d3fe5178e0b873a6945ed88f9a931cb52c499a2634d0978e0db6cd6d0e6` |

The independent ELF-function/retail comparison includes the return delay slot.

## Verification

Ten source-extracted freestanding 32-bit tests in
`tools/tests/test_game_highest_height_combiner.py` reuse the lowest combiner's
mock fixture but replace its production body with the actual highest combiner.
Only the three called helpers are mocked. Coverage includes all acceptance
combinations, strict/tied/unordered height selection, all 256 early-rejection
flag values, full-record copies, selected state/value preservation after
failure, low-byte return truncation, equal/NaN gates, snapshots before helper
mutations, late snapshot updates, all 65,536 selectors, and signed-zero bounds.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_highest_height_combiner
python3 -m unittest discover -s tools/tests
make tools-check
```

All 306 tool tests pass. Thirteen prior exact neighboring routines, including
the lowest combiner, remain retail-identical. All four semantic entity-query
hashes remain unchanged from Notes 765 and 771-773. The complete 5,712-byte
collector, 504-byte producer, and 16-byte return closure remain exact. Both
entire Init sections remain retail-identical with the lengths/hashes in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
These are build, instruction, and host-source behavior checks, not gameplay
qualification. No host-port build, guest execution, or compressed-ROM build
was performed.

## Progress / Next

Fresh inventory remains total 5,461 / 6,042 C rows (90.38%), 1,930,620 /
2,256,728 C bytes (85.55%); Game 4,788 / 5,321 C rows (89.98%), 1,759,184 /
2,072,880 C bytes (84.87%). Matcher becomes total 3,264 / 5,461 exact (59.77%)
and Game 2,591 / 4,788 exact (54.11%). Zero drift; 2,197 different rows remain.
README changes are aggregate-only; detailed updates remain in DOCS.

Next recover retained `func_150466F8`. Its inspected opening snapshots both
records, calls the recovered entity lowest combiner `func_150461D0`, then
queries terrain through `func_15044ED0`. Inspect its complete selection and
failure paths and caller contract before converting; its frame and call
interface differ from the count-preparing combiner recovered here. Remaining
entity-query byte matching and runtime qualification are separate open work.
