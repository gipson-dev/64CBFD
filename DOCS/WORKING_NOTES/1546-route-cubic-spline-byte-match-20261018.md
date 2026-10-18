# Route Cubic Spline Byte Match

Date: 2026-10-18. Consumer predecessor **a7df7c59**, tools predecessor
**81049a4**. Tools banked first as **b91fd0e**. Recover **func_150497E0**,
owner `generated_76C90`, VA **0x150497E0..0x150498A4**, ROM
**0x76C90..0x76D54**: **49 words /196 bytes /frame0x10**. One new guarded
byte match; the wider Game goal remains active. The vector builder and
derivative helper remain unfinished, not silently credited by these tests.

## Semantic Recovery

Replace the false zero-return C stub with
`f32 func_150497E0(f32 *points, s32 index, f32 fraction)`. Keep its address
name and a concise semantic comment. Its four-point window begins at
`points + index`. The sole current C caller is the already-matched
`func_15088D58`; its existing float-return/three-argument declaration is
correct and needs no edit. Other retained assembly callers are not converted
as part of this checkpoint.

Let the window be p0,p1,p2,p3, and half=-0.5*p0. Preserve each float32 rounding
node, not just the equivalent real-valued polynomial:

- Cubic: p3*0.5 + ((half + 1.5*p1) + -1.5*p2).
- Quadratic: p3*-0.5 + ((p0 + -2.5*p1) + (p2+p2)).
- Linear: p2*0.5 + half.
- Value: ((cubic*fraction + quadratic)*fraction + linear)*fraction + p1.

All source locals are used semantic values. No volatile qualifiers, dummy
stores, synthetic padding, inline assembly or compiler-profile change.
Declaration order and an explicit return value recover the retail frame,
coefficient homes and final return move. Native tests use valid float arrays
and bounded indices. Arbitrary guest index-word wrapping and aliases into
the argument/private homes qualify actual emitted MIPS, not portable C pointer
arithmetic or signed-overflow behavior for invalid native indices.

## Closed Normalization

The normal owner profile emits all **49 words/frame16**, with **34 different
words**. Append34 expected-word guards; this is **not** a direct/guard-free
compilation claim. The raw target has **zero relocations**, no pools, no helper
calls and no saved GPR/FPR changes. Preserve the derivative's raw placeholder
and its existing padded slot unchanged.

The target-specific symbolic lineage checker decodes all49 instructions.
It follows register values, constant bits, shifted/indexed addresses, private
memory, individual rounded add/multiply nodes, copies and the return. A full
49-operation bijection proves the same operation multiset, identical ordered
private stores, identical rounded return DAG, all final GPRs and FPR20..31.
Commutative operands are canonicalized; **floating operations are never
reassociated**. Both instruction budgets include the original final move,
JR and stack-restoring delay. There are no inserted or omitted words.

Retail reads input offsets0/4/8/12; raw reads0/8/4/12. Both first save A2 at
entry-SP+8, read all four points before either coefficient store, then store
quadratic at entry-SP-12 and linear at entry-SP-8 in that order. This ordering
gate is necessary even when the point window aliases the argument/private
homes. The normalization only reschedules independent reads/calculations
and routes temporary FP registers/commutative operands. It cannot move a read
across a possibly aliased store. Exact private writes/frame are preserved.

Raw input-read traces and fault register states are deliberately not claimed
equal. Raw NaNs compare class rather than payload; raw hardware FCSR, signaling
NaNs, exception timing and unaligned/MMU behavior are not modeled. The actual
guarded/padded function is instruction-for-instruction retail, including its
original operand order and schedule. No weaker model result is substituted
for the actual slot comparison.

## Focused Qualification

New tools: `experiments/game_route_cubic_spline.py` and
`tests/test_game_route_cubic_spline.py`. Ignored artifacts:
`conker/build/game-route-cubic-spline/`. Fourteen frozen input fingerprints
cover owner/ELF/guards/ROM, assembly, Makefile/symbol/header closure, prepared
IDO components and the live caller owner. This is a declared closure, not a
claim to fingerprint every unlisted dependency. Historical views are serial,
non-nesting and bound to the exact predecessor and first successor.

All **seven pre-install tests pass in44.950s**. The final **seven installed
tests pass in42.645s**, including two explicit alias-order gate mutations:

```sh
python3 -m unittest tools.tests.test_game_route_cubic_spline -v
```

- **18,212 three-way raw/padded/retail guest cases**, all49 target words,
  complete private/argument homes, saved ABI and full normalized/retail state.
  Cover finite cancellation, signed zeros, subnormals, infinities/qNaNs,
  sixteen fraction bit patterns, signed/large wrapping indices, both stack
  phases and guest point-window aliases into the fraction/coefficient homes.
- **71,216 native32 cases per O2/O0 UBSan profile**, including65,536 fraction
  steps. The exhaustive linear window0/1/2/3 independently expects1+fraction.
  Separate translation units use the actual typed C. Full input arrays and
  canaries remain unchanged; native indices stay inside valid objects.
- **Eight effective guest and native return-value controls** reject wrong
  window, half/basis/quadratic/linear coefficients, final point, missing final
  fraction and genuine FP reassociation. The cancellation fixture
  (-2,2^24,2^24,0) exposes reassociation. Native controls return wrong-result23,
  not a crash or private-offset difference.
