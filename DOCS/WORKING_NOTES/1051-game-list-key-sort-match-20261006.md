# Game List-Key Sorter Match

Date: 2026-10-06. Starting checkpoint: `b2ad7289`.

Recover `func_151406AC` in
[game_169510.c](../../conker/src/game_169510.c): **72-word body plus one
trailing nop / 73-word slot / 292 bytes**, VA0x151406AC..0x151407D0,
ROM0x16DB5C..0x16DC80, leaf frame **0x138**. Replace the false no-argument
zero-return C placeholder. Existing O2/g3 emits **54 body words directly**;
18 exact expected-word guards normalize three bounded pointer-register
lifetimes. The complete body and trailing nop then equal the
[unchanged retail reference](../../conker/asm/nonmatchings/game_169510/func_151406AC.s).
No new profile/shared header/data/symbol/layout or broad conversion batch.
Production linking/audit and the 83-test post-link regression pass.

## Recovered Contract

Returned signed-word identity token, unsigned column/row address arithmetic,
signed-halfword bypass. Nonzero low halfword returns the token without table
access, regardless of high incoming bits or invalid column/row values. Zero
bypass selects `D_800DCE50 + row*0x1A0 + column*4`. Owner-local prototype
recovered; no shared callback signature/table declaration change.

The private dummy occupies 0x110 bytes at SP+0x28. Its kind byte +0x18 and
signed value word +0x20 are zero, next +8 receives the initial head, and
head->prev +4 is set to the dummy. The opaque tail represents the local
frame footprint, not a claim that every allocated node has this size.
Sort the doubly linked list stably by
`(unsignedKindByte<<8) + (signedValueWord>>16)`. Capture each current node's
previous and original next pointers and key before walking backward. Equal
keys stop the backward search, preserving arrival order. On movement, keep
the captured unlink successor, then **reload current->next and current->prev**
for the successor repair. Capture insertion-point next once, publish it in
current->next, repair its prev, then publish current's prev and insertion
point's next in retail order. Advance using the original captured successor.
Finally publish dummy.next to the global root, clear that head's prev and
return the original token. No callbacks, allocation, graphics output or
invented pointer-return API.

Do not add cycle guards, empty-head fixes, sentinel-prev initialization or
key/index clamps. Retail **stores head->prev in a branch delay even when head
is null**, and its zero-key dummy has uninitialized prev. Valid-list tests use
nonnegative combined keys; negative signed high halves are allowed where the
kind component offsets them. Arbitrary negative combined keys can walk past
the dummy into uninitialized storage. A strict bounded guest model verifies
the observed failures, not native execution of undefined-input C.

## Compiler Evidence

[Persistent driver](../../tools/experiments/game_list_key_sort_candidates.py):
**six forms x four profiles = 24 controls**, real SDK integer/pointer layout,
fixed table anchor, empty diagnostics. Selected O2/g3: **72/0x138/18**
(words/frame/differences); plain O2: 72/0x138/26. O1/g3:102/0x130/102;
O1:101/0x130/100. Inner/outer for loops retain 18/26 O2 differences but alter
O1 body lengths. Loop-local or next-local declarations add one O2/g3 word and
give 27 differences; plain O2 remains 72/26. Shrinking the dummy tail gives
frame0x58 and 21/27 differences; O1 frame0x50. The retail-size dummy and
captured/live pointer lifetimes are required; no alternate profile installed.

Earlier ignored controls: 100 initial forms, 32 loop/scope/register controls
under `game-basis-quad-builder/next-sort/`, then 16 insertion-temporary controls
under `game-list-key-sort/`. Separating insertion temporary or changing its
word/pointer spelling does not improve the selected 18 words; block-local
insertion adds a word, next-first insertion shortens the body and shifts it.
These are compiler evidence, not alternate production bodies.

The guard test reconstructs every replacement from explicit register-field
maps, retaining opcodes, immediates, branch targets and operand ordering:

- Captured outer successor: raw T0 becomes retail A3 through the loop backedge;
  pre-unlink live temporary: raw A3 becomes retail T0. The capture move binds
  both sides of the exchange.
- Post-unlink insertion successor: raw A3 becomes retail T7, a distinct lifetime
  after the earlier temporary is dead. No cached-successor substitution.
- Final dummy-head publication: raw T7 becomes T9; second live head load uses
  raw T9 versus retail T3. The early branch-likely load feeds this same final
  publication path and is guarded consistently.

Exactly 18 guards, no relocation changes/insertion/omission/trampoline;
**55 of 73 slot words** (54 instructions plus trailing nop) emit unchanged.
Frame, argument truncation, arithmetic, loads/stores, branch-likely behavior
and ordering already match before normalization.

## Qualification

[Eight tests](../../tools/tests/test_game_list_key_sort_match.py):

- Complete 72-word raw body/frame and 18 register-only rewrites; all normalized
  73 slot words equal retail, including the unreferenced walker instruction.
- **5760 valid-list guest cases / two raw bodies**: lengths1..12, eight ordered,
  reverse, duplicate, zero, mixed kind/signed-value and equal-combined-key
  patterns; columns0/27/28/86/103, both rows, three tokens and two stack phases.
  High incoming bypass bits with zero low halfword still sort. Independent
  stable Python sorting verifies the entire node/table/guard footprint, not
  only traversal order. Ordered external reads/writes agree; saved GPR/FPR/
  SP/RA and no-call behavior checked. **69 words** covered on sorting paths.
- **65535 nonzero bypass guest cases / two raw bodies**: high incoming bits,
  invalid column/row, alternating stack phases, token return and zero external
  accesses. With sorting, **71 reachable body words** covered; the unreferenced
  load at VA0x1514079C is not artificially executed.
