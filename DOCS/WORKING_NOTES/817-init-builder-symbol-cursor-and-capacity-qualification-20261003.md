# Init Builder Symbol Cursor and Capacity Qualification

Date: 2026-10-03. Baseline: `82296be`.

## Result

Packed/bounded, no-unroll, bounded length scan, dynamic cursor, cached builder
counts/offsets, and remaining-count symbol cursor reach 4,160 O2 text bytes,
176 bytes over retail's 3,984. The core direct-call frame bound grows from
368 to 376 bytes. This is a size/stack tradeoff, not an unconditional win.

Aligned pointer-end cursor reaches 4,192/360, compared with 4,224/352 without
a builder cursor. It offers the same text size as the previous packed lead
at eight fewer stack bytes. Keep three non-dominated O2 comparison points:
4,224/352 without cursor, 4,192/360 aligned/end, and 4,160/376 packed/remaining.
Packed/end at 4,176/376 is not the smallest candidate at that frame bound.

Production Init assembly, default candidate shapes and README counts remain
unchanged. Original-entry ABI/storage qualification and exact-slot fitting
are still open; the candidate is not linked. Pending Game edits are excluded.

## Source Shape And Bounds

`INIT_DECODE_BUILDER_SYMBOL_CURSOR=1` captures the sorted base and a pointer
end after histogram/sorting setup, at the original symbol-index reset. It
tests cursor against end, reads once, and advances once per consumed symbol.
Mode 2 holds a remaining count instead, decremented after each such read.
Both retain the same count-zero/all-zero returns and padded-leaf behavior.
They do not replace the original `count` boundary with the nonzero count.
Table/allocation writes, previous-value reuse and error ordering are unchanged.

Both scratch representations have 288 sorted cells. On the qualified domain,
count is at most 288 and input/scratch storage is coherent. Cursor starts at
the first sorted cell; mode 1's endpoint lies within that array or one-past.
Each read has remaining capacity, and the final advance reaches at most
one-past. Mode 2 allows exactly the same number of reads without forming an
end pointer. Empty/all-zero returns occur before cursor setup. No pointer
subtraction, `restrict`, speculative full-buffer copy or new rejection is used.

The sorted/frame base must remain stable during emission, and workspace
writes must not corrupt the pointer-bearing state or sorted scratch. These
are explicit valid-storage/non-aliasing requirements, not recovered original
entry ownership. Out-of-range lengths, excessive count or alias corruption
are not newly qualified. Unselected source uses its original indexed accesses.

Driver option `--builder-symbol-cursor` defaults to `end` when selected;
`--builder-symbol-cursor remaining` selects mode 2. Separate suffixes preserve
all existing outputs. Source rejects modes -1/0/3; CLI rejects unknown choices.
Other trial combinations are not implicitly qualified.

## Guest Receipts

Frame rows use the current bounded-scan/dynamic-cursor shapes; aligned is
uncached, packed retains builder counts/offsets caching. Values are bytes.
Call-frame bounds exclude state, physical `0xA88` scratch and adapter/context.

| Shape / symbol cursor | O2 text | O2 builder frame | O2 core bound | O1 text | O1 builder frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Embedded / none | 4,928 | 208 | 456 | 5,328 | 128 | 344 |
| Embedded / end | 4,928 | 224 | 472 | 5,344 | 136 | 352 |
| Embedded / remaining | 4,880 | 216 | 464 | 5,344 | 136 | 352 |
| Aligned / none | 4,224 | 176 | 352 | 5,392 | 96 | 304 |
| Aligned / end | 4,192 | 184 | 360 | 5,408 | 104 | 312 |
| Aligned / remaining | 4,208 | 184 | 360 | 5,408 | 104 | 312 |
| Packed / none | 4,192 | 192 | 368 | 5,408 | 104 | 312 |
| Packed / end | 4,176 | 200 | 376 | 5,408 | 112 | 320 |
| Packed / remaining | 4,160 | 200 | 376 | 5,408 | 112 | 320 |

The smallest packed O2 builder public unit is 346 words, 53 over retail's
293, plus the unchanged 56-word lookup helper in its 402-word symbol region.
The prior region was 408 words. Core body stays 48 words, but its final slot
loses two padding words, from 50 to 48. Six builder words plus two alignment
words account for the 32-byte text saving. Other public-symbol region sizes
are unchanged. The complete ledger is 985 named-region + 55 leading-helper
words = 1,040, versus retail's 996: 44 words / 176 bytes over.

## Verification

- Initial pointer-end 61 native tests pass in 36.528 seconds.
- Final eight native classes pass all 130 tests in 102.248 seconds, including
  4,056 retail-page calls and sanitized end/remaining packed variants.
- Each class explicitly compares 288 all-zero lengths, a sparse complete
  tree with 286 zero lengths, and the full 288-symbol fixed tree against the
  actual assembly builder model, including output root/bits/allocation and
  every written workspace byte. These add 24 full-capacity comparisons.
- Six aligned/packed classes inherit generated complete-tree/runtime-width
  checks, plus physical scratch/error-state and frame-boundary tests.
- Two source/CLI rejection tests pass in 0.177 seconds.
- Twenty final-source IDO objects compile with independently checked empty
  logs; eight controls retain their pre-edit `.text` SHA-256 hashes.
- All 38 baseline semantic/frame/call/slot tests pass in 16.724 seconds.
  Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- The full all-project suite is not rerun here; its 1,544-test success belongs
  to Note 816. This checkpoint uses focused native/compatibility/codegen checks.
  Native execution is not execution of IDO objects or original-entry hardware.

## Reproduction And Next

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_symbol_cursor -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --bounded-length-scan --dynamic-cursor --cache-builder counts-offsets --builder-symbol-cursor remaining
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll --bounded-length-scan --dynamic-cursor --builder-symbol-cursor
```

Continue source/lifetime fitting against the 346-word builder unit; keep the
lookup helper's placement separate from its size. Preserve the lower-stack
comparison points. Aggregate and per-entry fitting, original ABI and storage
ownership must all be established before changing the production assembly.
