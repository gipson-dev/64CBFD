# Game Basis-Vector Quad Builder Match

Date: 2026-10-06. Starting checkpoint: `4030388b`.

Recover `func_15140410`, **167 words / 668 bytes**, VA
0x15140410..0x151406AC, ROM 0x16D8C0..0x16DB5C, frame **0x68**, in
[game_169510.c](../../conker/src/game_169510.c). Replace the false four-word
arguments/zero-return C placeholder with a semantic basis-vector quad builder.
Existing O2/g3 emits **165 words directly**; two expected-word guards swap
independent width and height-vector-pointer loads. No new profile/shared
header/data/symbol/layout or broad conversion batch. The
[retail reference](../../conker/asm/nonmatchings/game_169510/func_15140410.s)
is unchanged.

## Recovered Contract

Actor byte pointer, two three-float basis-vector pointers, signed-halfword view;
return the original allocated vertex pointer. Call
`func_151D5D60(actor+0x100, view, 0x40, &cursor, &fresh)` and capture the
original cursor. Null returns before any basis reads, indexed-slot accesses,
copies or vertex writes, including fresh=255. A fresh allocation copies the
actor+0xC0 template twice, into the live indexed actor+0x100 buffer slot and
its +0x40 half. Reload that slot after the first copy. The escaped cursor can
also be redirected by a callback; original-pointer return is independent.

Capture all six scaled basis components before output stores:
actor width +0x2C times widthAxis[0..2], actor height +0x30 times
heightAxis[0..2]. Four vertices use signs (+,+), (-,+), (-,-), (+,-).
For each coordinate, read actor translation +0x34/+0x38/+0x3C **live**, then
evaluate `(translation +/- scaledWidth) +/- scaledHeight`, rounding each
single-precision operation independently. Truncate to signed 32 bits and store
the low halfword, then clear each vertex flag. All twelve translation reads
remain live; do not snapshot them before aliasing writes. Captured components
do not change if output overlaps the basis vectors. Texture/color bytes remain
as copied or untouched on an existing buffer. No clamp/saturation/index fix.

The owner wrapper `func_1513F4B0` supplies actor+0x110/+0x11C basis pointers.
Recover the owner-local prototype and cast its three pointer arguments;
the wrapper's **13 words** remain unchanged and retail-exact. This removes
exactly its three Warning 712 pointer/integer diagnostics. Three other live
cross-owner callers retain their existing word ABI and untouched sources;
this does not claim qualification of every caller or a shared-header change.

## Compiler Evidence

[Driver](../../tools/experiments/game_basis_quad_builder_candidates.py):
**six forms x four profiles = 24 controls**, real SDK types/fixed backend and
copy anchors, empty diagnostics. Selected O2/g3: 167 words/frame 0x68/two
differences; plain O2: 167/0x68/eleven. O1 variants: 210/0x48/209.
Components-first multiplication introduces six commutative operand differences
(eight total O2/g3, seventeen plain O2). Named width/height scalars give
167/frame 0x70/31 or 35 differences; O1: 208/frame 0x50/208. Moving fresh
before the component declarations gives four or twelve differences; early
null return shortens to 165 words and gives 148/157 differences. A byte-output
form reproduces the selected result. No alternate profile/instruction body
was installed. Earlier 44 ignored preliminary controls remain in the prior
cached-quad receipt directory.

Only **0xA4/0xA8** differ: raw `C600002C,8FA30070` versus retail
`8FA30070,C600002C`. Load the actor width into F0 and the height-vector pointer
from private SP+0x70 into V1. Same two loads/registers, no dependence, call,
branch or relocation. The private frame does not alias caller-owned actor
storage in qualification; no MMIO/concurrency/stack-alias claim. Two exact
expected-word guards swap this independent schedule. All other 165 words,
frame, saved-register/F20/F22 lifetimes, multiply orders, conversion/store
order and return emit directly. No insertion/omission/trampoline.

