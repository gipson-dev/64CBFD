# Init Original Core Call Adapter And Exception Context

Date: 2026-10-03. Baseline: `63571c2`.

Follow-up: [Note 822](822-init-fpr-provenance-and-failure-frame-corrections-20261003.md)
maps scratch-FPR lifetimes and corrects newly exposed symbol/frame discrepancies.
The expanded seeded failure domain has different text/stack costs; this note's
unseeded size and original test-domain receipts remain historical measurements.

## Result And Boundary

An isolated assembly adapter now accepts the original three core arguments:
input in a0, output in a1 and workspace in a2. It constructs the recovered
40-byte C state, calls the actual compiled IDO core, publishes low-word f16-f19
state and preserves the original saved GPRs and return/SP contract.

The retained exception wrapper at `0x10005E1C..0x1000601B` executes around
that adapter. Only its JAL at `0x10005F2C` is redirected in the fixture;
production assembly is not patched. The original core cannot run in the guest
fixture, which contains only the wrapper, linked C and adapter instructions.

Seven CU1-clear vectors across six fresh images give 42 wrapper/adapter
comparisons. Retail pages 0, 169 and 506 add 18 comparisons, for 60 positive
context runs. Each first executes compiled fixed-table initialization.
Stored, fixed and dynamic success, reserved-block failure, repeat overflow,
bad stored inverse and failure after partial output are covered.

This does not complete original-ABI qualification. Six CU1-already-set
dynamic runs deliberately demonstrate the remaining scratch-FPR mismatch.
FR=0, hardware exception timing, caches and real allocation ownership remain
unqualified. No production C ownership, compiler shape or README count changes.

## Layout And Preservation

The adapter allocates retail's `0xA88` scratch/save frame, preserving s0-s7,
fp, gp and ra at their original offsets. An additional `0x48` bytes below it
hold a 32-byte O32 outgoing area and the 40-byte C state. The state frame
pointer targets the actual retail scratch base, not an unrelated fixture block.
The compiled call chain descends below that extra area.

Fixed-table initialization uses an independent normal test stack before the
exception run. An initial fixture attempt placed its C stack inside the retail
scratch and failed on corrupted addressing. Separating the initialization
lifetime fixes that fixture overlap; no guard or instruction check was weakened.

The exception run owns a private 4 KiB lower-stack range, 4 KiB workspace and
64 KiB output buffer. Numeric input/workspace/caller-SP addresses remain
`0x80033330`, `0x800340E8` and `0x80032A10`. Ownership of those private
buffers is not evidence that the original exception caller has that capacity.

Tests compare the core return and published f16-f19 values before wrapper
restoration, all ten C state words, complete scratch prefix through `0xA44`,
output/workspace write unions, full wrapper save cells, final GPRs, all full
FPR architectural values/masks, Status writes and FPR save/load addresses.
The adapter and compiled-core entry visits are mandatory; retail core visits
are forbidden. Representative-page input reads stay inside each rounded span.
Read-only image/fixed-table protection and caller-buffer write guards remain.

## Measured Costs

The adapter body is 212 bytes. Linked text grows by 224 bytes, including
alignment padding. The smallest combined candidate is 4,384 bytes against
3,984 retail bytes, a 400-byte excess before remaining entry requirements.

| Shape/profile | Linked text bytes | Conservative descent bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,536 | 3,184 | 3,184 |
| Frame O1 | 5,824 | 3,096 | 3,096 |
| Aligned/end O2/g3 | 4,416 | 3,128 | 3,128 |
| Aligned/end O1 | 5,632 | 3,080 | 3,080 |
| Packed/remaining O2/g3 | 4,384 | 3,144 | 3,144 |
| Packed/remaining O1 | 5,632 | 3,088 | 3,088 |

Descent is measured from the incoming core SP, not from the exception's
original remote SP. Bounds equal `0xA88 + 0x48 + compiled core call bound`.
For packed/remaining O2, the extra area and C call chain add 448 bytes below
retail scratch. Fitting and actual storage ownership remain independent gates.

## CU1-Set Gap

The retained wrapper always reloads f0 from its stale slot in the branch delay
slot, even when CU1 started set. That behavior, final GPRs and Status changes
are preserved. Published f16-f19 and untouched FPRs also agree.

The C core does not reproduce retail's f1-f11 builder scratch effects. Tests
require an observed architectural value/mask difference in that range rather
than claiming compatibility or replacing those values with synthetic defaults.
The final six-profile receipt reports differences in all eleven f1-f11 cells.
This is a model compatibility gap, not a measurement of hardware upper-half
behavior. The shared FR=1 transfer helper retains unknown-high-word tracking
after MTC1 and full doubleword save/load semantics.

## Verification

- Expanded initial suite: all 11 exception/adapter tests pass in 31.371 seconds.
- Final combined suite: all 95 focused tests pass in 144.955 seconds, including
  the unchanged builder/stream, native/retail frame, exception, call/slot tests
  and the separate direct-core representative-page test.
- Adapter qualification includes 60 positive CU1-clear context runs and six
  CU1-set gap runs, each with compiled fixed initialization. The direct-core
  representative regression adds 18 separate calls; do not mix those counts.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- No all-project test rerun, production build or new all-507-page adapter replay.
  Note 820's corpus receipt applies to direct compiled core calls, not this adapter.

## Next

- [x] Prototype the original three-argument core adapter in isolated linked images.
- [x] Run the retained CU1-clear exception wrapper around compiled core execution.
- [x] Qualify representative retail pages and measure added text/stack costs.
- [ ] Recover CU1-set f1-f11 scratch effects and qualify the full context contract.
- [ ] Establish original storage ownership and reduce combined code/stack costs.
- [ ] Preserve all required interior entries before production ownership changes.

```sh
python3 -m unittest tools.tests.test_init_decompressor_exception tools.tests.test_init_decompressor_guest_adapter -v -f
```
