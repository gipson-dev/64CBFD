# Game Lowest-Height Combiner: Direct Match

Date: 2026-10-03. Baseline: `9d543a0`.

## Result

`func_150461D0` replaces retained assembly ownership with the complete semantic
lowest-height combiner. All 164 words / 656 bytes match directly under the
existing `generated_71820` compiler profile. No new word guards, compiler
profiles, shared layout changes, or assembly substitutions were introduced.

The interrupted source edit was retained and verified after the user's Init
reassessment. Init still has 492 C rows and 47 assembly rows; only the two
deferred small leaves remain plausible independent ordinary-C experiments.
The fresh assessment is recorded in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).

## Recovered Contract

1. Reject only when `threshold < position[1]`. Clear result flag bit 2,
   return zero, and do not invoke preparation or either query.
2. Snapshot both entire 36-byte result records before preparing counts.
   Preserve metadata, state, value, and padding bytes as well as height/vertices.
3. Prepare adjacent primary/secondary counts through `func_15045714`, then
   call context-2 lowest query `func_15045880` with the primary count and first
   snapshot, followed by context-3 query `func_15045D48` with the secondary
   count and second snapshot. Keep the threshold argument by value.
4. Interpret each query's return through its low byte, not raw integer truth.
   With one accepted result, publish that result regardless of height order.
5. With both accepted or neither accepted, choose first only for strict
   `first.height < second.height`. Ties and unordered comparisons choose second.
   Copy the complete selected record and return normalized success when either
   query's low byte is nonzero. If neither succeeds, clear only bit 2 after
   copying and return zero.

Snapshot initialization precedes helper mutations of the original output.
The final comparison observes snapshot mutations made during either query.
No second threshold gate or invented state/value reset was added.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest slot | `0x150461D0..0x15046460` |
| Retail ROM interval | `0x73680..0x73910` |
| Linked size | 656 bytes / 164 words, no trailing slot padding |
| Differing words | 0 |
| Following symbol | `func_15046460 = 0x15046460`, unchanged |
| SHA-256 | `b8e8ed12477a0350a2cc502b2629563b95ef81f930a15bc76d207c643f2ae950` |

The full slot was independently compared using `tools.match_progress`'s ELF
function loader against retail ROM bytes, including the return delay slot.

## Verification

Ten source-extracted freestanding 32-bit host tests in
`tools/tests/test_game_lowest_height_combiner.py` cover early rejection for all
256 flag values, all acceptance combinations, strict/tied/unordered height
selection, full-record copies, low-byte truncation of positive/negative returns,
equal/NaN gates, preparation and query mutations, late first-snapshot mutation,
both-failed flag masking, all 65,536 selectors, and signed-zero threshold bits.
Only the three callees are mocked; the actual production body/layout is tested.
These are host behavior checks, not guest gameplay qualification.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_lowest_height_combiner
python3 -m unittest discover -s tools/tests
make tools-check
```

All 296 tool tests pass. Twelve exact neighboring cache/dispatch/query routines
remain retail-identical; the four semantic entity-query slot hashes remain
unchanged from Notes 765 and 771-773. The collector's 5,712 bytes, producer's
504 bytes, and return closure's 16 bytes remain retail-identical. Both entire
Init sections match retail: 164,048 code bytes and 17,376 initialized-data bytes,
with the hashes in Note 768. No host-port build, compressed-ROM build, guest
execution, or gameplay test was performed.

## Progress / Next

Fresh inventory: total 5,461 / 6,042 C rows (90.38%), 1,930,620 / 2,256,728
C bytes (85.55%); Game 4,788 / 5,321 C rows (89.98%), 1,759,184 / 2,072,880
C bytes (84.87%). Matcher: total 3,263 / 5,461 exact (59.75%); Game
2,590 / 4,788 exact (54.09%). Zero drift; 2,198 different C rows remain.
README contains only aggregate changes; detailed updates stay in DOCS.

Next recover the existing zero-return `func_15046460` highest-height combiner.
Its opening assembly rejects when `position[1] < threshold` and clears state
and value as well as flag bit 2; do not mechanically invert this lowest-height
body without inspecting the full success/failure publication paths. Remaining
entity-query byte matching and runtime qualification are still separate work.
