# Init Builder Sort Offset Local Trials

Date: 2026-10-04. Starting HEAD: `92c0adca`.

## Hypothesis

The retained sorted-symbol pass uses
`BUILD_SORTED[BUILD_OFFSETS[bits]++] = symbolIndex`. Packed O2 reloads the
bucket offset after the sorted store. An explicit local offset might eliminate
that reload and lower total text without another cached array pointer.
This differs from Note 865's length-cursor and cached-sorted-pointer trials.

Two isolated manual source trials retained the ascending indexed length scan:

```c
uint32_t offset = BUILD_OFFSETS[bits];
BUILD_SORTED[offset] = symbolIndex;
BUILD_OFFSETS[bits] = offset + 1;
```

The second places the offset update before the sorted store. These trials
assume separate valid scratch arrays and are not claims of arbitrary alias
equivalence. Neither receives semantic or production qualification: size and
stack evidence rejects both first.

## Measurements

Fresh compiler runs use the complete retained packed/remaining flag set from
the qualified baseline. Core bytes include alignment and embedded helpers;
public builder words are not presented as the whole connected core.

| Form | O2 core / builder words / frame / core call bound | O1 core / builder words / frame / core call bound |
| --- | ---: | ---: |
| Retained baseline | 4,384 / 333 / 200 / 392 | 5,824 / 496 / 120 / 352 |
| Local, sorted store first | 4,384 / 333 / 208 / 400 | 5,840 / 497 / 128 / 360 |
| Local, offset update first | 4,384 / 333 / 208 / 400 | 5,824 / 494 / 128 / 360 |

Both fail to reduce complete O2 text and increase both call bounds by eight
bytes. The second saves two public O1 builder words but no complete core text;
that is insufficient to retain an increased stack requirement.

Ignored receipts:

- `conker/build/init-sort-offset-local-trial-20261004/measurements.json`
- `conker/build/init-sort-offset-first-trial-20261004/measurements.json`
- Baseline: `conker/build/init-limit-baseline-20261004/measurements.json`

## Restoration And Checks

Both trial edits removed. Experiment source has an empty Git diff and restored
blob `bdc96bf5835c86bdd67a495e60f8a5b63cbe9071`, matching Notes 887/888.
Adapter remains unchanged. No new selector or production source change.

```sh
python3 -m unittest tools.tests.test_init_decompressor_semantic tools.tests.test_init_decompressor_slot_ledger -v -f
```

Seventeen restored-baseline semantic/ledger tests pass in 10.494 seconds,
no skips. The native semantic test includes all retail pages against zlib and
the pristine image; it is not a new compiled-guest guarded corpus run.

Retained linked O2 remains 4,576 bytes, 592 over retail. Production remains
492 C / 47 assembly Init functions. README and unrelated Game edits untouched.

## Next

- [x] Measure explicit local offsets in both store orders.
- [x] Reject text-neutral stack growth and restore the qualified source exactly.
- [ ] Investigate a different whole-core lifetime or shared-call opportunity;
  do not repeat these offset-local forms unchanged.
- [ ] Fit the region and complete reservation, ownership and hardware gates.
