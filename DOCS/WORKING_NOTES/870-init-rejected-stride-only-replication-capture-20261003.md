# Init Rejected Stride Only Replication Capture

Date: 2026-10-03. Baseline: `6709bfad`, retained Note 867 source.

## Result

Capturing only the builder's replication stride does not improve the current
packed-remaining configuration. Both trials are removed, restoring the source
exactly to HEAD. Unlike the prior leaf-table cache and pointer-cursor trials,
these retain `BUILD_WORKSPACE[table + next]` indexing and capture no table base.

The first form calculates `stride = 1u << BUILD_SHIFT(bits - consumed)`
before the existing for loop and uses `next += stride`. The second performs
the same calculation inside `if (next < size)` and uses a do/while store,
increment and bound check. Original numeric store indices and stride masking
are retained. No zero-run store or pointer endpoint is introduced.

## Measurements

Complete Note 867 packed-remaining configuration, core-only object receipts:

| Form | O2 core / bound / builder words / frame | O1 core / bound / builder words / frame |
| --- | ---: | ---: |
| Retained baseline | 4,400 / 392 / 333 / 200 | 5,840 / 352 / 496 / 120 |
| Stride captured before for | 4,416 / 400 / 334 / 208 | 5,840 / 360 / 497 / 128 |
| Gated stride and do/while | 4,400 / 400 / 333 / 208 | 5,856 / 360 / 499 / 128 |

Both trials add eight bytes to the builder frame and whole-core call bound
under both profiles. Neither improves aligned text across both compilers.
No new selector survives and no stack-budget tradeoff is silently accepted.

Ignored receipts: `conker/build/init-builder-stride-only-20261003` and
`conker/build/init-builder-gated-stride-only-20261003`. All four compiler logs
are empty. Source restoration passes `git diff --exit-code`.

## Retained Configuration Qualification

The fresh bounded guest suite is run only after restoring the source:

```sh
wsl python3 -m unittest tools.tests.test_init_decompressor_builder_allocation_table -v -f
```

The process terminates successfully: 33 tests in 260.739 seconds, 32 passes
and one intentional opt-in corpus skip. Ordered allocation commits, root
descent, initializer poison and neighbor red-zone guards pass. The nested
lookup gate fires on page 169 with 3,212 calls and 3,383 iterations.
All six fresh linked receipts retain the following text and total stack costs:

| Shape / profile | Linked bytes | Static / observed descent |
| --- | ---: | ---: |
| Frame / O2 g3 | 5,840 | 3,272 / 3,272 |
| Frame / O1 | 6,336 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,736 | 3,232 / 3,232 |
| Aligned end / O1 | 6,128 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,704 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,144 | 3,200 / 3,200 |

The full 507-page corpus remains opt-in and is not qualified by these
representative pages. No fresh production ROM build or hardware run is
claimed. Project tool and whitespace checks pass.

## Next Work

Do not repeat either stride-only shape unchanged, or the already rejected
leaf-base/pointer-cursor and mask/drop helper subsets. Current retained linked
experiment remains 4,704 bytes against retail's 3,984-byte decoder budget.
The public builder still needs 40 words removed; new structural dataflow or
caller evidence is needed. Corpus, ownership and hardware/context gates remain
separate from size fitting and bounded guest execution.

No production Init sources, defaults, progress CSV or README totals change.
Unrelated dirty Game source/tests remain preserved and excluded from staging.
