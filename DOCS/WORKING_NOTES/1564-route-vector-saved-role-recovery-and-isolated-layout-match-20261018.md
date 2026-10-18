# Route Vector Saved-Role Recovery And Isolated Layout Match

Date: 2026-10-18. Consumer predecessor: `2779401e`. Tools committed first as
`48c467e`. Continues [Note 1548](1548-route-vector-lifetime-screens-rejected-20261018.md)
without weakening its historical pins or replacing its rejected candidates.

## Result And Boundary

Target `func_15088F30`, owner `generated_B3020`, VA `15088F30..1508907C`,
ROM `B63E0..B652C`: **83 words, 332 bytes, frame 16**. Production still has
the original zero-return placeholder. This is an experimental normalized match,
not an installed recovery, direct compiler match, or new matching credit.

The complete semantic C now recovers the actual invariant roles and homes:
**S0 = &D_800D2350 at SP+8; S1 = 4 at SP+12**. Output cursors use caller
registers. The necessary retail stack gate passes. The prior extra sentinel
save is gone, and the duplicate candidate-index shift remains present.

The selected body emits 83 words with **56 raw word differences**. A closed,
file-free layout accounts for all of them and matches every independently
assembled retail word and both symbol bindings. It retains **83 distinct C
instruction origins**, with no insertion, omission, frame change, new load,
or new store. The only instruction-order change moves the independent low
address setup through the opening register moves, before any public access.

## Source And Layout

New experiments are `game_route_vector_saved_roles.py` and
`game_route_vector_layout.py`. The selected body keeps the existing byte-record
and three float-output interface, ordered signed-coordinate loads, captured
per-point table pointer, first type-four neighbor, FF fallback, and fresh
post-output Y/Z/speed reads from [Note 1545](1545-route-vector-semantic-model-and-stack-rejection-20261018.md).

Two source changes recover the necessary shape: compute the selected neighbor
through an equivalent halfword-pointer index, and assign the X product into
the captured speed temporary before the X addition. Z still freshly reloads
record speed; the X product must not become its input. This does not narrow
the signed coordinate difference or alter the public memory-access contract.

Thirty-eight complete-owner forms were measured: 18 pointer-expression forms,
12 conversion-lifetime forms and eight arithmetic-lifetime forms. All compile
without diagnostics and preserve the other 72 raw owner functions and literal
pools. Several recover two saves but remain 82 words; equal save count is not
treated as a match. The selected 83-word source is freshly compiled by tests.

The layout renames closed general-register roles and per-lifetime FP fields,
including the speed register's distinct product lifetime. It also commutes
six equality/address operations and two floating multiply/add operands.
Floating commutation is qualified under the finite/provider test model, not
as universal NaN-payload or FCSR/exception equivalence. Source and bindings
are checked before any transformation, and the complete normalized digest
is checked afterward:

| Artifact | SHA-256 |
| --- | --- |
| Raw C instruction body | `8824f4396809c366367e8bd116bd8426e5615a55ae3449643c83a7d0cdbe3710` |
| Normalized unlinked body | `02521a70c7569f4f8f3fc52db453699d6aba888811af5529a32cd687b4cebead` |

Both bindings name D_800D2350. HI16 remains at byte 12; LO16 moves from byte
40 to byte 20. No retail instruction-word table is used to generate output.

## Fresh Qualification

**Eight tests pass in 28.937 seconds, no skips:**

- All 83 normalized words and both bindings equal independently assembled
  retail. Normalization also succeeds with file reads disabled.
- **1,650 paired guest cases** compare complete public/private memory and
  interleaved access traces, including all 243 neighbor patterns, FF masks
  0/5/15, signed-coordinate boundaries, 16 speed bit patterns, ten guest
  aliases and both stack phases. All saved integer/FP ABI state is checked.
