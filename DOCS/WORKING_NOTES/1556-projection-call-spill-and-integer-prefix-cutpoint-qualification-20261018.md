# Projection Call Spill And Integer-Prefix Cutpoint Qualification

Date: 2026-10-18. Consumer predecessor **eaac3a9b**; tools **d818afc** is
banked first. Continue `func_150891E8`, owner `generated_B3020`, retail
VA150891E8..150896EC /ROMB6698..B6B9C,321 words/frame120. Experimental source
and proof-tool qualification only: no installation, guard or matching credit.

## Joint Call-Lifetime Recovery

The complete semantic body now jointly recovers all six initial saved roles,
the original saved-register prologue, frame120 and the selected-node save at
SP+0x48 across the second selector call. Reuse the existing semantic `node`
pointer in the common phase and give the initial scan's candidate address its
own `candidateNode` lifetime. No dummy effects, register hints or padding.

Normal O2/g3 emits **335 words /frame120 /311 size-adjusted differing words**.
Raw SHA-256:
`3489534941741d693be663d176f5a0317142535fc75abd62513d10721befb305`.
All18 bindings are checked. Raw word257 stores AFA30048; word260 reloads
8FB10048. Initial table/anchor/record/current-ID/previous-ID/actor roles remain
S0/S1/S2/S3/S4/S5, including the correct selector child S0-save value.

All **575/575 complete memories** now equal retail, rather than404/575 in
Note1555. All575 public states/calls also equal the independent reference.
Public ordered traces agree in445/575 cases; this is not an all-access-order
or full fault-state claim. Root instruction coverage is274 raw /272 retail.
Both the334-word Note1555 point and321/frame120/221-difference Note1552 point,
their snapshots and existing owned compiler captures remain unchanged.

The14 extra words are entirely before the cycle cut: raw164 vs retail150.
Every later call is uniformly14 words later. The remaining171-word suffix
still has **69 aligned word differences**. Equal output/private memory does
not authorize removing14 words or rewriting those69 by appearance.

## Integer-Prefix Cutpoint Proof

New `game_route_projection_prefix_proof.py` checks seven initializer paths
and2734 universal one-iteration paths. It compares branch predicates, every
ordered memory operation/version, preserved GP/SP/RA and the repeat-state
index/count/cached-table relation. Matched loop constants are established by
the initializer and preserved at the backedge. Unrelated caller-scratch
inputs are distinct per side. Full-body delay-slot-aware GP liveness checks
that excluded scratch is not live into the loop or suffix cuts.

Hash-consed symbolic expressions share persistent store histories. Reads
retain the entire memory version; there is no assumed disjointness, load
forwarding or non-aliasing shortcut. Prefix FPU state is untouched. Two
independent data rebases pass, including signed LO16/HI16 carry boundaries:

| Set | Flags | Count | Table | Mode |
| --- | --- | --- | --- | --- |
| 1 | 80097FFC | 80098000 | 800D8004 | 800D7FFC |
| 2 | 00018000 | 00017FFC | 00028004 | 00027FFC |

Seven wrong-store/stride/object/flag/kind/type/sentinel controls fail. This
proves the declared integer-prefix relation for ordinary sequential byte
memory, including partial aliases. It excludes MMIO/asynchronous memory,
PC/dead-GPR exception states, the floating-point suffix, whole-parent rebases
and full-function normalization. No normalized object or word guards exist.
An effective scope control changes a suffix DIV.S to MUL.S: the prefix proof
still passes, while the full-parent guest oracle rejects the result.

## Advisory Finding And Fix

One bounded tool-free Claude Code Pro advisory reviewed this new proof's
soundness, not the prior allocation question. Effective tools=[] and
mcp_servers=[], one attempt, exit0, no observed tool calls. CLI2.1.218;
packet1055 whitespace words, SHA-256
`40e61f46c77729874a88c35f0b4074266b1e8988264cf4c8483ebdcaed3d4ef8`.
Advisory prose is not independent execution or a proof certificate.

Independently reproduce its concrete issue: the old GP liveness decoder
omitted CTC1's GP read. Inserting CTC1 T0,FCSR at raw word165 falsely passed
the suffix-interface check. Neither frozen body contains CTC1/CFC1; both
contain only COP1 rs4/8/16/20, counts13/3/35/9. The frozen-prefix result was
not affected, but accepting that altered suffix was a real tool defect.

