# Init Rejected Take Bits Mask And Drop Inlining

Date: 2026-10-03. Baseline: `47b8de5a`, unchanged Note 867 experiment source.

## Result

Two new narrow helper trials do not improve the packed-remaining decoder.
Both are removed, with experiment source restored exactly to HEAD. Together
with Note 868, this rules out the three nonempty mask/drop inlining subsets
inside take_bits on the current retained configuration. It does not rule out
different caller/state designs or future compiler profiles.

## Source And Measurements

Refill remains the original `need_bits(s, width)` call in both trials.
Mask-only substitutes the exact low_mask body at its existing read site:

```c
value = s->reservoir & ((1u << (width & 31)) - 1);
drop_bits(s, width);
```

Mask-and-drop additionally substitutes:

```c
s->reservoir >>= width & 31;
s->bits -= width;
```

All modulo-32 masks remain. No refill caching, count narrowing, state-access
reordering or malformed-stream correction is introduced. These are direct
temporary source edits, not retained flags or production implementations.

Complete Note 867 packed-remaining configuration, core-only object receipts:

| Form | O2 g3 bytes / core bound | O1 bytes / core bound | O2 / O1 take_bits words |
| --- | ---: | ---: | ---: |
| Baseline | 4,400 / 392 | 5,840 / 352 | 20 / 21 |
| Drop only, Note 868 | 4,416 / 392 | 5,872 / 352 | 24 / 28 |
| Mask only, new | 4,400 / 392 | 5,856 / 352 | 20 / 24 |
| Mask and drop, new | 4,432 / 392 | 5,872 / 352 | 26 / 29 |

Mask-only preserves the 32-byte helper frame under both profiles; combined
inlining lowers its O2 helper frame to 24 while O1 stays 32. Neither changes
the maximum whole-core nested call bound. Both shared helper definitions
remain required by other callers; eliminating these calls does not eliminate
their definitions. The O2 same-size mask-only form still loses on O1, so it
is not retained as an additional selector with no aggregate benefit.

Ignored receipts are `conker/build/init-take-inline-mask-20261003` and
`conker/build/init-take-inline-mask-drop-20261003`. All four compiler logs
are empty. Baseline receipt is `init-take-drop-restored-20261003` from Note 868.

## Verification And Next Work

After removing both trials, `git diff --exit-code` passes for the source.
Fourteen call-graph, slot-ledger and retained allocation-table size gates
pass in 3.174 seconds, no skips. The size gate freshly compiles the retained
configuration. Tool and whitespace checks pass. No new guest stream/corpus
qualification or production build is claimed.

Continue with a new structural dataflow/caller hypothesis rather than these
three inlining subsets. The retained linked Note 867 experiment remains
4,704 bytes / 720 over retail; its builder is still 40 public words over its
slot. Changed-combination corpus and entry/context/hardware qualification
remain separate requirements before promotion. Current inventory and the
small bitmap/MMIO candidates are unchanged from Note 868.

Defaults, production sources and README totals remain unchanged. Unrelated
Game changes are neither modified nor staged.
