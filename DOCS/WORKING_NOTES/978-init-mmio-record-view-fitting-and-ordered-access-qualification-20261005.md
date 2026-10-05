# Init MMIO Record-View Fitting And Ordered-Access Qualification

Checkpoint: 2026-10-05. Started 2026-10-04 at HEAD `88993df5`.

## Result

Continue the second small Init target, `func_100038E0`, after the bitmap
trial in [Note 977](977-init-bitmap-all-ones-mask-fitting-and-retail-loop-boundary-20261004.md).
**A new volatile record view reduces complete O2/g3 text from 64 to 48 bytes
against the fully volatile scalar control, but none of the twelve compiled
shape/profile combinations matches the eleven-word retail body.**
The direct record form is eleven words / nine differences at O2/g3 and
eleven / eight at O1. Explicit record/target locals introduce an eight-byte
frame and seventeen-word O1 bodies. Keep the original assembly owner.
This is a new grouped-address hypothesis and emitted-access qualification,
not a production conversion or original-record-type provenance claim.

## Hypothesis

Previous trials treated the two RAM publications as independent scalar globals
while changing local-pointer lifetime, partial volatility or published-address
reads. See [Notes 750](750-init-mmio-pointer-lifetime-profile-trials-20261002.md),
[762](762-init-mmio-partial-volatility-trials-20261003.md) and
[885](885-init-mmio-published-address-dataflow-trial-20261004.md).
This new source instead groups the adjacent word/halfword fields through one
volatile record view, seeking shared address materialization without adding
reads, changing access widths or inventing a return value.

The isolated source `tools/experiments/init_mmio_record.c` has three opt-in shapes:

1. Scalar control: word and halfword publications are independently volatile,
   followed by the hardware halfword write. This is a prior-shaped control,
   not a new source hypothesis.
2. Direct record: publish `.address` and `.value` through a volatile record
   anchored at `D_80038070`, followed by the constant hardware destination.
3. Record/target locals: snapshot `&D_80038070` and the hardware pointer,
   publish through the record pointer, then write through the target pointer.

All three remain no-argument void routines with three sequenced volatile
statements. None reads back a publication. Guest-width assertions require
four-byte pointers/words and two-byte halfwords. Actual compiler-emitted layout
receipts confirm an eight-byte record with field offsets zero and four,
corresponding to `0x80038070` and `0x80038074`. The two padding bytes are never
written. Grouping is experimental: production declarations remain independent
`u32` / `u16` symbols and are not replaced by this type.

The read-only layout receipt is diagnostic data, not a proposed runtime field
or hidden executable helper. Size tables below measure all executable `.text`;
the standalone experiment also contains its diagnostic `.rodata` receipt.
No placement or production ownership acceptance follows from these objects.

## Complete Measurements

Cells are **body words / differing aligned positions / complete text bytes /
frame bytes**. Body includes the actual return delay instruction; complete
text additionally includes trailing object padding. Retail body is eleven
words / 44 bytes. Differences are not semantic mismatch counts or edit distances.

| Shape | O2/g3 | O2 | O1 | O1/g3 |
| --- | ---: | ---: | ---: | ---: |
| 1, fully volatile scalar control | 13 / 13 / 64 / 0 | 12 / 12 / 48 / 0 | 13 / 13 / 64 / 0 | 14 / 14 / 64 / 0 |
| 2, direct record | 11 / 9 / 48 / 0 | 10 / 11 / 48 / 0 | 11 / 8 / 48 / 0 | 12 / 10 / 48 / 0 |
| 3, record/target locals | 11 / 9 / 48 / 0 | 10 / 11 / 48 / 0 | 17 / 17 / 80 / 8 | 17 / 17 / 80 / 8 |

Direct record saves sixteen complete bytes over this scalar control at O2/g3,
O1 and O1/g3; O2 complete text ties at 48 bytes despite saving two body words.
This is not a better raw match than every earlier trial: older local-pointer
O2/g3 and published-address O1 forms also reached eleven words. None justified
replacement of the retained handwritten routine.

Both record forms have byte-identical optimized images. O2/g3 keeps a shared
RAM record base in V0, publishes the address from T6, reuses a 0x4040 value in
V1, and rematerializes the hardware base in T7. Retail keeps the hardware
address in V0, separately materializes both halfword values, and uses two RAM
symbol-address sequences. This is not a closed register rename or independent
schedule difference. O1 direct-record likewise rematerializes the hardware
base and moves its write into JR RA's delay slot; O1/g3 is twelve words.
No instruction guards or production compiler-profile overrides are added.

