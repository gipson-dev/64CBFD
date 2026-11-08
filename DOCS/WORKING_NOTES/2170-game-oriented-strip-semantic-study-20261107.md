# Oriented-strip semantic study and compiler layout limits

Date: 2026-11-07. Continues [Note 2169](2169-game-bending-quad-match-20261107.md)
from consumer `b7941c91ed3de56364ab2a54ab1cd6c4eddf70e0` and tools
`0cedb5db35c9e2d7040c521f21b9667534d6350f`. This banks reproducible research
for the active 80% matching goal. **No Game source is installed and no new
matching credit is claimed.** README aggregate rows remain unchanged.

## Current source boundary

`Vtx *func_1513FAB4(u8 *actor,u8 alternateOrder,f32 *scale,s16 view)` is
recovered as complete semantic C in the tools candidate module. It queries
the per-view 64-byte vertex buffer, captures first separately, reloads the
destination between two template copies, and returns null on failure.

The routine scales width/height with two input floats, forms a displacement
from actor+40/+44/+48 minus center+34/+38/+3C, and computes its endpoint and
midpoint. The original cross product of that displacement with midpoint minus
viewer position supplies the width direction. Normalize it by
width/sqrt(dot(side,side)), or write positive zero for zero squared length.
Emit four xyz/flag records in either cyclic corner order, preserving texture
and color bytes, and return the captured first pointer.

The prototype repairs in both 17-word local wrappers remain part of the private
compiler input. Their code/bindings stay fixed. No shared header is changed.
The production callback remains its 12-byte zero-return placeholder.

| Property | Retail | Current C study |
| --- | ---: | ---: |
| Words |336|337|
| Bytes |1344|1348|
| Frame |152|128|
| Cross-call word |111|99|
| Bound word differences plus extent |0|314|

VA 1513FAB4..1513FFF4, ROM 16CF64..16D4A4. Both use RA/S0; there is no
matching normalization. The source overflows the retail slot by one word,
and its private homes/control allocation differ substantially. A one-word
length gap is not near byte identity. Raw SHA-256:
`99ccd0b08050604207ed8535f5b300d4a4decb6275c1e87f89d3db40db9ef672`.

## Reproducible checks

Four research checks pass freshly in both tools configurations:

* Complete predecessor/candidate owner compilations preserve 58 raw neighbors
  and pools. Five helper bindings are checked. Warnings fall 43->39 with zero new
  warning: four old pointer/integer argument warnings disappear at the two
  privately repaired wrappers. Raw shape and source round trips are guarded.
* An independent ordered model agrees with **587 retail cases** and **582 raw
  nonprivate cases**. Cover both orders/upper bits, signed views, five
  geometries, zero/parallel directions, negative/zero scales, exceptional
  casts, helper changes, cursor redirects, actor/template aliases and selected
  private-home mutations. Helper argument observations normalize private
  pointer roles while preserving input float words; they do not equate frames.
* **334 of 336 words execute**. A separate control-flow reachability walk,
  including likely annulment, agrees with dynamic coverage. Words 139/232 are
  duplicate likely-branch fallbacks matching delay words 126/148; both incoming
  paths bypass them. Callee-saved GPRs/FPRs, RA and SP remain correct.
* Native32 O0/O2/O3 each pass **503 cases**, with SDK Vtx16/pointer32,
  pointer/u8/scale-pointer/s16 leaf ABI, float sqrt return, checked argument
  words, trapping UBSan, round-to-nearest and no FTZ/DAZ. Six compiled controls
  reject with exit 1: stub, wrong return, missing flags, wrong normalization,
  wrong height scale and missing order. The normalization negative retains a
  width use so a compiler warning cannot substitute for a semantic failure.
  Distinct camera records and an additional wrong-record-return control check
  returned helper data even when the logged view argument remains correct.

Native cases use valid disjoint objects and finite representable s32 casts.
The guest model canonicalizes NaNs; it does not emulate hardware FCSR,
NaN-payload propagation or floating exceptions. Raw private/fault identity,
arbitrary stack-output aliases and complete caller-chain execution are not
qualified. Passing this study suite explicitly leaves adoption_ready=false.

## Original helpers and callers

