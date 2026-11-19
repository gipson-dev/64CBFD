# Note 2575: Map-record dispatcher CFG relation

Date: 2026-11-19. Consumer baseline `437ab634837a4c53f4493303422a279b13e2fca8`;
tools baseline `a99a6f19009f1916f3d658ba87924c8e0f3be8b4`.

`func_15104A80` now passes a **complete paired control-flow/effect relation**
between retail's113 words and the existing private110-word C recovery. Both
retain the104-byte frame and all original sequence/packet homes. This closes
the source-ABI equivalence question around the differing dispatch branches and
argument setup. **No guard or source installation is made by this checkpoint,
and no conversion/matching credit is added.** The71 aligned word differences,
including the three-word length gap, still need a justified concrete layout
transformation followed by the independent object and whole-image gates.

## Relation and exact scope

`tools/tests/game_map_record_dispatch_15104a80_relation.py` interprets the
emitted instructions on both sides. Pure integer/address instructions can
advance independently. Ordered reads, writes, conditional decisions, calls and
returns must synchronize. Pending transfers and branch-likely annulment are
explicit, so a memory operation in a delay slot cannot silently disappear.

The abstract domain keeps32-bit modular affine equalities between GPRs, HI/LO,
immutable entry-register ghosts and the caller-owned saved-RA cell. Incoming
facts join by intersection. Every stable edge is checked again after the
worklist converges; the loop is qualified by its fixed point, not by a selected
execution count. Fresh read values overapproximate all synchronized memory
contents. Constant160 division has its signed truncation/remainder behavior;
the modeled instructions use non-trapping32-bit arithmetic.

The certificate contains61 paired effect-boundary nodes and77 edges, reached
after117 worklist steps. It checks21 read boundaries,20 writes,14 conditional
decisions,5 path-specific call boundaries and1 return boundary. Reachable
instruction coverage is110/113 retail and108/110 raw words. The remaining
retail indices67/84/103 and raw66/100 are unreachable constant setup; their
bytes and all14 relocation bindings remain covered by the existing fingerprints.

All ordered memory addresses, widths and stored values agree, including the
three copied nine-byte sequences, selected actor pointer and packet fields.
Calls agree on target, SP and explicit A0/A1 arguments. Return checks preserve
the actual incoming callee-saved registers, SP and RA; the callback's void V0
remains unconstrained. Potential writes aliasing the saved-RA cell discard its
value fact rather than assuming it survived.

The helper relation is explicitly a **source-ABI abstraction**: equal arguments
and memory receive the same public effects and synchronized arbitrary volatile
results while the caller-owned frame above argument homes survives. Raw call
continuation addresses differ. This does **not** claim literal temporary-GPR/PC
fault-state identity, equal physical callee-private RA spills, complete recovery
of `func_151177C0`, or recovery of queue consumer `func_15169260`. The previously
qualified original13-word wrapper, callback window, native bodies and bounded
access-prefix probes remain separate evidence. A future installed113-word body
must still be literally checked against retail, including its trap/PC layout.

## Fresh checks and retained evidence

Primary tools and a new941-file isolated sibling overlay each pass two fresh
tests. They compile the complete unchanged owner and recheck the110-word raw
fingerprint,104-byte frame, ten unchanged neighbors, original pools and five
unchanged pre-existing diagnostics before checking the relation.

The relation rejects131 effective instruction mutations covering every memory
offset, helper target, loop limit, relevant immediate and changed branch target
in both streams, including two explicit memory-delay annulment controls.
Twelve other mutations affect only redundant/unreachable pure
setup and intentionally pass the same relation; they are listed separately.
The abstract-domain test independently evaluates concrete witnesses across200
fixtures, including signed/wrapping affine offsets and incoming-branch meets,
and checks that materialization admits the original states.

The new runs import50 primary/51 overlay tool files, equal byte-for-byte except
the overlay's empty package bootstrap. The prior five-test semantic suites are
**fingerprint-reused, not described as freshly rerun**: all recorded task/import
inputs remain exact. Those suites contain1032 guest and native SDK32 cases,
O0/O2/O3 with UBSan/strict aliasing, effective source/instruction controls,
113 paired access-prefix cuts and61 original callback-window scenarios.
`make tools-check` passes freshly.

All1970 committed-baseline input fingerprints were checked before documentation
edits. Production source, original assembly, guards, Makefile, object files, ELF,
conversion CSV and root README remain unchanged. ELF SHA-256 remains
`d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.
The real independently dirty `64CBFD Tools` checkout retains its HEAD, exact raw
Git status and343 dependency hashes. Host Release and older private work remain
untouched. No Claude calls or push.

Fresh recount remains **4,565 / 5,516 (82.76%)**, Game **3,892 / 4,843 (80.36%)**,
zero drift and951 different;124 more matches are needed for85% at the current
denominator. The full85% goal remains active.

Graphify's normal update again refuses a shrinking corpus, preserving all
67,748 prior nodes. A scoped AST merge adds the two new checker files while
retaining prior node IDs and the original GLOBAL_ASM reference. This is not a
full-corpus re-extraction claim.

## Next concrete step

Derive the fail-closed relocation-aware instruction mapping for the original
dispatch/argument layout. Check the three inserted meaningful instructions and
every replacement against this relation; do not infer that71 literal rows are
automatically justified. Then qualify both object-padding routes, independent
symbol rebases, actual Make, strict full-image prediction and production audit.
Install, recount and credit the function only after those gates pass.

Reproduce: `python3 -m unittest
tools.tests.test_game_map_record_dispatch_15104a80_relation -v` under prepared
WSL. Ignored certificate and pipeline receipts are in
`conker/build/game-map-record-dispatch-15104a80-private/cfg-proof/` and
`qualified/CFG-relation.json`.
