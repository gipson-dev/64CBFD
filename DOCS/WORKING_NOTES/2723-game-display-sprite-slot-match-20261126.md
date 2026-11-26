# Display sprite slot guarded match - 2026-11-26

`func_15179600` replaces its zero-return placeholder in
`conker/src/game/generated_1A6360.c`. The full **108 words / 432 bytes match
retail after 12 expected-word guards**: 96 words emit directly from semantic
C, and 12 normalize two closed caller-saved GPR cycles. The original
**248-byte frame**, all 14 binding positions and all instruction positions
are preserved. VA `0x15179600..0x151797B0`, ROM `0x1A6AB0..0x1A6C60`;
no alignment tail, insertion, omission, relocation rewrite, frame patch or
compiler-profile/Makefile change. All eight owner neighbors and pools stay
fixed, including five exported retail jump labels.

Production: **4,702 / 5,528 (85.06%) total**, **4,029 / 4,855 (82.99%) Game**,
Init 492/492, Debugger 181/181, zero drift, 826 still different. One matching
credit, no conversion-row or denominator change, and no caller/helper credit.
The active **90% goal requires 4,976 matches: 274 more**.

The recovered interface is `void func_15179600(s32 randomizeHeight, u32 value)`.
The first argument controls the height branch; the second preserves a full
32-bit opaque value stored at descriptor+0x80. The local
`DisplaySprite15179600` view describes a measured 168-byte descriptor, with
the signed slot-index halfword at +0x84. Type/field names are inferred roles;
the effect's original name and visual identity remain unknown. The existing
canonical `struct108` supplies the camera's three float field offsets.

The function sets texture 17, value8A=51, tag 1 and flags 0, then calls the palette
initializer with RGBA `(255,255,255,80)`. Only afterward does it read the current
camera pointer and truncate XYZ to signed 32-bit. Two signed RNG remainders modulo
500 produce X/Z offsets. A zero first argument selects cameraY+500; a nonzero argument
uses a third signed remainder for Y. A final **unsigned** RNG remainder modulo
10 produces remaining=35..44 and mode=10..19. The routine sets lifetime 4,
flags 0x8C00, coordinates, the opaque value and the pre-factory slot index,
then calls `func_15168800(&sprite,255,0)`. On success it reloads the current
global index and table, stores the returned pointer, reloads the index again,
and increments it with signed 16-bit truncation. It adds no initialization for
unknown descriptor fields. In particular, initialHeight remains unwritten.

The first private source had 108 words/frame 240 with 40 differences. Reordering
meaningful local declaration groups restored descriptor SP+0x28 and reduced
the differences to 29. Capturing signed random draws in a shared `randomValue`
local restores frame 248 and all six coordinate/origin homes naturally, leaving
12 register differences. A pair of distinct draw/remainder locals also fits
the frame; the shared draw capture is selected. These are consumed algorithmic
values, not padding, dummy locals, larger descriptors or physical-register
bindings. RA is saved at SP+0x1C, incoming arguments at SP+0xF8/0xFC, and the
descriptor occupies SP+0x28..0xCF. X/Y/Z use SP+0xF4/0xF0/0xEC; captured
camera X/Y/Z use SP+0xE8/0xE4/0xE0.

The guard derivation explicitly maps raw to retail registers as two cycles:
`T2 -> T7 -> T9 -> T2` and `T3 -> T8 -> T1 -> T3`. In offsets 0x114..0x164,
each renamed role has one definition before its one use. None supplies a
memory base or ABI argument, and all roles end before the factory call.
The derivation changes only register fields and proves that every opcode,
immediate, relocation, memory access, FP word, call, branch and instruction
position remains fixed. No guarded position has a relocation. Expected raw
words reject changed inputs; the old complete guard CSV remains an exact
prefix, followed by these 12 derived rows.

Validation:

- Both complete owner padders use original `1A6360.s` and produce identical
  whole objects, with all eight raw/padded neighbors, pools and exported
  labels unchanged. The actual three-command Make recipe agrees under normal
  O2/g3/mips2/o32 with zero target diagnostics. The full build retains its
  existing duplicate-recipe warnings for generated_12D630, generated_F44D0
  and generated_F5800; no Makefile change or warning suppression.
- Guest: 856 cases per five streams, all 108 words exercised. Four literal
  retail/normalized/padded streams have identical full private state and
  127 fault-prefix quadruples. Raw C has identical memory access order,
  FP/FCSR, HI/LO, calls and complete results under the qualified providers.
  At faults, an explicit live-register relation checks the two cycles;
  **full raw fault GPR identity is not claimed**. The relation persists
  through the factory JAL's delay-slot store, before the call may clobber
  those volatile registers. The initial oracle boundary ended at the JAL;
  a literal delay-slot fault exposed that fixture omission, which was fixed
  and rerun before packaging. No production-source change was required.
