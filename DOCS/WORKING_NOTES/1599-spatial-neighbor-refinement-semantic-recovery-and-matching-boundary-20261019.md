# Spatial Neighbor Refinement Recovery And Matching Boundary

Superseded by [Note1600's installed complete match](1600-spatial-neighbor-refinement-complete-match-20261019.md).
The measurements below describe the earlier experimental checkpoint.

Verified: 2026-10-19. Complete experimental **func_15086098** is recovered,
with descriptive local names and its address-based export. **It is not
installed or byte-exact.** VA15086098..15086364, ROM B3548..B3814,
generated_B3020,179 retail words/716 bytes/frame112. Consumer predecessor
32dfec80; tools predecessor557a160. Tools checkpoint **94acbb1** banks the
three new files before the consumer documentation/tools pin. No push.

The selected primary body emits **176 words/frame112 with164 differences**.
The full routine fits with12 trailing zero bytes, but those bytes are not a
solution to the missing instructions. A fired first-access gate proves the
private save layout still differs. Production source, assembly, guards,
Makefile, ELF, ROM, progress CSV and root README remain unchanged. No new
guards, production build or matching credit.

## Recovered Interface

The complete routine and three aligned ROM JALs establish seven arguments:

```c
s32 func_15086098(f32 x, f32 y, f32 z, s8 count, s8 option,
                  u8 *list, u8 *state);
```

O32 carries x/y in F12/F14, z bits in A2, and count in A3. The callee saves
the full count word and reads its signed low byte. IncomingSP+10/+14/+18
hold option/list/state; option likewise uses its signed low byte. Count,
option and the helper's height band are not interchangeable with unsigned
bytes. The result is a **full32-bit index**, with255 as the sentinel. Do not
truncate helper results128,256 or-1 to a byte. Raw band words128 and255 are
passed unchanged in the outgoing word even though the typed callee observes
a signed low byte.

The experimental owner also corrects **func_15086C70** from `void` to `s32`
and returns func_150A3194's value. Retail leaves that full V0 live and this
parent consumes it. The correction emits the same20 instructions under both
full-owner profiles and matches the original80-byte wrapper. It is not yet
installed. Do not cast a void function pointer or silently discard its result.
Keep the unfinished func_15086364/FIND providers separate from this recovery;
no implementation or matching credit is claimed for them.

## Recovered Behavior

1. Always call height-band helper func_15085DA8(y), then closest-node helper
   func_15085DF8(x,y,z,0,band). Preserve their effects. Return its full index
   unchanged when signed count<=0 or index==255.
2. Query func_15086C70(index). If its nonzero record passes func_150A32B4
   with truncated integer XYZ, call func_15086364(index,count,option,list,state).
   Accept any full-word result other than255 through the final override.
3. Otherwise reload D_800D2350 after those helpers, cache its16-byte record
   table and D_8009D9D0, read unsigned node radius byte8 and compare threshold
   against the squared doubled radius. The true branch uses the same direct
   refinement/override path. Retail threshold bits4CBEBC20 equal100,000,000;
   a byte radius cannot reach that branch with the frozen value. Controlled
   mutable-data fixtures cover it without changing production constants.
4. Scan **all five** neighbor bytes9..13.255 skips one entry; it does not end
   the scan. Read signed16 X/Z coordinates, normalize neighbor-current with
   reciprocal square root, and project the supplied position onto the forward
   line. Require projection>0; there is no segment-end clamp. Use float32
   rounding after each operation and retain the first strict distance minimum.
5. If a neighbor wins, refine the **original index**, not the winning index.
   Accept that result only when it equals the winner. Preserve list/state
   pointer order, aliases, helper effects and the final255 override rule.

## Qualification

The eight focused recovery tests pass in57.034 seconds without skips:

- 103 fixtures/two stack phases produce206 completed retail/raw pairs against
  an independently structured reference. Compare full-word results, complete
  public buffers, helper argument/order transcripts and ordered stores. Cover
  signed/high-word byte inputs, full-width results, every neighbor slot,
  signed/extreme coordinates, zero-length edges, NaN/Inf geometry, equality,
  ties, seven helper/global mutations and list/state/global-byte aliases.
- Native32 O0, O2 and O2+UBSan each execute all103 fixtures with no sanitizer
  diagnostics. Thirteen **compiled and effective** negatives reject narrowed
  initial/refined results, unsigned count, signed radius, non-strict radius/
  projection/distance tests, stop-on255, four neighbors, unsigned coordinates,
  accepting any refinement, dropped wrapper V0 and a stale early table base.
  Each exits21..25; compiler errors, signals and unmapped backing are not passes.
- Public fixtures visit175/179 retail words. Preserve the unsigned-conversion
  correction at150861A0/A4/A8 and dead duplicate minimum copy at150861F0;
  they were **not executed**. Do not claim full instruction-path coverage.
- Twelve connected retail/raw runs execute the actual20-word height helper,
  20-word record wrapper and31-word containment wrapper. They check signed
  bands2/128/255, the live record return and all seven float query-packet
  fields. The nested FIND and query providers remain opaque; this is not a
  claim that their complete behavior or the complete engine was executed.
- The aligned ROM scan finds JALs atA4AF8,C7B7C,C7E10. Forty-eight runs execute
  the real22-word1509A6A8..1509A6FC caller/result-consumer window and original
  five-word epilogue. Its480-byte frame is an explicit live-in. Check cached
  byte setup, seven argument words, returned index publication and the fresh
  node category lookup after helper effects. This is not full-script/gameplay
  acceptance, and its actual caller deliberately supplies count0.
- Three independent GNU maps rebase code, all11 bindings/five helpers,
  globals and backing, including HI/LO carries. Thirty retail/raw pairs agree
  with the public reference. No normalized byte-identity claim is made.
- Both whole-owner profiles preserve72 neighboring functions and all pools.
  The real production padder preserves all73 addresses, other padded bytes
  and extents, retains the exact record wrapper, and adds only the candidate's
  12-byte trailing gap. The seven expanded Make commands reproduce the same
  qualified objects in an ignored shadow. Only the pre-existing func_150891E8
  normal-profile override is used. No new build rule or guard is proposed.
- The private mismatch gate fires at access0: retail saves eight bytes at
  incomingSP-40; raw saves at incomingSP-56. Both use frame112. This disproves
  literal private/fault-prefix identity even on count0. It is not portable C
  fault behavior or a hardware/FCSR acceptance claim.

An initial negative narrowed the local index declaration to signed8, which
GCC correctly rejected under -Werror because comparing it with255 is always
true. That compiler failure was not accepted. Casting the helper result while
keeping the32-bit local gives the intended compiling control and exits22.
The user confirmed the earlier output-path-truncated `../Conkers` file was
disposable compiler scratch; no recovery was requested or attempted. The
candidate compiler uses the corrected quoted output-path handling.

Shared project tools checks and syntax checks of the three task files in
both tools copies pass. Only previously absent task paths were copied.
The older standalone mirror HEAD ddbdd16 and all1,380 pre-existing dirty leaf
hashes are preserved; no mirror commit, reset, stash or clean was performed.
No Claude call, REA setup, dependency
change, real-save change or frozen host Release operation was involved.

## Source Screens

All listed primary screens have empty compiler diagnostics. Differences
include length differences; a smaller count is not a private-layout proof.

| Form | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Initial complete body; register args; cached XZ; plane offset |184|160|172|
| Scoped locals; scoped register args |184|136|172|
| In-place normalized vector; negative-first expression |176|128|140|
| Selected compact; reused distance; register index |176|112|164|
| Compact outer object |176|120|139|
| Compact ternary return |177|112|164|
| Compact separate diameter |176|120|166|
| Compact named band |176|120|165|
| Inlined coordinate reads, outer object |176|120|139|
| Separate threshold/minimum; negative-first form |177|128|147|
| Separate threshold/minimum, inner object |177|120|173|

Initial/scoped controls also emit identically under the normal profile.
Scoping real locals, reusing normalized vector variables, in-place radius
doubling and nesting the height call recover frame112 without dummy locals,
volatile declarations or physical-register C bindings. Moving the record
temporary outward recovers index S0 but expands the frame to120. Ordinary
`register` hints do not alter the selected object. Algebraic negative-first
forms still compile a subtract rather than retail's separate NEG/ADD.

Selected raw SHA256:

```text
f6147adcdba5d18669188d2c4c187c5e3142bd8a567a0abf5c7407b2974f05d0
```

## Production And Resume

Fresh matching remains **Game3,009/4,832 (62.27%)**,
**total3,682/5,505 (66.88%)**,1,823 different/zero drift. Init492/492 and
Debugger181/181 remain exact; generated_B3020 remains61/73 exact with12
remaining. Conversion remains5,505/6,044 (91.08%),86.08% bytes. Root README
has no new narrative or aggregate change. The production ELF is unchanged:

```text
6dae1b0cfba38f03c17601e1b9afdecefcfbd03f8302c4db89501b04801ac0bc
```

Continue **the same function**, not a broad conversion batch:

1. Recover index S0 and the original saved FP/RA/S0 homes, selected home58,
   refined home60 and saved-register lifetimes while preserving frame112.
2. Resolve input X/Z F28/F30, minimum F26, projection F24, reused Y/base-Z F20,
   and the locally materialized1.0 instead of the raw hoisted F30 constant.
   Preserve the original otherwise-unused F22 save/restore, not a new C effect.
3. Recover threshold-to-minimum copy, signed-coordinate access schedule,
   separate base-dot NEG/current-dot ADD and the five-iteration SLTI backedge
   including its branch-likely copy and multiplication hazard slots. These are
   measured differences, not a validated normalization recipe.
4. Require a source-derived word/binding accounting, full private/fault-prefix,
   saved-role, caller, alias and GNU/padder qualification before new guards or
   installation. Then strictly predict the complete production image and
   preserve all neighboring bodies/addresses/data/guard history. Keep the
   wider Game goal active.

From64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_spatial_neighbor_refinement_recovery -v
python3 -m tools.experiments.game_spatial_neighbor_refinement_candidates --screens
python3 -m tools.experiments.game_spatial_neighbor_refinement_candidates --whole
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored frozen inputs, compiler screens, emitted objects, native programs,
receipts, helper/caller/GNU cases, shadow Make build, qualification log and
Graphify before/after audit live under
`conker/build/game-spatial-neighbor-refinement/`.
