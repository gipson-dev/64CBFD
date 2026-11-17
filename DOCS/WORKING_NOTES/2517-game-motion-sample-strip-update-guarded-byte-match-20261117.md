# Motion-sample strip update recovery and guarded byte match - 2026-11-17

`void func_151AD174(u8 *record)` now replaces the empty registered callback
with the complete strip update. Its **494-word / 1,976-byte retail slot and
frame 0x308 are byte-exact in production**. Semantic C emits 491 words;
**273 relocation-aware expected-word guards and three insertions** normalize
private homes, allocation and scheduling, with no omissions. The one earlier
guard preserving the empty placeholder is retired explicitly. All other
existing guard bytes retain their order and content. This is a guarded C
match, with no compiler-profile or shared-header change.

Accepted total is **4,533 / 5,514 (82.21%)**, Game **3,860 / 4,841 (79.74%)**,
Init 492/492 and Debugger 181/181, with zero drift and 981 different.
**154 further matches** are needed for the active 85% goal. Conversion remains
5,514/6,048 (91.17%), covering 86.19% of bytes. Root README receives only the
Total and Game aggregate-row updates. Prior ordered-FP recovery is
[Note 2516](2516-game-strip-update-ordered-floating-point-recovery-and-stack-frontier-20261117.md).

## Recovered behavior and ABI

Owner `conker/src/game/generated_1D92F0.c`; VA 151AD174..151AD92C,
ROM 1DA624..1DADDC. The protected 101-descriptor table registers this
one-pointer void callback at descriptor+4 for classes 0x2F and 0x4E.
The constructor's local 88-byte record and 24-byte sample views are reused
without altering shared struct179/struct180 headers.

The signed halfword countdown at +0x52 uses wrapped subtraction and a negative
clamp. The byte count is captured before the mutable providers. Owner/effect
updates retain unsigned child fields, four trig calls, vertical velocity
adjustment and countdown/amplitude reset, with the original record, owner and
buffer reloads. The independent impulse contributes two more trig calls and
decays its timer. Both twenty-by-three position/velocity snapshots are retained.

The reverse scan applies gravity9, damping0.96, double-precision1.24 smoothing,
the category0x39 X ceiling1150 and the constraint against the already updated
next sample. Ordered force products, subtractions, smoothing addition and
final constrained-position additions are recovered. The movement score uses
absolute velocity X/Z. The sound gate retains its unsigned handle/query,
unsigned RNG modulo9 plus0x507 and all eleven full-width submission arguments.
Coordinate narrowing occurs at the original conversion/provider boundaries.
No extra null guards or physics behavior is introduced.

## Explicit private normalization and complete relation

The source already reproduces all **648,522 ordered FP observations** in the
existing **544-case finite matrix**. Four private words remained: the gravity
square's home A0 versus84 and first force-input Y/Z spills B0/AC.

An anchor-checked transformation derives a 494-word intermediate directly
from the raw C instructions, without copying a retail body:

- Move the square store/load from SP+A0 to SP+84.
- Insert the two Y/Z spill stores and one Y reload; use an existing NOP for
  the Z reload before its force product.
- Restore the first norm's likely-delay branch, placing the existing division
  in its taken delay while retaining the zero-path division after replacement
  of the denominator. Rebuild all 25 internal branch targets after insertion.

The intermediate and retail agree in all mapped RAM and all **792 private-frame
and incoming-home bytes**, across 544 cases and **1,976 provider entries after
call delays**. Wrong square home, Y spill source, Z spill home and ordinary
rather than annulled zero-norm delay each reject.

The symbolic relation composes the existing 18-path opening and generic
snapshot row with **two gravity paths, 288 generic reverse-row paths, and
four audio/return paths**. The row checks the index, 12-byte snapshot cursor,
24-byte point cursor, retained coefficients and loop-live roles at backedge.
Every private byte, ordered public store, stable read multiset, FP operation,
ordered operands/control input and abstract FP-status transition agrees.
The suffix observes private frames after call delays, allows conforming opaque
provider effects/clobbers and proves saved-register/frame restoration.

An independently renamed T6/T7 allocation passes all three new phases. Five
effective controls reject wrong square home, point stride, likely-delay form,
multiply operand order or audio volume. Entry/snapshot retains its six controls.
The guard mapping's two padded streams are independently identical to retail,
closing the composition.

