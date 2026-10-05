# Init Remaining Conversion Decision And Decoder Cache Matrix

Date: 2026-10-04. Starting HEAD: `ab84ebfd`.

## Decision

Resume the requested remaining-Init assessment from the banked baseline.
**Seventeen entries remain investigation targets, but no replacement is ready
for production adoption. Thirty other entries intentionally retain assembly.**
Some algorithms can be represented in C; that is different from preserving
retail instruction slots, machine interfaces and shared-entry contracts.
Completing restoration does not require replacing intentional assembly with C.

| Group | Entries / bytes | Current adoption gate |
| --- | ---: | --- |
| Bitmap `func_10005BE0` | 1 / 76 | Best checked C is 20 words versus 19 retail; endpoint branch and increment delay slot remain unresolved |
| MMIO `func_100038E0` | 1 / 44 | Full 11-word C match unresolved; retain exactly three ordered volatile stores and the void interface |
| Decoder `func_10006240` through `func_1000709C` | 10 / 3984 | Best qualified packed candidate is 4496 executable bytes, 512 over; private-stack and original entry ownership remain open |
| Cleanup/debug/glyph | 5 / 1308 | Best retained formatter connection is 608 versus 412 bytes, 196 over; interior entry, caller stack and occupied placement remain open |
| Boot/SDK/hardware/context | 30 / 6840 | Retain original assembly provenance and machine/register contracts; not ordinary missing-C functions |
| Total | 47 / 12252 | 492 C / 539 entries; no newly adopted conversion |

The complete per-function map remains in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).
The current connected decoder lead is the opt-in byte-depth candidate qualified
in [Note 975](975-init-builder-byte-depth-induction-and-rejected-replication-helpers-20261004.md).
Historical 528-byte decoder gaps in earlier notes describe the pre-byte-depth
candidate; the current gap is **512 bytes including the actual adapter**.

## Cache Interaction Matrix

Freshly compile all sixteen combinations of four existing selectors against
the byte-depth packed-remaining lead. Each case produces O2/g3 and O1 objects:
**32 fresh compiler objects**, measured as complete C text plus the actual
176-byte adapter. This is size/call-frame screening, not semantic qualification
of the changed-cache configurations.

- `workspace`: add `--cache-workspace`.
- `leaf`: add `--cache-leaf-table`.
- `allocated`: add `--local-allocated`.
- `sorted`: change `--cache-builder counts-offsets` to `--cache-builder all`.

All other byte-depth, distance-operation, ABI-shadow and connected-shape flags
remain fixed. Units below are bytes. Bounds are the conservative core
direct-call frame sum, not proof of gameplay stack reservation.

| Added caches | O2 C / executable | O2 builder frame / bound | O1 C / executable | O1 builder frame / bound |
| --- | ---: | ---: | ---: | ---: |
| None (control) | 4320 / 4496 | 200 / 400 | 5792 / 5968 | 120 / 360 |
| Sorted | 4320 / 4496 | 208 / 408 | 5792 / 5968 | 128 / 368 |
| Allocated | 4368 / 4544 | 208 / 408 | 5792 / 5968 | 128 / 368 |
| Allocated + sorted | 4368 / 4544 | 208 / 408 | 5808 / 5984 | 128 / 368 |
| Leaf | 4336 / 4512 | 208 / 408 | 5808 / 5984 | 128 / 368 |
| Leaf + sorted | 4336 / 4512 | 216 / 416 | 5824 / 6000 | 136 / 376 |
| Leaf + allocated | 4368 / 4544 | 216 / 416 | 5824 / 6000 | 136 / 376 |
| Leaf + allocated + sorted | 4368 / 4544 | 216 / 416 | 5824 / 6000 | 136 / 376 |
| Workspace | 4368 / 4544 | 208 / 408 | 5792 / 5968 | 128 / 368 |
| Workspace + sorted | 4352 / 4528 | 216 / 416 | 5808 / 5984 | 128 / 368 |
| Workspace + allocated | 4384 / 4560 | 216 / 416 | 5808 / 5984 | 128 / 368 |
| Workspace + allocated + sorted | 4384 / 4560 | 216 / 416 | 5808 / 5984 | 136 / 376 |
| Workspace + leaf | 4368 / 4544 | 216 / 416 | 5824 / 6000 | 136 / 376 |
| Workspace + leaf + sorted | 4352 / 4528 | 224 / 424 | 5824 / 6000 | 136 / 376 |
| Workspace + leaf + allocated | 4384 / 4560 | 224 / 424 | 5824 / 6000 | 136 / 376 |
| All four | 4384 / 4560 | 224 / 424 | 5840 / 6016 | 144 / 384 |

The uncached control remains the best screened O2 candidate. Sorted-only ties
text but worsens frame/bound; no other combination improves complete text.
No selector is promoted and no behavior equivalence is claimed for these
unqualified combinations. The existing opt-in options remain unchanged.

Receipts, flags, objects, logs and disassembly are ignored artifacts under
`conker/build/init-byte-depth-cache-matrix-20261004/`; `matrix.json` records
all flags plus public-unit and embedded-helper-region measurements.
The fixed base flags are `InitDecompressorBuilderByteLevelTests.shape_flags`
for `packed-remaining`, plus `--abi-fpr-shadow` and that class's
`shadow_extra_flags`. Apply the four selectors above and invoke
`tools/experiments/compile_init_decompressor.py --output <case-directory>`.
Use complete `.text`, not just the public builder symbol, for fitting decisions.

