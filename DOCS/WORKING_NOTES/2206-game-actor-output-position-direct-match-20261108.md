# Actor Output Position Direct Match - 2026-11-08

`func_1512623C` replaces its false zero-return placeholder with the complete
matrix-point/fallback-position query. The typed C body emits all **79 words /
316 bytes** directly, with the original **0x48-byte frame**, register roles,
stack homes, branch delays and floating operation order. **No guards**,
insertions, omissions or profile changes are used. Guard history is unchanged.

Production: Total **4,275 / 5,513 (77.54%)**, Game **3,602 / 4,840 (74.42%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,238** converted functions still different and **136** more exact functions
needed for 4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Recovered interface and ordered behavior

Owner `conker/src/game_14FF90.c`; original
`conker/asm/nonmatchings/game_14FF90/func_1512623C.s`.
VA **1512623C..15126378**, ROM **1536EC..153828**. Interface:

```c
void func_1512623C(struct127 *actor, ActorPositionMetadata14FF90 *metadata,
                  s32 category, f32 *x, f32 *y, f32 *z, s32 alternate);
```

The local metadata view describes the measured **signed halfword at +0x114**.
The legacy camera field points to an overly broad `struct127`; its existing
float description at that offset is not used for this query. No shared
structure/header is changed. Actor coordinates are +0x14/+0x18/+0x1C, and
the matrix pointer is +0x1D4. Matrices use a measured **0x40-byte stride**;
the legacy `struct255` size is unsuitable for array indexing, so the source
uses a byte pointer and explicit offset.

1. With a nonnull matrix pointer and **any nonzero seventh argument**, choose
   slot **3**, input point **(0, 20, 0)**. This branch skips the category test.
2. Otherwise, with matrices, seventh argument zero and full-word category
   **0x1B**, choose slot **4**, input **(0, 116, 130)**. Category is not narrowed
   to a byte. The initial private handoff incorrectly gave category 27
   priority; re-reading the branch at 15126288 corrected that before drafting.
3. Call `func_15143134(input, output, liveMatrices + slot * 0x40)` for a
   selected point. Read/store output X, then Y, then Z individually. The
   original homes X at incoming +0xC and its internal fallback flag at SP+0x44,
   then reloads them after the helper. The other output pointers remain in
   incoming +0x10/+0x14 homes.
4. With no selected point, store live actor X first. Then read live actor Y
   and the signed metadata height, calculate the separate single-precision
   multiply by **0.75f** and add, and store Y. Only afterward read/store Z.
   Early Y/Z snapshots change behavior when outputs alias actor coordinates.

The selected source keeps separate, meaningful `offset` and `matrix` steps
before the helper call. These recover the original frame and setup schedule;
no artificial storage or padding is added. Its complete raw SHA-256 is
`66b331530a26fc38f62feb111493042d85ddb68019013122ea5f393284241f67`.
The only relocation is R_MIPS_26 at **+0xAC**, to `func_15143134`.

## Actual callers and return-use proof

The aligned full-ROM census finds **two direct JAL entries**, both inside
original `func_15126378`, and no aligned entry/interior data pointers:

- Call **15126694 / ROM153B44**, argument window
  **15126668..1512669C**, 13 words.
- Call **15126BEC / ROM15409C**, argument window
  **15126BB0..15126BF4**, 17 words.

Both pass actor from parent SP+0xC8, metadata from camera+0x3D4, output
pointers camera+0x2F8/+0x2FC/+0x300, and seventh argument
`camera->flagsAt5F0 & 0x10`. First-window category loads from parent SP+0xB4
in the call delay; the second keeps the live A2 and stores it to that home.
All 13/17 window words execute in connected tests. The parent remains a C
placeholder; these original windows do not establish full-parent recovery.

The original leaves incidental V0=1 on normal fallback and V0=0 on the
selected-point path, but both callers ignore it. A bounded control-flow
liveness audit explores both branch edges after each call. The first reaches
the next call at **1512669C** before any V0 read. The second reaches either
an overwrite at **15126C7C** or the next call at **15126CE4**, also without a
V0 read. These audits visit 2 and 37 instructions respectively and reject
injected V0 uses, including a branch-delay use. A `void` C interface recovers
the retail control register and branch shape; an integer-return draft does
not. Incidental machine-state preservation is tested separately.

## Owner, padding and complete image

This is an ordinary C owner with one retained GLOBAL_ASM routine,
`func_151279A0`, rather than a text-only generated slice. Its assembly input
is frozen and unchanged. The 45-function owner preserves all **44 raw and
padded neighbors**, pools and register union. Its **five inherited compiler
warnings** are compared as exact normalized diagnostic sets; none is added.

The production `pad_c_object` path retains the existing oversized neighbor
`func_15125490` (104 compiled bytes in a 100-byte retail span) and its overflow
trampoline. It is not trimmed or excluded. The actual five-command Make
recipe, including assembly preprocessing/postprocessing, emits the exact
predicted complete owner. The independent generated-slice padder verifies
the **isolated target** against its original 79-word slot. It does not support
that neighbor's established overflow layout, so no whole-owner equivalence
between the two padder algorithms is claimed.

Independent whole-ELF prediction accounts for **230 changed bytes, zero
exclusions**, with no metadata-name reordering. Only this target body and
symbol extent change; all other bytes, including the existing overflow
region, are protected by the literal comparison. All **6,052 linked function
entries** retain their addresses. Protected data remains **720 owners /
189,088 bytes**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Validation and limits

Both tools environments pass eight fresh focused checks before installation
and eight after installation, sequentially, with identical detailed receipts:

- **3,042 direct cases per body**, all 79 words visited, alternate/category
  priority and width boundaries, signed height extremes, modeled nonfinite
  values, and unmapped metadata/coordinates on paths that do not read them.
- **640 output/metadata/private alias cases per body**, **1,408 fired literal
  fault-prefix triples** and **68 delay-slot cuts**. Original/raw/padded
  complete machine states agree. Guest-private aliases and instruction fault
  order do not establish portable C fault behavior.
- **144 cases per body through both original caller windows**, connected to
  the actual matrix helper, plus the effective return-use audit controls.
- **162 helper cases per body** execute original **func_15143134**, whose
  complete 98-word predecessor ELF body equals retail. Both floating and
  fixed matrix formats are covered. **83 helper words** are visited; the
  remaining paths include zero/null-point behavior unreachable from these
  fixed nonzero query points. Existing conversion/affine leaf providers are
  bounded; full SDK/hardware/gameplay execution is not claimed.
- **Nine independent GNU links in three jump regions**, **144 cases per
  body**, and the direct R_MIPS_26 binding checked at each layout.
- **Twelve compiled incorrect implementations** fail on public arguments,
  input vectors or memory: priority, narrowed category/alternate, wrong
  slots/stride, signedness/scale, early Y/Z reads, wrong point and omitted
  helper. Physical private-buffer placement is ignored in those negative
  comparisons; private helper-home mutations are excluded as counterexamples.
- Native32 **O0/O2/O3 each pass 25,920 cases** with trap UBSan, typed seven-
  argument calls, actor/metadata offset assertions and complete actor,
  metadata and output canaries. All 12 controls fail observably in each
  profile. Native aliases use actual float fields; guest-private and metadata
  type-punning aliases, and hardware NaN/FCSR behavior, remain outside claims.

Production object/ELF equal the independent prediction and linked recount.
The existing whole-ROM checksum mismatch still makes `make all` exit 2;
target build/link/progress and recount pass. The five existing C diagnostics
and duplicate generated_12D630 Make warning are unchanged. Shared tool smoke
is fresh in both copies; three unchanged regressions per copy are reused by
exact helper/test fingerprints and are not described as fresh runs.

## Bank and next boundary

Receipts: `conker/build/game-actor-output-position-1512623C-match/`.
The 105 frozen source/compiler/header/ROM/layout/caller inputs are audited
through adoption. The sibling tools checkout's 2,434 inherited dirty paths
are preserved, and the host Release remains frozen. Tools commit before the
consumer pin. Scoped Graphify refresh retains existing unscanned nodes
with evidence; it is not full-corpus extraction.

Next: **func_1514DE94**, owner `generated_179F30`, the next measured 79-word
unmatched Game routine. Audit its complete retail body, real ABI/callers and
owner/compiler profile before drafting, adoption or credit. The 80% goal
remains active.

Production ELF SHA-256: `ae6816b7fc062f1216e06bf8692c18182375b9649d6ae2cc4d25b9e703a5eb55`.

Production guard SHA-256 (unchanged): `b6321a2e129ea7f0550984349d4cdab102ff203b44de7fb0ee9bea04ddd89be0`.