All 95 original helper words compare against the banked ELF and ROM:
memcpy 11, buffer backend 52, handwritten cross product 19, viewer getter 13.
Selected cases connect their original instructions. The getter loads the
D_800DBFF0 pointer, indexes records by signed view*0x9A0, and returns +0x2F8.
The cross helper loads its inputs before writing output z,x,y. Its existing
handwritten assembly remains unchanged and receives no C-conversion credit.

The complete aligned-ROM census identifies three direct calls to FAB4 and
no entry/interior pointer to it. Existing caller slots compare across 85 words:

| Caller | Words | Call ROM | Renderer prefix slot |
| --- | ---: | --- | ---: |
| func_1513FA2C |17|16CF08|27|
| func_1513FA70 |17|16CF4C|28|
| func_151BE4B8 |40|1EB9F0|29|
| func_151B863C, calls FA70 |11|1E5B00|25|

These belong to the actual 39-entry prefix 22E8DC..22E978 used by the 295-word
renderer func_1513DB00. E7000000 afterwards is outside the pointer table.
The third direct caller validates an attached record, supplies live scaled
dimensions, and selects order 0. The renderer remains a production stub.
The separate func_151B863C C wrapper has an inaccurate return interface/no return
statement; repair it and execute all original caller paths before adoption.
This study inventories callers without claiming their runtime qualification.

## Source experiments and bounded review

No tested source fits both 336 words/frame 152. Endpoint arrays, scalar centers,
midpoint arrays/records, separated pointers, explicit normalization copies,
float-index/record views, declaration orders and f64 literal 0.5 controls are
retained in the ignored private directory. Equal counts can have different
raw hashes. The two explicit scalar-center orders are byte-identical; the
float-index and record views also produce identical raw bytes, neither a fit.

One bounded packet-only Claude review was attempted/completed through the
verified existing claude.ai/firstParty Pro route, with effective tools=[],
MCP=[], no tool use and no second writer. Packet SHA-256:
`46ee3a9aa5e835fb43ecda8aaca3998f238a6e57d6430a38c88938e66c9e3ea4`.
The suggested midpoint/endpoint conjunction overlaps an existing 358/frame 136
screen. Remaining order variants produce 358/136, 364/144 and 370/152, so none
fits. Reject the review's claim that the unused three-word band proves an
original vec3, and its claim that scalar endpoints recompute per vertex.
Those are unsupported/inconsistent with the captured endpoint source.

An independent IDO promotion probe gives leaf scalar/vector 14/19 words,
frames 0/16, and called scalar/vector 18/24 words, frames 24/40. Both vector
forms access stack slots; these probes do not show a wholly promoted vector
with an unused reserved home. The probe checker was corrected to find a
stack decrement after opening FP setup; checking only word 0 had misreported
the leaf-vector frame. This does not prove the origin of every retail gap.

## Banked boundaries and next action

Production source, headers, owner object, ELF/binary, guard history, Makefile,
ROM input, conversion CSV and README stay byte-identical to Note 2169.
This research does not run a production rebuild, append guards, alter the
conversion denominator or advance the match counter. Retained checkpoint:
Total 4239/5512=76.90%, Game 3566/4839=73.69%, Init 492/492,
Debugger 181/181, zero drift; **171 more** to 4410/80%.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regressions per copy are explicitly reused after exact fingerprints. An
overlay for the four new modules and recorded missing-helper fallback keep
the 2434 inherited dirty sibling paths intact. Commit tools first, then this
note/index leads/pin, refresh the scoped retained graph, and verify a fresh
terminal hook and unchanged production. No host/Release work or push.

Reproduce from the consumer root under prepared WSL:
`python3 -m unittest tools.tests.test_game_oriented_strip_1513fab4_study -v`.
Canonical receipts: `conker/build/game-oriented-strip-1513FAB4-study/`.
Private screens/review: `conker/build/game-oriented-strip-1513FAB4-private/`.

Next investigate compiler first-use/escape allocation and pre-cross temporary
spills, using complete disassemblies rather than forcing a frame or guessing
types from gaps. Caller execution, accurate return declarations, arbitrary
private/fault cases, a fitting raw/padded owner, literal full-image prediction,
actual Make, recount, adoption docs and final commits remain required before
any matching credit. Keep the 80% objective active.
