# Actor-slot allocator restored as direct C

Date: 2026-11-10. `func_1505ED34` now replaces its zero-return placeholder
with the full actor allocator: **95 words / 380 bytes**, original **0x20 frame**,
and **zero guards**. All words emit directly from semantic C under retail O2/g3.
No inserted/omitted instructions, assembly passthrough, padding, volatile fitting
variable, register hint, profile change or shared-header change.

Fresh production recount: **4,316 / 5,513 (78.29%)** total; Game **3,643 /
4,840 (75.27%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,197** different. **95 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion CSV and converted-function/byte totals stay fixed.

Baseline consumer `78c932e07b76c8f6fe9bf266a3aa3d36be74e11e`; baseline tools
`83fd921f42039b357f3125d4371a20f6cc3ea4be`, from
[Note 2246](2246-game-actor-anchor-updater-guarded-match-20261110.md).
The eight qualification files are banked first in tools commit `ece935d4b5061ecc64ef88ea36777dde0f3a7c8e`.
Local commits only.

## Recovered source and return contract

Owner `conker/src/game_83300.c`; retained original assembly
`asm/nonmatchings/game_83300/func_1505ED34.s`. Retail span: VA
**0x1505ED34..0x1505EEB0**, ROM **0x8C1E4..0x8C360**. The old 12-byte
placeholder differed at 85 retail-slot words. The recovered interface is:

```c
u8 *func_1505ED34(void);
```

The internal cursor is `struct127 *`, matching the SDK's 812-byte actor
layout and 26-element `D_800CC2D0` array. The public byte-pointer return agrees
with the existing C consumer in `generated_AEB40.c`; an explicit `(u8 *)actor`
conversion preserves that compatible cross-translation-unit declaration.
The local placeholder's s32 return is repaired. Other call sites remain
assembly or C placeholders; their original pointer consumers are qualified
without crediting their complete parent routines.

Search ordinary slots **0..24** for state zero. If full, first prefer state
**0x27** with a null transform pointer at **0x1D4**. If none, retry for any
state-0x27 actor. If still full, use reserved **slot 25**. Conditionally invoke
`func_15060F28(actor, 0)` when the chosen record is occupied. Always invoke
`func_1505F188(actor)` and return that same saved pointer.

The three scans short-circuit their limit tests and do not read slot 25 before
the final fallback. Preserve the retail's explicit occupied-state reloads and
distinct scans. The selected pointer/index survive cleanup in **SP+0x18/0x1C**;
the table and sentinel reload after the first cleanup are retained. Helper
clobbers and mutations must not change the already selected pointer.

## Direct emission and relocation alias

A for-loop body with `break` emits only 79 words. Compound scan conditions
recover the original 95-word shape. Declaring index before actor restores the
saved homes. Index-first initialization in the free scan and pointer-first
initialization in the two retry scans recover the final four scheduling words.
The API pointer conversion preserves all emitted code and the full image.

Raw target SHA256:
`7c935f52cc45b0ac9c592bb9d583f86a1230b3ca5a938b7933e1fd17b9bdccdb`.
Fourteen relocations bind the actor table and two helpers. Retail names the
first transform-field load as `D_800CC4A4`; compiled C uses
`D_800CC2D0 + 0x1D4`. Their bound instructions agree. Four independent symbol
sets preserve this field alias and exercise low halves **0, 0x7FFC, 0x8000,
0xFFFC**. Sixteen actual GNU linker results agree with the independent binder;
four deliberately broken aliases are detected. No guard normalizes the alias.

Both independent padders preserve the direct raw target. All **88 other owner
functions**, raw/padded relocations, constant pools and register information stay
equal. All eight inherited diagnostics remain fixed. The complete historical
guard manifest remains byte-for-byte unchanged.

## Functional, ABI and corruption evidence

- **348 guest cases / 696 executions**, with 348 complete raw/retail machine,
  memory, trace and call pairs. Execute **all 95 words**. Cover every ordinary
  slot, competing priorities, signed state extremes, empty/occupied reserved
  slot, eight sparse-memory cases, both stack phases and poisoned non-input
  registers. Opaque helpers mutate selected/adjacent records, overwrite their
  argument homes and clobber caller-saved GPR/FP registers.
- **340 native SDK32 cases per O0/O2/O3 profile**, **1,020 total runs**, with
  strict aliasing and UBSan. Each profile reproduces **7,194,224 serialized
  case/public-memory/call bytes**, including all 26 actor records. State/pointer
  fields are serialized canonically; native transform proxies are valid local
  addresses and are not dereferenced. Sparse unmapped cases remain guest-only.
- **14 effective compiled controls** complete normally and change an observed
  result. Reject wrong scan bounds, state/filter predicates, dropped null
  priority, omitted cleanup/initializer calls, wrong initializer slot, wrong
  occupied gate and incorrect pointer returns. No execution errors count as
  semantic counterexamples.
- Both padders, **109 stale word/binding corruptions**, **64 rebased guest
  executions**, **16 independent GNU linker checks**, **341 exact access-cut
  pairs**, and **eight whole-image corruptions** pass their expected checks.
  Fault-prefix agreement does not establish portable C fault semantics.

The whole aligned code-image census finds **five direct JALs** and zero aligned
literal pointers. Computed indirect calls remain unexcluded. Qualify **73
original caller-window words**, **150 pairs / 300 executions**, across:

| Call site | Parent | Verified consumption |
| --- | --- | --- |
| 0x1506C4E0 | func_1506C460 | saved scan index, returned slot and reserved threshold |
| 0x15073140 | func_15073118 | saved actor pointer, float/byte field stores |
| 0x15082B3C | func_15082A44 | saved argument and reserved-slot failure branch |
| 0x15083B08 | func_15083AC8 | slot-derived byte key and returned actor handle |
| 0x151952A0 | func_151951E0 | delay-slot parent store and new-actor field copies |

An additional **80 pairs / 160 executions** connect original cleanup,
initializer and default-field code, covering **152 helper words**. The
resource-free cleanup path is exercised for all four category values and
five unsigned RNG results, including 0x80000000/0xFFFFFFFF. Cleanup itself
calls the initializer; the allocator then initializes the selected actor again.
RNG and remaining cleanup leaf effects are opaque boundaries. Resource-owned
cleanup paths, complete parent algorithms, hardware execution and live gameplay
are not qualified here. The existing cleanup C stub remains unchanged and
uncredited; it is not treated as a working retail cleanup implementation.

## Production, tools and continuation

Freeze **2,229 input fingerprints** and exact mutable baseline files. Five
actual owner Make commands agree with independent before/proposed compiles.
The strict predicted ELF changes **267 bytes**: only the target body and its
symbol size **12 -> 380**. There are no metadata permutations and **zero
exclusions**. All **6,050 function addresses** remain fixed. All **189,088
protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production completes in **198.13 seconds**, reproducing the predicted
owner, ELF and binary. Existing duplicate `generated_12D630` recipe warnings
and expected whole-ROM checksum exit 2 remain; actual-ELF recount passes.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `9e54b312a2a06b164c8be4919a9f1c0f0db6f8a309bc9756a2ed74ec184958d2` |
| Built binary | `613fb8a8b515a1eb7cc2702f9de39bc084a4d6f06655da1e6f5890537174bbe0` |
| Padded owner | `e33a44e059a3da14e85ba32c817bdef2e9d695abae0003e0613fe04cc06b81a3` |

Eight fresh preinstall checks pass in each environment: mounted
**74.90 s**, sibling **95.49 s**.
Two fresh installed checks requalify Make/full image and guest behavior:
mounted **46.79 s**, sibling **29.95 s**.
The other six methods are explicit preinstall reuses with exact tool/import
fingerprints revalidated. Shared smoke runs are fresh; three unchanged
pure-helper regression receipts per environment are reused separately.
The earlier struct-pointer trial receipts are archived; final receipts cover
the compatible byte-pointer API. An eight-file sibling overlay avoids editing
its **2,434 pre-existing dirty paths**. Missing diagnostic/binding helpers use
explicit read-only mounted fallbacks; Make uses the mounted CLI while the
independent in-process padders use sibling helpers. Codex is sole writer;
zero Claude calls. No host-port source, saves or frozen Release is touched.

Scoped graph: **59,692 nodes / 113,081 links**. All
59,692 old nodes are retained or relocated, with outside-scope
definitions fixed apart from community metadata. Verify 71 owner C positions
and retain 18 assembly pragmas. New tools have 0
indexed nodes under existing submodule filters. Historical excluded nodes are
retained; this is not a full-corpus extraction. Post-commit receipts audit heading
relocations and actual graph-worker completion separately.

Reproduce under prepared WSL PSBBN:

```sh
python3 -m unittest tools.tests.test_game_slot_allocation_1505ed34_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Retained pre-adoption mutable inputs are required in
`conker/build/game-slot-allocation-1505ED34-match/frozen/`. No ROM/ELF binary is
committed; an unprepared clone is not claimed to reproduce this workspace image.

Next: investigate **`func_1509D780`**, 95 words/frame0x18,
in `generated_C9EC0.c`. Its 12-byte zero-return placeholder
still differs at 88 retail-slot words and is untouched/uncredited.
The complete original dispatches selectors 2..41 through `jtbl_8009F1AC`.
Qualify every table entry, packet widths/signs, helper contracts, return ABI and
callers before adoption. Keep protected jump-table data and the wider 80% goal.
