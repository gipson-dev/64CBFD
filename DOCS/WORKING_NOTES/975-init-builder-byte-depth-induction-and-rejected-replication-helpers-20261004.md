# Init Builder Byte-Depth Induction And Rejected Replication Helpers

Date: 2026-10-04. Starting HEAD: `859c2cad`.

Subsequent [Note 976](976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md)
screens sixteen cache combinations and rejects a persistent parent-mask
recurrence. Neither improves this qualified 4496-byte lead; production
conversion and the remaining 512-byte fitting gap stay open.

Subsequent [Note 979](979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
qualifies this banked packed O2/g3 image across all 507 pages in both masked
CU1 modes, 1014 passing paired runs. This closes its full corpus gate only;
fitting, entry/frame/private-stack and hardware gates remain open.

## Result

Continue Init fitting from
[Note 974](974-init-decoder-complement-low-mask-fitting-trial-20261004.md).
The new opt-in byte-depth counter saves **sixteen complete executable bytes in
both packed-remaining profiles**, with unchanged call-frame bounds. Optimized C plus the actual
adapter is now **4496 bytes versus 3984 retail: 512 bytes over**.
This is progress toward connected fitting, not production conversion.

Two distinct out-of-line replication helpers regress both text and stack.
Their source branches and compiler selectors are removed; only the byte-depth
trial is retained. No production owner, guard, profile or README total changes.

## Retained Byte-Depth Trial

`--builder-byte-level` replaces the builder's private tree-depth index with a
signed byte offset: initialize at -4, enter levels by adding four, and ascend
by subtracting four. The first table publication remains depth zero. Table
cells and prefix offsets address the same aligned words as the index control.
Frame-backed tables still contain guest addresses; the native non-frame table
still contains entry indices. Neither representation nor caller layout changes.

The trial does not pre-bias a C pointer before its array. It forms byte-addressed
cells only at actual level accesses; the initial -4 numeric value is not
dereferenced. Existing bounded lengths/tree/storage requirements still apply.
Pointer-ascent and indexed-ascent source paths both account for the new units.
Physical workspace, counts, sorted symbols, packed entries and ABI shadows are
unchanged; no additional array, helper or wrapper is introduced.

The scaled byte-cursor spelling in the parent-ascent path is intentionally
retained: simplifying its constant scale changed IDO register allocation and
lost the optimized whole-image reduction. Disabled-option source keeps the
original ++/-- and typed offset cursor. An initial spelling regressed the
disabled O2 control to 4368 bytes; that was rejected as an invalid baseline
comparison and corrected before qualification. Both banked disabled packed
instruction hashes below are restored, not merely equal-size controls.

## Complete Allocation

All rows use the established packed-remaining ABI-shadow configuration,
pointer-owned core, first-refill lookup and distance-operation capture. The
complemented-mask and entry-value options stay disabled. Totals include the
actual 176-byte adapter, not a prospective or omitted adapter budget.

| Profile / shape | C text | Executable | Builder region / public words | Builder frame | Core direct-call bound |
| --- | ---: | ---: | ---: | ---: | ---: |
| O2/g3 control | 4336 | 4512 | 401 / 333 | 200 | 400 |
| O2/g3 byte depth | 4320 | 4496 | 398 / 330 | 200 | 400 |
| O1 control | 5808 | 5984 | 560 / 488 | 120 | 360 |
| O1 byte depth | 5792 | 5968 | 556 / 484 | 120 | 360 |

Optimized embedded ABI-capture/lookup helpers remain 22 / 46 words; O1 remains
27 / 45. O2 public builder savings are three words; removal of one final core
alignment word supplies the fourth whole-image word. Core body stays fifty
words, now with no final padding. O1 saves four builder words; final core body /
allocation remains 86 / 89 words. Other named units retain their prior extents.

This is not a universal option win. Fresh controls for the other two established
shapes confirm these complete executable totals (including the same adapter):

| Shape | O2 control / byte depth | O1 control / byte depth |
| --- | ---: | ---: |
| Frame | 5504 / 5504 | 5984 / 5968 |
| Aligned-end | 4528 / 4544 | 5968 / 5952 |

Aligned-end O2 grows sixteen bytes. All corresponding call-frame bounds stay
unchanged. Keep the new option disabled by default and select it only as the
qualified packed fitting candidate, not an across-configuration replacement.

Complete object `.text` SHA-256:

```text
O2 control    177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d
O2 byte depth dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a
O1 control    8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755
O1 byte depth fff009d0196e62e0cbf661ac1398edf62d02c8943a8032171889b02999567394
```

## Rejected Replication Helpers

Unlike prior in-loop pointer/countdown trials, these factor packed replication
into a separate four-argument leaf to shorten the builder's live-register set.
After the original `next < size` gate, arguments are workspace + table + next,
size - next, the entry stride, and the packed word. The offset form starts a
zero offset, stores, adds stride and compares offset with span. The countdown
form additionally tracks a signed span and exits when it becomes nonpositive.

| Shape | O2 C / executable / builder public / bound | O1 C / executable / builder public / bound |
| --- | --- | --- |
| Offset helper | 4464 / 4640 / 354 / 416 | 5952 / 6128 / 511 / 392 |
| Countdown helper | 4464 / 4640 / 354 / 416 | 5968 / 6144 / 511 / 392 |

Both grow O2 by 128 bytes and sixteen bound bytes. The new helper and call
overhead do not reduce builder register pressure: its frame rises to 216 O2 /
144 O1 bytes. Reject before semantic qualification. No alias, malformed-input,
CU1 corpus or hardware equivalence is claimed for these discarded forms.
Their compiler receipts remain under ignored
`conker/build/init-builder-replication-helper-20261004/`.

## Verification And Next

**58 connected/native tests pass in 323.027 seconds, no skips.** A focused
publication rerun passes in 2.581 seconds after restricting the trace to the
physical sixteen-word table (excluding the first sorted-symbol cell). It is a
repeat, not additional coverage. Twenty separate inventory/slot-ledger/call-
graph checks pass in 0.857 seconds, no skips: 78 distinct passing checks.
Tool, whitespace and current-trial documentation-link checks pass.

The retained test module freshly compiles all three established shapes and both
profiles, links the actual adapter, and runs connected/native fixtures. Added
tests compare ordered depth-table publications against the retail builder,
including nested depth-sixteen trees, nonzero allocation and root widths 1/4/9.
Existing parent-root underflow, stale sorted-cell, allocation-order, failure-state,
CU1, saved-register and private-buffer fences remain requirements.
The new publication check covers 36 direct retail/compiled pairs across two
tree shapes, three root widths and six images. Packed O2 conservative/observed
total stack descent stays 3248 bytes; O1 stays 3208. These observations do not
prove private-stack reservation in real gameplay. Neither full guarded CU1
corpus is rerun, and prior default-candidate corpus receipts do not qualify
this changed option.

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level -q -f
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level.InitDecompressorBuilderByteLevelTests.test_ordered_depth_table_publications_match_retail -q -f
python3 -m unittest tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls -q -f
make tools-check
```

- [x] Measure complete byte-depth allocations in both profiles.
- [x] Restore both banked disabled-option instruction hashes.
- [x] Reject and remove both inferior out-of-line helper shapes.
- [x] Finish the retained connected/native tests and production slot audit.
- [ ] Remove at least another 512 complete optimized executable bytes.
- [ ] Prove private-stack reservation and original entry/frame/placement ownership.
- [ ] Rerun both full guarded CU1 corpora before adoption of a changed candidate.

Receipts/objects/logs/disassembly live under ignored
`conker/build/init-builder-byte-level-20261004/`. This checkpoint performs no
production relink, source-owner conversion, full guarded corpus, real hardware
or gameplay run. Production Init remains 492 C / 47 ASM entries; README
aggregates, sibling source/builds, frozen Release, saves and ROM promotion stay
unchanged. No push is included.
