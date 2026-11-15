# Game category record initializer: private recovery

Date: 2026-11-15. The next function is **`func_150169A0`**, the
**477-word / 1,908-byte** parent of the resource-cache builder adopted in
[Note 2456](2456-game-resource-cache-guarded-match-20261115.md). Its complete
private C draft emits **476 / 477 words / frame 0x58**, but still saves **S0 and S1**
instead of retail's S0 alone and differs in **457 linked instruction words**,
including its one-word deficit. It remains **uninstalled and uncredited**.
Frame agreement does not establish an exact match.

Production stays **4,496 / 5,515 (81.52%)** total and **3,823 / 4,842
(78.95%)** Game, zero drift, **1,019** different; **192** more matches reach
the active 85% goal. Init is **492 / 492**, Debugger **181 / 181**. The root
README's aggregate figures from Note 2456 remain current and unchanged.

## Frozen inputs and recovered behavior

Owner: `conker/src/game/generated_43D00.c`; original assembly:
`conker/asm/43D00.s`. VA **0x150169A0..0x15017114**, ROM
**0x43E50..0x445C4**. The current production definition remains its existing
zero-return placeholder. Private artifacts are under
`conker/build/game-record-initializer-150169a0-private/`.

The **812-input** snapshot records consumer
`735bbe2b58b5dde327c04b4d3fcc67179e4bd305` and tools
`1e3b5cc8e67476ccff4b8f6f20f7d86a9e79c1c6`. It includes 82 headers,
698 objects, the source, original assembly, guard manifest, conversion rows,
Makefile, linker script and actual production ELF. The prior resource-cache
snapshot is retained separately; it is not silently advanced.

The recovered draft:

1. Resets prior state, selects a ROM record bank, measures category data,
   allocates storage, DMA-copies the base records and appends loaded records.
   The original-count byte is captured before the append.
2. Calls `func_15017114(category)`, allocates byte and halfword per-record
   buffers using a captured count, clears them, and resets `D_800D1548`.
3. Scans the signed player count and halfword enable mask. Active slots use
   `func_150859AC((s16)slot, 1)` to select resource/type settings, flags and
   scale fields, then copy truncated actor coordinates and the heading byte.
   Disabled slots receive their original disabled marker.
4. Calls the now-exact `func_15016850`, fills zero identity bytes through
   `func_15083DA0()`, then submits the original three finalization calls.

The 0x30-byte private record view preserves every field offset and has a
compile-time size check. `D_800D20FC` retains the existing `struct258 *`
declaration; byte arithmetic selects the full records. Shared `struct127`
supplies actor coordinates with its original **0x32C stride**. Coordinate
conversions explicitly truncate to s32 before narrowing to s16; no portable
out-of-range float-to-s16 claim is made. The allocator uses the existing signed
s32 size parameter and the pointer-return
view already used by Init audio callers. No shared header, production compiler
profile, frame guard, dummy local or volatile declaration is changed.

Both retail jump tables and constants are decoded from the original input
and checked against the production ELF. The **38-entry** category switch
selects the larger **0x300-byte** bank for categories **0x1A, 0x24, 0x2B,
0x2D, 0x30, 0x33, 0x34, 0x3F**; other categories use the **0xF0-byte** bank.
The resource selector has **41 entries**, including the grouped ranges and
scene-dependent cases. Original scale constants are IEEE-single **0.6f** and
**0.7f**. The private compiler emits a **336-byte pool / 79 table entries**;
it is not installed into the protected retail data owner.

## Private qualification

- [x] Complete-owner O2/g3/mips2/o32 compilation, no diagnostics. Both other
  raw functions retain their instructions and named bindings. Candidate raw
  text SHA-256 is
  `43c4aa83a2394495d3d716ca65675451b2f89e8c2159fc08b9aa4f1d577d3539`,
  with **68 binding sites**.
- [x] **686 guest cases / two streams**, comparing original retail and the
  complete compiled C draft. Every mapped public byte and full public
  helper-entry snapshot agrees. Saved GPRs, saved FPRs and SP are preserved;
  both streams retain their readonly pool bytes.
- [x] The corpus includes all **256 category byte values**, all 41 resource
  selectors and three out-of-range selectors, six scene selectors, enable
  masks, signed count/split boundaries, signed/truncated coordinates, two
  stack phases, all 32 combinations of five provider-effect bits, and six
  empty-record cases. The 33-slot guest fixture deliberately remains distinct
  from the shared 26-actor native storage contract; native validation is open.
