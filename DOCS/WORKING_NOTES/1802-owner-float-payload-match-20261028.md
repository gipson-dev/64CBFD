# Owner float payload direct C match — 2026-10-28

`func_1510A344` is recovered in `conker/src/game/generated_1368C0.c` as
`void *func_1510A344(u8 *owner, s16 lifetime, u8 priority, s32 arg3)`.
All 50 instructions (200 bytes), the 72-byte frame and six symbol bindings
match directly from C under the existing IDO O2/g3/mips2/o32 profile.
No guards, volatile parameters or alignment words are needed. All nine
other functions in the complete owner are preserved.

The adopted ELF recount is **3,880/5,506 (70.47%)** total and
**3,207/4,833 (66.36%)** Game, with zero address drift. Init remains
492/492 and Debugger 181/181. There are 1,626 different C functions and
**250 more exact matches** needed to reach 4,130/5,506, the 75% threshold.

## Recovered behavior and interface

- VA `0x1510A344..0x1510A40C`; ROM `0x1377F4..0x1378BC`.
- A null owner returns null without dereferencing it or calling the factory.
- Otherwise the routine snapshots the owner pointer, its byte at offset
  `0x3B`, and three float values: zero, `D_800A2684` and `D_800A2688`.
- `OwnerFloatPayload` is 20 bytes: pointer at 0, identity byte at 4, three
  untouched padding bytes at 5–7, and floats at 8, 12 and 16.
- It calls `func_15149130(lifetime, -1, 28, -1, 1, 28, 20, priority, arg3)`.
  On success it copies the complete payload to the result at offset `0x28`;
  failure skips the copy. The result is an allocated pointer or null.
- The signed 16-bit lifetime and unsigned priority byte use their original
  argument lanes. The final word retains its numbered name because a more
  specific meaning has not been established here.

The source comment describes the owner payload. Field names retain the
three values' unproven meanings. Declaring the result before the payload
reproduces the retail stack layout without adding padding fields.
The original function name remains for traceability.

The rodata words are `0x3E50E561` and `0x3F526E98` at ROM `0x247144` and
`0x247148`. They remain external bindings rather than new literal pools.
Bindings are HI16/LO16 at `0x20`/`0x3C` for `D_800A2684`, `0x40`/`0x48`
for `D_800A2688`, and calls at `0x8C`/`0xA8` for the factory and `memcpy`.

## Qualification

Eight fresh checks passed in each tools copy. After production, two fresh
installed checks passed in each copy; six unchanged semantic checks were
reused only after complete input, module and artifact fingerprint identity.
Shared tools checks passed in both copies.

| Evidence | Measured result |
| --- | --- |
| Complete owner and actual Make | 10 functions, nine unchanged raw and padded neighbors; all three Make commands reproduced the qualified object; no compiler diagnostics |
| Direct guest execution | 1,584 cases; all 50 words covered; halfword/byte lanes, null and allocation gates, owner/output aliases, float bit patterns, payload snapshots and untouched padding |
| Original factory and byte-copy loop | 96 connected cases; 49 + 11 literal words retained, 47 + 11 reachable words covered |
| Original caller | 288 cases through the seven-word window at `0x15027674`; original argument loads and ignored-result return gate verified |
| Native 32-bit SDK | 184,320 cases each at O0, O2 and O3 with trapping UBSan, valid backing, output fences, owner/output aliasing and ten effective controls |
| Fault prefixes | 198 direct/connected and 97 caller prefix pairs; full guest state, PC and trace; 31 direct/connected delay-slot cuts |
| Independent GNU links | Three layouts, 96 cases; original assembly, actual-Make object and selected C agree, including signed-low constant addresses |
| Rejection controls | 56 changed word/binding probes, ten compiled semantic controls and nine whole-image corruptions rejected |
| Whole image | Exactly 154 changed bytes: 153 code bytes and one extent byte; zero metadata changes or exclusions |
| Protected Game data | 189,088 bytes across 720 owners unchanged |

