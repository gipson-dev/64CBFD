# Game Actor Triangle Cached Iterator Audit

Date: 2026-10-05. Starting checkpoint: `dd07fb80`.

Follow [Note 1016](1016-game-actor-triangle-reduced-frame-and-read-lifetime-screen-20261005.md).
No production code, assembly, compiler profile or guard changes. Installed
`func_1502F490` remains 302 words / frame 0x140 / 242 raw differences, with
all seven retail private homes but early ID/count reads 10/3 versus 1/1.

## Measured Controls

[Cached iterator driver](../../tools/experiments/game_actor_triangle_cached_iterator_candidates.py)
freezes the recovery independently of production. It screens 32 cached
metadata/output-cursor forms, 14 isolated early-pointer/determinant forms,
and 32 mixed early-range/late-edge bounds: **78 controls**, two IDO O2/g3
compiles per control to recover the SP-relative array homes. All compile
without diagnostics. No added locals solely for padding or enlarged arrays.

| Form | Body Words | Frame | Raw Differences | Early ID/Count Reads |
| --- | ---: | ---: | ---: | ---: |
| Installed checkpoint | 302 | 0x140 | 242 | 10/3 |
| Cached XYZ byte counter | 302 | 0x158 | 204 | 1/1 |
| Cached XYZ counter, separate offsets/base | 302 | 0x160 | 199 | 1/1 |
| Mixed range/edge bounds, same separation | 306 | 0x160 | 281 | 1/1 |

The default screen has 15 fitting forms / **990 bounded guest comparisons**;
all 14 isolated forms fit / **924 comparisons**. All 32 mixed forms exceed
the 302-word slot (306-309 words) and receive zero full comparisons. Their
accepted-path homes/read histories are measured, not full qualification.
The 1914 fitting comparisons use the existing 66-case bounded helper model;
they are not the full production native or connected-helper qualification.

All controls retain retail SP-relative homes and the separate relative-Y
history 5.5f then 1.25f versus blend-Y 1.25f once. Cached forms restore 1/1
early reads, but the best raw-score forms reserve 0x150-0x160 frames. None
is installed: smaller raw difference counts do not justify the frame
regression or claim the opening actor/SDK register lifetime is recovered.

An additional three-profile probe of the default cached XYZ-counter source
uses the same defines/includes/link symbols, replacing only `-g3` with
`-g0`, `-g1` or `-g2`. O2/g0 gives 301 words / frame 0x158 / 285 differences.
O2/g1 and O2/g2 each give 458 words / frame 0x110 / 458 differences and
IDO's warning that optimization requires g3. These are one-off compiler
receipts in ignored `profile-screen.json`, not installed profiles or
semantic/home-qualified controls. Do not infer correctness from them.

## Tests And Handoff

[Inventory tests](../../tools/tests/test_game_actor_triangle_cached_iterator_candidates.py)
bind all 78 names, unchanged capacities, cached reads, distinct mixed bounds,
fail-closed isolation/placement anchors, and three representative compiler
receipts. Two fitting representatives rerun all 66 bounded comparisons.

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_cached_iterator_candidates
wsl python3 -m tools.experiments.game_actor_triangle_cached_iterator_candidates --isolated
wsl python3 -m tools.experiments.game_actor_triangle_cached_iterator_candidates --mixed
wsl python3 -m unittest tools.tests.test_game_actor_triangle_cached_iterator_candidates tools.tests.test_game_actor_triangle_frame_candidates -q -f
```

Production counts and README aggregates are unchanged: 3304/5462 total,
2631/4789 Game exact, zero address drift, 2158 different Game C functions.
No host transplant, sibling build/save/frozen Release change or push.

The nine focused inventory/frame tests pass in 8.094 seconds, no skips.
`make tools-check` and whitespace checks pass. All 6060 live ELF slot
addresses, lengths and hashes agree with the accepted `dd07fb80` receipt.
The prior 367-test production corpus is not rerun for this audit-only commit.

Triangle next: original actor spill, cached metadata, SDK cursor lifetimes
and last eight frame bytes must agree together. Do not repeat mixed-bound
or debug-profile controls as unmeasured proposals. Continue the broader
Game goal with the 107-word actor context dispatcher `func_15044380`, whose
remaining frame/register lifetime is smaller and independently reviewable.
