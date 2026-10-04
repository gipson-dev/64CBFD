# Init Resume Conversion Readiness Audit

Date: 2026-10-04. Starting HEAD: `c3dbe82b`.

## Decision

Resume Init assessment, not the unfinished Game reset recovery. No remaining
Init assembly replacement is currently ready for production. Two small leaves
are ordinary C candidates; the ten-entry decoder has an experimental semantic
replacement, but fitting and ownership gates still prevent promotion. The
remaining 35 routines are not an independent ordinary-C conversion queue.

This updates [Note 889](889-init-current-assembly-conversion-decision-20261004.md)
with the decoder qualification and startup evidence collected since that audit.
Do not repeat its now-completed frame mapping or corpus steps as new work.

## Fresh Inventory And Ownership

Structured `Import-Csv conker/progress.init.csv` inspection reports:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

All 47 assembly rows were checked against their current source owners.
`init_5AB0` entries remain in `conker/asm/init_5AB0.s`; generated and other
wrapped entries retain `GLOBAL_ASM` source owners. The standalone `bcopy` and
`sqrtf` owners are SDK `.s` files, not missing C files. Inventory filename
labels alone are not filesystem paths or proof of representation.

| Group | Functions | Bytes | Can proceed as ordinary C? |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | Yes, experimentally; complete nineteen-word match still open |
| MMIO `func_100038E0` | 1 | 44 | Yes, with ordered volatile accesses; eleven-word match still open |
| Connected decoder | 10 | 3,984 | As a connected semantic rewrite, not independent leaf replacements |
| Separated SDK assembly | 19 | 2,288 | Retain original assembly provenance and machine contracts |
| Boot entry | 1 | 80 | Retain clear-and-jump assembly |
| Hardware/context/setup | 8 | 4,376 | Requires assembly/intrinsics and connected context proof |
| SDK thread queue leaves | 2 | 96 | Algorithms are C-expressible; retained original SDK assembly |
| Cleanup/debug/glyph | 5 | 1,308 | Recover nonstandard register and interior-entry interfaces first |
| Total | 47 | 12,252 | No newly achieved production conversion |

## Current Decoder Gate

The retained opt-in dynamic-order packed O2 candidate is 4,528 linked
executable bytes against 3,984 retail bytes: **544 bytes too large**.
[Notes 905](905-init-dynamic-order-o2-full-masked-cu1-clear-corpus-20261004.md)
and [906](906-init-dynamic-order-o2-full-masked-cu1-set-corpus-20261004.md)
record 507 paired pages each, covering both masked CU1 modes. Those runs are
prior qualification evidence, not rerun in this audit.

Recorded maximum stack descent is 3,248 bytes, minimum SP `0x80031D60`,
80 bytes above the known neighbor end `0x80031D10`. Neither that margin nor
the write-only live-SP guards prove ownership of the whole private reservation.
[Note 908](908-init-startup-thread-stack-top-and-constructor-contract-20261004.md)
pins startup stack tops and constructor writes, but the later +0x230 thread
context fence still applies. Hardware/context and production entry ownership
remain open. Do not promote solely because the decoder passes its corpus.

## Ordered Work List

- [x] Recount remaining Init assembly and verify source owners.
- [x] Rerun focused bitmap/MMIO, allocation, decoder ledger/storage and startup tests.
- [x] Account for both completed dynamic-order CU1 corpus runs in the decision.
- [ ] For a small exact conversion, develop a new bitmap code-generation hypothesis.
  Preserve the inclusive fill, pointer snapshots, post-fill count reload and
  delay-slot behavior. Note 903's explicit-return shapes emit 21 words, not 19;
  rerunning them unchanged will not resolve the match.
- [ ] Revisit MMIO only with a new explanation for its address lifetime and schedule.
  Preserve address publication, halfword publication, then the halfword MMIO
  store; do not use broad word guards to replace unmatched control/data flow.
- [ ] For the decoder, reduce complete linked executable size by at least 544 bytes
  without regressing ABI, semantic behavior or nested stack bounds. Note 907's
  rejected replication-span loops are not a retained improvement.
- [ ] Requalify any changed decoder candidate, including both full guarded corpora.
- [ ] Prove complete private-stack reservation, entry/frame ownership and required
  hardware/context behavior before switching decoder production ownership.
- [ ] After an achieved conversion, rebuild/link, regenerate progress and compare
  complete Init code/data sections before updating README aggregate tables.

Converting both small leaves would conditionally reach 494 / 539 C functions
(91.65%) and 151,916 / 164,048 C bytes (92.60%), leaving 45 assembly routines /
12,132 bytes. This is a target, not measured progress. A 100% C inventory is
not required to complete recovery of original handwritten SDK/hardware code.

## Fresh Verification

```sh
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract -v -f
```

All 38 tests pass in 3.171 seconds, no skips. These are bounded assembly,
model, storage and startup-contract checks, not hardware/gameplay acceptance.
No full decoder corpus or production rebuild was performed in this audit;
no fresh whole-section or aggregate byte-exact result is claimed.

Production Init sources, profiles, guards and README totals are unchanged.
The unfinished `generated_20AE20.c` Game recovery and unrelated actor/timeline
changes remain untouched. No sibling-port build, Release change or push.
