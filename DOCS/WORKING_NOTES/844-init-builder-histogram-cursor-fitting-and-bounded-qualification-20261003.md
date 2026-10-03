# Init Builder Histogram Cursor Fitting And Bounded Qualification

Date: 2026-10-03. Baseline: `cc2c25b`.

## Result

The opt-in `--builder-histogram-cursor` changes only the builder's length
histogram traversal. It saves 16 bytes in both packed/remaining compiler
profiles. The smallest linked decoder/adapter is now 4,864 bytes, still
880 bytes over the original 3,984-byte group. This is experimental fitting
progress, not a production assembly conversion.

Current structured inspection of `conker/progress.init.csv` confirms 492 C
rows / 151,796 bytes and 47 assembly rows / 12,252 bytes, totaling 539 rows /
164,048 bytes. No production build or matcher regeneration was performed in
this checkpoint. The remaining-assembly triage in [Note 792](792-init-resume-remaining-assembly-conversion-decision-20261003.md)
still applies: bitmap `func_10005BE0` and MMIO `func_100038E0` are the two
bounded ordinary-C candidates without proven matching replacements. The ten
decoder entries require connected interface recovery and fitting; most other
rows retain original SDK, hardware or nonstandard entry contracts.

## Source Shape And Size Trials

After the existing zero-count return, the histogram walks `lengths` through
a pointer cursor until `lengths + count`. It retains the histogram accesses,
all-zero return, subsequent symbol sorting, table allocation and ABI shadow
behavior. No early failure, count restriction or bit-refill reordering is
introduced. The original indexed loop remains the default.

Fresh packed/remaining trials used the existing frame, packed-entry, bounded
shift/scan, no-unroll, dynamic-cursor, counts/offsets cache, remaining-symbol
cursor, FPR shadow and shared-lookup flags:

| Trial | O2/g3 core text | O1 core text |
| --- | ---: | ---: |
| Fresh shared-lookup baseline | 4,560 | 5,936 |
| Histogram cursor only, retained | 4,544 | 5,920 |
| Sorting cursor only, rejected | 4,560 | 5,952 |
| Both cursors, rejected | 4,560 | 5,936 |

The sorting variants and their temporary selector are removed. They have
size receipts only, not semantic qualification. Ignored local receipts remain
under `conker/build/init-fitting-baseline-20261003` and
`conker/build/init-length-cursor-{histogram,sort,all}-20261003`.

## Qualified Costs

Fresh bounded-test builds use the final histogram-only flag. All retain
116-byte state and a 320-byte adapter:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,112 | 3,280 | 3,280 |
| Frame O1 | 6,432 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,896 | 3,240 | 3,240 |
| Aligned/end O1 | 6,224 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,864 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,240 | 3,192 | 3,192 |

Packed core-only call-frame bounds are 408/O2 and 344/O1. O1 grows eight
bytes from Note 829; this is not a universal stack improvement. Packed O2
retains minimum SP `0x80031D58`, 72 bytes above the known protected neighbor
ending at `0x80031D10`. This guard is not complete reservation ownership.

## Verification

The new test subclass reuses the 348 shadow and 72 masked comparisons:
420 bounded stream/context comparisons across six shapes/profiles and both
CU1 modes. They include representative retail pages 0, 169 and 506, failure,
empty-tree and multiblock cases; compare output, state, saved context, scratch
and modeled Status behavior. The nested lookup gate still records 3,212 calls
and 3,383 iterations on page 169 with exact output.

A direct builder test additionally performs 19 cases across six builds:
114 paired comparisons against the retail instruction oracle. Cases cover
zero count, all-zero histograms, incomplete/oversubscribed trees, relocated
allocation, full 288-symbol capacity, depth sixteen with five root widths,
and explicit base/extra arguments. It reuses the existing builder checks for
root/width/allocation, physical scratch/workspace bytes, saved registers,
frame bounds and adjacent guards. These are separate from the 420 stream
comparisons, not a full corpus or hardware receipt.

Terminal commands:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor
wsl python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor.InitDecompressorHistogramCursorTests.test_direct_builder_cursor_boundaries
```

The first run loaded the module before the direct test was added: 15 tests
in 191.017 seconds, 14 pass and one intentional corpus skip. The added direct
test passes separately in 3.897 seconds. Combined: 15 pass, one skip; compiler
and linker logs are empty. Root `make tools-check` and `git diff --check` pass.
No production build, full-suite, hardware, gameplay or sibling-port run.

## Next

- [x] Resume decoder fitting after the bounded diagnostic lifetime audit.
- [x] Measure three cursor shapes and retain only the smaller histogram loop.
- [x] Qualify bounded contexts and direct builder boundaries in both profiles.
- [x] Run all 507 pages on the changed packed O2 variant with masked CU1 set;
  subsequently completed in [Note 845](845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md).
- [ ] Repeat the changed full corpus with CU1 clear; other profiles remain open.
- [ ] Continue fitting: 880 linked bytes remain above retail capacity.
- [ ] Complete outstanding reservation/hardware/resume qualification before promotion.

Full-corpus entry point, not run in this checkpoint:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor.InitDecompressorHistogramCursorCorpusTests -v -f
```

Subsequent [Note 845](845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md)
qualifies this changed source's full masked CU1-set corpus. CU1-clear remains open.
Notes 830/831 qualify the previous lookup variant, not this changed source.
Production Init, adapter assembly, default experimental flags and README
aggregates stay unchanged. Unrelated Game work is preserved and excluded
from this checkpoint.
