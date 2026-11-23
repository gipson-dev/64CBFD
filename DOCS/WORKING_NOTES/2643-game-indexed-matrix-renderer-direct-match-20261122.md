# 2643 - Indexed-matrix renderer direct match and retail mode-zero carry

Date: 2026-11-22. The total 85% matching goal remains active.

`func_15168C4C` in `conker/src/game_1944C0.c` replaces its false zero-return
placeholder with the complete indexed-matrix debris renderer. All **122 words
and named relocations emit directly from C**, in the original **104-byte frame**,
with **zero guards, insertions or omissions**. The existing guard CSV remains
byte-identical. All 41 neighboring functions, pools and diagnostic sets stay fixed.

Original: `conker/asm/nonmatchings/game_1944C0/func_15168C4C.s`.
VA `15168C4C..15168E34`; ROM `1960FC..1962E4`; 488 bytes. Actual descriptor draw
registration: column 16, ROM `2302B0`, VA `8008B7F0`. No direct JAL targets it.

Production: **4,625 / 5,528 (83.66%) total**, **3,952 / 4,855 (81.40%) Game**,
zero address drift, **903 different**, **74 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Converted-function/byte rows stay unchanged.

## Complete source and measured layout

The ABI is `Gfx *(Gfx *output, void *record, s16 view)`. View is saved by the
original code but unused. The local 240-byte `IndexedMatrixRenderState` has
two 64-byte SDK matrices at 10, translation at 90, angles at 9C, scale at C0,
display-list pointer at D0, alpha at E5, tile offset at E6, mode selector at EC
and combiner selector at ED; offsets hexadecimal. Unread regions remain opaque.
The previous handoff's translation/angle labels were reversed: the complete
54-word `func_15043D90` helper and producer layout establish this correction.

The renderer passes all nine float arguments by their original o32 positions
to that helper, using the matrix indexed by live `D_800BE9C0`. It emits the
SDK pipe sync, black primitive color with the record's alpha, cache updates,
black environment color and tile-size command. It retains two alpha loads
and the original repeated signed-halfword cache reloads. Render modes use
`0x8ACA0` high bits and one of two low words. The actual 34-word mode helper
`func_15142FBC` executes in the guest; its actual semantic C executes natively.

Combiner selector 1 emits TEXEL0*SHADE RGB with PRIMITIVE*SHADE alpha in both
cycles using the SDK LERP macro. The renderer reloads the current buffer index
for its final matrix command, submits the record's display list and returns
the advanced cursor. Matrix-provider mutations test those live reloads and
the copied field reads. The matrix provider models argument/state transport,
not rotation arithmetic or FCSR behavior.

The first if/else candidate was 120 words in frame 104. A natural switch on
the mode selector restores all 122 original instructions without normalization.
Naming/comment clarification changes none of the 42 raw owner functions, pools
or diagnostics relative to that selected direct match. One duplicated adjacent
comment on the preceding parent is removed in this same owner; it has no code
or data effect. No shared headers or build profiles change.

## Mode zero is real and retains private stack contents

The three direct constructor callers, `func_15170B90`, `func_15170F4C` and
`func_15171200`, contain 205, 158 and 256 words. Their complete current slots
equal ROM. Their packet `control5C` stores are respectively **0, 2 and 1**.
SDK32 assertions connect all eight used producer fields to the new record
view after the constructor's 96-byte copy to record+0x90. The producer's separate
packet `mode` byte at 0x54 is an update selector, not this renderer's EC selector.

Only render modes 1/2 assign the local mode word at SP+60. Retail mode 0 and
other values read the preexisting word. This is retained explicitly in source,
including its uninitialized-C limitation; no zero/default value is invented.
The complete original/current 348-word parent and actual 47-word range helper
execute the real column 16 registration. **24 mode 2->0 sequences** establish
that the first draw leaves `0x504A50` in the reused private home and the next
draw reads it. A compiled source control adding a zero default produces a
real public command/helper-argument mismatch. This is behavioral evidence,
not just an instruction-count rejection.

The direct IDO build matches retail's machine behavior on those paths.
**Portable native C equivalence for mode 0/other uninitialized paths is not
claimed.** Native acceptance covers the defined post-provider modes 1/2.
Mode0/other modes remain explicit guest/private-home checks. A future host
port must choose its own defined handling deliberately; this decomp does not
change the original behavior to make such a choice.

## Fresh focused qualification

- Raw, padded and original renderer streams each pass **864 cases**, plus
  **32 seeded private-residue cases**. Every renderer word executes. Cases
  cover both buffers, byte endpoints, mode/combiner branches, cache hits and
  misses, signed-view/stack phases and post-helper live changes.
