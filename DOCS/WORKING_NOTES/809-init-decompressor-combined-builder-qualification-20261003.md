# Init Decompressor Combined Builder Qualification

Date: 2026-10-03. Baseline: `0a061b1`.

## Result

The bounded-shift builder composes with both aligned and directly packed
entries on the tested semantic domain. Alignment removes the unaligned word
store forms without losing the bounded-shift text/frame improvement. Direct
packing saves another sixteen O2 text bytes but is not an unconditional win:
frame-backed O2 stack demand grows eight bytes, and O1 text grows sixteen bytes.

No production source or default experiment changes. Exact Init assembly,
README aggregate counts and separately pending Game changes remain untouched.
This qualifies two previously untested flag combinations, not an entry adapter
or production conversion.

## Measurements

Eight fresh guest objects use the existing IDO O2/g3 and O1 profiles. All eight
compiler logs are independently checked empty. Every object reports entry
layout `[4, 4, 0, 1, 2]`, and its builder has zero static `swl`/`swr` opcodes.
These counts are not effective-address or dynamic execution proofs.

| Representation / flags | O2 text bytes | O1 text bytes | O2 builder frame | O1 builder frame | O2 core call-frame bound | O1 core call-frame bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Embedded aligned + bounded | 4,800 | 5,152 | 192 | 96 | 440 | 312 |
| Embedded packed + bounded | 4,784 | 5,168 | 192 | 96 | 440 | 312 |
| Frame-backed aligned + bounded | 5,200 | 5,424 | 192 | 96 | 400 | 296 |
| Frame-backed packed + bounded | 5,184 | 5,440 | 200 | 96 | 408 | 296 |

Packed implies aligned. Call-frame bounds exclude caller-owned scalar state,
scratch frame, exception context and any original-entry adapter. Embedded
state is still 2,668 guest bytes; frame-backed scalar state is forty bytes plus
the caller-owned `0xA88` frame. The smaller embedded text is not justification
for abandoning original physical-frame qualification.

Frame-backed packed O2 remains 1,200 bytes over the 3,984-byte retail region;
aligned O2 remains 1,216 bytes over it. Packed O1 is 1,456 bytes over retail,
compared with aligned O1's 1,440 bytes. Alignment plus bounded shifts is the
measured lower-stack choice, not a production configuration change.

## Builder Attribution

The actual assembly instruction list for `func_1000696C` contains 293 words.
Frame-backed aligned/bounded C emits 612 O2 builder words; packed/bounded emits
607. Packing therefore removes five builder words, but whole-text saving is
only four words because the trailing slot padding changes. The core body stays
48 words in both objects; its measured slot changes from fifty to fifty-one.
Do not describe that padding change as a new core instruction.

The packed O2 builder alone is 314 words / 1,256 bytes larger than retail,
exceeding the entire candidate's net text excess of 1,200 bytes. That identifies
builder dataflow/addressing as the next size investigation. It does not prove
that shrinking only this function will resolve ownership, original-entry ABI
or all fixed slot constraints.

At O1, aligned/packed builder bodies are 565/570 words with the same 96-byte
frame; other named bodies are unchanged. Packing's twenty-byte builder increase
becomes sixteen whole-text bytes because of final padding.

## Semantic Qualification

`tools/tests/test_init_decompressor_combined_builder.py` adds five classes:
embedded/frame-backed aligned + bounded, embedded/frame-backed packed + bounded,
and undefined-behavior-sanitized embedded packed + bounded. They inherit the
existing semantic and physical-frame tests, actual workspace alignment checks,
and generated-tree comparisons against the assembly interpreter.

All seventy focused tests pass in 41.987 seconds. Each class runs all 507 retail
pages against zlib and the pristine output image, including counts and buffer
guards: 2,535 new combination-specific native page calls. Each also compares
29 generated complete trees, including depth sixteen and clamped overwide root
requests: 145 new tree comparisons. Sanitized calls are included in both totals.

The bounded-shift domain from [Note 808](808-init-decompressor-entry-alignment-packing-and-bounded-shift-trials-20261003.md)
still applies: valid array indices, sufficient word-aligned workspace and
coherent scratch metadata. These tests do not qualify arbitrary corruption,
insufficient storage, all malformed states, MIPS scheduling or full hardware
exception behavior. No cache/flat-helper combinations are newly qualified.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_combined_builder -v
python3 tools/experiments/compile_init_decompressor.py --aligned-entry --bounded-builder-shifts
python3 tools/experiments/compile_init_decompressor.py --packed-entry --bounded-builder-shifts
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts
```

All combinations have separate ignored measurement/disassembly/object outputs.
Default source and compiler flags are unchanged. Root `make tools-check` passes.

## Final Verification

- All 827 project tool tests pass in 279.696 seconds.
- All seventy focused combination tests pass in 41.987 seconds.
- Eight fresh guest compiles pass with independently checked empty logs.
- Across twenty inherited native corpus methods, the complete suite executes
  10,140 retail page calls; this is native C output qualification, not hardware.
- New test-module syntax and `git diff --check` pass.
- No production build, original-entry adapter or gameplay run is claimed.

## Next

Use the aligned/bounded frame-backed shape as the lower-stack comparison point
and packed/bounded as the smaller O2-text comparison point. Investigate the
builder's repeated physical-table address/index translation and live-value
pressure against retail's register lifetime; retain both receipts so a size
change cannot silently hide a stack regression. Production replacement remains
gated on original-entry ABI, storage ownership and fitting code layout.
