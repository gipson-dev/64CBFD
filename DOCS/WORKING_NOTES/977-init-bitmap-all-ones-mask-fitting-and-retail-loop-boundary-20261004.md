# Init Bitmap All-Ones Mask Fitting And Retail Loop Boundary

Date: 2026-10-04. Starting HEAD: `a916e9f4`.

Subsequent [Note 978](978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md)
tests the next small Init target with a new grouped-address MMIO hypothesis.
It likewise yields bounded behavior evidence, not an adopted replacement.

Subsequent [Note 981](981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)
fits another nineteen-word body using grouped field reads and the two-based
mask. Seventeen positions and the original loop schedule still differ; its
ordered model qualification does not change the no-adoption boundary.

## Result

Continue the nearest small Init target from
[Note 976](976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md):
`func_10005BE0`, the inclusive bitmap fill and final-byte mask.

**A new unsigned all-ones mask variant fits the complete nineteen-word body,
but seventeen words differ from retail. Reject production adoption.**
The constant-lifetime hypothesis is not confirmed: IDO rematerializes the
all-ones word for the tail instead of preserving it. The one-word reduction
comes from simpler mask arithmetic, not recovering the retail loop schedule.
Older one-based-mask variants also fitted nineteen words; size alone is not
new matching or proof of an independent scheduling-only repair.

The standalone optimized `.text` stays **80 bytes for both new shapes**:
Shape 21 has 76 body bytes plus four trailing alignment bytes. There is no
complete optimized allocation reduction. The receipt and regression explicitly
account for those trailing bytes, not only words through the final return.

Nine new differential checks pass. The final allocation-aware combined suite
passes **119 tests in 64.560 seconds, no skips**, including those nine.
An earlier combined run passes in 66.027 seconds and a standalone nine-test
run passes in 2.338 seconds; these are repeated coverage, not additional tests.
Forty separate disabled-selector preprocessing comparisons confirm unchanged
Shapes 1..20 for host and guest declarations. No production Init owner,
compiler profile, word guard or README aggregate changes.

## New Hypothesis And Controls

The opt-in Shapes 21/22 use the existing guest-width unsigned address induction,
captured start/end addresses, inclusive volatile-byte fill, and late signed
count reload. Both remain void. The guest source checks both address and mask
types are 32 bits; the native source uses pointer-capable unsigned long.

- **Shape 21:** initialize `unsigned int value = ~0u`, fill bytes from that
  value, then when `bits != 0` mask with `~(value << bits)`. All shifting is
  unsigned; no signed-negative left shift is introduced.
- **Shape 22:** same all-ones fill, but keep the original decrement and
  `(2u << bits) - 1` tail. This isolates mask arithmetic from fill-value changes.
- **Shape 19:** freshly compile the retained `0xFF >> (8 - bits)` control.
  Its banked extents/difference counts/frames remain unchanged.

The driver accepts the two new shapes explicitly. Its default Shapes 1..11
selection is unchanged. These experiments do not invent a return value, add
global reads, hoist the count, or modify the assembly owner's declarations.

## Fresh Complete Bodies

Cells are **body words / different aligned positions / frame bytes**. All words
through the final return delay slot count; following object alignment is not
part of the body. Retail is nineteen words / 76 bytes. Difference counts are
not semantic mismatch counts or instruction edit distances.

| Shape | O2/g3 | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 19, right-shift control | 20 / 20 / 0 | 20 / 20 / 0 | 33 / 33 / 24 |
| 21, complemented all-ones mask | 19 / 17 / 0 | 19 / 17 / 0 | 32 / 32 / 24 |
| 22, all-ones fill / two-based tail | 20 / 19 / 0 | 20 / 19 / 0 | 33 / 33 / 24 |

Complete text allocation / trailing bytes are 80 / 4 for optimized Shape 21,
80 / 0 for optimized Shape 22 and Shape 19; O1 is 128 / 0 for Shape 21 and
144 / 12 for Shape 22 and Shape 19. Optimized body savings are absorbed by
alignment; O1 removes sixteen complete bytes but is still far beyond retail.