- An independent semantic reference compares complete public memory, call
  order, all 168 packet bytes and ordered truncations. Signed draw extremes,
  unsigned modulo 10, zero/nonzero/high-bit mode words, index halfword limits,
  success/failure, all four rounding modes, mutable camera pointers/data,
  pre/post-factory index/table changes and descriptor mutations are included.
  Incoming argument-home mutations are guest-only experiments. Finite and
  bounded-invalid TRUNC.W.S software results do not establish hardware trap
  delivery or portable C behavior for out-of-range conversions/overflow.
  Native cases separately use valid finite conversions and bounded additions.
- Connected guest checks run the original 105-word palette and 28-word factory
  with opaque allocator/copy contracts. The original 18-word RNG slot is pinned
  but remains opaque here. Palette dimensions include 0,47/31,65535. Every
  packet byte is compared even though the C descriptor is partly unwritten.
  No original allocator, copy backend, gameplay or hardware execution claim.
- The ROM census finds one aligned plain JAL at ROM 0x1A66C4 / VA 0x15179214
  in `func_15179008`, passing `(1,1)` and returning to 0x1517921C. No aligned
  plain pointers were found; compressed/script/derived references are not
  excluded. The full original 304-word/frame 64 parent and its jump table are
  pinned. Its production ELF slot remains different and receives no credit.
  On mode 1/low-timer fill-loop paths, 320 cases per original/raw stream execute
  944 connected children each and 80 parent words. An independent complete
  reference on these paths checks four attempts, the 300-slot limit, skipped
  attempts after reaching 300, failure and fresh index reloads. Three return
  poisons `(0,FFFFFFFF,13579BDF)` leave public effects unchanged through parent
  return, confirming the void child ABI. Origin/scatter followups use opaque
  contracts; other FSM states, audio paths and RNG-reset branches remain
  unqualified. This is not all-state/all-304-word parent coverage.
- Native: actual selected C in three translation units, 4,096 cases at each
  O0/O2/O3, strict aliasing, UBSan traps and LTO type checks. Typed camera,
  descriptor and slot-table views assert every accessed layout. Native
  providers observe 109 initially defined descriptor bytes and never read the
  other 59 before definition. A palette mutation defines retainedA4, which is
  then compared. Native output copies only defined fields into initialized
  arenas; it does not claim observation/copying of unknown C bytes. Whole
  initialized camera/table/output arenas, canaries, metadata, calls, globals
  and MXCSR agree. Eleven semantic negatives finish with comparison exit 42,
  including a cached post-factory table/index control. A compile warning in
  the first late-camera negative was corrected before it counted; compile
  failures, signals and traps never count as semantic rejection. Providers
  are noipa contracts, not original backend implementations.
- Both scoped padders reject 24 guarded-word corruptions, expose 192 other
  word and 28 binding corruptions, and reject oversize objects. Twenty GNU
  links and 100 guest rebases cover jump regions and signed-low carry seams.
  Original connected helpers are qualified only at retail addresses; rebase
  cases use opaque contracts. No guard masks a changed binding.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **320 changed bytes, zero exclusions**. All
  189,088 protected data bytes across 720 owners stay fixed. ELF SHA256:
  `ee22885afcb320ccbba8d90e50f830b0440aef653edfaba4e9f651bceea6d640`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 155.273 s | 5 fresh / 0 reused |
| preinstall-sibling | 116.352 s | 5 fresh / 0 reused |
| installed-primary | 94.357 s | 5 fresh / 0 reused |
| installed-sibling | 106.889 s | 5 fresh / 0 reused |

All 20 target tests are fresh, with matching primary/isolated-sibling source,
task, import and data fingerprints. Shared tools-check passes; unchanged
broad suites are reused explicitly, not reported fresh. Frozen inputs:
4050; copies: 2990. The separately dirty real
tools sibling is preserved. Tools commit:
`e8744c25b841522591420e623ad689da3289abab`. Baseline consumer:
`af2274ce6f593648ddb77230dc96d08fb70e4050`. Receipts:
`conker/build/game-display-sprite-slot-15179600-private`.

Zero Claude calls or subagents: local source screens and explicit register
derivation settle this routine. The historical generated host target remains
an empty stub, with active host implementation unqualified. No host transfer,
build, launch, Release change or push. Scoped Graphify refresh audits all nine
owner definitions, retains old IDs/qualification metadata and observes actual
hook termination; no full-corpus extraction claim. README receives aggregate
rows/date only. Continue toward 90% from the sealed checkpoint.
