# Init ABI Seed Pointer Cursor And Ordered Register Copy

Date: 2026-10-03. Baseline: `5683f10`.

## Result

Opt-in `--abi-seed-cursor` copies six saved words from the physical frame
to `abiSaved` through source/destination pointers. The loop terminates at
the six-word destination end. The indexed loop remains the default;
the new flag requires `--abi-fpr-shadow`, which already requires frame backing.
The later twelve-FPR snapshot capture is unchanged.

Frame-backed O2 linked text shrinks 64 bytes. Aligned and packed O2 text
stay unchanged, but both save eight bytes of stack descent. O1 linked text
grows 32 bytes in frame/aligned and 16 in packed, with unchanged bounds.
This is an opt-in profile tradeoff, not a universal smaller replacement.
Best packed O2 remains 4,784 linked bytes, 800 over the retail 3,984-byte
decoder group; no production conversion is claimed.

## Packed Trials

All trials include the Note 852 C options and use core-only size/bounds:

| Trial | O2 bytes / bound | O1 bytes / bound |
| --- | ---: | ---: |
| Note 853 C baseline | 4,480 / 400 | 5,888 / 352 |
| Seed and capture pointer cursors, rejected | 4,480 / 392 | 5,936 / 352 |
| Seed-only end-pointer cursor, retained | 4,480 / 392 | 5,904 / 352 |
| Seed-only countdown cursor, rejected | 4,480 / 392 | 5,920 / 360 |

Only the seed end-pointer option remains. Both-copy and countdown forms
have size evidence only, not semantic qualification. Packed O2 core frame
shrinks 32 to 24 bytes; its body stays 52 words, while final padding absorbs
surrounding layout changes. Packed O1 core grows 81 to 86 body words;
its frame stays 56 bytes. Rejected selectors/source branches are removed.

Ignored trial receipts: `conker/build/init-abi-copy-cursor-20261003`,
`init-abi-seed-cursor-20261003`, `init-abi-seed-countdown-20261003`.
Final receipts and linked images live in `init-abi-seed-final-{frame,aligned,packed}-20261003`.
Final links use the unchanged Note 853 core-owned-state adapter, 296-byte
body / 304-byte aligned text and 0x98 extra stack area. State remains 116 bytes.

## Costs

| Shape/profile | Linked bytes | Static total descent | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,952 | 3,272 | 3,272 |
| Frame O1 | 6,416 | 3,208 | 3,208 |
| Aligned/end O2/g3 | 4,800 | 3,224 | 3,224 |
| Aligned/end O1 | 6,208 | 3,184 | 3,184 |
| Packed/remaining O2/g3 | 4,784 | 3,240 | 3,240 |
| Packed/remaining O1 | 6,208 | 3,200 | 3,200 |

Packed O2 static minimum SP is `0x80031D68`, 88 bytes above the known
protected neighbor ending `0x80031D10`. Complete reservation ownership,
hardware faults and real scheduler/resume remain separate open gates.

## Ordered Seed Gate

A direct fixture records the first six actual frame reads in
`frame + 0xA48 .. 0xA60` and first six state writes in
`state + 40 .. 64`. All six builds read the saved words in ascending order
and write identical values in the same order, exactly four bytes per access.
The empty stored stream completes normally. The option's missing-shadow
configuration is rejected before compiling. These two direct gates pass
in 4.420 seconds.

The inherited domain retains poisoned core-owned fields and read-before-write
checks, 492 bounded stream/context comparisons, 114 direct builders, six
exact initializers and 48 direct header/alignment comparisons. It also
retains active repeat/overflow, stored-complement, nested lookup and byte
rewind gates. Copy-order proof does not assert asynchronous intermediate
state, hardware or complete ownership equivalence.

## Final Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_abi_seed_cursor
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl python3 -m unittest tools.tests.test_init_decompressor_core_owned_state.InitDecompressorCoreOwnedStateTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_core_owned_state.InitDecompressorCoreOwnedStateTests.test_adapter_omits_six_initializers_and_poison_gate_is_active
wsl make tools-check
git diff --check
```

Final module: 27 tests in 246.100 seconds, 26 pass and one intentional
full-corpus skip. All 492 bounded contexts, 114 builders, six initializers
and 48 direct header/alignment comparisons pass. Nested lookup retains
3,212 calls / 3,383 iterations; rewind retains 11 bits / one byte / three
remaining. All six observed stack descents equal their static bounds.

Thirteen call-analysis/slot-ledger tests pass in 0.096 seconds; two selected
omitted-option regressions pass in 6.378 seconds. Across these final commands,
41 tests pass and one skips. Compiler/linker logs are empty; tool and diff
checks pass. No production build, ordinary full-suite, changed full corpus,
hardware replay or sibling-port test is claimed.

## Next

- [x] Remove both-copy and countdown trials.
- [x] Prove six ordered seed reads/writes and reject the unsupported flag combination.
- [x] Rerun the full bounded module and record all six observed costs.
- [ ] Continue structural fitting; best linked O2 excess remains 800 bytes.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and complete ownership/hardware/resume gates.

Opt-in corpus class: `InitDecompressorAbiSeedCursorCorpusTests` in
`tools.tests.test_init_decompressor_abi_seed_cursor`. It carries the new
C flag, Note 853 adapter flag and poisoned core-owned-state fixture.
It is not run here; older corpus receipts are not reassigned. Production
Init, adapter assembly, defaults and README totals remain unchanged.
Unrelated Game work is preserved and excluded.
