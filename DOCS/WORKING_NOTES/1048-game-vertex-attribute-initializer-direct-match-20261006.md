# Game Vertex Attribute Initializer Direct C Conversion

Date: 2026-10-06. Starting checkpoint: `a6f722fc`.

Convert **`func_151400D0`, 48 words / 192 bytes**, VA
0x151400D0..0x15140190, ROM 0x16D580..0x16D640, frame zero, in
[game_169510.c](../../conker/src/game_169510.c). Retained assembly already
matched; complete semantic C now emits the same slot directly under existing
O2/g3. No new guards/profile/shared header/data/symbol/metadata. Keep the
[retail assembly](../../conker/asm/nonmatchings/game_169510/func_151400D0.s)
as the unchanged reference.

## Recovered Contract

Void return and two byte pointers. Four **10-byte input records** initialize
four **16-byte output vertices**. For each record, in the retail machine order:

1. Read unsigned halfword input+8 and store it to vertex+6.
2. Read signed halfwords input+0/+2/+4 in order and store their low bytes to
   vertex+0xC/+0xD/+0xE respectively.
3. Read signed halfword input+6, clear vertex+6 as a halfword, then store the
   captured low byte to vertex+0xF.

No clamp or saturation. Positions +0..+5 and texture coordinates +8..+0xB
remain untouched. The final flag halfword is zero, but its **intermediate
nonzero store must remain**: output may alias input and change later reads.
For output==input, writing the input+8 halfword to output+6 changes the alpha
read at input+6. Reading alpha after the flag clear is also observably wrong.
No snapshot of all input records; later records read current, possibly
modified memory. Tests distinguish exact ordered accesses from only final
colors and zero flags.

The C source directly assigns alpha before clearing the flag; IDO schedules
the clear between alpha's load and byte store, exactly as retail. The two
output writes are disjoint. A named alpha temporary preserves semantics but
changes register allocation. The two-pointer owner-local declaration replaces
the old signed-word return/argument placeholder. Its only live C caller,
`func_1513D2F0`, passes result+0xC0 and casts its existing table-address word
to `u8 *`. No shared prototype change or portable 64-bit pointer claim. The
helper return was never consumed. Both constructor and corner-helper words
remain identical; their experiment/native declarations are updated consistently.

## Compiler Evidence

[Driver](../../tools/experiments/game_vertex_attribute_initializer_candidates.py)
screens **six forms x four profiles = 24 controls**, isolated diagnostics
empty. Direct byte-pointer loop: **48 words/frame zero/zero differences**
under O2/g3. Plain O2 gives 47 words and two differences. O1/g3 and O1
retain a 22-word loop/frame eight with 47 differences.

Naming alpha forces V0 and shifts the later temporary cycle: 48 words but
32 differences. SDK Vtx-pointer named-alpha form has 33; direct Vtx form
has four scheduling differences. Halfword alpha also has 32. Indexed source/
output counters retain a 32-word O2 loop with 47 differences; O1 forms
grow to 60 words/frame eight and 60 differences. Tests bind all measured
lengths/frames/differences, including overflowing tails. Production uses the
original default full-unroll O2/g3 profile, not a new compile override.

## Qualification

[Eight tests](../../tools/tests/test_game_vertex_attribute_initializer_match.py)
use unchanged shared guest/native runners and an independent sequential
byte reference, not a whole-input snapshot:

- **456 guest cases / two bodies**: twelve signed/raw halfword patterns,
  **19 source/output relationships**, both stack phases. Selected C and retail
  each match complete external memory and every ordered read/write, including
  transient flags. No calls; saved GPR/FPR/SP/RA lifetimes hold; **all 48 words**
  execute. Ordinary-memory alias diagnostics, not MMIO/hardware acceptance.
- **65536 selected guest cases** sweep every halfword bit pattern, rotating
  aliases/stack phases, checking complete storage and intermediate traces.
- **131072 native standalone cases** sweep every halfword pattern through
  overlapping/disjoint source/output, checking entire 320-byte storage and
  32-bit pointer/halfword/byte layout. No invented initialization stores.
- **3072 connected guest cases / two bodies** execute actual constructor,
  corner helper and attribute helper. Flag branches, null/success, live
  descriptor index/variant, allocator/zero mutations, negative/full/dynamic
  bounds, resource gate, disjoint table and table==output helper aliases.
  Complete actor/external memory and ordered trace comparison; **all 217
  chain words** execute (114 + 55 + 48). The real helpers do not mutate the
  global default or bound; those former opaque-hook effects are removed, and
  the bound is initialized before entry. SDK/backend providers remain callbacks.