## Qualification

[Nine tests](../../tools/tests/test_game_basis_quad_builder_match.py):

- All 24 compiler controls, complete 167-word shape and exact two-load swap.
- **1728 guest cases / two raw bodies**: six incoming view patterns including
  signed/high-bit transport, fresh 0/1/255, null/success, copy mutations, four
  output aliases, three basis relationships, two stack phases. Independent
  sequential byte reference checks complete external storage and original
  return; ordered external accesses/calls match retail. All 167 words covered,
  saved GPR/FPR/SP/RA checked.
- **324 actual-backend guest cases / two bodies**: existing/new/failed buffer,
  flip 0/1/255, allocation-time flip mutation, three views/basis relationships,
  two stack phases. Execute actual 52-word `func_151D5D60`; allocation checks
  `(128,1,2,1)` and live post-allocation ping-pong selection. Copy providers
  mutate slot, basis/translation and escaped cursor. **218 reachable chain
  words** covered: its optional null-fresh-pointer store at backend+0x34 is
  unreachable because this caller passes a non-null fresh pointer.
- **198 guest float cases / two bodies**: fractional/signed zero/dimensions,
  large finite values, independently rounded additions and low-halfword wrap;
  finite signed-32-bit conversions only.
- **144 actual-owner-wrapper/backend guest cases / two bodies**: embedded
  actor basis vectors, four view patterns, three allocation outcomes, three
  flip values, mutation and two stack phases. Complete memory/traces and
  wrapper call contract; **231 reachable words**, not all 232 nominal words.
  The wrapper remains void; no invented pointer-return API claim for it.
- **576 native full-storage cases**: actual selected C, bounded providers,
  independent native-endian reference, entire actor and four guarded 160-byte
  arrays checked. Four signed-view patterns, three fresh values, null/success,
  mutations, output/actor/basis aliases. Backend fixture is noinline to keep
  escaped cursor opaque to GCC; production statements are unchanged.
- **65536 native null cases**: every signed-halfword view pattern, fresh=255,
  null basis pointers, no indexed-slot/basis/copy accesses. Native pointer4,
  halfword2, float4 and SDK-equivalent Vtx16 layouts checked.
- Eight compiled negatives reject stub, lost flags, grouped additions, eager
  translation snapshot, live component recomputation, stale slot, changed
  return and wrong backend size. First seven differ in actual memory/return;
  wrong size must fail the exact backend contract, not unsupported opcodes.
- Production source/local prototype/owner casts/full retail slot/backend;
  exactly two target guards and normalized complete words equal retail.

Allocation and SDK memcpy remain bounded providers. This is not full SDK,
hardware FCSR, NaN/infinity/out-of-s32 conversion, gameplay or host acceptance.
Aliased fixtures use finite ordinary storage, not arbitrary private-frame
aliasing or concurrent/device memory.

## Linked Audit

Build/link/progress pass. Only the basis-quad slot changes across **6059
function slots**; all addresses/sizes fixed. Target SHA-256:
`46cbfb4aac12b25496b679ce199c88b6d773990c9005e24e9962c6be8629b45b`.
Protected `.init`, `.init_data`, `.debugger`, `.game_data` unchanged;
**720 owners / 189088 bytes** remain retail-exact. **10665 existing guards**
preserved in order plus the two loads; current total **10667**. Owner diagnostics
drop from 48 to **45**: exactly three expected Warning 712 removals, all other
warnings identical after shifted-line normalization, **zero new**. Owner
wrapper/backend/constructor/corner/attribute/prior quad slots unchanged.

Already counted as C, so converted totals stay **5464/6042**, Game
**4791/5321**, bytes **85.57% total / 84.89% Game**. Exact total now
**3328/5464 (60.91%)**, Game **2655/4791 (55.42%)**, **2136 different**,
zero drift; Init492/492 and Debugger181/181 unchanged. README receives only
aggregate numbers. All **75 focused post-link tests pass in 765.095 seconds**,
no skips; **32 docs / 3353 relative links / zero broken**. Tools check,
compileall and diff check pass. Five older tests advance only their global guard
count to 10667; their own guards/contracts are unchanged.

