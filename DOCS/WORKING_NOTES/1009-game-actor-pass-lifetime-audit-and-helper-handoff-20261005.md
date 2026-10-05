# Game Actor Pass Lifetime Audit And Helper Handoff

Follow-up: [Note 1010](1010-game-actor-reference-coordinate-phase-match-20261005.md)
recovers the connected coordinate phase; this caller baseline remains unchanged.

Date: 2026-10-05

## Checkpoint

Continue from `4a05e25a` and [Note 1008](1008-game-actor-pass-array-layout-and-connected-selector-20261005.md).
The production `func_1502BEE4` is unchanged: **175 body / 176 slot words,
frame 0x88, 109 differing words**, no word guards or compiler override.
Depths remain SP+0x3C, queue SP+0x58 and captured count SP+0x38. The
maximum-depth spill remains SP+0x78 instead of retail SP+0x34.

## Bounded Compiler Screens

Three reproducible source families were added to
`tools/experiments/game_actor_update_pass_candidates.py`:

- `--lifetime`: 24 forms reuse the actor pointer or existing index during
  predecessor traversal, with word/halfword/byte index and declaration-order
  controls. The word-index actor form is 173 words / frame 0x80 / 174
  differences; the word-index chain form is 188 words / frame 0x80 / 178 or
  179 differences. Narrow index forms change loop shape and do not improve it.
- `--scope`: eight forms move the traversal cursor into its actual branch
  scope, optionally using indexed outer traversal. Pointer-scan forms emit
  176 words / frame 0x88 / 133 differences; indexed forms emit 180 words /
  frame 0x88 / 168 differences. Correct length is not a matching proof.
- `--pointer-home`: 144 declaration-order forms keep the recovered pointer
  traversal and four-way sorting loop. All emit 175 words / frame 0x88;
  30 have 113 differences and 114 have 115. None places the maximum-depth
  spill at SP+0x34. No form improves the production 109 differences.

These are **176 compiled forms**, not 176 fully qualified alternatives.
Three additional exploratory inner-index forms also emit 176 words / frame
0x88 / 133 differences, with displaced stack slots. They are not selected.
No fake padding or broad instruction-word normalization was introduced.

## Stack And Lifetime Evidence

| Control | Body Words | Frame | Differences | Max | Depths | Queue | Count |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Retail | 176 | 0x88 | 0 | 0x34 | 0x3C | 0x58 | 0x38 |
| Production | 175 | 0x88 | 109 | 0x78 | 0x3C | 0x58 | 0x38 |
| `lifetime-actor-s32-1-1` | 173 | 0x80 | 174 | 0x34 | 0x3C | 0x58 | 0x38 |
| `lifetime-index-s32-1-1` | 188 | 0x80 | 178 | 0x34 | 0x3C | 0x58 | 0x38 |
| `scope-0-0-0` | 176 | 0x88 | 133 | 0x78 | 0x40 | 0x5C | 0x3C |
| `scope-0-1-1` | 176 | 0x88 | 133 | 0x3C | 0x44 | 0x60 | 0x40 |

Offsets above come from the emitted MIPS stack-address/load/store words,
not compiler debug-local metadata. The actor-reuse form has four saved
general registers rather than retail's three and keeps a stride constant
live into queued dispatch, replacing retail's shift sequence with multiply.
Matching all four private homes alone therefore does not recover retail's
register lifetimes or frame. The scope forms illustrate the converse:
correct frame/length can coexist with wrong homes and instruction schedule.

## Verification And Audit

The focused pass/dispatcher corpus passes **20 tests in 47.471 seconds,
no skips**. A new test compiles six representative controls, pins their
length/frame/difference and available stack-offset measurements, and compares
**48 completed guest cases** with retail. These cover reserved-slot roots,
deep chains through inactive predecessors, byte-mask wrapping, captured-queue
mutation and live later-slot activation, with volatile-register clobbering.
Twenty-four cases connect the actual selector and dispatcher; the other
24 use phase callback mutations. Full external memory/events and restored
saved registers/SP are checked. This bounded matrix does not qualify every
alternative or full gameplay; the existing 16384-case native production
reference test remains intact and passes.

No production or README changes are made in this checkpoint. The existing
6060 linked slots were snapshotted for the next helper audit. Tools and
whitespace checks pass.
The existing
linked pass hash remains
`c32708201e59edf73b9986867a0afa76d7a8da115d8a38d0f703cbaa85422758`.
The patch CSV remains unchanged at SHA-256
`22f784b5c5dc38114c6d2ed9da81fb74ea9ac3eb5c97c4a3be57d129d1fa4099`.
Exact counts remain **3302 / 5463 overall**, **2629 / 4790 Game**, zero drift;
these counts are carried from the last verified linked baseline, not a new
conversion or match. Sibling sources/builds/saves and frozen Release remain
untouched. No push is made.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --lifetime
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --scope
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --pointer-home
wsl python3 -m unittest tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Bank this audit, then recover **`func_1502F3C8`**, the 50-word actor attachment
coordinate phase called immediately after the captured updates. Inspect its
five-argument `func_1502F490` call and post-call float comparison before
implementing it. This is a connected helper path, not an abandonment or
completion claim for `func_1502BEE4`: its maximum-depth spill, phase-local
base/end address lifetime and final schedule remain open. The Game objective
remains active.
