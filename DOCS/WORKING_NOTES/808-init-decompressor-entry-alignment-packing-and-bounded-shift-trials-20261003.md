# Init Decompressor Entry Alignment, Packing and Bounded Shift Trials

Date: 2026-10-03. Baseline: `45e4075`.

## Result

The bounded-builder-shift representation improves both text and ordinary C
stack measurements. Frame-backed O2/g3 text falls from 5,312 to 5,200 bytes,
and the core direct-call frame bound falls from 416 to 400 bytes. O1 text falls
from 5,600 to 5,424 bytes, with the bound falling from 328 to 296 bytes.
This is still 1,216/1,440 bytes over the 3,984-byte retail region. It remains
an opt-in experiment, not a production conversion or qualified entry adapter.

Alignment-only and directly packed entry variants establish the retail storage
shape but do not solve fitting layout. Production assembly and README
aggregates remain unchanged; pending Game edits are preserved separately.

## Entry Storage Evidence

Retail parent links store operation, bit count and value using two byte stores
and one halfword store at `0x10006C28..0x10006C30`. Replicated leaf entries are
different: `0x10006CD0..0x10006CE4` forms a packed word, and the replication loop
uses aligned `sw` at `0x10006CFC` and in its branch delay at `0x10006D0C`.
Do not describe both paths as field-by-field stores.

The original C entry is four bytes but has two-byte alignment. IDO copies its
local record with `swl`/`swr`. `INIT_DECODE_ALIGNED_ENTRY` uses a union containing
the same fields and a word-alignment member, preserving size and field offsets.
Field access macros select the original struct or the union's named fields;
no packed-pointer cast or manual endian conversion is needed for this mode.

`INIT_DECODE_PACKED_ENTRY` constructs the leaf word directly and writes the
aligned union word. Guest packing follows the retail big-endian layout. Native
packing uses the compiler's declared byte order so native field readers still
see the same values. Unknown native byte order is explicitly rejected. Packed
mode requires aligned mode; the driver supplies that dependency automatically.
Parent links retain their original separate field stores.

A new guest/native receipt records size, alignment and field offsets. Default
is `[4, 2, 0, 1, 2]`; aligned/packed modes are `[4, 4, 0, 1, 2]`. The native
tests also check actual workspace/fixed-table base addresses are word-aligned.
These modes do not qualify an arbitrary two-byte-aligned caller buffer.

## Builder Shift Bounds

`INIT_DECODE_BOUNDED_BUILDER_SHIFTS` changes only the builder's shifts and its
consumed-bit low-mask expression. General bit readers retain modulo-32 masks.
The source hypothesis is based on the constructor's clamped width domain,
not on assuming all input shifts are safe:

| Builder expression | Bound on coherent constructor state |
| --- | --- |
| Tree minimum/maximum and clamped root width | 1 through 16 |
| `consumed` at entry emission/backtracking | 0 through 15 |
| Parent `consumed - width`, only above root | 0 through 15 |
| `bits - consumed` for entry replication | 1 through 16 |
| `bits - 1` | 0 through 15 |
| Allocation `levelBits` | At most 17, including the retail ceiling increment |

Each new table advances consumed by width only when `bits > consumed + width`,
so consumed stays below bits. At the root, offset zero is initialized to zero;
the zero-width low mask stops coherent backtracking there. The allocation scan
can increment once even when already at its ceiling, so its bound must include
that increment. A valid nonzero length supplies the min/max bounds; zero-count
and all-zero-length paths return before these expressions.

The trial still requires valid array indices, sufficient workspace and coherent
scratch metadata, as the current C representation does. It does not qualify
arbitrary alias corruption or invalid length-array memory. No new early return
or validation branch is added to the retail algorithm.

Generated tests build 29 complete trees, including depth-16 skew trees and
shallow trees with an overwide requested root that clamps to the actual maximum.
They trace the actual assembly's variable shift register values, compare C
status/root/width/allocation and every written workspace byte, and run under
undefined-behavior sanitization. The cases are repeated for embedded,
frame-backed and sanitized representations: 87 tree comparisons. This supports
the bounded-domain argument but is not an exhaustive proof of all malformed
states or a hardware execution receipt.

