# Game Record Callback Update Conversion

Date: 2026-10-08

## Result

Continue [Note 1144](1144-game-record-ring-renderer-conversion-20261008.md)
using the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Install complete `func_151D7264` in
[generated_204660.c](../../conker/src/game/generated_204660.c):
VA 0x151D7264..0x151D73A8, ROM 0x204714..0x204858,
**81 words / 324 bytes / frame 0x40**. Retain the original assembly reference.

Selected semantic C emits 72 retail words directly. Nine scheduling words
are derived by a closed normalizer and installed as expected-word guards;
this is **not a direct guard-free match**. All seven relocation-bearing words
remain unchanged. Fresh linked audit confirms **81 / 81 retail words**, zero
differences or drift, and **every byte of the complete ELF unchanged**:
SHA-256 `f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
All 6,058 symbols' bodies, addresses and extents, including protected data,
remain unchanged. Exactly one progress row changes asm -> c, adding 324 C bytes.
The manifest preserves the old 11,460 guards as an identical byte prefix and
adds exactly nine, for **11,469**. Makefile and original assembly are unchanged.

| Section | Converted | Converted bytes | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,483 / 6,042 (90.75%) | 1,937,984 / 2,256,728 (85.88%) | 3,394 / 5,483 (61.90%) | 0 | 2,089 |
| Init | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,810 / 5,321 (90.40%) | 1,766,548 / 2,072,880 (85.22%) | 2,721 / 4,810 (56.57%) | 0 | 2,089 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

The 6,042 main progress slots exclude 16 linked overflow symbols. Raw CSV has
6,044 records because two section headers repeat. Root README changes only
the four affected aggregate rows; function narrative belongs here.

## Recovered Contract

The target has a void contract; no meaningful V0 return value is claimed.
Capture owner XYZ at +0x30/+0x34/+0x38 and bit 0 of +0x2D before invoking
the `D_8008FCA0` callback indexed by `owner[0x2C]`, passing owner itself.
Selector +0x2C is unsigned. Do not invent a
null-callback guard or claim every possible selector is valid in the retail table.

Callback failure writes signed halfword -1 at +0xE and ORs byte +0xD with 1.
Preserve the emitted read of byte +0xD before that halfword store. On success,
observe the callback's current flag, position, threshold and attachment changes.
If either current or captured flag is clear, call `func_151D77C8`.
Otherwise calculate current minus captured XYZ, pass that delta to
`func_15143E64`, and compare its single-precision length strictly below the
live threshold at +0x3C. False, equal and unordered comparisons clear the
attachment. A true comparison keeps an existing attachment or calls
`func_151D7830` if the live slot at +0x28 is null. The length helper may change
the live threshold or slot; those reads must remain after its call.

Keep the owner+0x28 pointer in private frame slot +0x1C across the length call,
delta at +0x20..+0x28, captured flag at +0x2F and position at +0x30..+0x38.
The incoming owner home is +0x40; RA is +0x14. Qualification distinguishes
owned stack state from public memory and does not claim raw/retail private
fault-state identity.

## Fitting And Closed Normalization

The natural complete form is 81 words/frame0x40 with 19 differences. A typed
record form reduces this to 17; 24 actual declaration permutations fit the
selected record/previous/flag/delta order to nine. Test 60 complete forms and
seven effective compiled semantic negatives. An exploratory volatile-owner
form changes public read order and is not selected even when logical outputs agree.

| Profile | Words | Frame | Raw differences |
| --- | ---: | ---: | ---: |
| O2 g3, selected | 81 | 0x40 | 9 |
| O2 | 79 | 0x40 | 77 |
| O1 g3 | 84 | 0x38 | 77 |
| O1 | 84 | 0x38 | 78 |

No production compiler profile change. The
[candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_callback_update_candidates.py)
requires the complete 81-word extent, frame word and exact nine input words
at +0x78..+0x98. Move the pure owner+0x28 calculation ahead of the current-flag
load; derive that load's new base/offset from the input word. Retarget the two
moved branch immediates by one while preserving their destinations. Exchange
the private captured-X/current-X loads around the old-flag branch delay slot.
No retail-word lookup, inserted/omitted words, padding or FP register renaming.
All seven relocated words lie outside this block and remain unchanged.

Reject all nine stale expected guards, wrong extent and ineffective partial
normalizations. Omitting the moved pointer causes a real unmapped read;
omitting the current-flag gate is witnessed by captured flag 1 followed by a
callback clearing the live flag. Neither witness depends on budget exhaustion
or an unsupported opcode. Public access order is qualified separately from
private stack-load boundaries and hardware fault metadata.

## Qualification

The [11-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_callback_update_match.py)
reuses existing numeric execution and domain helpers, with a separate typed
reference. It does not introduce a new instruction emulator.

- **3,360 cases / 10,080 executions** compare raw C, normalized C and retail.
  Cover all 256 selectors through a fabricated valid callback table, six flag
  values, zero/nonzero callback returns, nine callback/length mutation modes,
  strict FP edges, null/nonzero attachments and both stack phases. All 81
  target words are reached. Normalized/retail complete model state agrees;
  raw public memory/access prefixes and canonical calls agree with the reference.
- **624 real missing-byte pairs** and 32 lazy trimmed cases qualify fault
  prefixes and complete normalized/retail model state, not portable invalid
  C access or hardware CP0/FCSR traps.
- **67,736 native 32-bit C cases** use actual GCC-compiled static C, a volatile
  callback pointer and 512-byte canaries. Cover all 65,536 flag/selector pairs,
  every failure-byte value and live mutations. Callback and distance stubs
  are bounded; this does not qualify an actual native square-root routine.
- **120 cases / 360 executions** connect actual linked table slots 2/3/4:
  complete 19/11/11-word callbacks, 12-word magnitude and 26-word attached
  clear. Qualify concrete clear writes and both stack phases. Retail table
  slots 0/1 are not yet qualified by this connected test.
- **16 cases / 48 executions** connect complete 67-word allocation and the
  original 115-word constructor, including null/valid allocator outcomes,
  exact arguments and payload/record writes. Allocator/copy/zero remain
  bounded hooks. The production linked constructor is still a false-zero
  placeholder; executing its original body here does not restore it.
- Preserve **22 copied-owner neighbors**, pools, relative relocations and
  four existing diagnostics. Actual padder emits 324 bytes without `.space`.
  Four independent GNU symbol sets provide 144 padded execution cases, with
  table HI/LO carry controls and reference comparison. This is not a separately
  rebased original-assembly pair.
- **96 table/owner alias cases** cover failure fields, attachment, captured
  position and live threshold across four table rebases. Raw and normalized
  public prefixes/calls/memory agree with the separate reference.

Fresh pre-install **11 tests pass in 72.557s**; post-install **11 pass in
77.792s**, no skips. Installation-aware source/guard/progress/full-ELF checks
pass. Fresh 14 shared tests pass before installation in 0.242s; mounted and
older standalone project checks pass. Post-install 24 shared padder/linker
tests pass in 0.507s; both project tools checks pass again. Eight tools files
parse and match the older mirror. **131 documents / 4,125 relative links /
zero broken** pass. Prior renderer/neighbor module receipts remain historical;
they are not a fresh full renderer run. Full ELF identity covers their unchanged
production bytes, not broader runtime acceptance.

Earlier fixture failures were corrected before these clean runs: inherited
FCSR initialization, native C warning formatting, exploratory volatile-form
classification and an ineffective both-flags-zero partial-transform witness.
Do not report those earlier commands as passing. Production rebuild succeeds
with existing duplicate generated_12D630 recipe warning and existing C diagnostics.

## Receipts And Banking

Ignored receipts live in `conker/build/game-record-callback-update-test/`:
`baseline.json`, `before.elf`, `before-manifest.csv`, `installed-audit.json`,
`after.json`, `slot.json`, `guest.json`, `faults.json`, `forms.json`, `owner.json`,
`linked.json`, `native.json`, `connected.json`, `allocation.json`,
`partial-negatives.json` and `aliases.json`.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
PYTHONPATH=. python3 conker/build/game-record-callback-update-test/audit.py
make -C conker match-progress NON_MATCHING=1
python3 -m unittest tools.tests.test_game_record_callback_update_match -v
```

