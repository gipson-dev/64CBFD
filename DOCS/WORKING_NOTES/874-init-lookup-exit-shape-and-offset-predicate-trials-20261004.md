# Init Lookup Exit Shape And Offset Predicate Trials

Date: 2026-10-04. Baseline: `9dd113cd` (Note 873).

## Result

Two first-refill lookup exit forms do not reduce the complete packed object
text. Both temporary edits are removed; the experiment source is restored
exactly to HEAD. No new option or production conversion survives.

Disassembly first rules out operation-read caching as an instruction-removal
hypothesis: the retained O2 helper already has one operation-byte load at
offset 0x6C4, reused for both leaf predicates and the child width.

## Trials

The common-return form keeps shared dispatch, but tests
`operation > 16 && operation != 99`, performs child drop/refill/value sampling
in the true branch, and breaks to a return after the loop in the false branch.
It saves raw helper words but padding absorbs the complete-object savings.

The offset-predicate form sets `width = operation - 17u`, continues for
`width < 239 && width != 82`, then increments width before child processing.
All 256 possible unsigned operation bytes are checked by a host algebra
probe: child classification matches operation > 16 and operation != 99,
and every accepted child width matches operation - 16. This is not 256
MIPS executions or guest semantic qualification. Refill and child-value read
order remain spelled as in Note 873; no trial full guest run is claimed.

Complete Note 873 packed-remaining configuration, core-only measurements:

| Exit form | O2 core / lookup words / core bound | O1 core / lookup words / core bound |
| --- | ---: | ---: |
| Retained early return | 4,384 / 46 / 392 | 5,824 / 45 / 352 |
| Child gate, common return | 4,384 / 45 / 392 | 5,824 / 42 / 352 |
| Offset predicate, common return | 4,384 / 46 / 392 | 5,824 / 44 / 352 |

The common-return form is the better raw helper alternative, but offers no
whole-text saving on these receipts. Do not present the helper-word reduction
as a reduction of the 704-byte linked excess. Its receipt can inform future
combined alignment trials; it is not a retained selector or qualified source.

Ignored receipts:

- `conker/build/init-lookup-child-gated-common-return-20261004`
- `conker/build/init-lookup-offset-operation-gate-20261004`

All four compiler logs are empty. Source restoration passes scoped
`git diff --exit-code`. Fifteen call-graph/ledger and retained first-refill
size/dependency tests pass in 2.778s, no skips. These freshly compile the
restored configuration; they do not qualify the discarded trial functions.
Project tool and whitespace checks pass.

## Pick Up

The retained Note 873 option stays at 4,688 linked O2 bytes / 704 excess;
its changed full corpus remains open. Notes 871/872 continue to qualify only
the prior omitted-option baseline. Do not repeat these two exit forms or
operation-read caching unchanged as aggregate fitting improvements.

Production Init sources, defaults, progress CSV and README totals remain
unchanged. Unrelated Game source/tests are preserved and excluded from staging.
