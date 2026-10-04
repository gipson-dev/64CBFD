# Init Decoder Entry-Value Lifetime Fitting Trials

Date: 2026-10-04. Starting HEAD: `00f89acb`.

Subsequent Game checkpoint: [Note 968](968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
qualifies and banks the separate metadata/maintenance edits preserved here.
This note's default-image identities and rejected Init experiment stand.

## Decision

Continue the requested Init work from
[Note 966](966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md)
with a new decoder dataflow hypothesis. Capturing immutable table values before
bit removal shortens the optimized compressed-decoder unit by one word in two
variants, but **does not reduce the complete executable**. Reject adoption:
the retained candidate remains 4512 bytes against 3984 retail, 528 bytes over.

The new option is disabled by default. No production Init owner, word guard,
compiler override or README aggregate changes. This is a bounded semantic-C
fitting experiment, not original-C provenance or a completed conversion.

## Hypothesis And Scope

`--entry-value-local` captures the table entry's halfword value after rejecting
operation 99, before calling `drop_bits`. Literal/length and distance paths can
be selected independently with `literal`, `distance` or `both` (the default
when the option is present without a value). Source macro modes are 2, 3 and 1
respectively; direct compilation rejects other mode values.

The captured value replaces later reads for literal output, length-base addition
or distance-base addition. The table remains unchanged during bounded compressed
decoding; the existing inherited test explicitly rejects table writes there.
The experiment changes read lifetime/order, and may read an unused value on an
end-of-block path. It does not claim identical intermediate access traces,
interrupt observations or behavior for unqualified table/state/output aliases.
Operation-99 rejection, bit consumption, signed limits, overlapping match copies,
produced-count commits and ABI shadow snapshots remain requirements.

## Complete Size Measurements

These fresh measurements use the established packed-remaining flags from
`InitDecompressorDistanceOperationLocalTests`, including physical frame scratch,
packed entries, no unroll, bounded shifts, captured builder counts/offsets,
remaining-symbol cursor, first-refill lookup, core-owned pointers and the actual
176-byte adapter. All totals include the adapter, not just public C bodies.

| Entry-value capture | O2 compressed words | O2 C text | O2 executable | O1 compressed words | O1 C text | O1 executable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Disabled control | 119 | 4336 | 4512 | 157 | 5808 | 5984 |
| Literal/length only | 118 | 4336 | 4512 | 157 | 5808 | 5984 |
| Distance only | 119 | 4336 | 4512 | 158 | 5808 | 5984 |
| Both | 118 | 4336 | 4512 | 158 | 5808 | 5984 |

Optimized allocation/padding absorbs the one-word public-unit saving. O1's
one-word growth in the distance/both variants likewise does not change the whole
allocation. The compressed unit keeps its 64-byte O2 / 56-byte O1 frame. The
core's conservative direct-call frame bounds remain 400 / 360 bytes. Nothing
has been moved into an uncounted wrapper or new data owner.

This attribution is checked against a fresh disabled control: the actual final
core body remains fifty O2 / eighty-six O1 words. The O2 core's physical final
slot grows from 51 to 52 words when compressed decoding saves a word; its
trailing alignment grows from one to two words. Conversely, O1 distance/both
grow compressed decoding from 157 to 158 words while the final core slot shrinks
from 89 to 88, with unchanged 86-word core body. Physical slot sizes must not
be mistaken for semantic core changes.

## Verification

**151 trial tests pass in 1008.263 seconds, no skips.** Twenty separate
inventory/slot-ledger/call-graph checks pass in 2.316 seconds, no skips:
171 distinct passing checks across the two invocations. Three final focused
size reruns pass in 6.206 seconds after strengthening the padding assertions;
these repeat existing tests and are not counted as additional distinct coverage.

The new module compiles all three retained shapes and both compiler profiles
for each capture mode, links the real adapter, and inherits the complete bounded
connected decoder tests. Its 151 tests include the native semantic control,
CU1-clear/set paths, context and failure snapshots, malformed/repeated blocks,
fixed tables, signed stale cells, nested lookup, representative retail pages,
poisoned state fields, live-SP fences and saved-register contracts.

Each guest class also recompiles the disabled packed-remaining control and
requires the banked instruction hashes, independently of debug/source hashes:

```text
O2 .text 4336 bytes 177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d
O1 .text 5808 bytes 8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755
```

The audit verifies all 47 retained ASM owners/raw slots and the existing linked
Init code/data and Game data. Each optimized packed trial retains 3248 bytes of
static/observed total stack descent, including the adapter and inherited decoder
frame; private-stack reservation is still unproven. Both disabled-option control
instruction hashes above are freshly verified for every guest capture class.
The production ELF is unchanged by these isolated experiments; no new production
rebuild is claimed. Project tool and whitespace checks pass.

```sh
python3 -m unittest tools.tests.test_init_decompressor_entry_value_local -q -f
python3 -m unittest tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls -q -f
make tools-check
```

Qualification receipts are written under the ignored
`conker/build/init-entry-value-local/` directory. Neither full 507-page guarded
CU1 corpus is rerun. Bounded fixtures and compiled-instruction models are not
hardware execution or gameplay acceptance.

## Next Work

- [x] Measure literal/length, distance and combined capture separately.
- [x] Count complete executable allocation and actual adapter costs.
- [x] Reject adoption despite the one-word optimized public-unit saving.
- [x] Preserve all existing production owners and raw section identities.
- [x] Finish all 151 connected/native trial checks and default instruction-image checks.
- [ ] Find a complete-image reduction, not merely a smaller public routine.
- [ ] Resolve decoder private-stack reservation and entry/placement ownership.

Production Init remains 492 C / 47 assembly entries. The seventeen investigation
targets and thirty intentional assembly owners remain as classified in Note 966.
Three pending Game metadata/cache-maintenance edits are preserved and excluded
from this Init checkpoint. No sibling source/build, frozen Release, save, ROM
promotion, hardware/gameplay acceptance or push is included.
