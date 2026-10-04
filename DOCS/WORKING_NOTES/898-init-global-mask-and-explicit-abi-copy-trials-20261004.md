# Init Global Mask And Explicit ABI Copy Trials

Date: 2026-10-04. Starting HEAD: `68da84f8`.

## Hypotheses

Two new shared-helper trials use the complete packed scan-deficit flags:

1. Replace the pure `low_mask` function with a single-evaluation expression
   macro at every call site. Unlike earlier partial inlining trials, this
   removes the standalone helper entirely. The expression retains width & 31.
2. Restore the mask helper; replace the six-word loop in `abi_capture` with
   six explicit saved-register assignments, retaining ascending copy order.

These are isolated source/compiler experiments, not production conversions.

## Measurements

| Form | O2 whole text / core call bound | O1 whole text / core call bound |
| --- | ---: | ---: |
| Qualified scan-deficit baseline | 4,384 / 392 | 5,792 / 352 |
| Global low-mask expression | 4,384 / 400 | 5,808 / 352 |
| Explicit six-word ABI capture | 4,400 / 392 | 5,792 / 352 |

Global mask replacement removes the helper but increases dynamic public words
256 -> 259 and its frame 104 -> 112 in O2. Other allocation/layout changes
leave complete O2 text neutral while increasing the call bound eight bytes.
O1 grows sixteen bytes. Explicit ABI capture grows O2 sixteen bytes without
improving O1. Reject both before semantic qualification; no selector survives.

Ignored receipts:

- `conker/build/init-global-low-mask-expression-trial-20261004`
- `conker/build/init-abi-capture-explicit-six-copy-trial-20261004`

## Restoration And Verification

Both original helpers restored exactly: experiment source diff empty, blob
`42b4a7d418964cb81900a6206fb31096e9089bd4`, matching Notes 893/894.
Sixteen call-graph/ledger, packed size, ordered seed and distance-builder
failure/empty-tree tests pass in 22.728 seconds, no skips. Those tests exercise
the restored candidate; no discarded-source semantic or corpus credit.
Project tool and whitespace checks pass. No new full corpus or ROM build.

Qualified packed O1 remains 5,984 linked bytes; best default O2 remains 4,576 /
592 excess. Production/defaults/README and unrelated Game work unchanged.
Next fitting work needs a different dataflow/ownership hypothesis, not another
unchanged partial/global mask or explicit-copy attempt.
