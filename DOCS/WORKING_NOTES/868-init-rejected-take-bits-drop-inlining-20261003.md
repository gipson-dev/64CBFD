# Init Rejected Take Bits Drop Inlining

Date: 2026-10-03. Baseline: `8a0b6e6f` (Note 867).

## Result

Inlining only `drop_bits` inside the default `take_bits` path grows both
packed compiler outputs. The trial is removed; the experiment source is
restored exactly to HEAD. No production conversion or new option survives.

This differs from the earlier broad flattened-bit trial: refill and mask
calculation remain helper calls, and only the two drop statements are copied:

```c
need_bits(s, width);
value = s->reservoir & low_mask(width);
s->reservoir >>= width & 31;
s->bits -= width;
```

Modulo-32 shift handling is retained. The standalone drop helper remains
necessary for other callers, so this does not remove its text.

## Measurements

Complete Note 867 packed-remaining configuration, including table-derived
allocation; these are core-only object measurements, not fresh linked runs:

| Form | O2 g3 core bytes / call bound | O1 core bytes / call bound |
| --- | ---: | ---: |
| Retained baseline, freshly recompiled | 4,400 / 392 | 5,840 / 352 |
| Inline drop inside take_bits | 4,416 / 392 | 5,872 / 352 |

Trial take_bits is 24 words / 24-byte frame under O2 and 28 words /
32-byte frame under O1. Its smaller local frame does not improve the
whole-core nested call bound. Trial compiler logs are empty.

Ignored receipts:

- `conker/build/init-take-inline-drop-20261003`
- `conker/build/init-take-drop-restored-20261003`

After restoration, `git diff --exit-code` for the experiment source passes.
Fourteen call-graph, slot-ledger and parent-cursor size tests pass in 1.898s.
No guest stream suite, full corpus, production ROM build or hardware run
is claimed in this checkpoint. Earlier corpus results do not qualify the
changed Note 867 option combination.

## Remaining Init Decision

Fresh structured progress-file inspection still reports 492 C functions /
151,796 bytes and 47 assembly functions / 12,252 bytes (539 / 164,048 total).
This is current inventory, not a fresh production byte-match measurement.

The two small ordinary-C candidates remain `func_10005BE0` (76-byte bitmap)
and `func_100038E0` (44-byte MMIO). Their characterized contracts are known,
but no complete nineteen-word or eleven-word matching C replacement exists.
Do not repeat the already rejected bitmap/profile and partial-volatility
matrices unchanged. See [Note 792](792-init-resume-remaining-assembly-conversion-decision-20261003.md).

Ten assembly rows belong to the 3,984-byte connected decompressor. The
retained Note 867 packed O2 linked experiment is 4,704 bytes, 720 over budget;
its public builder is 333 words against a 293-word retail slot. Continue
structural fitting only with a new hypothesis, then qualify the changed
combination's corpus, entry ownership and hardware/context boundaries before
production promotion. The other 35 rows have SDK, hardware, boot, context or
nonstandard debug/glyph contracts and should not be forced into ordinary C.

Production sources, README totals and defaults remain unchanged. Unrelated
dirty Game source and tests are preserved and excluded from this checkpoint.
