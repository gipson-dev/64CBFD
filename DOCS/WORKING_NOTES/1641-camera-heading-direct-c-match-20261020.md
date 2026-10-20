# Camera Heading Direct C Match

Date: 2026-10-20. Consumer predecessor: `41ea23d7`; tools predecessor:
`12b5844`. Tools **c6aefcc** are committed first. No push.
The **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_151220D0`'s zero-return placeholder in
[generated_14F580.c](../../conker/src/game/generated_14F580.c) with the complete
camera-heading update. Preserve the address-based name, use the existing
`struct108` camera and `struct17` vector, and add a purpose comment.
VA **151220D0..15122170**, ROM **14F580..14F620**.

All **40 executable words / 160 bytes**, **40-byte frame**, three call
relocations and the global's HI16/LO16 pair emit directly from normal **IDO
O2/g3**. The first semantic draft is exact: no guards, profile changes,
physical register bindings, dummy locals or shared-header changes.

Read the descriptor as an **unsigned halfword**. If mask **0x4** is clear,
obtain `current - origin` through `func_15048F90`, then add late reads of
`target.x - current.x` and `target.z - current.z`. Preserve the vector Y.
Call `func_15048FC8` for the X/Z heading, store degrees at camera+0x37C,
then load `D_800A3460` and store the float32 product at +0x39C. The constant
is **0x3C8EFA35**, the original degree-to-radian factor. This is not a length
calculation. Always continue through `func_15122980`, including the gated path.

The existing camera's +0x2C8/+0x2D0 fields are declared as raw words. Local
float views preserve their bits without changing the shared layout.
The original incoming camera home is **SP+0x28**; the local vector is at
**SP+0x1C**. Both helper calls may clobber caller-owned registers.

## Focused Qualification

[The qualification module](../../tools/experiments/game_camera_heading.py)
freezes **15** source/header/assembly/image/build inputs.
[Eight tests](../../tools/tests/test_game_camera_heading.py) pass in both
tools copies, before and after installation, without failures/errors/skips:

| Stage | Primary | Older Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 7.209s | 7.043s |
| Installed source | 8.569s | 9.512s |

- **680 cases / 1,360 original-versus-C modeled phases** compare complete
  modeled state, packets, late reads, both stack alignments and clobbers.
  Visit all 40 target words. Sweep low/high descriptor bytes, finite float32
  cancellation, subnormals/signed zero, provider mutations and heading values.
- **652 native32 cases**, at O0/O2/O3 with trap UBSan and FP contraction off,
  validate independent float32 reference results, vector pointers/order,
  live fields, unchanged descriptor/pointer and object fences. The native
  record is an independently checked 32-bit subset; emitted IDO instructions
  separately establish the real shared-header offsets.
- **Nine compiled semantic negatives** all compile and reach rejection23.
  An additional guest store-order negative rejects loading the factor before
  writing degrees; **56 guest alias phases** cover degree/global overlap.
  The synthetic global/object overlap is not claimed as a portable C object.
- Scan all pristine functions and aligned ROM pointers: both direct JALs are
  `func_15126138` at **15126218** and `func_151283B8` at **1512846C**;
  no aligned literal target pointer is found. The first run correctly failed
  its incomplete caller inventory; expand coverage before installing.
- Execute the complete **67-word dispatcher in 52 phases**, and the complete
  **65-word camera parent in 88 phases**, including 40 reaching this routine.
  Check mode/descriptor/actor gates, changed-position bookkeeping, restored
  camera argument and unconditional parent continuation. Preparation,
  other dispatch targets and the parent's finalizer remain bounded providers.
- Three independent GNU call/global rebases pass **51 phases**, including
  signed LO16 carry boundaries, and exact original/C words for all bindings.
- Execute all **14 original vector-difference words** and all **56 original
  angle-helper words** in **18 phases**, including zero and signed quadrants.
  The lower arcsine call uses bounded host asin after the actual guest ratio;
  its original polynomial and hardware FCSR behavior are not executed.
- Execute the original final helper's **DC==4 gate/continuation** in eight
  phases: all **20 reachable words** and its three lower call packets.
  The non-DC4 branch and lower update bodies are not executed or claimed.
- Nine strict-image negatives reject header, target/unrelated code, data,
  extent, reordered symbol/string corruption and truncation/append changes.
  Both shared tools checks pass. Native/model checks do not establish
  hardware/MMU/FCSR, malformed-memory, full-gameplay or host acceptance.

The mirror baseline is **ddbdd16**, with **1,494** existing dirty paths.
Preserve every status/hash and HEAD, add only these two absent task files,
verify both copies byte-identical and all four files AST-valid. Final mirror
dirty count is **1,496**; do not commit/reset that independently dirty mirror.
Broader unchanged suite receipts are reused through the strict source/image
proof, not reported as fresh reruns. Routine task: **zero Claude calls**.

## Production And Closed Metadata Accounting

Preserve the one other raw/padded owner function, bindings, pools and compiler
diagnostics. The actual Make path has **three productive commands** and its
normal O2/g3 raw/padded output matches the independently qualified objects.

The first new reference to the already-defined `D_800A3460` rotates a single
three-entry symbol bucket from **D_800A3460, D_80091710, func_150097CC** to
**D_80091710, func_150097CC, D_800A3460**, with exactly corresponding string
records and st_name offsets. No names or named definitions change, except
the intended target extent **12 -> 160**. Predict this precise permutation
from the frozen predecessor; do not exclude symtab or strtab.

Production passes in **26.303s** and reproduces the independent prediction
exactly: **177 changed ELF bytes = 130 code + 47 metadata**. Metadata includes
the target size and this closed permutation. **Zero metadata exclusions**.
All **6,055 other bodies**, **6,056 addresses**, **189,088 protected Game-data
bytes / 720 owners**, ROM, original assembly, shared headers, guards, Makefile
and progress CSV remain fixed. The inherited duplicate generated_12D630
recipe warning remains; this is not a warning-free build.

ELF SHA-256:
`16cb0e775581a68a4fca982d44748a59308d69d8343c022e6ca2c6fad4f77af2`.

Fresh standard full matcher: **3,706/5,505 exact (67.32%)**; Game
**3,033/4,832 (62.77%)**; **1,799 different / zero address drift**.
Init remains 492/492; Debugger 181/181. Converted counts/bytes are unchanged.
The 75% threshold is 4,129, leaving **423** more matches. The ELF-pinned queue
has 1,665 placeholders, 125 semantic/other and nine unlocated source shapes;
these are triage screens, not installation authority.

## Next Target

Queue **func_150C5BD4**, `generated_F2820.c`, VA **150C5BD4..150C5C74**,
ROM **F3084..F3124**, **40 words / frame24**. Inspect its attachment pointer,
identity byte, optional transform table and `func_15143134` interface.
Preserve the repeated pointer reads, Boolean return and branch-likely paths,
including three duplicate loads in the original slot. No draft, installation
or matching credit is claimed for it. Keep `func_1508CAD8` queued separately.
