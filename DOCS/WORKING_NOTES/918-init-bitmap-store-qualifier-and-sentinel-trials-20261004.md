# Init Bitmap Store Qualifier And Sentinel Trials

Date: 2026-10-04. Starting HEAD: `3321e2d2`.

## Hypotheses

Retail `func_10005BE0` fills through an inclusive end pointer with a direct
pointer branch and increment delay slot. Existing postincrement C introduces
an XOR; the break-based form introduces an extra branch. Two new isolated
shapes in `tools/experiments/init_bitmap_ordered.c` test different causes:

- Shape 8 removes volatile from byte-pointer accesses, retaining pointer
  snapshots and the post-fill count read. This tests whether volatile inhibits
  the required compiler schedule; it is not a production memory-contract change.
- Shape 9 snapshots `end + 1` as the stopping pointer, then compares the
  already advanced cursor directly. This requires a valid one-past endpoint;
  equivalence is not asserted for invalid endpoints or pointer wraparound.

The driver now also measures O2/g3 with `-Wo,-loopunroll,0` for every shape.
No guards, production profiles or assembly owners are changed.

## Measurements

| Shape | O2/g3 words / differences | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 1, control | 20 / 19 | 20 / 19 | 31 / 31 |
| 8, nonvolatile byte stores | 20 / 19 | 20 / 19 | 31 / 31 |
| 9, end-plus-one sentinel | 33 / 33 | 20 / 20 | 33 / 32 |

Difference counts compare instruction positions through the return delay slot
against all nineteen retail words; they are not semantic mismatch counts.
No profile of any of the nine retained shapes matches the complete slot.

The sentinel enables loop unrolling under ordinary O2. Disassembly shows a
remainder loop and four-byte unrolled loop. Disabling unrolling restores a
short direct-comparison loop but retains sentinel preparation and the wrong
store/increment schedule. Removing volatile alone does not remove the extra
word. Neither hypothesis resolves the production conversion.

## Qualification And Decision

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries -v -f
```

All nine warning-clean host executables pass 79 fixtures each: 711 shape/case
combinations, including 158 contributed by the two new forms. Count aliasing,
endpoint-cell aliasing, surrounding bytes and repeated filling are covered.
Only shapes 4/5 assert return values; new shapes remain void.
All 33 retained-contract tests pass in 2.025 seconds, no skips.

The host fixtures establish bounded behavior for their valid endpoints, not
guest instruction ordering, arbitrary pointer provenance, invalid termination,
concurrency or hardware. The assembly tests continue verifying the retained
retail owner; they do not qualify the trial C as a replacement.

Retain the reproducible experiments, reject both as production replacements.
Do not repeat qualifier removal or sentinel preparation unchanged. A future
attempt needs an explanation for both the direct original-pointer branch and
retail register/scheduling allocation, without broad instruction replacement.

Init remains 492 C / 47 assembly functions. Decoder candidate and its remaining
528-byte fitting deficit and ownership gates are untouched. README aggregates
are unchanged. Unrelated actor/timeline work is preserved and excluded; no
sibling source import, host build, Release change or push is needed for rejected
standalone compiler trials. Artifacts stay in ignored `conker/build/init-bitmap-ordered/`.
