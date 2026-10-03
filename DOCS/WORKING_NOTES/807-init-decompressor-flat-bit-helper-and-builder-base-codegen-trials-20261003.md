# Init Decompressor Flat Bit Helper and Builder Base Codegen Trials

Date: 2026-10-03. Baseline: `3ce309f`.

## Result

Two focused source hypotheses change the isolated guest C's code generation,
but neither supplies a fitting production replacement. Flattening `take_bits`
removes its nested helper frame while increasing total text. Capturing builder
scratch-array bases reduces text but increases its ordinary C frame. Keep both
opt-in; the default candidate and exact production assembly remain unchanged.
The connected retail region is 3,984 bytes. Init remains 492/539 C functions
with 47 assembly routines; README aggregate counts are unchanged.

## Source Hypotheses

`INIT_DECODE_FLAT_BITS` puts the existing refill, mask and drop bodies directly
inside `take_bits`. It preserves their state-access order and width masking;
it does not cache reservoir/input state across the refill loop, reorder partial
failure publication, or remove checks. The helper's nested calls disappear,
but the separate helpers remain needed elsewhere.

`INIT_DECODE_CACHE_BUILDER=1` captures count, sorted-symbol and offset array
bases for the builder. Mode 2 captures only counts and offsets, leaving the
less frequently used sorted-symbol base as before. Array writes, root lifetimes,
workspace address translation, allocation logic and returns are unchanged.
Captures occur after the original zero-count guard. Unsupported cache values
are rejected at compile time.

These captures follow the recovered fixed physical-frame base. Tests do not
qualify arbitrary workspace/input aliasing into the candidate scalar state or
an externally mutated frame pointer. Original-entry adapter and ownership
qualification remain separate requirements; no production alias promise is
inferred from successful host tests.

## Guest Measurements

All values below use the physical-frame representation, four-byte entries,
forty-byte scalar state and the same `0xA88` scratch frame layout.

| Variant | O2/g3 text | O1 text | O2/g3 builder frame | O1 builder frame | O2/g3 core call-frame bound | O1 core call-frame bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 5,312 | 5,600 | 208 | 128 | 416 | 328 |
| Flat bit helper | 5,344 | 5,680 | 208 | 128 | 416 | 328 |
| Cache all three bases | 5,216 | 5,552 | 224 | 144 | 432 | 344 |
| Cache counts/offsets | 5,248 | 5,552 | 224 | 136 | 432 | 336 |

The flat helper is a zero-frame leaf under O2/g3 and an eight-byte leaf under
O1. Stored-block direct-call bounds fall from 80/72 to 48/48 bytes. The complete
core bound does not fall because the builder path remains dominant.

All-three caching saves 96 O2/g3 text bytes and 48 O1 text bytes, at the cost of
sixteen frame bytes in both profiles. Two-array caching retains the O1 saving
with only eight additional frame bytes; it saves 64 O2/g3 text bytes but still
adds sixteen frame bytes there. The smallest measured text is still 1,232
bytes over retail. No variant improves both text and the core frame bound.

The embedded-array representation does not share these text savings:
baseline 4,928/5,328 bytes, flat helper 4,960/5,408, all-three cache
5,072/5,376, and counts/offset cache 5,072/5,360. Do not generalize the
frame-backed improvement to all representations.

Call-frame bounds are the existing relocation-aware conservative direct-call
sums, not guest runtime high-water. They exclude caller-provided frame,
scalar storage, adapter and exception context. Export-to-next-export slots can
include unnamed helpers; whole-text size is the meaningful fitting measurement.

## Reproduction

From the repository root in WSL:

```sh
python3 tools/experiments/compile_init_decompressor.py --frame-backed
python3 tools/experiments/compile_init_decompressor.py --frame-backed --flat-bits
python3 tools/experiments/compile_init_decompressor.py --frame-backed --cache-builder
python3 tools/experiments/compile_init_decompressor.py --frame-backed --cache-builder counts-offsets
python3 -m unittest tools.tests.test_init_decompressor_flat_bits -v
python3 -m unittest tools.tests.test_init_decompressor_cached_builder -v
```

Each driver option has its own ignored output suffix; baseline receipts are not
overwritten by the variants. Object logs, disassembly, layout and call graphs
remain under `conker/build/init-decompressor-semantic*`. Omitting `--frame-backed`
also measures the original embedded-array representation. Combined helper/cache
flags are accepted by the driver but are not covered by these measurements or
the new variant test classes; do not infer their qualification.

Host tests inherit ten semantic methods per embedded-state mode and fifteen
semantic/physical methods per frame-backed mode, including the new shared retail
corpus method. The three source choices add 75 variant test methods covering
builders, every length/distance extra-bit class,
stored/fixed/dynamic and mixed streams, failure publication, limits, full frame
bytes, root aliases, 316-length-cell domain and relocated workspace addresses.
They compare the actual compiled C with the retained assembly model; they are
not guest execution or hardware exception acceptance.

The shared corpus test exercises all 507 retail pages in both baseline modes
and all six new C variants: 4,056 native C page calls. Expected bytes come from
ROM-identity-checked zlib streams and pristine decompressed Game slices.
It checks returned/produced counts, exact output, unchanged input, output
sentinels, and frame guards where applicable. This broadens actual C coverage;
it does not measure guest scheduling, prove fitting layout or validate arbitrary
malformed-input aliasing.

## Verification

- Initial flat helper's 23 methods pass (17.882 seconds); initial all-three
  builder cache's 23 methods pass (15.109 seconds).
- All 656 tests before adding the shared retail corpus pass (149.427 seconds).
- Sixteen isolated guest compiles pass with empty logs: both representations,
  four source choices and two compiler profiles.
- Fresh default `.text` bytes compare exactly with the prior object text under
  both representations/profiles. Optional trials do not perturb default codegen.
- Five initial baseline/frame-variant retail corpus methods pass (3.392 seconds).
- All 664 project tool tests pass (138.302 seconds), including all eight
  all-retail-page C corpus methods and the final source modes.
- All sixteen guest logs are independently checked empty; all four changed/new
  Python modules pass syntax compilation.
- Root `make tools-check` and `git diff --check` pass.

## Next

Target builder register pressure and memory access shape with an explicit new
dataflow hypothesis. A text-only win that grows stack use is not sufficient.
The recovered ABI/ownership gates from Notes 805/806 still apply. Preserve the
exact baseline until a fitting C candidate and its original-entry contract are
both qualified; do not manufacture a conversion with broad word guards.