The contract is normal nontrapping execution with mapped disjoint record,
point buffers and private frame/snapshot views, count0..20 and row0..18,
and conforming opaque providers. It does not assert literal fault-register
state, arbitrary stack aliases, cycle timing, hardware or host gameplay.

## Qualification

All **five pre-install tests pass fresh in both tools configurations**:
436.950s primary and 432.384s overlay/sibling, including fingerprints/imports.

- Both real padders preserve all 32 neighbors and pools. Original assembly
  and both objects agree through **12 GNU links**, with four code layouts
  and independently relocated data/call symbols, including HI16 carries.
  All 23 original bindings are covered.
- **514 raw-word/binding corruptions**, **1,092 stale CSV controls** and
  **279 replacement/insertion controls** reject. All 273 rows are pinned.
  Remove the old placeholder guard by exact bytes; preserve every other row
  before appending the qualified rows.
- **544 cases per retail/raw/intermediate/strict/layout stream** compare public
  bytes, complete calls, coefficient reads and preserved registers. Normalized
  streams also agree in mapped RAM and provider frames. Coverage is489/494
  retail/normalized and486/491 raw.
- Exact selected SDK32 C passes O0/O2/O3 plus four effective score, timer,
  signed-countdown and smoothing controls: seven native executions, 544 cases.
  No native FP-status or hardware assertion is inferred.
- The original 74-word caller runs **64 cases per stream**, both classes/rows
  and depths0/3. Normalized mapped RAM/private stack agrees; caller coverage
  is73/74 and a wrong callback-pointer control rejects.

After installation, a fresh owner compilation and **two fresh production
execution checks** run guest544 and caller64 cases across six streams,
including the actual production ELF. The unchanged object/rebase/proof/native
gates are explicitly reused by task/input and fixture fingerprints, rather
than described as fresh repeats. Source/ABI/owner checks remain enforced.

## Strict production adoption

Baseline consumer **df6254fc**, tools **dadc7ed**. The **1,525-input** snapshot
uses 1,517 immutable prior-snapshot links and eight copied task files, with zero
live-worktree hardlinks. Real shadow Make and production Make compile the C;
no prebuilt object is installed. Exactly source, guard CSV, owner object and
ELF change; **1,521 frozen inputs remain unchanged**. Only one of 698 objects
changes. All 32 neighbors, all other **6,050 bodies** and all **6,051 function
addresses** remain unchanged. Pools and register metadata stay qualified.

Every ELF byte equals the independent prediction: **1,687 changed bytes,
zero exclusions**. All **20,289 named definitions** agree except target size.
Five serialization groups containing thirteen names account exactly for
symbol/string ordering; they are predicted bytes, not excluded ranges.
Named-symbol, symbol-name, protected-data and target-word corruptions reject.
All **189,088 protected bytes / 720 owners** remain exact. Recount,
match-progress and shared tools checks pass. The generated_12D630 duplicate
recipe warning is pre-existing; this is not a warning-free-build claim.

Production ELF SHA256:
`9a3fca4a18c45119a77ad987895ba93c8f600ab46acbad5513147499567074b3`.
Selected raw SHA256:
`d3408ea6ebd5cbbbf188e34aecbf49e0c6ea6b39ab389091e7ad4d20ddaf8c9b`.
Run `python3 -m unittest tools.tests.test_game_strip_update_151ad174_match -v`
with a fresh owned `CBFD_STRIP_UPDATE_MATCH_WORK` path. Receipts, actual imports
and declared post-install reuse remain under the ignored
`conker/build/game-next-151ad174-private/adoption-final/` packet.

The sibling's 2,434 dirty paths and 339 scoped dependencies remain untouched.
The host path has diagnostic folders only; no host source, Release or save
changes are made. No additional Claude call is used. Graphify retains prior
IDs and an explicit tools-to-function reference through a scoped AST refresh;
this is not a full-corpus re-extraction. Commit tools before consumer.

## Next callback

Read-only discovery identifies **func_151AD92C**, 464 words / frame0x130,
VA 151AD92C..151AE06C, ROM 1DADDC..1DB51C. The same two descriptors register
it at+8, and it has one direct call. Its zero-return placeholder remains.
Next establish the draw caller/ABI and recover vertex/display-list behavior
with the accepted strip views, then qualify independently. Discovery gives
no conversion or matching credit.
