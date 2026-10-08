# Game Attachment Selection Closed Scheduling Match

Date: 2026-10-08

## Result

Continue `func_15031FC8` from [Note 1116](1116-game-attachment-selection-frame-and-opening-recovery-20261008.md).
The complete semantic dispatcher replaces the zero-return placeholder in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
Selected IDO 5.3 O2/g3 C emits **1,148 words / 4,592 bytes**, frame **0x48**,
with **304 raw word differences**. The fresh production ELF and actual
owner/padder/link experiment match **all 1,148 retail words**, and all
**674 original table target PCs**
and assembled label offsets agree. This is a **guard-normalized match**, not
a claim that the compiler emits the complete retail body directly.

Production qualification comprises **14 symbolic table-binding rows** and
**67 closed scheduling rows** in
[retail_word_patches.us.csv](../../conker/retail_word_patches.us.csv).
No generated Game data, zero-return fallback, filler words, synthetic private
storage, compiler-profile, Makefile or shared-header change.

VA `0x15031FC8..0x150331B8`, ROM `0x5F478..0x60668`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
Full model/action/type, callback, state-copy, alias and clamp contract remains
the recovery documented in [Note 1114](1114-game-attachment-selection-dispatcher-recovery-20261008.md).

## Final Source Recovery

Action **0x85** uses an if/else chain for types 0x13E, 0x13F and 0x7C before
the original positive-float fallback. Action **0x98**, model 0x8B, stores
`node[2] = 6` before assigning choice5. These source shapes recover thirteen
and two remaining control-flow/scheduling differences respectively.
Raw C improves from319 to304; frame, all six private homes, first19 and final68
words and all table pool entries remain intact.

Twelve meaningful field-pointer controls still emit identical raw text/pools.
Earlier C1147/394, C1148/frame0x38/349, C1148/frame0x48/321 and C319 forms are
retained as controls. Seven ordinary controls cover **588 executions**; all
five compiled semantic negatives remain effective.

## Closed Scheduling Transformation

[Normalizer](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_selection_schedule.py) accepts
the measured compiler body, **not retail ROM words**. It checks extent,
eleven instruction anchors and the exact four cached-model branch uses.

1. Swap the flags copy and outer branch, putting the flags copy in the delay slot.
2. Relocate the early V1-to-A0 model copy into the nested action route. Preserve
   V1 as the cached model for the four earlier/later comparisons; retarget only
   those four comparison source-register fields from A0 to V1.
3. Move the existing nested constant into the freed node-home load position,
   and move that existing node-home load to the case0x99 entry. The case target
   enters the load before its old cursor instruction, not after it.
4. Derive the **57 affected local branch displacements** from the closed
   instruction-origin permutation and the explicit case-entry mapping.

Every one of the **1,148 original compiler instruction origins occurs exactly
once**. Nonbranch instructions retain their original words; branch changes are
only derived local displacements and the four cached-model source registers.
One model-copy omission and one node-load insertion implement relocation, not
deletion of semantic work or slot filling. The first19/final68 words are untouched.

`schedule_guards()` refuses relocated instructions at patched source offsets.
The existing padder enforces static expected words and expected relocations;
the build does not silently regenerate guards. Tests compare all installed rows
with the measured owner-generated rows. No shared padder implementation change.

The seven address pairs remain bound to their **original physical symbols**,
preserving **D_800970DC = 0x3C088889** and the original scalar gap.
Address binding and target compatibility are verified separately: raw C still
has590/674 fitting table entries, while the normalized body has674/674.
Compiled private table pools are diagnostic artifacts, never replacement data.

## Qualification

The full dependency-driven ELF/progress rebuild succeeds. All **40 unique
checks are verified across combined and targeted runs**. The final **20-test
focused run passes in116.371s**, zero skips/errors/failures; exhaustive92,992
dispatch cases passed in the combined run. Existing whole-repository compiler/assembler and
duplicate generated_12D630 recipe warnings remain; isolated/copied target
compilation has zero strict diagnostics, not a warning-free repository claim.

The strengthened suite checks the actual padded object with original tables,
not an isolated body using regenerated table targets. It executes **6,352
cases** across callbacks/float patterns, lazy/fault prefixes, aliases and every
table domain. Eighteen stale scheduling controls are rejected; five compiled
semantic negatives are rejected or remain nonmatching. An unrelated choice-word
mutation survives normalization, proving this is not a retail-word replacement.
Both raw bindings and normalized schedules pass56 independent table/carry/entry
links each. Thirty-nine fully postprocessed neighbors and existing useful pools
remain unchanged. Ten final padder/word-patch regressions pass in0.041s.
Tools, Python syntax, CLI/profile/field/control/owner and whitespace checks pass.
Documentation validation: **99 documents /4,139 relative links /zero broken**.