## Rejected Prefix-Mask Recurrence

A distinct state-representation trial retained the consumed-prefix mask across
symbols. Initialize a local mask to zero, recompute it after table allocation's
`consumed += width`, then shift it right by bounded width on parent ascent.
Both pointer-cursor and indexed parent tests used this local value instead of
recomputing the mask in each condition. Unlike the earlier mask-reuse trial,
this is a persistent recurrence across symbols and ascent levels.

| Profile / shape | C / executable bytes | Builder public / region words | Builder frame / core bound |
| --- | ---: | ---: | ---: |
| O2 control | 4320 / 4496 | 330 / 398 | 200 / 400 |
| O2 recurrence | 4352 / 4528 | 338 / 406 | 200 / 400 |
| O1 control | 5792 / 5968 | 484 / 556 | 120 / 360 |
| O1 recurrence | 5792 / 5968 | 486 / 558 | 128 / 368 |

Reject before semantic qualification: O2 grows 32 bytes; O1 ties complete text
but increases stack. Remove the temporary `--parent-mask-recurrence` selector
and C branches with scoped edits. Both experiment sources are restored to
their banked contents; there is no retained code change from this trial.
No malformed-input, alias, CU1 corpus or hardware equivalence is claimed.
Ignored compiler receipts remain under
`conker/build/init-parent-mask-recurrence-20261004/{control,recurrence}/`.

## Verification

**78 retained-decoder/inventory/slot/call checks pass in 313.925 seconds;
43 bitmap/MMIO/formatter checks pass in 52.296 seconds. No skips in either
suite: 121 passing checks across the two runs.** These rerun existing coverage,
not 121 newly added tests. Tool, whitespace and current-assessment link checks
also pass. The two experiment sources have no diff from starting HEAD.

The retained-byte-depth and production audit suite is rerun after restoring
the rejected source. It freshly compiles the retained connected shapes and
both profiles, tests actual adapters and checks disabled-option instruction
hashes. The inventory audit independently checks checksum-verified retail,
every retained source owner/raw slot, complete existing Init code/data and
Game data. This is an existing linked-artifact audit, not a production relink.

Fresh bitmap controls (O2 / O2 no-unroll / O1 words) are preincrement
32 / 20 / 32, right-shift mask 20 / 20 / 33, and address-difference
22 / 22 / 33, versus nineteen retail. Each suite records 501 completed model
pairs and six bounded prefixes. The MMIO checks reassemble the original leaf
and verify its ordered stores; historical MMIO C matrices are not recompiled.
The formatter tests freshly verify the 608-byte best retained connection and
its separate placement/stack gates. None of these is a new fitting hypothesis.

The retained packed decoder's fresh complete text hashes remain:

```text
O2 byte depth dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a
O1 byte depth fff009d0196e62e0cbf661ac1398edf62d02c8943a8032171889b02999567394
```

O2 conservative/observed total stack descent remains 3248 bytes; O1 remains
3208. Complete existing Init code (164048 bytes), Init data (17376 bytes),
and Game data (189088 bytes / 720 owners) remain raw retail-exact. These
bounded tests do not rerun either full guarded decoder corpus or establish
hardware/gameplay/private-stack-reservation acceptance.

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls -q -f
python3 -m unittest tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_mmio_assembly tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
make tools-check
```

## Next Steps

1. **Nearest small candidate: bitmap.** Develop a new endpoint-branch and
   increment-delay scheduling hypothesis, retaining inclusive fill, captured
   endpoints, wrapping arithmetic, aliases and the late signed count reload.
   Require all nineteen words; prior 20-word variants are negative evidence.
2. **Second small candidate: MMIO.** Seek justified address-lifetime/provenance
   evidence. Preserve word `0xBC000C02` to `0x80038070`, halfword `0x4040`
   to `0x80038074`, then halfword `0x4040` to `0xBC000C02`. Do not add a
   global read or invent a return contract to force register allocation.
3. **Sustained connected work: decoder.** Remove another 512 complete
   executable bytes. Prefer a genuinely new builder/shared-call structure
   hypothesis; this cache matrix and mask recurrence do not improve fitting.
   Count helpers, padding and adapters, then prove original entry/frame/
   placement ownership and private-stack reservation. Rerun both full guarded
   CU1 corpora before adopting a changed candidate.
4. **Formatter is separate.** Close the 196-byte connected gap and prove
   interior-entry/caller-stack/nonoverlapping placement; a fitted glyph leaf
   alone is not an adoptable replacement for the five-entry path.
5. **Adopt only after proof.** Change only the established production owner,
   relink, regenerate progress, and compare adjacent slots plus complete Init
   code/data and Game data against pristine retail. Update README aggregates
   only after an actual conversion or matching change.

- [x] Recount and classify all 47 remaining Init ASM entries.
- [x] Screen all sixteen cache combinations in both profiles.
- [x] Reject/remove the inferior persistent-mask recurrence.
- [x] Restore banked experiment sources and rerun 121 checks without skips.
- [x] Verify all retained raw slots and complete existing Init/data plus Game data.
- [ ] Qualify a complete small-leaf replacement before changing ownership.
- [ ] Close connected decoder/formatter fitting and entry/stack/placement gates.

No production ownership, profiles, guards or README totals change. No fresh
production relink, full guarded corpus, hardware/gameplay acceptance, sibling
source/build, frozen Release, save changes, ROM promotion or push is included.
