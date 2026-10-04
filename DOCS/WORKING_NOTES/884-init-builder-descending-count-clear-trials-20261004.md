# Init Builder Descending Count Clear Trials

Date: 2026-10-04. Baseline: `fdc294f2`, unchanged Notes 879-881 sources.

## Hypothesis And Domain

The forward count clear uses a counter and induction address to zero all
17 buckets before histogram construction. A descending index might remove
loop-control instructions. Two forms were measured:

```c
for (bits = 17; bits-- != 0;) BUILD_COUNTS[bits] = 0;
```

```c
bits = 17;
do { BUILD_COUNTS[--bits] = 0; } while (bits != 0);
```

Both enumerate buckets 16..0 once, versus the original 0..16 order. The
count-zero early return remains before clearing. Subsequent histogram and
minimum-length selection do not use the terminal counter value. This is a
final-array-value observation, not arbitrary alias or asynchronous store-order
equivalence. Neither trial received guest qualification.

The pointer-endpoint clear rejected in
[Note 860](860-init-builder-running-offset-sum-text-stack-tradeoff-20261003.md)
was not repeated. Both new trials use the complete retained packed-remaining
options, including first-refill lookup and table-derived allocation.

## Measurements

| Form | O2 core text | O2 public builder words | O2 builder frame / core bound | O1 core text | O1 public builder words | O1 builder frame / core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Qualified forward baseline | 4,384 | 333 | 200 / 392 | 5,824 | 496 | 120 / 352 |
| Descending post-decrement | 4,384 | 333 | 208 / 400 | 5,856 | 501 | 128 / 360 |
| Descending pre-decrement | 4,384 | 332 | 200 / 392 | 5,840 | 497 | 120 / 352 |

Post-decrement saves no O2 text and adds eight bytes to both core bounds;
O1 also grows 32 text bytes. Pre-decrement saves one raw O2 builder word,
but whole core text stays unchanged and O1 grows 16 bytes. Neither improves
aggregate fitting. Both branches are removed; no CLI option remains.

Ignored receipts/disassemblies are under
`conker/build/init-count-clear-descending-trial-20261004/` and
`conker/build/init-count-clear-predecrement-trial-20261004/`. All four trial
compiler logs are empty. Baseline receipts remain at
`conker/build/init-limit-baseline-20261004/` (Note 882).

## Restoration And Verification

The semantic source matches qualified Git blob
`bdc96bf5835c86bdd67a495e60f8a5b63cbe9071` exactly, with empty scoped diff.
Thirteen focused retained tests pass in 10.319 seconds, no skips: ledger,
corpus selection, FR=1 word loads, packed size, executed callee-clobber guard,
and direct builder cursor boundaries. Relevant guest gates freshly compile
and link all six retained shapes. Tool and whitespace checks pass. No full
bounded or corpus rerun is claimed here.

Notes 880/881's 1,014 paired pages remain scoped to the restored forward
baseline. Linked O2 stays 4,576 bytes, 592 over retail; total bound 3,240.
Production remains 492 C / 47 assembly rows. README/defaults and production
sources stay unchanged; unrelated Game source/tests are preserved and unstaged.

## Next Work

Do not repeat these clear-loop forms unchanged. Continue aggregate fitting
and entry/frame ownership, full reservation and hardware/context gates.
No production conversion, ROM build or sibling-port test is claimed.
