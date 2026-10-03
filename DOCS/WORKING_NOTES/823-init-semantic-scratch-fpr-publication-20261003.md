# Init Semantic Scratch-FPR Publication

Date: 2026-10-03. Baseline: `92c2d9d2`.

## Result And Boundary

The isolated decompressor now has an opt-in `--abi-fpr-shadow` variant.
Semantic snapshots and the corresponding adapter preserve the tested retail
exception-wrapper FPR effects on both CU1-clear and CU1-set paths. This is a
bounded FR=1 architectural model result, not hardware timing qualification,
full-corpus acceptance, or a production conversion.

Production Init remains 492 C functions / 47 assembly functions, with
151,796 C bytes and 12,252 assembly bytes. The current CSV was rechecked.
No production source, ownership, linker layout or README aggregates changed.
Unrelated pending Game source/tests remain excluded from this checkpoint.

## Implementation

- The flag requires frame backing and implies distance-root seeding. Default
  compiler and adapter profiles retain their existing state/layout.
- Opt-in O32 state grows from 40 to 116 bytes: six historical S-register values,
  twelve scratch-FPR low words, and a dirty indicator. Entries remain four bytes.
- Incoming history comes from the adapter's saved retail S0-S5 frame cells.
  Compressed decoding tracks subsequent literal, length/distance and table-leaf
  history, using the actual fixed-table base when operating on fixed tables.
- Dynamic decoding captures the code-builder boundary and the later literal/
  distance-builder boundary. Early errors retain the last actual snapshot.
  Paths without scratch-FPR writes leave the dirty indicator zero.
- The shadow adapter publishes f0-f11 with MTC1 only when a snapshot exists.
  This preserves low words and the model's unknown-high-word masks even if a
  low word happens to be unchanged. Publication is deferred to core return;
  it does not reproduce instruction timing or intermediate hardware faults.
- Its private outgoing/state area grows from 0x48 to 0x98 bytes. The original
  0xA88 physical scratch frame and saved-register offsets remain unchanged.
  The test fixture's state address is derived from this explicit area size.

## Measured Costs

All six profiles are freshly compiled and linked with the conditional adapter.

| Shape/profile | C text | Combined text | Core-call descent bound/observed |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,808 | 6,128 | 3,272 / 3,272 |
| Frame O1 | 6,160 | 6,480 | 3,192 / 3,192 |
| Aligned/end O2/g3 | 4,608 | 4,928 | 3,240 / 3,240 |
| Aligned/end O1 | 5,968 | 6,288 | 3,176 / 3,176 |
| Packed/remaining O2/g3 | 4,576 | 4,896 | 3,256 / 3,256 |
| Packed/remaining O1 | 5,984 | 6,304 | 3,184 / 3,184 |

The adapter body is 320 bytes (also its linked contribution), versus the
default 212-byte body / 224-byte linked contribution. Smallest combined text
is 912 bytes over retail's 3,984-byte region, and 464 bytes larger than the
root-seeded variant in Note 822. Private fixture storage and observed descent
do not establish the original caller's allocation ownership.

## Verification Scope

The new six-test module performs 204 shadow context comparisons across six
images: standard success/error cases, dynamic repeat overflow, fixed-literal
history, fixed match-copy history before dynamic success/early failure,
dense/repeated/sparse incomplete literal trees, and ROM pages 0, 169 and 506
in both CU1 modes. The flag-rejection test additionally checks frame backing.

Comparisons cover complete final GPR/FPR values and known-bit masks, Status
changes, wrapper FPR save/load addresses, result/state fields, physical
scratch prefix, output/workspace writes and retained wrapper context cells.
Call gates require the compiled core and adapter and forbid the retail core.
Representative ROM reads must stay within their rounded DMA spans.

The final combined shadow/default-adapter/provenance suite passes all 17 tests
in 170.610 seconds. An initial combined run exposed a borrowed-helper fixture
selection regression; the helper now defaults to the original fixture, and
the complete combined suite was rerun successfully after that correction.
Another 93 contract/table/decoder/stream/exception/frame/native-semantic/
frame-backed/call/slot regressions pass in 31.371 seconds, including the native
all-retail-page semantic check. Together these runs pass 110 focused tests.
Compiler, assembler and linker logs are empty. Root `make tools-check`, three
Python syntax checks and `git diff --check` pass.

The all-507-page compiled guest corpus from Note 820 was not rerun on this
shadow source. No production build or all-project test rerun is claimed.

## Next Gates

- [x] Recover scratch-FPR source values and write boundaries (Note 822).
- [x] Implement optional semantic snapshots and return-time publication.
- [x] Qualify both CU1 modes for the bounded vector/sample domain above.
- [ ] Expand CU1-set qualification to the full retail corpus and additional
  multi-dynamic and distance-builder failure histories.
- [ ] Establish original stack/state/workspace allocation ownership.
- [ ] Fit corrected semantic code and adapters without displacing neighbors.
- [ ] Only then consider production ownership conversion.

The remaining ordinary Init candidates are still bitmap `func_10005BE0`
(76 bytes) and MMIO `func_100038E0` (44 bytes), neither with a demonstrated
matching compiler replacement. Original SDK/boot/privileged assembly should
not be treated as ordinary missing-C backlog; see the inventory in Note 801.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_fpr_shadow tools.tests.test_init_decompressor_guest_adapter tools.tests.test_init_decompressor_fpr_provenance -v -f
```
