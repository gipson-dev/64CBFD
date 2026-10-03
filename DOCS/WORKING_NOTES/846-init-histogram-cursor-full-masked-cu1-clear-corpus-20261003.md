# Init Histogram Cursor Full Masked CU1-Clear Corpus

Date: 2026-10-03. Source baseline: `ee39f1da`; experimental source remains
the histogram variant committed in `59e910e3`.

## Result

All 507 retail Game pages pass the changed histogram-cursor decoder's
packed/remaining O2/g3 corpus with exception-masked entry and CU1 clear.
The terminal process exits zero: one opt-in test passes in 768.820 seconds,
with no skips or failures. This closes the independent CU1-clear gate from
[Note 845](845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md).

Together, Notes 845/846 provide 1,014 paired page comparisons for the changed
packed O2/g3 source across masked CU1-set and CU1-clear contexts. They do not
qualify other profiles, generic contexts or actual hardware behavior.

## Command And Terminal Receipt

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor.InitDecompressorHistogramCursorCorpusTests -v -f
```

The live checkout and corpus subclass were inspected before launching. The
subclass explicitly compiles `--loop-lookup` and `--builder-histogram-cursor`;
the selected entry Status is printed as `0x0400FF00`. Setup freshly compiles
and links six images before selecting the single requested packed O2/g3
profile. No source or adapter edits occurred during the run.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4864 depth=3256 low=0x80031D58 margin=72
shadow corpus complete: modes=clear runs=507
Ran 1 test in 768.820s
OK
```

Linked text is 4,864 bytes. Maximum observed descent is 3,256 bytes, minimum
SP `0x80031D58`, with 72 bytes above the protected neighbor ending at
`0x80031D10`. These agree with Note 845; the extra CU1-clear context does not
increase the measured bound in this corpus.

## Scope And Remaining Fitting

The inherited comparison checks page supply/pristine output, retail and
changed guest results, GPR/FPR state and scratch snapshots, modeled Status
writes, wrapper FPR save/restore behavior, physical scratch and changed
output/workspace bytes. Rounded input read bounds, entry visits, stack
bounds and the protected-neighbor write fence remain active. CU1-clear
exercises the wrapper save/restore path independently of Note 845.

The full corpus contains successful retail pages, not all malformed inputs.
Keep Note 844's bounded error and direct-builder receipts separately. Real
DMA/cache/TLB, asynchronous faults, scheduler resume, gameplay and complete
reservation ownership remain outside these deterministic instruction models.

A read-only inspection of the existing packed O2 size receipt separates the
remaining 880-byte excess into 560 bytes of core excess and the 320-byte
adapter: 4,544 + 320 versus 3,984 retail bytes. Builder public unit is 345
words versus its retail 293; its 417-word enclosing slot also contains the
22-word ABI capture and 50-word lookup helpers. That slot must not be
mistaken for 417 builder-body words. This is size accounting, not evidence
that individual retail entries can be replaced independently.

Root `make tools-check` and `git diff --check` pass. No production build,
ordinary full-suite rerun, hardware replay or sibling-port test is claimed.

## Next

- [x] Changed packed O2/g3 full masked CU1-set corpus: Note 845.
- [x] Changed packed O2/g3 full masked CU1-clear corpus: this note.
- [ ] Return to builder/shared-helper/adapter fitting; 880 linked bytes remain.
- [ ] Full-corpus qualification for the other five shapes/profiles.
- [ ] Complete outstanding reservation/hardware/resume qualification before promotion.

Prefer a scoped builder dataflow or shared-helper layout hypothesis next;
retain measured variants only after size and bounded-contract checks. Do not
remove observable scratch writes or introduce broad guards to force fitting.

Production Init, decoder/adapter source, default flags and README aggregates
are unchanged in this checkpoint. Existing uncommitted Game work is preserved
and excluded from the documentation commit. Nothing is pushed.
