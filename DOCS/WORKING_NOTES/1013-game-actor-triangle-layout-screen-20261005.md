# Game Actor Triangle Layout Screen

Date: 2026-10-05. Starting checkpoint: `623b96ae`.

After banking [Note 1012](1012-game-actor-triangle-remap-semantic-recovery-and-matrix-tail-restoration-20261005.md),
continue byte matching `func_1502F490` with a narrow array/output-pointer
screen. **No production source, linked instruction or progress count changes.**
The installed semantic C remains 298 body / 302 slot words, frame 0x160,
275 real differences; original matrix leaf/tail assembly remains exact.

## Reproducible Screen

[Candidate driver](../../tools/experiments/game_actor_triangle_layout_candidates.py)
provides ten forms, written only under `conker/build/game-actor-triangle-layout`.
It combines the checkpoint or an explicit three-output-cursor loop with two
array declaration orders and vertex capacities 3/8. These larger capacities
are controls, not an assertion of retail array extent.

| Form | Body Words | Frame | Differences | Bounded Guest Cases |
| --- | ---: | ---: | ---: | ---: |
| Checkpoint | 298 | 0x160 | 275 | 24 |
| Explicit XYZ output cursors / byte counter | 308 | 0x170 | 284 | 0 |
| Checkpoint, reverse home order, capacity 3 | 298 | 0x160 | 275 | 24 |
| Checkpoint, reverse home order, capacity 8 | 298 | 0x178 | 275 | 24 |
| Checkpoint, forward home order, capacity 3 | 298 | 0x160 | 275 | 24 |
| Checkpoint, forward home order, capacity 8 | 298 | 0x178 | 275 | 24 |
| Output cursors, reverse home order, capacity 3 | 308 | 0x170 | 284 | 0 |
| Output cursors, reverse home order, capacity 8 | 308 | 0x180 | 284 | 0 |
| Output cursors, forward home order, capacity 3 | 308 | 0x170 | 284 | 0 |
| Output cursors, forward home order, capacity 8 | 308 | 0x180 | 284 | 0 |

All ten forms compile without diagnostics. None reduces frame size or real
differences. Declaration reordering changes emitted bytes, even though the
body length, frame and total difference count remain the same. Equal metrics
are **not** proof of identical instruction layout or lifetimes. No nonbaseline
form is byte-identical to the checkpoint.

All five fitting forms pass **120 total bounded retail/C guest comparisons**:
IDs 0/7/127/255, both O32 stack phases and three coordinate cases (accepted,
accepted despite weight sum > 1, and rejected). Whole external memory, ordered
external writes and seven-argument call logs agree. Oversized 308-word forms
are not installed or claimed qualified. This screen does not repeat the
complete semantic/native/tail suite for each candidate and is not sufficient
to ship a new production form.

## Audit Boundary And Next

The saved GPR block already occupies retail offsets +0x28..+0x4C. The frame
mismatch is above it in private arrays/spills; simply naming three output
pointers and a byte cursor does not recover their retail allocation. The
qualified production checkpoint remains unchanged across all 6060 slots.
Its 53 focused / 355 full regression tests and complete protected-section
audits remain the evidence for that checkpoint, not new tests of these ten
forms. No new guards, compiler profiles, sibling builds or push.

The new driver passes Python compilation and `make tools-check`; whitespace
checks pass. A fresh live-ELF comparison agrees with all 6060 checkpoint slot
receipts, and the patch CSV hash remains unchanged. All **2972** checked
relative links resolve across eleven current/working-note/README documents.

Current exact C remains **3304 / 5462 total**, **2631 / 4789 Game**, zero
address drift, **2158 different**. README aggregates do not need another edit.

Next: investigate the spills' actual use/lifetime and first-use ordering,
including the separate float-edge loops and matrix-loop bounds. The original
array homes and detailed semantic gates are in Note 1012. Preserve its fresh
source reload, first-match range selection and ordered aliased coordinate
updates. Add an explicit overlapping-range first-match control before
altering range loops. Do not install the larger cursor form or mask the
remaining differences with a broad guard batch.

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_layout_candidates
wsl make tools-check
git diff --check
```

The Game goal remains active. This is a bounded negative matching audit,
not a new exact function or a reason to pause.
