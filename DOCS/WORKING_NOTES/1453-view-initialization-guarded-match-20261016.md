# View Initialization Guarded Match

Date: 2026-10-16. Consumer predecessor **f3369015**, tools predecessor
**dbca3c5**. This completes the adjacent recovery queued in
[Note 1452](1452-frame-timing-frontend-allocation-provenance-20261016.md), not
func_15019F20's separate 141-word timing match or the wider Game queue.

## Result And Interface

Replace func_1501A220's zero-return stub and obsolete commented draft in
conker/src/game_476D0.c with the complete semantic view initializer:

```c
void func_1501A220(s32 viewCount, s32 projectionMode);
```

VA **0x1501A220..0x1501A39C**, ROM **0x476D0..0x4784C**. All **95 words /
380 bytes** are now linked byte-exact with **eight relocation-aware prologue
guards**. The normal-profile C itself has 95 words, frame **0x28**, the retail
saved-register/argument homes and **eight raw differences**. No trailing
padding, private constant pools or compiler-profile change. Do not label
this an unguarded direct C match.

Recovered behavior:

- Publish the requested view count. Allocate one slot for zero, otherwise
  the wrapping unsigned count plus two; request **0x180** bytes per existing
  ViewProjection476D0 and **16** bytes per auxiliary slot. Use the actual
  allocator's signed-word return/argument interface and `(1, 1, 0)` options.
  Publish both results, including zero/high addresses; add no failure shortcut.
- Reload the live count after allocation. For one view, load the signed height
  word, convert to float, subtract 2.0f, multiply by the retail **0.8f** factor,
  truncate, subtract the **signed remainder modulo four**, then divide by the
  original adjusted height. A bit mask is wrong for negative heights.
- Call func_150006E0 with the live category, initialize views through the
  inclusive live count, and reload that count after each callback. Reuse the
  final loaded value for the optional extra `(index, 0, 1023, 0)` call.
- Store flags D_800BE617=1, D_800BE614=1, D_800BE635=0 **before** the final
  func_1510B070(projectionMode) callback. Preserve callback mutations.

The legacy shared variables header incorrectly types D_800968E0 as s32.
Hide only that declaration locally and declare the original f32 constant;
do not change the shared header or create a new constant. Its existing
48-byte owner at **0x800968E0..0x80096910 / ROM 0x23B3A0..0x23B3D0** remains
unchanged, including the factor's **0x3F4CCCCD** bits. D_800BE63C is correctly
accessed as the first signed word of its existing array.

The original direct caller func_15007B3C independently assembles/links to all
**426 retail words**. Its actual four-word cut at **0x15007D90..0x15007DA0**
loads the requested count from D_800BE9E8, calls this initializer and sets
A1=1 in the delay slot. The next instruction calls func_15012F90, without
using a return value. **The current C caller remains a stub.** This verifies
the original boundary, not a working linked startup pipeline.

## Closed Prologue Guards

All differences are confined to **+0x0C..+0x28**. The eight guards derive
from existing compiler words/bindings rather than replacing arithmetic with
retail literals. Routing below is target offset from raw source offset:

| Target | Raw Origin | Action |
| --- | --- | --- |
| +0x0C | +0x14 | Move count-address LO16 setup and binding |
| +0x10 | +0x18 | Save RA |
| +0x14 | +0x0C | Save old S1 before its overwrite |
| +0x18 | +0x1C | Save S0 |
| +0x1C | +0x20 | Home incoming A1 |
| +0x20 | +0x28 | Store count through equivalent incoming A0 alias |
| +0x24 | +0x24 | Test equivalent incoming A0 alias |
| +0x28 | +0x10 | Copy A0 into S1 in the branch delay slot |

The count HI16 stays at +8; its LO16 moves from +0x14 to +0x0C. Frame size,
saved homes S0/S1/S2/RA at SP+0x18/+0x1C/+0x20/+0x24, incoming second-word
home SP+0x2C, all calls, branch displacement and the other **87 raw words**
are unchanged. Full memory/GPR/FPR state agrees at the actual prologue join
for 420 cases. Raw instruction-fault prefixes are deliberately **not** claimed
equivalent; the normalized instructions reproduce literal retail fault order.

Sixteen complete-owner source screens distinguish the scaled-height temporary,
size expression and live-count carrier. Reusing the incoming count parameter,
the named scaledHeight and sizeof the existing view type gives the selected
95-word/eight-difference form. Repeated size ternaries exceed the slot and
are rejected. These shape screens alone are not semantic qualification.

## Fresh Qualification

Eight focused pre-install tests pass in **18.122s**. After the normal build,
all **11 final tests pass in 41.745s**:

```sh
python3 -m unittest tools.tests.test_game_view_initialization \
    tools.tests.test_game_view_initialization_installed -v
```