Per "Keep commited", bank tools
**f7272ba3c22e051c01033134fabd6d901cb07f4c** first, then parent source/manifest/
docs and that exact gitlink. Two new tools files are copied to the older mirror
only after absent-path gates and exact-byte checks. Preserve older HEAD ddbdd16,
its independently dirty shared helper/effect test and all unrelated paths;
do not reset or duplicate its history. Progress CSV, ELF, ignored receipts and
the local checker are not committed. No push requested/performed.

Manual Graphify refresh refuses 16,879 nodes over retained 38,667. Fail-closed
preservation covers 19,398 nodes from 2,972 still-existing excluded files.
Preserve the graph without force; refresh repair remains open. No OGL/Release,
runtime/save/editor, bridge or account changes. The wider Game goal stays active.

## Next Work

Next retained **func_151D75C4**, VA 0x151D75C4..0x151D7724,
ROM 0x204A74..0x204BD4: **88 words / 352 bytes / frame 0x30**.
It is actual callback table slot 0. Recover actor/pointer/type/identity gates,
joint-index and position tables, complete matrix transform and live flag update,
then signed optional secondary callback selection. Respect post-call pointer
homes and lazy reads; recover the whole routine before fitting. Its qualification
can close the slot-0 connection gate above. Table slot 1, linked setup and
hardware/gameplay acceptance remain separate. `func_151D8718` is already converted.
