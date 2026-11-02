# 1978 - Resource-header scan recovered as a guarded byte match

`func_15003570` now matches all **62 retail words**, with its natural **48-byte
frame**. Semantic C restores the original explicit alignment branch;
**19 checked guard rows** restore bounded register roles, independent schedules
and the endpoint relocation alias. Actual Make and the independent Native ELF
recount confirm **4,045/5,507 (73.45%)**, Game **3,372/4,834 (69.76%)**, zero drift
and 1,462 different. One match is added; **86 more** are needed for the 4,131
threshold. The wider 75% objective remains active.

## Contract and source recovery

Owner `game_305D0`, source `conker/src/game_305D0.c`, VA
`0x15003570..0x15003668`, ROM `0x30A20..0x30B18`. Keep `void(void)` and the
existing shared unsigned-halfword table declarations. The earlier semantic
recovery and complete lifecycle fixture are documented in [Note 968](968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md).

Allocate `(16,1,2,0)` once. Starting at `D_1A37E0`, process all **7,762 records**.
For each, capture the low address bit, align the source down, and request sixteen
bytes into the same buffer with DMA mode 1. Ignore its returned status. Assemble
header bytes 0/3/1/2 as a big-endian word, read the current unsigned compressed
length **after DMA and before publishing the extent**, truncate with a halfword
store, then advance the logical unaligned source by that length. Zero lengths
still perform DMA and publish an extent. Free the original buffer after the
complete table. No allocation-failure guard or extra extent validation is added.

The old C was 58 words/frame48/54 real differences. Restoring the explicit
odd-source if/else gives 62 words. Moving constant pointer setup after allocation
and using the natural big-endian expression reduces the raw gap to 18 words.
Header/advance inlining, scalar signedness, pointer-declaration order, assignment
order and a register storage hint were screened without improving this fit.
No hint is retained. The source uses the real array endpoint `D_800B87A0+7762`;
no padding, physical register binding, inline assembly or compiler profile change.

Raw isolated payload SHA-256: `6c9da53b1f6b2b86f923c1b34b061e45a97035ddc42b580b4eef5a02f4b8447a`.

## Derived layout, not a copied replacement body

The 19 CSV rows consist of 18 instruction-word differences and one relocation-only
row. A standalone derivation transforms the source-emitted words and is then
compared with independently assembled original code:

- Swap S2/S3 only across their active cursor interval, preserving original caller
  saves/restores. Length and extent cursor roles move together.
- Restore the anonymous header pointer V3->V0, assembled value A0->V3 and captured
  advance A1->T8 in their bounded lifetimes; normalize the commutative header
  address addition. Every use is accounted for.
- Swap independent LO completions at **+0x4C/+0x54**, extent increment and value
  addition at **+0xB0/+0xB4**, and length increment and extent store at
  **+0xBC/+0xC0**. No instruction is inserted, deleted or moved across a call.
- Rebind endpoint HI16 at+0x40 and LO16 at+0x4C to `D_800BC444`, removing the
  original array-end addend15524. Before and after, the retained alias is exactly
  extent base+15524. Three GNU layouts independently rebase the length table,
  code, source parity and extent/end group, including HI/LO carries.

All 62 normalized words and relocation bindings equal original assembly. Exact
expected words and bindings guard every changed row; the prior CSV is an exact
prefix. The raw C has the original length/frame already. Shared headers,
padders, Makefile and profiles are unchanged.

## Fresh execution checks and limits

- **Six complete guest scans / 18 original, raw and normalized executions** visit
  all 62 words and every one of 7,762 records. They cover three layouts, zero and
  high-bit lengths, source parity, current/next-length and extent mutations from
  DMA, and scratch buffers aliasing either table. The synthetic DMA stream uses
  an independent logical cursor, never a compiler-selected register. Complete
  normalized bounded GPR/FPR/HI/LO, memory, calls and access traces agree; raw
  final state also agrees. A target-specific 600k integer-step bound covers full
  scans without changing the shared emulator's 50k limit.
- **38 access-prefix pairs** compare original/normalized bounded machine state.
  **Three NULL-allocation executions stop at the first DMA-call prefix**, before
  an invalid header read. This does not claim graceful failure. Raw fault-state,
  PC/BD parity, real allocation/DMA/free implementations and hardware are not
  newly qualified; those providers remain explicit mocks.