The whole-ROM aligned scan finds one JAL at ROM `0x54B30` / VA
`0x15027680`, with no full function-pointer words. The original caller is
`func_150265CC`, whose C remains a placeholder in `generated_50D80.c`.
Its bounded window loads the owner from `SP+0x764`, a signed halfword from
`SP+0x662`, and a byte from `SP+0x773`, then passes final argument 1 in the
call delay slot. It ignores the pointer result and branches to `0x15029BA4`
with return value 1. This is not a current C caller edge or full-parent proof.

The connected helpers are the original `func_15149130` and `memcpy` bodies.
The factory's category-95 arm at `0x15149164`/`0x15149168` is unreachable
for this caller's fixed flags value 1; both literal words remain preserved.
The original 11-word byte-copy loop is fully covered. The allocator
`func_15167A68` and `bzero` remain bounded external services. No complete
allocator, parent, native provider or gameplay acceptance is claimed.

The factory's existing shared declaration spells its size argument as
`struct37 *`; its original instructions add `0x28` to the supplied byte
count. This recovery uses the observed integer count in its local declaration
and preserves the existing provider and shared headers. Their broader C
type cleanup is not part of this target's matching credit.

Native checks do not assert indeterminate padding values. Guest tests
preserve the original bytes and cover incoming-home mutations separately.
Compiled negative controls terminate without incidental faults, and their
semantic comparisons exclude private stack addresses and unspecified padding.
The initial interpreter lacked the factory's signed-byte load; implementing
that instruction fixed the harness. The candidate C did not change.

## Image and provenance

Production reproduces the private link exactly. Independent prediction
changes only the literal 200-byte body and symbol extent from 12 to 200.
All 6,056 canonical function addresses and the other 6,055 bodies remain
fixed. The progress inventory and inherited guard CSV are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor ELF | `d58ca358aebe9cfdc02775b59e8fb8c705be28ed99b204ad673680e9cd5e5c16` |
| Adopted ELF | `712971ca8c175d1ccaa01a4a1ae99e00065d15835ebc66a6e508d62b40ba6368` |
| Adopted owner C | `3cbb0358584c830296f60fa606b830ac894baca4fd062946b53e62dade8058ff` |
| Qualified padded owner | `06f74de47c393d2f64a3d1192b0a9e9f97da1892f4fd4abf47f0f9448c534eff` |
| Raw relocatable body | `4a5b8b2816a89997ccbdb96b2ccfb95bf8626f394a38b7dbab2d46bbb0ebcc82` |
| Retail body | `dfa842c69b3013af1892d55de2b678a98d85f067bebb2c239ff5e90a18927c2a` |

Tools were committed first as `2097c26a74eef914aeabc74df69d93f40ca80bcc`,
following `4e83f09976b576d0befab468b3a490d05f9f98d3`. The consumer predecessor
is `f050930c1e6982385f667f8bee5d3571f6a83912`. The older tools mirror's
1,847 inherited dirty paths are preserved; three qualified modules are
added without committing that mirror. No push is performed.

Receipts live under `conker/build/game-owner-float-payload-match/`: 456
focused inputs, the 16,512-path input seal, private/canonical checks,
actual-Make proof, production audit, live recount and independent final
audit. The scoped Graphify refresh preserves old nodes and still-valid
relationships, retiring only the old placeholder's incorrect s32 return edge.
Historical clustering and centrality are not recomputed.

## Review and continuation

Codex implemented and validated this routine. Claude budget/attempted/completed:
0/0/0. The 75% goal remains active. Next inspect the 50-word `func_151AF270`
in `conker/src/game/generated_1D92F0.c`. `func_1514E920` remains parked and
uncredited. Remaining shapes: 1,497 placeholders, 120 semantic/other and nine
unlocated functions. Queue ordering is a screen, not matching qualification.
