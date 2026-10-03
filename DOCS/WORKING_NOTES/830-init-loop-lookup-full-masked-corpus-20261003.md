# Init Loop Lookup Full Masked Corpus

Date: 2026-10-03. Baseline: `936f969`.

## Result

All 507 retail pages pass the new `--loop-lookup` shadow variant with masked
Status `0x2400FF00`, CU1 set, and packed/remaining O2/g3. The task-owned process
terminates successfully in 759.786 seconds, exit code 0. Linked text is 4,880
bytes; observed maximum descent is 3,256 bytes, lowest SP 0x80031D58, neighbor
clearance 72 bytes.

This closes the changed-source full masked corpus gate for that profile/mode.
The other five profiles and CU1-clear full corpus remain open. Production
Init assembly, default compiler shapes, README totals and pending Game work
are unchanged. No sibling repository or frozen release artifact was touched.

## Exact Command And Receipt

From the `64CBFD` repository root in PowerShell:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_loop_lookup.InitDecompressorLoopLookupCorpusTests -v -f
```

```text
shadow corpus context: exception-masked status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 pages=507 text=4880 depth=3256 low=0x80031D58 margin=72
Ran 1 test in 759.786s
OK
```

The explicitly named corpus subclass supplies `--loop-lookup` through the
shadow fixture's optional compile flags. Setup freshly compiles all six
variant images, then selects packed/remaining O2 for the page loop. Building
the other five images is not full-corpus execution of those profiles.
No source or harness edits were made while the run was live.

## Qualification Scope

Each page is decoded through the compiled adapter/core and compared with the
retained original wrapper/core. Checks cover output against the retail image,
modeled GPRs and FPR values/known-bit masks, Status traces, FPR save/load
addresses, pre-wrapper scratch FPRs, base state, physical scratch,
output/workspace changes and wrapper context cells. The compiled entry must
execute instead of the original decoder core. Input reads remain within each
rounded DMA span and the corrected neighboring-thread guard stays enabled.

The known neighboring retail thread footprint ends at 0x80031D10. Its
non-overlap with the lowest tested SP is not proof of complete storage
ownership. The input/output/workspace and stack are private modeled buffers.
The fixture models FR=1 architectural values; it is not a hardware pipeline,
cache/DMA timing model, complete exception-handler replay or synchronous-fault
reentrancy proof.

The loop variant saves 16 linked text bytes against the old packed O2 profile,
but remains 896 bytes larger than the 3,984-byte retail group. Stack costs are
unchanged. Elapsed wall time is a receipt, not a controlled speed comparison.

## Separate Historical Receipts

- [Note 829](829-init-shared-lookup-loop-fitting-and-context-qualification-20261003.md)
  retains the 420 bounded context comparisons across six profiles/both CU1 modes
  and its explicit nested-path probe. The 507 page comparisons here are separate,
  not added to that bounded-suite count. Its 29 passing tests are not rerun here.
- [Note 827](827-init-full-masked-shadow-corpus-20261003.md) remains the full
  masked 507-page pass for the old default lookup shape at 4,896 bytes.
- [Note 825](825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
  remains the corrected-boundary generic-context pass, Status 0x2400FF01.

No receipt is relabeled to another source/context/profile. No new production
build, complete project suite, hardware test or gameplay qualification is claimed.
Root `make tools-check` and `git diff --check` pass after the documentation update.

## Next

- [x] Full masked 507-page corpus on loop-lookup packed O2/g3, CU1 set.
- [ ] Full masked corpus on remaining loop-lookup profiles. Omit the profile
  selector in the command above to run all six images, not merely compile them.
- [ ] Explicit CU1-clear corpus selection and full-page qualification; the
  current corpus entry is CU1-set only.
- [ ] Complete original stack/state/workspace ownership and synchronous-fault bounds.
- [ ] Continue builder/helper/adapter fitting; the 896-byte excess still blocks
  production replacement alongside the independent interface/ownership gates.
