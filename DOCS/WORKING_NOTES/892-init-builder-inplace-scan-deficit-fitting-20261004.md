# Init Builder In-Place Scan Deficit Fitting

Date: 2026-10-04. Starting HEAD: `3d21f2db`.

## Result

Opt-in `--builder-scan-deficit` combines the table-width scan's comparison
and subtraction. Packed O1 core text falls 32 bytes, from 5,824 to 5,792;
packed O2 stays 4,384. Both retained packed call bounds and builder frames
remain unchanged. This improves the secondary profile, not the best O2 excess.
No production conversion or compiler default changes.

The CLI requires `--bounded-builder-shifts`. The new bounded fixture selects
that flag explicitly for all six shapes; it is not inherited accidentally
only from the packed/aligned shape setup.

## Dataflow And Domain

The original scan compares `counts[scan] >= slots` and breaks before subtracting
on that path. The option uses:

```c
slots -= BUILD_COUNTS[scan];
if ((int32_t)slots <= 0) break;
```

Only the continuing path uses the updated slots in a later iteration. After
the break, table size comes from `levelBits`, not slots. The same levelBits
update and same histogram reads occur; no stores or frame accesses move.

For the bounded domain (count <= 288, widths/depth <= 16), each loaded scan
bucket is before max: scan = consumed + levelBits, and the loop requires
levelBits < ceiling <= max - consumed. Thus it never loads counts[max],
which the builder rewrites with available slots and which may wrap on an
oversubscribed tree. All sampled counts remain ordinary histogram counts
0..288. Doubled slots are positive and at most 65,536; the prior continuing
subtraction is positive and the scan depth caps doubling. The mathematical
deficit is therefore within -287..65,536. MIPS signed interpretation of its
unsigned wrapped representation gives the same break classification.
This is not an unrestricted count, invalid-depth or arbitrary alias proof.

## Measurements

| Form | O2 core / public builder / frame / call bound | O1 core / public builder / frame / call bound |
| --- | ---: | ---: |
| Baseline | 4,384 / 333 / 200 / 392 | 5,824 / 496 / 120 / 352 |
| Separate signed local, rejected | 4,384 / 333 / 208 / 400 | 5,808 / 490 / 128 / 360 |
| In-place deficit, retained opt-in | 4,384 / 333 / 200 / 392 | 5,792 / 488 / 120 / 352 |

With the unchanged 192-byte direct-load adapter, packed O1 linked text is
5,984, down from 6,016. Packed O2 remains 4,576 / 592 over retail. Reject the
separate local's stack growth; retain only the in-place opt-in form.

Ignored receipts:

- `conker/build/init-builder-scan-deficit-trial-20261004`
- `conker/build/init-builder-scan-inplace-deficit-trial-20261004`
- `conker/build/init-scan-deficit-default-check-20261004`

## Default Preservation

Fresh packed compilation without the new option matches the old baseline
whole unrelocated `.text` exactly in both profiles (objcopy extraction):

| Profile | SHA-256 |
| --- | --- |
| O2/g3 | `87164a2c6d5d2de55fbc3e46d4c0e08b50e9781474225d8a83686369b03013c7` |
| O1 | `764dc0153115aed423164610da01fc8b12bf0fd7716996c5ec98150f69e36521` |

The retained default lookup size test also passes in 2.049 seconds. Old corpus
evidence does not qualify the new option, even though O2 has the same size.

## Qualification

New tests inherit the live-SP/callee/direct-FPR bounded guest suite and add
packed size/frame assertions, CLI dependency rejection, signed-domain algebra,
and a positive executed-branch gate. The branch gate finds the unique BLEZ or
BLEZL in the public builder, executes a depth-sixteen tree and requires a
nonzero visit count across all six images. It passes in 2.551 seconds.

The algebra check covers every positive slot value through 65,536 with count
extrema and around-equality samples. It supplements the range argument; it
does not exhaust all frame histories or replace guest differential tests.

Whole bounded run: 40 tests in 268.066 seconds, 39 passes and one explicit
opt-in corpus skip. The branch-execution test was added after that process
imported the module and passed separately as above; combined, forty bounded
tests pass and one corpus test is skipped. Source/CLI did not change during
the run. No failed setup is counted as qualification: the initial run rejected
the missing bounded-shifts selection on the frame shape, then the fixture was
corrected to select it for every shape before the successful whole run.

| Shape / profile | Linked text | Static / observed stack descent |
| --- | ---: | ---: |
| Frame / O2 g3 | 5,568 | 3,256 / 3,256 |
| Frame / O1 | 6,000 | 3,176 / 3,176 |
| Aligned end / O2 g3 | 4,608 | 3,232 / 3,232 |
| Aligned end / O1 | 5,984 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,576 | 3,240 / 3,240 |
| Packed remaining / O1 | 5,984 | 3,200 / 3,200 |

Frame-shape figures also include the newly explicit bounded-shifts selector;
do not attribute that shape's entire difference to the deficit alone.
Packed O2 minimum SP remains `0x80031D68`, 88 above the known neighbor.
This is not complete reservation/ownership proof. Project tool and whitespace
checks pass. Full guarded corpus and hardware/context remain unqualified.

## Next

- [x] Measure separate-local and in-place scan deficits.
- [x] Retain only the in-place opt-in form; default text remains exact.
- [x] Confirm the changed branch executes across six compiled shapes.
- [x] Pass inherited bounded guest/ABI/live-SP suite and default size regression.
- [ ] Run full guarded corpora for the new option before assigning full-corpus credit.
- [ ] Continue best-profile fitting, full reservation, ownership and hardware/context.

Production Init, word guards, README totals, sibling-port artifacts and Release
are unchanged. Unrelated Game source/tests remain untouched and unstaged.
