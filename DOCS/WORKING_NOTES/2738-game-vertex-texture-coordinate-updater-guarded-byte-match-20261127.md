# Vertex texture-coordinate updater guarded byte match - 2026-11-27

`func_15062FC0` replaces its zero-return placeholder in
`conker/src/game_83300.c` with the complete **106-word / 424-byte** updater.
Body and slot are VA `0x15062FC0..0x15063168`, ROM `0x90470..0x90618`.
The original zero-byte frame, incoming argument-home store, four bindings,
four-way unrolled loop and all branch-delay work are preserved. There are
no helper calls or floating-point operations.

The actual production recount is **4,717 / 5,528 (85.33%) total** and
**4,044 / 4,855 (83.30%) Game**, with Init 492/492, Debugger 181/181,
zero drift and 811 still different. This adds one accepted match with
unchanged conversion rows and denominators. The **90% goal stays active**:
**259 more matches** reach the required 4,976 / 5,528.

## Interface and recovered behavior

| O32 word | Recovered role |
| --- | --- |
| 0 | `struct127 *owner` |
| 1 | Signed part index; -1 skips the part table |
| 2 | Unused incoming word, still stored at SP+8 by retail and emitted C |
| 3 | Signed S period, snapshotted before register reuse |
| 4 | Signed T period at SP+16 |
| 5 | Signed count at SP+20 |
| 6 | Wrapping 32-bit S offset at SP+24 |
| 7 | Wrapping 32-bit T offset at SP+28 |

The public interface is `void`; recovered callers declare the parent
interfaces as void and the original call sites do not explicitly read
the child result. The complete 68-word parent forwards the last child V0
through its epilogue without reading it. Three arbitrary result poisons
preserve its public effects and call arguments. The actual emitted raw
and normalized target still leave the same current pointer in V0 as
retail on every modeled path. Historical C return spelling remains
unproven; transitive whole-program return-liveness is not claimed.

The mesh byte at owner+`0x1C8` selects an eight-byte bank pair beginning
at owner+`0x28C`. `D_800BE9C0` selects the current pointer, while the other
pointer uses the literal `selector == 0` test. The test is not replaced
by a binary-only complement: native valid objects include nonbinary
selectors, and guest tests cover all byte values with mapped addresses.
The other pointer is loaded even when the current pointer is NULL; the
NULL current path then exits before part/coordinate access.

For part != -1, owner byte 4 selects a pointer through `D_800C4020`; the
signed word at that table's part index is added to both vertex pointers.
SDK `Vtx` has stride 16, with signed S/T halfwords at offsets 8/10.
For each nonzero offset, compare the current coordinate with its signed
period first: subtract one period if greater, otherwise add one period
if the coordinate is negative. Equality is not a wrap condition.
Offsets use unsigned modulo32 arithmetic, avoiding signed C overflow.
Negative and zero counts skip writes, after the original pointer/wrap work.

Each vertex is updated in order: read source S, store destination S,
read source T, store destination T, truncating both writes to 16 bits.
This sequence matters for overlapping buffers. No restrict assumption,
shared actor-layout repair, helper wrapper or new storage is introduced.
The original word2 home is a guest ABI observation; native C tests do
not claim portable access to an unescaped incoming argument home.

## Closed register-role proof and complete owner

The selected source uses an actual S-period snapshot to keep that input
live while pointer temporaries are formed. It emits exactly 106 words
under the unchanged O2/g3 profile. Eighty-five bound words already match.
Twenty guards normalize temporary GPR roles in the opening pointer/part
lookup; one guard at offset `0xD0` reverses equivalent integer ADDU operands.
All four external bindings keep their positions and symbolic identities.
No instruction insertion/omission, artificial padding, frame or FP rewrite
is involved.

The paired SSA proof treats each memory load as an independently
unconstrained value and compares every access address, width and store
value. It checks both branch predicates and all suffix-live registers
at three frontiers: NULL current, part -1 and part lookup. CFG liveness
includes machine V0 and preserved registers. The rest of the routine is
literal identity, except the non-trapping commutative ADDU. Four effective
controls reject wrong bank stride/test, clobbered period and subtraction.
This proves the closed normalization for all input values, beyond a finite
case screen. Raw dead scratch registers may differ; literal complete raw
register/fault-state parity is not claimed.

Both complete padders reproduce the frozen before object and produce the
same selected object. All **88 neighbors**, pools, prior guards and
**18 GLOBAL_ASM bodies** remain unchanged. The independent original-owner
layout reference pins 13,648 ROM words across 89 functions and 61 retained
ASM files. Eight preexisting compiler diagnostics remain unchanged; the
target introduces none. No Makefile/profile change is needed.

