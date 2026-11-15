# Game configurable particle original roles and checked normalization

Date: 2026-11-14. **Private qualification milestone only. No production
installation, guard rows or matching credit.** `func_15175390` now retains
its original saved-register roles and private stack homes. A checked,
source-derived normalization produces all **370 retail words**. The raw
C object still differs in **219 words**, versus the earlier candidate's
201; its recovered lifetimes/homes are stronger evidence than that smaller
literal difference count. Production remains the placeholder, and the
owner remains **2 / 9 C-exact**.

VA **0x15175390..0x15175958**, ROM **0x1A2840..0x1A2E08**.
Both raw and normalized streams have **370 words / 1,480 bytes**, with the
original **0xB8-byte frame**. The refined proposal and static normalizer are
in `tools/experiments/game_configurable_particle_15175390_normalization.py`.
Raw SHA-256: `8055bc014c509dfc595ad13ad0ac1045b6136aa2e094a2d3e3decb6b427f8aec`.
[Note 2443](2443-game-configurable-particle-recovery-and-frame-fit-20261114.md)
retains the earlier reconstruction, its semantic model and its fitting
limitations as historical evidence; its selected source is not overwritten.

## Recovered source shape

An explicit negative-first if/else for the second signed remainder allows
S1 to hold the divisor until its last use and then the world Z coordinate.
Keep the first remainder's default-plus/negative-correction shape: changing
both expressions makes IDO cache incoming Y in FP and spill the ground bit.
Capture tilt before ground flags after allocation and retain the measured
local declaration order. These changes recover:

| Role | Register / private home |
| --- | --- |
| Allocated particle | S0 |
| Signed divisor, then Z | S1 |
| Variant | S2 |
| X / Y | S3 / S4 |
| Captured inner radius | S5 |
| Loop counter | S6 |
| Captured tilt / ground bit | S7 / FP |
| Relative vector | SP+0x88 / +0x8C / +0x90 |
| Surface output | SP+0x80 |
| Cached heading | SP+0x9C |
| Transient heading across tilt RNG | SP+0xA0 |
| Cached toward-view flag | SP+0x78 |

Incoming Y retains its original SP+0xC4 home. The proposed owner corrects
the PRNG return declaration from unsigned to signed, consistent with the
primary PRNG interface. Full recompilation preserves all **eight other
function bodies and named bindings**, including the two existing matches;
normalized owner data/rodata pools remain absent. No source/global/header
change has been installed.

## Derivation and local proof

The normalizer accepts only the pinned raw body and all **27 named
bindings**. It applies a complete 370-slot permutation, expected old/new
caller-temporary register fields and explicitly declared CFG lowerings.
It never reads retail bytes while transforming the object and contains no
replacement copy of the retail function. All **397 altered-word/binding
controls** are rejected.

The operation inventory is closed after accounting for four redundant
source operations: the second remainder's V1-to-A0 copy, a mutually
exclusive extra state-home load, a duplicate ordinary surface-local load,
and a duplicate material shift. Retail instead has three unconditional
branch edges and one NOP. The output preserves every slot, constant,
saved/FPR register field and named binding; **168 word slots** move,
**76 words** change caller-temporary fields, and two BEQL forms become BEQ.
Three explicit edge redirects preserve the affected joins. This is more
than independent scheduling and is not described as direct C matching.

`game_configurable_particle_15175390_normalization_proof.py` checks the
complete inventory and the specific lowerings:

- The remainder copy has one consumed use before A0 is redefined; V1 is
  unchanged, and the destination consumes V1 directly.
- Two symbolic surface paths compare ordered memory effects, final memory
  and live saved registers. Only the consecutive ordinary surface-local
  read pair is coalesced. The material phi, common shift, delay slot and
  kind-table result agree; a wrong kind offset fails effectively.
- **54 actual query branch/delay executions** cover zero/nonzero state,
  captured ground, positive/negative/zero remainders and arbitrary provider
  changes to the later state home. The post-provider reload remains
  independent; it is not folded into the earlier state read. An incorrect
  query register is rejected.

These local proofs and finite behavioral cases do not establish raw
instruction-fault order or portable C semantics for an uninitialized
surface local. The scheduled earlier Y/state loads retain that limitation.
No production guard proposal is installed at this stage.

## Fresh qualification

The mounted suite and an isolated replay using sibling dependencies pass:

- **1,152 cases** across retail, raw C and normalized streams compare the
  independent model's public memory and helper packets, including aliases,
  provider mutations, allocation failure, type/model modes and stack phase.
- **63 directed cases** cover heading wrap and scale boundaries.
- **Eight emitted guest boundaries** compare three break-7, two break-6
  and three invalid-conversion cases. This is public-prefix/boundary
  evidence, not complete private-register or hardware exception parity.
- **24 retained-surface cases** execute retail and normalized streams only.
  A query that leaves SP+0x80 unwritten has no portable raw-C claim.
- Three effective recompiled source controls reject unsigned remainder,
  the reversed query gate and incorrect first-record sound behavior.
- The corpus visits **366 / 370 retail words**; unvisited offsets remain
  `0x140`, `0x200`, `0x3A8`, `0x578`. Literal normalization still compares
  all 370 words. Unsupported instructions do not count as source controls.
- Shared `make tools-check` passes.

Reproduce from the consumer root in the prepared PSBBN/IDO environment:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_configurable_particle_15175390_normalization -v
make tools-check
```

The isolated overlay copies eight task files with byte-identical contents;
it uses sibling dependencies with mounted fallback for missing modules.
It is not a claim that the dirty sibling checkout alone contains the new
suite. Sibling HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with all **2,439**
dirty paths preserved; before/after status SHA-256 remains
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`. Routine work uses zero Claude calls.

## Production boundary and next gate

All **805 frozen production inputs** remain unchanged: **698 objects**,
**82 headers**, the owner/caller sources, guard history, conversion rows,
retail inputs and linked ELF. ELF SHA-256:
`f3bedd6992fd8680e7436464997937845a18b6786ba192fad13892a342545fc6`.
No production rebuild or new recount is claimed here; the unchanged
production checkpoint remains total **4,487 / 5,515 (81.36%)**, Game
**3,814 / 4,842 (78.77%)**, zero drift, **1,028** different C functions.
**201 more C matches** reach 85% at this denominator.

The next gate is the native32 ABI/record suite, then execution through the
five real caller windows, both object padders with independent rebases,
and independent actual-Make/full-image prediction. Only after those gates
may the body and guards be considered for production installation, linked
audit, fresh recount and matching credit. Retain the current raw SHA and
full named bindings; do not advance production pins speculatively.

Scoped Graphify AST refresh covers the four new tools files and retains
all **60,703** existing IDs: **60,722 nodes /
114,260 links**, zero lost nodes. This is not full-corpus extraction.
Tools commit `f65b6f0c8fe80983d69583e9147f53c62cb22805` banks the qualification before this consumer handoff.
Root README aggregate rows remain accurate and unchanged. Keep the 85%
goal active; no push. No host sources are available under `64CBFDOGL`
here, so no host adoption/runtime acceptance is claimed; Release stays frozen.
