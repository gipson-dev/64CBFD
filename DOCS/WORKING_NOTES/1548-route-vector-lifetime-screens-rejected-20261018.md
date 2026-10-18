# Route Vector Lifetime Screens Rejected

Date: 2026-10-18. Consumer predecessor **6aefaedb**; tools predecessor
**bcfe55a**, new tools checkpoint **3bd5e4e** banked first. Target
**func_15088F30**, owner `generated_B3020`, VA **0x15088F30..0x1508907C**,
ROM **0xB63E0..0xB652C**, retail **83 words /frame0x10**.
This is a rejected-fit checkpoint with **zero matching credit**, not an
installed recovery. The wider Game matching goal remains active.

## Fresh Checkpoint

[Note1545](1545-route-vector-semantic-model-and-stack-rejection-20261018.md)
qualifies the original semantic model and its private-stack rejection. Its
physical ELF/guard pins predate both now-matched spline helpers; do not weaken
those historical checks to run it against a different image.

New experiment `tools/experiments/game_route_vector_lifetime_fit.py` retains
the original thirteen-input closure, but establishes a separate checkpoint
using the exact post-Note1547 ELF and guards. Source B3020, retail assembly,
ROM, symbols, headers, profile and prepared compiler hashes remain the same.
The original model module and its fingerprints are unchanged. This closure
does not cover every unlisted dependency.

The recovered public contract is still Note1545's four output points, first
type4 neighbor, signed32 coordinate differences, FF fallback, captured table
per valid slot, fresh post-store Y/Z/speed reads and ordered guest aliases.
Retail saves only S1/SP+0xC and S0/SP+8, holding constant4 and the global
pointer address. The output cursors belong in caller registers. None of the
new forms recovers that private contract.

## Measured Screens

All sources compile as complete owners with the existing B3020 O2/g3,
compiler-only no-unroll profile, without diagnostics. No compiler install,
profile change, assembly substitution or production guard is introduced.

| Forms | Count | Words / Frame | Word Differences | Saved Homes |
| --- | --- | --- | --- | --- |
| Local-output baseline and all nonempty top-level pointer-const masks | 16 | 83 /16 | 78 | S2/+0xC, S1/+8, S0/+4 |
| Six local declaration-group orders | 6 | 83 /16 | 78 | S2/+0xC, S1/+8, S0/+4 |
| Same six orders with named table-address/count invariants | 6 | 82 /16 | 77 | S2/+0xC, S1/+8, S0/+4 |

The fifteen qualifier masks affect only pointer bindings, never pointed-to
objects. IDO CFE requires the caller declaration to carry the same explicit
top-level qualifiers as the definition; the experiment derives that local
declaration from the generated definition. An initial mismatched-prototype
compile was rejected, then corrected. No production interface was changed.

Declaration groups are outputs, byte pointers, integers and float temporaries;
only their order changes. Tests prove the executable source tails are fixed.
The named version additionally assigns the pure address and constant once,
without moving the valid-slot table load out of its loop. Within each family,
all declaration orders emit identical complete raw bytes and bindings.

| Raw Body | SHA-256 | Relative HI16 / LO16 Offsets |
| --- | --- | --- |
| Local / all const masks | 4f916fe4c212cefecfdfe585fd3448578d0cf62b80560f508e9b8b2650406919 | 16 /44 |
| Named invariants | 7b5905ce1dfdc0d4a531873a512cdbdcd73e76ae071311d27bff3d1027ff5470 | 60 /72 |

Both relocation pairs reference D_800D2350. Do not confuse the new local
83-word raw body with Note1545's different assigned-exit83-word model
(`83c683a0...`,76 differences). Named invariants do not solve the remaining
fit, and neither a shorter body nor equal frame size earns matching credit.

## Fresh Validation

```sh
python3 -m tools.experiments.game_route_vector_lifetime_fit --screen all
python3 -m unittest tools.tests.test_game_route_vector_lifetime_fit -v
```

The final six-test run passes in **95.436s**; the preceding six-test run
passed in56.714s. Each test setup recompiles and checks all28 forms, rather
than trusting earlier JSON receipts. Ignored artifacts are under
`conker/build/game-route-vector-lifetime-fit/`.

