# Init Dynamic Length Base and Pointer Cursor Trials

Date: 2026-10-03. Baseline: `3fd1e9a`.

## Result

Dynamic cursor-only improves both O2 text and stack measurements. Packed/bounded,
no-unroll, builder counts/offsets cached now occupies 4,208 bytes with a 368-byte
core direct-call frame bound, versus 4,224/400 previously. It remains 224 bytes
over the 3,984-byte retail region. Uncached aligned/bounded with cursor reaches
4,240/352, versus 4,256/384: the lower-stack O2 comparison point.

Capturing the dynamic length base alone gives a small text saving but increases
the packed candidate's bound to 408. Combining it with cursor reaches 416.
Do not combine individually plausible changes without measuring their overlap.
Cursor-only, without dynamic base capture, is the useful O2 source lead here.

Production Init assembly, default candidate text hashes and README aggregates
stay unchanged. Original-entry ABI, storage ownership and individual slot
fitting remain open. Separately pending Game changes remain outside this work.

## Source Shapes and Bounds

`INIT_DECODE_CACHE_DYNAMIC_LENGTHS` captures `LENGTHS(s)` after validating the
dynamic header and uses the same pointer for code-length setup, expanded-length
writes and subsequent builder calls. It does not copy or snapshot buffer data.
It requires the selected frame/base not to be mutated by aliased input/output
or workspace writes during the call. That is an experimental stable-base
assumption, not established production ownership.

`INIT_DECODE_DYNAMIC_CURSOR` captures the expanded-length cursor after the
code-table builder call. It writes `*cursor++`, compares the cursor to its end,
and checks repeat count against `end - cursor` before writing a repeated run.
Header setup, builder calls, previous-length behavior, root fields and error
ordering are otherwise unchanged. The default retains indexed writes and the
original integer repeat bound.

After existing header validation, literals are at most 286 and distances at
most thirty, so total is at most 316. The physical frame has exactly 316 staging
length cells. Cursor starts at the first cell; its end is within that array or
one-past. Every direct store starts with cursor below end. Repeat count is
checked against the remaining cells before incrementing the pointer. Thus the
pointer difference is nonnegative and at most 316 on coherent state, and its
`uint32_t` conversion preserves the value. The indexed repeat test cannot
overflow either on this domain: index is at most 316 and repeat at most 138.

No new malformed-input rejection or early return is added. The retail handling
of repeat-first and partially decoded error state is preserved. Valid input
storage, coherent scratch, independent stable state/frame pointers and enough
workspace remain required. Arbitrary alias corruption is not qualified.

The driver adds `--cache-dynamic-lengths` and `--dynamic-cursor` with separate
output suffixes. Neither implies the other, and no production recipe changes.

## Length Base Capture Receipts

Values are bytes; dynamic frame is the ordinary C frame for that routine.
Core bounds exclude caller state, `0xA88` scratch, exception context and adapter.
Packed rows include builder counts/offsets caching; aligned rows do not.

| Representation / shape, base capture selected | O2 text | O2 dynamic frame | O2 core bound | O1 text | O1 dynamic frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Embedded baseline | 4,944 | 160 | 456 | 5,328 | 120 | 352 |
| Frame baseline | 5,296 | 128 | 424 | 5,600 | 96 | 328 |
| Frame baseline / no unroll | 4,368 | 128 | 408 | 5,600 | 96 | 328 |
| Frame aligned/bounded / no unroll | 4,256 | 128 | 392 | 5,424 | 96 | 296 |
| Frame packed/bounded / no unroll | 4,208 | 128 | 408 | 5,424 | 96 | 304 |

The frame-backed O2 dynamic body falls from 224 to 221 words, but its frame
grows from 120 to 128 bytes. Padding can absorb the twelve-byte body saving;
aligned whole-text size remains unchanged. Embedded O2 text grows sixteen bytes.
This is not an across-representation/profile improvement.

## Cursor Receipts

All rows are frame-backed. The first four omit length base capture; the last
selects both experiments. Packed rows retain builder counts/offsets caching.

