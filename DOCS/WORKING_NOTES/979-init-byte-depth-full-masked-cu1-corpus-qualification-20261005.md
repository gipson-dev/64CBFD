# Init Byte-Depth Full Masked CU1 Corpus Qualification

Date: 2026-10-05. Starting HEAD: `5238ece0`.

## Scope

Continue connected Init qualification after
[Note 978](978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md).
The current lead is Note 975's opt-in byte-depth builder, packed-remaining
O2/g3, distance-operation capture, pointer-owned core and actual 176-byte adapter.
Its bounded suite was qualified previously, but the full masked corpus was
still open. Earlier distance-operation corpora used the index-depth candidate
and do not qualify the changed byte-depth image.

The new dedicated opt-in entry point is
`tools/tests/test_init_decompressor_builder_byte_level_corpus.py`.
It inherits the established full corpus, guards and comparison engine, selects
exactly packed-remaining/O2/g3, requires exception-masked context and pins the
compiled object's complete instruction SHA-256 before page execution.
The ordinary bounded byte-depth module remains separate and unchanged.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=both CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level_corpus -v -f
```

Setup freshly compiles all six connected images, then chooses the single
specified candidate. It verifies 4320 C text bytes plus 176 adapter bytes =
4496 executable bytes, compared with 3984 retail. The complete object hash is:

```text
dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a
```

The read-only ROM and decompressed-image references are checksum-validated by
the established retail-page setup. Each rounded DMA input is paired with
retail execution and the pristine image's corresponding output page.
Compiled adapter/core visits are required; the original retail core is not
used as a fallback for the candidate execution.

## Result

**Both full masked CU1 modes pass: 507/507 pages each, 1014 paired runs.
The single full-corpus test completes in 1604.214 seconds with exit zero,
no failures and no skips.** Both terminal measurements report 4496 executable
bytes, 3248-byte stack descent, low address `0x80031D60` and 80-byte clearance
above the known neighbor ending at `0x80031D10`.

The terminal receipt has `complete: true`, counts 507/507 and
`source_hashes_unchanged: true` for all eight monitored files. The object hash
and complete allocation match the banked candidate. The stack-descent receipt
field records the final CU1-set mode; the terminal output independently records
the same bound for CU1-clear. This closes the candidate-specific full masked
corpus gate, not fitting, placement, reservation or hardware acceptance.

## What Is Compared

- All 507 retail pages under masked CU1-clear Status `0x0400FF00`.
- The same 507 pages under masked CU1-set Status `0x2400FF00`.
- Return result, decoded output and original scratch-frame contents.
- Complete final GPR/FPR state, FPR transfer footprints and Status writes.
- Changed workspace/output cells and saved-context storage.
- Input reads within each DMA-rounded transfer.
- Static direct-call stack bounds and known-neighbor clearance.
- Active callee-preservation, live-SP write and input/fifth-slot initialization guards.

These are guarded guest/model comparisons, not hardware interrupt timing,
asynchronous faults, arbitrary aliases, original entry/slot placement or
private-stack reservation ownership. The live-SP guard fences writes, not
all possible below-SP reads. Known-neighbor clearance does not establish
exclusive ownership of the intervening BSS interval.

## Supporting Checks

Thirty-two fast checks pass in 1.483 seconds, no skips. They include five new
candidate-setup/reporting tests plus existing corpus selection, inventory, slot ledger,
call graph and startup-thread tests. The new orchestration tests explicitly
reject generic context, wrong/multiple profile selections before object access,
and a wrong compiled instruction hash. They confirm the byte-depth flag and
pointer-owned/live-SP guarded fixture are inherited.

After the full failfast run and receipt verification, harden reporting only:
count successful comparisons and reject a failed unittest outcome before
setting the completion marker. Two mocked success/failure controls qualify
these gates. A collected subtest failure in a non-failfast run can no longer
produce a successful completion marker. These controls are reporting tests,
not additional MIPS execution evidence.

The full run's eight before/after hashes describe the files during that run.
The corpus reporter itself is subsequently edited for these failure gates;
its final source hash therefore differs from the full-run receipt. Candidate
C, adapter, flags and comparison/guard engine remain unchanged. The 1014-run
corpus is not repeated for this reporting-only change; the subsequent 32-test
suite checks the final reporter plus the existing production audits.

The startup checks retain their earlier boundary: they prove published thread
stack tops and context writes, not ownership of the entire decoder gap. No
additional reservation is inferred from those stack tops or untouched bytes.

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level_corpus_selection tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_startup_thread_contract -q -f
make tools-check
```

The new full-run receipt records paired counts, selected Status values,
complete sizes, instruction hash, terminal stack descent and eight before/
after source/adapter/guard hashes. It lives under ignored
`conker/build/init-byte-depth-corpus-20261005/exception-masked-clear-set/qualification.json`.
Candidate C, adapter, compiler options and production owners are unchanged.

## Remaining Gates

- [x] Finish both 507-page masked CU1 modes and verify terminal receipts.
- [x] Pin candidate selection, instruction hash and complete allocation.
- [x] Add selection/reporting rejection controls and pass thirty-two supporting checks.
- [ ] Remove another 512 complete executable bytes before placement.
- [ ] Prove private-stack reservation and original entry/frame/placement ownership.
- [ ] Qualify remaining hardware/context behavior before adoption.

No production conversion, relink, README aggregate, sibling source/build,
frozen Release, saves, ROM promotion or push is included. Init remains
492 C / 47 ASM entries; this corpus closes one candidate-specific gate,
not Init or the broader decomp goal. Next connected work is a new whole-image
fitting hypothesis to remove 512 bytes, then original entry/frame/placement
and private-stack ownership proof. Any changed candidate needs fresh qualification.
