# 1820 - Actor height position - 2026-10-29

`func_150BA930` is recovered in `conker/src/game/generated_E7970.c` as
`s32 (f32 *position, u8 *actor, HeightResult71820 *result, u8 unused)`.
All 52 words /208 bytes emit directly from semantic C, using the original
48-byte frame and four bindings. There are no guards, alignment words,
insertions, omissions or custom compiler profile. The original name remains;
the comment describes position copying and the optional vertical query.

## Behavior and interface

Copy actor X (+0x14) first. Choose actor height (+0x180) for Y when it exceeds
`D_8009FE60`; otherwise use actor Y (+0x18). Copy actor Z (+0x1C) last. These
ordered stores matter when output overlaps actor coordinates or height.
A null result buffer returns 1. Otherwise capture an XYZ start vector using
current output Y plus 100, call `func_1504715C(result, actor)`, then reload
output Y and call `func_15046C80(start, 0, outputY - 100, result)`. Return that
query's full s32 result. Provider mutation of output Y therefore changes the
lower bound while preserving the previously captured start vector.

The output pointer survives calls in S0. The start vector is at frame+0x24 /
incoming SP-12. The unused fourth argument is stored in its original home.
Opaque forward declarations use the existing named HeightResult71820 and
HeightActor71820 structures and preserve the canonical helper signatures.

The only aligned JAL to this routine is VA 0x150BAA44 / ROM 0xE7EF4 in
`func_150BAA14`. Its original 20-word prefix gates on actor+0x1D4, passes a
position at parent frame+0x6C, result at +0x48, and the low byte of its second
argument as the unused fourth argument. It stores the callback result's low
byte at parent frame+0x43. The caller remains a C placeholder; the prefix
qualification does not grant it matching credit or claim full-parent execution.

## Qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production passes two fresh installed methods per copy; six semantic methods
are reused only under exact module/input/artifact fingerprints.

- 1,696 guest cases cover six output layouts, four result layouts, all fourth
  argument bytes/high homes, non-finite float values and provider effects.
  Full state, call packets, return words and access traces agree. Coverage is
  51/52 instructions: retail's duplicate load at 0x150BA978 is unreachable.
- 150 fault-prefix comparisons include 15 delay-slot cuts. No portable C
  fault, FCSR, hardware or gameplay behavior is inferred.
- Native32 O0/O2/O3 each pass 9,216 cases with trapping UBSan, fresh untyped
  backing and nine effective negative controls. Output/result overlaps and
  mutable output Y are exercised. Nine separately IDO-compiled mutations
  also produce observable memory/call/packet/return differences.
- 288 original caller-prefix cases qualify the gate, argument addresses,
  ignored fourth argument and low-byte result consumption.
- 648 connected original-helper cases execute the original 89-word initializer and
  32-word query router in their relevant scopes, visiting 88 and 29 words.
  The query status domain is 0/1/2; entity checks and lower queries are bounded.
  Fresh comparison shows the current query router is byte-exact, while the
  current initializer is not. The initializer evidence is original-code
  execution, not matching credit or equivalence of its current C instructions.
- Three GNU layouts/18 cases preserve complete original/compiler/padded code,
  including JAL and signed HI16/LO16 relocation carries. Three raw payload/
  relocation mutations and six complete-image corruptions are rejected.
- Actual Make uses compiler, padder and assembler with no diagnostics. All
  five neighboring functions and owner data pools remain unchanged.
- The entire ELF changes by 152 predicted bytes: 151 code bytes and one
  target-extent byte, zero other metadata or exclusions. All 6,056 function
  addresses, 6,055 other bodies and 189,088 protected Game bytes/720 owners
  remain fixed. Guards, shared headers, map and C inventory remain fixed.

16,638 sealed and 645 focused inputs are audited. The older tools mirror keeps
all 1,901 inherited dirty paths plus the three new modules. Tools `3ea9c56`
precedes the consumer commit. No push is performed.

ELF SHA-256: `ead9c7a16e0b4227f788916bbf6498b99040aa424634394d85a0ecab8bc3e1a0`.
Object: `ab4430d78e37a138108834a17545c1014d9a5f446a85e0871b7207a56e31a618`.

## Progress and continuation

Actual live-ELF recount: **3,898/5,506 (70.80%)** total,
**3,225/4,833 (66.73%)** Game. Init 492/492 and Debugger 181/181 remain exact;
zero address drift; **232** more exact C functions reach 75%.
`func_1514E920` and `func_151D7000` remain parked and uncredited.

Graphify receives a scoped changed-source/tool/Markdown refresh with all old
nodes and valid relationships retained. The target retains its s32 return,
so no return relationship is retired. Helper/caller evidence records the
initializer's current non-matching status and original execution scope.
Historical global analytics remain historical; no full-corpus extraction claim.

Local receipts and handoff: `conker/build/game-actor-height-position-match/`.
