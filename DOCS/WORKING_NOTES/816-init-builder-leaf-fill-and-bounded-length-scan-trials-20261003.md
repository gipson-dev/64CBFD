# Init Builder Leaf Fill and Bounded Length Scan Trials

Date: 2026-10-03. Baseline: `0285a92`.

## Result

Removing redundant min/max histogram scan bounds improves both O2 comparison
points by sixteen text bytes without increasing their call-frame bounds.
Packed/bounded, no-unroll, cursor, builder counts/offsets cached reaches
4,192/368 bytes (text/core direct-call bound), versus 4,208/368. Aligned,
uncached reaches 4,224/352, versus 4,240/352. The smallest candidate is still
208 bytes over the 3,984-byte retail region, before an original-entry adapter.

Per-run leaf table capture is a negative fitting result: both leading O2
objects retain their text sizes but grow their frame bounds eight bytes.
Both experiments stay opt-in. Production Init ASM and README counts are
unchanged. Separately pending Game edits remain outside this checkpoint.

## Symbol Regions Versus Public Call Units

The 413-word builder figure in Notes 812-815 is its public-symbol region, not
the standalone builder body. IDO places the unnamed lookup helper between
the builder and compressed decoder. In the packed cursor control, builder
occupies 357 words and lookup occupies 56, together 413. Its public builder
unit is 64 words over retail's 293; the region is 120 over. The helper has to
be placed somewhere, so this distinction does not remove aggregate excess.

The receipt now records `slot_words` on every direct-call unit, and
`public_unit_words` / `embedded_helpers` on each public-symbol measurement.
It verifies that those units exactly partition each region, then includes
the breakdown in the retail ledger. Unit boundaries use public symbols and
resolved JAL targets, not guessed source-line boundaries. Padding remains
part of unit size; legacy `body_words` describes the region's final return
extent and must not be read as excluding unnamed helpers.

The bounded-scan packed O2 builder unit is 352 words, with the same 56-word
helper: a 408-word region. Core remains 48 body words, but final alignment
changes its slot from 49 to 50 words. Thus five builder words saved yield
four net words saved. The ledger is 993 named-region words plus 55 leading
helper words = 1,048, versus retail's 996: 52 words / 208 bytes over.

## Source Changes And Preconditions

`INIT_DECODE_CACHE_LEAF_TABLE` captures workspace plus table index and fill
stride inside the existing nonempty-run gate. It retains numeric indexing,
so it does not advance a pointer beyond the table after the final store.
Every store has `next < size`; stride is positive under the existing width
domain. The experiment assumes the workspace base is not mutated by aliased
workspace writes during the run. This is not original-entry ownership proof.

`INIT_DECODE_BOUNDED_LENGTH_SCAN` keeps the count-zero and all-zero returns,
then scans buckets 1..16 for the first and last populated buckets without
redundant index-limit tests. For valid input lengths in 0..16, a nonempty
histogram that is not all-zero must have a populated bucket in 1..16. Both
scans therefore stop inside the same histogram. Existing coherent scratch,
valid arrays, sufficient capacity and independent state requirements remain.
Out-of-range lengths or alias-corrupted counts are not newly accepted inputs.
The histogram already indexed input lengths before either source variant.

No error ordering, count publication, allocation update, table layout or
entry packing changes. No `restrict`, assembly word guards or production
entry adapter is introduced. Driver options are `--cache-leaf-table` and
`--bounded-length-scan`, with separate output suffixes and no default change.
Their combination is not qualified in this checkpoint.

## Guest Receipts

All shapes below use cursor-only dynamic code; frame rows use no-unroll and
bounded shifts, packed rows also use counts/offsets caching. Values are bytes.
Bounds exclude caller state, physical `0xA88` scratch and exception/adapter.

| Shape / trial | O2 text | O2 builder frame | O2 core bound | O1 text | O1 builder frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Embedded / control (no cursor) | 4,928 | 208 | 456 | 5,328 | 128 | 344 |
| Embedded / leaf capture (no cursor) | 4,912 | 216 | 464 | 5,360 | 136 | 352 |
| Embedded / bounded scan (no cursor) | 4,896 | 208 | 456 | 5,312 | 128 | 344 |
| Aligned / control | 4,240 | 176 | 352 | 5,408 | 96 | 304 |
| Aligned / leaf capture | 4,240 | 184 | 360 | 5,424 | 104 | 312 |
| Aligned / bounded scan | 4,224 | 176 | 352 | 5,392 | 96 | 304 |
| Packed / control | 4,208 | 192 | 368 | 5,424 | 104 | 312 |
| Packed / leaf capture | 4,208 | 200 | 376 | 5,440 | 112 | 320 |
| Packed / bounded scan | 4,192 | 192 | 368 | 5,408 | 104 | 312 |

## Verification

- Final 135 focused tests pass in 97.183 seconds; initial leaf-only 74 pass
  in 69.645 seconds. Eight native classes add 4,056 retail-page calls.
- Six aligned/packed native classes inherit generated complete-tree and
  runtime shift checks, including depth sixteen and sanitized variants.
  Empty/all-zero, incomplete and oversubscribed trees retain existing oracles.
- Twenty final-source guest objects compile with independently checked empty
  logs. Eight controls retain pre-edit `.text` SHA-256 hashes. All objects'
  public-unit/helper sizes independently sum to their symbol-region sizes.
- Root `make tools-check`, four Python syntax checks and `git diff --check`
  pass. All 1,544 project tool tests pass in 813.680 seconds.
- Native tests do not execute IDO objects. No production build, original ABI
  adapter or hardware/gameplay qualification is claimed.

## Reproduction And Next

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_fill_and_scan tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --cache-builder counts-offsets --bounded-length-scan
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll --dynamic-cursor --bounded-length-scan
```

Keep bounded scan as the new measured size/stack comparison; reject leaf
capture as the fitting lead. Continue builder register-lifetime/source-shape
work against its actual unit and account for helper placement separately.
Preserve all original entry, slot-size, storage and matching gates.
