# Init Builder Reversed Code Toggle First Loop

Date: 2026-10-03. Baseline: `8847df9a`.

## Result

The isolated compiler supports opt-in `--builder-code-toggle`. It uses
a toggle-first loop for reversed Huffman-code increment. Packed O2 public
builder shrinks three words, 341 to 338; aligned object padding absorbs
the saving, so packed linked text remains 4,736 / 752 over retail. Packed
O1 public builder shrinks five words, 501 to 496, saving 16 linked bytes.
All six call bounds remain unchanged. No default or production change.

This is local builder fitting and some profile text saving, not a new
smallest packed O2 total. Notes 862/863 qualify the omitted-option source;
they are not assigned to this changed code even where text size is equal.

## Source And Equivalence

After `next = 1u << BUILD_SHIFT(bits - 1)`, the opt-in loop is:

```c
do {
    code ^= next;
    if (code & next) break;
    next >>= 1;
} while (next != 0);
```

The original clear-while-set loop plus final XOR remains under `#else`.
The new loop clears already-set bits and continues; at the first unset
bit, XOR sets it and the loop exits. For the all-ones code, the mask reaches
zero after clearing the last bit, leaving code zero. The original final
zero-mask XOR is a no-op. Both terminal code and mask are identical.
The bounded builder has widths 1..16 and an initially zero code; widths
only increase as the histogram is scanned. No higher code bits are introduced.

The rewrite touches local unsigned values only. It does not alter table
stores, allocation, leaf operation/value selection, signed stale-symbol
classification, prefix offsets, incomplete/oversubscribed handling,
parent ascent, state/FPR capture or adapter source. No malformed-input
fix, defensive early return or new scheduling-word guard is introduced.

## Measurements

Complete Note 861 configuration plus `--builder-code-toggle`, with the
same 296-byte body / 304-byte aligned ABI-shadow, core-owned-state adapter:

| Shape / compiler | Linked text before / after | Core call bound | Total static / observed descent |
| --- | ---: | ---: | ---: |
| Frame / O2 g3 | 5,888 / 5,888 | 424 | 3,272 / 3,272 |
| Frame / O1 | 6,368 / 6,336 | 360 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,768 / 4,752 | 376 | 3,224 / 3,224 |
| Aligned end / O1 | 6,144 / 6,128 | 336 | 3,184 / 3,184 |
| Packed remaining / O2 g3 | 4,736 / 4,736 | 392 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,160 / 6,144 | 352 | 3,200 / 3,200 |

Packed public builder words/frame are 338/200 in O2 and 496/120 in O1.
The O2 builder region includes the unchanged 22-word ABI-capture and
50-word lookup helpers: 338 + 22 + 50 = 410 words. Public builder still
exceeds the 293-word retail slot by 45 words. Saved public words are not
claimed as saved aggregate words where padding absorbs them.

Ignored initial measurement objects, logs and disassembly:
`conker/build/init-builder-code-toggle-20261003`. This first trial compiled
the direct replacement before it was placed behind the option; the final
guest suite freshly compiles/links the flagged source for all six shapes.

## Verification

`tools/tests/test_init_decompressor_builder_code_toggle.py` inherits the
offset-sum bounded suite, including direct builder comparisons, fixed
initializers, ordered prefix/repeat stores, malformed paths, ABI context,
poisoned core-owned initialization, nested lookup and header alignment.
Its size gate requires the exact packed public-body/frame and total/call
bound pairs above, not merely a smaller text section.

A separate host algebra gate compares both terminal code and mask for
all 131,070 code values across widths 1..16, including every rollover.
It passes; this is finite-domain arithmetic verification, not an additional
131,070 MIPS executions. Compiled behavior is covered by the guest suite.

Fresh guest run: thirty tests in 251.697 seconds, 29 pass and one
intentional full-corpus skip. All six observed descents equal their static
bounds. The inherited 504 context comparisons, 132 direct builders, six
fixed initializers, 48 direct header-alignment executions, ordered prefix
and repeat stores, nested lookup and failure paths pass. The independent
host algebra gate was added after this run loaded and executed separately
with the helper/baseline checks below; it is not claimed in this run's count.

The algebra gate plus thirteen call/ledger helpers and omitted-option size
gate pass together: fifteen tests, 4.088 seconds, no skips. Final combined
coverage is 44 pass / one skip. Tool and diff checks pass. A fresh compile
without `--builder-code-toggle` in
`conker/build/init-code-toggle-omitted-option-20261003` reproduces the
qualified Note 861 baseline. GNU objcopy extraction and cmp against
`init-builder-offset-reuse-available-20261003` confirm both O2 and O1
`.text` sections are byte-identical, not just equal in length. This is not
an entire-object or production-ROM claim.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_builder_code_toggle -v -f
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_builder_offset_sum.InitDecompressorBuilderOffsetSumTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_builder_code_toggle.InitDecompressorBuilderCodeToggleTests.test_exhaustive_reversed_code_increment_widths -v
wsl make tools-check
git diff --check
```

No current-option full corpus, production build, hardware replay or
sibling-port test is claimed. README totals stay unchanged; unrelated
Game edits remain preserved and excluded from this checkpoint.

## Next

- [x] Measure toggle-first reversed-code increment and retain it only as opt-in.
- [x] Check every bounded code/mask pair and preserve omitted-option text.
- [x] Finish fresh compiled guest qualification before banking the option.
- [ ] Continue builder/shared-helper fitting; packed O2 excess stays 752 bytes.
- [ ] Qualify the changed selected combination's corpus before promotion.
- [ ] Complete other-profile, ownership, hardware and scheduler-resume gates.
