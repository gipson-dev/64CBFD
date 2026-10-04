# Init Builder Table Derived Allocation Fitting

Date: 2026-10-03. Baseline: `7f08671c`.

Follow-up: [Note 871](871-init-allocation-table-full-masked-cu1-clear-corpus-20261004.md)
qualifies all 507 packed-remaining O2/g3 pages with exception-masked CU1 clear
on the unchanged retained combination. [Note 872](872-init-allocation-table-full-masked-cu1-set-corpus-20261004.md)
adds the matching CU1-set run: 1,014 paired pages across both masked modes.

## Result

Opt-in `--builder-allocation-table` carries the newly allocated table
directly in `table`, derives its header index as table - 1, and commits
allocated = table + size. Packed O2 core text falls 4,416 to 4,400; linked
text is 4,704, 720 over retail. Public builder falls 336 to 333 words.
Packed O1 text/bound hold and its public builder falls 497 to 496.
All six call bounds remain unchanged from Note 866.

The original path remains the default. This is isolated fitting, not a
production conversion or current-option full-corpus qualification.
Production/defaults/README totals stay unchanged.

## Allocation Dataflow

The selected option emits:

```c
table = BUILD_ALLOCATED + 1;
*link = table;
link = &ENTRY_VALUE(&BUILD_WORKSPACE[table - 1]);
*link = 0;
SET_TABLE(s, level, table);
/* Existing conditional parent fields use table as the new value. */
BUILD_ALLOCATED = table + size;
BUILD_COMMIT_ALLOCATION;
```

`BUILD_NEW_TABLE` selects table only for this option and next otherwise;
the existing link/parent expressions use that alias. The default keeps
its original post-link allocation reload, table = next, and += size + 1.
Both paths retain the same store order: previous link, new header clear,
table pointer, conditional parent fields, then allocation commit.

Unsigned table - 1 recovers the captured old allocation; table + size is
old allocation + size + 1 modulo 32 bits. The option eliminates allocation
reloads after link/parent writes. Its domain keeps state, workspace and
physical frame storage separated; this is not arbitrary alias or asynchronous
observation equivalence. No width, size, link ownership, root, parent-ascent,
code increment, stale-word or malformed-input classification change is made.

## Trials And Costs

Complete Note 866 packed configuration, unchanged core-owned ABI-shadow
adapter (296 body / 304 aligned bytes), state 116 bytes:

| Allocation path | O2 core / bound / public builder | O1 core / bound / public builder |
| --- | ---: | ---: |
| Note 866 baseline | 4,416 / 392 / 336 | 5,840 / 352 / 497 |
| Direct table, old allocation reload/commit | 4,416 / 392 / 335 | 5,840 / 352 / 496 |
| Table-derived header and commit, selected | 4,400 / 392 / 333 | 5,840 / 352 / 496 |

The direct-table-only trial saves public words but no aligned total.
The selected path adds the header/commit derivation. It is the only new
selector; no separate direct-only option survives. Packed builder frames
remain 200 O2 / 120 O1. O2 region is 333 + 22 ABI-capture + 50 lookup =
405 words; public builder still exceeds the 293-word retail slot by 40.

Fresh linked six-shape measurements:

| Shape / compiler | Linked text before / after | Core call bound | Total static / observed descent |
| --- | ---: | ---: | ---: |
| Frame / O2 g3 | 5,856 / 5,840 | 424 | 3,272 / 3,272 |
| Frame / O1 | 6,352 / 6,336 | 360 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,736 / 4,736 | 384 | 3,232 / 3,232 |
| Aligned end / O1 | 6,144 / 6,128 | 344 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,720 / 4,704 | 392 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,144 / 6,144 | 352 | 3,200 / 3,200 |

No profile grows text or stack relative to Note 866. Its inherited aligned
stack penalty relative to earlier variants remains; this does not erase it.
Packed minimum-SP bound stays 0x80031D68 with 88-byte known-neighbor
clearance, not complete reservation/hardware safety proof.

Ignored initial direct-source measurement directories:

- `conker/build/init-allocation-direct-table-20261003`
- `conker/build/init-allocation-derived-table-20261003`

Final tests freshly compile/link the flagged source for all six shapes.

## Active Allocation Observer

The first observer incorrectly assumed retail writes FPR19 after every
allocation. An isolated gate fails (1.769 seconds), and its already-loaded
full run stops after 22 tests in 179.099 seconds: 20 pass, one skip, one
assertion failure. This is a harness expectation error, not a suppressed
decoder mismatch. Assembly inspection identifies the actual lifetime:

- 0x10006998 loads FPR19 into s3.
- 0x10006C34 adds table size to s3.
- 0x10006C38 adds the header slot, completing each allocation update.
- 0x10006DB8 writes s3 to FPR19 once at function return.

The corrected observer asserts that exact word 0x26730001 occurs only at
0x10006C38, executes it normally, then records register 19 (s3). The compiled
fixture records each four-byte store to state + 28 after construction.
Complete [1,2,3,3] and depth-16 trees with root width one and incoming
allocation 11 require multiple retail updates. All twelve compiled executions
across six builds must match the full ordered update sequence, final FPR19
and return value. This gate passes in 2.297 seconds.

## Verification

Fresh corrected whole guest run: 33 tests in 253.827 seconds, 32 pass and
one intentional full-corpus skip. All six observed descents match static
bounds; packed minimum SP and known-neighbor clearance remain observed
0x80031D68 and 88 bytes. The inherited 504 context comparisons, 132 direct
builders, six fixed initializers, 48 direct header-alignment executions,
131,070 host code/mask pairs, ordered prefix/repeat writes, root descent
and failure gates pass, alongside the new allocation observer.

Thirteen call/ledger helpers and omitted-option size pass: fourteen tests,
1.989 seconds, no skips. Final combined count is 46 pass / one skip,
excluding the earlier failing and isolated observer runs. A fresh omitted-option compile in
`init-allocation-table-omitted-option-20261003` reproduces Note 866's O2/O1
text sections byte-for-byte against the initial offset-cursor receipts,
verified with GNU objcopy and cmp. This is not an entire-object or ROM claim.
Tool and diff checks pass.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_builder_allocation_table -v -f
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_parent_ascent_cursor.InitDecompressorParentAscentCursorTests.test_packed_profile_size_reduction -v
wsl make tools-check
git diff --check
```

No changed-option full corpus, production build, hardware replay or sibling
port test is claimed. Notes 862/863 remain scoped to the earlier source
without toggle-first, parent cursor or table-derived allocation. Unrelated
Game work remains preserved and excluded.

## Next

- [x] Measure direct-table and table-derived allocation forms.
- [x] Correct the observer to the actual retail counter lifetime and compare ordered updates.
- [x] Finish fresh corrected guest qualification before banking the option.
- [x] Qualify all 507 current packed-remaining O2/g3 corpus pages with masked CU1 clear (Note 871).
- [x] Qualify the current combination's full masked CU1-set corpus (Note 872).
- [ ] Continue fitting; packed linked excess remains 720 bytes.
- [ ] Qualify changed selections and other-profile/ownership/hardware/resume gates before promotion.
