# Init Bitmap Unsigned Range Comparison Trials

Date: 2026-10-04. Production baseline: `ec2bf64f`.

## Hypothesis And Scope

The equality/postincrement control emits XOR to preserve the old cursor's
comparison across its increment. Two new isolated shapes test whether a
valid-buffer unsigned range comparison removes that extra instruction:

- Shape 10: store, then compare the old cursor address with end using `<`
  while postincrementing the cursor.
- Shape 11: store/postincrement, then compare the new cursor address with
  end using `<=`.

Both cast to unsigned long before comparison, avoiding relational comparison
of unrelated C pointers. Qualification is restricted to valid, ascending,
nonwrapping intervals with valid pointer increments. Neither shape preserves
retail's invalid/reversed/wrapping endpoint behavior, and neither is a proposed
production replacement on the strength of the bounded host fixtures alone.

## Measurements

| Shape | O2/g3 words / differences | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 1, equality control | 20 / 19 | 20 / 19 | 31 / 31 |
| 10, old cursor unsigned `<` | 20 / 19 | 20 / 19 | 30 / 30 |
| 11, advanced cursor unsigned `<=` | 20 / 19 | 20 / 19 | 32 / 32 |

Retail has nineteen words. Difference counts are aligned instruction-position
comparisons, not semantic discrepancy counts. Both new O2 shapes still need
an `sltu` followed by a conditional branch; the store stays in the branch
delay slot at cursor minus one. Retail instead stores first, branches directly
on cursor/end equality and increments in the delay slot. Range comparison
changes the predicate instruction but does not resolve length or scheduling.

## Verification And Decision

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries -q -f
```

All eleven warning-clean host executables pass 79 fixtures each: 869
shape/case combinations, 158 added by the two new forms. Count-cell and
endpoint-cell aliasing, boundary counts, surrounding bytes and repeat fills
remain covered. New forms do not assert a return value. All 33 retained
contract tests pass in 1.999 seconds, no skips.

Reject both as production replacements. Do not repeat unsigned range
predicates unchanged. Further bitmap matching needs an explanation for the
direct endpoint branch, retail store/increment schedule and register
allocation, not merely a different predicate. The observed valid-buffer
equivalence does not justify weakening the full retail endpoint contract.

Reproducible source/driver changes remain under `tools/experiments/`;
measurements and disassembly are in ignored `conker/build/init-bitmap-ordered/`.
Production Init source, profiles and word guards are unchanged. Init remains
492 C / 47 assembly routines. Decoder's 528-byte fitting deficit and ownership
gates remain unchanged. No README aggregate change, sibling build or push.
