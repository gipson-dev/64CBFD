# Init Full Masked Shadow Corpus

Date: 2026-10-03. Baseline: `a9e2b68`.

## Result

All 507 retail pages pass the compiled shadow corpus with the explicit
`exception-masked` context, Status `0x2400FF00`, CU1 set, and the
`packed-remaining/o2g3` profile. The test terminates successfully in 709.832
seconds, exit code 0. This closes the full masked corpus gate for that one
profile/mode, not for all six profiles or CU1-clear entry.

Production Init remains unchanged. This is experimental instruction-model
qualification, not a new C owner, complete exception-handler replay, hardware
test, interrupt-pipeline test, or synchronous-fault/reentrancy proof.

## Command And Terminal Receipt

From the `64CBFD` repository root in PowerShell:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_shadow_corpus -v -f
```

```text
shadow corpus context: exception-masked status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 pages=507 text=4896 depth=3256 low=0x80031D58 margin=72
Ran 1 test in 709.832s
OK
```

The task-owned process is terminal. The corpus setup freshly compiles all six
shadow images and then selects the requested image; only the selected image
receives all 507 page comparisons. Compilation of the other images is not
full-corpus qualification of those profiles.

## Coverage And Costs

For every page, the harness checks the expected decompressed output against
the retail image and compares the compiled adapter/core with the retained
retail wrapper/core. Checks include final modeled GPRs, FPR values and known-bit
masks, Status and Status-write traces, FPR save/load addresses, pre-wrapper
f0-f11, base state, physical scratch, changed output/workspace bytes and wrapper
context cells. Input reads remain bounded by the page's rounded DMA span.
The compiled adapter/core must execute instead of the original decoder core.

The protected neighboring retail thread footprint ends at `0x80031D10`.
The minimum observed SP is `0x80031D58`, leaving 72 bytes; the fixture rejects
writes into the protected neighbor. These are private modeled buffers, not
proof of complete runtime storage ownership.

Linked text remains 4,896 bytes, 912 bytes over the 3,984-byte retail group.
Maximum observed stack descent remains 3,256 bytes. No compiler shape,
decoder source, adapter source, default context or production link changed.
The 420 bounded shadow comparisons from Note 826 remain a separate receipt;
the 507 page comparisons here are not added to that bounded-suite count.

## Evidence Boundaries

- Root `make tools-check` and `git diff --check` pass after the documentation
  update. No test implementation changed in this checkpoint.
- [Note 825](825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
  retains its generic-context full corpus receipt, Status `0x2400FF01`.
- [Note 826](826-init-exception-entry-mask-and-masked-context-qualification-20261003.md)
  establishes the original IE/EXL mask prefix and the explicit context selector.
  Its six-profile/both-mode samples are not a full-page corpus.
- This run uses the selector's masked Status; it does not execute the entire
  original exception handler before every page.
- No new production build, full project test suite, hardware run or gameplay
  qualification is claimed. README aggregate tables are unchanged.
- Pending Game changes and sibling repositories are untouched and excluded
  from this checkpoint.

## Next

- [x] Full 507-page masked corpus, packed/remaining O2/g3, CU1 set.
- [ ] Full masked corpus on the other five compiled profiles.
- [ ] Explicit CU1-clear full-corpus selection and qualification; the current
  corpus test is CU1-set only.
- [ ] Complete stack/state/workspace ownership and synchronous-fault bounds.
- [ ] Reduce/fix fitting before changing production ownership.

The next full-corpus profile gate can omit the profile selector to exercise
all six images in the masked CU1-set context. Do not infer those passes from
this one-profile receipt. The small bitmap/MMIO candidates remain separate
matching investigations, not conversions achieved by the decompressor tests.
