# 2485 - Full side-ring renderer recovery and exposed stack homes

`func_1519FE6C` now has a complete **private, uninstalled C recovery**. The
selected source emits **639 words / frame 0xE8**, versus retail's **632 words /
frame 0xF0**. It preserves the allocator cursor at incoming-SP **-4** and the
graphics sync byte at **-95**. Length, frame, saved-register and whole-CFG
normalization remain open; **no C-match credit is awarded**.

Production stays at **4,512 / 5,514 (81.83%)**, Game **3,839 / 4,841 (79.30%)**,
zero drift. **175** more matches are required for the active 85% goal. The
previous emitter match remains installed and committed.

## Complete source and ABI

Owner `conker/src/game/generated_1CC440.c`; VA `1519FE6C..151A084C`, image
`1CD31C..1CDCFC`, 2,528 retail bytes. The body renders the same 36-byte side
entries as a backward strip with three vertices per point and four G_TRI1
commands per segment. It writes complete 16-byte SDK vertices, including
zero flags and edge alpha, and returns the updated graphics command cursor.

The signed count gate runs before allocation. `func_151D5D60` receives
effect+0x84, signed-16 view, capacity*48+0x120 bytes, a four-byte output slot
and a null optional fresh-byte pointer. Null allocation avoids loading payload
and entry pointers. Those pointers are captured after allocation and retained
across the six graphics setup providers; later public fields reload at their
retail points. The texture descriptor is `D_80090E0C`, index 57, flags 62.
Environment/primitive colors, geometry, combine and render-mode arguments are
recovered from the complete assembly and checked independently.

Both fade loops enter once even with an initial zero count. Their count is
narrowed to signed 16 bits; factors wrap as bytes. Forward fading starts at
the head. Backward fading starts at tail-1, wraps and scales the retained
light halfword. Texture endpoints use signed halfword wrapping and a signed
remainder modulo 1024 before calculating their midpoint. Mode 6 selects one
edge orientation; other modes select the reverse orientation.

The initial segment uses the literal **0.0001f** movement threshold. Later
joins test exact zero before reciprocal square root. Positions use entry
x/height/z order, while the effect's attached point is ordinary x/y/z order.
The independent model initially confused those two layouts; the literal
retail stream rejected it, and the model was corrected before qualification.
Signed tags remain halfwords; the final vertex opacity is a byte. Every
vertex field and all five generated graphics commands per segment are checked.

The third callback table, **D_8008A2A4**, contains this function at **slot 5**
(8008A2B8 / image 22ED78). Complete original `func_15147C4C`, 52 words, loads
the selector from effect+0x31. Its JALR at 15147CF8 passes the effect, updated
command cursor and signed view loaded by LH in the 15147CFC delay slot; the
callback return propagates to its caller. This is a checked N64 register-level
ABI; no shared callback-type migration or portable whole-program C claim is made.

## Selected source and remaining gaps

The initial complete typed source was **648 words / frame 0xF8**, cursor home
-40 and sync home -41. Natural outer gates, explicit mode cases, byte opacity,
halfword tags and declaration ordering recover **639 / 0xE8** and both exposed
homes. Position homes are **-24 / -36**; the three signed texture coordinates
start at **-92**. ECOFF local records and actual callback pointer arguments both
verify the selected homes. No padding arrays, synthetic live values or volatile
hints were added to force the frame.

The selected body still saves **S0-S3**, while retail saves **S0-S2**. It has
seven extra instructions and **627 positional word differences**, including
the length difference and the effects of shifted code/register allocation.
These measurements do not establish a safe guard recipe. No normalization,
padding, insertion, omission, compiler-profile change or production replacement
has been attempted.