- All28 candidates preserve every raw word and relative binding in the other
  **72 owner functions**, including the complete live118-word parent, plus
  normalized literal pools. The candidate prototypes are not installed.
- **168 guest fixtures per distinct raw body**,336 paired candidate/retail
  cases, compare complete public memory and exact interleaved access traces.
  Cover signed-coordinate boundaries, FF combinations, neighbor selection,
  sixteen speed bit patterns, ten guest aliases and both stack phases.
  Saved integer/float ABI state is checked on each ordinary return. Two
  independently mutated LH-to-LHU bodies have effective public-result
  witnesses. This bounded screen is not a new native32 or full-fault suite.
- The necessary retail stack gate rejects both complete bodies. An actual
  first-private-store fault witnesses S2 at entry-SP-4 in each candidate,
  versus retail's S1. Private memory differs. No whole-private/fault-state,
  NaN-payload/FCSR, hardware or gameplay equivalence is claimed.
- All**165 raw instruction words**, four target bindings and**26 live or
  frozen input alterations** are individually rejected by strict guards.
  Unknown source interfaces and changed local prototypes are also rejected.
- Shared padder/PC16 tests pass **eleven per tools copy**; both tools smoke
  checks and consumer `make tools-check` pass. Four copied task files pass
  ASCII/AST checks; both corresponding pairs are byte-identical.

The new bodies fail the private gate before installation. No actual padded
candidate/rebase qualification, whole-link prediction or production rebuild
is claimed or needed for this rejected screen. Note1545's larger semantic,
native, fault, parent and rebase receipts remain historical evidence for its
different pinned model, not fresh qualification of these new raw bodies.
Claude calls: **zero** this checkpoint; no repeat of the prior advisory.

## Preserved Production

| Artifact | Unchanged SHA-256 |
| --- | --- |
| Whole ELF | fc9f2b74bd97121aa678270092047b76914852ea483a10c1bc35a32b504c021b |
| B3020 source | ce0cf9b5504e5b41b267c09d69c3bdc9ed2f24533ed7de0dd68935bd678f467f |
| Matched spline source | 8e9c9885e7772fbd356120a036307a2ba8202d04fc72de82a3027dba7f750dde |
| Guard manifest | 65de253d70fd8071c62dd8c1f87dbe89107c2713dbb3d30ae3a728d5b9a6447f |
| Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Last verified official totals remain **Game2,984/4,828 (61.81%)**,
**total3,657/5,501 (66.48%)**, Init492/492, Debugger181/181,
**1,844 different /zero drift**. No recount is inferred from the experiments;
conversion counts and root README remain untouched.

Standalone mirror HEAD **ddbdd16** is unchanged. Preserve all**1,222 prior
dirty-file hashes**, adding only the two absent task files for1,224. No mirror
commit/reset, push, host action or frozen Release action. The user confirmed
the old accidentally overwritten `.../.vscode/Conkers` file was disposable
scratch; no recovery is needed. IDO outputs remain relative paths without
spaces, passed as argument-array entries by the existing compiler wrapper.

## Resume Here

Continue the same vector's invariant/output-cursor lifetime and inner-loop
address-expression fit. The missing duplicate candidate shift and original
branch/delay layout remain required alongside the exact public read order.
The const-binding and six declaration-group orders are now measured dead
ends; do not rerun them or silently loosen the old model's pins. Use a new
strict checkpoint if a later production edit changes this physical baseline.

Before any installation, recover the two real saved invariant roles and
original private homes, then qualify the complete owner, parent interface,
actual padding and independent rebases. Any normalization needs its own
closed proof before immutable whole-link prediction and a linked audit.
Both spline helpers remain byte-exact; parent15087350 and wider queues stay
open. This checkpoint is progress in the audit, not a completed Game goal.

Scoped Graphify refresh: **42,554 nodes /82,626 links /4,205 communities**.
Preserve19,398 nodes from2,972 excluded-but-existing files. All42,542 other
old IDs remain; three line-disambiguated UPDATE_LOG heading IDs relocate by
the eleven added lines with their labels/files retained. This note contributes
seven nodes. Tools remain subject to the configured submodule exclusion;
this is not a fresh graph AST-coverage claim for the new experiment/tests.
The original graph and ID audit are ignored task artifacts, not committed
graph output or rewritten history.
