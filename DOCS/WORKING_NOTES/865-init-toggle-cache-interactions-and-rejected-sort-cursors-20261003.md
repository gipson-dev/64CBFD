# Init Toggle Cache Interactions And Rejected Sort Cursors

Date: 2026-10-03. Baseline: `fee89628`.

## Result

Fresh fitting measurements on the Note 864 combination reject all tested
cache/parent/sorted-pointer additions and both new sorted-length cursor
loops. No new implementation is retained. The temporary source edits are
removed exactly; scoped Git diff for the experiment source is empty.

This is not an unchanged rerun of Note 855: the base now includes dynamic
repeat-value fill, reused offset accumulator and toggle-first code increment.
These later changes could alter allocation interactions, but the fresh
receipts show no improvement. Current packed O2 remains 4,736 linked bytes,
752 over retail, with 392 core call bound and 200-byte builder frame.
Current packed O1 remains 6,144 linked / 352 bound / 120 builder frame.
Defaults, production and README totals stay unchanged.

## Cache Matrix

All masks use the complete Note 864 packed/remaining configuration. The
four independent bits add existing selectors:

| Bit | Option |
| ---: | --- |
| 1 | `--cache-workspace` |
| 2 | `--local-allocated` |
| 4 | `--cache-leaf-table` |
| 8 | `--cache-dynamic-lengths` |

`--builder-simple-operation` is already in the base, unlike Note 855's
five-bit matrix. All sixteen masks compile freshly with both profiles:

| Mask | O2 core bytes / bound | O1 core bytes / bound |
| ---: | ---: | ---: |
| 0, unchanged base | 4,432 / 392 | 5,840 / 352 |
| 1 | 4,448 / 400 | 5,856 / 352 |
| 2 | 4,432 / 400 | 5,856 / 352 |
| 3 | 4,464 / 408 | 5,856 / 360 |
| 4 | 4,432 / 400 | 5,872 / 360 |
| 5 | 4,448 / 408 | 5,872 / 360 |
| 6 | 4,432 / 408 | 5,872 / 360 |
| 7 | 4,464 / 416 | 5,888 / 368 |
| 8 | 4,432 / 424 | 5,840 / 360 |
| 9 | 4,448 / 432 | 5,840 / 360 |
| 10 | 4,448 / 432 | 5,856 / 360 |
| 11 | 4,464 / 440 | 5,856 / 368 |
| 12 | 4,432 / 432 | 5,856 / 368 |
| 13 | 4,448 / 440 | 5,872 / 368 |
| 14 | 4,448 / 440 | 5,872 / 368 |
| 15 | 4,464 / 448 | 5,888 / 376 |

No addition lowers either profile's text or call bound below the base.
Equal O2 text masks still lose on stack and/or O1 text. Caching dynamic
lengths alone keeps both text sizes but increases O2 bound by 32 and O1
by eight. The combined maximum O2 bound is 448, 56 above baseline.

## Parent And Sorted Cache Matrix

A second four-mask matrix tests byte parent addressing and caching all
builder arrays, including sorted symbols. The latter overrides the base
`--cache-builder counts-offsets` with `--cache-builder all`.

| Additions | O2 core / bound / public builder | O1 core / bound / public builder |
| --- | ---: | ---: |
| None, repeated base | 4,432 / 392 / 338 | 5,840 / 352 / 496 |
| Byte parent | 4,448 / 392 / 342 | 5,840 / 352 / 497 |
| All builder arrays | 4,432 / 400 / 338 | 5,856 / 352 / 498 |
| Both | 4,464 / 400 / 346 | 5,856 / 352 / 499 |

Again, no metric improves. These are compiler measurements only, not new
semantic qualifications of these optional combinations.

## Rejected Sorted-Length Loops

Two direct source trials replace the indexed sorted-length pass after the
existing count-zero gate. They read lengths through a pointer and preserve
the original ascending symbol index and nonzero-length store expression:

```c
{
    const uint32_t *cursor = lengths;
    symbolIndex = 0;
    do {
        bits = *cursor++;
        if (bits != 0) BUILD_SORTED[BUILD_OFFSETS[bits]++] = symbolIndex;
        symbolIndex++;
    } while (symbolIndex != count);
}
```

The second trial changes only the condition to `cursor != lengths + count`.
They introduce no memcpy, reordered sorted store or malformed-input fix.
Both are rejected by text/stack evidence before semantic qualification.

| Sorted pass | O2 core / bound / public builder / frame | O1 core / bound / public builder / frame |
| --- | ---: | ---: |
| Original indexed | 4,432 / 392 / 338 / 200 | 5,840 / 352 / 496 / 120 |
| Length cursor, index limit | 4,432 / 400 / 338 / 208 | 5,856 / 352 / 500 / 120 |
| Length cursor, pointer limit | 4,432 / 400 / 339 / 208 | 5,856 / 352 / 501 / 120 |

No new selector or source branch survives. The original sorted pass is
restored exactly; the committed Note 864 flag set is unchanged.

## Receipts And Verification

Ignored measurement directories:

- `conker/build/init-toggle-cache-interactions-{0..15}-20261003`
- `conker/build/init-toggle-parent-sorted-{0..3}-20261003`
- `conker/build/init-toggle-sort-index-cursor-20261003`
- `conker/build/init-toggle-sort-end-cursor-20261003`

Structured receipt re-reading verifies all 22 compile directories / 44
objects, empty compiler logs and baseline no worse on all four metrics
(O2/O1 text and O2/O1 call bound). The base is repeated in the second
matrix, so this is not 22 unique configurations. No rejected combination
gets semantic or full-corpus credit.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_builder_code_toggle.InitDecompressorBuilderCodeToggleTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_builder_code_toggle.InitDecompressorBuilderCodeToggleTests.test_exhaustive_reversed_code_increment_widths tools.tests.test_init_decompressor_builder_offset_sum.InitDecompressorBuilderOffsetSumTests.test_packed_profile_size_reduction -v
wsl make tools-check
git diff --check
```

All sixteen focused restored-baseline tests pass in 3.633 seconds, no
skips. Tool/diff checks pass. This is not a fresh whole bounded run or
full corpus. Notes 862/863 remain full-corpus evidence for the source
without toggle-first; Note 864 remains bounded evidence for that option.
No production build, hardware replay or sibling-port test is claimed.
Unrelated Game work remains preserved and excluded.

## Next

- [x] Re-measure cache interactions on the changed Note 864 combination.
- [x] Measure parent/sorted-cache additions and reject inferior sort cursors.
- [x] Restore exact source and pass focused baseline gates.
- [ ] Investigate allocation/parent-ascent dataflow or shared-call overhead, rather than repeat these rejected forms.
- [ ] Reduce the remaining 752 linked bytes and qualify changed selections before promotion.
- [ ] Complete other-profile, ownership, hardware and scheduler-resume gates.
