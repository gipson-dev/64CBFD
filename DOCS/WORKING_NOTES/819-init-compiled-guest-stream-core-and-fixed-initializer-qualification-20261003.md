# Init Compiled Guest Stream, Core and Fixed Initializer Qualification

Date: 2026-10-03. Baseline: `7b826ae`.

## Result

Actual linked IDO instructions now execute the connected stored, fixed,
dynamic and core paths under the bounded MIPS model. Forty-eight cases across
six fresh images give 288 stream/core comparisons against retail assembly.
Every case first executes the compiled fixed-table initializer and compares
its allocation, roots/widths and table bytes, giving 288 initializer runs.

The final 74 combined checks pass. They also rerun all 186 compiled-builder
comparisons from Note 818 and the unchanged native/retail oracles. No candidate
C, compiler profile, production ownership, word guard or README count changes.
Smallest text stays 4,160 bytes, 176 over retail before original-entry adapters.
Pending Game edits remain outside this checkpoint.

## Harness Extension

The guest-only control-flow loop adds signed BLEZ/BGTZ and REGIMM BGEZ forms,
with their supported likely variants, plus SRA data execution needed by the
cursor pointer difference. The retail reference interpreter is unchanged.
Unknown REGIMM forms/instructions still fail. Primitive tests cover 24 signed
branch/value combinations, checking both destination visits and delay-store
annulment, plus three signed-shift boundaries.

The same three frame-backed shapes (baseline, aligned/end, packed/remaining)
are freshly compiled and linked at O2/g3 and O1. Stream tests and builder
regressions use separate temporary six-image sets, not stale ignored outputs.
Each compile/link must have an empty log and the expected profile/text receipt.
Linked `.text`/rodata remain read-only. Caller state is at `0x60000`, physical
frame at `0x70000`, normal O32 stack at `0x10000`, output at `0x40000` and
input at `0x50000`. Those addresses are test-owned, not exception ownership.

Compiled fixed setup writes into caller-owned workspace at `0x8003BE90`.
It must produce allocation 658 and roots/widths 1/7 and 626/5, preserve saved
O32 registers and leave reserved frame/save cells untouched. The complete
table matches retail-written fields; unused header bytes have explicit `0xA5`
seeds in both comparisons. That table becomes read-only during decoding.
Initializer and stream use independent caller scratch lifetimes, represented
by resetting the supplied frame after initialization.

## Cases

| Group | Cases | Compiled connected runs |
| --- | ---: | ---: |
| Stored/fixed payloads, long overlap copy and guarded history underflow | 8 | 48 |
| Dynamic repeats, repeat-first, overflow, invalid header/code and late error | 6 | 36 |
| Bad stored inverse and strict stored/match limits 0..5 | 13 | 78 |
| Two core headers, four input alignments, two workspace limits and invalid header | 17 | 102 |
| Two generated dynamic payloads, mixed blocks and core failure after output | 4 | 24 |
| Total | 48 | 288 |

Core valid cases are 2 header forms x 4 alignments x 2 workspace addresses =
16, plus one malformed-header case. Workspace `0x42000` lies within the owned
output buffer after an 8,192-byte gap; both the real C workspace pointer and
its numeric address use that location, matching retail's alias/layout case.
The baseline workspace is `0x20000`. No arbitrary caller aliasing is qualified.

Mixed stored/fixed/dynamic input must visit the compiled stored decoder twice,
compressed decoder twice and dynamic decoder once. Other explicit gates
confirm entry into the requested path after initializer traces are cleared.
Valid raw expected-output cases also agree with independent zlib decoding.

## Acceptance Checks

- Stream/core return, input cursor, reservoir, bit count, produced count,
  limit, allocation, output/workspace/frame pointers match the retail state.
- Core compares against the snapshot at retail `0x100062F0`, before saved
  gp/fp/s7 restoration. Its actual scratch base is incoming SP minus `0xA88`;
  direct stream uses the incoming frame. Both are explicitly seeded alike.
- The complete physical frame prefix through `0xA44` matches. Guest save cells
  `0xA44..0xA87` and surrounding guards remain `0xA5`.
- The union of retail and guest writes in output/workspace is compared byte by
  byte, detecting extra guest writes as well as missing/different results.
  All runtime writes remain inside explicit owned ranges; input and fixed
  tables cannot be written during decoding. Image read-only ranges are not
  shared mutable state between fixtures.
- s0-s7, gp, sp, s8 and ra restore correctly. Observed normal C stack descent
  stays within each stream/core receipt's conservative direct-call frame bound.

The guarded underflow case preserves retail's behavior rather than adding a
history-validity check. Fixed-wrapper error suppression, partial output and
inverse-length error lifetimes remain part of the compatibility contract.

## Verification

- Initial connected six-test suite passes in 43.473 seconds after correcting
  fixture guard ownership and core-frame mapping and adding SRA semantics.
- Final 74 combined guest builder/stream, native semantic/frame, retail stream/
  decoder and call/slot tests pass in 81.193 seconds.
- Twelve fresh objects and linked images cover six connected profiles and six
  independent builder regression profiles; compiler/linker logs are checked empty.
- Root `make tools-check`, three Python syntax checks and `git diff --check` pass.
- No production build or full all-project test rerun. This is a test-harness
  checkpoint; prior full-suite results are not presented as a new complete run.

## Boundary And Next

The actual compiler words now have connected execution coverage for these
vectors, not only native C coverage. This remains a bounded low-word model,
not R4300 hardware, exception FR=1 state, DMA/cache behavior or the original
shared-register/FPR entry ABI. It does not establish caller allocation capacity
or general malformed-input safety. The complete 507-page retail corpus has
native/retail qualification but is not yet replayed through this guest harness.

Next qualify original retail pages through compiled guest core execution,
then continue original-entry adapter and size/stack fitting as independent gates.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_streams tools.tests.test_init_decompressor_guest_builder -v
```
