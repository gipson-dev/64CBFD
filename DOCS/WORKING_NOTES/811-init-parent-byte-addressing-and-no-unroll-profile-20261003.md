# Init Parent Byte Addressing and No-Unroll Profile

Date: 2026-10-03. Baseline: `e141840`.

## Result

Byte-offset parent lookup does not improve the measured guest candidate.
Disabling IDO loop unrolling does: frame-backed aligned/bounded O2 text falls
from 5,200 to 4,256 bytes, and its core direct-call frame bound falls from 400
to 384 bytes. This leaves 272 bytes over the 3,984-byte retail region, down
from 1,216. It is the strongest measured fitting lead so far, not a production
conversion or original-entry ABI qualification.

The packed/bounded no-unroll candidate also occupies 4,256 bytes but has a
392-byte bound. Alignment/bounded without parent byte addressing or workspace
caching is therefore the lower-stack comparison point at this text size.
Production assembly, default experiment text and README aggregates stay exact
and unchanged. Separate Game changes are not part of this checkpoint.

## Source Trial

`INIT_DECODE_BYTE_PARENT` spells the parent lookup as a workspace byte offset:
the stored guest table label minus the guest workspace label, rounded down to
a four-byte entry boundary, plus the selected entry's four-byte displacement.
It preserves separate parent field writes and all stored table metadata.
It does not cast a guest absolute address into a native pointer. Both labels
remain 32-bit, including subtraction after a wrapped table label.

The native pointer additions require coherent metadata and sufficient backing
storage for the translated parent entry. Arbitrary corrupt indices, insufficient
capacity and overflowing out-of-object pointer arithmetic are not qualified.
The low-bit mask preserves the original index form's rounding; it is not a new
alignment assumption. The mode requires physical frame tables and is rejected
without `INIT_DECODE_FRAME_BACKED` at compile time and `--frame-backed` in the
driver.

## Profile Trial

`--no-unroll` adds the existing project IDO flag `-Wo,-loopunroll,0` to both
guest profiles and writes distinct `-no-unroll` outputs. The production Makefile
already uses this option on other recovered slices. This is an isolated
experiment; no production compiler recipe is changed. The original driver
profiles and default output names remain unchanged.

The O1 objects' size/frame measurements do not change under this flag. O2
does substantially change. Do not describe native GCC tests as execution of
the IDO no-unroll objects; those objects have compilation/layout/call-ledger
receipts only in this checkpoint.

## Guest Matrix

Frame-backed measurements, in bytes. Bounds exclude caller scalar state,
the `0xA88` scratch frame, exception context and any entry adapter.

| Mode | O2 text | O2 builder frame | O2 core bound | O1 text | O1 builder frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 5,312 | 208 | 416 | 5,600 | 128 | 328 |
| Baseline + byte parent | 5,312 | 208 | 416 | 5,600 | 128 | 328 |
| Aligned + bounded | 5,200 | 192 | 400 | 5,424 | 96 | 296 |
| Aligned + bounded + byte parent | 5,216 | 192 | 400 | 5,424 | 96 | 296 |
| Packed + bounded | 5,184 | 200 | 408 | 5,440 | 96 | 296 |
| Packed + bounded + byte parent | 5,184 | 200 | 408 | 5,456 | 96 | 296 |
| Baseline + no unroll | 4,384 | 192 | 400 | 5,600 | 128 | 328 |
| Baseline + byte parent + no unroll | 4,384 | 192 | 400 | 5,600 | 128 | 328 |
| Aligned + bounded + no unroll | 4,256 | 176 | 384 | 5,424 | 96 | 296 |
| Aligned + bounded + byte parent + no unroll | 4,272 | 176 | 384 | 5,424 | 96 | 296 |
| Packed + bounded + no unroll | 4,256 | 184 | 392 | 5,440 | 96 | 296 |
| Packed + bounded + byte parent + no unroll | 4,256 | 184 | 392 | 5,456 | 96 | 296 |

Twenty-six fresh guest compiles cover this matrix and two embedded default
controls. All compiler logs are independently checked empty. Eight preexisting
control `.text` byte sequences compare exactly after recompilation: both
embedded default profiles and six frame-backed baseline/combined profiles.
The CLI rejects `--byte-parent` without a frame-backed representation.

## Instruction Attribution

Aligned/bounded frame-backed O2, with only unrolling changed:

| Named unit | Default slot words | No-unroll slot words | Saving bytes |
| --- | ---: | ---: | ---: |
| Builder | 612 | 422 | 760 |
| Compressed block decoder | 131 | 100 | 124 |
| Fixed table setup | 95 | 82 | 52 |
| Core slot | 50 | 48 | 8 |

The core body remains 48 words; its two-word slot reduction is padding, not
removed instructions. Other named units and the leading helper region retain
their lengths. These savings sum to 944 bytes, exactly the whole-text change.

The no-unroll builder is still 422 words versus retail's 293: 129 words /
516 bytes over that original function. Dynamic decoding and other individual
slots still need their own fitting analysis. The 272-byte aggregate deficit
does not prove that every function can occupy its original address, or that
ordinary C frames can replace retail's shared-register entry convention.

## Semantic Qualification

Four new native classes cover frame-backed byte parent lookup at baseline,
aligned/bounded, packed/bounded and sanitized packed/bounded. All 71 focused
tests pass in 40.153 seconds. They inherit all 507 retail pages, semantic error
paths, physical scratch checks and 29 generated complete trees per class.
This adds 2,028 native retail page calls and 116 generated tree comparisons.

Each class also tests five guest workspace labels, including `0xFFFFFFC0`
and `0xFFFFFFFC`, with a narrow root and nonzero initial allocation. These
twenty wrapped-label comparisons verify status, root, width, allocation,
all frame bytes after table-label translation, and every written workspace
byte against the actual assembly interpreter. The native workspace pointer
is independent of the guest label.

These tests qualify the source trial on the stated domain. They do not prove
MIPS execution/scheduling, exception hardware behavior, DMA/cache ownership
or original-entry ABI. Cache-workspace / cached-array / flat-helper combinations
are not newly qualified by this matrix.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_byte_parent -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --byte-parent
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --byte-parent --no-unroll
```

## Next

Final verification: all 976 project tool tests pass in 340.930 seconds. The
suite's twenty-nine native corpus methods execute 14,703 retail page calls.
Root `make tools-check`, both changed/new Python syntax checks and
`git diff --check` pass. Both the native compiler and CLI reject byte-parent
mode without frame tables. No production build or hardware/gameplay run is
claimed.

Retain the aligned/bounded no-unroll shape as the strongest lower-stack fitting
lead. Do not pursue byte-parent or workspace capture as improvements. Use the
rolled builder's live-value/register ledger to investigate its remaining
129-word excess, and separately map individual routine fitting constraints.
Production replacement remains gated on fitting layout, storage ownership
and the original-entry ABI, not just aggregate size or native output tests.