- Strict guest empty-head fixture faults on the exact write `(address4,size4)`.
  Negative combined-key fixture walks uninitialized dummy prev and faults on
  the exact byte read at 0xA5A5A5BD. Both raw bodies reproduce these preconditions;
  this does not claim guest device/exception/hardware behavior.
- All 24 persistent compiler controls and empty diagnostics.
- Eight compiled negatives: stub, descending comparison, unstable equal keys,
  unsigned value shift, missing final head-prev clear, missing successor-prev
  repair, wrong row stride and full-word bypass. Memory/return differences
  detect seven; reversed comparison's invalid sentinel walk must fail the
  exact mapped-memory contract, not an unsupported-instruction assertion.
  Positive equal-key fixtures detect instability before a zero-key sentinel
  failure can mask the intended observation.
- **960 native full-storage ordering cases**, lengths1..12/eight patterns/five
  columns/two rows. Actual selected C, independent array-selection reference
  with ordinal tie break; entire 3456-byte guarded node storage and 832-byte
  table checked. Pointer4/halfword2/dummy0x110/kind0x18/value0x20 layouts checked.
- **65536 native signed-value-high-half cases**, two nodes, kind128 ensures a
  nonnegative combined key; varying ignored low word bits. **65535 native
  nonzero bypass cases**, invalid row/column, unchanged complete storage/token.
- Production body/prototype/type/complete slot and exactly18 guarded rows;
  callback references in the retail table retain entries28/86.

This is finite ordinary valid-list qualification, not every alias/corrupt
list, upstream callback, native undefined-input behavior, hardware exception,
dispatch-chain/gameplay or sibling host acceptance. No tests install a null
or cycle safety workaround.

## Linked Audit

Build/link/progress pass. Only target changes across **6059 function slots**;
all addresses/sizes fixed. Target SHA-256:
`4d59c23fd994aede10bfad7e7a1fda13a47272854dd2859e92a29f886237bbfc`.
Protected `.init`, `.init_data`, `.debugger`, `.game_data` unchanged;
**720 owners / 189088 bytes** remain retail-exact. **10667 existing guards**
preserved in order plus18, current total**10685**. All **45 preexisting owner
warnings** identical after shifted-location normalization; **zero new**.
Constructor, corner/attribute helpers, both recent quad builders, owner wrapper
and actual buffer backend remain unchanged and retail-exact. No warnings in
the recovered sorter; existing generated_12D630 recipe warnings are unrelated.

Converted totals remain **5464/6042** and Game**4791/5321**, bytes**85.57% total /
84.89% Game**, because this false stub was already counted as C. Exact totals
now **3329/5464 (60.93%)**, Game **2656/4791 (55.44%)**, **2135 different**,
zero drift; Init492/492 and Debugger181/181 unchanged. README receives only
aggregate numbers. Tools/compileall/diff checks pass; **33 docs / 3365 relative
links / zero broken**. All **83 post-link regression tests pass in 839.818
seconds**, with no skips; the suite includes this sorter's eight tests,
retained geometry/effect/allocator recoveries and five word-patch relocation
tests.
Six older tests advance only global guard totals; own contracts stay unchanged.

Ignored receipts: `conker/build/game-list-key-sort/measurements.json`,
`audit.json`, `after.json`, starting from the basis-builder `after.json`;
behavior/negative/native objects under `game-list-key-sort-test/`.

## Cross-Project Boundary

Read-only sibling source inspection finds `64CBFDOGL/recomp_out/.c` already
contains retail-translated `func_151406AC`, with host-only inner/outer cycle
guards and diagnostics. It is **not a false zero-return placeholder**.
Its old comment reverses +4/+8 link labels; the actual guest instructions use
prev+4/next+8 as recovered here. Preserve those host safeguards; no mechanical
guest-C import or regeneration. File evidence is not active executable/
dispatch/runtime proof. No sibling source/build/save/frozen Release changes,
runtime launch or push.

## Next Work

Adjacent `func_151407D0` in `game_16DC80.c`: **53 words / 212 bytes**, frame
0x40, VA0x151407D0..0x151408A4, ROM0x16DC80..0x16DD54. Current no-argument
zero-return stub is false. Retail takes source pointer, byte count, descriptor
pointer, five byte selectors (one signed byte), channel and context. Mutate
descriptor byte+1 to3 and OR flags+0x40 with0x40400000 **before allocation**.
Forward the recovered argument transport to `func_1513D524` with setup=1;
on success copy source to result+0x110 using live original arguments, then
clear payload word+0x44, set signed selector byte+0x59, increment live
`D_800DC9F0` and return allocation. Allocation failure returns null but retains
descriptor mutations. Preserve source/descriptor/payload alias behavior and
post-copy counter read. `func_1513D524` currently has a false void C signature;
recover its pointer return and verify unchanged wrapper instructions before
connecting the native chain. No next-function body installed yet.

Bounded ignored compiler screen: **128 controls** (24 initial forms/profiles,
24 return/source type controls, 40 flow/payload controls and 40 finalize
controls), all completed with empty diagnostics. Ordinary structured C gives
54 words/frame0x40/19 differences, including an extra branch-likely return
word. Explicit success-to-finalize control flow gives **53/0x40/10** under
the existing O2/g3 profile, with the opening 27 instructions direct. The
remaining region changes independent stack loads/stores and counter-address
setup across the success join; branch offsets differ with that placement.
No next-function guards installed or equivalence assumed. Early-null gives
53/0x40/17; payload/return typing and volatile controls do not improve the
best ten-word candidate. Ignored receipts/scripts are under
`conker/build/game-list-key-sort/next-payload*`. Next qualify that candidate's
two raw bodies and allocation/copy aliases, then recover the wrapper's return
ABI and prove its 28-word slot unchanged before a separate installation.
