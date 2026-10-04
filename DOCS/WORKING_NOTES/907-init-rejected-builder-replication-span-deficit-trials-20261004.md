# Init Rejected Builder Replication Span Deficit Trials

Date: 2026-10-04. Starting HEAD: `79c9d070`.

## Hypothesis

Note 870 already rejected stride capture, and Note 828 rejected leaf-pointer
endpoint iteration. Test a different termination shape: a signed remaining
span decremented by stride, preserving the existing `next < size` first-store
gate. This aims to replace the repeated unsigned index-versus-size comparison.

Two temporary forms replace only the non-cached leaf replication branch.
Both use the complete Note 904 packed pointer-owned/dynamic-order configuration.
They are compiler/size trials only; no execution equivalence is claimed.

Entry-unit form:

```c
if (next < size) {
    uint32_t stride = 1u << BUILD_SHIFT(bits - consumed);
    int32_t fillLeft = (int32_t)(size - next);
    do {
        BUILD_WORKSPACE[table + next].alignment = packed;
        next += stride;
        fillLeft -= stride;
    } while (fillLeft > 0);
}
```

The second form uses `stride = 4u << BUILD_SHIFT(bits - consumed)`, numeric
`fillOffset = (table + next) << 2`, and
`fillLeft = (int32_t)((size - next) << 2)`. Each packed word store addresses
`(uint8_t *)BUILD_WORKSPACE + fillOffset`, then advances the numeric byte offset
and subtracts the byte stride. It creates no pointer endpoint, captures no
workspace/table base, and retains the same first-store gate. This variant tests
whether moving scale/address arithmetic outside the loop offsets span tracking.

The proposed deficit domain relies on bounded widths; no native signed/unsigned
conversion or broad malformed-input equivalence is established by compilation.

## Measurements

Core object receipts, excluding unchanged 176-byte adapter:

| Form | O2 core text / public builder words / builder frame / core call bound | O1 core text / public builder words / builder frame / core call bound |
| --- | --- | --- |
| Qualified dynamic-order baseline | 4352 / 333 / 200 / 400 | 5808 / 488 / 120 / 360 |
| Entry-unit span deficit | 4384 / 343 / 216 / 416 | 5824 / 494 / 128 / 368 |
| Byte-unit span deficit | 4384 / 344 / 216 / 416 | 5840 / 496 / 136 / 376 |

Both add 32 O2 core bytes and sixteen bytes to its nested call bound. The
entry-unit form grows O1 sixteen text bytes/eight bound bytes; byte-unit form
grows O1 thirty-two text bytes/sixteen bound bytes. Neither improves fitting.
Do not retain a selector or accept these regressions as a stack tradeoff.

Ignored receipts: `conker/build/init-builder-fill-deficit-trial-20261004/`
and `conker/build/init-builder-fill-byte-deficit-trial-20261004/`.
Each contains both profiles, object disassembly and measurements. Reproduction
uses Note 904's complete flags, including `--dynamic-order-cursor`, after applying
the corresponding temporary source shape above. No trial source survives.

## Restoration And Checks

The semantic source is restored exactly to HEAD, verified with
`git diff --exit-code -- tools/experiments/init_decompressor_semantic.c`.
No new compiler option, test fixture or assembler change remains.

Seventeen focused tests pass in 5.916 seconds, no skips: retained size/alignment,
direct builder cursor boundaries, ordered allocation commits, executed
scan-deficit branch, six call-graph analyzer checks and seven slot-ledger checks.
These run after restoration and qualify the retained source, not rejected forms.

```sh
python3 -m unittest tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorTests.test_direct_builder_cursor_boundaries tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorTests.test_ordered_allocation_commits_match_retail_counter tools.tests.test_init_decompressor_dynamic_order_cursor.InitDecompressorDynamicOrderCursorTests.test_compiled_deficit_branch_is_executed tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger -v -f
make tools-check
git diff --check
```

Project tool and whitespace checks pass. Notes 905/906 remain prior full-corpus
evidence for the unchanged retained candidate, not freshly rerun here.

## Decision

- [x] Measure entry-unit and byte-unit replication deficits.
- [x] Reject both and restore the qualified source exactly.
- [ ] Further fitting, full reservation, entry/frame ownership and hardware/context.

Retained packed O2 remains 4528 linked / 544 excess / 3248 descent; O1 remains
5984 linked / 3208 descent. Production Init remains 492 C / 47 ASM functions.
Production sources, README totals, word guards, sibling-port artifacts and
unrelated Game work remain unchanged. No ROM build or hardware run claimed.