Fix MTC1/CTC1 reads and MFC1/CFC1 definitions, reject unsupported COP1 rs,
and test all four moves plus the actual inserted live-scratch counterexample.
Also explicitly require the frozen epilogue cuts, raw327 /retail313; changed
early-exit offsets on either side now fail. This does not claim a complete
general-purpose MIPS decoder or synchronized exception PCs. Retain the packet,
answer, lifecycle receipt and independent reconciliation under ignored build
artifacts. No second review, compiler observation or new dependency setup.

## Fresh Qualification

`python3 -m unittest tools.tests.test_game_route_projection_call_lifetime_fit -v`:
**eleven tests pass in24.879 seconds**, no skips. In addition to the complete
memory and prefix proofs above:

- 16 complete null returns and all240 actually fired null-access-fault-prefix
  memories agree. No full nonnull fault qualification is inferred.
- 1458 full-memory first-selector prefixes:243 five-slot patterns, three mode
  bytes, two preference flags. Helpers have not yet executed at that boundary.
- 24 high object-pointer cases and four private-preference-home alias cases.
  The compiled nonvolatile cached-preference control forwards0/1 instead of2.
- Five effective compiled semantic C controls; the negative-coordinate case
  is actually selected and both raw/retail pass the corresponding positive.
- 335 raw-word flips,18 binding removals and32 live/snapshot corruptions fail
  closed. Ten retained source screens and240 sampled public cases pass their
  audits but fail the retail extent, so none qualifies for installation.

Eight full-owner screens preserve72 like-for-like normal-profile neighbor
bodies/bindings and pools each. Two typed-global screens are isolated target
compilations; do not claim owner-neighbor coverage for those. The selected
point is not an accepted production profile override. The production owner
still uses its original no-unroll profile.

| Screen | Words /Frame /Different |
| --- | --- |
| Node lifetime | 335 /120 /311 |
| First-next, candidate-next, node-first-next | 332 /120 /308; different raw bodies |
| Typed table loop | 334 /120 /311 |
| Typed table node | 335 /120 /312 |
| Two-slot prefix | 282 /120 /297 |
| Two-slot prefix with inline address | 290 /120 /301 |
| Unsigned counter, unequal bound | 335 /120 /311; identical to selected |

Shared padder/PC16 tests pass eleven per tools copy; both smoke checks and
consumer tools-check pass. Three new task files are ASCII/AST valid and
byte-identical between primary and standalone mirror. Commands also include
`python3 -m tools.experiments.game_route_projection_call_lifetime_fit --qualify`
and `--audit`, requiring the prepared consumer and frozen sixteen inputs.
Ignored artifacts: `conker/build/game-route-projection-call-lifetime-fit/`.

## Resume And Preservation

Next analyze the14-word unrolled-prefix expansion and69 aligned suffix
differences. Recover the original321-word source shape while keeping the
joint saved-role/SP+0x48 contract. Alternatively, a structural normalization
needs its own closed transformation and complete suffix/FPU/call proof;
this prefix proof alone is insufficient. Native32, full-parent independent
rebases, nonnull fault/caller qualification, actual padding, first whole-ELF
prediction and installation audit remain open. Vector15088F30, other parent
150896EC and the wider Game queue remain open.

No production build/recount or matching credit. Source/ELF/guards/profile and
root README remain unchanged. Last freshly measured totals remain Note1554's
**Game2986/4828 (61.85%)**, total **3659/5501 (66.52%)**,1842 different /zero drift.
Live SHA-256 checks retain ELF6157cecd, parent-ownerf7db991f,
enqueue-owner31ed15c5, guardsd6a8f7c3 and Makefile840897f1.

Preserve standalone mirror HEADddbdd16 and all1240 prior dirty leaf hashes;
only the three absent task files are added, giving1243 dirty paths. No mirror
commit/reset, push, host-port or frozen Release action, save/configuration
change or original compiler-capture replacement. Root README stays aggregate
only; this handoff belongs here and in the concise documentation indexes.

Scoped Graphify refresh:42628 nodes,82693 links,4017 communities. Retain42616
old IDs; three duplicate UPDATE_LOG headings relocate uniquely with their
line offsets. Keep19398 nodes from2972 excluded-but-existing files, without
a full-scan purge. Tools stay outside the configured current graph corpus;
do not claim new Python AST graph coverage. Before graph and ID audit remain
ignored artifacts, with no tracked graph churn.
