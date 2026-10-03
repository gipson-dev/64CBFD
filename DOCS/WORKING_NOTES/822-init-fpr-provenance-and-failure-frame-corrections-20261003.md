# Init FPR Provenance And Failure-Frame Corrections

Date: 2026-10-03. Baseline: `97a0229`.

## Result

The f1-f11 gap from Note 821 now has instruction-address and semantic-variable
provenance. Two experimental C discrepancies found during that recovery are
corrected: sorted-symbol classification now uses retail's signed comparisons,
and an opt-in physical-frame variant seeds the distance root from the final
code-length lookup index before calling the literal builder.

All 103 focused tests pass. Production Init ownership and README counts are
unchanged. The adapter still does not publish the recovered f1-f11 scratch
effects; mapping them is not full CU1-set compatibility.

## Register Lifetimes

The new fixture tracks actual instruction fetches, including delay slots,
without changing the shared retail interpreter. It records MTC1 source GPRs
and values, builder return roles and code/length decoding boundaries.

The builder's saves at `0x10006970..0x10006994` write f2-f11 from s0-s7,
fp and gp. The first save executes in a branch delay slot. Dynamic f0/f1
writes occur at `0x10006520/24` and `0x1000676C/70`.

| FPR | Code-builder snapshot | Literal/distance-builder snapshot |
| --- | --- | --- |
| f0/f1 | Literal and distance counts | Same counts |
| f2 | Live incoming/historical s0 | Last code-length table lookup index |
| f3 | Code-length scan ends at 19 | Last literal length symbol, or zero after exhausted repeats |
| f4 | Live historical s2 | Previous decoded length |
| f5 | Live historical s3 | Code-length lookup mask |
| f6 | Live historical s4 | Total literal plus distance length count |
| f7 | Live historical s5 | Code-length tree root |
| f8 | Workspace address | Workspace address |
| f9 | Input cursor at the call | Cursor after decoded lengths |
| f10/f11 | Bit count and reservoir at the call | Bit count and reservoir after decoded lengths |

Tests match later snapshots to frame lengths, recovered code root/width and
the length-completion boundary. A preceding fixed block changes the first
f2 snapshot to mask-table address `0x8002C0C0`, but later snapshots use the
lookup index instead. An initial incoming-s0 hypothesis for all calls was
therefore rejected by the trace, not baked into a replacement.

Stored/fixed-only and reserved-block paths do not write f1-f11. Repeat overflow
leaves only the code-builder snapshot, with no later literal/distance saves.
CU1-clear restores complete FPR values; CU1-set retains MTC1 low values and
unknown-high masks, except the wrapper's unconditional stale-f0 reload.
Future publication must preserve these write lifetimes, not uniformly overwrite
all scratch FPRs at core return.

## Signed Symbol Correction

Retail `0x10006C74` uses SLT against the simple-symbol threshold and
`0x10006C84` uses SLTI against 256. The candidate had unsigned comparisons.
The C now casts both threshold operands and the 256 comparison to `int32_t`.

A sparse incomplete tree leaves explicitly seeded `0xA5A5A5A5` words in the
sorted tail. Before correction, compiled C treated that word as a large unsigned
metadata index and made an unmapped guest read. Retail treats it as negative
and emits an operation-16 leaf with value `0xA5A5`. The final regression
requires that retail effect and compares the corrected guest's complete state,
workspace/output writes and restored context. No tail clearing, new validity
check or safer-but-different behavior is substituted.

Unseeded compiler text/frame sizes remain at the previous measured values;
instruction bytes are not claimed unchanged after the signedness correction.

## Distance Root Lifetime

Retail `0x10006760` stores live s0's low halfword to scratch `0xA3A` before
the literal builder. At that point s0 is the final code-length lookup index,
not the core caller's original s0. An incomplete literal tree can return before
the distance builder replaces the cell. Unseeded C retained `0xA5A5` instead.

`--seed-distance-root` requires `--frame-backed`, retains the last lookup entry
and writes its workspace-relative index before the literal build. It changes
no state/frame layout or adapter assembly. Its output path has a distinct
suffix; existing unseeded experiment outputs are not overwritten.

Four gated width-nine failure vectors use literal lengths directly or through
repeat-16, with and without preceding fixed/stored blocks. The sparse case
adds a fifth failure vector. Builder visits prove that code and literal builds
ran, while the distance build did not. Unseeded images differ at exactly
`0xA3A/0xA3B`; seeded images match the entire scratch prefix and state/write
checks on all six profiles. Seeds are 1 or 2, derived from the actual lookups.

Early all-zero and width-one probes did not produce the intended builder-error
gate: retail continued decoding. They were not accepted as failure evidence.
The final width-nine tree occupies 257 of 512 literal leaves and demonstrably
returns the required incomplete-tree status before distance construction.

## Measured Seeded Costs

| Shape/profile | C text | Text with adapter | Descent bound/observed |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,344 | 5,568 | 3,192 / 3,192 |
| Frame O1 | 5,648 | 5,872 | 3,096 / 3,096 |
| Aligned/end O2/g3 | 4,240 | 4,464 | 3,152 / 3,152 |
| Aligned/end O1 | 5,440 | 5,664 | 3,080 / 3,080 |
| Packed/remaining O2/g3 | 4,208 | 4,432 | 3,168 / 3,168 |
| Packed/remaining O1 | 5,456 | 5,680 | 3,088 / 3,088 |

For packed/remaining O2, seeding adds 48 text bytes and 24 call-frame bytes.
The combined 4,432-byte variant is 448 bytes over retail's 3,984-byte region.
The unchanged adapter body remains 212 bytes, 224 with linked alignment.
Private fixture buffers and these stack bounds do not establish real caller
allocation ownership. Unseeded 4,384-byte combined text remains a size datapoint,
not a fully compatible replacement for the new failure-frame domain.

## Verification

- Final eight-test provenance/correction module passes in 51.202 seconds.
- Final combined 103-test focused suite passes in 176.123 seconds.
- Twelve fresh core/adapter images cover six unseeded and six seeded variants.
  Five failure vectors give 30 unseeded gap receipts and 30 fully matching seeded
  context runs. Seeded standard vectors/retail pages add 60 matching context runs.
- Builder/stream, native semantic/frame, original exception, call/slot and
  representative direct-core regressions pass. Native all-507-page checks rerun;
  the full six-image guest corpus from Note 820 is not rerun on this source.
- Root `make tools-check`, three Python syntax checks and `git diff --check` pass.
- No production build or complete all-project test rerun is claimed.

## Next

- [x] Recover instruction-level scratch-FPR source values and write boundaries.
- [x] Fix signed sorted-symbol classification and qualify the sparse failure.
- [x] Prototype and qualify the missing distance-root lifetime with an opt-in flag.
- [ ] Publish semantic FPR snapshots with per-path write tracking, including
  incoming/history values before code construction and partial-error lifetimes.
- [ ] Qualify complete CU1-set adapter context, then expand its retail corpus.
- [ ] Establish actual storage ownership and fit corrected code plus entry adapters.

```sh
python3 -m unittest tools.tests.test_init_decompressor_fpr_provenance -v -f
```
