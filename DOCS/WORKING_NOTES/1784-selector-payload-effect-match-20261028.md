# Selector payload effect - direct C match

Verified 2026-10-28. Restore func_1500A6D8 in game_36680:
VA 0x1500A6D8..0x1500A79C, ROM 0x37B88..0x37C4C, 49 words / 196 bytes.
Normal O2/g3 emits every retail instruction directly. The frame is 0x50,
all seven relocations match, and the complete guard manifest stays unchanged.

## Recovered behavior and interface

The interface is void func_1500A6D8(struct226 *actor, s32 command).
D_80082BEC supplies a six-byte table: {7,8,9}, {8,9,10}. Copy it locally,
select row 1 when D_800BE9F0 is 6 and row 0 otherwise, then index by
command minus 0x49. The original callback table supplies commands 0x49..0x4B.
The local aggregate uses ordinary C structure initialization. Its declaration
order and explicit if/else recover the retail stack and branch layout without
an array-initializer extension or compiler-profile override.

Call func_150B060C with the unsigned selector and a 24-byte UnkB060C output.
Its existing payload layout is reproduced locally with identical members.
The actual helper consumes two arguments; residual A2 is not a third formal.
On lookup failure, stop. Otherwise set Header fields to 0, 23, 300 and 0,
then call func_1516037C(header, actor, 24, 255, 1). On allocation success,
copy all 24 payload bytes to effect +0x18. The function returns void.

Header byte 5 retains its incoming stack contents, as in retail. Guest tests
check that exact byte through the original six-byte header copy. Native tests
validate the initialized fields without assigning meaning to uninitialized
padding. Payload changes made during the factory call remain visible to the
subsequent copy.

Typed helper declarations are local to this owner. Three older calls require
explicit Header/actor pointer casts; their instructions and bindings remain
unchanged. Shared headers and other source owners are unchanged. All six
inherited compiler warnings remain at the same expressions; no warning is added.

| Retail property | Qualified result |
| --- | --- |
| Frame / saved register | 80 bytes; RA at SP +0x1C |
| Selector / payload / header locals | SP +0x24 / +0x30 / +0x48 |
| Actor argument home | SP +0x50 |
| Selector table relocations | HI16/LO16 at +0x14/+0x18 |
| Category relocations | HI16/LO16 at +0x20/+0x38 |
| Lookup / factory / copy calls | +0x60 / +0x98 / +0xAC |
| Owner preservation | 81 neighbors, bindings and pools; one retained GLOBAL_ASM |

## Original callback and helper qualification

The aligned ROM census finds no direct J/JAL and exactly three target pointer
literals, at ROM 0x2277E0/0x2277E4/0x2277E8: slots 73/74/75 of D_80082BFC.
The complete 17-word func_1500A94C preserves A0/A1 for that callback and ignores
its return. Its valid, rejected and null callback routes execute in the tests.
The table and current dispatcher remain byte-exact and unchanged.

Execute the complete 39-word func_150B060C and 32-word func_1516037C with the
caller and restored target. Verify lookup failure, the signed coordinate
endpoints, allocation arguments (53,1,48,1,255,1), six header bytes, actor
pointer at +0x14 and 24 payload bytes at +0x18. The 97 integration cases visit
every instruction in all four routines. func_151149AC, func_15167A68 and memcpy
remain bounded providers; this does not claim full-game visual acceptance.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, both pass two fresh installed methods; six semantic methods
are reused only with exact module, input and artifact fingerprints.

- 1,112 guest cases visit all 49 target words, exercising all selector byte
  values, category boundaries, nonzero lookup returns, allocation failure,
  outgoing argument-home clobbers, helper mutations and actor/output aliases.
- 54 access-prefix pairs preserve complete state, memory traces, PC and delay
  slots. Failed lookup/allocation never accesses the payload destination.
- Native32 O0/O2/O3 each pass 49,152 cases with trapping UBSan, exact ABI layout
  assertions and complete actor/output fences. Twelve semantic negatives fail
  in native runs and twelve separately compiled IDO negatives fail in guest runs.
- Three GNU layouts exercise HI16/LO16 carries and 72 guest cases. Raw C,
  original and actual Make objects link identically. Three raw/binding and six
  whole-image corruption controls are rejected.
- The actual five-command Make recipe, including asm_processor and pad_c_object,
  reproduces the qualified compact and padded owner. Make retains its known
  unrelated duplicate generated_12D630 recipe warning.

The immutable qualification seal covers 16,386 paths and 379 focused inputs.
Production reproduces the independent entire-image prediction: exactly 149
changed bytes, comprising 148 code bytes and one symbol-size byte (12 -> 196),
with zero exclusions. All 6,056 addresses, 6,055 other linked bodies and 720
protected Game owners / 189,088 bytes remain unchanged. The Makefile, layout,
conversion CSV and complete guard manifest are preserved.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler / original body | c18bf186ea8126f645e9c0af683b8171e34db8109d4f23a3c12214daedfe3d2b |
| Linked retail slot | 562cf1ff5272e4dff3f3dcb753e52b752b3fcbfe9df67019f68526dbcc5300d1 |
| Adopted owner object | 491d7d38b9b8503f1619f0facee947e830bfb0e4e234135ec6ca8cb823cf6e39 |
| Adopted ELF | 3d06b6465acf80871e73d069921a2701d18617a79d1ce99d9c8ab5bc91883c09 |

## Bank and measured progress

Predecessor consumer: 70a5be1f3ee8244d2dc691437eac6f3153df1943.
Tools committed first: f3e54d723ebb921dd6b5960ec91898333cf5484e.
The consumer commit updates this source, the tools pin and measured docs.
No push is performed. Preserve all 1,793 inherited older-mirror dirty paths
and the three new qualification modules; do not reset or commit that mirror.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,862 / 5,506 (70.14%) | 0 | 1,644 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,189 / 4,833 (65.98%) | 0 | 1,644 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

268 more exact functions are needed to reach 4,130 / 75%. Remaining source
shapes: 1,515 placeholders, 120 semantic/other and nine unlocated. This function
is the only newly credited entry. Keep func_1514E920 parked and uncredited.
Next inspect func_1509CE64 in generated_C9EC0; screening alone earns no credit.

Retained evidence: conker/build/game-selector-payload-effect-match/ contains
preparation.json, both canonical/installed receipts, sealed-production-proof.json,
sealed-live-adoption-audit.json, canonical-function-views.json and
75-percent-queue.json. The final handoff records the consumer commit, scoped
graph refresh and independent closing audit. Root README changes only totals.
