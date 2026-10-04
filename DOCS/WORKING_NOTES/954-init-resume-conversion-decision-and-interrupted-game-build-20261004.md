# Init Resume Conversion Decision And Interrupted Game Build

Date: 2026-10-04. Starting HEAD: `5d660515`.

## Decision

Some remaining Init assembly is C-expressible, but **none of the retained
replacement candidates is ready for production adoption**. Init has 492 / 539
C entries (91.28%), covering 151,796 / 164,048 bytes (92.53%). Its 47 assembly
entries occupy 12,252 bytes. This resume freshly checks the inventory, source
owners, existing linked bytes and retained compiler/contract tests.

The per-function inventory remains in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md), with the
connected conversion requirements in
[Note 951](951-init-resume-conversion-readiness-and-repeatable-audit-20261004.md).
Do not replace correct original assembly with placeholders to increase C counts.
Intentional assembly and incomplete semantic recovery are different categories.

## Init Conversion Order

| Priority | Entries | Retail bytes | Adoption gate |
| --- | --- | ---: | --- |
| 1 | `func_10005BE0` | 76 / 19 words | New compiler shape must fit and preserve inclusive filling, captured endpoints, alias-sensitive count reload and mask |
| 2 | `func_100038E0` | 44 / 11 words | Preserve the three ordered stores and widths; qualify the complete emitted body without invented return semantics |
| 3 | Ten decoder entries, `func_10006240` through `func_1000709C` | 3,984 | Reduce the complete connected image, then prove entry/register/stack reservation and placement contracts |
| 4 | Five cleanup/diagnostic/glyph entries | 1,308 | Fit and qualify the whole calling path, including interior entry and both caller stack regimes |
| Retain | Thirty boot, hardware/context and SDK entries | 6,840 | Preserve established original assembly owners; not an ordinary original-C recovery queue |

The retained group is a provenance/interface decision, not a claim that all
thirty algorithms are mathematically impossible to express in C.

### Small Leaves

Fresh bitmap compiler tests still reject the existing alternatives. Equality-exit
forms emit 21 optimized words; the taken-edge form emits 20; unsigned
address-difference emits 22. None fits the nineteen-word slot. Passing bounded
alias/wrap tests does not make an oversized implementation adoptable.

The MMIO leaf's original trace is freshly checked and reassembled:

1. Word `0xBC000C02` to `0x80038070`.
2. Halfword `0x4040` to `0x80038074`.
3. Halfword `0x4040` to `0xBC000C02`.

The published-address C trial's O1 eleven-word result remains prior compiler
evidence from [Note 885](885-init-mmio-published-address-dataflow-trial-20261004.md),
not a fresh C compilation here. It has an extra address copy and different
return-delay schedule, with eight aligned word differences. Other profiles
also introduce a global read or exceed the allocation. Do not adopt it or
invent a return value solely to force the retail register choice.

The next small-leaf experiment needs a genuinely new control-flow or
address-lifetime hypothesis. Repeating rejected forms unchanged adds no
conversion progress.

### Connected Paths

The decoder size test freshly compiles/links its six retained shape/profile
images. The best packed O2 candidate is **4,336 C bytes plus a 176-byte adapter:
4,512 executable bytes**, or **528 bytes over** the 3,984-byte allocation.
This run checks fitting, not the full decoder execution corpus. After a source
change, rerun both guarded CU1-clear/set corpora and resolve private-stack and
entry ownership before changing production ownership.

The fresh formatter suite recompiles the retained separate/shared/split setup
controls. Their optimized connected allocations remain 624 / 608 / 624 bytes
against 412 retail bytes. The C writer's 29-word body fits its thirty-word
leaf, but the connected path does not. The experimental address `0x10009000`
is occupied by production `func_10008F90`; a fitted isolated leaf does not
resolve text placement, inherited registers or stack ownership.

## Fresh Verification

- 93 combined Init inventory, bitmap, MMIO, storage, startup and connected
  formatter/adapter tests pass in 73.659 seconds, no skips.
- One separately invoked decoder size test passes in 3.939 seconds, no skips.
  Total: 94 passing tests across two invocations; not a full-corpus decoder rerun.
- All 47 assembly owners and retained linked slots match checksum-verified retail.
- Existing ELF Init code: 164,048 bytes, zero differences.
- Existing ELF Init data: 17,376 bytes, zero differences.
- Existing ELF Game data: 189,088 bytes / 720 owners, zero differences.

The checks use the last successfully linked production ELF. They do **not**
establish that the current dirty Game source successfully rebuilds.

```sh
python3 -m unittest tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -v -f
```

## Interrupted Game Work

The interrupted production build completed with an error, not a successful
relink. The preserved `func_150E8D5C` child-emission recovery compiles to
`0x384` bytes (225 words), exceeding its `0x380`-byte (224-word) retail slot
by one word. `pad_generated_object.py` correctly rejects it.

Two pre-existing dirty files remain intact and outside this Init checkpoint:
`conker/src/game/generated_113D60.c` and
`conker/src/game/generated_15D730.c`. The latter's pointer-interface edits
also still need qualified raw-byte/caller checks. No child conversion,
successful current-source relink or gameplay acceptance is claimed.

Resume Game work by removing the one-word size excess without changing the
child's RNG/store/callback contract, adding focused chain tests, then relinking
and checking wrappers, neighbors, all Init sections and Game data. This is
separate from the requested Init conversion assessment.

## Checkpoint

- [x] Recount and resolve all 47 remaining Init assembly entries.
- [x] Verify the existing raw code/data and retained owners.
- [x] Recompile the retained bitmap/formatter controls and decoder size images.
- [x] Record the interrupted Game build failure without altering its source.
- [ ] Fit and qualify a new small-leaf implementation before adoption.
- [ ] Resolve connected decoder/glyph text, placement and stack ownership.
- [ ] Repair and qualify the preserved Game child callback before banking it.

No production Init source/profile/guard changes, README aggregate changes,
ROM promotion, sibling or Release changes, runtime qualification or push.
