# Init Explicit Corpus CU1 Modes And Clear Full Pass

Date: 2026-10-03. Baseline: `6d82e07`.

## Result

The corpus now accepts explicit CU1 entry modes. A real masked CU1-clear run
passes all 507 pages on loop-lookup packed/remaining O2/g3 in 741.930 seconds,
exit code 0. Text/descent remains 4,880/3,256, lowest SP 0x80031D58, known
neighbor clearance 72 bytes. Together with Note 830's separate CU1-set pass,
this qualifies both entry modes over all pages for that one variant/profile.

No decoder/adapter implementation, production owner, default compiler shape
or README aggregate changes. The 896-byte text excess, complete storage/fault
ownership and other full-corpus profiles remain open. Game changes and sibling
repositories remain untouched.

## Explicit Selection

`CONKER_INIT_SHADOW_CORPUS_CU1` accepts:

- `set` (default): execute CU1-set entry only.
- `clear`: execute CU1-clear entry only.
- `both`: execute all pages with CU1 clear, then all pages with CU1 set.

Unknown selections fail before compilation. The context selector remains
independent: generic Status is 0x2400FF01/0x0400FF01, exception-masked Status
is 0x2400FF00/0x0400FF00 for set/clear respectively. `context_status` retains
CU1 set as its default argument and rejects nonsingle modes such as `both`;
the selection helper expands `both` explicitly.

Defaults remain generic context, CU1 set, and all six images unless a profile
selector is supplied. Existing module/class commands remain valid. The test
method is renamed to `test_all_507_retail_pages_selected_cu1_modes` to avoid
claiming CU1 set when another mode is selected.

Each mode resets measured maximum depths, reports its own Status, progress,
profile costs and terminal receipt. The final total must equal
507 * selected-profile-count * selected-mode-count. No mode can silently
reuse another mode's accumulated stack maximum.

## Real CU1-Clear Command And Receipt

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_loop_lookup.InitDecompressorLoopLookupCorpusTests -v -f
```

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4880 depth=3256 low=0x80031D58 margin=72
shadow corpus complete: modes=clear runs=507
Ran 1 test in 741.930s
OK
```

Setup freshly compiles six loop variants, but only the selected image executes
all pages. The retained wrapper's CU1 enable/save/restore path is compared with
the compiled adapter/core. Existing complete modeled register/FPR context,
Status traces, scratch/workspace/output, rounded DMA span and protected-neighbor
checks remain active. No source/harness edits occur while the run is live.

## Selector And Regression Tests

- Nine tests in the selection/mask modules pass in 51.027 seconds. This includes
  the existing original Status-prefix/route checks and 72 default-source
  masked guest sample comparisons using the new single-mode status helper.
- Pure selection tests cover all four Status values, mode expansion/defaults,
  and rejection. Invalid environment choices are proven to fail before the
  stubbed compiler setup is called.
- Synthetic orchestration tests dispatch 507 mock pages through both contexts
  and all three mode choices with six fake images. They check argument/status
  forwarding, exact mode counts, depth resets and labeled terminal output.
  These mocks do not execute MIPS and are not guest/corpus qualification.
- Ordinary default and loop-lookup corpus class discovery still skips both
  tests unless explicitly enabled. No unwanted long test starts.
- The real CU1-clear corpus above is a separate one-test execution receipt.
- Root `make tools-check`, three Python syntax checks and `git diff --check` pass.

The unchanged decoder source means [Note 830](830-init-loop-lookup-full-masked-corpus-20261003.md)
still supplies the separate masked CU1-set full corpus receipt. A real single
invocation of `both` is not claimed; its dispatch has synthetic coverage and
each mode has its own real one-profile receipt. Neither is full qualification
of the other five profiles. [Note 829](829-init-shared-lookup-loop-fitting-and-context-qualification-20261003.md)
retains its bounded 420-comparison receipt, not rerun or expanded here.

No new production build, full project suite, FR=0/hardware/pipeline/cache test
or gameplay qualification is claimed. Private buffers and non-overlap do not
establish complete allocation ownership or synchronous-fault reentrancy.
Elapsed time is not a controlled speed comparison.

## Next

- [x] Explicit CU1 set/clear/both selection with independent mode receipts.
- [x] Real full masked corpus, loop-lookup packed O2, CU1 clear.
- [x] Both entry modes qualified in separate full-page runs for that profile.
- [ ] Remaining five loop-lookup profiles, both entry modes. Use `both` and
  omit the profile selector to exercise all six images (6,084 comparisons).
- [ ] Complete storage ownership and synchronous-fault bounds.
- [ ] Further builder/helper/adapter fitting; 896 bytes remain over retail.

The default-source corpus class also accepts these selectors, but has no new
CU1-clear full-page receipt from this run. Keep source/profile identity explicit.
