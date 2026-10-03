# Init Compiled Guest Builder Differential Execution

Date: 2026-10-03. Baseline: `dee7bf0`.

Follow-up: [Note 819](819-init-compiled-guest-stream-core-and-fixed-initializer-qualification-20261003.md)
extends the guest-only control flow and qualifies connected stream/core vectors
and compiled fixed initialization. The retail oracle remains unchanged and
all builder comparisons are rerun. Original-entry/hardware gates remain open.

## Result

The actual IDO-generated builder now executes in a bounded big-endian MIPS
instruction model and agrees with the retained retail assembly model. This
closes a missing guest-codegen execution check for the builder only; previous
native C qualification and guest size receipts did not execute these words.

Six freshly compiled and linked images cover frame baseline, aligned/end
cursor and packed/remaining cursor, each at O2/g3 and O1. Thirty-one input
cases execute against all six images: 186 compiled guest builder comparisons.
Return, root/width, allocation, written table bytes and physical scratch agree.
Saved O32 registers and SP restore correctly; measured stack descent remains
within the receipt's conservative builder direct-call frame bound.

No candidate C, production source, compiler profile, word guard, assembly
ownership or README count changes. Smallest text remains 4,160 bytes, 176
over retail, before original-entry adapters. Pending Game edits are excluded.

## Test-Only Guest Harness

`init_decompressor_guest_oracle.py` reuses `BuilderFixture`'s low-word integer
execution, direct calls, return handling, branches and delay slots. The guest
subclass adds only SLTIU, SLTU, XORI and big-endian SWL/SWR forms needed by the
compiled builder profiles. It does not alter the retail reference interpreter.
Unsupported instructions continue to fail rather than silently acting as NOPs.

A structured ELF32 section/symbol reader loads newly linked big-endian MIPS
executables. It checks file ranges, symbol tables, section overlap/alignment,
absence of retained relocations and the named builder entry. This is a test
section loader, not an operating-system loader or complete N64 emulator.
Code/rodata are read-only; runtime writes are restricted to explicitly owned
state, stack, frame, workspace and root/width buffers. Missing reads fail.

The test driver compiles each shape into a temporary directory and links it
with `mips-linux-gnu-ld`, text at `0x10400000`, data at `0x10500000`, entry
`init_decode_build`. The normal O32 call supplies state/lengths/count/simple
in a0-a3 and bases/extras/root/bits at stack offsets 16/20/24/28. The linked
guest layout must be four-byte entries and forty-byte frame-backed state.
Both compiler profiles and their measured whole-text sizes are required.
Compiler and linker logs must be empty. No stale build object is imported.

The physical caller frame is separately owned at `0x50000`, not the compiled
function's ordinary call stack at `0x10000`. This deliberately tests the
semantic C interface, not the original shared-register/FPR entry ABI.

## Cases And Acceptance Checks

| Group | Cases | Compiled guest runs |
| --- | ---: | ---: |
| Empty/all-zero, small, incomplete and oversubscribed trees; nonzero allocation | 10 | 60 |
| Full 288-cell inputs and explicit base/extra stack arguments | 4 | 24 |
| Depth-sixteen complete tree at five root widths and twelve seeded complete trees | 17 | 102 |
| Total | 31 | 186 |

The full-capacity cases include all-zero lengths, 286 zero lengths followed
by a complete two-symbol tree, and the full fixed 288-symbol tree. Root widths
include 0/1/4/7/9; this is not arbitrary malformed caller-state qualification.
The explicit extra/base case checks non-null O32 stack arguments and leaf
values/operations, not only literal-only tables.

Every run checks:

- v0, root halfword, width word and allocation count against actual retail words.
- Every retail-written workspace byte and the complete frame prefix through
  `0x548`, including table addresses, histogram, sorted cells and offsets.
- All other state fields remain unchanged; a guard after the final allocation
  remains `0xA5`, as do frame guards and original save cells `0xA44..0xA87`.
- s0-s7, gp, sp, s8 and ra match their caller values after return. Writes that
  cross root/width widths, caller buffer ends or read-only image ranges fail.
- Stack descent does not exceed the builder call-graph receipt's frame bound.

Primitive tests separately cover paired unaligned stores at all four offsets,
unsigned immediate sign extension before comparison, unsigned register compare,
XORI, taken/untaken regular/likely delay stores, write guards and truncated ELF.

## Verification

- Initial eight guest/primitive tests pass in 4.008 seconds.
- Final 63 combined guest, retail contract/table, native semantic/frame and
  call/slot tests pass in 21.269 seconds. The final guest runs include tighter
  state preservation, allocation-end guards and compile-shape checks.
- Six final-source objects and six linked images have independently checked
  empty compiler/linker logs. No production build is performed.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- The full all-project suite is not rerun here. Its last complete run is in
  Note 816; this checkpoint changes only test harnesses and documentation.

## Boundary And Next

This is execution of linked guest compiler words under a bounded model, not
R4300 hardware, cache/DMA, exception FR=1 context or original-entry acceptance.
The model remains low-word and shares existing instruction primitives with
the retail oracle; primitive tests and native comparisons reduce, but do not
eliminate, correlated-model risk. No original register/FPR adapter is present.
Only the builder has new compiled guest execution coverage; connected decoder
and core guest paths remain unqualified by this harness.

Next extend compiled guest qualification to stored/fixed/dynamic connected
paths before attempting the original-entry adapter. Keep size/stack fitting,
caller storage ownership and hardware context gates independent.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_builder -v
```