- **957 fired instruction-memory prefix cuts across 22 fixtures** preserve
  complete memory and completed access order, including the original two
  saved homes. A fired post-setup cut confirms both invariant register values.
  These are synthetic access boundaries, not hardware traps or a proof of
  scratch-register identity at every fault PC.
- **65,680 native32 cases per O0/O2 build**, both with UBSan, include all
  65,536 signed coordinates. Aligned host-endian pointer32 checks and full
  output/record/table comparisons pass. Three independently compiled semantic
  negatives exit ordinary wrong-result 23: unsigned coordinates, narrowed
  differences and stale/product speed. Native tests use `-fno-strict-aliasing`;
  incompatible halfword/float/pointer guest aliases remain guest-only.
- The actual private mixed-profile padder/assembler matches all 83 words.
  Primary and normal-profile compilations each preserve 72 neighbors; the
  existing projection override and every other padded owner byte, address,
  extent and literal pool remain fixed. The private 83-row manifest retains
  all **2,476,075 existing guard bytes** unchanged. No production rows are added.
- Six independent GNU links cover three code/global placements across HI16/
  LO16 carry boundaries; **198 paired guest executions** retain full memory
  and access equality, including rebased aliases and both stack phases.
- **85 raw-word/binding controls, 64 layout-recipe controls and 44 live/
  snapshot input corruptions** fail closed. The new 22-input checkpoint is
  separate from the unchanged original model and lifetime-screen checkpoints.

Initial harness failures were corrected: access-cut indices are zero-based,
the native command factory takes an optimization flag, and the raw emitter
needs the selected function's metadata, not the whole function dictionary.
None was counted as a semantic negative. The final eight-test run is fresh.

## Preserved Production And Repository

Production owner, guards, Makefile and ELF remain byte-for-byte at Note 1563:

| Artifact | Unchanged SHA-256 |
| --- | --- |
| Whole ELF | `15138e12aba5c25923d3438ff1db199d550accd18ad4596918a4b2ecd71ec8fd` |
| B3020 source | `a98ad9f3b781a4f93f39e45cbbe9646054c60c7b1d329bb5b2d21fb1499f7573` |
| Guard manifest | `d9a994d78370af27db71af35f5639096bb0afc56e63b197b7bc6b19bffb7f902` |

No production rebuild or recount is inferred. Last verified totals remain
**Game 2,989/4,828 (61.91%)**, **total 3,662/5,501 (66.57%)**, Init 492/492,
Debugger 181/181, **1,839 different and zero drift**. Root README is unchanged.

Three repository-setup tests and smoke checks pass in both tools copies;
consumer `make tools-check` passes. Copy only the three absent task files to
the standalone mirror, preserving all 1,265 prior dirty-file hashes and its
older `ddbdd16` HEAD. It now has 1,268 dirty leaf paths, without reset or mirror
commit. All three pairs are byte-identical, ASCII and AST-valid. Tools are
committed before the consumer pin; no push, Claude call, emulator/debugger
session, host-port action or frozen Release action.

## Resume This Function

```sh
python3 -m unittest tools.tests.test_game_route_vector_saved_roles -v
python3 -m tools.experiments.game_route_vector_saved_roles --qualify
```

Ignored artifacts under `conker/build/game-route-vector-saved-role-fit/`
retain the 38 source screens, raw/normalized receipts, native sources and
binaries, original assembly object, private guards/objects and rebase links.

Continue **this same function**, not another source batch. Audit all incoming
interfaces: B3020 retail assembly already shows four calls in the retained
func_15087350 and one in the live C func_15088D58. The typed local declaration
preserves every parent byte in the fresh owner comparison, but the complete
caller audit and connected-caller qualification are still separate gates.
Then qualify the actual expanded Make path, lock the first whole-ELF
prediction, install only this body/guards/interface, rebuild, audit all linked
code/addresses/protected data and recount. Broader C proof, strict hardware
FP/trap behavior, unknown indirect interfaces and gameplay remain explicit
limits. The wider Game matching goal stays active.
