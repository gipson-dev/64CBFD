# Viewport Initializer Recovery And Matching Boundary

Date: 2026-10-16. Consumer predecessor **566bd258**, tools predecessor
**fed3fa9**. Continue the target queued in
[Note 1456](1456-view-point-projection-direct-match-20261016.md).

**Research checkpoint, not an installed conversion or a byte-exact function.**
The complete semantic candidate is banked in tools. Production game_476D0.c,
the linked ELF, progress CSV, Makefile and guard manifest remain unchanged.
No matching or conversion credit is added, and the wider Game goal stays open.

## Target And Recovered Contract

func_1501A8C0: **373 words / 1,492 bytes**, VA
**0x1501A8C0..0x1501AE94**, ROM **0x47D70..0x48344**, frame **0x48**.
The archive still has GLOBAL_ASM and no C body for this function. Recover the
complete body from retail, not another zero-return placeholder:

```c
void func_1501A8C0(s32 index, s32 layout, s32 depth, s16 transferFov);
```

- Read signed word dimensions from the D_800BE638 / D_800BE650 tables. Nonzero
  layout subtracts two from each dimension; layout 1 applies D_800BE6B8 to
  width and its horizontal base FOV. Preserve individual live base reads.
- Populate aspect/layout fields, base/effective FOVs, half-extents, signed
  origin halfwords and four clip bounds. Origin addressing is **layout*20 +
  index*4** from D_800BE668, not the old ambiguous struct140 layout.
- The fourth argument uses its **signed low halfword**. Nonzero calls the
  real two-word interface func_1501B0A0(index, layout); otherwise derive the
  two axis scales from the reference dimensions without simplifying away the
  original float32 divisions and products.
- Cache each half-angle across sinf/cosf, then reload the live view base and
  extent before storing its projection coefficient. Names for layout-only
  fields describe their observed data role, not a fully accepted renderer API.
- Build the temporary SDK Vp using float-to-word truncation and halfword
  stores. **Depth is a full signed word shifted before narrowing**, not a
  signed halfword shifted first. Copy four ordered words into the selected
  page, then into **!page**, not page XOR 1 for arbitrary nonzero bytes.
- Set scale 1, remember the bounds predicate before clamping, call the clamp,
  forward (index, 0.0f, 0.0f, scale) to func_1510B32C and publish the byte mark.

The scratch owner names the proven width/height, axis scales, status byte,
aspect/FOV/coefficient fields inside the existing **0x180** record. These
proposed declarations and the full body are not installed in production yet.

## Source Fitting Evidence

All source configurations use the normal O2/g3 profile. The first complete
body emits **373 words / frame 0x38 / 198 differences**, with no diagnostics
or private pools. A named origin pair addressed through bytes recovers the
original address-expression shape and reduces the score to **98**, but still
has a wrong 0x40 frame. Do not promote a lower difference count with a wrong
frame or compensate with stack-home guards.

Capturing the reference dimensions, preserving repeated full-word depth
expressions, and recovering the right/bottom source operand order yields the
selected **373 words / frame 0x48 / 49 differences**. The first **94 words**
are exact; the original argument homes, saves/restores and sine home
**SP+0x34** are retained. Raw object SHA-256:
**6cc0dd6c52665773dbb2a5ef7e185af99be4b3aad7ef9a1d14cde4d3ae1e6e3e**.
All **34 relocation bindings** are pinned, and all ten other normal-profile
owner functions retain their literal words/bindings.

There are **170 recorded source configurations**, including all **120**
declaration permutations of the selected five locals. No permutation improves
49. Named border/trig temporaries, split ratio intermediates, width-only
carriers and integer-height carriers do not solve the literal allocation.
These are shape screens, not independently qualified alternate recoveries.

## First Literal Boundary

At **0x1501AA38**, retail emits `mtc1 at,f16` for 0.5f; raw C emits
`mtc1 at,f14`. Stop before **0x1501AA3C**: complete memory, GPRs and access
prefix agree, but the FPR bank does not. The test requires this failure to
remain visible. A passing terminal output must not be called private/fault
matching.

Of the **49** different words, **48 change floating-register encoding fields**;
the remaining word is the commutative address add at **0x1501AE34**:
raw **0x01B01821**, retail **0x020D1821**. This classification is diagnostic,
not proof of one global register permutation. Do not turn it into a blind
patch list. Recover the C lifetimes or prove each closed live interval first.

