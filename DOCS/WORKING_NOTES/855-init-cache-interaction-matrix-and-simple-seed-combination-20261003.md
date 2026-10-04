# Init Cache Interaction Matrix And Simple Seed Combination

Date: 2026-10-03. Baseline: `472c929`.

## Result

A bounded 32-combination packed compiler matrix adds five existing options
to the Note 854 flags. Only adding `--builder-simple-operation` gives the
smallest O2 text with the baseline stack bounds and smallest O1 text.
This combines the existing Note 847 arithmetic operation selection with
the later decoder/seed changes; neither compiler defaults nor source bodies
change this turn. The combined behavior gets its own fresh qualification.

All three O2 linked shapes save 16 bytes. O1 frame/aligned save 32 bytes;
packed O1 saves 16. Best packed O2 is now 4,768 bytes, 784 over retail's
3,984-byte group. All static stack bounds remain unchanged from Note 854.
This is isolated fitting progress, not a production conversion.

## Matrix Domain

Base flags are the Note 854 packed/remaining configuration, including
histogram/fixed cursors, masked dispatch/byte rewind, packed header, shared
stored/dynamic extraction, ABI seed cursor and FPR shadow.

The five independent matrix bits are:

| Bit | Existing option |
| ---: | --- |
| 1 | `--cache-workspace` |
| 2 | `--local-allocated` |
| 4 | `--cache-leaf-table` |
| 8 | `--cache-dynamic-lengths` |
| 16 | `--builder-simple-operation` |

Each mask 0..31 compiles freshly with both O2/g3 and O1: 64 object receipts.
These are size/frame measurements only; qualification is assigned to mask 16.
Representative results, including all equal-minimum-O2 masks:

| Mask | O2 core bytes / bound | O1 core bytes / bound |
| ---: | ---: | ---: |
| 0, baseline | 4,480 / 392 | 5,904 / 352 |
| 16, selected | 4,464 / 392 | 5,888 / 352 |
| 18 | 4,464 / 400 | 5,904 / 352 |
| 20 | 4,464 / 400 | 5,904 / 360 |
| 22 | 4,464 / 408 | 5,920 / 360 |
| 24 | 4,464 / 424 | 5,888 / 352 |
| 28 | 4,464 / 432 | 5,904 / 360 |
| 15 | 4,512 / 448 | 5,952 / 368 |
| 31 | 4,496 / 448 | 5,920 / 368 |

Other cache combinations have no size/stack advantage over mask 16. A fresh
receipt re-reading asserts mask 16 is no worse on all four metrics (O2/O1
text and O2/O1 call bound) than every other mask.
Full ignored receipts are under `conker/build/init-cache-interactions-{0..31}-20261003`.
Final all-shape receipts and `*-core-owned.elf` images are under
`init-simple-seed-final-{frame,aligned,packed}-20261003`. They use the
unchanged Note 853 adapter: 296-byte body / 304-byte aligned text.

## Linked Costs

| Shape/profile | Linked bytes | Static total descent | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,936 | 3,272 | 3,272 |
| Frame O1 | 6,384 | 3,208 | 3,208 |
| Aligned/end O2/g3 | 4,784 | 3,224 | 3,224 |
| Aligned/end O1 | 6,176 | 3,184 | 3,184 |
| Packed/remaining O2/g3 | 4,768 | 3,240 | 3,240 |
| Packed/remaining O1 | 6,192 | 3,200 | 3,200 |

State remains 116 bytes. Packed O2 minimum-SP bound remains `0x80031D68`,
88 bytes above the known protected neighbor ending `0x80031D10`.
That fence is not complete reservation ownership or hardware/resume proof.

## Boundary And Stale-Word Gate

Three direct builder cases add 18 paired comparisons across six builds:
symbols 254/255, symbols 255/256 and an incomplete `[0,2,2]` tree that
consumes a stale sorted word. The signed `0xA5A5A5A5` value classifies as
a literal, not an extra/base lookup. Expected operations/values are:

- 254/255: `(16,254)`, `(16,255)`.
- 255/256: `(16,255)`, `(15,256)`.
- Incomplete physical table: `(16,1)`, `(16,0xA5A5)`, `(16,2)`, `(99,0xA5A5)`.

Paired return/state/full-table/frame checks pass; separate compiled executions
also assert these explicit table cells. The isolated gate passes in
2.473 seconds. Direct builder comparison count rises from 114 to 132.

Inherited tests retain 492 bounded stream/context comparisons with poisoned
core-owned fields, six exact fixed initializers, 48 direct header/alignment
comparisons, ordered seed copies and active repeat/overflow, nested lookup,
stored-complement and byte-rewind gates.

## Final Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_simple_seed_combination
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl python3 -m unittest tools.tests.test_init_decompressor_abi_seed_cursor.InitDecompressorAbiSeedCursorTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_abi_seed_cursor.InitDecompressorAbiSeedCursorTests.test_seed_copies_six_ordered_saved_register_words
wsl make tools-check
git diff --check
```

Final module: 28 tests in 241.600 seconds, 27 pass and one intentional
full-corpus skip. All 492 bounded contexts, 132 direct builders, six exact
initializers and 48 direct header/alignment comparisons pass. Explicit
literal/EOB/stale cells and ordered seed-copy gates pass. Nested lookup
retains 3,212 calls / 3,383 iterations; byte rewind retains 11 bits / one
byte / three remaining. All six observed stack descents equal their bounds.

Thirteen helper/slot-ledger tests pass in 0.033 seconds; two selected
seed-only omitted-option regressions pass in 3.393 seconds. Across these
final commands, 42 tests pass and one skips. Compiler/linker logs are empty;
tool/diff checks pass. No production build, ordinary full-suite, changed
full corpus, hardware replay or sibling-port test is claimed.

## Next

- [x] Measure all 32 cache/builder combinations on both packed profiles.
- [x] Select mask 16 and qualify literal/EOB/signed-stale boundaries.
- [x] Rerun the full bounded module and record all six observed costs.
- [ ] Continue structural fitting; best O2 excess is 784 bytes.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and remaining ownership/hardware/resume gates.

Opt-in corpus class: `InitDecompressorSimpleSeedCombinationCorpusTests`
in `tools.tests.test_init_decompressor_simple_seed_combination`, carrying
the selected C flags and Note 853 adapter/poison fixture. It is not run
here; older corpus receipts are not reassigned. Production Init, source
bodies, adapter, defaults and README totals remain unchanged. Unrelated
Game work is preserved and excluded.
