# Init Builder Wide Operation And Header Packing Trials

Date: 2026-10-04. Starting HEAD: `679c0634`.

## Hypothesis

The packed O2 builder masks the simple-symbol operation to a byte and copies
the result before shifting it into the high byte. A wider local operation may
let the final shift discard high bits without that intermediate narrowing.
This is a local-accumulator experiment, not a change to the table entry layout.

Two isolated trials on the complete scan-deficit packed configuration:

1. Widen only `entryOperation` from uint8 to uint32. Keep entryBits narrow and
   the guest packing expression unchanged. Preserve little-endian native
   truncation with `(uint8_t)entryOperation` before its low-byte OR.
2. Keep that wider operation, but combine the header first:
   `packed = ((entryOperation << 8) | entryBits) << 16 | value`.

Neither changes state stores or the packed table ABI. Both are rejected on
whole-text/stack measurements before semantic qualification.

## Measurements

| Form | O2 core / public builder / frame / call bound | O1 core / public builder / frame / call bound |
| --- | ---: | ---: |
| Qualified scan-deficit baseline | 4,384 / 333 / 200 / 392 | 5,792 / 488 / 120 / 352 |
| Wide operation | 4,384 / 331 / 208 / 400 | 5,792 / 488 / 128 / 360 |
| Wide operation, combined header | 4,384 / 331 / 208 / 400 | 5,792 / 488 / 128 / 360 |

The expected two public O2 words disappear, but alignment leaves whole core
text unchanged. Both profiles gain eight bytes in the builder frame and core
call bound. Reject both; no smaller linked candidate is retained.

Ignored receipts and disassembly:

- `conker/build/init-builder-wide-operation-trial-20261004`
- `conker/build/init-builder-wide-combined-header-trial-20261004`

## Restoration And Verification

Both edits removed. Experiment source diff is empty and restored blob is
`42b4a7d418964cb81900a6206fb31096e9089bd4`, matching Notes 893/894.
Twenty semantic/ledger and scan-deficit size/executed-branch/domain tests pass
in 12.163 seconds, no skips. Native semantic coverage includes all retail
pages; this is not a fresh compiled-guest full guarded corpus. No discarded
trial receives semantic or corpus credit. Project tool/whitespace checks pass.

Qualified packed O1 remains 5,984 linked bytes; default best O2 remains 4,576
(592 over retail). Production sources, defaults, profiles, guards and README
totals unchanged. Unrelated Game work remains untouched and unstaged.

## Next

- [x] Measure wider operation and combined-header packing on the current option.
- [x] Reject whole-text-neutral stack growth and restore qualified source.
- [ ] Seek a different lifetime/packing opportunity; these forms are not savings.
- [ ] Complete best-profile fitting, full reservation, ownership and hardware gates.