The raw recovery additionally qualifies **92,992 guest dispatch cases**,
**2,415 callback/float cases**, **12,348 actual native32 C executions**,
thirteen required fault prefixes, six valid aliases and588 ordinary control
executions. No single all-green40-test rerun is claimed after the two fixture
corrections; all affected checks and remaining dispatcher checks are covered by
the clean20-test final run.

The first post-install **40-test combined run** takes642.079s:38 pass, two
copied-owner neighbor checks fail. These are test-fixture pool assumptions,
not production changes: removing cleanup/action from a copied owner moves
selection's packed table bases from412 to220/192 respectively. The older
checks required literal byte equality and hard-coded the pre-selection pool sizes.

The corrected tests use actual relocation ownership and validate all14
table-address words, allowing **only seven checked LO addend shifts**. Every
other neighbor instruction/relocation stays exact; all674 selection identities,
prior pools, target-owned additions and alignment bytes are checked. The real
padder is still exercised on the complete selected owner with the unmodified
production guards. Both repaired tests plus all four binding tests pass in
**21.587s**, zero skips/errors/failures. This test-only correction changes no
production source, guard row or linked byte. The first preliminary label receipt
also needed the original label names rather than an assumed `_game_data` suffix;
the corrected test uses assembler-resolved differences, not discarded nm symbols.

The focused coverage receipt is corrected to the **measured 3,925 cases**,
not the older fixed-offset total4,005. Earlier notes overcounted this receipt by
80; the executed cases and recorded coverage were unaffected. All674 keys and
1,125/1,148 retail words execute; the23 missing indices remain explicitly recorded.

The defined return, call ABI, ordered public accesses, object memory and saved
state are qualified. Incidental GP/FP, arbitrary private-frame aliases, full
callee bodies, FCSR, hardware, gameplay and PC-port acceptance remain open.

```sh
python3 -m tools.experiments.game_node_selection_candidates --field-forms --owner --controls
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_node_selection_recovery tools.tests.test_game_node_selection_binding tools.tests.test_game_node_selection_schedule tools.tests.test_game_node_tile_match tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match -v
make tools-check
```

## Linked Audit

Against `conker/build/game-node-tile-test/after.json`:

- All **6,058 symbols /6,042 retail slots /sixteen overflow symbols** retained.
  Only `func_15031FC8` changes; **6,057 other symbol bodies** and every
  address/extent remain unchanged. Its former1,119 placeholder differences are zero.
- `.init`, `.init_data`, `.debugger` and `.game_data` unchanged.
  All **720 Game-data owners /189,088 bytes** remain exact, SHA256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- All **11,063 prior guard rows** preserved exactly; **81 target rows** added,
  total **11,144**. Prior prefix and target-tail hashes are checked independently.
- Conversion CSV hash unchanged. This placeholder already counted as C;
  conversion counts/byte percentages do not increase.
- Exact total **3,371/5,467 (61.66%)**, Game **2,698/4,794 (56.28%)**,
  **2,096 different /zero drift**. Init492/492 and Debugger181/181 remain exact.
- Root README changes only the two aggregate matching rows. Detailed recovery
  stays in this note and the documentation indexes.

Authoritative next checkpoint: **`conker/build/game-node-selection-test/after.json`**.
Auditor: ignored `audit-installed.py` and `audit-installed.json` beside it.

## Next Work

The next local placeholder after the already-restored attachment helpers is
**`func_150334B8`**, a **68-word /272-byte leaf**, no frame, VA
`0x150334B8..0x150335C8`, ROM `0x60968..0x60A78`.
Static inspection identifies action0x37's fourth tile-size scan and signed
one-step coordinate wrapping; incoming actor is saved but not read by the body.
It has no calls or global relocations. This is an inventory, not a semantic or
matching qualification. Recover it independently after banking this dispatcher.

Other owner placeholders, resolver `func_15031070` C84/frame0x20/40 differences,
matrix/callee and wider Game work remain open. No sibling Release, save,
runtime, hardware or push action.

Ignored evidence: `game-node-selection/`, `game-node-selection-test/`,
`game-node-selection-binding-test/`, `game-node-selection-schedule-test/`, and
`game-node-selection-{outer-key,closed-schedule,route-shapes}/` under `conker/build/`.
