# Cyclic Weight Profiles Complete Match

Verified: 2026-10-19. **func_1508BC20 is installed and all189 linked words
are byte-exact**, including its136-byte frame and756-byte slot.
VA1508BC20..1508BF14, ROM B90D0..B93C4, generated_B3020.
Consumer predecessor01ab9b25; tools predecessor342de47. Tools checkpoint
**d3b35eb** banks the five new qualification files before the consumer
source/Make/guards/docs/tools pin.
No push. The wider Game goal remains active.

This is a **guarded match, not direct compiler identity**. Complete semantic C
under the normal O2/g3 profile emits188 words/frame136 with167 positional word
differences. All188 source words and six bindings are retained; one early
return-address-load copy restores189 words. The188 expected-word guards include
156 identity checks and32 schedule/home/relocation changes. No ROM word-array
replacement, omitted source operation, dummy local or physical-register C
binding is used.

## Recovered Contract

The actual caller at ROM B7124/VA15089C74 ignores the routine's return register.
The recovered interface is **void func_1508BC20(void)**, not the false s32
zero-return placeholder. Descriptive count, row, position, direction, weight
value/delta and scratch names preserve the address-based export. A short source
comment also identifies the inclusive RNG endpoint's unchecked index.

1. Capture signed-byte D_8008FD8C and the initial D_800D23B0+15B4 byte-table
   base before any helper. Compute step170/max(2,count>>1). All256 signed-byte
   inputs produce a divisor2..63, so the original unconditional signed DIV
   cannot divide by zero or overflow. Count<=0 makes no RNG calls or public
   weight stores, but retail still performs the division and private step store.
2. For every positive-count row, reset direction-1, value85 and delta=step,
   then clear exactly16 scratch bytes. Take two separate RNG samples: truncate
   sample1*float(count) for the initial index, and choose direction+1 only
   when sample2 is strictly greater than0.5. Equality and unordered NaN retain-1.
3. Search occupied signed scratch bytes in that direction, wrapping negative
   positions to count-1 and high positions to0. Mark the selected byte1. The
   scratch is cleared per row, not once for the entire table. Retain the search
   even where ordinary, in-range draws select an already-zero scratch byte.
4. Write count bytes in cyclic position order. Store value when signed value
   <256, otherwise255. Advance/wrap the position, add delta, and negate delta
   whenever the updated value>=256. Do not clamp the internal value or change
   the equality boundary. Advance the row base by16, not by count.

The count, table base and float count stay cached across both RNG calls and
all rows. Completed guest aliases overwrite the global count or context word
with weight bytes while later rows still use those original captures.

## Legacy Endpoint

The frozen RNG scale is **0x37800080**, not an exclusive-upper-bound scale.
Actual25-word func_150ADA68 with seed **0x15D45** updates the seed to
0x115D4FFFF and returns float32 **1.0**. There is no initial index clamp.

For count<=15, index=count still lies inside the16-byte scratch array, and
the routine can first write the byte just beyond the active count. At count16,
the emitted retail routine instead reads the **uncleared byte at SP+60**,
immediately after scratch SP+50..5F. Poison0 permits index16 and writes that
extra byte1, affecting later rows; poisonA5 forces a wrapped search. Both
behaviors, including the extra byte's persistence, are retained and guest-tested.

**This is not a portable C safety claim for the count16 endpoint.** The C
retains the unchecked16-byte legacy representation. No extra-byte initializer,
expanded scratch allocation or index clamp is invented as an original source
fact. Native fixtures reject any first-draw stream whose truncated scratch
index is outside0..15, including odd-length sample cycles; the rejection gate
itself is tested. Synthetic callback-written scratch masks are guest-only
controls, not claims about the real RNG or C access to another function's locals.

## Matching Recipe And Profile

The existing owner rule already compiles a normal-profile object for
func_150891E8. The Make change adds **only func_1508BC20** to that same
per-function selection. Every other function stays on its existing profile.
The normal object filters only the owner's no-unroll flag; no additional
compiler invocation, global flag change or unrelated override is added.

