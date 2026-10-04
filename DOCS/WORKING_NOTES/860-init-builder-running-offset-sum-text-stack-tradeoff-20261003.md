# Init Builder Running Offset Sum Text Stack Tradeoff

Date: 2026-10-03. Baseline: `6842440f`.

Follow-up: [Note 861](861-init-builder-offset-accumulator-lifetime-stack-recovery-20261003.md)
reuses the existing accumulator and removes this variant's packed stack
penalty without losing its text saving. Measurements below remain the
historical Note 860 implementation, not the revised source.

## Result

The isolated compiler now supports `--builder-offset-sum`. It replaces
the prefix-offset loop's previous-offset reload with an unsigned running
sum. The original loop remains the default; production Init is untouched.

For Note 858's full packed/remaining configuration, this saves 16 aligned
O2 text bytes but increases the conservative call bound by eight bytes.
Linked text is 4,736, still 752 over retail's 3,984. This is a text/stack
tradeoff, not a dominating replacement for the 4,752-byte / 392-bound
baseline, and not promotion or byte matching. O1 text and bound hold.

## Source And Domain

```c
BUILD_OFFSETS[1] = 0;
{
    uint32_t sum = 0;
    for (bits = 1; bits < max; bits++) {
        sum += BUILD_COUNTS[bits];
        BUILD_OFFSETS[bits + 1] = sum;
    }
}
```

The empty-count and all-zero returns remain before this loop. `max` is
1..16 in the existing bounded domain. For max 1 it performs no additional
prefix stores. Unsigned addition preserves modulo-32-bit arithmetic.
Counts and offsets are separate physical frame arrays; counts[max] keeps
the retail available-slot replacement, and this loop never reads it.
Histogram, sorting, incomplete/oversubscribed classification and table
construction are unchanged. Eliminating offset reloads is not a claim of
arbitrary alias or asynchronous observation equivalence.

## Measurements

Trials use all Note 858 packed/remaining flags; only the final retained
trial adds `--builder-offset-sum`. The adapter remains 296 body bytes /
304 aligned bytes with ABI shadow and core-owned state.

| Trial | O2 core / bound | O1 core / bound | O2 builder public words / frame |
| --- | ---: | ---: | ---: |
| Unchanged baseline | 4,448 / 392 | 5,856 / 352 | 343 / 200 |
| Count-clear pointer endpoint, rejected | 4,448 / 400 | 5,856 / 352 | 345 / 208 |
| Indexed running sum, opt-in | 4,432 / 400 | 5,856 / 352 | 341 / 208 |
| Running sum with two pointer cursors, rejected | 4,448 / 408 | 5,888 / 360 | 343 / 216 |

O1 public builder words are respectively 499, 500, 501 and 507; frames are
120, 120, 120 and 128. The selected O2 builder region is 413 words, with
341 public words plus the unchanged 22-word ABI-capture and 50-word lookup
helpers. Public builder still exceeds the 293-word retail slot by 48 words.
Aligned object padding means the two public words saved yield four words
of aggregate text saving; this is not four public builder words removed.

The rejected clear loop was a do/while zero-store cursor ending at counts
+ 17. The rejected prefix loop advanced a count cursor from counts + 1
and an offset cursor from offsets + 2 until countCursor == counts + max.
Neither rejected form survives as a source branch or compiler selector.

Fresh six-shape linked text / total static and observed descent:

| Shape / compiler | Linked text | Total static / observed descent |
| --- | ---: | ---: |
| Frame / O2 g3 | 5,888 | 3,272 / 3,272 |
| Frame / O1 | 6,368 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,768 | 3,232 / 3,232 |
| Aligned end / O1 | 6,144 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,736 | 3,248 / 3,248 |
| Packed remaining / O1 | 6,160 | 3,200 / 3,200 |

The packed O2 bound implies minimum SP 0x80031D60 and 80-byte clearance
above the known neighbor ending at 0x80031D10, versus baseline's 88.
This is not proof of the full stack reservation or hardware safety.
Frame O1 grows 16 linked bytes; the option is not a universal size win.

Ignored measurement artifacts:

- `conker/build/init-builder-clear-cursor-20261003`
- `conker/build/init-builder-offset-sum-20261003`
- `conker/build/init-builder-offset-cursors-20261003`

## Verification

`tools/tests/test_init_decompressor_builder_offset_sum.py` inherits the
Note 858 bounded contexts, builder cases, fixed initialization, overflow,
repeat-fill, ABI shadow and core-owned poison gates. A new active store
observer checks the ordered prefix writes across six compiled shapes for
max depths 1, 3 and 16, including an incomplete tree: 24 executions.
The first max writes must have exactly the expected frame addresses,
unsigned cumulative values and four-byte store widths.

The first broad run stopped at an obsolete 392-byte size-test expectation
after 22 tests in 207.576 seconds: 20 pass, one corpus skip, one assertion
failure. The measured bound is 400. The expectation is corrected explicitly;
the stack increase is not concealed. A fresh whole run is required below.
The corrected size and ordered-prefix gates pass separately (2.909 seconds).
Thirteen helper tests and the omitted-option baseline size gate pass
(14 tests, 2.211 seconds). Tool and diff checks pass.

Fresh whole-run result: 30 tests in 246.963 seconds, 29 pass and one
intentional full-corpus skip. With the fourteen separate helper/baseline
checks, final coverage is 43 pass / one skip. Static descent equals observed
descent for all six shapes; packed minimum SP is observed, not just inferred.
The inherited 504 context comparisons, 132 direct builders, six fixed
initializers and 48 direct header-alignment executions pass. These are
bounded-domain checks, not the whole retail corpus or hardware proof.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_builder_offset_sum -v -f
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_dynamic_repeat_fill.InitDecompressorDynamicRepeatFillTests.test_packed_profile_size_reduction -v
wsl make tools-check
git diff --check
```

No current-option full 507-page corpus is claimed. Notes 856/857 remain
receipts for the earlier build without either repeat-value or offset-sum.
The opt-in corpus class selects the exact new combination for future runs.
No production build, hardware replay or sibling-port behavior is claimed.
README totals stay unchanged; unrelated Game work is preserved and excluded.

## Next

- [x] Measure builder initialization and prefix dataflow alternatives.
- [x] Retain the indexed sum only behind an explicit experiment option.
- [x] Check ordered prefix writes and preserve the omitted-option baseline.
- [x] Finish the fresh bounded regression run before banking this option.
- [ ] Reduce builder/shared-call text without further eroding stack clearance.
- [ ] Qualify the selected changed combination on the full corpus in both masked CU1 modes.
- [ ] Complete other-profile, ownership, hardware and scheduler-resume gates before promotion.