## Emitted-Access Qualification

`tools/tests/test_init_mmio_record.py` freshly compiles and links all twelve
objects, then uses the established `BuilderFixture` instruction engine with
narrow MMIO address/width fences. Hardware addresses are dictionary-backed
guest-model memory only. The test never executes the candidate on the host.

Nine new tests pass in 6.796 seconds, no skips. The suite records **60 complete
retail/C paired traces**, using five distinct initial register/memory seeds
across twelve images. Every candidate has exactly these external accesses:

```text
write 0x80038070, 4 bytes, 0xBC000C02
write 0x80038074, 2 bytes, 0x4040
write 0xBC000C02, 2 bytes, 0x4040
```

There are no external reads. Full external memory and surrounding bytes agree;
callee-saved registers and stack pointer are preserved. Actual minimum stack
descent agrees with each measured zero/eight-byte frame. Private stack traffic
is modeled separately, not discarded from the machine execution. Return-delay
tests explicitly confirm that delayed hardware stores execute before return.
The incidental V0 result is deliberately not treated as a return contract.

Negative controls verify that the oracle detects reordered halfword stores
despite identical final memory, reports an added hardware halfword read, and
rejects wrong-width or record-padding writes. Layout, complete text/trailing
bytes, old assembly ownership and empty compiler logs are also checked.
These are bounded emitted-instruction checks, not hardware timing, concurrent
memory, original record provenance or byte-exact matching acceptance.

The combined MMIO, bitmap, inventory, decoder ledger/storage/size-control,
startup and connected formatter suite passes **128 tests in 66.503 seconds,
no skips**, including the nine new checks. The standalone run overlaps that
coverage and is not nine additional distinct tests. Complete existing Init
code (164048 bytes), Init data (17376 bytes), all 47 retained ASM owners/raw
slots, and Game data (189088 bytes / 720 owners) remain retail-exact.
This is an existing linked-artifact audit, not a fresh production relink or
qualification of real hardware. The current 4496-byte byte-depth decoder
lead is unchanged and is not freshly full-corpus qualified by this suite.
Tool, whitespace and current-note link checks pass.

An initial compiler invocation with absolute source/output arguments failed
with an empty log. Following the existing project convention of relative
source/output paths from `conker/` fixes the invocation; all final compiler
logs are empty. The driver removes stale objects before compilation and checks
fresh success before reading linked outputs. It never relinks production.

```sh
python3 tools/experiments/compile_init_mmio_record.py
python3 -m unittest tools.tests.test_init_mmio_record -q -f
python3 -m unittest tools.tests.test_init_mmio_record tools.tests.test_init_bitmap_all_ones_mask tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -q -f
make tools-check
```

Objects, logs, linked ELFs, layout bytes, disassembly, measurements and
`qualification.json` live under ignored `conker/build/init-mmio-record-20261004/`.
The tracked source, driver and tests make this negative fitting result repeatable.

## Adoption Boundary And Next

- [x] Test grouped record addressing separately from prior scalar controls.
- [x] Measure complete allocations and real return delay instructions in four profiles.
- [x] Verify compiler-emitted field layout and absence of padding writes.
- [x] Qualify sixty ordered retail/C traces and register/stack preservation.
- [x] Add order/read/width rejection controls rather than relying on final values alone.
- [x] Finish 128 combined checks and verify all existing Init/data and Game data.
- [ ] Recover all eleven retail words without broad normalization.

Do not promote the experimental record type or use the published word as a
read-back destination merely to force register allocation. Grouped addressing
and explicit locals now have measured negative evidence. Further MMIO fitting
requires a genuinely new address-lifetime/scheduling/provenance hypothesis.
The bitmap's fitted all-ones body likewise does not match its retail loop/tail.
Connected decoder fitting still needs 512 bytes including its adapter, plus
entry/frame/private-stack ownership; formatter fitting remains 196 bytes over.

Init remains 492 C / 47 ASM entries. Production source owners, shared
declarations, compiler profiles, guards and README aggregates are unchanged.
No production relink, full guarded decoder corpus, hardware/gameplay test,
sibling source/build, frozen Release, saves, ROM promotion or push is included.