- Keep the compiler's matching136-byte frame, saved GP register allocation,
  remainder/four-record weighted-store loop and branch-delay updates.
- Move the proven-safe division/check block before the positive-count gate.
  Schedule the zero row initialization, float conversion/cache, scratch/end
  addresses and row's initial value/direction/step like retail.
- Recover the five private homes: float count40->48, constant step48->6C,
  saved row64->84, scratch68->50 and scratch end78->60. Saved GP homes18..3C
  and the frame extent remain unchanged.
- Recover the four-byte scratch-clear order, including its delay store. Rebase
  all crossing branches and convert the early BLEZ to BLEZL with a copied
  original LW RA3C in the delay slot, jumping past the common RA reload.
- Retain all188 unique source origins and six relocations. The inserted word
  is copied from the existing common epilogue RA load, not a new computation.
  Expected-word/relocation checks cover the156 unchanged words too.

An empty-count access12 control exposes why matching frame size is insufficient:
retail requests a step write at incomingSP-1C while raw requests an RA read at
incomingSP-4C. Both gates fire before the access. The normalized code restores
the literal original private/fault prefix, not portable C fault semantics.

```text
Normal raw: df73a3db75bc1d3e8d61487629cf1ea7dc9bcb7f3d80d9bc5c7c1bf56406cf06
Normalized: d679333ccc0f40f736ec6bb2092f3346336763b6263f96f35f0d88053a754666
```

Compiler controls have empty diagnostics. The selected/if-store forms are
117 words/frame152 under the primary no-unroll profile and188/frame136 under
normal. Explicit four-byte clear emits121/frame160 primary,209/frame112 normal;
cached float count emits188/frame144 normal. Array-last/row-first and explicit
do-row controls keep188/frame136 but do not solve the schedule. The simple
complete source plus qualified normal selection is retained.

## Fresh Qualification

**Eight installed tests pass in62.999 seconds**, without skips. The100-fixture
pre-install suite also passed all eight in80.120 seconds:

- 100 fixtures/two stack phases give200 completed retail/normalized/raw triples
  against an independent public reference. Compare all public bytes, helper
  calls and ordered stores. Retail/normalized also agree in every GP/FP/LO
  value, condition, private memory, requested access, event and visited-PC set.
  Raw agreement is public only; this is a void routine, not a result-value test.
- 1,386 confirmed own-access-cut pairs compare full retail/normalized states
  for empty, remainder, unrolled, occupied/wrapped and mutated-helper cases.
  Another32 fired endpoint cuts check all16 SP+60 reads with poisons0/A5.
- Fixtures visit182/189 retail words. Preserve the unvisited BREAK7 atBC8C,
  unreachable overflow check/slot/BREAK6 atBC9C/BCA0/BCA4, remainder saturation
  store atBDA4 and dead duplicate stores atBE70/BEB0. A maximum three-cell
  remainder starting85 with step<=85 cannot reach a saturated store. No claim
  that all189 words executed; all189 words match literally.
- Native32 O0, O2 and O2+UBSan pass88 explicitly backed fixtures. Include safe
  first1.0 draws for counts<=15 and larger-count zero-origin cases through127;
  these synthetic backed tables do not establish an engine-wide count limit.
  Fourteen compiling negatives exit21/22/23 for sign, divisor/budget, initial
  value, saturation/bounce equality, RNG calls, rounding/clamping, delta reset,
  stale/reloaded captures and row stride. Signals/compiler failures are not passes.
- Four additional compiling guest-only search controls reject non-strict
  direction, missing lower/upper wrapping and inverted occupancy. Multi-marked
  probes exercise repeated search iterations. The native safety gate rejects
  count16 first1.0 and an unsafe odd sample cycle while allowing backed count15.
