# Game Record Neighbor Visitor Byte Match

Date: 2026-10-06. Starting checkpoint: `360abd58`.

Replace `func_1508B2A8`'s false zero-return placeholder in
[generated_B3020.c](../../conker/src/game/generated_B3020.c) with the complete
recursive record-neighbor visitor. Its **84 words / 336 bytes** occupy
0x1508B2A8..0x1508B3F8, ROM 0xB8758..0xB88A8. Semantic C emits all 84 words;
six expected-word guards normalize two complete temporary-register lifetimes.
The linked slot is byte-exact. No insertion/omission, overflow, assembly edit
or new compiler override.

## Recovered Contract

The first argument is an unsigned-byte node ID; the second is a query pointer.
The private named-tag query type has the following recovered layout:

| Offset | Field | Size |
| --- | --- | --- |
| +0x00 | X | float |
| +0x04 | Z | float |
| +0x08 | Squared-distance threshold | float |
| +0x0C | Distances | 8 floats |
| +0x2C | Count | signed halfword |
| +0x2E | IDs | 8 bytes |
| +0x36 | Visited flags | 32 bytes |

Used fields end at +0x55; the ordinary aligned structure size is **88 bytes**,
including two trailing padding bytes. [functions.h](../../conker/include/functions.h)
declares the matching opaque named tag and `void` prototype. No shared data
layout or unrelated prototype is changed.

- Mark the entry ID before loading global D_800D2350 or node/query coordinates.
  The bank is `id >> 3`, but the bit is `1 << (id & 3)`, not `id & 7`.
  IDs differing by four in the same bank therefore collide; preserve retail.
- Nodes have stride 16. Signed halfword X at +0 and Z at +4 form the squared
  distance using float32 operations. Y at +2 is not used.
- Strict `query->threshold < distance` selects the append path. Equality and
  unordered comparisons instead select neighbor traversal.
- Append only when the signed count is less than eight. Retail has no lower
  bound. Write the ID byte, reread count for the distance store, then reread
  count for its increment. Negative-count ID writes can alias the count bytes;
  caching the original count changes the guest contract.
- Otherwise visit exactly five neighbor bytes at +9..+0xD, depth first. Skip
  neighbor 255 and already-marked bits. Entry ID 255 is a valid table index;
  255 is a sentinel only in the neighbor list.
- Retain the parent's table/walk pointer across recursion. Each child loads
  the global anew after its own visited write. Recursive calls execute the
  connected instruction body, not an opaque helper mock.

The frame is **0x30**, saving S2/S4/S3/S1/S0 at +0x20/+0x28/+0x24/+0x1C/+0x18
and RA at +0x2C. Argument narrowing/home, floating-operation order, branch
delays, walk/counter lifetimes and restoration match retail. No defined return
value is claimed.

## Compiler And Guard Audit

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_neighbor_visit_candidates.py)
freezes the raw byte-query baseline independently. **24 unique controls**
complete with empty compiler diagnostics.

| Control | Words | Raw Differences |
| --- | --- | --- |
| Raw byte-query / one walker | 82 | 57 |
| Separate parent and walking pointers | 83 | 29 |
| Reuse Z as squared distance | 83 | 26 |
| Late narrowed neighbor index | 84 | 7 |
| Typed query plus late index (installed) | 84 | 6 |
| Opaque query argument plus typed local | 84 | 28 |

Separate cursors recover the parent/walk lifetime; reusing Z recovers the
retail floating temporary. `(u8)(id / 1)` retains the separate narrowed bitmap
index and emits no divide. The typed query also recovers both address operand
orders. Compiler phase-order explanations are inference from emitted output,
not instrumented pass traces. The existing no-unroll slice profile stays
unchanged; isolated default O2/g3 emits the same 84-word, six-difference body.

The six CSV guards are exactly two V0-to-V1 renames:

| Offset | Expected | Replacement | Lifetime |
| --- | --- | --- | --- |
| +0x030 | 024F1021 | 024F1821 | Bitmap pointer definition |
| +0x034 | 90580036 | 90780036 | Bitmap byte load |
| +0x048 | A04A0036 | A06A0036 | Bitmap byte store |
| +0x0F8 | 308200FF | 308300FF | Masked neighbor definition |
| +0x0FC | 000258C3 | 000358C3 | Neighbor bank use |
| +0x108 | 304E0003 | 306E0003 | Neighbor bit use |