## Guest Measurements

All values below use forty-byte scalar state and the same caller-owned `0xA88`
frame. Bounds are conservative direct-call sums, excluding those caller objects,
the adapter and exception context.

| Variant | O2/g3 text | O1 text | O2/g3 builder frame | O1 builder frame | O2/g3 core bound | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 5,312 | 5,600 | 208 | 128 | 416 | 328 |
| Aligned entry | 5,312 | 5,600 | 208 | 128 | 416 | 328 |
| Direct packed entry | 5,296 | 5,616 | 208 | 136 | 416 | 336 |
| Bounded builder shifts | 5,200 | 5,424 | 192 | 96 | 400 | 296 |

The alignment-only builder slot loses one word, but whole-text padding absorbs
the saving. Direct packing saves sixteen O2/g3 bytes but regresses O1 text/frame.
The bounded-shift trial eliminates builder low-mask helper calls as well as
redundant masks, reducing spill pressure. It is the first trial here to improve
both text and core frame bound, but still does not fit the original region.

The guest call ledger now counts `sw`, `swl` and `swr` opcode forms per unit.
These are static counts, not dynamic execution counts or effective-address
alignment proofs. A synthetic test pins the counter independently of the guest
objects. The entry-layout parser checks byte layout and selected alignment.

Both profiles have one static `swl` and one `swr` in the baseline builder;
aligned and packed modes have zero of each. Bounded-shift mode alone retains
the baseline entry alignment and those two store forms. Do not attribute its
text/frame savings to the separate alignment change.

Embedded-state text is 4,928/5,328 bytes at baseline, 4,928/5,328 aligned,
4,896/5,344 packed, and 4,800/5,152 with bounded builder shifts. The bounded
mode's improvement therefore holds for both representations, unlike the earlier
builder-base capture trial.

## Reproduction

Run from the repository root in WSL:

```sh
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry
python3 tools/experiments/compile_init_decompressor.py --frame-backed --bounded-builder-shifts
python3 -m unittest tools.tests.test_init_decompressor_aligned_entry -v
python3 -m unittest tools.tests.test_init_decompressor_bounded_shifts -v
```

Each mode writes separate ignored objects/logs/disassembly/JSON. Omitting the
frame option tests embedded scratch. Combinations with the earlier cache/flat
flags or with each other are not qualified by these standalone mode tests.
The host corpus is inherited by all new classes, including the sanitizer class;
all 507 retail pages are checked for exact output/counts and input/output guards.
These tests do not claim MIPS scheduling or full exception hardware acceptance.

## Verification

- Initial alignment-only 27 tests pass (15.978 seconds).
- Initial bounded-shift/sanitizer 35 tests pass (36.503 seconds); the added
  generated-tree sanitizer test also passes (0.578 seconds).
- All 757 project tool tests pass (201.989 seconds), including final packed and
  generated-tree modes. Fifteen corpus methods execute 7,605 native C retail
  page calls, including sanitized calls.
- Twenty-eight isolated guest compiles pass: both representations, seven
  standalone source modes and two profiles. All logs are independently checked
  empty; the complete entry/frame layout and call-ledger receipts are refreshed.
- Fresh default `.text` bytes compare exactly with the prior object text for
  both representations/profiles. Measurement data and optional typedefs do not
  perturb default instruction bytes.
- Root `make tools-check`, four Python syntax checks and `git diff --check` pass.
- No production source build, original-entry adapter, gameplay/hardware run or
  aggregate conversion increase is claimed.

## Next

Continue the builder dataflow investigation using the bounded-shift result as
the measured lead, while retaining the default and exact production baseline.
Keep explicit ownership and malformed-state boundaries visible. A smaller C
object alone does not settle the original shared-frame ABI or fitting slot;
no broad word guards or aggregate conversion increase is justified yet.