- 194 stale raw-word/binding controls cover188 words and all six bindings.
  The quotient-domain proof checks every signed-byte bit pattern. Ninety
  composed runs execute the actual25-word retail RNG across counts1/4/16,
  five seeds and two poisons, comparing full public seed/table stores and
  literal private state. The current production RNG's100 bytes also equal retail.
- The aligned ROM scan finds one JAL atB7124. Thirty-six runs execute its
  actual23-instruction post-call prefix and stop at a confirmed pending read
  in the real24th instruction. The40-byte caller frame is an explicit live-in.
  Check the saved A0 halfword and five byte clears through freshly reloaded
  context pointers after callback mutations. No synthetic return path, full
  caller-return or gameplay acceptance is claimed.
- Three independently assembled/linked GNU maps give24 rebased raw/normalized
  pairs, literal retail equality, both global HI/LO carries and both RNG calls.
  Two completed count/context-publication alias triples preserve cached bases
  and count. Those overlapping guest regions are not native layout claims.
- Both whole-owner profiles preserve72 neighbors and all pools. The real
  padder preserves all73 addresses/extents except the target's declared size.
  Seven expanded Make commands reproduce the two selected normal functions
  and the qualified padded object. Four complete-image corruption controls
  and two actual padder stale-CSV controls reject changes.

Shared project tools and syntax checks in both copies pass. Preserve the
standalone mirror HEAD ddbdd16 and all1,387 pre-existing dirty leaf hashes.
Only five absent task files were copied; later native-gate edits affect only
those new task files in both copies. No mirror commit/reset/stash/clean.
Prior unchanged neighbor-suite receipts are reused, not freshly rerun.

## Installed Baseline

The complete production ELF equals the independently predicted first link:
**565 changed bytes =563 target-code bytes + two target-size bytes**.
Only func_1508BC20's symbol size changes12->756. No symbol-order adjustment
or whole-section exclusion is used. All6,056 other bodies and all6,057 addresses
are fixed. Protected Game data is189,088 exact bytes across720 owners, zero
differences. Original assembly, RNG/scale data and conversion CSV are unchanged.
The broad shared-manifest rebuild retains unrelated generated-code warnings;
the qualified target/owner compiler diagnostics are empty.

```text
Source: 55493079cdf8df8d1e59d06e0ccfd9fb983798529ff6c2a91dfb5b788760be74
Make:   6e6563d792c110f74f44d615c62f04e87430aa0c0e44b1bd7817ffd6d91a8063
Guards: 1511ad9a4d25fd2dd8835143b187edc5c224ec6e89272eb4c5a8b45a074a8043
ELF:    ac9821636fcdf152a879c87120645fbc265991065a2b2568e545fc0126dd14ba
```

Fresh matching: **Game3,011/4,832 (62.31%)**, **total3,684/5,505 (66.92%)**,
**1,821 different/zero drift**. Init492/492 and Debugger181/181 remain exact.
Owner **63/73 exact,10 remaining**. Conversion stays5,505/6,044 (91.08%) and
86.08% bytes. Root README changes only its two matching aggregate rows;
function narratives stay in docs. No Claude call, REA setup, dependency change,
real-save operation, host build or frozen Release operation was involved.

## Resume

Next: **func_15086D94**, existing C with207 retail words/frame144 and102
differences, VA15086D94..150870D0, ROM B4244..B4580. Freeze this installed
baseline, inspect the full routine/callers and match its actual interface and
lifetimes before another qualified installation. The other nine owner
nonmatches remain separate unfinished work. Keep the wider Game goal active.

```sh
python3 -m unittest tools.tests.test_game_cyclic_weight_profiles_match -v
python3 -m tools.experiments.game_cyclic_weight_profiles_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored compiler screens, frozen inputs, normalized/source-origin/private/
native/RNG/caller/GNU receipts, Make shadow, first link, production build/audit,
installed test log, remaining-owner inventory and graph audit live under
`conker/build/game-cyclic-weight-profiles/`.
