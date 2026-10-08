# Game Graph Edge Crossing Lifetime Improvement

Date: 2026-10-06. Starting checkpoint: `10ee9722`.

Continue matching `func_15086D94` in
[generated_B3020.c](../../conker/src/game/generated_B3020.c), preserving the
complete semantic recovery from
[Note 1025](1025-game-graph-edge-crossing-recovery-20261006.md).
**Real differences improve from 151 to 102. This is still not byte-exact.**

The entire **207-word / 828-byte slot now emits from C without padding**.
Frame improves from the preceding 0x78 shape to **0x80**, but retail is 0x90.
Slot: 0x15086D94..0x150870D0, ROM 0xB4244..0xB4580. No new guards, compiler
profile, assembly, overflow, insertion/omission or data ownership change.

## Recovered Lifetimes

- Preserve original start/end sides separately from their conditionally
  negated copies. Copy the start side before calculating the end side.
- Use an explicit five-byte edge cursor. Retain indexed 16-byte node addresses
  with `i << 4` and `id << 4`, avoiding the unrelated running-record stride.
- Initialize owner index before the positive-count gate and use a do-while
  outer loop. Its closing condition spells `i < D_80087290`; IDO common-loads
  this nonvolatile global, so the linked body still contains exactly **one**
  signed count load after the height callback. It does not reload the count
  during iteration. This closes the retail signed-less-than loop tail rather
  than emitting the preceding equality test.
- Name the two intersection coordinates before evaluating their tangent
  distance. Preserve operation association, conditional negation, endpoint
  rules, unsigned record filters and the full s32 height result.
- Keep minimum 100.0f and retail's **last-fraction result**, including later
  rejected finite-edge crossings. Do not return the minimum or initialize
  the unused no-hit fraction.

The ten-word saved-register/query-X prefix at offsets +4..+0x28 and the
complete seven-word loop tail at +0x2A8..+0x2C0 now emit directly and match
retail. Argument homes still reflect the non-matching frame. These are
specific matched regions, not a claim that all saved-register scheduling or
the complete body is byte-exact.

## Compiler Screen

[Lifetime driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_graph_edge_crossing_lifetimes.py)
retains the previous 151-difference source as an independently compiled
checkpoint. Eight mutually exclusive screen modes provide **209 unique
source controls**, all compiled under the existing no-unroll profile with
empty diagnostics. Each mode writes its own ignored JSON receipt under
`conker/build/game-graph-edge-lifetimes/`.

| Mode | Controls |
| --- | ---: |
| Paired/array local layouts (default) | 54 |
| Counted-loop shapes | 16 |
| Side-copy timing | 21 |
| Named integer endpoint coordinates | 40 |
| Register hints | 26 |
| Declaration/member order | 31 |
| Reused float parameters | 6 |
| Named geometric temporaries | 15 |

| Form | Words | Frame | Real Differences |
| --- | ---: | ---: | ---: |
| Frozen installed checkpoint | 206 | 0x78 | 151 |
| Paired minimum/fraction | 206 | 0x78 | 149 |
| Early side copies / indexed counted loop | 206 | 0x80 | 129 |
| Global-condition counted loop | 207 | 0x80 | 103 |
| Named intersection point (installed) | 207 | 0x80 | 102 |
| Baseline side array (not installed) | 207 | 0x90 | 187 |

Array layouts can produce the desired frame but introduce non-retail stack
spills and saved-register choices. Oversized and narrowed/signedness control
forms are not installed. Register hints and declaration permutations do not
improve the 103-difference loop checkpoint; do not repeat that screen as a
promising physical-register fix. No arbitrary unused padding local is added.

## Qualification

[Edge tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_graph_edge_crossing_match.py) now
compare **four** guest bodies with the independent float32 reference: retail,
installed source, original semantic baseline and the frozen 151-difference
checkpoint. The 2177-case corpus preserves ordered height calls, external
writes, full non-stack footprints and saved GPR/FPR state at both stack phases.
The 288 native cases extract the actual installed source and check all 8192
record bytes and globals. Retail's late-rejected-crossing, endpoint, full-band,
wide-ID, signed-count, mutation and unordered-coordinate boundaries remain.

[Lifetime tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_graph_edge_crossing_lifetimes.py)
bind the 209-control inventory, complete fitting length, exact saved prefix
and loop tail, single count load, selected-source identity and frozen
checkpoint hash. The paired-local rewriter protects struct member declarations
while replacing scalar uses and rejects missing input instead of silently
generating a different experiment.

All **62 combined tests pass in 239.103 seconds**, no skips: four lifetime
screen tests, 13 edge tests, 15 root lookup tests, 14 parent tests, three
parent-lifetime tests and 13 visitor regressions. Five pre-install four-body
checks also passed before changing production source.

Executed retail coverage remains **198/207 words**; the nine unvisited
negative-extent words at 0x15087004..0x15087024 remain an explicit bounded gap.
No shared oracle changes. Full production helper-chain/gameplay/FCSR and
exception-mode acceptance remain separate; parent/root behavioral fixtures
still use opaque callbacks.

## Linked Audit

The before receipt equals all 6059 slots from the committed checkpoint.
After rebuilding, every name, address and length survives. **Only
func_15086D94 changes**; all other 6058 slots, including the direct-matched
root and 282-difference parent, remain byte-for-byte unchanged.

Target SHA-256:
`f09995b4041d5bc71e391c716b87cd775b915726fe676b4d8928423d268c1530`.
Before/after/audit receipts live under ignored
`conker/build/game-graph-edge-lifetime-test/`; behavioral receipts remain
under `conker/build/game-graph-edge-crossing-test/` and now report four models.

Init **164048 bytes**, Init data **17376 bytes**, Debugger **19800 bytes** and
Game data **189088 bytes / 720 owners** remain retail-exact. All **10643 CSV
guard rows** remain unchanged. Build/progress/match-progress and tool checks
pass; the unrelated duplicate generated_12D630 recipe warning is unchanged.
Whitespace checks and **3045 relative links across nine documents** pass,
zero broken links. No generated experiment/build output is committed.

Counts remain **3309/5462 total exact (60.58%)**, Game **2636/4789 (55.04%)**,
Init **492/492**, Debugger **181/181**, zero drift and **2153 different Game C**.
README aggregates/date remain correct and unchanged; this improvement is
documented here, not as a function-by-function narrative in the main README.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --loops
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --sides
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --coordinates
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --registers
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --declarations
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --parameters
wsl python3 -m tools.experiments.game_graph_edge_crossing_lifetimes --geometry
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_graph_edge_crossing_lifetimes tools.tests.test_game_graph_edge_crossing_match tools.tests.test_game_root_neighbor_lookup_match tools.tests.test_game_zone_neighbor_selection_match tools.tests.test_game_zone_neighbor_selection_lifetimes tools.tests.test_game_record_neighbor_visit_match -q -f
wsl make tools-check
git diff --check
```

Wait for relinking to finish before linked-image tests. Next match the retail
**0x90 frame and minimum home +0x50** (current +0x58; fraction already +0x54).
The normal still uses F14/F20 rather than retail F12/F14; start/copy values
use F12/F18/F16 rather than F18/F16/F20. Normal rotation and the second plane's
constant lifetime also differ. These are not merely two independent schedule
words and are not fixed by reordering declarations or adding register hints.
Continue with meaningful calculation/scoped-local lifetimes; do not install
array spills or a broad guard replacement simply to force the frame.

Then revisit the parent's private homes/address lifetimes and connected helper
qualification. No sibling source/build/save/frozen Release change or push.
The full Game matching goal stays active.
