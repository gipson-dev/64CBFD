# Init Builder Offset Accumulator Lifetime Stack Recovery

Date: 2026-10-03. Baseline: `7ce4f88e`.

Follow-up: [Note 862](862-init-offset-sum-full-masked-cu1-clear-corpus-20261003.md)
banks all 507 fresh pages for this revised combination with masked CU1 clear.
[Note 863](863-init-offset-sum-full-masked-cu1-set-corpus-20261003.md) banks
the matching CU1-set run: 1,014 paired pages across both modes for this
packed O2 profile. The historical bounded measurements below are unchanged.

## Result

The existing opt-in `--builder-offset-sum` now reuses the builder's
`available` variable instead of introducing a new scoped `sum` variable.
Fresh IDO compilation preserves all six text sizes from Note 860 while
recovering eight call-bound bytes in aligned O2, aligned O1 and packed O2.
Other call bounds stay unchanged. No new selector is needed; the original
non-option loop and production sources remain untouched.

Packed O2 retains 4,736 linked bytes, 752 over retail, with a restored
392-byte core call bound and 88-byte known-neighbor clearance. This removes
Note 860's packed stack penalty. It is a size/stack improvement over the
4,752-byte Note 858 packed baseline, not byte matching, slot ownership,
full-corpus qualification or hardware acceptance. Frame O1 still grows
16 text bytes relative to Note 858; it is not a universal profile win.

## Lifetime And Source

```c
incomplete = available - BUILD_COUNTS[max];
BUILD_COUNTS[max] = available;
BUILD_OFFSETS[1] = 0;
#ifdef INIT_DECODE_BUILDER_OFFSET_SUM
available = 0;
for (bits = 1; bits < max; bits++) {
    available += BUILD_COUNTS[bits];
    BUILD_OFFSETS[bits + 1] = available;
}
#else
/* Original previous-offset loop remains here unchanged. */
#endif
```

The original availability value has already been committed to counts[max]
and used to calculate `incomplete`. It has no later reader. Reusing it for
the prefix accumulator leaves the persistent count and classification
values intact. The accumulator remains unsigned, with the same modulo-32
addition and identical prefix stores; max 1 still performs no extra stores.
No histogram, sorted-symbol, table allocation, workspace, error handling,
ABI state or adapter source change is introduced. As in Note 860, removed
offset reloads are qualified in the separated physical-frame domain, not
as arbitrary alias or asynchronous observation equivalence.

The evidence is the measured compiler output, not a claim about IDO's
internal allocation algorithm. Packed O2 builder frame shrinks 208 to 200
bytes; public unit stays 341 words. The builder region still contains
22 ABI-capture and 50 lookup helper words, for 413 total. Public builder
still exceeds retail's 293-word slot by 48 words. Fitting is unfinished.

## Fresh Measurements

Adapter body/aligned text remain 296/304 bytes; state remains 116 bytes.
Total descent includes the 0xA88 retail frame and 0x98 extra adapter area.

| Shape / compiler | Linked text | Core call bound before / after | Builder frame after | Total static / observed descent after |
| --- | ---: | ---: | ---: | ---: |
| Frame / O2 g3 | 5,888 | 424 / 424 | 216 | 3,272 / 3,272 |
| Frame / O1 | 6,368 | 360 / 360 | 136 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,768 | 384 / 376 | 184 | 3,224 / 3,224 |
| Aligned end / O1 | 6,144 | 344 / 336 | 104 | 3,184 / 3,184 |
| Packed remaining / O2 g3 | 4,736 | 400 / 392 | 200 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,160 | 352 / 352 | 120 | 3,200 / 3,200 |

Packed minimum SP is 0x80031D68, above the known neighbor ending at
0x80031D10 by 88 bytes. This does not establish the full stack reservation
or real scheduler/hardware safety.

Ignored persistent compile receipt, objects, logs and disassembly:
`conker/build/init-builder-offset-reuse-available-20261003`. It uses the
complete Note 858 packed/remaining flags plus `--builder-offset-sum`.
The regression suite freshly compiles and links all six shapes with ABI
FPR shadow and core-owned state, checking empty compiler/link logs.

## Verification

The size regression now requires packed O2's 392-byte bound and 200-byte
builder frame, plus unchanged O1's 352/120. The inherited active ordered
prefix observer still covers 24 executions across all six shapes at
depth boundaries 1, 3 and 16, including an incomplete tree.

Fresh whole bounded run: thirty tests in 250.756 seconds, 29 pass and one
intentional full-corpus skip. All six observed descents match their static
bounds; the restored packed minimum SP and 88-byte clearance are observed
in this bounded suite. The inherited 504 context comparisons, 132 direct
builders, six fixed initializers, 48 direct header-alignment executions
and ordered prefix/repeat stores pass. Tool/diff checks pass.

Thirteen call-graph/ledger helper tests and the omitted-option Note 858
size gate pass: fourteen tests, 1.820 seconds, no skips. Final combined
test coverage is 43 pass / one skip. A fresh omitted-option compile in
`conker/build/init-offset-reuse-omitted-option-20261003` reproduces 4,448
O2 and 5,856 O1 core bytes. Extracting each object's `.text` with GNU
objcopy and comparing with `init-copy-refill-baseline-check-20261003`
using `cmp` succeeds for both profiles: all text bytes match, not merely
section sizes. This is not an entire-object or production-ROM claim.
The new source is
not assigned prior full-corpus receipts: Notes 856/857 are still scoped
to the older build without repeat-value or offset-sum options.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_builder_offset_sum -v -f
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_dynamic_repeat_fill.InitDecompressorDynamicRepeatFillTests.test_packed_profile_size_reduction -v
wsl make tools-check
git diff --check
```

No production build, full retail corpus, hardware replay or sibling-port
test is claimed for this bounded checkpoint; later corpus receipts are
linked above. Production/defaults/README totals stay unchanged; unrelated
Game edits are preserved and excluded from this checkpoint.

## Next

- [x] Recover the offset-sum option's extra stack cost without losing its text saving.
- [x] Finish fresh bounded qualification before banking the revised option.
- [ ] Continue builder/shared-helper fitting; 752 linked bytes remain over retail.
- [x] Run the selected revised combination's full corpus in both masked CU1 modes (Notes 862/863).
- [ ] Complete other-profile, ownership, hardware and scheduler-resume gates before promotion.
