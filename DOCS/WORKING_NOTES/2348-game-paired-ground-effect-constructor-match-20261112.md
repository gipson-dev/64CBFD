# Paired Game ground-effect constructor matches

Date: 2026-11-12. `func_150C6460` (`generated_F3270`) and
`func_150C6D90` (`generated_F3BA0`) replace zero-return placeholders with
semantic C. Each reproduces all **163 retail words**, using 90 checked,
relocation-aware guards including one inserted word. Their callers are
`func_150C5DC0` and `func_150C66F0`, respectively.

Both select a position from their actor or a transformed preset, query the
surface above and below it, construct a 40-byte effect descriptor and a
32-byte payload, and call `func_1513C73C`. On success the payload is copied
to the new effect. The two variants use distinct presets, scales, factory
variants and owner slots. The unused descriptor and payload bytes remain
untouched, as in retail; the factory copies the entire descriptor.

Tools commit `31b2eed` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_paired_ground_constructor_match -v
```

Both independent padders reproduce the complete retail bodies and relocation
bindings, while preserving nine other functions and the constant pools in
each owner. The eight-check suite passed with mounted tools and staged sibling
dependencies. Per function it exercises 80 ordinary cases, 1,808 overlap
cases, original callers, 96 connected RNG cases, 96 connected factory-wrapper
cases and 12 GNU links at three symbol bases. Forty overlap cases stop at the
same modeled exception in all four programs; they are not complete executions.
The connected factory test visits 100 of 104 helper instructions; transform,
query, palette selection and deeper allocation services remain modeled.
Native 32-bit builds at `-O0`, `-O2` and `-O3` each pass 40 cases with UBSan
and seven effective negative controls.

For each function 760 modeled memory-access cuts agree on public memory and
helper calls; the retail and padded programs additionally agree on full
modeled memory and access traces. The unguarded compiler body differs in
private frame state at 88 cuts because of instruction scheduling. These are
modeled fault prefixes, not proof of portable C fault semantics or gameplay.

The actual Make build matches the independently audited shadow ELF, binary
and owner objects. The strict image audit accounts for all **1,167** changed
bytes with zero exclusions; only the two target functions changed, all
**6,050** function addresses stayed fixed, and all **189,088** protected
Game-data bytes were unchanged. The other 1,452 linked objects and conversion
rows were preserved. A fresh linked recount reports Game **3,738 / 4,842
(77.20%)**, total **4,411 / 5,515 (79.98%)**, zero drift and **136** more
Game matches needed to reach 80%.

The scoped Graphify refresh retained or relocated all 59,959 previous nodes,
with 59,961 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
