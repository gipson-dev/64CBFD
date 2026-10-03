# Init Histogram Cursor Full Masked CU1-Set Corpus

Date: 2026-10-03. Source baseline: `59e910e3`.

## Result

All 507 retail Game pages pass the full shadow-context corpus for the changed
histogram-cursor decoder, packed/remaining O2/g3 profile, exception-masked
entry with CU1 set. This closes the first changed-source full-corpus gate in
[Note 844](844-init-builder-histogram-cursor-fitting-and-bounded-qualification-20261003.md).
It is new evidence for that source, not a reassignment of Notes 830/831.

The terminal process exits zero: one opt-in test passes in 744.102 seconds,
with 507 paired page comparisons, no skips and no reported failures.

## Command And Terminal Receipt

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor.InitDecompressorHistogramCursorCorpusTests -v -f
```

The corpus subclass explicitly selects `--loop-lookup` and
`--builder-histogram-cursor`. The existing setup freshly compiles and links
six shadow images before selecting the single requested profile; this run
executes only packed/remaining O2/g3. The CU1 selector is unset, whose explicit
default is `set`; the printed entry Status confirms `0x2400FF00`.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4864 depth=3256 low=0x80031D58 margin=72
shadow corpus complete: modes=set runs=507
Ran 1 test in 744.102s
OK
```

| Measured property | Result |
| --- | ---: |
| Paired retail/experimental page runs | 507 / 507 |
| Linked core plus adapter text | 4,864 bytes |
| Maximum observed stack descent | 3,256 bytes |
| Minimum observed SP | `0x80031D58` |
| Known protected neighbor end | `0x80031D10` |
| Minimum measured clearance | 72 bytes |
| Original retail group capacity | 3,984 bytes |
| Remaining size excess | 880 bytes |

The size and stack values agree with Note 844's bounded receipt. No new
source, adapter, production profile or word guard is introduced here.

## What The Gate Proves

The live comparison harness was inspected before interpreting the receipt.
Each page verifies the rounded DMA supply against ROM and the expected
decompressed bytes against the pristine image. Retail and changed guest
paths then compare results, GPRs, full modeled FPR state and scratch FPR
snapshots, modeled Status writes, wrapper save/load behavior, base decoder
state, physical scratch and changed output/workspace bytes. Stack bounds,
rounded input read bounds, entry-path visits and the protected-neighbor
write fence remain active.

This is deterministic instruction-oracle evidence for the selected corpus,
profile and context. It does not prove real DMA/cache/TLB behavior,
asynchronous faults, scheduler resume, gameplay, all reservation ownership,
other compiler profiles or the CU1-clear context. Successful page streams
also do not replace Note 844's separate malformed/direct-builder tests.

Root `make tools-check` and `git diff --check` pass. No production build,
full ordinary test suite, hardware replay or sibling-port test is claimed.

## Next

- [x] Full 507-page changed histogram variant, masked entry with CU1 set.
- [ ] Same changed packed O2/g3 corpus with masked CU1 clear.
- [ ] Full-corpus qualification for the other five build shapes/profiles.
- [ ] Continue fitting: remove the remaining 880 linked bytes above retail.
- [ ] Complete outstanding reservation/hardware/resume qualification before promotion.

Next independent gate:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_histogram_cursor.InitDecompressorHistogramCursorCorpusTests -v -f
```

That command was not run in this checkpoint. Production Init remains
unchanged; README aggregate numbers are not changed by experimental
qualification. Existing uncommitted Game work is preserved and excluded
from this documentation checkpoint. Nothing is pushed.
