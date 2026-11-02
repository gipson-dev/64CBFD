# 1998 - Effect-overlap scanner recovered as guarded C

Verified 2026-11-02. Production **4,065/5,511 (73.76%)**; Game
**3,392/4,838 (70.11%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,446 different; one newly converted and byte-exact function. The active
80% target is **4,409/5,511**, requiring **344 more**. This is progress toward
that goal, not completion.

## Interface and recovered behavior

`s32 func_151555AC(f32 *center, f32 *extent, s32 *tags, s32 tagCount)`
replaces the assembly placeholder in `conker/src/game/generated_17CAF0.c`.
Original `17CAF0.s`: VA151555AC..1515572C, ROM182A5C, 384 bytes, 96 words
and a 72-byte frame.

The routine snapshots the two selected list-column indices from `D_800A6030`
and scans both columns in each of the two 0x1A0-byte rows rooted at
`D_800DCE50`. Each linked node preserves its next pointer before processing.
For positive `tagCount`, the requested tag array is searched backward; a tag
match then tests the node's X/Y center against the requested rectangle after
adding both X/Y extents. Every comparison is inclusive. The first overlap
returns one; exhausted lists, an empty tag list or no overlap return zero.

The retail census finds one aligned JAL at ROM `0x182974`, no literal function
pointer and exactly one source call from `func_1515548C`. That caller passes
the descriptor's first two floats, its copied position pair, the tag array and
the signed count through the ordinary four-register O32 ABI. Complete parent
gameplay execution is not claimed.

## Guarded compiler match

The semantic C has the exact 96-word length and 72-byte frame. Eighty-one
relocation-aware expected-word guards normalize independent compiler register
allocation, FP operand roles and instruction scheduling; no word is inserted
or omitted. The raw object and retail body each contain six bindings to the
same three globals:

- `D_800A6030` supplies the two selected list columns;
- `D_800DCE50` anchors the two-row list table;
- `D_800DD190` is the exclusive end marker after the second row.

All six raw relocation rows and all six retail relocation rows are checked.
Raw unresolved payload SHA256:
`622b82f3ea6c9912453a5986fcef3597b78d08107cf9f7ce24c88cab3769cf4b`.
Retail unresolved payload SHA256:
`6c4c31148b9ec2611d3f735c3731f0ee8ce044cb8620ce572f8542d9e432b04f`.

## Fresh qualification

- Guest execution runs 323 independent fixtures against both the raw compiler
  body and the guarded retail body. At least 94 of 96 words execute while
  preserving all callee-saved registers and producing the same public memory
  and result as an independent model.
- The fixtures cover both rows, both selected columns, null and multi-node
  chains, forward traversal with a saved next pointer, backward tag scans,
  zero/negative/positive counts, misses, early and late matches, and every
  inclusive X/Y boundary plus just-outside cases.
- Native 32-bit O0/O2/O3 runs cover all four list slots, both nodes per slot,
  all four tag positions and 25 boundary modes. Six source mutations are
  effective negative controls under every optimization profile.
- The permanent caller check proves the sole retail JAL, absence of a literal
  pointer and the single four-argument C call. The function itself is a leaf.
- Guard-staleness controls reject mutations at the entry, each relocation
  schedule and the final epilogue. All 40 neighboring owner functions remain
  identical; the owner contains 41 functions in total.

The five permanent tests pass before and after installation. The bounded
Graphify refresh is structural AST only, retains every prior node and every
prior valid edge occurrence, and uses zero LLM tokens. It is not a full-corpus
extraction or global reclustering.

## Owner, image and production result

The real generated-owner recipe and padder produce the independently frozen
object exactly. Protected Game data remains exactly 189,088 bytes across 720
owners with zero different bytes. The strict complete-image predictor has no
exclusions, and the installed production rebuild reproduces its frozen owner,
ELF and map identities:

- owner object SHA256:
  `486b0599b1480bcbe15d9fa114c62a563916857a4660d1bf07d53d9dff2b8a80`;
- linked ELF SHA256:
  `752feb861f0a37a4ce3ee397f1a52952a048048aff9c3521ad2b3ff3d9b122da`;
- linker-map SHA256:
  `ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The repository's final retail-ROM checksum still fails because 1,446 converted
functions remain non-exact; the owner, ELF and map identities prove that this
recovery itself introduces no image drift. The canonical regenerated progress
catalog marks `func_151555AC` as C, and the independent matcher credits it.

The qualification tools were committed first at `f55bcb3`. The retained stage
is `conker/build/game-effect-overlap-scanner-151555AC-match/`; it contains the
source, guest, native, caller, guard, owner and complete-image receipts. The
root README changes only aggregate rows. No Claude call or gameplay claim was
needed.

## Next step

Continue the ordinary Game queue from the fresh non-exact ranking. Keep the
handwritten custom-ABI `func_150A76F0` in its separate assembly workstream and
keep any new candidate private until the same ABI, runtime, owner, actual-Make,
whole-image, recount, documentation and graph-retention gates pass.
