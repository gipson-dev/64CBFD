# Note 2572: Nearest-height ordered register relation

Date: 2026-11-19. Consumer baseline `e17ca32ee1bd495a1cc4cda3f858341421efee2e`;
tools baseline `0a1d0efa1ff3aa0fc3053e1adaa31b0b1e43fb5c`.

`func_15104634` now has a **272-word private C recovery with 121 remaining
register-field differences**, down from137. The original224-byte frame,
SP+0x60/+0x6C/+0x78 arrays, saved FP argument lifetimes and12 bindings remain.
A whole-body per-PC register relation now preserves ordered memory and FP
effects across the complete control-flow graph. **The candidate remains
uninstalled, with no word guards or matching credit.**

Production source, objects, ELF, guard history, Makefile, conversion CSV and
root README are unchanged. Fresh recount remains **4,564 / 5,516 (82.74%)**,
Game **3,891 / 4,843 (80.34%)**, zero drift and952 different. **125 further
matches** are needed for85% at this denominator. The full85% goal stays active.

## Source change that closes the ordered orientation gap

Sequenced product assignments added instructions and were rejected. Reusing
the orientation temporary for the later running minimum, reversing the two
source product terms and writing the Z-delta assignment first recovers the
original six coordinate loads and ordered arithmetic. The actual emitted
orientation block uses X0/X1 before Z0/Z1 and the original product/add/negation
sequence. Its only remaining two word differences are GPR fields for the
accepted-index address calculation. No FP commutation, reassociation, private
cell permutation, volatile qualifier or compiler-profile override is used by
the emitted-code relation checker. All121 differences change register fields;
instruction operations, constants, memory offsets and branch destinations agree.

The canonical text and raw fingerprint are in the six-file recovery fixture.
Four copied-owner neighbors and constant pools still compile unchanged under
the existing O2/g3 profile. The earlier compiler trace belongs to the previous
137-difference source; it is retained as historical layout evidence, not reported
as a fresh fingerprint-qualified trace of this candidate.

## Whole-body register invariant and its scope

`game_nearest_height_15104634_relation.py` propagates paired register-value
equalities, joins predecessor states by intersection and iterates loops to a
fixed point. It then rechecks every stable edge. The completed certificate has
**241 control-flow nodes,269 edges,839 worklist steps and all272 instruction
positions**, including the three fallback moves not visited by public fixtures.
Branch choices are conservatively overapproximated; no finite count or path
sample is substituted for loop closure. Normal and likely delay slots are
handled separately, including delay instructions also reached sequentially.

All memory operations must use related addresses and store values at the same
instruction position. Reads supply coupled values from equal memory, and writes
preserve whole-memory equality. Both provider calls occur before allocation
diverges; complete paired input register state is checked there. Return status,
saved registers, stack and return address agree. Arithmetic and comparisons
require the same operation, ordered operands and related FCSR state. There are
54 static potentially status-affecting FP sites,37 read sites,11 write sites,
two calls and one return. These are static site counts, not runtime visit counts.

Six effective instruction negatives reject a changed coordinate home, FP
product operand, branch destination, delay-slot index store, RA restore and
saved FP pair. The checker also rejects unsupported writes to architectural
zero and invalid double-register pairs. All1088 raw bytes and12 bindings remain
independently fingerprint-gated by the existing recovery test.

This is an emitted-code ordered-effect and live-role relation for synchronized
initial memory/FCSR and ordinary deterministic execution. It covers the same
memory/FP fault dispatch conditions and preceding effects under the role
relation; **raw physical temporary-register dumps are not asserted identical**.
It is not a hardware FCSR experiment, interrupt model, portable C fault theorem,
or permission to install literal replacements without the remaining guard,
padder, rebase, actual-Make and linked-image gates.

## Query size and the original overflow boundary

The model and SDK32 harness now allocate40 query records. Native cases exercise
query counts through39 with at most24 accepted upward-facing triangles. Keeping
the candidate's unchecked24-index local preserves its observed frame and homes;
25/26-index source controls increase the frame to232. This is evidence about
the selected source, **not recovery of the original debug array declaration**.

A separate paired emitted-instruction probe supplies25..39 all-upward hits.
Both instruction streams have identical ordered memory traces, public/private
memory, calls and outcome. Counts25/26 still fit the physical frame; counts27..29
overwrite now-unused incoming argument homes and return. At **30 accepted hits**,
the store for index29 reaches SP+0xEC, the saved output pointer. The later output
store then targets unaligned address29. Counts30..39 reach that same modeled
alignment boundary. No out-of-bounds native C case is executed and no new
runtime bounds check changes retail behavior. Original asset-level guarantees
and original declared local-array length remain unknown.

## Fresh checks and repository boundaries

Both primary tools and an isolated931-file sibling overlay pass **six tests**:

- 494 cases per original/private instruction stream, five effective instruction
  controls, complete public results/providers, saved F20/F22 pairs and the same
 269 dynamically visited words.
- 419 actual SDK32 C cases each at O0/O2/O3, strict aliasing, UBSan and
  float-cast-overflow checks; eight effective source controls per profile.
- The original21-word caller window still passes its32 scenarios per stream,
  checking F12/F14/A2/A3 and the actor-height clamp. Full caller/gameplay
  qualification is not claimed.
- Whole-body ordered register proof and15 paired overflow probes described above.

Primary314 imports and overlay315 imports have identical dependency bytes
apart from the overlay's empty bootstrap. The overlay contains339 unchanged
sibling files,585 explicit primary fallbacks,6 task files and1 bootstrap. The
real dirty `64CBFD Tools` sibling retains its HEAD, raw status and343 dependency
hashes. `make tools-check` passes. Of1954 committed-checkpoint inputs,1949 remain
unchanged and five are the explicitly fingerprinted recovery-tool updates; the
sixth task file is the new relation helper. No host source or frozen Release
artifact changes; the older private actor-burst candidate is preserved.

Graphify's native update again refuses a shrinking corpus. A scoped five-file
AST merge retains all67641 old IDs and adds the relation helper. This is not a
full-corpus extraction. Commit-hook writers must be observed terminal before
historical heading aliases and the final graph digest are sealed.

## Resume from here

1. Use the selected text and six tests in the committed nearest-height fixture.
   The private packet is `conker/build/game-nearest-height-15104634-relation-private/`.
   Do not restart rejected FP-expression, declaration or capacity screens.
2. Derive only the121 register-field guards from this closed role relation and
   original relocatable assembly. Qualify both padders, independent symbol
   rebases, guard negatives and the actual generated-C Make recipe.
3. Predict the complete linked image before installation, including the original
   stub's instruction-slot and symbol-extent changes. Audit every neighbor,
   address, protected section, data and guard/conversion row without exclusions.
4. Install only after those gates; rebuild production, run both installed suites,
   recount the real ELF, update aggregate README rows and commit tools first.

Reproduction under prepared WSL: `python3 -m unittest
tools.tests.test_game_nearest_height_15104634_recovery -v`.
