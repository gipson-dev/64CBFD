# Init Fixed Length Cursor Endpoint Trials

Date: 2026-10-04. Starting HEAD: `24d645e0`.

## Hypotheses

The distance-length initializer reloads the frame pointer during each of its
thirty ascending stores. Two isolated trials replace the indexed loop with a
pointer cursor: one compares against `LENGTHS(s) + 30`, the other captures a
local end pointer from the freshly sampled base after the first builder call.

A third trial restores the distance loop and derives literal range endpoints
from the current cursor: add 144, 112, 24 and eight entries for the four
constant ranges. It replaces only the selected fixed-length-cursor branch.
No builder call or ABI snapshot is moved. Separate state/frame storage is a
bounded fixture assumption, not unrestricted alias equivalence.

## Compiler Measurements

All trials use the complete packed scan-deficit configuration. Table columns
are whole core bytes / public fixed-initializer words / initializer frame.

| Form | O2 | O1 |
| --- | ---: | ---: |
| Qualified baseline | 4,384 / 78 / 40 | 5,792 / 116 / 48 |
| Distance cursor, repeated end expression | 4,384 / 78 / 40 | 5,808 / 119 / 56 |
| Distance cursor, captured end | 4,384 / 77 / 40 | 5,808 / 119 / 56 |
| Literal relative endpoints | 4,384 / 75 / 48 | 5,808 / 119 / 56 |

Whole-core call bounds remain 392 O2 / 352 O1 because another path dominates.
All forms fail to shrink complete O2 text and grow O1 text sixteen bytes.
Relative literal endpoints also increase the O2 initializer frame eight bytes.
Reject all three before semantic qualification; public word savings alone
do not reduce the linked excess.

Ignored receipts:

- `conker/build/init-fixed-distance-cursor-trial-20261004`
- `conker/build/init-fixed-distance-cached-end-trial-20261004`
- `conker/build/init-fixed-literal-relative-ends-trial-20261004`

## Restoration And Checks

All edits removed. Scoped source diff is empty; restored blob
`42b4a7d418964cb81900a6206fb31096e9089bd4` matches Notes 893/894.
Nine ledger, retained packed size and ordered full fixed-initializer tests
pass in 4.200 seconds, no skips. The initializer gate compares ordered length
stores and complete tables across six freshly compiled shapes. This is
restored-baseline evidence, not qualification of discarded source forms.
Project tool and whitespace checks pass; no new full corpus run is claimed.

Qualified packed O1 stays 5,984 linked bytes; best default O2 remains 4,576 /
592 excess. No production, defaults, README or unrelated Game changes.
Next fitting work should use a different lifetime/dataflow hypothesis, not
repeat these endpoint forms unchanged.
