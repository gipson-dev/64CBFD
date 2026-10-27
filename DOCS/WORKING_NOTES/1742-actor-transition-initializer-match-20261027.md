# 1742 - Actor transition initializer match

Verified 2026-10-27, following [Note 1741](1741-group-type2-actor-reset-match-20261027.md).

## Result

Replaced the zero-return placeholder for `func_15063570` in
`conker/src/game/generated_90840.c` with the actor transition initializer.
The complete **184-byte / 46-word** body matches directly from semantic C at
VA `0x15063570..0x15063628`, ROM `0x90A20..0x90AD8`.
There are **zero guards**, inserted words or omitted instructions. The retail
40-byte frame, saved RA at SP+0x24, incoming actor home at SP+0x28 and floating
zero setup after the first provider all match. The normal O2/g3 profile applies;
this owner does not use the preceding recovery's no-unroll override.

The captured, actually adopted Native ELF recount is **3,819 / 5,506 exact
(69.36%)**, Game **3,146 / 4,833 (65.09%)**, Init 492/492 and Debugger 181/181.
Address drift is zero; 1,687 C functions differ. These are restorations of
existing C inventory rows, so converted-function/byte totals and progress CSV
bytes stay fixed. The 75% threshold is 4,130, requiring **311 more** exact
functions. The wider goal remains open.

## Behavior and interfaces

The recovered interface is `void(struct127 *actor)`. Signed 32-bit
actor-minus-pool division by `sizeof(struct127)==0x32C` selects the pool
entry. The function writes 0x3B to its nested record's byte 0x78, reloads the
nested pointer, and writes 2 to byte 0x11A. That reload is observable if the
first byte store aliases the pointer field; a compiled cached-pointer control
is rejected by the guest checks.

It calls `func_15083568((u8 *)actor, 0x89, 1.0f, 0)`, then uses the
original actor argument to set `disable_jump=20`, `disable_run=0` and
`unk83=0`. The first provider's returned pointer is ignored. Finally it
calls `func_1505E650((u8 *)actor, 0x221, 1.0f, 0.0f, 0.0f, 0.0f, 0)`.
Provider mutations after the final call remain observable.

The actual `func_15083568` definition in `generated_AEB40.c` is
`u8 *(u8 *, s32, f32, s32)`; the older shared-header void/struct-pointer
declaration is stale. The local declaration uses the defining interface.
The animation provider remains assembly; its original/retained 95-word body
and the established seven-argument declaration confirm the actor pointer,
u16 state home, four f32 arguments and final s32 mode. Local declarations and
pointer casts express those ABI requirements without changing shared headers
or the existing neighboring provider declaration.

The sole aligned direct JAL is ROM `0xC68A4`, inside retail
`func_15097A8C`. Its full original body is 2,146 words; its actual
142-entry table maps event 108 to `0x150993C8`. Payload state 0x3B passes
the actor lookup result as the target's sole argument and ignores its return
register before returning 1. State 9 calls the neighboring handler instead.
Missing actors and invalid events take the original no-target paths.

The current decomp dispatcher and its lookup remain zero-return placeholders.
The caller check therefore uses the complete original retail body and actual
table, covering the target route and nearby rejection paths (44 dispatcher
instructions), with lookup/other-handler contracts bounded. It does not claim
the dispatcher is restored or that every retail branch is covered. Original
and retained animation assembly are also connected on two bounded early-exit
routes. No helper receives new C matching credit or gameplay acceptance.

## Qualification and preservation

The raw selected C and independently assembled retail target agree in all
46 words and four bindings: one HI16/LO16 pool-address pair and two R_MIPS_26
provider calls. The first source candidate matches without scheduling guards.
Six independent GNU links across three layouts preserve those bindings and
signed-low carry behavior; 288 rebased guest cases per tools copy pass.

All 18 other owner functions and normalized pools are unchanged. The actual
five-command Make path preprocesses GLOBAL_ASM, compiles with IDO, applies ASM
postprocessing, pads and assembles the object. All 19 compact functions and
the complete padded object reproduce the qualified artifacts. Baseline,
proposed-owner and isolated-target diagnostics are empty. Existing unrelated
Make duplicate-recipe warnings remain separate.

Both tools copies pass eight fresh canonical methods, zero errors/failures/
skips, in 6.111 and 6.124 seconds. Both shared tools checks pass. Per-copy
coverage includes:

- 1,104 target guest cases, all 26 valid pool slots, all 46 instructions, signed
  truncation/nonmultiple guest inputs, four alias layouts and provider effects
  before/after the flag stores. Invalid indices are not native C claims.
- 96 original/retained 95-word animation-provider cases on the busy and invalid
  actor early exits, and 192 original retail dispatcher cases.
- Native32 O0/O2/O3 with 53,248 cases per profile, actual SDK layout assertions,
  typed function pointers, valid actor arrays, typeless nested allocations,
  trapping UBSan and 14 effective semantic controls.
- 56 fired guest fault prefixes, effective compiled cached-pointer and unsigned
  index controls, and two guest-only incoming-home alias cases.
- Three raw/binding negatives, seven strict-image corruptions and three wrong
  input controls. The word-patch manifest is unchanged.

The seal covers **16,137 Native inputs** and **73 focused frozen inputs**.
Actual production Make completes in **0.669 seconds** and exactly reproduces
the independent full-image prediction: **148 changed bytes = 147 target code
+ 1 symbol-size byte**, **zero exclusions**. All 6,056 addresses and all 6,055
other bodies stay fixed. Protected Game data is exact across 720 owners /
189,088 bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After installation both copies pass two fresh owner/image checks. The six
unchanged semantic methods are reused only under exact source/tool/snapshot/
prepared-artifact fingerprints. Four adopted outputs are source, owner object,
complete ELF and map. Guard/layout manifests and progress CSV remain fixed.
The Native ELF capture is recounted independently of a projected increment.

| Artifact | SHA256 or commit |
| --- | --- |
| Tools commit | bf1d5f2d3db38b15a82d2b91d233bc8bc72867b3 |
| Adopted ELF | 6642e143d16dba8b2e9be4234878b37a5de348678e41d352d1b40ff3f9c30d89 |
| Recovered owner source | 9573c1410dd759dc7ee15a8387ecc084d9fc21ff2ce76f44ed0d40bb4f24ed2f |
| Padded target owner object | bbc10faa727c03449fd71baeaf397e16aacdc51df5c4920e02abddd1e22e6e6c |
| Raw selected C payload | dd042b5f73285ac02fde20b2ee9fc2c9529723e0833712bbd7cfe9122b88c478 |
| Input snapshot | f4e30148c071def73f2c4ef178f0d1a1a3b42b83a9f7815e8c7387fe838bc89d |

Receipts and frozen evidence are in
`conker/build/game-actor-transition-start-match/`. The rejected launcher
attempt and rejected fixture run are retained. Fixture fixes concern assembly
whitespace, a negative-control name colliding with the native entrypoint, and
classifying the actual unsigned-index access fault. The semantic C candidate
and frozen compilation did not change. WSL/compiler installations and sibling
host/editor/Release checkouts are unchanged. Routine Claude calls: 0.

## Next boundary

The next screened placeholder is `func_150BCFB8` / `generated_E8C10`,
another 46-word window. It remains uncredited until source/ABI/caller, complete
owner/Make, guest/native, image, production, recount and documentation gates
pass. Root README changes remain aggregate rows only. Refresh the changed
sources structurally, retain old nodes and validate any superseded placeholder
type relationships against the actual declaration change; keep historical
community/centrality claims separate from current extraction.
