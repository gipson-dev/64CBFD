# Init Bitmap Address-Difference Induction Trial

Date: 2026-10-04. Starting HEAD: `b6eefb75`.

## New Hypothesis

Continue [Note 951](951-init-resume-conversion-readiness-and-repeatable-audit-20261004.md)'s
Init assessment with a new, isolated `func_10005BE0` compiler-shape trial.
The previous equality forms retain the old cursor through an XOR temporary.
Shape 18 instead samples an unsigned address difference before incrementing:

```c
do {
    *(volatile u8 *)cursor = 0xFF;
    difference = cursor - end;
    cursor++;
} while (difference);
```

Both pointer snapshots use `unsigned long`, checked as 32 bits on the O32 guest.
Modulo subtraction is zero exactly at the captured inclusive endpoint, including
the modeled wrapping-address domain. The count read and original two-based mask
remain after filling; no return value, null guard or finite loop cap is invented.
The hypothesis is late zero-comparison folding, not another Boolean equality
form or end-plus-one sentinel. It is an experiment, not original-C provenance.

## Fresh Measurements

| IDO profile | Body words | Different retail positions | Frame bytes |
| --- | ---: | ---: | ---: |
| O2/g3 | 22 | 21 | 0 |
| O2/g3, no unroll | 22 | 21 | 0 |
| O1 | 33 | 32 | 16 |

Retail has nineteen words. Differences count aligned word positions and excess
body words through the return delay instruction, not semantic differences or
instruction edit distance. All compiler logs are empty; each shape's host
executable passes all 79 bounded fixtures.

O2 removes XOR but strength-reduces the difference into a second induction
variable. It emits `subu a1,v0,v1` once, saves a copy with `move a0,a1` at the
loop head, increments V0 separately and increments A1 in the branch delay slot.
The branch tests A1 rather than the original cursor/end pair. This is 22 words,
not a closed register-renaming or independent scheduling repair of nineteen.
No instruction guards are added, and no production owner/profile changes.

## Qualification

New `tools/tests/test_init_bitmap_address_difference.py` runs the freshly
compiled images through the existing bounded guest/model oracle. It checks
external read/write order and resulting memory, not only final bytes. The
corpus covers all low-three-bit count classes, zero/negative signed counts,
retail allocator counts, single/multibyte ranges, repeated calls, start/end/count
storage aliases, wrapping addresses and reversed-endpoint prefixes. Callee
registers, SP restoration and per-profile frame descent are checked.

Eight new tests pass. They record **501 completed retail/C pairs and six
bounded prefix pairs**, three compiler images total. Output-fence rejection and
the retained hoisted-count mutant demonstrate rejecting oracle paths. These are
model-address-domain checks, not hardware, arbitrary concurrent mutation or
whole-game acceptance.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 18
python3 -m unittest tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

**All 93 combined tests pass in 57.551 seconds, no skips.** The three retained
bitmap suites each record their established 1,002 pairs and twelve prefixes.
The seven inventory/ownership tests again verify all 47 retained assembly
slots, full existing Init code/data and all 189,088 Game-data bytes / 720 owners.
No production relink or newly compiled production-artifact claim is made here.

Per-profile objects, logs, linked binaries and disassemblies remain under
ignored `conker/build/init-bitmap-ordered/shape18-*`.
`address-difference-qualification.json` stores this trial's own measurements and
oracle counts; the driver's shared `measurements.json` can be overwritten by
later retained-shape suites and is not the sole evidence for this trial.

## Decision And Next Work

- [x] Test the new unsigned address-difference folding hypothesis.
- [x] Qualify its executed alias/wrap/stack contract within the bounded model.
- [x] Check all complete emitted bodies against the nineteen-word allocation.
- [x] Reject the oversized form without production edits or broad word guards.
- [x] Preserve exact Init owners/data and unchanged README aggregates.
- [ ] Adopt a small Init candidate only after fitting and contract proof.
- [ ] Resolve connected decoder/glyph fitting and ownership before adoption.

Shape 18 does not move the production conversion boundary. Do not repeat it
unchanged or treat removing XOR as sufficient. Init still has 492 C / 47
assembly entries, and retained boot/hardware/SDK owners remain intentional
assembly. The decoder's freshly verified 528-byte excess and glyph's connected
412-byte budget are unchanged from Note 951.

For the broader decomp goal, the verified next semantic recovery remains
`func_1514470C`, the 218-word descriptor-position writer required by the pending
[Game weighted emitter](950-game-weighted-event-emitter-semantic-recovery-20261004.md).
Its retail body has four descriptor modes, signed dimensions and three output
stores; its current C owner remains a zero-return placeholder. The existing
`func_151436B4` spherical-coordinate helper already has a semantic body, so do
not mistakenly replace it as another placeholder. Recover the position writer
and qualify the actual caller/helper chain before claiming the emitter is
runtime-ready. Existing Game edits are preserved separately, not qualified or
committed by this Init checkpoint. No sibling/Release build, ROM promotion,
hardware/gameplay claim or push is made.
