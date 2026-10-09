# Game Record Ring Renderer Conversion

Date: 2026-10-08

## Result

Finish the complete `func_151D80C4` from
[Note 1143](1143-game-record-ring-renderer-live-value-proof-20261008.md), using
the [focused workflow](../AGENT_WORKFLOW.md). VA 0x151D80C4..0x151D8718,
ROM 0x205574..0x205BC8: **405 words / 1,620 bytes / frame 0xD0**.
Install the unchanged qualified SETUP_FITTED semantic renderer in
[generated_204660.c](../../conker/src/game/generated_204660.c).
Its unnormalized compiler output has **185 real word differences**.
The closed normalizer derives exactly 185 expected-word guards; the installed
linked routine is **405 / 405 retail words, zero differences or address drift**.
Retain the original assembly reference. This is not a direct, guard-free match.

Fresh full linked audit confirms **every byte of the complete ELF unchanged**:
SHA-256 `f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
All 6,058 symbols' bodies/addresses/extents and protected data are unchanged.
The only progress change is this 1,620-byte row, asm -> c. The manifest retains
the old 11,275-row byte prefix and adds 185 rows, for **11,460 guards**.
Makefile, original assembly and retail reference are unchanged.

Fresh aggregate measurements:

| Section | Converted | Converted bytes | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,482 / 6,042 (90.73%) | 1,937,660 / 2,256,728 (85.86%) | 3,393 / 5,482 (61.89%) | 0 | 2,089 |
| Init | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,809 / 5,321 (90.38%) | 1,766,224 / 2,072,880 (85.21%) | 2,720 / 4,809 (56.56%) | 0 | 2,089 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

The 6,042 main progress slots exclude 16 linked overflow symbols. The raw CSV
has 6,044 records because two section headers repeat. Root README changes only
its four affected aggregate rows; function narrative belongs here.

## Closed Normalization

The [pure normalizer](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_normalization.py)
requires the complete 405-word masked-source SHA-256
`8fafaaa5a9f93eb1636fb25571e4fd8dee30d6d82fb83d4c9191680a9bd0e242`
and the exact 16 relocation records. It performs no retail-file lookup.
Derive the factor block from its expected input, then rewrite 230 GP fields
across 180 instructions and the paired S2/S3 entry-save registers/slots.
The resulting 185 changed words partition into eight factor-block words,
two entry saves and 175 other live-GP allocation words.

All 16 relocated instruction words are unchanged. Every added guard has
expected/replacement relocation `-`; symbolic rebasing is qualified in four
independently GNU-linked symbol sets, not by pretending these guards relocate.
No instruction insertion, omission, padding or FP-register rewrite is added.
The conditional whole-CFG certificate covers 383 nodes, 404 reachable words,
560 obligations and six calls; the unreachable +0x1A8 word is unchanged.
Owned-frame closure, live-role joins and volatile-register kills are explicit
assumptions/checks, not merely an instruction-mask comparison.

## Qualification

The [matching suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_matching.py)
reuses the existing numeric MIPS oracle and independent reference.
It adds a thin access-boundary stop wrapper, not another emulator.

- 432 complete-entry cases / 1,296 executions compare raw, normalized and retail.
  Normalized/retail complete model GP/FP/LO/condition/FCSR, memory, events and
  calls agree. Raw/retail public prefixes and complete exit memory agree.
- 24 fixtures cover **9,096 injected memory-access boundary pairs / 18,192
  executions** and **2,664 real missing-first-read-byte pairs / 5,328 executions**.
  Normalized/retail complete model state agrees at every tested boundary.
- Reject 405 stale instruction controls, 16 stale relocation controls, wrong
  extent, four effective partial GP transformations and one broken entry save.
  Partial-transform witnesses are changed output, real missing storage or ABI
  failure, not unsupported instructions or timeouts.
- Compile the actual copied owner: preserve 22 neighboring functions, pools,
  relative relocations and the same four diagnostics. Raw copied and isolated
  target words/relocations agree. The real padder emits exactly 1,620 bytes,
  no padding, and rejects all 185 stale expected-word guards plus bad relocation
  metadata. Four independent original/padded/raw links run 1,152 executions.
- Preserve the older complete recovery controls after installation by
  reconstructing the original owner and using the old guard prefix for raw
  controls. Reverse reconstruction recovers the exact old source/progress
  fingerprints. No shared helper or compiler profile changes.

Fresh pre-install run: **31 tests pass in 209.682s**, no skips: seven matching,
eight proof and sixteen SETUP_FITTED recovery tests. An earlier seven-test
command had one fixture failure: its stale-word bit was in a legitimately
masked J26 relocation field. Correct the control to bit 31; its corrected
selector passes in 3.887s before the clean 31-test run. Do not call that earlier
command passing.

Fresh post-install run: **31 tests pass in 227.669s**, no skips, using the same
seven matching / eight proof / sixteen SETUP_FITTED selection. Installation-
aware source/guard/progress branches pass; the full linked baseline remains
byte-exact. All six renderer tool files parse and match the reviewed older
mirror; **130 documents / 4,117 relative links / zero broken**.

Fresh post-install 14 shared tests pass in 0.138s; mounted and older standalone project
tools checks pass. Prior unchanged neighbor-suite receipts remain historical,
not a fresh full recovery-module run. Production build succeeds with the
existing duplicate generated_12D630 recipe warning and existing C diagnostics.

## Receipts And Banking

Ignored receipts live in `conker/build/game-record-ring-renderer-test/normalization/`:
`closure.json`, `stale.json`, `partial-negatives.json`, `private-exits.json`,
`private-boundaries.json`, `owner.json`, `linked.json`, `audit-installed.json`
and `after.json`. Pre-install `before.elf`, `before-progress.json` and
`before-manifest.csv` provide byte/row/prefix comparison, not an inferred count.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
PYTHONPATH=. python3 conker/build/game-record-ring-renderer-test/normalization/audit-installed.py
make -C conker match-progress NON_MATCHING=1
python3 -m unittest tools.tests.test_game_record_ring_renderer_matching tools.tests.test_game_record_ring_renderer_proof tools.tests.test_game_record_ring_renderer_recovery.GameRecordRingRendererSetupFittingTests -v
```