## Qualification and production evidence

- Native actual C: **409,120 cases at each of O0/O2/O3**. Every 16-bit
  S/T coordinate pattern, all 256 identities, valid within-actor mesh/bank
  pairs, eight typed Vtx overlap modes, NULL paths, negative/zero counts,
  unroll boundaries and wrapping offsets are covered. A byte-offset
  reference checks the complete initialized world. Separate translation
  units/noipa boundaries, strict aliasing, UBSan traps and LTO type checks
  are enabled. All ten controls fail with logical exit42, not a signal/trap.
- Guest: **3,096 cases per stream / 12,384 runs** across retail, raw and
  both normalized streams. All 106 words execute. Complete memory, ordered
  access trace, machine V0 and preserved state agree. Three pointer domains,
  all identity/mesh/bank bytes, two-byte overlaps, metadata and incoming-home
  aliases are covered. Those extra raw-address probes are guest-only;
  native tests use valid typed objects. Normalized complete states and
  **92 fault triples** agree. Five effective controls include the hazardous
  T-read/S-write reorder on a two-byte alias.
- Callers: **24,096 connected runs** with three result poisons. All 68
  words of original `func_150ED638` execute across clamp boundaries and both
  28/124-vertex routes. It reaches 78 child words; the separate guest corpus
  covers all 106. The 554-word `func_15061B4C` is ASM/ROM pinned, with its
  actual four-word child-call window executed. Its complete broader actor
  loop is not executed here. Eight-word arguments and public effects agree;
  six caller/window controls are effective. No whole-program gameplay or
  hardware acceptance is inferred from these scopes.
- Boundaries: all **212 word mutations**, **eight binding mutations**,
  **42 injected guard bindings** and **42 guard removals** are visible or
  rejected. Both overflow controls reject. Twenty independent GNU links
  cover four symbol groups, independent global addresses, HI16/LO16 carries
  and raw/manual/retail/both-padder routes.
- The actual **five-command Make recipe**, including GLOBAL_ASM processing,
  reproduces the complete qualified owner. An independent frozen-before-C
  plus original-ASM prediction equals the entire linked ELF: **343 changed
  bytes, zero exclusions**. All 720 data owners / 189,088 protected bytes,
  outside guards, neighbors, addresses and conversion rows stay fixed.
  Actual production Make and the live recount confirm the installed result.

The packet runs freshly in both the primary tools checkout and an isolated
tools twin before and after installation. The real sibling tools checkout,
its HEAD, 353 dependency fingerprints and dirty work are preserved.

| Phase | Elapsed | Tests |
| --- | ---: | ---: |
| pre-primary | 293.331 s | 5 fresh / 0 reused |
| pre-sibling | 313.427 s | 5 fresh / 0 reused |
| installed-primary | 272.376 s | 5 fresh / 0 reused |
| installed-sibling | 292.092 s | 5 fresh / 0 reused |

Reports agree across 323 primary / 324 twin imports and 246 tool data inputs. All eleven task files are independently copied. Shared `make tools-check` passes. The frozen input set contains 4,284 hashes and 3,849 snapshot copies. Claude calls: **0**; no subagents or pushes.

Tools commit: `76af5102b702b39f72a9700134afaf115801c725`.
Production ELF SHA256: `12fb3c38383e3d3b6ffc9ac171fa921f25b471da18dc3dee27a3804cab124362`.
Complete owner C SHA256: `f926ecb639c9c7e9ac1fe7724954be4953eab3a30d2a6b98802f24a6c692f1e4`.
Padded owner SHA256: `c956d620fd20faebcc0c3d27d96ce828260191a72f51df128da56e5e7839a711`.
Guard manifest SHA256: `188302aeb00fd1c0e66a956d0bee24a9bb13df13787c0ee9c4d45c9043bf83cb`.

## Host applicability, graph and continuation

The read-only sibling audit records `64CBFDOGL/recomp_scene/cd64_out/func_15062FC0.c` (present: True, SHA256 `73c92a11f15fc5c1252322e5acf67a63eac4c0f8ca3f3a2123171c76ae2ea753`). No active host implementation is qualified or transferred; no host edit, build or launch is made. Release stays frozen.

Graphify refreshes the changed source and packet with all 71 current C definitions and 18 assembly bodies audited. Every prior node ID and qualification proof is retained, and actual Git hook producers are observed terminal before publication. Full-corpus re-extraction is not claimed. The sealed bank retains exact inputs, paired closures, build/image proofs, graph and commit receipts.

Continue with another ordinary unmatched Game routine from this sealed checkpoint. The 145-word `func_1514EECC` remains private and uncredited because its 296-byte frame still differs from retail 288. The 90% objective remains open.
