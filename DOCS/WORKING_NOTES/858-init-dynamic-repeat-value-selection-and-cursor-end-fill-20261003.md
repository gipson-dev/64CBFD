# Init Dynamic Repeat Value Selection And Cursor-End Fill

Date: 2026-10-03. Baseline: `6b2d5228`.

## Result

Opt-in `--dynamic-repeat-value` selects the repeated value once after the
existing overflow gate. Code 16 retains `previous`; all other repeat codes
set it to zero. With `--dynamic-cursor`, the fill computes its destination
end once and stores until that endpoint. The non-cursor shape retains a
count loop but also selects the value once. Existing source stays the default.

Frame O2 linked text saves 32 bytes; aligned/packed O2 save 16. Every O1
shape saves 32. All six call-stack bounds stay unchanged. Smallest packed
O2 is 4,752 linked bytes, still 768 above the 3,984-byte retail group.
This is experimental structural fitting, not production conversion.

## Nonzero Repeat And Failure Contract

The literal branch handles all symbols below 16 before this path. Repeat
16/17 requests 3..6 / 3..10 lengths; the otherwise branch requests 11..138.
Thus a repeat always requests at least three slots. The overflow gate runs
before selecting/resetting `previous` or computing the destination endpoint.
After that gate, the cursor-end do/while has a nonempty bounded range.

Overflow still returns before any repeated-length store or previous-value
reset. No defensive early return or changed malformed-symbol interpretation
is added. The exhausted local repeat counter is not exported or subsequently
read; removing its countdown in cursor mode does not change final state.
Asynchronous intermediate-register/hardware equivalence remains unqualified.

## Trials

Packed measurements include the Note 855 simple-operation/seed combination:

| Trial | O2 core bytes / bound | O1 core bytes / bound |
| --- | ---: | ---: |
| Note 855 baseline | 4,464 / 392 | 5,888 / 352 |
| Select value once, count loop, superseded | 4,464 / 392 | 5,856 / 352 |
| Select value once, cursor-end fill, retained | 4,448 / 392 | 5,856 / 352 |

Packed dynamic body shrinks 261 to 256 words in O2, 319 to 311 in O1;
frames remain 104/112. The count-only trial measured 260/312 body words.
The O2 body now fits within the 257-word retail dynamic slot by size only;
this does not preserve that entry's shared-frame ABI or prove matching words.
Final padding absorbs one of the five O2 body words saved against baseline;
all eight O1 body words are reflected in the text saving. Cursor-end mode
saves one further O1 body word over the count-only trial, but padding
absorbs that word, leaving equal O1 text for those two forms.
The superseded cursor-mode count branch is removed;
non-cursor count fallback is part of the qualified final implementation.

Ignored receipts: `conker/build/init-dynamic-repeat-value-20261003`,
`init-dynamic-repeat-value-end-20261003` and
`init-dynamic-repeat-final-{frame,aligned,packed}-20261003`.
Final links use the unchanged core-owned-state adapter (296-byte body,
304-byte aligned contribution); C state remains 116 bytes.

## Linked Costs

| Shape/profile | Linked bytes | Static total descent | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 5,904 | 3,272 | 3,272 |
| Frame O1 | 6,352 | 3,208 | 3,208 |
| Aligned/end O2/g3 | 4,768 | 3,224 | 3,224 |
| Aligned/end O1 | 6,144 | 3,184 | 3,184 |
| Packed/remaining O2/g3 | 4,752 | 3,240 | 3,240 |
| Packed/remaining O1 | 6,160 | 3,200 | 3,200 |

Packed O2 minimum-SP bound remains `0x80031D68`, 88 bytes above the known
protected neighbor ending `0x80031D10`. This is not complete reservation
ownership or hardware/scheduler-resume proof.

## Ordered Fill Gate

The earlier zlib-valid repeat stream exercises codes 16/17/18 with zero
previous and repeat counts including three and 138. A new zlib-valid stream
builds four three-bit literals plus one one-bit EOB: code 16 repeats a
nonzero previous length of three, with zero fills before/after it. Both
streams decompress to `A`.

Across six builds, the gate observes all 277 ordered four-byte staging
writes: 19 code-alphabet stores followed by 258 decoded-length stores.
Both streams have exactly the expected address/value/size sequence, including
nonzero repeat 16 and minimum/maximum fills. Constructor writes are excluded
by activating observation only after fixture setup. The direct gate passes
in 8.495 seconds.

Twelve additional paired stream/context runs cover the nonzero stream in
all six builds and both masked CU1 modes. The bounded context count rises
492 to 504. Inherited repeat overflow gates remain active, alongside 132
builders, six exact initializers, 48 direct header/alignment comparisons,
ordered ABI seed copies and poisoned core-owned-state checks.

## Final Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_dynamic_repeat_fill
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl python3 -m unittest tools.tests.test_init_decompressor_simple_seed_combination.InitDecompressorSimpleSeedCombinationTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_simple_seed_combination.InitDecompressorSimpleSeedCombinationTests.test_simple_symbol_boundary_and_signed_stale_word
wsl make tools-check
git diff --check
```

Final module: 29 tests in 255.923 seconds, 28 pass and one intentional
full-corpus skip. All 504 bounded contexts, 132 builders, six initializers
and 48 direct header/alignment comparisons pass. Ordered repeat writes and
inherited overflow paths pass across both cursor and non-cursor shapes.
Nested lookup retains 3,212 calls / 3,383 iterations; rewind retains 11 bits /
one byte / three remaining. All six observed descents equal their bounds.

Thirteen helper/slot-ledger tests pass in 0.039 seconds; two selected
omitted-option regressions pass in 2.285 seconds. Across final commands,
43 tests pass and one skips. Compiler/linker logs are empty; tool/diff
checks pass. No production build, ordinary full suite, changed full corpus,
hardware replay or sibling-port test is claimed.

## Next

- [x] Measure count-only and cursor-end forms; retain smaller cursor-end form.
- [x] Prove ordered zero/nonzero fills, repeat extremes and unchanged overflow behavior.
- [x] Rerun the full bounded module and record all six observed costs.
- [ ] Continue structural fitting: smallest linked O2 excess is 768 bytes.
- [ ] Fresh changed-option full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and complete ownership/hardware/resume gates.

Opt-in corpus class: `InitDecompressorDynamicRepeatFillCorpusTests` in
`tools.tests.test_init_decompressor_dynamic_repeat_fill`. It carries the
new C flag plus the existing adapter/poison fixture. It is not run here;
Notes 856/857 remain qualification for the previous no-new-option build,
not this changed fill. Production Init, adapter, defaults and README
totals remain unchanged. Unrelated Game work is preserved and excluded.