Ignored receipts under `conker/build/game-basis-quad-builder/`: 24-control
`measurements.json`, `audit.json`, `after.json`, starting from
`game-cached-quad-builder/after.json`. Behavior/native/negative/owner/backend
receipts under `conker/build/game-basis-quad-builder-test/`.

## Host Boundary And Next Work

Read-only sibling inspection finds generated `64CBFDOGL/recomp_out/.c`
still contains `func_15140410`'s false zero-return reference body. No scoped
native source override was found. This is file evidence, not current
executable or active-dispatch proof. Host regeneration/adoption needs its
own task; no mechanical guest-C transfer into the recomp context.
No sibling source/build/save/frozen Release change, runtime launch or push.

Next inspect adjacent **`func_151406AC`**, VA0x151406AC..0x151407D0,
ROM0x16DB5C..0x16DC80: **72-word body plus one trailing nop / 73-word slot**,
frame **0x138**, leaf routine. Current no-argument zero-return C stub is false.
Retail accepts a returned identity token, column, row and signed-halfword
bypass. Nonzero bypass returns token without table access. Otherwise it uses
`D_800DCE50 + row*0x1A0 + column*4` and a stack dummy node to stably sort a
doubly linked list by `(kindByte<<8) + (signedValue>>16)`. Preserve captured
current key/next pointer, repeated live predecessor/successor reads, store
order and equal-key stability. **Head->prev=&dummy executes in a branch delay
even for a null head**, and final head->prev=0 likewise assumes non-null.
Dummy key is zero and its prev is uninitialized: determine upstream head/key
invariants before qualifying normal C, particularly negative keys. Do not
invent a null-safe path, sentinel initialization, index clamp or field name
semantics. Existing table is declared byte storage, two 0x1A0 rows, not a
confirmed shared node layout. No next-function candidate installed yet.

Follow-up bounded screen under `game-basis-quad-builder/next-sort/` completes
**100 controls** (25 forms/four profiles). A 0x110-byte dummy and separate
captured-next/live-temporary variables recover the **72-word body, frame
0x138**, with 18 remaining O2/g3 differences (plain O2: 26). Reuse the initial
head variable as the insertion cursor and compute the current key after the
predecessor/next captures. Best source is `reuse-key-late-o2g3.c`; raw body
remains non-matching, no guards installed. Other source forms range from
70..74 O2 words and from 0x58..0x140 frames. O1 controls are longer/worse.

Preliminary independent stable-sort reference checks **864 valid-list cases /
two raw bodies**: lengths 1/2/3/4/6/12, six ordered/reverse/duplicate/zero/mixed
key patterns, both observed callback columns 28/86, both rows, three returned
tokens and two stack phases. Complete node/table bytes and ordered external
accesses agree with retail. **65535 nonzero bypass cases / two bodies**, with
high incoming bits and invalid column/row values, return the token without
external access. **71 reachable body words** covered; the unreferenced walker
load at VA0x1514079C is not artificially executed. This is not native,
invalid-list, dispatch-chain or production qualification. The updater accepts
nonnegative combined keys in these fixtures, including negative signed value
halves offset by kind=128; arbitrary negative combined keys remain outside
the tested sentinel contract.

Read-only dispatcher inspection of `func_151674F8` establishes the observed
table-callback route: it checks the row/column head at VA0x151675F8 before the
callback at VA0x15167784. The two `func_151406AC` entries are at table addresses
0x8008BA6C/0x8008C634, offset +0x14 of 0x34-byte entries 28/86. This explains
the observed route's non-null gate, not every possible callback caller or
all upstream key values. Next: narrow the 18 words, qualify native sorting,
negative controls and actual dispatch/provider boundaries before installation.
