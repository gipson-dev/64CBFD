# Init Remaining Assembly Readiness Refresh

Date: 2026-10-04. Starting HEAD: `ec2bf64f`.

## Decision

Resume the requested Init assessment, not the adjacent Game emitter helper.
Some remaining assembly can be expressed in C, but no remaining replacement
is currently qualified for production. Keep retail assembly ownership until
the relevant matching, ABI, storage and hardware gates are satisfied.

Current structured `conker/progress.init.csv` inventory:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

## Conversion Groups

| Group | Functions | Bytes | Next decision |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | Best small ordinary-C target; nineteen-word match remains open |
| MMIO `func_100038E0` | 1 | 44 | C-expressible ordered accesses; eleven-word match remains open |
| Connected decoder | 10 | 3,984 | Experimental semantic C; fitting and ownership gates remain |
| Separated SDK assembly | 19 | 2,288 | Retain original machine-level implementations |
| Boot `func_10001000` | 1 | 80 | Retain clear-and-jump assembly |
| Hardware/context/setup | 8 | 4,376 | Connected ABI and hardware proof required, not pure-C substitution |
| SDK thread queue leaves | 2 | 96 | C-expressible algorithms, retained original assembly provenance |
| Cleanup/debug/glyph | 5 | 1,308 | Recover interior-entry and live-register contracts first |
| Total | 47 | 12,252 | No newly achieved production conversion |

The complete grouping/ownership background remains in
[Note 909](909-init-resume-conversion-readiness-audit-20261004.md).
Its decoder deficit of 544 bytes is superseded by the qualified candidate
in Notes 911-913: **4,512 linked bytes versus 3,984 retail, 528 bytes excess**.

## What Changed Since The Earlier Assessment

- [Note 918](918-init-bitmap-store-qualifier-and-sentinel-trials-20261004.md)
  rejects nonvolatile byte stores and end-plus-one sentinel shapes. The former
  still emits twenty words; the latter emits thirty-three, or twenty with
  unrolling disabled. None fits and matches all nineteen retail words.
- [Note 912](912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md)
  and [Note 913](913-init-distance-operation-o2-full-masked-cu1-set-corpus-20261004.md)
  record 507 paired decoder pages per masked CU1 mode. Those are prior
  candidate-specific receipts, not corpus reruns during this assessment.
- Full private-stack reservation, production entry/frame ownership and
  required hardware/context behavior are still unresolved. The 80-byte
  measured neighbor margin is not proof of allocation ownership.

## Ordered Next Steps

- [x] Recount the current Init CSV and review the latest conversion receipts.
- [x] Rerun the six focused contract suites: 38 tests pass, no skips.
- [ ] For `func_10005BE0`, develop a new compiler-shape explanation for the
  direct inclusive endpoint branch and increment delay slot. Preserve pointer
  snapshots and the post-fill count reload, including alias behavior. Do not
  repeat the rejected qualifier, sentinel or explicit-return trials unchanged.
- [ ] Compile and compare a new bitmap trial independently before changing
  the production owner. Require the complete nineteen-word slot and contract
  tests; do not replace broad unmatched flow with instruction guards.
- [ ] Revisit `func_100038E0` only with a new address-lifetime/scheduling
  hypothesis. Preserve address publication, halfword publication, then MMIO
  halfword store; host store tracing is not hardware acceptance.
- [ ] For the connected decoder, remove at least 528 linked executable bytes
  while preserving behavior, ABI and nested stack bounds. Requalify changed
  source/layout in both full guarded corpora.
- [ ] Prove complete reservation, entry/frame ownership and hardware/context
  requirements before decoder production adoption.
- [ ] After an actual conversion, rebuild/link, regenerate progress and
  compare full Init code/data before changing README aggregate tables.

Both small leaves together would conditionally reach 494 / 539 C functions
and 151,916 C bytes, leaving 45 assembly routines / 12,132 bytes. That is a
target, not achieved progress. Finishing Init does not require rewriting
original handwritten SDK or hardware assembly into artificial C.

## Fresh Verification And Scope

```sh
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract -v -f
```

All 38 tests pass in 2.246 seconds, no skips. These are bounded assembly,
model, allocation, decoder-storage and startup checks, not whole-game or
hardware acceptance. No full decoder corpus was rerun here.

The initial default `make -C conker progress` hit the whole-ROM checksum
gate because the current project contains non-matching Game bodies. Use
`make -C conker NON_MATCHING=1 progress` for this checkout; the checksum
failure alone does not establish an Init regression.

Production Init/Game source, compiler profiles, word guards and README
aggregate tables remain unchanged. Detailed updates stay in working docs.
No sibling-port build, Release change or push.
