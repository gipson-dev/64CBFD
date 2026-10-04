# Init Bitmap Unsigned Induction Guest Qualification

Date: 2026-10-04. Starting HEAD: `6b5593d7`.

## New Hypothesis

Following [Note 940](940-init-pause-resume-conversion-decision-20261004.md),
test whether an unsigned address induction variable or endpoint-derived
countdown changes IDO's inclusive-loop lowering. Prior unsigned comparisons
in Note 927 still used pointer induction and excluded wrapping intervals.
The new forms perform induction in unsigned arithmetic instead:

- Shape 12: capture both addresses as `unsigned long`, store through the
  current address, then compare the old address with end while incrementing.
- Shape 13: capture both addresses, derive `remaining = end - cursor`, then
  store/postincrement while the old remaining count is nonzero.

The guest compile explicitly requires a 32-bit `unsigned long`. The native
host fixture uses its native pointer-sized unsigned long; it does not prove
32-bit wraparound. Both forms retain volatile byte stores, endpoint snapshots,
the post-fill signed count reload and the original two-based mask expression.
There is no zero-count shortcut or narrowed ascending-range predicate.

## Fresh Compiler Results

Retail is nineteen words with no stack frame. Each cell below reports
**body words / differing aligned positions / frame bytes**. Object alignment
after the final return delay slot is excluded from body length, not treated
as free space inside the retail slot.

| Shape | O2/g3 | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| Existing pointer equality control, 1 | 20 / 19 / 0 | 20 / 19 / 0 | 31 / 31 / 16 |
| Unsigned address equality, 12 | 20 / 19 / 0 | 20 / 19 / 0 | 31 / 31 / 16 |
| Unsigned endpoint-distance countdown, 13 | 22 / 21 / 0 | 22 / 21 / 0 | 34 / 34 / 24 |

Shape 12's entire extracted `.text`, including object padding, is byte-identical
to the freshly compiled shape-1 control under all three profiles. It therefore
does not remove the XOR temporary or alter the mask/register schedule.

Shape 13's O2 loop places the cursor increment in the conditional branch delay
slot, but adds the captured-endpoint subtraction, an unsigned nonzero test and
a remaining-count decrement. The resulting loop is still not retail's direct
cursor/end comparison. The O1 countdown also grows the frame from 16 to 24 bytes.
Reject both as fitting improvements; no word guards or production extraction.

## Actual Guest Differential Tests

New `tools/tests/test_init_bitmap_unsigned_induction.py` recompiles and
independently links the control and both trials under three profiles. The
six trial images execute through the existing MIPS guest-fixture interpreter.
The retail control is checked directly against pristine ROM before comparison.

Qualification compares the complete interleaved external read/write trace,
access widths and values, external memory, callee-saved registers and SP.
O1's newly allocated private stack cells are explicitly excluded from external
trace/memory equality; observed descent must match the compiled leaf frame.
Output writes are fenced to the fixture-owned byte set.

- 77 count/endpoint fixtures, each executed twice for every trial image:
  **924 completed retail/C pairs**. Covers counts 1..64, selected zero/negative
  signed-halfword cases, characterized resize counts and 32,767; all eight
  mask remainders, surrounding sentinels and repeat fills are checked.
- Five start-pointer, end-pointer and count-storage alias cases per image:
  **30 completed pairs**. Includes separate high/low count-byte aliases.
- Eight modulo-32-bit wrapping-address fixtures per image: **48 completed
  pairs**, spanning `0xFFFFFFFC..0xFFFFFFFF` then `0..3` in the memory model.
- Two reversed-endpoint cases per image: **12 bounded prefix pairs**. An
  explicit stop gate fires before the seventeenth byte store. Both paths must
  match the first sixteen stores and must not read the count before completion.
  This is not a full 2^32-byte execution or termination proof.

Total: **1,002 completed pairs plus 12 bounded prefixes**. An injected retail
mutation hoists the count load before the fill; the count-alias case detects
both trace and output divergence (`0x7F` retail versus `0x07` mutant). Separate
fence controls reject out-of-output stores. These controls verify that the
alias and write-boundary gates actually reject incorrect behavior.

The three warning-clean native host executables also pass their 79 fixtures
each: 237 host shape/case combinations. Those native tests are distinct from
the guest-pair count and do not establish wraparound or hardware validity.

## Reproduction

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 1 12 13
python3 -m unittest tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract -q -f
```

The final combined run passes **46 tests in 5.079 seconds**, no skips. Eight new tests cover paired
execution, aliases, wrap/prefix behavior, rejecting controls and compiler
receipts; the other 38 preserve the existing focused Init contracts.
Generated binaries, disassembly, measurements and `unsigned-qualification.json`
remain under ignored `conker/build/init-bitmap-ordered/`.

The driver now accepts a selected shape list and records leaf frame sizes.
Its no-argument selection remains shapes 1..11, preserving the previous driver
workflow. There is no change to production compiler flags or link inputs.
`make tools-check` also passes; documentation links and whitespace are checked.

## Decision And Handoff

Retain both as rejected opt-in experiments, not production C conversions.
Unsigned induction alone does not explain retail's nineteen-word schedule.
Do not repeat these shapes unchanged or convert a twenty/twenty-two-word body
with broad instruction replacement. Init remains 492 C / 47 assembly routines;
README aggregate tables remain unchanged.

Before another production conversion/link, finish the preserved Game-data
owner-order repair identified in Note 939 and the build boundary in Note 940.
Its first span gate exposed eight bytes of assembler-only trailing padding
in the `0x236578` owner. Qualify any padding treatment and missing literal
owners without discarding semantic data, then compare the entire physical
Game-data section against retail. That is a distinct unfinished repair, not
an Init regression or a completed build in this trial.

No full production rebuild, guest hardware execution, decoder full-corpus
rerun, sibling-port build, Release change or push is claimed. Wrapping addresses
are abstract fixture addresses, not safe or mapped real-hardware accesses.
