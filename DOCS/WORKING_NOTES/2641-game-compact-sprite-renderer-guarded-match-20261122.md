# 2641 - Compact sprite renderer and direct caller ABI

Date: 2026-11-22. The total 85% matching goal remains active.

`func_15168118` in `conker/src/game_1944C0.c` replaces its false zero-return
placeholder with a complete compact sprite renderer. Its **341 raw C words**
normalize to all **337 retail words and named relocations**, in **frame 168**,
with **201 expected-word/binding guards**, **four omissions**, and **zero
insertions**. Raw C is not byte-exact. The omissions coalesce four proved
argument copies; every other instruction origin remains exactly once.

Original: `conker/asm/nonmatchings/game_1944C0/func_15168118.s`.
VA `15168118..1516865C`; ROM `1955C8..195B0C`; 1,348 bytes.

Production: **4,623 / 5,528 (83.63%) total**, **3,950 / 4,855 (81.36%) Game**,
zero address drift, **905 different**, **76 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Converted-function/byte rows stay unchanged.

## Recovered source and ABI

The ABI is `Gfx *(Gfx *output, void *record, s16 view)`. A measured local
76-byte `CompactSpriteState` view extends the preceding updater's view with
render settings/orientation, signed width/height, primitive RGBA and
environment RGB. Opaque regions retain unknown contents. No shared header
or build-profile changes are required.

The local 20-byte `CompactSpriteDrawPacket` has signed XYZ and dimensions,
alpha/animation bytes, flip flags at `0xD`, opaque bytes and a descriptor
pointer at `0x10`. Flags 4/8 initialize that packet byte before the texture
provider; a detached mask local would be incorrect. A texture header below
`0x10000000` is a direct image; otherwise its frame table is indexed by
signed phase shifted right eight. The texture provider receives all eleven
retail arguments, then the source copies the record's XYZ into the packet.

Negative width uses the absolute camera yaw plus low-byte orientation times
1.40625, repeated 360-degree folding, 180-degree folding and 90-degree
reflection. The signed dimension is scaled by `D_800A6CA0`, truncated and
clamped to at least 1,024. Negative height uses absolute camera pitch,
`max(0, original width) + height`, `D_800A6CA4`, subtraction of the original
height, and truncation. Inputs in the fixtures remain finite and within the
qualified conversion domain.

Flag `0x100` selects custom geometry/combiner/modes from settings at `0x14`;
flag `0x200` adds `0x100000`. The other route selects modes by texture kind
and flag `0x10`. Retail retains a type 3 test after the type 5 gate makes it
unreachable; the source keeps and comments that original structure. Primitive
RGBA follows; environment RGB uses flag 1, special blue/white textures, or
zero. The projection provider returns the final graphics cursor.

The direct **21-word/frame24 `func_15178750`** in
`conker/src/game/generated_1A5440.c` previously under-declared the renderer
with one argument. Its declaration and call now explicitly pass cursor,
the original record, and signed view. The visibility owner loaded from
record+`0x14` is used only for the visibility test. Passing it to the renderer
would be wrong. The full caller still emits all 21 retail words directly from
C, and its complete padded owner stays byte-identical. The field's dual
settings/visibility-owner role is documented without inventing a shared type.

## Source-origin and private-storage qualification

The final named primitive-color/render-word locals recover the 168-byte frame
without fake padding or physical-register bindings. Explicit green captures
on the two outer branches recover retail's duplicated load. Source naming
and comments change none of the 42 renderer-owner or 11 caller-owner raw
function payloads relative to their selected complete candidates.

Four ORI/copy pairs, raw indices 189/193, 217/218, 240/241 and 262/263, coalesce
the mode argument directly into A1. Static register/use/CFG checks establish
that old A1 is unused between each pair and no temporary use escapes before
the caller-clobbering call, including its delay instruction. Omitted words
are neither branch targets nor executed delay instructions.

The 337 retained origins preserve opcode, function, literal and named binding.
Only register roles, measured local-object homes, independent scheduling and
source-derived branch labels change. One source edge 33->40 becomes 33->41
because a pure sync-address ADDIU moves to the common branch delay slot;
its temporary is untouched until outgoing-argument store 50. No arbitrary
retail instruction stream or shape-alignment output is installed.

The raw private flag LBU at 19 executes speculatively in a normal branch delay
slot; retail's corresponding load 20 only runs on the bit 8 path. The byte is
initialized on entry and false-path T9 dies at the constant definition 28.
The per-origin observer qualifies 2,790 such dead-load instances. It tracks
private-pointer provenance rather than relocating integers that happen to
equal stack addresses. Raw full access order/private fault identity is not
claimed. Finite f32 add/multiply commutation is qualified by the bounded model;
FCSR/nonfinite/asynchronous effects are outside that model.

## Fresh checks and production audit

