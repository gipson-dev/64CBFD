# Entity overlap collector direct byte match - 2026-11-28

`func_151873E4` in `conker/src/game/generated_1B1600.c` replaces its three-word
zero-return placeholder with the complete **127-word / 508-byte** overlap
collector and output-count updater. VA `0x151873E4..0x151875E0`, ROM
`0x1B4894..0x1B4A90`, frame **32**, **no guards or alignment tail**. Every
bound word emits directly from C. All 31 raw/padded neighbors and pools stay
fixed, including the sequenced N94 actor extents and its two existing guards.

Actual production: **4,728 / 5,528 (85.53%) total**, **4,055 / 4,855 (83.52%)
Game**, Init 492/492, Debugger 181/181. Zero address drift; 800 still different.
Conversion rows, denominators and all guard bytes are unchanged. Exactly one
new match is credited; **248 more** reach the active 90% target of 4,976/5,528.
The related provider's ABI repair earns **zero** matching credit.
Previous consumer `188b9393`; tools `533cccddb0281d5b24e6a79a3dccdb2f3844c43b` was committed first.

## Recovered source and observed ABI

The recovered interface is:

```c
s32 func_151873E4(s32 x, s32 z, s32 halfSize, ClipVertex *out,
                 f32 transform[4][4], ClipVertex *limit, s32 outCount);
```

The function returns the initial count immediately when `D_800DBEF0` is zero.
Otherwise it selects context 2, advances the output cursor by the initial
count, publishes four query bounds using explicit unsigned32 wrapping, and
scans the post-context entity count. Each entity has stride **0xA0**, signed
x/z at +0x10/+0x14, unsigned width/depth at +0x50/+0x52, flags +0x4F and a
disable byte +0x6E. The local `OverlapEntity1B1600` view fills fields absent
from the SDK view; no shared SDK/header change is required.

Disabled entities and flags `& 0x60` are excluded. The larger unsigned extent
forms the four signed overlap comparisons, retaining edge contact and the
retail behavior for negative or wrapped half sizes. Selected indices are
stored as halfwords in `D_800D37E0`. A nonempty list calls the index provider,
copies the **post-provider** context, publishes the selected count, invokes
the vertex provider and adds its returned pointer difference in 20-byte
vertices to the initial count. Empty/negative post-context counts skip the
scan, while a negative nonzero entry count still calls the context wrapper.

The indexed entity expression and explicit max-width/depth ternary recover
retail's pointer lifetime and branch shape. Earlier exploratory forms emitted
125 or 126 words and remain rejected. Source was rebased onto the sealed N94
owner, preserving its explicitly sequenced output stores.

Byte identity alone did not qualify the first draft's last pointer arguments.
Inspection corrected the draft's integer mode/flags to a **matrix pointer**
and **output-limit pointer**. The original provider loads twelve float words
from A2 at +0/+4/+8, +0x10/+0x14/+0x18, +0x20/+0x24/+0x28 and
+0x30/+0x34/+0x38. Its limit comparison uses A3, and its shared return copies
the output cursor A1 into V0. The caller computes matrix stride 64 and output
stride 20, reserving 40 bytes at the limit. Correcting those types/names
preserves all 127 emitted words and the original frame. The precise historical
C spelling remains unproven; the chosen views obey the observed word contract.

## Related provider declaration and fully declared image delta

`func_150A5E44` in `conker/src/game/generated_D3040.c` was an untyped integer
zero-return placeholder. Its definition now agrees with the caller's four
pointer arguments and pointer result. An identical local `ClipVertex` view
keeps the two C declarations compatible without widening shared headers.
Its body remains an explicitly documented **unrecovered null placeholder**.

Under the existing O2/g3 profile, naming the four parameters emits four
ordinary O32 argument-home stores before the old null-return instructions:

```text
sw a0,0(sp); sw a1,4(sp); sw a2,8(sp); sw a3,12(sp)
move v0,zero; jr ra; nop
```

The stub grows from **3 to 7 words**, with no frame allocation. All **16 other
raw functions**, their pools, all original assembly and original addresses
remain unchanged. An independently assembled reference adds exactly those
four stores to the frozen complete padded owner and shortens only the local
zero-fill; it equals the actual selected owner byte for byte. The existing
GLOBAL_ASM recipe is replayed completely, including pre/postprocessing and
all five commands. Its **41 pre-existing odd-FPR assembler warnings** are
retained with the exact four-line shift caused by the added instructions;
there are zero new compiler or assembler warnings.

The unchanged null result is not a recovery of the original 190-word
handwritten provider. That body, its internal entries and larger effects
remain unfinished. There is no provider match credit or blanket exclusion.

## Fresh qualification

