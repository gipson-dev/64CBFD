# Open sequence candidate screens

Date: 2026-11-12. This is a private screening handoff, not a production
conversion. Reproduce from the `64CBFD` root using
`wsl -d PSBBN --exec python3 -m tools.experiments.game_sequence_open_candidates`.
The tools packet stores both drafts and uses the existing O2/g3/no-unroll owner
compiler, independently assembled retail functions, owner-neighbor, pool and
register-metadata comparisons. Tools commit `45468e0` precedes this note.

`func_1501E81C`, VA `0x1501E81C..0x1501EA18`, ROM
`0x4BCCC..0x4BEC8`, is called by the just-restored slot-refresh path. The
selected uninstalled draft emits 128 words/frame 80 versus retail 127 words/
frame 72. It has 62 relocation sites on each side; 21 words match at the same
positions and 90 occur in the same relative order. These latter counts are
screening aids, not proof of equivalence. A 120-permutation local-declaration
screen found no exact candidate; a handful of union/array/control-flow forms
also failed. The two sizes, stack locals, conditional command scheduling and
register placements require further fitting and qualification.

The original saves the prior scene only when the initial selector equals
`0x25`, calls `func_1501D348`, then reloads the selector before deciding whether
to restore that saved word. If the selector becomes `0x25` only during the
call, retail reads the earlier stack word without initializing it in this
function. The current draft has the corresponding uninitialized C local and
must not be installed on the assumption that such a change is impossible.
`func_1501D348` can call other providers and can re-enter this sequence path;
reachability of that particular mutation is not established. The original
also retains dependencies on the still-placeholder `func_1501EA18` and
`func_1501E540`. A qualified solution needs a defensible guest/portable-C
boundary and real-helper or mutation evidence, not just a compilable draft.

`func_1501FC8C`, VA `0x1501FC8C..0x1501FE68`, ROM
`0x4D13C..0x4D318`, selects a pair of sequence points, clamps a percentage,
and either interpolates them or returns the first point. The selected
uninstalled draft emits 118 words/frame 96 versus retail 119 words/frame 96,
with nine relocation sites on each side. It has 68 aligned words and 87
ordered-equal words. Its candidate owner changes `.reginfo`, so even a later
target match needs an owner-level metadata audit. `func_1501F72C`, which
supplies the frame and points, remains a placeholder. Floating-point edge
cases, output aliases, helper mutations and the one-word control-flow
difference require qualification; no runtime or exact-match claim is made.

Both screens found all 56 other owner functions, normalized pools and
diagnostic categories unchanged. The teardown screen also retained register
metadata; interpolation did not. The screens ran using the mounted tools and
staged sibling dependencies with mounted fallbacks, preserving the sibling's
pre-existing work. No candidate was installed, no production ELF was rebuilt,
and no progress count changed. Last verified production Game count remains
**3,725 / 4,840 (76.96%)**, with 147 more exact functions needed for 80%.

The scoped Graphify refresh retained unrelated nodes: 59,928 before and
59,930 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