- Native32 **O0/O2/O3 each pass two complete scans /15,524 entry checks**, plus
  the NULL first-DMA prefix, with UBSan and table/buffer fences. Nine effective
  controls reject missing alignment, ignored header skip, missing skip advance,
  signed lengths, pre-DMA cached lengths, wrong byte order, short table count,
  missing free and an invented NULL gate. The established lifecycle fixture is
  reused with the actual selected body substituted.
- Complete aligned ROM census finds one JAL at **ROM0x34D58 /VA0x150078A8** and no
  direct J/pointer literal. The original 124-word `func_15007830` still equals
  its retained slot. Its real five-word window runs **two complete cases /six
  executions**, connecting the target, following flag clear at `D_800BEAAB`,
  and next helper call. All window words execute, and the target result is not
  consumed. Full startup execution and the next helper implementation remain
  outside this qualification.
- Both raw/padded owners retain **eight neighbors**, identical pools and zero
  diagnostics. The actual **three-command plain-owner Make recipe** reproduces
  the qualified padded object literally. No GLOBAL_ASM body is involved.
- Each tools copy passes **five focused tests and shared checks before and after
  installation**, plus **23 existing metadata/cache lifecycle checks afterward**,
  without skips. Public target checks freshly compile, pad and relink the three
  layouts. The existing lifecycle fixture keeps its other bodies/measurements;
  only this target's raw 62/frame 48/18-difference measurement and digest advance,
  with a checked role/schedule transform to the exact production slot. Its guard
  check requires the full frozen CSV prefix plus exactly 19 target rows. Consumer
  root selection now respects the existing test environment for the older mirror.
  Routine work uses zero Claude calls.

## Literal image and closed linker metadata accounting

The frozen baseline ELF is
`d84330cbf2a3b42de99a5866420c428b00e42a6735f43a6601c76e4235255996`.
The target's248-byte slot is replaced and its symbol size changes **232->248**.
Private linking also reverses the adjacent `n_alSynFreeVoice` / `D_8009E694`
symbol/string ordering. The independent predictor serializes exactly those two
16-byte records and their adjacent 28-byte string block from the prior image,
checks unique name offsets and adjacency, and proves the complete named-definition
multiset unchanged. It rejects an unexpected ordering or alias into the strings.
No entire section or metadata region is excluded. An initial target-only image
comparison caught this ordering change; the failed prediction is retained.

Actual production ELF equals that complete prediction literally. All **6,052
function addresses**, **6,051 other bodies**, ELF length, map and protected
**189,088 Game bytes /720 owners** stay fixed. The 17,732-file seal audit permits
only source, guard CSV, owner object, ELF and the reviewed legacy test in both
tools copies before documentation. No dependent-object delta is excluded.

Production ELF SHA-256:
`f95f2f13f43d030328e6432e0240099f9abae1a5a5133719f649dd7cad72cf2c`.

Stage `conker/build/game-resource-header-scan-15003570-match/` retains frozen
inputs, **42 immutable preparation pins**, source screens, derivation, original
objects, complete runtime receipts, failed/successful image predictions, Make
commands/object, production and Native recounts, seal and handoff. Preparation's
first LO-swap offsets were corrected from live disassembly before the successful
+0x4C/+0x54 derivation. Four new public tools modules and one scoped legacy test
update support this match. The **14-file AST refresh** retains all old nodes and
valid edge occurrences, with no obsolete type edges to retire: this function
already had its void interface. Modified legacy-test source positions are updated
from its own tools history. Zero LLM tokens; no full-corpus extraction or global
reclustering. README changes aggregate rows only. Commit tools before consumer;
no push. Existing mirror edits, archives, private candidates and host Release stay
preserved. The inherited duplicate-recipe warning is not called a clean build.

Next ordinary unmatched candidate: **`func_150488C8`**, a 58-word retail slot with no frame in
`game_75C90`. Audit its signed scalar interpolation, unsigned lookup values,
endpoint path, truncating index, float32 operation order and caller input domain.
Unreachable unsigned-conversion blocks must remain emitted. No C body, runtime
qualification or matching credit is installed for it here. Historical full-image
fixtures and parked candidates require explicit rebase before reuse. Continue
toward the complete 75% objective.
