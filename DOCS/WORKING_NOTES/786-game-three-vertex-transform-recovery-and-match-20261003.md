# Three-Vertex Transform: Recovery And Match

Date: 2026-10-03. Baseline: `a493827`.

## Recovered Contract

Full inspection of `conker/asm/71820.s:134` corrects the prior handoff:
`func_1504452C` is a vertex transform, not a sibling context dispatcher.
Its recovered interface is void with three vertex pointers, a 3-by-3 float
output, supplied sine/cosine coefficients, three origin coordinates, and a
signed byte offset. The no-argument zero-return placeholder is removed.

For each of exactly three pointers, add the byte offset, load signed halfwords
X/Y/Z at offsets 0/2/4, and publish:

```text
dx = vertex.x - originX
dy = vertex.y - originY
dz = vertex.z - originZ
output.x = dx * cosine + dz * sine
output.y = dy
output.z = dz * cosine - dx * sine
```

There are no helper calls, allocation, normalization, clamping, or trigonometric
evaluation. Coefficients need not describe a unit rotation. Each input pointer
is read when its iteration is reached; output is nine floats. The existing
16-byte `QueryVertex71820` representation supplies the signed coordinate fields.
Negative offsets are valid only when the adjusted address remains within the
appropriate readable allocation; no bounds defense absent from retail is added.

## Source And Guards

The first source shape explicitly distinguished the last vertex's store order;
it emitted 52 body words plus 23 padding nops and 67 differences. Removing that
unnecessary conditional produces retail's 75-word peeled loop and `0x18` frame,
with no padding. The resulting twenty differences are limited to these cycles:

- GPR `$t8` / `$t9` exchange.
- FPR `$f12` / `$f16` exchange.
- FPR `$f14` / `$f18` exchange.
- Independent origin-Y/origin-Z load order at offsets `0x24` / `0x28`.

Twenty expected-word guards normalize only those differences. They add/remove
no instructions and have no relocation changes. The arithmetic, loop bounds,
pointer increments, stores, saved registers, and return contract are retained.
No new compiler profile or assembly body substitution is used.

The guard regression reconstructs all 75 unguarded words from the retail body
and CSV expectations, applies the register permutations across the entire body,
then exchanges the two independent stack loads. It requires the result to equal
all retail words, not merely the guarded positions. Each CSV replacement is
also checked against the original word; extra/duplicate guards, omitted words,
insertions, and relocation changes are rejected.

## Tests

Eleven tests in `tools/tests/test_game_three_vertex_transform.py` extract the
actual production definition and vertex layout. Ten freestanding 32-bit/SSE
behavior tests cover identity, quarter turn, fractional origins, signed-halfword
extremes, positive/negative record offsets, pointer reordering/repetition,
non-unit coefficients, 128 coefficient/origin combinations, NaN propagation,
and a vertex at the origin. They check all nine outputs, preserved input bytes,
and guards on either side of the output. The eleventh test proves the bounded
word normalization described above.

Finite host results are compared bitwise with separate scalar calculations
under the existing no-FMA SSE harness; NaN comparisons check propagation, not
payload identity. This does not qualify MIPS floating-point bit parity, exception
behavior, misaligned/out-of-range addresses, or overlapping input/output storage.
It is not guest execution or gameplay acceptance.

## Final Verification

The final shared-CSV rebuild completes successfully. Independent extraction
matches all 75 words / 300 bytes against retail. Twenty expected-word guards
normalize the proven allocation/load differences; no padding remains.

| Item | Verified result |
| --- | --- |
| Guest interval | `0x1504452C..0x15044658` |
| Retail ROM interval | `0x719DC..0x71B08` |
| SHA-256 | `942d8eef361ca47eeb5fd3ceb5457f64dab3e9b7c383c270e657689584075a02` |
| Following symbol | `func_15044658 = 0x15044658`, unchanged |

All 416 tool tests, including eleven focused tests, pass. Full build/matcher,
project checks, and whitespace checks pass. All 22 previous exact regression
slots and nine prior non-matching hashes remain unchanged. The collector,
producer, and return closure remain exact; both complete Init sections match
retail with the lengths/hashes in Note 782. A shared-CSV timestamp causes the
broader code-object rebuild; warnings in other existing sources remain and
did not prevent the successful link and checks.

The unguarded 75-word slot hash is
`d53b305fecba415b0994e9619931da23ed1cc9a61dc5c6b36e78d5f217730e73`.
It has twenty differences before normalization. The initial conditional-store
shape's unguarded slot hash was
`00d0fd5babdf64ef9f68ce26a83f8b256c5735468077c9a1227a0c237e120cfb`.

Inventory remains 5,462 / 6,042 C rows; Game 4,789 / 5,321. Matcher increases
to 3,269 / 5,462 exact (59.85%) and Game 2,596 / 4,789 (54.21%). Zero drift;
2,193 different C rows remain. README changes only the aggregate matcher
tables; detailed recovery updates stay in DOCS.

## Next

Recover the explicit context argument of `func_1510F800` in
`generated_13BB20.c`, checking the complete eight-word wrapper and retained
assembly setter `func_150A49F4`. The current wrapper is not empty: it forwards
through a no-argument C call. Its incidental guest register forwarding must not
be mistaken for an explicit recovered C interface. This corrects the earlier
placeholder shorthand in Note 785.

Dimension helper `func_1507C3E0` remains empty and must also be recovered before
qualifying the actor/context chain. `func_15044380` remains non-matching at
twenty words, and actor preparation remains exact assembly with the stale-stack
index boundary from Note 784. Init's two small candidates remain deferred.
The vertex transform does not resolve any of those separate contracts.

The sibling port and frozen Release artifacts are untouched. No compressed-ROM
build, guest execution, host-port build, or gameplay test is part of this recovery.