These cover every use of the respective temporary in +0x30..+0x48 and
+0xF8..+0x108. **78 words emit unchanged directly**. No relocation, branch,
frame, floating instruction/order or save/restore is patched. Actual emitter
tests reject a stale expected word or unexpected relocation at every offset;
omitting any one guard has a behavioral counterexample.

## Qualification

[Matching tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_neighbor_visit_match.py)
pass **13 tests in 57.942 seconds**, no skips, against the final linked build.

- **4096 three-way leaf cases** compare retail, raw selected C and guarded C,
  including all 256 entry bytes, high argument bits, two stack phases,
  finite/strict-equality/NaN/infinity/signed-zero coordinate profiles and
  signed count boundaries.
- **4608 three-way recursive graph cases** cover cycles, bit collisions,
  sentinel/visited suppression, output capacities and all **84/84 words**.
- An independent float32, depth-first reference verifies ordered writes/calls
  and complete non-stack memory. Three-way comparisons additionally verify
  ordered reads, all memory and recursive calls.
- **120 append count-boundary cases**, **20 count-byte alias cases**, one
  explicit collision graph and **two physical visited/global alias cases**
  bind fresh count/global reads and retained parent pointers. ID 255 correctly
  leaves the negative count unchanged in the alias fixtures.
- **2304 source-extracted 32-bit native graph footprints** verify the entire
  88-byte query, eight outside sentinel bytes, unchanged global and all 4096
  node bytes, including unused padding. Native fixtures use ordinary counts
  0/7/8; negative-count physical aliases are guest-only, not a claim of
  cross-endian native portability.
- Six compiled semantic negative controls reject wrong mask, missing mark,
  wrong coordinate plane, cached count, inclusive threshold and an inverted
  ordered predicate that mishandles NaN.
- Production body/query/prototype identity, compiler inventory/anchors,
  unchanged next symbol, final linked slot and actual fail-closed guards are
  asserted. No shared oracle implementation is changed this turn.

Record dispatch matching/native, position/radius append, optional-size loader
and actor context dispatch modules pass **49 focused regression tests in
103.543 seconds**, no skips. The historical full corpus is not rerun wholesale.

These are bounded instruction/native fixtures, not full parent-caller,
FCSR/exception, strict-C physical-alias/concurrency or hardware/gameplay
qualification. Parent `func_1508B3F8` remains a placeholder.

## Linked Image Audit

Fresh DECOMP ELF/progress/match-progress targets succeed. The broad header/CSV
rebuild emits existing unrelated warnings; it is not a warning-free build.
Comparing against the prior checkpoint's **6059 slots** finds identical symbol
names, addresses and lengths, with **only func_1508B2A8 changed**. No overflow
movement or trampoline retargeting occurs in this turn.

Target SHA-256:
`32ce3898fe6eede60deaa4147b5140cda8bc47c2ba0d213a0b220ac3e95aff23`.
Ignored before/after/audit receipts are under
`conker/build/game-record-neighbor-visit-test/`; the 24-control inventory is
`conker/build/game-record-neighbor-visit/screen.json`.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes** and Game data **189088 bytes / 720 owners** remain retail-exact.
All **10637 older CSV rows** remain unchanged; exactly six target rows bring
the table to **10643**. No padding/emitter guard or data-ownership rule is relaxed.

Fresh exact totals: **3308/5462 (60.56%)**, Game **2635/4789 (55.02%)**, Init
**492/492**, Debugger **181/181**, zero retail address drift and **2154 different
Game C**. Conversion counts and retained Init assembly inventory are unchanged.
README updates only its snapshot date and aggregate tables.

`make tools-check`, whitespace and **3014 relative links** across nine
current/working documents pass; zero broken links.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_record_neighbor_visit_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_record_neighbor_visit_match -q -f
wsl python3 -m unittest tools.tests.test_game_record_dispatch_match tools.tests.test_game_record_dispatch tools.tests.test_game_position_radius_append_match tools.tests.test_game_optional_size_loader_match tools.tests.test_game_actor_context_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next inspect parent `func_1508B3F8` and its query construction/call contract
before choosing its recovery scope. The triangle read/frame boundary in
[Note 1017](1017-game-actor-triangle-cached-iterator-audit-20261005.md),
func_150E6FAC's duplicated RA load and handwritten func_150A76F0's separate
register-contract lane remain open. Note 1020's proposed 1508B2A8 recovery
is now complete.

No sibling source/build/save/frozen Release change, host transplant or push.
The full Game matching goal remains active.
