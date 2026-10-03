# Game Highest-Height Query Semantic Recovery

Date: 2026-10-02

Follow-up: [Note 760](760-game-collector-context-assembly-restoration-20261003.md)
restores the then-placeholder collector/context group to original byte-exact
assembly. The query itself remains non-matching; gameplay qualification is open.

## Result

`func_150450CC` replaces its zero-return placeholder with the complete recovered
candidate selection and result publication routine. It remains non-matching:
143 compiler body words fit its 144-word / 576-byte retail slot, followed by
one padding nop. A fresh linked comparison reports 76 differing word positions,
down from the placeholder's 135. No word guards, overflow body, compiler profile
override, or assembly replacement were added for this function.

The checkout began clean at `cfb42bc`, nineteen commits ahead of origin. The
slot remains `0x150450CC..0x1504530C`, ROM `0x7257C..0x727BC`.
C representation and matching aggregates do not change: the placeholder already
counted as C, and the recovered routine is still not byte-exact.

## Recovered Contract

Inputs are a three-float position pointer, a float threshold passed through the
mixed integer/float o32 argument layout, and a result pointer. Local structures
recover the actual guest strides and offsets:

| Structure | Bytes | Fields |
| --- | ---: | --- |
| Vertex | 16 | Signed halfword XYZ at 0/2/4; remaining ten bytes untouched |
| Triangle | 12 | Three vertex-array pointers |
| Candidate | 16 | Signed fixed height, triangle pointer, vertex index, unused word |
| Result | 36 | Height at 0; nine signed vertex halfwords at 4; metadata at `0x18`; flags/state at `0x1C/0x1D`; value at `0x20` |

The retail uses `D_800D3300` as an array address, not a loaded global pointer.
The local typed view reflects that evidence without rewriting the shared
header's older pointer declaration or unrelated consumers. Metadata is a
32-bit stored value; no host object ownership is inferred from it.

1. If position Y is below the threshold, clear flag mask `0x02` and return zero.
   Leave every other output byte and the query globals untouched; call no helper.
2. Otherwise set output height to the original `D_80098D44` value. Its retail
   bits at ROM `0x23D804` are `0xC61C4000`, representing `-10000.0f`.
3. Call the existing context-reset wrapper with mode zero. Then publish the
   reloaded XYZ and threshold to `D_800DBE68/6C/70/74`, and call
   `func_150A3A70` with X and Z truncated toward zero.
4. For a positive returned count, scan all sixteen-byte candidates. Convert
   signed fixed height to float and multiply by `1/256`. Select only heights
   at or below the current position Y and strictly above the current output
   height. Equal-height ties retain the earlier candidate. Position Y and
   output height are reloaded during the scan, preserving helper-time mutation.
5. If selected, cache its triangle's vertex-pointer base and vertex index before
   the copy. Copy three signed XYZ triples from sixteen-byte vertex records.
   Reload the candidate's triangle pointer afterward for metadata lookup.
6. If a metadata table exists, use the signed triangle index relative to
   `D_800DBE3C` (twelve-byte triangle stride); otherwise publish metadata zero.
   Set state to one, OR flags with `0x07`, and clear the value word.
7. Return one only when threshold is at or below the selected height. A selected
   height below threshold still publishes the result and retains flags `| 7`.
   Do not clear `0x02` on that path. With no selected candidate, clear `0x02`
   and return zero, retaining the sentinel or any helper-mutated output height.

NaN comparisons preserve the retail ordered-comparison behavior. No new bounds
clamp, null guard, or defensive result reset is added. Integer coordinate casts
are qualified only for finite, representable inputs in these host tests.

## Tests and Verification

Eleven new tests extract the actual types and function body into a freestanding
32-bit fixture, mocking only the context wrapper and candidate collector. They
cover guest layout, all 256 initial flag values on early/selected-failure paths,
inclusive upper/threshold bounds, highest selection and first ties, negative
fractional fixed heights, signed vertex extremes and stride, nonpositive counts,
strict sentinel exclusion, null metadata, negative in-array metadata indexing,
helper mutation/reloads, preserved padding, and NaN comparisons.

All 164 tool tests, `make tools-check`, and `git diff --check` pass. The full
`make -C conker NON_MATCHING=1 all match-progress -j4` code build passes.
Independent comparisons retain exact constructor, allocator, list processor,
overlap, and position/scale wrapper spans. The neighboring 108-byte
`func_15045714` also remains exact. Both complete Init sections match retail:
164,048 code bytes and 17,376 initialized-data bytes.

The query slot SHA-256 is
`64640310ebe9fdbfb77fbdd8c9a4794d7a53897feb86f643d838cc449b78ca34`.
It is a hash of the non-matching recovered slot, not the retail hash.
The following routine stays at `0x1504530C`. Total matching C stays
3,255 / 5,461 (59.60%); Game stays 2,582 / 4,788 (53.93%), with zero drift
and 2,206 differing C rows. README aggregates are unchanged.

## Declaration Boundary

A slice-wide typed declaration for `func_1510F800` changed the independent
`func_15045714` compiler register allocation and tripped its strict expected-word
guard. A block-scope declaration was also rejected by IDO when the later legacy
call redeclared the function. Neither experiment remains in production.
The slice's existing implicit-call convention is preserved; the fixture has
an explicit mock prototype. Global API declaration cleanup remains separate
work, not a claim of ISO C conformance or a reason to weaken existing guards.

## Collector Gap and Next Work

The production `func_150A3A70` is still a zero-return placeholder in
`generated_D0F20.c`, so the candidate-producing gameplay path is not qualified.
The retail body is explicitly nonstandard: it saves `$s0..$s7`, `$fp`, `$gp`,
and `$ra` in floating registers, uses a shared interior entry at `func_150A3B20`,
and branches to later shared cleanup. Its inventory boundary is not a complete
ordinary ABI function. Do not convert or restore only the first named span.

Next audit the complete handwritten collector/cleanup group in `asm/D0F20.s`
and its inventory/source owners, then bank a coherent restoration or establish
a whole-contract semantic rewrite. Keep this query in the non-matching cleanup
queue. Another ordinary source recovery can use `func_15045384`, but it does
not resolve the collector dependency.

No gameplay qualification, guest execution, compressed-ROM build, sibling
host-port edit, or frozen Release artifact change was performed.
