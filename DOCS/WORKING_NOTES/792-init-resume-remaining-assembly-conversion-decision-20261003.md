# Init Resume: Remaining Assembly Conversion Decision

Date: 2026-10-03.

## Result

The live inventory still contains 47 Init assembly rows / 12,252 bytes.
Two small routines are bounded semantic C candidates, but neither has a
proven matching replacement. No Init conversion is made in this assessment.
The other 45 rows are not a queue of independent ordinary-ABI C functions:
they include original SDK assembly, privileged instructions, shared-frame
decompression, and nonstandard debug/glyph entry contracts.

This resumes the user's Init request. Existing uncommitted Game copy/clamp
work and its documentation are preserved, not banked or reverted here.

## Fresh Verification

- Structured inspection of `conker/progress.init.csv`: 492 C rows / 151,796
  bytes; 47 assembly rows / 12,252 bytes; total 539 rows / 164,048 bytes.
- `make -C conker NON_MATCHING=1 all match-progress -j4` succeeds. Production
  build is up to date; the regenerated matcher reports Init 492/492 exact,
  zero address drift, and zero different C rows.
- All 20 tests across `test_init_mmio_assembly`, `test_init_memory_clear`,
  `test_init_bitmap_assembly`, and `test_init_bitmap_allocator_contract` pass.
- Independent linked ELF extraction matches both complete retail sections:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

The existing duplicate recipe warning remains. These checks do not execute
MIPS hardware, validate gameplay, or establish that every existing guarded C
routine has independently proven semantics. No full test-suite rerun is
claimed for this assessment.

## Conversion Triage

| Group | Rows | Bytes | Next action |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | First bounded C candidate; new compiler/dataflow hypothesis needed |
| MMIO `func_100038E0` | 1 | 44 | Second bounded candidate; preserve volatile width/order and full slot |
| Separated SDK assembly | 19 | 2,288 | Retain original implementations |
| Boot `func_10001000` | 1 | 80 | Retain clear-and-jump entry contract |
| Hardware/context/setup | 8 | 4,376 | Assembly/intrinsic support and connected interface recovery |
| Shared-frame decompressor | 10 | 3,984 | Whole connected-contract project, not leaf substitutions |
| SDK thread queue leaves | 2 | 96 | Retain original assembly provenance |
| Cleanup/debug/glyph | 5 | 1,308 | Recover nonstandard register/link interfaces together |
| Total | 47 | 12,252 | No achieved conversion in this assessment |

Complete names and concrete register/frame evidence are in
[Note 735](735-init-retained-assembly-reassessment-20261002.md); its preceding
48-row inventory predates the successful memory-clear conversion.

## What Has Already Been Resolved

The bitmap's next step is no longer simply "investigate its caller/allocator."
[Note 788](788-init-bitmap-retail-caller-domain-and-edge-contract-20261003.md)
establishes counts 107..362 at the only direct retail resize call and tests
pointer snapshots, post-fill count reload, alias timing, and invalid endpoints.
[Note 789](789-init-bitmap-allocator-provenance-and-rear-bound-correction-20261003.md)
establishes conditional configuration/heap separation for successful allocation
from a valid heap and corrects the allocator's rear-bound C arithmetic.
Indirect/external calls, corrupted heaps, and allocation failure remain outside
that successful-allocation argument.

The outstanding bitmap obstacle is code generation: the completed
[55-shape/profile matrix](751-init-bitmap-loop-mask-profile-trials-20261002.md)
does not reproduce the nineteen-word slot. Its closest listed shape differs
at fifteen aligned positions; that is not a register-only normalization proof.
Retail stores before testing, increments in the loop delay slot, reloads the
count after filling, and decrements the remainder in a conditional delay slot.
Do not add a zero-count early return, hoist the count, or replace this control
flow with broad word guards just to raise C totals.

MMIO must publish `0xBC000C02`, publish halfword `0x4040`, then write halfword
`0x4040` through that address. The retained address lifetime, two constant
materializations, and nop return delay slot still lack a matching C explanation.
The prior [partial-volatility trials](762-init-mmio-partial-volatility-trials-20261003.md)
are completed evidence, not a fresh experiment to rerun unchanged.

## Pick Up Here

1. For a small matching Init conversion, develop a genuinely new bitmap
   source/compiler hypothesis against the characterized contract. Keep trial
   objects separate from production until their full nineteen words match.
2. Require instruction/dataflow equivalence, source-owner extraction, and
   unchanged `func_10005C2C` address before replacing the bitmap assembly.
   Then rerun focused tests, regenerate progress, and compare both sections.
3. Revisit MMIO only with new evidence explaining its eleven-word schedule.
   Otherwise retain it rather than repeat the existing profile matrices.
4. For substantial Init semantic recovery instead, begin by mapping the ten
   decompressor entries' shared registers, stack slots, interior entry points,
   and caller ownership. Establish input/output oracle fixtures before any
   connected rewrite. This is larger interface recovery, not a ready conversion.

If both small candidates eventually succeed, Init would reach 494/539 C rows
(91.65%) and 151,916/164,048 C bytes (92.60%), leaving 45 assembly rows /
12,132 bytes. These are conditional targets, not measured progress. A fully
C-expressed rewrite is a different objective from retaining a byte-exact
retail image; original hardware/SDK assembly does not need to be forced into C.

README aggregate numbers and all production Init source, profiles, and guards
are unchanged. No compiler matrix, host-port build, guest execution, gameplay
qualification, or Release modification was performed.