Selected raw text SHA-256:
`c04f5dc1324f7969b3093335463cdd7be05de52ad111d147b6b59514cde30c66`.
Initial raw text SHA-256:
`48140c79b53ab334dcce6ee801de1001406f7e1c06fd7771412ae593d39c6b6a`.
All **13 relocations** are pinned for each source. Complete-owner compilation
preserves all **38 other functions**, including the previous emitter's raw
words/bindings. The compact pool's first twelve emitter literal bytes remain
fixed; the renderer's epsilon replaces the final four alignment bytes.
Production pools and protected data remain unchanged.

Source probes retain their diagnostics. A byte-owner/record-view composition
that initially produced an incompatible-pointer warning was rejected and
corrected; qualified candidates compile without warnings. The local m2c output
is a retained advisory, not the source or type authority. **Zero Claude calls**
were needed for this recovery.

## Fresh qualification and preservation

- **299 guest cases per retail/initial/selected stream** compare complete
  public snapshots, all vertices/commands, provider arguments and return value.
  The streams visit **627 / 642 / 634 instructions**, respectively. Concrete
  FP opcode/operand sequences agree for all 299 selected cases; this is not an
  all-input FCSR/trap-order proof.
- **Six effective guest corruptions** cover signed count, allocation size,
  zero-count fade entry, negative texture remainder, height component and last
  triangle. Separate lazy-pointer tests remove payload/entry pointer bytes on
  inactive and null-allocation paths.
- **299 native cases per profile**, O0/O2/O3 with and without strict aliasing,
  UBSan, provider arguments, complete typed public objects and **512-byte
  vertex / 512-byte command windows** pass. **Twelve source controls** are
  effective. The attempted unsigned-view control was ineffective because the
  allocator's signed-16 prototype narrows it again; it was replaced by an
  allocation-size corruption and is not counted.
- **128 connected cases per stream** execute the complete original 52-word
  allocator and 52-word dispatcher. All **52 allocator words** and 45 dispatcher
  words fire. Cache reuse, allocation failure/success, signed views, both page
  selections, forwarded arguments and returned cursor agree. Deep allocation,
  transform and graphics services remain explicitly bounded hooks.
- The primary two-test suite passes in **57.344s**. The sibling overlay runs
  the same six task files against its own available dependencies and passes
  in **86.361s including startup**; task hashes
  and its full pre/post Git status are retained. Existing sibling edits are
  preserved. `make tools-check` passes.
  A subsequent report-key correction distinguishes compact alignment from
  retail data. Only that dictionary keyword changed; both compiler gates were
  refreshed with identical C bodies/raw hashes. The existing native/guest
  receipts remain applicable, and the source-hash amendment is retained.
- A new **881-input baseline** begins at consumer d430461c / tools a496efa.
  Every frozen production input remains byte-identical: source, guard history,
  objects, linker script, conversion rows, ELF and protected data are unchanged.
  The prior emitter's 880-input baseline was neither advanced nor overwritten.

Production ELF SHA-256 remains
`902b8b86f8ffc963c593e33b844245bf4d295dd69bd42944159f66be2b92d20e`.
No host-port source/build applies; frozen Release artifacts and saves remain
untouched. No emulator, rendering hardware or native hardware FCSR behavior is
claimed by this private recovery.

Receipts and surviving probes:
`conker/build/game-side-ring-renderer-1519fe6c-private/`.
The scoped graph refresh retains all **62,509 prior IDs** and adds an explicit
reference to this function. Commit-hook retention is checked separately; this
is not a full-corpus extraction claim.
Native `graphify update .` refused a 62,552-to-26,731-node shrink and kept the
graph. No force, re-extraction of the full corpus, or package upgrade was used.

Reproduce in the prepared consumer:

```sh
python3 -m unittest tools.tests.test_game_side_ring_renderer_1519fe6c_recovery -v
make tools-check
```

Continue **this renderer**: recover the S3/entry-base lifetime and retail frame,
then reduce the seven-word length gap and prove remaining register, private
stack and branch-schedule transformations over its complete CFG. Preserve the
now-correct exposed homes and both normalization predicates. Only after that
run both padders, independent symbol rebases, actual Make, strict whole-image,
production, recount and documentation gates before claiming a new match.