The optimized Shape 21 loop remains:

```text
li    a1,-1
xor   v0,v1,a0
addiu v1,v1,1
bnez  v0,loop
sb    a1,-1(v1)       # branch delay slot
```

Retail instead uses `sb; bne cursor,end,loop; addiu cursor,1`. The candidate
retains the extra XOR predicate and stores after incrementing through the
adjusted address. Its tail reloads `-1`, masks the late count, shifts in the
zero-count branch delay slot, then complements with NOR and stores. Retail
decrements in that slot and follows with the two-based shift/subtract sequence.
The candidate's only equal aligned words are the final return and its nop.
No broad instruction normalization is justified by a nineteen-word extent.

## Bounded Qualification

`tools/tests/test_init_bitmap_all_ones_mask.py` freshly compiles the control
and both new shapes under all three profiles. Its instruction fixture executes
the six new-shape guest images against checksum-verified retail assembly:

- **1002 completed retail/C execution pairs** and twelve bounded-prefix pairs.
- Complete external access order, width, address and value agreement.
- Positive, zero and signed-negative counts; all remainder classes; repeats.
- Surrounding-byte preservation and captured start/end/count storage aliases.
- Guest-width wrapping addresses in the model, not physical hardware.
- Reversed-endpoint prefixes without an early count reload.
- Preserved callee-saved registers and profile-specific stack descent.
- Output-fence and hoisted-count-load rejection controls.
- Explicit full-slot mismatch, XOR-loop and constant-rematerialization checks.
- Complete text and trailing-byte checks: the optimized whole allocation is neutral.

Warning-clean native compilation passes 79 fixtures for each of the three
shapes: 237 shape/case combinations, 158 from new Shapes 21/22. The native
fixtures do not exercise arbitrary pointer wraparound or reversed endpoints.
All outputs are under ignored `conker/build/init-bitmap-ordered/`, including
`all-ones-mask-qualification.json`, binaries, compiler logs and disassembly.

The combined 119-test run also recompiles previous bitmap trials, checks MMIO,
allocator/startup/storage contracts and connected formatter boundaries,
and verifies retained Init ownership/raw slots. It passes the established
pre-byte-depth decoder size control; it does not freshly qualify or alter
the byte-depth lead from Note 975. Complete existing Init code (164048 bytes),
Init data (17376), and Game data (189088 / 720 owners) remain raw retail-exact.
Tool checks, whitespace and current-note links pass.

The forty preprocessing comparisons use `cc -E -P` for Shapes 1..20, with
and without `HOST_TEST`, comparing current source against
`git show a916e9f4:tools/experiments/init_bitmap_ordered.c`. This confirms
unchanged disabled source, not a new hardware/compiler-provenance claim.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 19 21 22
python3 -m unittest tools.tests.test_init_bitmap_all_ones_mask -q -f
python3 -m unittest tools.tests.test_init_bitmap_all_ones_mask tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -q -f
make tools-check
```

## Continue

- [x] Test a new all-ones value-lifetime hypothesis with an arithmetic control.
- [x] Measure complete bodies under all three retained profiles.
- [x] Qualify the new bounded guest/host memory behavior and rejection controls.
- [x] Verify old-shape preprocessing and run the 119-test regression suite.
- [x] Preserve all existing production Init slots/code/data and Game data.
- [ ] Recover the original direct cursor/end branch and increment delay slot.
- [ ] Recover the original two-based mask/register schedule before adoption.

Retain the reproducible trials, not a production replacement. Do not repeat
another mask-only substitution as a solution to the loop problem. Further
bitmap work needs a justified branch/delay scheduling or provenance hypothesis.
MMIO remains the next small target; connected decoder fitting is still 512
bytes over including its adapter, and formatter fitting is 196 bytes over.

Init stays at 492 C / 47 ASM entries. No production relink, full guarded
decoder corpus, hardware/gameplay acceptance, sibling source/build, frozen
Release, saves, ROM promotion, README aggregate change or push is included.
