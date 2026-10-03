# Init Builder Operation Selection Fitting And Rejected Dataflow Trials

Date: 2026-10-03. Baseline: `46c0d4d`.

## Result

An opt-in `--builder-simple-operation` forms the simple-symbol operation as
`15 + ((int32_t)symbol < 256)` instead of a ternary selection. The enclosing
signed comparison against `simple` remains unchanged. Both forms yield 16
for the literal class and 15 for the end-marker class, including retail's
signed classification of stale sorted words. Value truncation and all scratch
stores remain intact. Original source shape remains the default.

All 420 bounded stream/context comparisons and 114 direct builder comparisons
pass across six fresh shapes/profiles. Frame O2 linked text shrinks by 32 bytes;
aligned O2 by 16; all three O1 builds by 16. The best packed O2 linked size is
still 4,864 bytes: its two-word builder reduction is absorbed by trailing
alignment padding. The remaining excess over retail stays 880 bytes.

This is actual fitting progress for alternate profiles and builder-body size,
not a production conversion or a reduction of the best linked O2 total.

## Size-Only Trials

All packed trials add to the established frame/packed, bounded shifts/scans,
no-unroll, dynamic cursor, cached counts/offsets, remaining-symbol cursor,
FPR shadow, shared lookup and histogram cursor flags.

| Trial | O2 core text | O1 core text | O2 core frame bound | O1 core frame bound |
| --- | ---: | ---: | ---: | ---: |
| Histogram baseline, freshly compiled | 4,544 | 5,920 | 408 | 344 |
| Local prefix sum, indexed stores | 4,544 | 5,920 | 416 | 344 |
| Local prefix sum, pointer cursors | 4,544 | 5,952 | 424 | 352 |
| Cached current-level prefix code | 4,560 | 5,904 | 408 | 344 |
| Arithmetic simple operation, retained | 4,544 | 5,904 | 408 | 344 |
| Match-copy length countdown alone | 4,544 | 5,920 | 408 | 344 |
| Countdown plus arithmetic operation | 4,544 | 5,904 | 408 | 344 |

Prefix-sum, cached-prefix-code and countdown flags/source branches are removed.
No semantic qualification is claimed for those rejected variants. Existing
workspace/allocation/byte-parent trials were consulted in Notes 811/812/828;
their completed matrices were not rerun as new work.

Ignored receipts remain under `conker/build/init-prefix-{sum,cursor,code}-20261003`,
`init-simple-operation-20261003`, `init-match-countdown-{alone,simple}-20261003`
and `init-simple-baseline-20261003`.

## Qualified Costs

Final retained-flag builds have 116-byte state and the unchanged 320-byte
adapter. Terminal bounded receipts:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,080 | 3,280 | 3,280 |
| Frame O1 | 6,416 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,880 | 3,240 | 3,240 |
| Aligned/end O1 | 6,208 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,864 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,224 | 3,192 | 3,192 |

Compared with Note 844, stack bounds are unchanged in all six profiles.
Packed O2 retains minimum SP `0x80031D58` and 72-byte clearance above the
known protected neighbor. That is not complete reservation ownership.

Fresh packed object accounting explains the rounded totals:

- O2 builder public unit: 345 to 343 words. Enclosing slot: 417 to 415,
  including the same 72 helper words. Core body remains 60 words, but its
  slot grows from 60 to 62 with trailing padding: net text change zero.
- O1 builder public unit: 504 to 499 words. Enclosing slot: 579 to 574,
  including the same 75 helper words. Core body remains 89 words; its slot
  grows from 91 to 92: net text reduction four words / 16 bytes.

An isolated O2 linked-image comparison against the earlier histogram receipt
is not byte-identical (833 code words differ). Equal text size is not code
identity; no previous full-corpus receipt is reassigned to this opt-in form.

## Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_simple_operation
```

Terminal result: 16 tests in 191.120 seconds, 15 pass and one intentional
full-corpus skip. Setup freshly compiles and links all six selected images;
compiler and linker logs are empty.

The subclass reuses 348 shadow plus 72 masked comparisons, checking output,
state, saved GPR/FPR context, scratch FPR snapshots, modeled Status behavior,
physical scratch/workspace, DMA input bounds and neighbor guards. It also
reuses 19 direct builder cases across six builds: 114 paired comparisons for
zero count, empty/incomplete/oversubscribed trees, full symbol capacity, depth
sixteen, allocation offsets and explicit base/extra arguments. The separate
nested lookup gate reports 3,212 calls / 3,383 iterations on page 169.

Root `make tools-check` and `git diff --check` pass. Fresh compilation with
the new flag omitted preserves packed text/frame receipts 4,544/408 O2 and
5,920/344 O1; this is not a new default full-corpus run. No production build,
ordinary full-suite run, hardware replay or sibling-port test is claimed.

## Next

- [x] Measure prefix-sum, prefix-code and match-countdown hypotheses.
- [x] Remove rejected branches; retain arithmetic operation selection opt-in.
- [x] Qualify all six bounded contexts and direct builder boundaries.
- [ ] Continue fitting to reduce the best linked O2 total, not just rounded-away body words.
- [ ] Full corpus for this new operation option and other profiles before promotion.
- [ ] Complete outstanding reservation/hardware/resume qualification.

The default histogram variant retains its separate full masked-CU1 receipts
in Notes 845/846. This new option has bounded qualification only. Production
Init, adapter assembly, default flags and README totals are unchanged.
Unrelated Game edits are preserved and excluded from this checkpoint.
