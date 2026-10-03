# Init Fixed Length Pointer Ranges And Complete Table Qualification

Date: 2026-10-03. Baseline: `94275e6`.

## Result

Opt-in `--fixed-length-cursor` expresses the fixed literal-length initializer
as four pointer ranges: 144 entries of 8, 112 of 9, 24 of 7 and eight of 8.
The two builder calls and thirty distance-length stores remain unchanged.
The original conditional indexed loop remains the default.

Packed/remaining O2 core text shrinks from 4,544 to 4,528 bytes. Including the
unchanged 320-byte adapter, the new best linked text is 4,848 bytes: 864 bytes
over the original 3,984-byte group, down from 880. This is a real linked-size
reduction, not a builder saving absorbed by padding. Packed O1 grows 48 bytes.
Production assembly is unchanged; this is not a completed conversion.

## Trials

All trials use the established frame/packed, bounded shifts/scans, no-unroll,
dynamic cursor, cached counts/offsets, remaining-symbol cursor, FPR shadow,
shared lookup and histogram cursor options. Optional arithmetic operation
selection is measured separately:

| Fixed-length trial | O2 core text | O1 core text |
| --- | ---: | ---: |
| Histogram baseline | 4,544 | 5,920 |
| Indexed constant ranges | 4,560 | 6,000 |
| Pointer constant ranges, retained | 4,528 | 5,968 |
| Arithmetic-operation baseline from Note 847 | 4,544 | 5,904 |
| Indexed ranges plus arithmetic operation | 4,560 | 5,984 |
| Pointer ranges plus arithmetic operation | 4,528 | 5,952 |

The indexed form and temporary range selector are removed. Arithmetic plus
pointer is size-only evidence in this checkpoint; the runtime-qualified
variant does not select the arithmetic-operation option. No semantic or
full-corpus claim is made for those measured combinations.

Ignored receipts remain under
`conker/build/init-fixed-ranges-{indexed,cursor}-{histogram,simple}-20261003`.
Packed fixed-initializer body shrinks from 82 to 78 words at O2; core body/
slot stay 60/60, so all four saved words survive into linked text. O1
initializer grows from 104 to 116 words; core body/slot stay 89/91.

## Qualified Costs

Final retained-flag bounded builds keep 116-byte state and a 320-byte adapter:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,096 | 3,280 | 3,280 |
| Frame O1 | 6,480 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,880 | 3,240 | 3,240 |
| Aligned/end O1 | 6,272 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,848 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,288 | 3,192 | 3,192 |

All O2 shapes shrink 16 bytes and all O1 shapes grow 48 relative to Note 844.
All stack bounds are unchanged. Packed core-only bounds remain 408/O2 and
344/O1. Packed O2 minimum SP is `0x80031D58`, retaining the measured 72-byte
known-neighbor clearance; complete reservation ownership remains unproven.

## Verification

The inherited domain passes 420 stream/context comparisons and 114 direct
builder comparisons across all six shapes/profiles. Error, empty-tree and
multiblock gates remain exercised; the nested lookup sample still records
3,212 calls / 3,383 iterations on page 169. Fixtures execute the changed
initializer, rather than injecting a prebuilt fixed table.

A new direct initializer fixture records stores in the literal-length staging
interval and executes the compiled initializer alone. All six builds have
exactly the expected 318 ordered four-byte stores: 288 literal lengths, then
thirty distance lengths of 5. All final staging words, allocation 658,
roots/widths 1/7 and 626/5, and all 2,632 fixed-table bytes match the retail
builder oracle. Following workspace bytes and reserved frame guards remain
unchanged; saved registers and direct call-frame bounds pass. These six
initializer comparisons are separate from the 420/114 domains.

Terminal commands:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_fixed_length_cursor
wsl python3 -m unittest tools.tests.test_init_decompressor_fixed_length_cursor.InitDecompressorFixedLengthCursorTests.test_fixed_initializer_ordered_lengths_and_complete_table
```

The first run loaded the module before the direct initializer test was added:
16 tests in 196.640 seconds, 15 pass and one intentional full-corpus skip.
The added initializer test passes separately in 3.521 seconds. Combined:
16 pass, one skip. Fresh compiler and linker logs are empty.

Root `make tools-check` and `git diff --check` pass. No production build,
ordinary full-suite, new full corpus, hardware replay or sibling-port test
is claimed. Notes 845/846 remain receipts for the earlier histogram variant,
not this changed initializer.

## Next

- [x] Compare indexed and pointer fixed-length range shapes.
- [x] Retain a smaller linked O2 initializer and record the O1 growth.
- [x] Qualify bounded contexts, direct builders and the complete fixed table.
- [ ] Continue actual fitting; 864 linked bytes remain above retail capacity.
- [ ] Full changed corpus in both masked CU1 modes before promotion.
- [ ] Other-profile full corpus and outstanding ownership/hardware/resume gates.

Full-corpus entry point, not run here:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_fixed_length_cursor.InitDecompressorFixedLengthCursorCorpusTests -v -f
```

Keep fitting variants opt-in; do not promote from size and bounded tests alone.
Production Init, adapter assembly, default options and README aggregates
remain unchanged. Existing uncommitted Game work is preserved and excluded
from the checkpoint. Nothing is pushed.
