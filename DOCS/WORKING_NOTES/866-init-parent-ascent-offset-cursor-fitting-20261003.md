# Init Parent Ascent Offset Cursor Fitting

Date: 2026-10-03. Baseline: `b2b7a43e`.

## Result

Opt-in `--parent-ascent-cursor` traverses builder parent offsets with a
descending pointer while retaining the original integer level and consumed
bit updates. Packed O2 core text falls 4,432 to 4,416; with the unchanged
304-byte aligned adapter, linked text is 4,720, 736 over retail. Packed
O2/O1 call bounds and O1 text hold. Public builder is 336 words in O2,
down from 338, and 497 in O1, up from 496 but absorbed by padding.

This is a selected packed-profile improvement, not a universal win.
Frame O2 saves 32 bytes; frame O1 grows 16. Aligned O2 saves 16 but adds
eight bound bytes; aligned O1 grows 16 and adds eight bound bytes. All
profiles are measured and bounded, without assigning production acceptance.
Defaults/production/README totals remain unchanged.

## Source And Root Barrier

```c
{
    const uint32_t *offsetCursor = BUILD_OFFSETS + level;
    while ((code & BUILD_LOW_MASK(consumed)) != *offsetCursor) {
        offsetCursor--;
        level--;
        consumed -= width;
    }
}
```

The original indexed loop remains the default. The cursor starts at the
same offset as the indexed expression and decreases alongside level, so
it reads the same offset values in the same logical order. No table store,
allocation, code increment, width calculation, root update or FPR capture
is moved. The rejected mask-reuse variants below are removed.

In the bounded domain, widths are 1..16. The first emitted symbol must
allocate level zero: initial consumed is -width and the allocation condition
is bits > 0. Thereafter consumed is level * width, preserved by allocation
and ascent updates. Offsets[0] is explicitly zero. At level zero the mask
is zero, so both sides of the comparison are zero and ascent stops. The
cursor is never decremented before the array root in this domain. This
argument is not an arbitrary malformed-frame or alias-equivalence claim.

## Trial Measurements

All three initial trials use Note 864's complete packed/remaining flags:

| Trial | O2 core / bound / public builder | O1 core / bound / public builder |
| --- | ---: | ---: |
| Note 864 baseline | 4,432 / 392 / 338 | 5,840 / 352 / 496 |
| Offset cursor, retained opt-in | 4,416 / 392 / 336 | 5,840 / 352 / 497 |
| Reuse next as mask, rejected | 4,432 / 392 / 338 | 5,856 / 352 / 498 |
| Offset cursor plus reused mask, rejected | 4,416 / 392 / 336 | 5,856 / 352 / 499 |

Mask reuse sets `next = BUILD_LOW_MASK(consumed)` before the loop and after
each consumed update, then compares code & next. It has no packed O2
advantage and grows O1 text by 16, whether alone or combined. Rejected
forms receive compiler evidence only, not semantic qualification.

Packed builder frames stay 200 O2 / 120 O1. The O2 builder region contains
336 public words plus the unchanged 22 ABI-capture and 50 lookup helper
words, 408 total. Public builder still exceeds its 293-word slot by 43
words. The linked reduction is not claimed as four public words removed.
State remains 116 bytes; adapter body/aligned text remains 296/304.

Fresh six-shape linked measurements:

| Shape / compiler | Linked text before / after | Core bound before / after | Total static / observed descent after |
| --- | ---: | ---: | ---: |
| Frame / O2 g3 | 5,888 / 5,856 | 424 / 424 | 3,272 / 3,272 |
| Frame / O1 | 6,336 / 6,352 | 360 / 360 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,752 / 4,736 | 376 / 384 | 3,232 / 3,232 |
| Aligned end / O1 | 6,128 / 6,144 | 336 / 344 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,736 / 4,720 | 392 / 392 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,144 / 6,144 | 352 / 352 | 3,200 / 3,200 |

Packed minimum-SP bound remains 0x80031D68, 88 bytes above the known
neighbor ending at 0x80031D10. This is not complete stack-reservation or
hardware safety proof. The changed profile needs its own corpus receipts.

Ignored initial trial receipts:

- `conker/build/init-parent-ascent-offset-cursor-20261003`
- `conker/build/init-parent-ascent-reused-mask-20261003`
- `conker/build/init-parent-ascent-cursor-mask-20261003`

These precede the final option guard; final tests freshly compile/link the
flagged source for all six shapes with the core-owned ABI-shadow adapter.

## Verification

`tools/tests/test_init_decompressor_parent_ascent_cursor.py` inherits the
toggle-first bounded suite. A new get observer records four-byte offset
reads for complete [1,2,3,3] and depth-16 trees, each with root width one,
across all six builds: twelve executions. It requires an actual adjacent
offset[1] to offset[0] read pair, with zero at the root.

The strengthened short-tree fixture rejects a four-byte read at root - 4.
That physical word is the final sorted slot, unused by these small complete
trees; this guard is not imposed on general full-capacity cases. An explicit
negative read after each execution proves the guard is active. The final
observer version passes with the helper/baseline gates below.

Fresh guest run: 32 tests in 249.516 seconds, 31 pass and one intentional
full-corpus skip. All six observed descents equal static bounds. The inherited
504 context comparisons, 132 direct builders, six fixed initializers,
48 direct header-alignment executions, 131,070 host increment pairs,
ordered prefix/repeat writes and failure gates pass. The strengthened guard
was added after this run loaded and passes separately in the focused gate;
no claim is made that its negative read was in the original run's count.

Thirteen call/ledger helpers, omitted-option size and strengthened observer
pass together: fifteen tests in 8.741 seconds, no skips. Combined executions
give 46 passing tests / one skip, including the observer retest. Tool/diff
checks pass. A fresh omitted-option
compile in `init-ascent-cursor-omitted-option-20261003` reproduces Note 864's
O2/O1 `.text` sections byte-for-byte against the Note 865 mask-zero objects,
verified with GNU objcopy and cmp. This is not an entire-object or ROM claim.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_parent_ascent_cursor -v -f
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_builder_code_toggle.InitDecompressorBuilderCodeToggleTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_parent_ascent_cursor.InitDecompressorParentAscentCursorTests.test_parent_offsets_descend_to_root_without_underflow -v
wsl make tools-check
git diff --check
```

No changed-option full corpus, production build, hardware replay or sibling
port test is claimed. Notes 862/863 remain full-corpus receipts for the
older source without toggle-first or ascent cursor. Unrelated Game work
remains preserved and excluded.

## Next

- [x] Measure parent cursor, mask reuse and their combination.
- [x] Retain only the cursor behind an explicit option, preserving defaults.
- [x] Observe descent to the root and activate the short-tree underflow guard.
- [x] Finish the fresh compiled guest suite before banking the option.
- [ ] Continue fitting; selected packed O2 remains 736 linked bytes over retail.
- [ ] Qualify the changed combination and other-profile/ownership/hardware/resume gates before promotion.
