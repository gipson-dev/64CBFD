# Init Dynamic Code Lookup Capture and Inline Mask Trials

Date: 2026-10-03. Baseline: `c1064cb`.

## Result

None of the three dynamic lookup trials improves the O2 fitting lead. Capturing
table base, width and mask raises the cursor candidate's dynamic frame from
88 to 128 bytes. Mask-only capture raises it to 120. Inline mask calculation
keeps the 88-byte frame and removes the direct `low_mask` dependency, but adds
two body words and sixteen whole-text bytes.

Retain the previous cursor-only O2 comparison points: packed/cached-builder
4,208 text bytes / 368-byte core call-frame bound, and uncached aligned
4,240/352. The smallest candidate remains 224 bytes over the retail region.
These new modes are reproducible opt-in experiments, not promoted defaults.
Exact production Init assembly, default text hashes and README aggregates
remain unchanged; separately pending Game changes stay outside this work.

## Source Modes and Domain

`INIT_DECODE_CACHE_DYNAMIC_CODE` accepts three explicitly guarded values:

- `1` / driver `all`: capture code width, mask and workspace table base after
  the code-table builder returns, then reuse them through the length stream.
- `2` / `mask`: capture only the low mask after construction; retain frame
  width/root and workspace-pointer reads at lookup.
- `3` / `inline`: compute the original modulo-32 mask expression at lookup,
  without a cache variable or a direct low-mask helper call.

The builder's return status remains handled exactly as before; no new early
return or malformed-input check is introduced. Entry bit consumption, symbol
read timing, repeat behavior, cursor limits and subsequent builder calls retain
their previous source order. The general helper and all unrelated callers are
unchanged; this is not global helper inlining or a production compiler change.

Full capture requires stable code root/width, workspace base and frame during
the decoded-length loop. Mask-only requires stable code width. These assumptions
exclude aliased state/root corruption and are not proven production ownership
facts. Inline retains the original field reads and modulo-32 expression rather
than narrowing the shift domain. All variants still require coherent scratch,
valid input storage and sufficient workspace; the cursor's existing 316-cell
boundary qualification remains in force.

The driver option is `--cache-dynamic-code [all|mask|inline]`, with `all` when
no value is supplied. Each selection has a separate output suffix. A native
compiler check rejects values zero/four through the source guard, and the CLI
rejects an invalid choice. Omitting the option retains the original lookup.

## Full Capture Receipts

Text and frames are bytes. Bounds exclude caller scalar state, `0xA88` scratch,
exception context and original-entry adapter. Aligned/packed rows use the
existing cursor; packed includes builder counts/offsets caching.

| Shape, full capture selected | O2 text | O2 dynamic body words | O2 dynamic frame | O2 core bound | O1 text | O1 dynamic frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Embedded baseline | 4,960 | 214 | 168 | 464 | 5,360 | 128 | 360 |
| Frame baseline | 5,328 | 229 | 136 | 432 | 5,616 | 104 | 336 |
| Frame baseline / no unroll | 4,400 | 229 | 136 | 416 | 5,616 | 104 | 336 |
| Frame aligned/bounded/cursor / no unroll | 4,256 | 223 | 128 | 392 | 5,424 | 112 | 312 |
| Frame packed/bounded/cursor / no unroll | 4,224 | 223 | 128 | 408 | 5,440 | 112 | 320 |

Full capture grows text and stack in both representations/profiles. The cursor
shape grows from 220 to 223 dynamic words and from 88 to 128 frame bytes.
Do not infer a net benefit from eliminating repeated frame reads alone.

## Narrower Cursor Trials

All rows use physical frame scratch, bounded builder shifts, no unroll and the
dynamic cursor. Packed includes cached builder counts/offsets; aligned does not.

| Entry / lookup | O2 text | O2 dynamic body words | O2 dynamic frame | O2 core bound | O1 text | O1 dynamic frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aligned / original | 4,240 | 220 | 88 | 352 | 5,408 | 104 | 304 |
| Aligned / mask only | 4,256 | 222 | 120 | 384 | 5,408 | 104 | 304 |
| Aligned / inline | 4,256 | 222 | 88 | 352 | 5,408 | 104 | 304 |
| Packed / original | 4,208 | 220 | 88 | 368 | 5,424 | 104 | 312 |
| Packed / mask only | 4,224 | 222 | 120 | 400 | 5,424 | 104 | 312 |
| Packed / inline | 4,224 | 222 | 88 | 368 | 5,424 | 104 | 312 |

The inline call ledger has no direct edge from dynamic decoding to the leading
low-mask helper at text offset zero. Full/mask capture retain a direct edge,
now used by the source's pre-loop computation. Nested `take_bits` helper use
is not removed. This is a static direct-call observation, not measured runtime
instruction count, timing or hardware performance proof.

The dynamic body still grows two words with inline. Whole-text growth is four
words because trailing slot padding also changes. No other fitting conclusion
can be drawn from the removed helper edge. The original cursor object retains
its independently checked 1,052-word / 224-byte-excess ledger from Note 813.

## Qualification

Eleven native classes test full capture in embedded/frame-backed baseline and
both cursor comparison shapes, sanitized packed capture, aligned/packed mask
capture plus sanitizer, and aligned/packed inline plus sanitizer. Initial full
capture 76 tests pass in 45.706 seconds. Final 178 focused tests pass in 94.755
seconds, including 5,577 native retail page calls. Nine classes inherit 29
generated-tree comparisons, adding 261 checks against the assembly model.

Frame classes retain physical scratch/error lifetime, maximum 316-cell length
stream, fixed-root tail reuse and frame guards. Sanitized classes include the
entire retail corpus and physical-boundary checks. This qualifies source modes
on the stated domain, not IDO execution or arbitrary-state behavior.

Twenty-six final-source guest compiles pass: eight unchanged controls, ten full
capture shapes and eight narrower shapes. All logs are independently checked
empty. Full-capture objects are refreshed after introducing the mode guard;
all eight control text SHA-256 hashes remain unchanged.

No new qualification is claimed for mask/inline without cursor, embedded
mask/inline, or combinations with length-base / local-allocation / byte-parent /
workspace / builder cached-all / flat-helper trials. Native GCC output tests and guest
compiles do not prove MIPS scheduling, exception hardware, DMA/cache ownership
or original-entry ABI.

## Final Verification

- All 1,415 project tool tests pass in 557.410 seconds.
- Final 178 focused tests pass in 94.755 seconds; initial full-capture 76 pass
  in 45.706 seconds.
- Fifty-six native corpus methods execute 28,392 retail page calls.
- Twenty-six final-source guest compiles have independently checked empty logs;
  eight control text hashes remain unchanged.
- Direct-call receipts confirm inline removes the dynamic-to-low-mask edge;
  unsupported source values and invalid CLI choices are rejected.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- No production build, original-entry adapter or hardware/gameplay run is claimed.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_dynamic_code_cache -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --cache-dynamic-code
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --cache-dynamic-code mask --cache-builder counts-offsets
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --cache-dynamic-code inline --cache-builder counts-offsets
```

## Next

Keep original lookup with cursor-only as the measured O2 lead. Reject the three
lookup variants as size improvements. Inspect repeat-fill value/control-flow
and the rolled builder's scalar lifetimes against retail next; do not repeat
this capture/inlining matrix without a new hypothesis. Continue individual-slot,
original-entry adapter and storage-ownership qualification separately from
aggregate size. Production assembly remains the exact baseline.
