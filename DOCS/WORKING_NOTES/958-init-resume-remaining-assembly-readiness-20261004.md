# Init Resume: Remaining Assembly Readiness

Date: 2026-10-04. Starting HEAD: `245359b1`.

## Answer

**Some remaining Init assembly is suitable for further C recovery, but no
retained replacement is currently ready to adopt.** This resume follows the
requested Init assessment, not the separate pending Game child recovery.
The checkout was clean when the assessment began.

Init remains **492 / 539 C functions (91.28%)**, with **151,796 / 164,048 C
bytes (92.53%)**. The remaining **47 assembly entries total 12,252 bytes**.
Every assembly owner resolves, every retained linked slot is retail-exact,
and the entire existing Init code/data image is also retail-exact.

The complete per-function inventory is in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).
There are seventeen investigation targets, not seventeen approved conversions.
Thirty established boot/hardware/context/SDK owners should remain assembly.
Some retained SDK algorithms are expressible in C; retention is a provenance
and machine-interface decision, not a claim of mathematical impossibility.

## Conversion Decisions

| Target | Entries / retail bytes | Can be expressed in C? | Ready to replace assembly? |
| --- | ---: | --- | --- |
| Bitmap `func_10005BE0` | 1 / 76 | Yes; semantic experiments exist | No: full nineteen-word retail body is not reproduced |
| MMIO `func_100038E0` | 1 / 44 | Yes, preserving ordered volatile accesses | No: full eleven-word body and access contract need qualification together |
| Decoder `func_10006240` through `func_1000709C` | 10 / 3,984 | Connected semantic implementation exists | No: best executable image is 4,512 bytes, 528 over budget; stack/entry ownership remains open |
| Cleanup/diagnostic/glyph path | 5 / 1,308 | Partial connected semantic recovery exists | No: caller interfaces, interior entry, fitting and placement remain open |
| Boot/hardware/context/SDK owners | 30 / 6,840 | Mixed; some algorithms are C-expressible | Retain the proven original assembly and register/machine contracts |

### Small Leaves

The bitmap has older nineteen-word C candidates, but they are non-matching:
the one-based-mask forms recorded in
[Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md) have fifteen
or sixteen differing aligned positions. That is historical compiler evidence,
not a new compilation of those forms in this resume. Do not describe the
bitmap as having no candidate that fits; **fitting and full matching are
separate gates**.

The freshly recompiled right-shift/value-lifetime form still emits twenty
optimized words against nineteen retail. Address-difference emits twenty-two;
equality-exit forms emit twenty-one. The retained tests cover captured
endpoints, inclusive filling, post-fill signed count reads, aliases, wrap and
bounded reversed-range prefixes. A new source shape must preserve these
observations and explain the direct endpoint branch/increment delay slot.
Repeating rejected forms unchanged is not conversion progress.

The MMIO assembly is freshly reassembled and checked against retail. Its
external store contract remains:

1. Word `0xBC000C02` to `0x80038070`.
2. Halfword `0x4040` to `0x80038074`.
3. Halfword `0x4040` to `0xBC000C02`.

The published-address trial in
[Note 885](885-init-mmio-published-address-dataflow-trial-20261004.md) can fit
eleven O1 words, but differs at eight aligned positions, including an extra
address copy and changed return-delay scheduling. Its C matrix was not rerun
here. Extra global reads, invented return values or broad instruction guards
are not an acceptable way to declare this handwritten routine recovered.

### Connected Paths

The decoder fitting test freshly compiles the retained shape/profile images.
The best packed O2 distance-operation-local implementation remains **4,336
C bytes plus a 176-byte adapter = 4,512 executable bytes**. Conversion needs
at least 528 bytes of reduction before considering production placement.
The ten retail entries share registers and inherited stack state; replacing
them as ten ordinary independent helpers would break the calling contract.
After any candidate change, rerun both full guarded CU1-clear/set corpora and
prove private-stack reservation and entry/frame ownership. This resume reran
the size check, not those corpora.

The formatter tests freshly compile the connected separate/shared/split
setup controls: **624 / 608 / 624 bytes**, with **48 / 80 / 64-byte stack
descent**, against a **412-byte** connected retail budget. The best control
is still 196 bytes over. The writer's twenty-nine-word C body fits its
thirty-word leaf, but that is not a complete calling-path conversion.
Experimental placement at `0x10009000` overlaps `func_10008F90`; the two
diagnostic caller stack regimes and interior entry remain ownership gates.

## Next Init Work

1. Keep the exact production assembly baseline and the existing inventory.
2. Attempt bitmap or MMIO only with a new, specific compiler/provenance
   hypothesis; require the complete slot and behavioral contract before adoption.
3. For sustained connected recovery, resume the existing decoder candidate:
   measure a targeted reduction, include the adapter in the total, and reach
   the 3,984-byte budget without moving work into uncounted wrappers.
4. Qualify decoder stack/entry ownership and rerun both guarded corpora after
   changes. Treat glyph fitting/placement as a separate connected project.
5. Only then change a production owner, relink, regenerate progress and check
   neighbors plus complete Init code/data and Game data against retail.

No broad conversion batch is justified by the current evidence. The Game
`func_150E93DC` placeholder remains separate pending work; it was not edited.

## Fresh Verification

- **101 Init inventory, bitmap, MMIO, storage, startup and connected glyph
  checks pass in 60.943 seconds, no skips.**
- **One decoder fitting check passes in 2.065 seconds, no skips.**
- Total: **102 passing tests across two invocations**.
- All 47 retained source owners and raw linked slots are verified.
- Existing linked Init code: 164,048 bytes, zero differences.
- Existing linked Init data: 17,376 bytes, zero differences.
- Existing linked Game data: 189,088 bytes / 720 owners, zero differences.

```sh
python3 -m unittest tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -v -f
```

The section audits compare the existing production ELF against checksum-verified
retail. No production rebuild or full decoder corpus rerun is claimed.
Bounded compiler/model tests are not hardware or gameplay acceptance.

## Checkpoint

- [x] Resume from the clean banked baseline and follow the requested Init scope.
- [x] Recheck inventory, all assembly owners and all retained linked slots.
- [x] Recompile retained bitmap/glyph controls and the decoder size images.
- [x] Distinguish C-expressible candidates, fitted candidates and approved adoption.
- [ ] Qualify a complete small-leaf replacement with a new source hypothesis.
- [ ] Fit and qualify connected decoder/glyph ownership before conversion.

Only working documentation changes. Production source, profiles, word guards
and README aggregates remain unchanged. No sibling/Release changes, ROM
promotion, runtime acceptance or push.
