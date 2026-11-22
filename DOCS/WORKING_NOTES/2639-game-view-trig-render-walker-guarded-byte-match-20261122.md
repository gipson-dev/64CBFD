# 2639 - View trig cache and render callback walker

Date: 2026-11-22. The full 85% matching goal remains active.

`func_15167310` in `conker/src/game_1944C0.c` now contains complete semantic C
for the live-view sin/cos cache and both render callback rows. Its **124 raw C
words** normalize to all **122 retail words and named relocations**, in
**frame 104**, using **45 expected-word guards, three omissions and one
insertion**. This is a guarded match; raw C is not byte-exact.

Original: `conker/asm/nonmatchings/game_1944C0/func_15167310.s`.
VA `15167310..151674F8`; ROM `1947C0..1949A8`; 488 bytes.

Production: **4,621 / 5,528 (83.59%) total**, **3,948 / 4,855 (81.32%) Game**,
zero address drift, **907 different**, **78 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Conversion rows remain unchanged.

## Semantic body and recovered SDK interface

The first gate uses signed interpretation of the wrapped 32-bit expression
`(u32)D_80082FA0 + 1`. This preserves the original INT_MAX boundary without
signed C overflow. Each view reloads the live `D_800DBFF0` base and reads
`struct108.unk3A0`, with the measured `0x9A0` view stride. The angle is captured
in F20 and supplied unchanged to both sinf and cosf, despite volatile helper
clobbers or changes to the view data. The view limit is reread after the
helpers. An additional view-0 sin/cos pair always runs, including when the
initial view gate is false. Its two outputs are locally declared as
`extern f32 D_800DD1D0[2]`.

The second phase visits 104 columns, with both rows inside each column.
Rows are `0x1A0` bytes apart. A null head skips the callback lookup; a null
callback skips the entire depth change. For a live list, the signed depth byte
is incremented, next is snapshotted from node+8, the callback runs, and both
depth and the saved continuation are reread. The callback itself is reloaded
for each node. After the list the live depth is decremented. Callback changes
to next, depth, future heads or the descriptor must remain visible in this
specific order.

`struct115.unkC` is recovered as `void (*)(struct102 *)` at offset 12. The
old 16-byte opaque region becomes four bytes, this callback, then eight bytes.
The descriptor stays 52 bytes, with every existing member offset unchanged.
The target and its sole direct caller's declaration in `game_45B80.c` become
`void func_15167310(void)`. Existing numeric function/field names are retained;
comments describe measured roles without inventing original type names.

## Frame and normalization limits

The source keeps the column offset in a measured stack view at SP+0x4C with
16 trailing bytes explicitly named `unidentified04`. Those bytes have **no
recovered semantic purpose**. This is frame scaffolding, not a claim about the
original local type. It preserves frame 104, F20/F21 at SP+0x18, saved GPR/RA
homes at SP+0x20..0x44, and their complete lifetimes.

The normalization is derived from compiler words, not copied from retail.
It renames closed temporary-register roles, moves independent address setup,
and schedules the cosine store after its pointer increment with offset -4.
The latter preserves the address modulo 32 bits. A cached descriptor base
replaces repeated per-head materializations. The raw null-callback BEQL
increments the row in its delay and skips the common increment; retail's BEQ
has a NOP delay and reaches the common increment. Decoded two-path checks
show exactly one row increment for all head/callback gate combinations.

The canonical C compares against the actual `D_800DCE50` array end. Retail
instead materializes `D_800DD190`; the fold is valid only with the verified
linked relation `D_800DD190 == D_800DCE50 + 0x340`. One end-address LUI is
inserted and three redundant compiler words omitted. The guard CSV retains
the complete prior byte prefix, and every expected word/relocation fails
closed. The original routine remains independently GNU-assembled truth.

## Qualification and production audit

- The include closure and actual Make database identify **305 header
  consumers** among 698 active C owners. Every affected recipe was replayed
  privately, then every production object compared to its qualified result.
  Loaded code/data, all function words and named bindings stay fixed except
  the intended target. There are no changed auxiliary named symbols. Seven
  private/production objects differ only in non-loaded `.mdebug`; their
  compiler command, source/header path and timestamp strings are recorded
  explicitly. The installed phase checks each complete production object's
  exact hash as well as its sections/bindings. These are reconciled debug
  differences, not excluded linked-image ranges. The
  missing literal `PR/sptaskoff.h` belongs to an inactive assembly-only branch;
  all C recipes explicitly select `_LANGUAGE_C`.