- Actual SDK32 native O0/O2/O3 each pass **864 defined-mode cases** under
  strict aliasing and UBSan. All used offsets, the 240-byte record, matrix
  stride and eight producer-to-record mappings are asserted. Checks compare
  all numeric and opaque record bytes, all 512 command bytes including untouched
  words, caches, ordered helper arguments, cursor and record/output/cache
  canaries. Numeric fields are serialized separately from opaque host bytes.
  Eighteen deliberate source controls all fail through comparison, including
  argument ordering, cached state, tile bounds, mode words, combiner, display
  list and a stale final buffer index. The narrow GCC warning suppression
  reflects the retained uninitialized path; tests invoke only defined modes.
- The complete **26-word constructor**, **28-word allocator wrapper** and
  **20-word list inserter** pass **192 cases** with bounded malloc and bcopy
  providers. Null assets, allocation failure, byte narrowing, both rows,
  existing heads and live packet mutations are covered. All 96 copied bytes,
  opaque contents and untouched allocation regions compare. **48 constructed
  records** then run through both complete renderer streams and actual mode
  helper. Allocator and bcopy internals are not claimed executed.
- The complete parent/range/renderer/mode-helper connection passes **336
  cases per stream**, with **480 leaf invocations each**. An independent leaf
  reference checks full public state, argument log and cursor at every actual
  return to the parent. Cases use the real column 16, rows0/1, empty/multiple
  nodes, three parent rollback modes and the private-word carry sequences.
  The actual descriptor has no before hook and retains its original after-list.
  Unused parent callback paths are covered by the unchanged prior parent
  qualification; they are not called fresh coverage here.
- Both padders emit the direct 122-word target unchanged. **12 GNU links**
  cover four HI16 carry boundaries. **96 guest rebase runs** independently
  move the buffer/cache globals while preserving their field offsets; the
  actual mode helper is rebound too. Four deliberately wrong word/binding
  outputs fail full comparison. No new guard rows are added.
- **337 raw/padded/retail full access-prefix triples** compare memory,
  GPR/FPR, HI/LO, traces and calls, including mode 0/nonzero residue. No
  asynchronous/provider-internal/FCSR/hardware or gameplay acceptance is inferred.
- The complete real Make recipe reproduces the full padded owner in three
  commands. All 41 neighbors, including the just-restored parent and compact
  sprite renderer, remain fixed. Five gates run fresh in each tools setup;
  each installed run freshly recompiles/replays Make/links the complete image
  and explicitly reuses four semantic gates only after exact source, binding,
  import, manifest, artifact and native-binary fingerprints agree. `make
  tools-check` passes. The real sibling's dirty state, HEAD and 353 dependency
  hashes are preserved through a disposable overlay.

## Production image and review

The entire production ELF equals an independent prediction: **382 changed
bytes, zero exclusions and zero metadata permutations**. Only the 488-byte
target slot and its symbol size 12->488 change. The independent reference
compiles the frozen OLD owner with OLD guards, requires its entire object to
equal the baseline, and replaces only this slot with independently assembled
original code. The new C is not used to construct that reference. Complete
symbol definitions, strings and geometry are checked; no actual-C diff
windows or arbitrary metadata bytes enter the prediction.

All **189,088 protected Game data bytes across 720 owners**, other loaded
bytes, function addresses/extents, conversion rows, the entire guard CSV,
headers, profiles and private inputs stay fixed. Production Make and the
live recount supply the totals above. Existing duplicate generated_12D630
recipe and legacy owner diagnostic warnings remain; this is not a warning-free
build claim. The changed owner's diagnostic set equals its frozen predecessor.

Raw target SHA256:
`2d715980f037f3aa951d267bc983e1a6fc4318a5a6836d10aa2f4bc699e47953`.
Qualified owner SHA256:
`9175dc49f783db602570293af2d6015431bee69b45f55330671676684b65d5ed`.
Production ELF SHA256:
`b5a050548b5e10f903f01558f1f60c93434b969050f66cfe3989687f2aab8578`.

```sh
python3 -m unittest tools.tests.test_game_indexed_matrix_renderer_15168c4c_match -v
```

Artifacts: `conker/build/game-indexed-matrix-renderer-15168c4c-private/`.
Frozen-input checks fail closed. Codex owns implementation/validation;
Claude calls: 0/0. No account/provider changes, push, host import or Release
changes. The available sibling binary-based configuration does not consume
this decomp C directly. Continue remaining Game functions toward 85%.

Graph maintenance: the native update exited 1 with all
71,729 prior IDs retained. The subsequent serial scoped extraction
covers 9 C/Python files with no missing AST sources, producing
71,811 nodes / 174,762 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
