# Sequence interpolation layout follow-up

Date: 2026-11-12. This is an uninstalled screen, not a matching conversion.
The reproducible 24-layout screen is in tools commit `58a7dcd`:

```sh
wsl -d PSBBN --exec python3 -m tools.experiments.game_sequence_interpolation_screen
```

For `func_1501FC8C` (VA `0x1501FC8C..0x1501FE68`, ROM
`0x4D13C..0x4D318`) moving the `times` pointer before the points array in the
local declarations improves the screening score from 87 to 93 ordered-equal
words out of 119. All 24 permutations of the first four declarations produced
118 words and a 96-byte frame. This score only measures words in relative
order; it does not prove execution or floating-point equivalence. The best
variant has 69 equal words in the same positions. All 24 retain the 56 other
compact owner functions, normalized constant pools, and diagnostic categories.

A further deterministic sample of 80 permutations across all eight local
declarations reached at most 91 ordered-equal words; this was a sample, not an
exhaustive search. Six control-flow forms and 16 zero/numerator/output-shape
experiments likewise produced no direct 119-word match. Some output-shape
experiments changed multiply operand order and were screening probes only, not
approved semantic replacements. Their scripts remain in the ignored local
`conker/build/game-sequence-1501fc8c-screen/` investigation directory.

The compact candidate's `.reginfo` differs from the baseline. The screen also
independently runs the project's generated-object padder and assembler on both
complete owners: their padded `.reginfo` bytes are identical and all zero.
This narrows the concern to compact metadata; it does not establish that a
future linked image or protected data is unchanged. A production Make build,
independent padding and full-image audit are still required.

The recovered assembly contains one direct `jal` reference, at
`0x1501F684` inside `func_1501EC38`; this is an assembly-text census and does
not exclude indirect calls. Its caller passes the first output pointer in
`a2`, the second in `a3`, the third at caller `sp+0x10`, and the group at
`sp+0x14`. The sequence sampler `func_1501F72C` is still a C placeholder.
The candidate reloads the runtime table after the helper, as the retail routine
does, but helper mutations, caller boundaries, memory access and output alias
behavior remain to be qualified.

The missing instruction is not safely resolved by length alone. Retail
computes `time - start` before comparing the segment duration with zero;
the best compiled draft computes it only on the nonzero-duration path.
Floating-point exception and non-finite behavior need explicit guest and
native investigation, alongside the closed register/scheduling changes and
any proposed relocation-aware guards. Do not assume the two instruction
orders are equivalent for every machine state.

Mounted tools and the staged sibling-dependency run returned identical
24-variant reports; the sibling checkout's 2,434 pre-existing dirty paths
remained unchanged under its preservation check. No production source, guard,
ELF or match count changed. A fresh production ELF recount confirms Game
**3,725 / 4,840 (76.96%)**, requiring **147** more exact Game functions for
80%; the total is **4,398 / 5,513 (79.78%)**, zero drift.

Next, recover a source/guard shape with a defensible floating-point boundary,
then qualify the real caller, modeled and real-helper behavior, both padders,
actual Make, protected data and strict independently predicted linked image
before installing or crediting the function. If that is not tractable, select
another Game candidate rather than crediting an incomplete interpolation.

The scoped Graphify refresh retained all out-of-scope nodes: 59,930 before,
59,932 after, and three relocated IDs matched by signature. Its fail-closed
path retained 31,816 existing nodes; this was not a full-corpus extraction.