- Raw, padded and retail guest streams each pass **2,970 cases**, plus
  **36 independently rebased runs**. The per-origin operand/result observer
  separately passes all 2,970 cases, with no differing retained origin.
  The static copy/liveness proof covers the unreachable retained branch too.
- Actual SDK32 native O0/O2/O3 each pass **1,890 cases** under strict aliasing
  and UBSan. All 17 used record offsets, packet layout and camera stride 9A0 /
  fields 380/388 are asserted. Checks include full records and opaque bytes,
  aligned metadata, mode table, command words, ordered provider observations,
  returned cursor, full camera bytes and record/output/camera canaries.
  An additional 360 finite camera/phase cases are checked in both complete
  MIPS streams before their expectations enter the native table.
- **17 effective source controls** all fail through the comparison oracle,
  covering flips, signed frame indexing, phase packing, angle folds, width
  minimum, height arithmetic, custom flags, combiner byte, mode bit, primitive
  channels, special blue fallback and final cursor submission.
- The complete direct caller and leaf run **448 cases per stream**, with
  **112 renderer invocations each**. The wrong visibility-owner argument
  control is rejected. Guest views outside the C shift domain remain explicit
  guest extensions, not portable native caller coverage.
- The complete original **348-word/frame144 `func_151674F8`** render-list
  parent runs **116 cases per leaf stream**, with **224 leaf invocations**
  each, both actual slot8 call sites 151677F8/151678B0, rows 0/1, empty/multiple
  nodes, three draw modes, pre/post callbacks, budget rollback, viewport and
  saved-next retention. Descriptor columns **5/66** are checked in ROM at
  **230074/230CD8** and in private/production data. Frozen original assembly
  independently assembles to all 348 ROM words. Three controls reject missing
  registration, lost saved next and a descriptor passed in place of a node.
  Word 224 is an unreachable duplicated depth-byte load; 347 words execute.
  The parent's current false C placeholder remains unchanged and uncredited.
- **323 normalized/retail access-prefix pairs** compare full memory, GPR/FPR,
  trace, calls, observations and HI/LO. **37 raw/padded/retail public provider
  boundary triples** compare public state, calls and returned cursor. Provider
  internals remain bounded contracts; no FCSR, timing, hardware or gameplay
  acceptance is inferred.
- Both production padders match. **12 GNU links** across four HI16 carry
  boundaries match. Six malformed expected-word/binding controls are rejected;
  two wrong replacements fail complete-output comparison.
- Both full owners preserve all **41 renderer neighbors** and **10 caller
  neighbors**, pools and compiler diagnostic sets. The actual Make recipes
  reproduce both padded owners in six commands. The caller object stays
  `69db84bac3dc9a94146701892c2da25571974691914061117e28085b838579c3`.
- The entire production ELF equals an independent prediction: **1,111 changed
  bytes, zero exclusions**. Only the 1,348-byte target, its size 12->1348 and
  three explicitly reconstructed symbol/string permutations are allowed.
  Seven symbol records and 77 string bytes are reconstructed, with 41 metadata
  bytes different; the complete named-definition multiset stays fixed.
  No actual-diff windows are copied into the prediction.
- All **189,088 protected Game data bytes across 720 owners**, other loaded
  bytes, addresses, extents, conversion rows and the old guard-byte prefix
  stay fixed. Shared headers and Make profiles stay fixed.
- Seven gates run fresh in each tools configuration. Each installed run
  freshly recompiles both owners, replays real Make and compares the entire
  linked image; six semantic gates are reused only after exact source,
  binding, import, manifest, artifact and native-binary fingerprints agree.
  Those six are explicit reuses. `make tools-check` passes. The real sibling's
  dirty state, HEAD and dependency hashes stay intact through disposable
  overlay checks using its own Make padder.

Raw target SHA256:
`8160dc7ead367f9cef2e0af47b7aa43ad74852b7aaffc078b06643b00d6bc4b6`.
Qualified renderer owner SHA256:
`3d8f4cfb4ca5dc13c3fb78e17e4c5b8373af6e6df322656a48d41afee56ec178`.
Production ELF SHA256:
`d4fe18a2d8fb16767851c49b3da28ef6d77fe3f37ca1eac9aeebbf03c74e22d4`.

```sh
python3 -m unittest tools.tests.test_game_compact_sprite_renderer_15168118_match -v
```

Artifacts: `conker/build/game-compact-sprite-renderer-15168118-private/`.
Frozen-input checks fail closed. Codex owns implementation/validation;
Claude calls attempted/completed: 0/0, with no auth/provider changes after the
existing local inventory reported logged out. No push or host/Release changes.
Continue the remaining Game functions toward 85%.

Graph maintenance: the native update exited 1 with all
71,525 prior IDs retained. The subsequent serial scoped extraction
covers 13 C/Python files with no missing AST sources, producing
71,624 nodes / 173,505 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