Per "Keep commited", bank tools **36bead05dd9ad357e8f5641f8b2f2d229814c296**
first, then parent source/manifest/docs and that exact gitlink. Regenerated
`conker/progress.csv` is an ignored build output; audit it and record its
measurements without force-adding it or the ELF/temporary receipts.
Mirror only the reviewed recovery update and two new tool files after
prior-hash/absent-path gates. Preserve older standalone HEAD ddbdd16 and its
independently dirty shared helper and effect-registration test; do not reset
or duplicate its history. No push requested/performed.

Manual Graphify refresh after code changes refuses 16,869 nodes over retained
38,655; fail-closed preservation covers 19,398 nodes from 2,972 still-existing
excluded files. Preserve the graph, do not force or claim graph repair.
Routine work uses one Codex writer and zero Claude calls.

## Boundary And Next Work

This qualifies emitted normalized instruction order and model state, not
portable C invalid-access behavior, hardware CP0/FCSR traps or gameplay.
Raw/retail private fault-state identity is not claimed. Bounded setup/deep
callees, including linked dispatcher/combiner recovery, remain separate.
No host port, runtime/save/editor, bridge, account or frozen Release changes.
The wider Game matching goal remains active.

Next retained target is **func_151D7264**, VA 0x151D7264..0x151D73A8,
ROM 0x204714..0x204858: **81 words / 324 bytes / frame 0x40**.
Capture the previous XYZ and flag before the callback selected by unsigned
state byte +0x2C through D_8008FCA0. Recover failure marking, live callback
changes, distance computation and all record-update branches before fitting.
Qualify actual connected helpers and aliases/access order rather than assuming
this callback is immutable. Graph query finds no target node; inspect retail
assembly and direct caller/table references. The other retained routine in
this owner is func_151D75C4; func_151D8718 is already converted, not the next target.
