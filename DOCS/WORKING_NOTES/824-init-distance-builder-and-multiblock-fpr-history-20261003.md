# Init Distance-Builder And Multiblock FPR History

Date: 2026-10-03. Baseline: `9157895`.

Follow-up: [Note 825](825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
identifies the larger retail 32-FPR thread footprint, guards that neighbor,
and qualifies all 507 pages for the smallest shadow profile with CU1 set.
It supersedes the guest-thread-size hypothesis below; full ownership remains open.

## Result

The optional shadow adapter now has stronger bounded qualification: twelve
additional streams exercise distance-builder outcomes and scratch-FPR lifetimes
across multiple blocks. Both CU1 modes pass on all six compiled profiles,
adding 144 comparisons to Note 823's 204, for 348 shadow comparisons total.
No semantic C or assembly implementation changes were needed for these cases.

Production Init ownership, linker layout and README aggregates are unchanged.
The pending Game updater/tests remain outside this checkpoint.

## New Gates And Cases

The shared adapter comparison helper optionally checks f0-f11 low words at
`0x10005F34`, before the wrapper's unconditional f0 reload. The shadow suite
enables this check for all existing and new cases. Complete final FPR values
and known-bit masks remain checked separately, along with GPRs, Status,
save/load addresses, scratch/frame/state and output/workspace contents.

The four distance cases transmit a complete code-length tree and a complete
two-symbol literal tree. Retail instruction visits prove all three builders
ran; captured v0 at `0x100067E0` distinguishes actual distance-builder failures
from successful construction. Decoder-entry visits further prove rejection
occurred before compressed decoding for the two failure cases.

| Distance lengths | Retail outcome |
| --- | --- |
| 2, 2 | Incomplete distance tree; builder returns an error; no output |
| 1, 1, 2 | Oversubscribed distance tree; builder returns an error; no output |
| 1, 1, 1 | Accepted by retail's width-one special path; literal A succeeds |
| 0 | Empty distance tree accepted; literal A/end-of-block needs no distance |

The initial all-width-one probe was not accepted as error evidence: retail
returned success. It remains an explicit accepted-path regression instead.
The corrected mixed-width oversubscription supplies the verified error gate.

Eight further streams begin with a successful nonfinal dynamic A block:

- Another successful dynamic block: AA, six builder calls.
- Incomplete distance construction in the next block: partial A, six calls.
- Code-length repeat overflow in the next block: partial A, four calls.
- Reserved block type after the first block: partial A, three calls.
- Invalid dynamic literal-count header: partial A, three calls.
- Stored XY followed by another dynamic block: AXYA, six calls.
- Fixed BC, empty stored alignment, then dynamic success: ABCA, six calls.
- The same fixed/stored history followed by repeat overflow: partial ABC,
  four calls, preserving the code-builder snapshot of historical values.

The test constructs bit-contiguous blocks without padding between compressed
blocks. It checks retail builder call counts and expected output/result before
comparing compiled variants. No missing-gate output is treated as evidence.

## Costs And Ownership Boundary

All six fresh shadow images retain Note 823's measured costs: smallest combined
text is 4,896 bytes, 912 over retail's 3,984-byte region. Its observed/bounded
core-call descent is 3,256 bytes; the largest tested shape remains 3,272 bytes.
The 116-byte state and 320-byte adapter are unchanged.

A scoped source inspection identifies concrete addresses for the next ownership
audit, not an allocation proof:

- `init_5AB0.s` at `0x10005E1C..0x10005E2C` switches to `D_80032B18`, saving
  the prior SP there and allocating the 0x80 GPR context. The later 0x88 FPR/
  Status context places the core caller SP at `0x80032A10`.
- `undefined_syms_auto.txt` assigns `D_80031AE0` and `D_80032B18` their named
  addresses. `variables.h` types the former as OSThread, and `init_1050.c`
  creates thread 3 in it. It is a live object, not generic scratch storage.
- The lowest observed shadow SP is `0x80031D48`, calculated from the caller SP
  minus the 3,272-byte maximum descent. This must be checked against the actual
  guest-sized thread object, other storage and all relevant writers.

The raw address gap does not authorize extra stack allocation. The startup BSS
segment is not an explicit reservation manifest, and no hardware execution or
complete storage-owner audit is claimed here.

## Verification And Next

The full shadow/default-adapter/provenance suite was freshly compiled and run.
All 19 tests pass in 239.549 seconds, including the eight-test shadow suite.
Compiler, assembler and linker logs remain empty. Root `make tools-check`,
Python syntax checks and `git diff --check` pass. No production build,
all-project regression run or full compiled shadow corpus is claimed.

- [x] Qualify distance-builder rejection with instruction/return-value gates.
- [x] Qualify empty and width-one special distance outcomes.
- [x] Qualify multiple dynamic blocks and intermediate fixed/stored history.
- [x] Check core-return scratch FPRs before the wrapper can overwrite f0.
- [ ] Run full retail corpus through the shadow adapter, particularly CU1-set.
- [ ] Verify guest OSThread size and complete original storage-owner boundaries.
- [ ] Fit corrected code plus entry adapters before production conversion.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_fpr_shadow tools.tests.test_init_decompressor_guest_adapter tools.tests.test_init_decompressor_fpr_provenance -v -f
```
