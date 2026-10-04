# Init Mask Before Refill Lifetime Trials

Date: 2026-10-04. Starting HEAD: `7d5eec39`.

## Hypothesis And Scope

Computing the pure modulo-32 low-bit mask before `need_bits` may change
register lifetimes across the refill call and reduce shared-helper text.
This is not the rejected inline-mask or operation-cache trial: the helper call
is retained, only its evaluation moves before refill. State read/write order
and child entry-value sampling remain unchanged in the source.

Two isolated trials use the complete retained packed/remaining compiler flags:

1. In `take_bits`, compute `uint32_t mask = low_mask(width)` before refill,
   then sample `s->reservoir & mask` after refill and retain `drop_bits`.
2. Restore `take_bits`. In first-refill lookup, compute the initial mask before
   the first refill; recompute after child drop and before child refill, then
   use the local mask for each workspace index. Keep the child root read after
   refill, as in the qualified baseline.

## Measurements

| Form | O2 whole core bytes / call bound | O1 whole core bytes / call bound |
| --- | ---: | ---: |
| Retained baseline | 4,384 / 392 | 5,824 / 352 |
| Take-bits mask before refill | 4,400 / 392 | 5,840 / 352 |
| Lookup masks before refill | 4,416 / 392 | 5,856 / 352 |

Both increase complete text in both profiles. Neither improves the call bound.
Reject both before semantic qualification; no corpus credit is assigned to
either discarded source. The lifetime hypothesis does not yield a fitting
improvement in these measured configurations.

Ignored receipts, objects, disassembly and compiler logs:

- `conker/build/init-take-mask-before-refill-trial-20261004`
- `conker/build/init-lookup-mask-before-refill-trial-20261004`
- Baseline: `conker/build/init-limit-baseline-20261004`

## Restoration And Verification

Both edits removed. Experiment source has an empty scoped Git diff and blob
`bdc96bf5835c86bdd67a495e60f8a5b63cbe9071`, matching Notes 887/888.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_lookup_first_refill.InitDecompressorLookupFirstRefillTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_lookup_first_refill.InitDecompressorLookupFirstRefillTests.test_first_refill_requires_shared_loop -v -f
```

All fifteen tests pass in 5.627 seconds, no skips. The retained lookup size
test freshly compiles its six shapes and checks packed core sizes/bounds and
builder sizes. Its legacy adapter size assertion is not a fresh direct-FPR
adapter qualification. No full semantic suite or guarded corpus is rerun here.

The qualified direct-load linked O2 baseline remains 4,576 bytes / 592 excess.
No production Init source, compiler defaults, profiles, guards, README totals
or sibling-port artifacts change. Unrelated Game work remains untouched.

## Next

- [x] Measure pure mask lifetime before refill in both shared helpers.
- [x] Reject whole-text growth and restore the qualified source exactly.
- [ ] Investigate another core dataflow opportunity; do not repeat these forms
  as prospective savings without a changed compiler/context hypothesis.
- [ ] Complete fitting, full reservation, ownership and hardware/context gates.
