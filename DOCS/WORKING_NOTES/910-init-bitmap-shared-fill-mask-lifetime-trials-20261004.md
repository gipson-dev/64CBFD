# Init Bitmap Shared Fill/Mask Lifetime Trials

Date: 2026-10-04. Starting HEAD: `c3dbe82b`.

## Hypothesis

Retail `func_10005BE0` reuses `$t0` for the initial 0xFF fill byte and the
two-based final mask. Express that lifetime through one C `int value`, assigned
before the pointer snapshots and reassigned inside the nonzero remainder gate.
Try both the existing separate decrement and an `if (bits--)` condition.

These are isolated scheduling experiments, not changes to the production
assembly owner or a recovered return signature. Retail uses a direct pointer
branch; the existing optimized C trial introduces an XOR temporary.

## Fresh Measurements

`tools/experiments/init_bitmap_ordered.c` now retains shapes 6 and 7.
The driver compiles all seven shapes under IDO O2/g3 and O1, links at the
retail address with absolute globals, and compares through the return delay
slot against the complete nineteen-word ROM slot.

| Shape | O2/g3 words / differing positions | O1 words / differing positions |
| --- | ---: | ---: |
| 1, existing control | 20 / 19 | 31 / 31 |
| 6, shared fill/mask value | 20 / 19 | 37 / 37 |
| 7, shared value and postdecrement condition | 22 / 21 | 38 / 38 |

No shape matches. Shape 6's complete extracted O2 `.text` is byte-identical
to shape 1, SHA-256
`8eee6750d14b442c7fbd1482dd70cfd40a2406bb25e9d5bec27e5970f90f9b7a`.
IDO splits the source variable's lifetimes into the same separate registers;
the XOR loop and advanced-cursor delay-slot store remain. Shape 7 adds two
tail moves rather than reproducing retail's nineteen-word schedule.

## Qualification

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries -v -f
```

All seven warning-clean host executables pass 79 fixture cases each, 553
shape/case combinations; the two new forms contribute 158 combinations.
Fixtures include signed/zero count cases with explicitly valid endpoints,
repeat filling, surrounding bytes, count aliasing and endpoint-cell aliasing.
Return assertions remain restricted to shapes 4/5; shapes 6/7 are void.
These host fixtures do not establish guest instruction-order equivalence,
invalid-endpoint termination, hardware behavior or production suitability.

All 33 retained-contract tests pass in 2.395 seconds, no skips.
Measurements/disassembly remain under ignored `conker/build/init-bitmap-ordered/`.

## Decision

Retain the reproducible experiments but reject both forms as production
replacements. Do not retry shared source-variable lifetime alone: it does not
constrain IDO register allocation or eliminate the loop XOR. A future matching
attempt needs a different code-generation explanation, not broad word guards.

No production Init code, profiles, word guards, declarations, README totals,
decoder candidate, sibling artifacts or Release changed. Pending Game source
and actor/timeline work remain untouched.
