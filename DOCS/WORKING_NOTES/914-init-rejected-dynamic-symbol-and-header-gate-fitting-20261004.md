# Init Rejected Dynamic Symbol And Header Gate Fitting

Date: 2026-10-04. Starting HEAD: `77938e2b`.

## Result

Two new isolated dynamic-decoder source trials do not improve the complete
packed candidate. Both are removed; `init_decompressor_semantic.c` is restored
exactly to the qualified distance-operation baseline in Notes 911-913.
No selector, production conversion or new candidate survives.

Lookup operation caching was excluded before editing: Note 874 already showed
the retained lookup loads its operation once and reuses it. That is not new
instruction-removal work. The two measured hypotheses below are different.

## Trials

Use the complete packed-remaining configuration from Note 911, with its
distance-operation-local flag enabled and the same IDO O2/g3 and O1 profiles.
These measurements are complete core-object text and static nested core call
bounds, not newly linked adapter footprints or guest execution of rejected code.

1. Move the dynamic code-length symbol read before bit removal:

```c
symbol = ENTRY_VALUE(entry);
drop_bits(s, ENTRY_BITS(entry));
```

The baseline spells those statements in the opposite order. This measures the
symbol's changed lifetime across state updates. It is not retained semantic
equivalence evidence for arbitrary aliased workspace/state objects.

2. Restore the symbol ordering. Replace the dynamic count-validation gate with:

```c
if ((packed & 0x1E) == 0x1E || (packed & 0x3C0) == 0x3C0) return 1;
```

The two five-bit fields reject values 30 and 31. Their upper four bits are
all ones exactly for those two values; the low bit is irrelevant. An exhaustive
host algebra check over all 16,384 possible fourteen-bit headers confirms this
predicate agrees with `literals >= 287 || distances >= 31` after biasing counts
by 257 and 1. This is predicate evidence, not 16,384 MIPS executions or complete
decoder qualification.

## Measurements

Each profile cell is core bytes / dynamic words / dynamic frame / core call bound.

| Form | O2/g3 | O1 |
| --- | --- | --- |
| Qualified baseline | 4336 / 247 / 112 / 400 | 5808 / 313 / 120 / 360 |
| Symbol before drop | 4336 / 245 / 152 / 440 | 5808 / 314 / 120 / 360 |
| Encoded header mask gate | 4352 / 249 / 112 / 400 | 5808 / 315 / 120 / 360 |

The symbol trial saves two public dynamic words but no complete text, and
grows its O2 frame and nested core bound forty bytes. The header gate grows
complete O2 text sixteen bytes and leaves bounds unchanged; O1 complete text
is neutral. Reject both before semantic qualification. Neither is an improvement
to the qualified 4,512-byte linked candidate's 528-byte retail excess.

Ignored receipts, logs and disassembly:

- `conker/build/init-dynamic-symbol-before-drop-baseline-20261004/`
- `conker/build/init-dynamic-symbol-before-drop-trial-20261004/`
- `conker/build/init-dynamic-header-mask-gate-trial-20261004/`

## Restoration And Verification

Scoped `git diff --exit-code -- tools/experiments/init_decompressor_semantic.c`
passes. Restored source SHA-256 matches both qualified corpus runs:
`43A3897FE734E8000F4C156CDB3DB69722D25A210B5B518C02EA315BD71CA0C2`.

```sh
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_backreference_table_storage_is_stable_during_decode tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger -v -f
```

All fifteen tests pass in 5.813 seconds, no skips. They freshly compile the
restored six-image configuration, check packed size/alignment/bounds, execute
the backreference table-stability guard, and validate call-graph/slot accounting.
No discarded-trial guest semantics, full corpus rerun, production link or
hardware execution is claimed. Project tool and whitespace checks pass.

## Next

Continue with a different fitting hypothesis. Do not retry symbol-before-drop
or the encoded header mask gate unchanged. Notes 912/913 remain the unchanged
candidate's full qualification across both masked CU1 modes. Full reservation,
entry/frame ownership, hardware/context and 528-byte fitting gates remain open.

Production Init sources, profiles, guards and README totals are unchanged.
Pending Game/actor/timeline work is preserved and unstaged. No sibling artifact,
Release change or push.
