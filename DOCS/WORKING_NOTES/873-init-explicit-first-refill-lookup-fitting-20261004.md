# Init Explicit First Refill Lookup Fitting

Date: 2026-10-04. Baseline: `f965d456`.

## Result

Opt-in `--lookup-first-refill` removes the per-iteration null-entry selector
from the shared lookup helper. Packed O2/O1 core text each falls sixteen
bytes, with unchanged whole-core call bounds. The original shared-loop and
two-path lookup defaults remain unchanged; production ownership is untouched.
This is isolated fitting, not a production conversion or full changed corpus.

## Dataflow

The option requires `--loop-lookup` and selects
INIT_DECODE_LOOKUP_FIRST_REFILL inside that branch:

```c
InitDecodeEntry *entry;
need_bits(s, width);
for (;;) {
    entry = &s->workspace[root + (s->reservoir & low_mask(width))];
    if (ENTRY_OPERATION(entry) <= 16 || ENTRY_OPERATION(entry) == 99) return entry;
    width = ENTRY_OPERATION(entry) - 16;
    drop_bits(s, ENTRY_BITS(entry));
    need_bits(s, width);
    root = ENTRY_VALUE(entry);
}
```

Both paths begin with the same refill and root dispatch. For a child, both
read its operation, select width, drop its entry bits, refill, then read its
value for the next masked table index. The child value is deliberately not
captured before refill. low_mask remains a pure modulo-32 expression; no
operation classification, state update, refill, malformed correction or
workspace caching is changed. The new root local replaces the old null/non-null
selector, not the root passed to callers or a persistent state field.

The CLI rejects the option without the shared loop before compilation. A new
test subclass selects it on the complete allocation-table configuration and
inherits the bounded context/builder/header/repeat/stack guards. A separate
corpus class is available for later full qualification.

## Costs

| Packed profile | Core before / after | Core bound | Lookup words before / after | Lookup frame before / after |
| --- | ---: | ---: | ---: | ---: |
| O2 g3 | 4,400 / 4,384 | 392 | 50 / 46 | 48 / 48 |
| O1 | 5,840 / 5,824 | 352 | 48 / 45 | 40 / 32 |

Public builder bodies/frames remain 333/200 O2 and 496/120 O1. The O2
builder region is now 333 + 22 ABI-capture + 46 lookup = 401 words. Reducing
the embedded lookup does not change the public builder's forty-word excess.
Packed linked O2 is 4,688 bytes, 704 over retail's 3,984-byte group.

Initial direct-source receipt is
`conker/build/init-lookup-explicit-first-refill-20261004`. The initial guest
run passes 33 tests / one intentional corpus skip in 247.203 seconds. The
source guard wiring is then verified and the final opt-in source freshly
recompiled by a second whole guest run; its final result is recorded below.
The initial run is not substituted for that final qualification.

## Final Verification

The final opt-in source freshly compiles/links six shapes and passes 34 tests
in 241.971 seconds: 33 passes, one intentional opt-in full-corpus skip.
Allocation order, parent-root descent, initializer poison, neighboring-thread
red zone, repeat/overflow, stored complement, header alignment, both CU1
context modes and representative retail pages pass. The nested-lookup gate
still fires on page 169 with 3,212 calls / 3,383 iterations.

| Shape / profile | Linked bytes before / after | Total static / observed descent |
| --- | ---: | ---: |
| Frame / O2 g3 | 5,840 / 5,824 | 3,272 / 3,272 |
| Frame / O1 | 6,336 / 6,336 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,736 / 4,720 | 3,232 / 3,232 |
| Aligned end / O1 | 6,128 / 6,128 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,704 / 4,688 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,144 / 6,128 | 3,200 / 3,200 |

All static bounds hold, including the inherited aligned-profile costs.
Packed O2 minimum SP remains 0x80031D68 with known-neighbor margin 88;
this is not complete reservation/hardware proof. Sixteen supporting
call-graph/ledger/selection and omitted-option size tests pass in 2.027s,
no skips. Final combined count is 49 passes / one skip, excluding the initial
trial run. Project tool and whitespace checks pass. No production build,
full changed corpus, hardware replay or sibling-port test is claimed.

An omitted-option compile at
`conker/build/init-first-refill-omitted-option-20261004` reproduces both
O2/O1 .text sections byte-for-byte against the retained Note 868 baseline
objects, verified with GNU objcopy and cmp. This proves only text identity,
not entire ELF or production ROM equivalence.

## Next

- [x] Finish final opt-in bounded guest qualification.
- [ ] Qualify the changed combination's full masked CU1-clear corpus.
- [ ] Qualify the changed combination's full masked CU1-set corpus.
- [ ] Continue size fitting, entry ownership and hardware/context qualification.

Notes 871/872's 1,014 paired pages remain qualification for the omitted-option
baseline only. Production sources, defaults, progress CSV and README counts
remain unchanged; unrelated dirty Game work is preserved and not staged.
