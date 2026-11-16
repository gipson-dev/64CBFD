# Camera-facing ribbon renderer full recovery and guarded byte match - 2026-11-16

`Gfx *func_151A3BE4(u8 *owner, Gfx *output, s16 view)` replaces its zero-return
placeholder with the complete camera-facing ring ribbon renderer. Semantic C
emits **619 words / frame 0x128**. **357 relocation-aware expected-word guards**
normalize register allocation and scheduling to the complete retail slot,
with **no insertions or omissions**. VA 151A3BE4..151A4590,
ROM 1D1094..1D1A40. This is a guarded C match, not a direct compiler match.

Actual production recount: total **4,524 / 5,514 (82.05%)**, Game
**3,851 / 4,841 (79.55%)**, Init 492/492, Debugger 181/181; zero address drift,
990 still different, **163** more matches to 85%. Conversion stays
5,514/6,048 (91.17%) and 86.19% of bytes. The wider matching goal stays active.

## Recovered behavior and ABI

Fewer than two live records returns the incoming graphics cursor. The vertex
allocator receives the owner cache at +0x84, signed 16-bit view and
capacity*32+160 bytes; a null result returns without drawing. The renderer
caches record storage (+0x94), profile (+0x98), and view-specific eye position
before graphics setup. The existing 24-byte sample names position, value,
lifetime, mark and phase; this renderer uses value as the ribbon half-width.
The new local profile names both fade counts/steps, flags and phase offset.
Unknown bytes retain reserved offset names. No shared header/profile changes.

The two optional fade scans preserve the retail do/while entry even when the
initial count is zero, byte wrapping and signed short countdown. Graphics
setup retains all eight provider ABIs, including memcpy's destination, source
and byte count, the private cursor at incoming SP-4 and sync byte at
SP-93. Providers are allowed o32 caller-register clobbers and public mutation;
all actual pointer/integer arguments and post-call reads are qualified.

The renderer chooses an owner-position or prior-record starting point,
computes the camera-facing perpendicular and its length, handles a zero
normal, and writes two vertices per point. Coordinates truncate; UV, RGB,
opacity and flag stores retain their order. Each segment appends one vertex
command and two triangles. At a phase wrap, it copies the current 32-byte
pair first, then subtracts 0x4000 from the two emitted source UVs. The cloned
pair keeps its original UVs for the next segment. Reverse ring traversal
preserves head termination, wrap, lookahead and saved-register lifetime.

## Fresh qualification and retained failures

Five maintained tests pass at the same ten task-file fingerprints in primary
tools, an isolated sibling overlay, and installed production.

The smaller v6 draft matched sampled public outputs but changed FP order in
974 of 1,004 earlier cases; it remains rejected. The selected v7 preserves the
normalization length/scale as real locals, restores frame 0x128 and both exposed
homes, and agrees on ordered FP. No dummy padding or physical-register bindings
are used.

- Whole-function symbolic composition closes **50 component paths**, including
  both fade loops, setup, both normalizations, vertex-pair writes, commands,
  seam copy, loop tail and epilogue. Its fixed point checks values carried
  untouched through phases, all private cut inputs and saved GPR/FPR custody.
  Ordered FP operands/operations/FCSR and public writes/providers agree;
  ordinary read inventories agree between public writes. All **618 reachable
  instructions** in each stream are covered. The unreachable word at +0x31C
  remains fingerprinted and normalized with the entire 619-word body.
- **15 instruction corruptions** and **nine cut/ABI-assumption corruptions**
  reject independently of fingerprint guards. Three positive controls pass:
  renamed symbolic roles, a temporary GPR swap and a dead-word mutation.
- Independent guest model: **1,052 cases per retail/raw/guarded stream**,
  complete initialized public memory, provider arguments, return cursor,
  private exposed homes and ordered FP operations. Two guest alias families
  overlap the vertex output with profile/records. No FP order disagreements.
- Native32 C: **992 finite, disjoint typed cases each at O0/O2**, UB traps,
  strict aliasing, complete owner/profile/record/vertex/command snapshots and
  unchanged view storage. Thirteen semantic negatives compile and exit 3.
  An earlier fixture interpreted untouched random command bytes as pointers;
  its failure and diagnostic are retained. Relocation now requires an actual
  expected vertex command/address, and a wrong source-pointer control rejects.
- **2,048 connected cases per stream** execute the original 52-word dispatcher
  `func_15147C4C`, 52-word cache allocator and 11-word memcpy, visiting every
  word. They qualify signed views, transform arguments, selector bypass/release,
  cached/new/failed allocations, both buffer pages, seam and non-seam paths.
  The first maintained attempt correctly failed its COPY coverage assertion:
  its phase inputs never crossed a seam. The archived attempt has no acceptance
  credit; adding independent seeds 0/10 fixes coverage without changing C.
- Both actual whole-owner padders retain all 22 neighbors and pools.
  **619 raw-word + 14 binding corruptions** and two stale actual CSV controls
  reject. Three independent GNU links check rebases including HI/LO carries.
  The previous CSV bytes remain an exact prefix; only 357 target rows append.

The symbolic domain is normal mapped/aligned public RAM with a private disjoint
stack. Public reads may commute with FP operations, preserving ordered FP and public
writes; this is not arbitrary fault-prefix or general C aliasing equivalence.
Native validation covers finite valid typed inputs, not hardware FCSR. Graphics
services, upstream transform, release and deep allocation remain bounded opaque
providers. No gameplay or hardware acceptance is claimed. Guarded literal
identity separately restores the original instruction stream.

## Production and reproduction

The accepted-state freeze starts consumer `2451f513` / tools `b85ff1c6`.
All **1,301 prior inputs** stayed unchanged before expanding the task freeze to
**1,321 inputs**. The failed fixture snapshot remains archived. Exactly source,
guard CSV, owner object and ELF change; **1,317 inputs remain unchanged**.
Actual Make shadow and production rebuild source through the existing profile;
no prebuilt object is installed. All 23 raw owner functions agree with the
qualified owner, and both padding routes preserve the 22 neighboring functions.

The whole ELF equals the independent byte prediction with **1,878
changed bytes / zero exclusions**. Named definitions agree except the target
size; no symbol/string permutation is needed. Symbol-value/name,
protected-byte and target-word corruptions reject. Every address and all other
6,050 bodies remain fixed. Only one of 698 objects changes. Progress/conversion
CSV is unchanged. All **189,088 protected bytes / 720 owners** stay exact,
SHA256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256: `163661f209789afbf34072f2d1abd8eebd2c6c956a8fd74fe02afef2e35e96ea`.

Reproduce: `python3 -m unittest tools.tests.test_game_ribbon_renderer_151a3be4_recovery -v`.
Receipts: `conker/build/game-next-151a3be4-private/adoption/`.
Sibling dirty state and scoped dependencies remain unchanged; actual imports
record overlay/sibling/primary origins. Scoped Graphify refresh retains old
node IDs and records the manifest reference; it is not full-corpus extraction.
The native update refused a 63,539 -> 26,834-node shrink. The scoped ten-file
AST merge retains all 63,539 prior IDs instead of forcing that overwrite.
Zero Claude calls. No host, frozen Release, save, dependency upgrade or push.
Commit tools first, then consumer source/guards/pin/docs. Next inspect
`func_151A4638` (129 words / frame 0xA8); `func_151A4590` already matches.
Keep the 85% goal active.