## Fresh Recovery Qualification

All **seven recovery tests pass in 34.931s**:

```sh
python3 -m tools.experiments.game_viewport_initialize
python3 -m unittest tools.tests.test_game_viewport_initialize_recovery -v
```

- **1,144 paired guest cases**, including **two invalid-conversion prefixes**,
  compare retail and raw C with an independently grouped float32 reference.
  Exercise all **373 root words**, signed/full-word flags and depth, five
  layout choices, high page bytes and overlapping viewport backing.
  Full memory, ordered accesses and helper argument packets agree. Invalid
  conversions stop before the cast result; no hardware exception/FCSR claim.
- **216 paired callback cases** test live view-base/page/FOV reloads and the
  cached pending angle at two stack phases. Positive receipts assert the
  mutation gate actually fires. Bounded helper writes are contracts, not
  claims about natural runtime mutations.
- Execute the actual **44-word bounds predicate and 87-word clamp**. All 131
  words also match the frozen consumer ELF/ROM span. FOV transfer, trig and
  final projection still use explicitly bounded contracts in these tests;
  their complete connected chain is an outstanding installation gate.
- Six independently compiled negatives produce actual output/packet
  mismatches: full-word instead of halfword flag, narrowing depth before the
  shift, page XOR, wrong origin stride, unsigned origin and cached view base.
  An oversized negative is run at a separate code address; an explicit
  overlap guard rejects overwriting a connected helper. No unmapped access,
  compiler failure, signal or sanitizer trap counts as an effective control.
- GNU-assemble the complete original 373-word routine against ROM. Preserve
  all ten normal owner neighbors, reject all **373** word corruptions, **34**
  binding corruptions plus an extra, private pools and a stale source anchor.
  All **130** pinned live inputs remain identical to the frozen baseline.

Fixture repairs, not production fixes: assign callback mode after the reused
oracle constructor so it is not reset; move the alternate bank away from the
simulated stack; and keep oversized negative code disjoint from helper code.
The failed probes are not qualification receipts. No native32, full original
caller, connected complete helper-chain, all-access fault-prefix or linked
installation acceptance is claimed by this checkpoint.

## Bank And Preservation

Tools **54aff6840f8babc0ca85b917f1a26b2614cc0e9e** banks the three research
files before the consumer documentation pin. Both copies pass Windows AST;
eleven shared padder tests pass in each checkout: active **0.031s + 0.020s**,
older mirror **0.030s + 0.019s**. make tools-check passes. Three task-file
pairs are identical. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **911** initial dirty-file
hashes and **914** final dirty paths; do not commit/reset that mirror.

Production ELF remains
**23d5ee08fc033c461872a1e3382969e6cd5587791ff3b4108c1350c08c9962cf**,
owner remains
**6caa0dcc8c1ceaac1b96be30cbbc3d3f50dbc7ae61445c24641a81f036a0a61b**,
guards remain
**23a0277187ad0fb321d436abc593093eb6dea2afa9013ae2c6aea12f1fe5a6b6**.
No normal production build is needed for this non-installed checkpoint.
README aggregate rows remain unchanged: Game **2,934/4,828 (60.77%)**, total
**3,607/5,501 (65.57%)**, different **1,894**, zero drift. No push, Claude,
host-port change or frozen Release action.

## Resume Here

1. Continue **the same func_1501A8C0**, not the next smaller function. Start
   with `SELECTED` and the first F16/F14 live-role boundary at 0x1501AA38.
2. Keep **373 / frame 0x48 / sine SP+0x34 / all saved lifetimes** fixed while
   recovering the scratch allocation. More declaration-only permutations
   repeat a completed 120-case screen; investigate actual value lifetimes.
3. Resolve the last commutative address expression at 0x1501AE34 without
   disturbing the other record reads. No frame/home patches are authorized
   by these partial measurements.
4. Before installation, complete native32 O2/O0/UBSan, real FOV/trig/projection
   integration, actual caller cuts, literal private/fault prefixes, both
   owner selections/rebases and the independent first whole-ELF prediction.
5. Only then install, run the normal build and focused installed suite,
   measure fresh aggregates and advance exact successor fixtures. Keep the
   wider Game queue and timing's 141 differences separately open.