- **1,704** three-way guest cases (852 fixtures, two stack phases) compare
  retail, raw C and normalized instructions, ordered callback arguments,
  pre-callback 264-byte snapshots, public writes and terminal complete memory,
  GPRs and FPRs. Each emitter dynamically visits all 95 words.
- **852 native32 cases each at O2 and O0**, with UBSan, actual separate C
  body units, full public-region canaries and callback snapshots. No -fwrapv
  requirement. Preserve negative-zero bits; qualify NaN class, not payload.
- Seven compiled semantic controls fail for measured argument/snapshot
  differences: cached loop count, cached single-view gate, unsigned remainder,
  missing extra call, wrong size, wrong height and late flags. No compile
  failures, signals or undefined behavior count as effective rejection.
- **420** raw/normalized prologue joins cover full-width incoming words, two
  stack phases and three previous S1 values; preserve old S1 before copying.
- Reject all 95 raw-word corruptions, all 26 binding corruptions plus an extra
  binding, a private pool and 72 guard-field corruptions. The real padder also
  rejects wrong expected words/relocations.
- Three independent original-assembly links and three normalized rebase links
  agree across all 95 words, including moved LO16 and HI16 carry boundaries.
- Verify the full original caller and **40 actual call-cut cases** across ten
  opaque-provider mutation modes. Two high-count cases qualify three-call
  prefixes only, not billions of iterations or dynamic index wrap.
- **128** normalized instruction-fault prefixes match retail complete state.
  Hardware exception/FCSR behavior and portable C fault semantics are not
  emulated. Providers are opaque contracts, not the actual allocator/renderer.

The initial caller fixture needed explicit ELF function type/size directives:
the existing glabel/endlabel assembler macros do not emit those attributes.
That fixture-only failure was corrected before the passing pre-install run;
original assembled instruction bytes did not change.

## Complete Image And Counts

Before installation, independently relink the frozen predecessor and the
new normalized owner into the **entire ELF**. The predicted image changes
only **298 target code bytes and two target symbol-size bytes**, extent
12 -> 380: **300 changed ELF bytes**, zero metadata permutations/exclusions.
The subsequent normal build exactly reproduces that first prediction.

```sh
python3 -m tools.experiments.game_view_initialization --prelink
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Both 3,257,636-byte images have complete hashes:

- Before: **44fa0f9f11ce36d6aad05a9214d8b025c687e54bb6dbf9e857386e2f47f3ebd3**.
- After: **c25f1fbae94e8c9b8d29e63636728c7d0b5fdb46028ab3549edd44fea03632b2**.

The installed checks protect all **114** live inputs, accept only the exact
successor, retain all **111** other inputs and the literal old guard prefix,
and reject source/image/symbol/binding controls. All **ten owner neighbors**
keep their raw words/bindings and diagnostics remain empty. Protected data
layout stays **189,088 bytes / 720 owners / zero different bytes**. No section,
unrelated body, symbol serialization or private data change is excluded.

Fresh official totals: Game **2,931/4,828 (60.71%)**, overall
**3,604/5,501 (65.52%)**, still different **1,897**, address drift **zero**.
Init remains 492/492 and Debugger 181/181 byte-exact among C functions.
Conversion remains 5,501/6,044 functions and 86.04% bytes overall; the stub
already counted as C. Root README changes only its Game/Total matching rows.

## Tools Bank And Next Work

Tools **51ebd75c07ba7a26d51be88df83b877d52595146** banks the six new files
before the consumer pin. All six are byte-identical in the active checkout
and older mirror; Windows AST passes for all 12 copies. Eleven shared padder
tests pass in each checkout (0.030s + 0.031s active; 0.033s + 0.018s mirror),
and make tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, every one of its **887** initial
dirty-file hashes and **893** final dirty paths. Do not commit/reset it.
Zero Claude calls, no push, host-port change or frozen Release action.

Next recover adjacent **func_1501A39C**, still a zero-return stub in the same
owner: **61 retail words / 244 bytes / frame 0x18**, VA
**0x1501A39C..0x1501A490**, ROM **0x4784C..0x47940**. Retail iterates **two**
cursor/output rows (not the obsolete draft's three), emitting five graphics
commands per row and publishing each resulting cursor in the loop's delay
store. The view address advances by **0x10** per row from D_800BE628+0x40,
not by the initializer's 0x180 allocation stride. Audit table/output aliases,
SDK command widths, saved S0..S4 lifetimes and the actual interfaces before
installation. Original calls exist in func_1501878C and func_1501C880; current
C also calls it from func_150186D0. The old draft's Gfx * return is unproven.
Keep timing's 141 differences, remaining view providers, the wider Game and
additional-source queue separate. No full startup, frame or gameplay claim.

Follow-up completed in [Note 1454](1454-two-row-display-list-setup-guarded-match-20261016.md):
the two-row display-list setup is all 61 words guarded-exact. Continue the
adjacent 124-word func_1501A490 scissor/cursor stub; timing stays open.