- Native SDK32: **2,048 cases per O0/O2/O3**, eight effective semantic controls,
  wrapped bounds, zero/negative/positive counts, unsigned dimensions, edge
  contact, provider mutations and matrix/limit pointer identities. Every
  byte of **5,120 entity bytes, 2,560 vertex bytes, 128 matrix bytes and 64
  list bytes** is checked, together with all published globals and the result.
  Pointer arithmetic stays within valid typed native arrays. Strict aliasing,
  trapping UBSan and LTO type checks remain enabled, with zero compiler warnings.
- A separate native link uses the **actual selected provider owner definition**
  against the recovered declaration in another translation unit. The typed
  pointer interface links and preserves its null result. A deliberately wrong
  integer matrix declaration fails specifically with `lto-type-mismatch`.
- Guest: **896 cases x four streams / 3,584 executions**, comparing original
  GNU-linked retail, raw C, and both complete padded objects. All **126
  reachable words** execute; unreachable index **13** is retained byte-exact.
  **3,652 fault cuts** compare complete literal prefix states across all four
  streams. Nine alias modes include 384 guest-only cases: future entity fields
  overlapping the list, bound/count/pointer metadata, output/list overlap and
  incoming-home mutations. Three sparse pointer domains and two stack phases
  are covered. Invalid typed/private-home aliases are not native-C acceptance.
- Original caller: the complete **711-word parent** is pinned, with its actual
  **45-word window** executed in **756 fixtures x four / 3,024 connected runs**.
  All seven argument words, the three incoming stack words, matrix/limit
  calculations, prior-provider mutations, post-provider reloads, the result
  branch and result store are qualified. Four controls reject wrong seventh
  argument, matrix stride, limit reserve and ignored result. This is bounded
  window evidence, not complete-parent execution.
- The original **eight-word context wrapper** executes all eight words in
  sixteen fixtures, proving A0 forwarding to its opaque setter. The 96-word
  index-provider entry and 190-word append-provider slot are pinned for ABI
  inspection; their larger execution remains opaque.
- Both complete target padders preserve the frozen before object and all 31
  neighbors. The target's actual three-command recipe uses unchanged
  `-O2 -g3 -Wo,-loopunroll,0 -mips2 -o32`. **16 actual GNU links** independently
  rebase all 127 words and 29 binding positions, including signed HI16/LO16
  seams. Thirteen full-image corruption controls reject, including the related
  provider's argument store, extent and symbol definition.
- Independent prediction combines frozen-before C, the **original target
  assembly**, and the provider's explicit four-store ABI reference. Private
  and actual production images agree across **549 changed bytes**, **zero
  exclusions**, both changed extents and ten declared symbol-table record
  permutations with identical named definitions. All other linked bodies,
  addresses, extents, conversion rows, guard bytes and **720 protected data
  owners / 189,088 bytes** stay fixed. ELF SHA256:
  `0d8a0333ffe6d7843af9847714b159f99ff21a3256e282f1867ba75586b7176a`.
- Five packaged tests pass freshly in both tools roots before and after
  installation: **20 fresh checks**, equal reports and audited imports/data.
  Shared `make tools-check` passes. The closed twin uses 2,507 immutable
  dependency hardlinks and twelve independent task-file copies. The real
  tools sibling's native Windows status and all pinned files are preserved.

No Claude call was needed: the provider/caller instructions and discriminating
native type checks settle this routine ABI question. Codex remains the sole
writer. These checks do not establish full provider/gameplay/hardware acceptance.

## Documentation, graph and continuation

The root README receives only its two aggregate matching rows. The detailed
recovery is here, with concise entries in the five current indexes. Scoped
Graphify AST refresh retains prior IDs and qualification metadata, and marks
the related provider as ABI-only/unmatched. It is not a full-corpus extraction.
Actual hook-terminal, graph, immutable-bank and production receipts are in
`conker/build/game-entity-overlap-collector-151873e4-private/`.

The read-only host audit found generated stubs in the two inspected
`intro_effect_dispatch_out` files, and neither definition in the previously
inspected `combined_objpass.c`. That evidence does not prove an active host
implementation. The context-wrapper ABI is distinct from these decomp C
declarations; active host build selection remains unverified. No host edit,
build or launch occurs, and Release remains frozen.

No push or subagent is used. The wider 90% goal stays active. Next qualify the
92-word `func_1500AC14` resource-slot initializer from the sealed N95 bank,
including its provider/return ABI and unsigned-divide trap boundary. Its
read-only handoff is `NEXT_TARGET.md`; no new source or match is credited.
Keep N82 `func_1514EECC` parked
and preserve the separate mixed-boundary handoffs for `func_150AE280` and
`func_150A6760`.

Fresh packaged-suite durations in seconds: pre-primary 206.38, pre-sibling 201.449, installed-primary 194.591, installed-sibling 227.054.
