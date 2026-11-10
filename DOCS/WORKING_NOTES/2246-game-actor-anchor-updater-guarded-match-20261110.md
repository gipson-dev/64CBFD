# Actor anchor-coordinate updater guarded match

Date: 2026-11-10. `func_15060BE0` replaces its zero-return placeholder with a
complete semantic anchor updater. IDO emits **93 words / 372 bytes** and the
original **0x18 frame**. **27 checked word normalizations** recover retail's
positive-zero initialization and one closed FP temporary-register cycle.
No inserted/omitted instructions, frame adjustment, arithmetic substitution,
compiler-profile change or assembly passthrough.

Fresh production recount: **4,315 / 5,513 (78.27%)** total; Game **3,642 /
4,840 (75.25%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,198** different. **96 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion CSV and converted-function/byte totals stay fixed.

Baseline consumer `762363f2deb0d38dab9a06e553edeac385eb69c8`; baseline tools
`12448af5469002ba3d942c4f68ddb65db6d8838c`, from
[Note 2245](2245-game-actor-slot-sector-search-direct-match-20261110.md).
The eight qualification files are banked first in tools commit `83fd921f42039b357f3125d4371a20f6cc3ea4be`.
Local commits only.

## Recovered source and memory views

Owner `conker/src/game_83300.c`; original assembly retained at
`asm/nonmatchings/game_83300/func_15060BE0.s`. Retail span: VA
**0x15060BE0..0x15060D54**, ROM **0x8E090..0x8E204**. The 12-byte placeholder
had 80 differing words across its retail slot. The semantic interface is:

```c
void func_15060BE0(struct127 *actor);
```

Read actor ID first. ID 0xFF, a null transform pointer or nonzero
`D_800C3E90` selects the actor-position fallback. These gates short-circuit;
the global flag is not read after either earlier rejection. Otherwise obtain
the model descriptor from `D_800D1C90[id]`. Descriptor byte **0x27** selects a
**0x40-byte / sixteen-float matrix**. Its signed halfword at **0x14** scales
`actor->y_scale` into a radial displacement.

For a nonzero displacement, snapshot matrix direction floats at 0x10/14/18.
Compute their single-precision norm; divide the radial displacement by the
norm when nonzero, retaining zero otherwise. Multiply the three direction
components by that factor. A zero displacement directly clears all components.
Then read each translation at 0x30/34/38 immediately before its output store,
add the component, truncate to signed **32-bit** integer and retain its low
16 bits in actor coordinates **0x1BC/1BE/1C0**. Earlier halfword writes can
change a later translation through overlapping data views; keep those loads live.

The fallback converts actor positions at 0x14/18/1C. Retail schedules all three
fallback conversions before its first coordinate store. The transformed path
converts/stores each axis before loading the next translation. Invalid-conversion
prefix tests distinguish these schedules without inventing an invalid result.

The existing SDK marks descriptor +0x14 and actor +0x1BC storage as padding,
and its transform pointer uses an incomplete container view. The function uses
explicit signed-halfword and sixteen-float views over that storage. Shared
headers remain unchanged. Native qualification explicitly uses
**`-fno-strict-aliasing`**; it does not establish a strict-aliasing build or a
portable big-endian overlap implementation on a little-endian host.

No direct caller or aligned literal target pointer exists in the retained
code-image census. Computed indirect calls remain unexcluded. The one-pointer
A0 input is established by the body and poisoned-non-input tests. `void` is a
semantic state-updater interface; the original C return type is **not proven**.
The emitted routine retains retail's incidental V0 flag, zero for fallback and
one for the transformed path. Guest tests check that value and all GPR state.
No caller window or runtime reachability is claimed.

## Natural frame and guarded FP roles

The first in-place vector source emits 91 words without a frame. Separate
direction/output locals recover 93 words but initially use frame 0x20. Reusing
the radial scalar for its eventual Y component and declaring X, Z, Y in the
recovered order yields frame **0x18** and the actual **SP+4** Z spill. A typed
sixteen-float row expression restores the original address-add operand order.
No padding, volatile fitting variable or register hint is retained.

Raw target SHA256:
`05d15471760e6fb827162caafe3ea9f8504875105bb05eeb39f4d19ac4ac3d0c`.
The four original relocations already agree: HI16/LO16 `D_800C3E90` at byte
offsets **28/40**, and HI16/LO16 `D_800D1C90` at **56/64**.

Five changed words recover the zero path: word 29 and unreachable word 53
initialize F0 instead of F8; words 54..56 become NOP, store F0 to SP+4 and copy
F0 to F2. All values are positive zero. The Z spill address and relative order
of memory accesses remain equal; its instruction PC moves by one word. This
is not a claim of raw/normalized instruction-fault PC identity.

Twenty-two other changes implement the closed temporary cycle
**raw F4 -> retail F10, F6 -> F4, F8 -> F6, F10 -> F8** in words 57..92.
The transformed region 57..76 and fallback region 79..90 define every one of
those four registers before reading it. Each defines all four before exit.
The proof rejects any stale source word or relocation, decodes only qualified
FP/load/store forms, and checks both region closures. No argument, component,
saved FP register, address, branch, frame offset or arithmetic operation changes.

All **88 non-target owner functions**, raw/padded relocations, constant pools
and register information remain equal. Eight inherited owner diagnostics stay
fixed. All previous guard bytes remain an exact prefix; append only the 27
derived rows for this function.

## Functional, domain and corruption checks

- **961 guest cases / 2,883 executions** compare raw C, normalized and original
  programs. There are **891 normal returns** and **70 invalid-conversion
  prefixes**. Normalized/original pairs agree on complete memory, GPR/FPU state,
  access traces and stop state. Raw/normalized pairs agree on memory, GPRs and
  access order, with the explicit closed FP register relation. Cover all byte
  IDs, signed descriptor extremes, index 255, signed zeros, subnormals,
  overflowing norms, infinities, quiet NaNs, sparse rejected inputs and
  overlapping actor/model/translation storage.
- All **92 reachable words** execute; static CFG analysis proves word **53**
  unreachable from normal entry. The compiler still emits it and its guarded
  form matches retail literally.
- **619 native SDK32 cases at O0/O2/O3**: **1,857 total runs**, **6,190 exact
  serialized case/output bytes per profile**, UBSan and explicit float-cast-overflow
  instrumentation enabled. All other actor bytes and complete model, buffer,
  pointer table and flag inputs remain unchanged. Native cases use the real
  187-entry pointer table, disjoint data views and valid signed-32 conversion
  results. Endianness-sensitive overlaps and extended table IDs remain guest-only.
- **17 effective compiled semantic controls** complete normally in the valid
  conversion domain and produce observable output disagreements. Invalid
  prefixes and execution errors are not counted as witnesses. Controls reject
  wrong gates, signed distance, scale, norm/square root, component factors,
  zero handling, fallback, output offset, cached translations and reversed stores.
- Both independent padders reproduce the original 93-word payload and
  bindings. Reject **97 source-word/binding corruptions**, **three guard-record
  corruptions** and **two independent stale-expected-word padder attempts**.
  **48 executions across four independent symbol sets** cover low halves 0,
  0x7FFC, 0x8000 and 0xFFFC. **72 normalized/original instruction-access cut
  pairs** agree on complete prefix state, including partial transformed stores.
- **72 poisoned-non-input executions / 24 complete normalized-retail pairs**
  preserve results while varying all caller-saved non-argument GPR/FP inputs.
  Callee-saved state and normal-return SP/RA remain intact. The census finds
  **zero direct J/JAL sites and zero aligned literal target pointers**.

Invalid conversions stop **before** the first such instruction. Their result,
FCSR behavior, exceptions and subsequent stores remain unqualified. These
checks do not establish portable C fault semantics, hardware execution or live
gameplay acceptance. Exact final instructions preserve the retail routine;
the instruction model does not supply missing hardware evidence.

## Complete image, tools and continuation

Freeze **2,214 input fingerprints**, retaining exact mutable baseline files.
Five actual owner Make commands and independent before/proposed compiles agree.
The complete predicted ELF changes exactly **258 bytes**: the recovered
372-byte target slot and its symbol size **12 -> 372**. There are no metadata
permutations and **zero exclusions**. Eight independent image corruptions are
rejected, including the dead word and adjacent code.

All **6,050 function addresses** remain fixed; only the target canonical body
changes. All **189,088 protected bytes / 720 data owners** remain exact,
SHA256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production completes in **58.81 seconds**. Existing duplicate
`generated_12D630` recipe warnings and expected whole-ROM checksum exit 2 remain;
the owner, predicted binary, strict full image and actual-ELF recount pass.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `69a3adeec282684120c1225e9caf0ee95aaf772850eb3f1be7b1b231ee82a428` |
| Built binary | `f016d0a3eee918294a82f87f2bed9a7c9852803fb7c60c81a6073cc1a251c95b` |
| Padded owner | `417ba04b5d299648998553879a29f8a03b8fcca78539ec822917123cdb35a9df` |
| Guard manifest | `88c8afe2b5a0d9549aaefe013ea3c33f6de48052759f1d6a65d4a93c1f08bf0f` |

Eight fresh preinstall checks per tools environment pass: mounted
**214.97 s**, sibling **83.70 s**. Two fresh
installed checks per environment requalify actual Make/full image and complete
guest behavior: mounted **158.91 s**, sibling
**46.88 s**. Six other checks are explicit preinstall reuses,
with every tool/imported dependency fingerprint revalidated. Fresh shared smoke
checks pass; three unchanged pure-helper regression receipts per environment
are reused separately.

The sibling uses an eight-file private overlay, with explicit read-only mounted
fallbacks for missing diagnostic, binding, CFG and prior float-instruction
helpers. Consumer Make invokes mounted CLI tools; independent in-process
padder checks use sibling helpers. Its **2,434 pre-existing dirty paths** are
preserved. Codex is the only writer; **zero Claude calls** are used. No host-port
source, saves or frozen Release artifact is touched.

The scoped code graph contains **59,686 nodes / 113,074 links**.
All **59,686 old nodes** are retained or relocated, and definitions
outside changed paths remain equal apart from community metadata. Verify all
71 owner C positions and retain its 18 assembly pragmas. The new tools have
**0 indexed nodes** under existing submodule filters. Historical
excluded nodes remain retained; this is a scoped refresh with a recorded
coverage gap. Private post-commit receipts also audit heading relocation.

Reproduce under WSL PSBBN in the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_actor_anchor_15060be0_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Exact retained pre-adoption mutable inputs are required under
`conker/build/game-actor-anchor-15060BE0-match/frozen/`. No ROM or ELF binary
is committed; a clean clone without those inputs is not claimed to reproduce
the workspace image.

Next: investigate **`func_1505ED34`**, 95 words/frame 0x20, in the same
owner. Its 12-byte zero-return placeholder still differs at
85 retail words and remains untouched/uncredited. The original
code searches slots 0..24, then recycles eligible state-0x27 actors or the
reserved slot 25 before calling the existing initializer and returning the
chosen pointer. The preliminary census finds five direct call sites. Qualify
all callers, pointer return types, helper effects, saved pointer/index homes
and reserved-slot behavior before implementation. Keep the 80% goal active.