- **131072 connected native cases** run actual constructor C and entry
  instrumentation forwarding to **both real helper bodies**. Every descriptor
  index/variant pair through both allocator outcomes; independent byte
  references verify entire actor, helper fields and 64-byte guarded input
  storage. Live post-zero descriptor index and later view mutations retained.
  The equivalent file-scope corner-table declaration supplies fixture data.
  No backend/gameplay/host adoption claim.
- Six compiled negatives detect stub, omitted intermediate flag store,
  alpha read after flag clear, wrong input stride, three instead of four
  records and displaced color store. Each must differ in **actual memory**,
  not merely instruction/access count.

All **60 focused post-link tests pass in 730.693 seconds**, no skips. Previous constructor and
corner fixtures keep opaque attribute callbacks in their isolated contracts,
now with the correct void/pointer prototype; this suite owns the actual chain.
Their complete compiler controls and source bindings are rerun as well.

## Linked Audit

Build/link/progress pass. Target SHA-256:
`7bf57077ef295e2586d51522f8bc862c4de71a19b776f019a04f7a9999ec81c8`.
**All 6059 linked function slots are identical** to the assembly checkpoint;
all addresses/sizes fixed. Protected `.init`, `.init_data`, `.debugger`,
`.game_data` unchanged. **720 Game-data owners / 189088 bytes** remain
retail-exact; **10660 guards** identical and in order. Owner retains **48
identical preexisting warnings**, zero new after shifted-location normalization;
none in the converted helper. Existing generated_12D630 duplicate-recipe
warnings remain unrelated.

Genuine assembly-to-C conversion increases converted counts:
**5464/6042 (90.43%)**, Game **4791/5321 (90.04%)**. Converted bytes
**85.57% total / 84.89% Game**. Exact totals **3326/5464 (60.87%)**,
Game **2653/4791 (55.37%)**, **2138 different**, zero drift. Init492/492
and Debugger181/181 stay exact. README receives aggregate measurements only.
Ignored receipts under `conker/build/game-vertex-attribute-initializer[-test]/`;
baseline snapshot `conker/build/game-view-corner-initializer/after.json`.
Tools check, compileall and diff check pass. **30 docs / 3329 relative links /
zero broken**. No sibling source/build/save/frozen Release
change, runtime launch, push or full caller/backend/hardware/gameplay/host claim.

## Next Work

Recover **`func_15140190`, 134 words / 536 bytes**, VA
0x15140190..0x151403A8, ROM 0x16D640..0x16D858, frame **0xD0**. Its current
untyped C body returns zero; it is a false placeholder, not a semantic quad
builder. The [retail body](../../conker/asm/nonmatchings/game_169510/func_15140190.s)
has actor-pointer/signed-halfword-view arguments and returns the original
allocated vertex pointer, null on failure.

`func_151D5D60(actor+0x100, view, 0x40, &cursor, &fresh)` fills pointer and
fresh-byte outputs. On null, stop. If fresh, copy actor+0xC0 to the live
actor+0x100 indexed buffer twice, the second copy at +0x40; **reload the slot
after the first callback**. Construct four width/height signed corner vectors
from actor+0x2C/+0x30. Call orientation helper `func_150A8050` with actor's
three words +0x40/+0x44/+0x48, then set translation from +0x34/+0x38/+0x3C.
For each point, call actual matrix helper `func_150A7960`, truncate three
coordinates to signed integer/halfword output, zero vertex flags and advance
the escaped cursor by 16. Preserve original-pointer return and byte counter.

Recover local ABI, output-slot lifetimes, fresh-copy mutations and float/matrix
contracts before installation. The retained **40-word `func_150A7960` returns
normally**, storing Z in its return delay; the separate `func_150A7A00` tail
contract in the triangle-transform tests must not be confused with this callee.
Use those existing arithmetic/alias tests without claiming full hardware FCSR
behavior. `func_15152190`'s 228-word placeholder and semantic/non-matching
`func_1513264C` extended constructor remain separate pending work.

Initial isolated screen: **four forms x four profiles = 16 controls**, no
diagnostics. Baseline byte-counter SDK-vertex C gives **132 words / frame
0xD0 / 114 differences** under O2/g3; plain O2 retains 132 words/frame 0xD0
but 124 differences. O1 variants give 169 words/frame 0xA8/169 differences.
Declaring matrix first gives 118 O2/g3 differences; byte-output form equals
baseline. Widening the counter gives 127 words/frame 0xD8/123 differences
under O2/g3, not the correct frame. No candidate is installed or behavior-
qualified. Ignored source/object/disassembly inputs and measurements are under
`conker/build/game-vertex-attribute-initializer/next-quad/`, driven by
`screen-next.py` in its parent. Next inspect stack layout, saved-register
lifetimes and escaped-cursor reloads before widening the compiler screen.
