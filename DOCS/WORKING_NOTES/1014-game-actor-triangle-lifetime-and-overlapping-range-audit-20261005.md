# Game Actor Triangle Lifetime And Overlapping Range Audit

Date: 2026-10-05. Starting checkpoint: `8197f874`.

Continue [Note 1013](1013-game-actor-triangle-layout-screen-20261005.md) on
`func_1502F490`, not another conversion batch. **Production remains unchanged**:
298 body / 302 slot words, frame 0x160, 275 differing words. The function is
complete semantic C, not byte-exact. The original matrix leaf/tail remains
retained assembly. No guards or compiler profiles are added.

## Compiler Controls

[Lifetime driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_triangle_lifetime_candidates.py)
banks **34 controls**: partial/full phase scopes, dead temporary reuse,
range-do loops, edge cursors, vertex capacities 3/8, direct metadata accesses,
indexed vertex cursors, pointer bounds and four weight-selection shapes.
All compile without diagnostics. The **29 fitting forms** each pass **66
bounded retail/C guest cases**, **1914 comparisons total**. Five oversized
forms are not installed or claimed qualified.

| Representative Form | Body Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Installed checkpoint | 298 | 0x160 | 275 |
| All phase scopes | 298 | 0x160 | 275 |
| Reused dead temporaries | 298 | 0x148 | 278 |
| Reuse plus range-do loop | 294 | 0x148 | 295 |
| Reuse plus edge pointers | 300 | 0x150 | 275 |
| Direct ID/count/range | 303 | 0x140 | 292 |
| Direct metadata/indexed vertices | 305 | 0x138 | 300 |
| Direct metadata/range-do/indexed vertices | 298 | 0x130 | 297 |
| Short ID/count types | 298 | 0x160 | 275 |
| Less-than outer point bound | 295 | 0x158 | 295 |
| Nonzero-first if/ternary weights | 297 | 0x160 | 275 |
| Truthy ternary weights | 300 | 0x160 | 275 |
| Initialized fallback weights | 295 | 0x160 | 274 |

Phase scopes and short metadata types do not reduce the frame. Dead temporary
reuse reduces it by 24 bytes but changes early register allocation and raises
the difference count. The 0x138-frame control exceeds the 302-word slot and
does not recover the retail saved-register/array schedule. The smaller 0x130
frame also changes the saved-register block and has 297 differences. None is
installed on the strength of a frame size alone.

The initialized-weight control improves the raw difference count by one word,
but its frame remains wrong and it shortens the body to 295 words instead of
recovering retail's 302-word control flow, including the cold-path duplicate
`mtc1` schedule. Its 66 bounded probes are not complete production acceptance.
It remains a recorded candidate, not a new exact function or an installed fix.

Bounded cases include IDs 0/7/127/255, both O32 stack phases, accepted/rejected
weights, two overlapping ranges, live ID/buffer/source/vertex/input mutations,
ordered null/count gates, degenerate and signed geometry, output aliases,
single-precision rounding, sparse high joints and high unsigned counts.
Ordinary cases execute the real 40-word matrix leaf; mutation cases use the
qualified callback model. Compare complete external memory, ordered external
writes and seven-argument call logs. This does not qualify all retail assets,
FCSR/traps/subnormals/legacy NaNs or PC gameplay.

## First-Match Gate Closed

[Transform tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_triangle_transform_match.py)
now explicitly test two overlapping-range shapes under both stack phases.
Expected matrix indexes are `(0,0,2)` and `(0,1,1)`, for both matrix banks.
The third range is unmapped so premature continued scanning fails. An
incorrect overwrite/last-match C control produces different call logs and
is rejected. This closes the explicit missing gate identified in Note 1013.

The complete transform module now covers **1719 three-way guest cases**;
300 / 302 reachable retail words and the existing 53 / 53 matrix/continuation
words remain its coverage boundary. The native independent-reference fixture
now includes the same overlap shapes: **64512 whole-state/reference cases**
(256 IDs x 18 patterns x 14 mutation modes), plus **33 alias cases**.
An initial two-test overlap/native run passes in **25.173 seconds**, no skips.

[Driver tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_triangle_lifetime_candidates.py)
check its 34-name inventory, source anchors, fail-closed replacements, weight
mode validation and unchanged production-source binding. No shared oracle
or production assertion is weakened.

All **57 focused checks pass in 309.237 seconds, no skips**, covering the
new driver, complete transform, buffer copy, coordinate phase, update pass
and dispatcher. `make tools-check` and whitespace checks pass. The prior
355-test full-regression receipt belongs to the unchanged production
checkpoint; the full resource/tool corpus is **not rerun in this audit**.
The current edits are confined to tests, a new experiment driver and docs.

A fresh live-ELF audit agrees with all **6060 checkpoint function slots**,
including addresses and lengths. Complete Init **164048 bytes**, Init data/
rodata **17376 bytes**, Debugger **19800 bytes**, and Game data **189088
bytes / 720 owners** remain retail-exact. The patch CSV remains **10622 rows**,
SHA-256 `b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.
All **2981** checked relative links resolve across twelve current/working-
note/README documents.

## Frame Evidence And Next

One accepted retail/installed trace observes no memory accesses in the lower
gaps: retail SP+0x50..+0x7C (**44 bytes**) versus current SP+0x50..+0xB8
(**104 bytes**). Retail's SP+0x100..+0x114 inter-array gap (**20 bytes**) is
also untouched in that trace. This is trace evidence, not proof for every
possible execution or an assertion that the retail vertex array has capacity
eight. Call these reserved private homes/gaps, not confirmed live spills.

The next useful investigation is mixed scalar/array declaration placement
and compiler-reserved homes while retaining the original argument spills
and independent early/SDK pointer lifetimes. Reusing a pointer across phases
can force it into a saved register earlier than retail; inlining the cached
ID can keep the actor in S5 and alter the whole saved-register block. Do not
repeat plain phase scopes, short metadata types or a frame-only optimization
as if they resolve that allocation problem. Preserve the now-qualified
first-match gate, fresh second-source reload and ordered coordinate aliases.

Current exact C remains **3304 / 5462 total**, **2631 / 4789 Game**, zero
address drift, **2158 different**. README aggregates remain accurate and are
not changed. The 47 retained Init ASM routines and sibling sources/builds/
saves/frozen Release are untouched. No host transplant or push.

## Reproduction

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_lifetime_candidates
wsl python3 -m unittest tools.tests.test_game_actor_triangle_lifetime_candidates tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_buffer_copy_match tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

The Game goal remains active; no new byte-exact function is claimed here.

The subsequent declaration-only private-array home recovery is recorded in
[Note 1015](1015-game-actor-triangle-private-home-recovery-20261005.md).