- SDK32 descriptor/view layout checks pass at O0/O2/O3. The target complete
  owner preserves all **41 neighbors**, pools and diagnostics. Its real
  three-command Make recipe exactly reproduces the qualified owner.
- Raw, padded and retail guest streams each pass **1,376 cases**, exercise
  every instruction, and pass **36 independent rebase runs**. Tests cover
  wrapped count boundaries, skipped/zero/four-view paths, signed depth bytes,
  null heads/callbacks, dense and sparse lists, row/column order, non-finite
  angle bits, live base/count changes, and callback-controlled continuation.
  Trig/callback internals are bounded contracts, not full libultra/gameplay
  execution. Extended depth fixtures explicitly map backing bytes.
- Native SDK32 O0/O2/O3 each pass **227 cases** with strict aliasing, UBSan,
  actual struct102/108/115 records, record canaries, unchanged record fields,
  all cache/head/descriptor/continuation outputs and ordered helper traces.
  Native depth stays within six slots and view count within four; the existing
  SDK byte-table view is retained for pointer heads.
- **13 effective source controls** reject count off-by-one, wrong angle
  field, reloaded angles, missing final outputs, wrong sin/cos destination,
  missing last column/second row, wrong descriptor, depth changes, late next
  capture, ignored continuation, and once-only callback capture.
- The actual two-word JAL/delay window at VA `15018930`, ROM `45DE0`, in
  `func_1501878C` executes the complete callee in **12 runs**. Baseline,
  private-image and production windows remain identical. This qualifies the
  direct call window and repaired void declaration; the enclosing renderer
  is not claimed as a complete connected-caller test. The prior aligned ROM
  census finds one direct JAL, no direct-J and no pointer literal.
- **1,714 access-prefix triples** pass across three discriminating cases.
  Padded/retail compare complete GPR/FPR, memory, trace, calls and HI/LO state.
  Raw C compares complete public/frame memory, FPR state and ordered access
  observations. Raw temporary/descriptor registers differ; raw full-GPR fault
  identity is not claimed. FCSR, timing, asynchronous writes and helper faults
  are outside this bounded model.
- Both production padders and **12 GNU links** across four HI16 carry cases
  match all 122 words/bindings. **Eight malformed guard controls** reject
  changed expected words/relocations, including omission/insertion sites.
- The **entire production ELF** equals an independent prediction with
  **442 changed bytes, zero exclusions**: the 488-byte target slot, symbol size
  12->488, and exactly two bounded symbol/string swaps:
  `D_800DD1D0`/`D_80096530` and `func_15002878`/`D_800E0DFC`. Preimages,
  contiguous strings and unchanged canonical named definitions are checked.
  All **189,088 protected Game data bytes / 720 owners** stay exact.
- Six gates run fresh in each tools configuration before installation.
  The production debug-metadata finding required tightening the phase gate;
  consequently all six installed gates also run fresh in each configuration.
  No semantic reuse is claimed for this function. Complete source, guard,
  bindings, artifact, native-binary, import and data fingerprints are retained.
  `make tools-check` passes. The real sibling's dirty state, HEAD and 353
  dependency hashes remain intact; paired tests use a disposable overlay.

Raw target SHA256:
`e25e472fbc23d897367f829f2ce120ae5a2aabd5b98fbe3bacf1ef623bab36a7`.
Qualified complete owner SHA256:
`0c9f10b055ec941d8698d062c1a9a346b2122f143aef90ef7a6ff1b0c1798651`.
Production ELF SHA256:
`f208907a9e34917842d66e6cc78606004b9755f60816bbc1013216f10f09682f`.

```sh
python3 -m unittest tools.tests.test_game_view_trig_render_walker_15167310_match -v
```

Artifacts: `conker/build/game-view-trig-render-walker-15167310-private/`.
The packet requires frozen inputs and fails closed on fingerprint changes.
Codex owns implementation/validation; Claude calls attempted/completed: 0/0.
The available sibling host configuration consumes binary words, not this C;
read-only applicability does not establish host parity. No host/Release changes,
push, hardware or gameplay acceptance. Continue remaining Game functions.

Graph maintenance: the native update exited 1 with all
71,363 prior IDs retained. The subsequent serial scoped extraction
covers 11 C/Python files with no missing AST sources, producing
71,430 nodes / 172,160 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