- [x] Provider effects exercise live record-table redirection, updated actor
  positions, count changes after preparation/allocation/cache/identity calls,
  and captured allocation lengths. Helper internals are opaque; these checks
  do not reconstruct those providers or establish gameplay behavior.
- [x] **473 / 477** original words are executed. A separate structural check
  accounts for the four unexecuted words: the constant-48 divide guard's
  bypassed `break` at **0x15016A90**, and loads at **0x15016C34, 0x15016E00,
  0x15016E84** bypassed by the preceding unconditional branch/delay pair and
  absent from both branch and table targets. The empty-count case exercises
  the original likely-branch delay load at **0x15017088**.
- [x] Three supported-instruction controls reject a changed category-switch
  offset, active marker and position-store destination. The first fixture
  attempt accidentally placed ALT at guest STACK (0x40000); it was rejected,
  moved to 0x60000 and protected by an overlap assertion before these results.
- [x] Aligned input census finds one direct call at ROM **0x35380**, VA
  **0x15007ED0**, and no literal function pointer. The authentic **JAL / LW A0**
  delay-slot window passes **48 cases per stream**, including category load,
  helper packets, entry snapshots, public memory and saved-register/SP state.
  Complete caller reconstruction and the parent result-use proof remain open.

Fresh mounted suite: **84.943 s**. Sibling overlay:
**43.839 s**, four byte-identical task files, **64 guest
cases / two streams** plus the **48 caller cases / two streams** and fresh
candidate compilation. The larger mounted corpus is not described as a fresh
sibling execution. Fresh `make tools-check`: **passed**.

Reproduce using the prepared consumer and retained snapshot:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_record_initializer_150169a0_recovery -v
```

The initial 680-case receipts remain archived under `qualified-680/`.
`qualified-477/` retains the later 686-case receipts for the earlier draft.
That draft used an unsigned allocator-size prototype and emitted 477 words.
ABI review corrected the size to the signed s32 view used by Init; IDO then
emits 476 words and the raw fingerprint above. The current suite requalifies
that corrected draft. The old word count is not retained by using the wrong
interface. No production allocator or shared declaration is edited.
Source-form screens for integer banks, unsigned/byte counts, unsigned stride,
declaration order, a source register hint, short/unsigned player indices,
byte actor views and retail case-block order are retained as private
experiments against the earlier unsigned-size draft. None resolves the extra
S1 save; none is installed or credited.

## Production boundary and next work

All **812 frozen production inputs** are verified before and after the mounted
suite. Source, CSV, original data pools, conversion rows, headers and objects
remain fixed. Production ELF SHA-256 remains
`668933c3c17e33b1f6d52729397cdfaf7a88690fac78d81bae9cde41c9b80d9c`.
The accepted production match and its protected-data audit are Note 2456;
this private recovery adds zero match credit.

Sibling HEAD/status preservation: **HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,439 dirty paths** and status SHA-256 `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb` remain fixed**.
Scoped Graphify AST merge covers four new tools files, retaining all
**61,188 old IDs**, zero loss: **61,188 nodes / 114,934 links**. This is
not a full-corpus re-extraction. Routine Claude calls: zero. Tools commit
`a63c765fe4974d25c681685e8d19d8ae9fe3f1d3` precedes the consumer documentation/pin commit.
No push; host Release remains frozen.

Continue this function. First recover the original single saved-register
lifetime and stack homes: **S0 SP+0x20**, **RA SP+0x24**, bank **SP+0x4C**,
captured allocation count **SP+0x40**, player index **SP+0x3C**, and identity
index **SP+0x54**. The private draft reuses an extra S1 for the bank, stride,
captured count and loop indices; equal frame size does not qualify those
differences. Retain all live-provider and empty-count tests while resolving
the full instruction/table layout.

Then complete native32/ABI result-use qualification, any required access-order
or fault boundary, both actual padders and independent rebases, exact data
binding, actual Make, strict whole-image prediction, production adoption,
recount and documentation gates. The separate common particle updater remains
private at [Note 2452](2452-game-common-particle-frame-native-and-callers-20261114.md).
The 85% goal remains active.