| Shape | O2 text | O2 dynamic frame | O2 core bound | O1 text | O1 dynamic frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline + cursor | 5,296 | 88 | 384 | 5,584 | 104 | 336 |
| Baseline / no unroll + cursor | 4,368 | 88 | 368 | 5,584 | 104 | 336 |
| Aligned/bounded / no unroll + cursor | 4,240 | 88 | 352 | 5,408 | 104 | 304 |
| Packed/bounded / no unroll + cursor | 4,208 | 88 | 368 | 5,424 | 104 | 312 |
| Packed/bounded / no unroll + cursor + base capture | 4,208 | 136 | 416 | 5,408 | 104 | 312 |

Cursor-only dynamic O2 body is 220 words and its frame is 88, versus 224/120
before. The smallest object's deepest direct-call sum is 24 + 64 + 88 + 192 =
368 bytes (core, stream, dynamic and builder). Aligned uses a 176-byte builder,
giving 352. Base capture plus cursor increases dynamic frame to 136 instead.
O1 cursor shapes save text but increase their bound compared with the previous
indexed forms; this is an O2 fitting/stack lead, not a uniform compiler win.

## Updated Slot Ledger

The smallest cursor-only object has 997 named-slot words plus 55 leading helper
words, totaling 1,052. Retail's 994 body words plus two alignment NOPs total
996. The deficit is therefore 56 words / 224 bytes, independently checked.

Relative to [Note 812](812-init-rolled-scratch-cache-and-local-allocation-trials-20261003.md),
only the dynamic slot shrinks, from 224 to 220 words. Its retail body has 167,
so it remains 53 words over. Builder remains 413 versus retail 293, 120 over.
Other slot counts, helper region and missing original-wrapper qualifications
remain unchanged. A smaller aggregate still does not prove exact-slot fitting
or provide an original-entry adapter.

## Semantic Qualification

Ten native classes test embedded/frame-backed length base capture, aligned
capture, packed cached-builder capture, sanitized packed capture, frame baseline
cursor, aligned cursor, packed cached-builder cursor, combined capture/cursor,
and sanitized combined capture/cursor. Initial base-only 76 tests pass in
53.646 seconds; the final 159 focused tests pass in 91.648 seconds.

Each class executes all 507 retail pages, adding 5,070 native page calls. Seven
classes inherit 29 generated tree checks, adding 203 assembly comparisons.
Frame classes inherit exact physical scratch/error lifetimes, maximum 316-cell
connected lengths, fixed-root tail reuse and guards around the `0xA88` frame.
Sanitized calls include both corpus and those physical-boundary checks.

Twenty-eight final-source guest compiles pass: eight unchanged controls, ten
base-only shapes and ten cursor shapes. Logs are independently checked empty.
All eight controls retain their pre-edit `.text` SHA-256 hashes. Base-only
objects are recompiled after the final cursor edit, not taken from the initial
source snapshot.

Native GCC tests do not execute IDO objects or prove MIPS scheduling, exception
hardware, DMA/cache ownership or original-entry ABI. Embedded cursor and
local-allocation / byte-parent / workspace-cache / cached-all / flat-helper
cursor combinations are not newly qualified.

## Final Verification

- All 1,237 project tool tests pass in 448.497 seconds.
- Final 159 focused tests pass in 91.648 seconds; initial base-only 76 pass
  in 53.646 seconds.
- Forty-five native corpus methods execute 22,815 retail page calls.
- Twenty-eight final-source guest compiles have independently checked empty
  logs; eight control text hashes remain unchanged.
- The 1,052-word object ledger and 368-byte deepest direct-call frame sum are
  independently checked from the fresh object receipt.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- No production build, original-entry adapter or hardware/gameplay run is claimed.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_dynamic_lengths -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll --dynamic-cursor
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --cache-builder counts-offsets
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --cache-dynamic-lengths --dynamic-cursor --cache-builder counts-offsets
```

## Next

Retain cursor-only as the O2 dynamic source lead and the two measured text/stack
comparison points, 4,208/368 and 4,240/352. Investigate dynamic code-table lookup
and bit-helper call overhead against retail's stable decoding state, while
preserving malformed/error ordering. Continue to track builder excess and
entry/slot/ownership gates separately; production assembly remains the baseline.