- **Nine independent original/raw/padded links and216 three-way rebased
  cases** prove actual padding and the full slot at three code placements.
  There are no symbol bindings to synthesize or silently assume.
- **48 access-fault prefixes** cover normal, argument-home and coefficient-
  home inputs at both stack phases. Raw finite memory prefixes agree, while
  raw read/register traces differ as documented. Normalized/retail complete
  fault states and traces agree. No portable C fault or hardware FCSR claim.
- **96 three-way complete118-word caller executions** run555 connected
  helper words. Replace only the actual cubic body; the sole bounded provider
  supplies u16 atan. Public actor/record results, calls and saved ABI agree.
  The vector/derivative overlays are retail code for qualification; their
  production stubs and whole-gameplay acceptance remain open.
- Mutation checks reject all49 raw-word changes, an unexpected binding,
  all34 changed guard expectations, actual reassociation, both alias-order
  gate violations and all28 live/snapshot input changes. Preserve the one
  raw owner neighbor and all normalized pools/bindings. No existing guard,
  fixture, profile or shared padder implementation is weakened.

Shared padder/PC16 checks pass **eleven per tools copy**, both smoke checks
and root tools-check pass. Four task copies parse as ASCII/Python AST; both
pairs are byte-identical. Older mirror HEAD ddbdd16 stays fixed: preserve all
**1,218 previous dirty hashes**, adding only two absent paths for1,220. No
mirror commit/reset, push, new Claude call, host or frozen Release action.

## Installation Audit

Predict before editing production. Append only34 generated CRLF guard rows
after checking the complete old prefix and successor hash. Replace only the
cubic function and the now-partial-placeholder owner comment. Rebuild with
existing flags, no new Makefile rule:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_76C90.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv \
    -o build/conker.us.elf -o progress.csv match-progress NON_MATCHING=1
```

An initially unsuppressed progress command began rebuilding unrelated
objects due to the new guard-file timestamp. Stop that specifically verified
owned make process; confirm no compiler child survives. A subsequent dry run
showed only relinking/progress generation with the corrected flags. Complete
that relink and repeat the full audit and installed tests. Do not interpret
the aborted command or its existing-source warnings as a passing report.

Actual whole ELF still equals the **first prediction byte-for-byte**:
**167 changed bytes =166 target-code +one target-size encoding byte in
.symtab**. Zero metadata exclusions. Canonical definitions change only target
extent12->196; all **6,057 function addresses**, other bodies and all other
section bytes remain fixed. Actual owner/padding/relocations match qualified
output. Preserve every old guard byte. Protected Game data stays
**189,088 bytes /720 owners /zero differences**.

| Artifact | SHA-256 |
| --- | --- |
| Raw cubic target | b2d8f9b5410e50f177b8f8b59a4bbcb956473af9d1481f190f95cadc66d72468 |
| Whole ELF | 055db7d5df3a748216eb8cf6b24368f725a9ceda248401800f20de907fd784aa |
| Owner source | 3484c495a255bd206395c84453825482f9e53030eb7aef8edeab667ba78f2ce7 |
| Guards | af22dc5c79d21f0e0cab24517eae418e3e970d9309176c84fe52d12be0560362 |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Fresh official totals: **Game2,983/4,828 (61.79%)**, **total3,656/5,501
(66.46%)**, Init492/492, Debugger181/181, **1,845 different /zero drift**.
The old false C stub was already counted converted. Root README changes only
its Total/Game aggregate matching rows; function narratives stay in this note.

## Next Work

Continue the connected derivative **func_150498A4**, **62 words/frame0x20**,
VA0x150498A4..0x1504999C, ROM0x76D54..0x76E4C. Its retail body is complete
and read. The ignored `game-route-splines/scalar-value-first-last.c` probe now
emits62 words/frame32 with saved F20/SP8 and the correct cubic/linear private
homes. It computes the value before the derivative store, avoiding the bad
direct-expression reload of points[index+1] after an aliased output write.
It remains unqualified/uninstalled. Its copy/NOP budget and derivative-store
versus return schedule need an independent closed-lineage proof and real
input/output aliases. Do not weaken/reuse the49-word proof as blanket approval.

Keep **func_15088F30** open under Note1545. Ten bounded outer-loop probes and
six named-invariant/local-width combinations did not remove its three saves.
Five fresh owned UOPT mode5 traces completed, fired the diagnostic probes,
reached driver exit0 and preserved complete normal text/functions/bindings/
pools. They expose the current parameter/local allocation constraints; debug
real-number output is suppressed, so printed costs/timings are not evidence.
Ignored receipts/scripts remain in `game-route-vector-builder/allocation/`.
No new vector source or matching credit. Earlier malformed ad hoc spline
probes are not qualified candidates; only the complete pinned source above
is used for this match. Parent15087350 and the wider Game queues remain open.

Scoped Graphify refresh: **42,536 nodes /82,609 links /4,122 communities**.
Preserve19,398 nodes from2,972 excluded-but-existing files. All42,524 other
old IDs remain; three line-disambiguated UPDATE_LOG heading IDs relocate with
their labels preserved. The new note contributes seven nodes. Source target
and derivative resolve at L6/L22. New tools remain subject to the configured
submodule scan exclusion, not a fresh AST-coverage claim for those files.
Original graph and preservation audit are ignored task artifacts; no full-scan
purge, graph-output commit or history rewrite.
