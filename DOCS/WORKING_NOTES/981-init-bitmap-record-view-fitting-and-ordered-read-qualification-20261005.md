# Init Bitmap Record-View Fitting And Ordered Read Qualification

Date: 2026-10-05. Starting HEAD: `39bbc51a`.

## Scope And Result

Continue remaining Init fitting after
[Note 980](980-init-packed-bit-width-screen-and-restored-candidate-20261005.md).
The small bitmap leaf `func_10005BE0` remains a nineteen-word handwritten
routine. Prior scalar C has an extra XOR comparison word; the fitted all-ones
variant in [Note 977](977-init-bitmap-all-ones-mask-fitting-and-retail-loop-boundary-20261004.md)
changes mask arithmetic and does not recover retail's loop/tail schedule.

The new isolated grouped volatile view captures the same start/end fields and
reloads the signed count after filling. **Both optimized profiles emit a
nineteen-word body while retaining the two-based mask. Seventeen positions
still differ from retail: do not adopt.** The saving is an address-lifetime
change, not recovery of the direct endpoint branch/increment delay slot.
Complete standalone text remains 80 bytes after four bytes of alignment.

This is not a claim that the original globals were declared as one C record.
Their scalar production declarations and assembly owner remain unchanged.

## New Isolated Shapes

Extend `init_bitmap_ordered.c` and its driver with explicit opt-in Shapes 23/24:

- Shape 23: direct fields of a volatile record linked at `0x8003BE70`.
- Shape 24: the same fields through a locally captured volatile record pointer.
- Shape 12: freshly compile the unchanged unsigned scalar induction control.

The guest record is sixteen bytes: start pointer at zero, unused word at four,
signed halfword count at eight, unused halfword at ten, end pointer at twelve.
A compiler-emitted readonly layout receipt is independently extracted and
checked as `(16, 0, 8, 12, 2)`, including count width. Neither unused field is
accessed by either candidate. The extra linker symbol aliases only this
experimental record; no production symbol/type ownership changes.

The native host path keeps the existing independent scalar globals because
host pointer width/layout differ from guest o32. All 79 strict host algorithm
cases pass per shape, but they do not qualify the guest record layout.
Actual emitted guest code and ordered model traces qualify that layout and
its access behavior separately.

The driver default remains Shapes 1..11. Shapes 1..22 preprocess identically
to starting HEAD in all 44 host/guest selections. No prior selector or body
changes. The new alias is supplied only for Shapes 23/24; existing compiler/profile
checks below verify their retained extents and behavior.

## Measurements

| Shape / profile | Body words | Differing positions | Frame bytes | Complete text / trailing bytes |
| --- | ---: | ---: | ---: | ---: |
| 12 scalar O2/g3 | 20 | 19 | 0 | 80 / 0 |
| 12 scalar O2/g3 no-unroll | 20 | 19 | 0 | 80 / 0 |
| 12 scalar O1 | 31 | 31 | 16 | 128 / 4 |
| 23 direct record O2/g3 | 19 | 17 | 0 | 80 / 4 |
| 23 direct record O2/g3 no-unroll | 19 | 17 | 0 | 80 / 4 |
| 23 direct record O1 | 31 | 31 | 16 | 128 / 4 |
| 24 local record O2/g3 | 19 | 17 | 0 | 80 / 4 |
| 24 local record O2/g3 no-unroll | 19 | 17 | 0 | 80 / 4 |
| 24 local record O1 | 32 | 32 | 24 | 128 / 0 |

Both optimized record views have identical complete instruction images. They
retain a common base in A1, load start/end from offsets zero/twelve and later
read the signed count with `lh v0,8(a1)`. This removes the tail's scalar LUI.
The opening still needs LUI plus ADDIU for the common base, so it does not
save an opening instruction. The optimized loop remains:

```text
xor   a0,v0,v1
addiu v0,v0,1
bnez  a0,loop
sb    a2,-1(v0)     # branch delay slot
```

Retail instead uses `sb t0,0(v0)`, direct `bne v0,v1,loop`, then increments
V0 in the delay slot. The new tail retains `2 << (bits - 1)` but its constant,
register allocation and schedule also differ. This is not a closed scheduling
or register-allocation cycle suitable for broad word guards.

O1 direct record ties the scalar control; the explicit pointer adds a word and
eight stack bytes. No default/profile is promoted. No complete allocation
saving is inferred from nineteen body words in an eighty-byte text section.

## Qualification

Ten new tests pass in 2.469 seconds, no skips. They qualify six emitted guest
images against the original retail instruction fixture: **1002 completed
paired traces and twelve bounded reversed-endpoint prefixes**. Coverage includes:

- Positive, zero and negative signed counts, every remainder and repeated calls.
- Captured start/end behavior when output aliases those global storage words.
- Late count reload when byte/halfword count storage is overwritten by filling.
- Unsigned wrapping address arithmetic in the model, not real hardware.
- Ordered external reads/stores, complete external memory and neighboring sentinels.
- Preserved callee registers, restored SP and profile-specific frame descent.
- Output fences and a deliberately hoisted count-read rejection control.

A new extra-read control replaces the return-delay NOP with a read of unused
record offset four. Final memory remains identical, but the ordered trace
reports the extra read. Normal candidates read only start (word), end (word),
then count (signed halfword); no unused field is read or written.

**All 138 final combined checks pass in 70.804 seconds, exit zero, no skips.**
The preceding 138-check run also passed in 68.870 seconds; the final rerun
checks the driver after limiting the experimental alias to the new shapes. The
ten new checks join the existing bitmap/MMIO/formatter/owner/slot/storage/startup
coverage. Complete existing Init code (164048 bytes), Init data (17376 bytes),
all 47 retained ASM owners/raw slots, and Game data (189088 bytes / 720 owners)
remain retail-exact against checksum-validated ROM. This is an existing linked
artifact audit, not a fresh production relink. The decoder C/adapter/flags and
Note 979's full masked corpus candidate remain unchanged.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 12 23 24
python3 -m unittest tools.tests.test_init_bitmap_record_view -v -f
python3 -m unittest tools.tests.test_init_bitmap_record_view tools.tests.test_init_mmio_record tools.tests.test_init_bitmap_all_ones_mask tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -q -f
make tools-check
```

Objects, logs, linked ELFs, layout bytes and disassembly are ignored under
`conker/build/init-bitmap-ordered/`. Each suite overwrites the generic
`measurements.json`; this suite's dedicated `record-view-qualification.json`
retains its own measurements and completed/prefix counts. Tracked sources,
driver and tests make the result repeatable. Tool/whitespace/scoped-link checks
pass. No hardware, allocator ownership or gameplay acceptance is inferred.

## Adoption Boundary And Next

- [x] Screen grouped field addressing while retaining unsigned induction and two-based mask.
- [x] Verify compiler-emitted guest layout and six complete model instruction images.
- [x] Qualify ordered reads, aliases, wrapping model behavior and unused-field rejection.
- [x] Preserve all 44 old host/guest preprocessing selections and pass 138 combined checks.
- [ ] Recover the original endpoint branch/increment delay and full nineteen-word schedule.
- [ ] Establish original type/address-lifetime provenance before any production record declaration.

Keep production assembly. Further bitmap fitting needs the original loop/tail,
not another unqualified grouped-type promotion. Decoder fitting still needs
512 complete bytes plus entry/frame/private-stack/hardware proof; formatter
connection remains 196 bytes over. Init remains 492 C / 47 ASM owners.
No production conversion/relink, README aggregate, host source/build, frozen
Release, save, ROM promotion or push changes are included.
