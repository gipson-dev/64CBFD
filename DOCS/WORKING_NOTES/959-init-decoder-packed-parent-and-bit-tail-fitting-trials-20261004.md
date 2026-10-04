# Init Decoder Packed Parent And Bit Tail Fitting Trials

Date: 2026-10-04. Trial baseline: `245359b1`.
The separate inventory assessment is banked in `720f082d` / Note 958.

## Decision

Continue the requested Init work with two new isolated decoder fitting
hypotheses, not another inventory-only assessment. **Reject both for adoption:**
packed parent entries grow the optimized executable by sixteen bytes; sharing
refill while inlining the bit-extraction tail grows it by thirty-two.
The qualified distance-operation-local baseline remains the best candidate:
**4,512 executable bytes against 3,984 retail, still 528 bytes over**.

Both options are disabled by default. No production Init owner, compiler
profile, word guard or README aggregate changes. These are experimentally
qualified C shapes, not completed conversions or original-C provenance claims.

## Size Attribution

The baseline C object's text is 4,336 bytes. The builder's public symbol
region occupies 401 words, but only **333 words belong to the builder's
actual direct-call unit**. Two unnamed units in that region occupy 22 and
46 words; inspecting their instructions/call targets shows they implement
ABI capture and table lookup, not builder-only code. The ledger's physical
symbol regions must not be mistaken for semantic function ownership.
The retail builder slot itself is 293 words.

### Packed Parent Entry

`--packed-parent` implies word-aligned entries and selects an explicit
endian-aware four-byte parent store. Operation/bits retain byte truncation,
and the child-table index retains halfword truncation. No unspecified entry
bytes are initialized: all four parent-entry bytes already have assigned
fields. The experiment changes the three retail-sized field stores into
one word store; it does not claim identical intermediate memory access width,
instruction scheduling, interrupt observations or retail instruction bytes.

IDO adds shifts/masks and OR operations to form the packed word. The optimized
builder unit grows from 333 to 337 words; the complete text grows by sixteen
bytes. O1 grows the builder unit by one word but remains inside the same
whole-object alignment allocation, so its total text size is unchanged.

### Shared Refill, Inline Bit Tail

`--inline-bit-tail` keeps `need_bits` shared, then directly masks the
reservoir and consumes the requested width inside `take_bits`. It removes
the tail's calls to `low_mask` and `drop_bits` without duplicating the refill
loop. Shift counts still use the existing masked-width semantics.

The optimized extraction helper grows from twenty words / 32-byte frame to
twenty-six words / 24-byte frame. Other callers still require the mask/drop
helpers, so those units do not disappear. The core allocation also grows
from 51 to 53 words. Overall, text grows by eight words / thirty-two bytes.
The maximum direct-call frame bound stays 400 bytes.

`--flat-bits` was measured on the same current baseline as a compiler control:
it also grows optimized text by thirty-two bytes, and its O1 image grows more.
It is existing source, not a third new retained implementation. CLI and direct
source checks reject combining the two alternative bit-extraction shapes.

## Complete Executable Measurements

Every total includes the actual 176-byte adapter. The retail budget is 3,984
bytes. These are complete text allocations, not just public C bodies.

| Shape | O2 C text | O2 plus adapter | O2 excess | O1 C text | O1 plus adapter |
| --- | ---: | ---: | ---: | ---: | ---: |
| Retained baseline | 4,336 | 4,512 | 528 | 5,808 | 5,984 |
| Packed parent | 4,352 | 4,528 | 544 | 5,808 | 5,984 |
| Inline bit tail | 4,368 | 4,544 | 560 | 5,840 | 6,016 |
| Existing flat-bits control | 4,368 | 4,544 | 560 | 5,872 | 6,048 |

Freshly recompiling with both new options disabled produces exactly the same
object instruction bytes as the initial control compilation in this turn:

```text
O2 .text 4336 bytes 177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d
O1 .text 5808 bytes 8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755
```

This is instruction-image equality, not equality of source hashes or debug
metadata. Historical full-corpus source hashes are not claimed current after
adding the opt-in branches.

## Qualification

The new module `tools/tests/test_init_decompressor_parent_and_bit_tail_trials.py`
reuses the complete bounded connected decoder tests for each guest variant,
across all three retained shapes and both compiler profiles. It also exercises
native-endian packed-parent semantics and specifically proves actual parent
word stores occur while all retail-written table bytes and the trailing fence
remain intact. Allocation commits, shared frame state, context snapshots,
CU1-clear/set paths, failures, malformed/repeated blocks, representative retail
pages, live-SP fences and saved-register contracts remain test requirements.

**All 105 trial tests pass in 641.203 seconds, no skips.** Twenty existing
inventory/slot-ledger/call-graph checks pass in 0.932 seconds, no skips.
Total: **125 passing tests across these two invocations**. Fifteen focused
trial/native checks also pass in 14.662 seconds; they repeat checks in the
105-test module and are not counted as additional distinct coverage.
Project tool checks and direct-source incompatibility guards pass.

Both optimized packed-remaining images retain the 3,248-byte static/observed
total stack descent, including the adapter and inherited decoder frame.
That measurement does not establish ownership of the private stack region.

The first long run was deliberately interrupted after correcting a new test's
JSON list-versus-tuple assertion. It is not counted as a completed passing run.
The corrected full run is separate. Neither full 507-page guarded CU1 corpus
was rerun: the new shapes regress fitting and are not adoption candidates.
Bounded model/compiled-instruction checks are not hardware or gameplay proof.

```sh
python3 -m unittest tools.tests.test_init_decompressor_parent_and_bit_tail_trials -q -f
python3 -m unittest tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls -q -f
make tools-check
```

Ignored standalone controls, compiler logs, disassemblies and measurements
live under `conker/build/init-packed-parent-20261004/`. The compiler driver
accepts `--packed-parent` and `--inline-bit-tail` for reproducing the options
with the existing distance-operation-local flags; the test classes provide
the complete flag and adapter contracts.

## Next Work

- [x] Attribute public symbol regions versus actual call units before fitting.
- [x] Measure new parent-packing and shared-refill/inline-tail hypotheses.
- [x] Verify default-option instruction images remain unchanged.
- [x] Complete connected regression qualification for both rejected trials.
- [ ] Find a reduction in the complete image, not an uncounted wrapper shift.
- [ ] Resolve private-stack reservation, entry ownership and placement before adoption.

Production Init remains 492 C / 47 assembly entries. Its existing linked code,
data and all Game data remain raw retail-exact. No production rebuild, sibling
source import/build, Release change, ROM promotion, runtime acceptance or push.
