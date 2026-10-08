# Game Attachment Selection Frame And Opening Recovery

Date: 2026-10-08

## Result And Boundary

Continue the complete **`func_15031FC8`** candidate from
[Note 1115](1115-game-attachment-selection-lifetime-and-table-binding-20261008.md).
Selected semantic C now emits **1,148 words / 4,592 bytes**, retail's **0x48
frame**, all six measured private homes and **319 fixed-slot word differences**,
down from 349. The **first 19 words** and **final 68 words** are directly exact.
The complete dispatcher remains **experimental, non-matching and uninstalled**.

The [candidate driver](../../tools/experiments/game_node_selection_candidates.py)
retains the earlier C1147/frame0x38/394 as `BASELINE`, C1148/frame0x38/349
as `LIFETIME`, and C1148/frame0x48/321 as `FRAME`. No dummy storage,
volatile annotation, instruction insertion/omission, production guard, profile,
Makefile, shared header, production owner or Game-data edits.

## Frame Recovery

Name the final attachment's existing **end/current field addresses**, not
long-lived loaded float values. Keep the source, choice, attachment, field
pointers, flags, model, type, copy policy and limit declarations in the measured
order. The addresses are computed after the last state-copy-induced attachment
reload, and the final reads remain **end before current**.

This recovers the frame/private homes without changing the final FP register
sequence. Naming float values instead recovers the homes but changes FP
allocation, producing 328 differences. Field pointers preserve the original
sequence and give **321 differences**, with the complete final 68 words exact.

The declaration order is a **matching annotation**, not proof of the original
source declarations or names. Every added local represents an existing field
address and is used in the clamp; there are no unused variables or synthetic
frame bytes.

| Logical Home | Retail SP Offset | Selected SP Offset |
| --- | ---: | ---: |
| Incoming node | 0x48 | 0x48 |
| Cached source / T0 | 0x44 | 0x44 |
| Choice / A2 | 0x40 | 0x40 |
| Initial masked flags / T2 | 0x30 | 0x30 |
| Copy-state policy / T1 | 0x24 | 0x24 |
| Saved RA | 0x1C | 0x1C |

`--field-forms` retains **twelve source controls**: f32/u8 field pointers,
optional use in the progress copy, and three address-assignment orders. All
twelve emit **identical selected text and pool bytes** at O2/g3. Pointer
computations do not add public reads; required attachment reloads remain intact.

## Opening Recovery

Move the default `copy_state = 1` assignment after the initial flag read. The
compiler now emits retail's ORI at word8 and copy-state initialization in the
attachment branch delay at word10. The 319-word-difference form differs from
the 321 intermediate **only by swapping these two independent words**;
the complete table pool is unchanged. It adds no guard or instruction.

The binding test checks that closed swap, **all first 19 words**, private homes,
**all final 68 words**, and every retained field form. It does not infer full
function parity from those matching regions.

## Other Measurements

Bounded raw screens retain 55 declaration/intermediate forms, 26 float-local
placements, twelve field-pointer forms, 28 nested-switch forms, 24 model/type
scope forms, 27 opening forms and 26 byte-model-key forms. These include repeated
controls, not 198 distinct semantically qualified sources. Only the selected
recovery and its explicitly tested controls are qualified.

| Complete Form | Words | Frame | Differences | Exact Table Target PCs |
| --- | ---: | ---: | ---: | ---: |
| Previous lifetime | 1,148 | 0x38 | 349 | 590/674 |
| Named end/current floats | 1,148 | 0x48 | 328 | 590/674 |
| Field pointers / original opening | 1,148 | 0x48 | 321 | 590/674 |
| Selected field pointers / recovered opening | 1,148 | 0x48 | 319 | 590/674 |
| Unsigned normalized nested key / older opening | 1,148 | 0x48 | 303 | 590/674 |
| Byte model / older opening | 1,147 | 0x48 | 895 | 84/674 |

The lower raw count from a normalized nested key is **not selected**: it adds
key arithmetic absent from retail and changes the cached model register shape.
Raw fixed-slot counts are not a ranking of faithful source reconstruction.
Byte-model forms remove a word but shift later targets; they are not padded
into the retail slot. Scoped keys/casts do not resolve the original scheduling.

## Remaining Instruction And Table Gates

The original **V1-to-A0 model copy** still occurs too early in selected C,
at `0x1503201C` instead of the nested route's `0x1503247C`. The masked-flags
copy also executes before the outer branch rather than in its delay slot.
The first C table target remains `0x15032038`, versus original `0x15032034`.

Original table target PCs remain **590/674 exact**, with **84 entries one word
late**: all35/all43 entries in the first two tables and six of29 action-table
entries. The other four tables' targets agree. This is an entry-weighted label
comparison, not execution of C through original table data.

The **14 experimental address-binding rows** continue to qualify seven physical
table symbols across D_800970DC's scalar gap. Correct bases are not original
target compatibility. Do not install the current body, regenerate retained
Game data, promote rows to production, or hide the non-fitting dispatch layout
with broad word guards.

## Qualification

The C321/frame0x48 intermediate passes six targeted recovery tests plus four
binding tests in **38.588 seconds**, then all **34 recovery/binding/installed
tile-cleanup-action tests in 586.460 seconds**, zero skips/errors/failures.
The strengthened twelve-field-form binding run passes separately in15.088s.

All **thirteen final C319/frame0x48 tests pass in 495.191 seconds**: nine
recovery/four binding, zero skips/errors/failures. These include **92,992 guest
dispatch cases**, **2,415 callback/float cases**, **12,348 actual native32 C
executions**, thirteen required faults, six valid aliases and4,005 focused
coverage cases. All674 original table keys and1,125/1,148 retail words execute;
the23 unexecuted indices remain explicitly recorded, not assumed unreachable.

Six ordinary source controls cover **504 executions**, including all three
earlier selected forms; all **five compiled negatives** remain effective.
Owner/padder checks preserve39 fully postprocessed neighbors and prior useful
pools, qualify14 experimental rows/56 independent links, reject six stale
controls and catch two effective binding negatives. Twelve field forms emit
identical full text/pools; the first19/final68 words, homes and closed opening
swap are verified directly against the original slot/intermediate.

All **ten padder/word-patch tests pass in0.043s**. Tools, Python syntax, CLI /
profile/field/control/owner screens and whitespace checks pass. Documentation
validation: **98 documents /4,123 relative links /zero broken**.
The unchanged-installed audit again verifies all6,058 symbols/addresses/extents,
protected sections,720 data owners,11,063 guards and conversion hash.

Full callee bodies, incidental GP/FP,
arbitrary private-frame aliasing, FCSR, hardware, gameplay and PC-port acceptance
remain open, even though the frame and six explicit homes now match.

```sh
python3 -m tools.experiments.game_node_selection_candidates --field-forms --owner --controls
python3 -m unittest tools.tests.test_game_node_selection_recovery tools.tests.test_game_node_selection_binding -v
python3 -m unittest tools.tests.test_game_node_tile_match tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match -v
make tools-check
```

## Preserved Baseline

No production rebuild or promotion. Installed baseline remains
**`conker/build/game-node-tile-test/after.json`**: 6,058 symbols /6,042 slots /
sixteen overflow symbols, protected Init/Debugger/Game-data sections,720 exact
Game-data owners /189,088 bytes,11,063 production guards and conversion hash.
The production dispatcher remains its padded zero-return placeholder with
1,119 differences. README aggregate totals and history remain unchanged.

Installed exact counts remain **3,370/5,467 (61.64%)** total,
**2,697/4,794 (56.26%)** Game, **2,097 different /zero drift**. This experimental
fit improvement receives no conversion or byte-match credit. No sibling
Release, save, runtime, hardware or push action.

Ignored evidence: `game-node-selection/{profiles,controls,fields,owner}.json`,
`game-node-selection-test/`, `game-node-selection-binding-test/`, and
`game-node-selection-{private-homes,float-homes,pointer-homes,nested-switch,model-scope,opening-schedule,byte-model-key}/measurements.json`.

## Next Work

1. Continue this dispatcher from the selected **C1148/frame0x48/319** form.
   Frame, homes, opening initialization and tail are established; preserve them.
2. Recover the original nested model-key lifetime and copy scheduling. Fit the
   early phase and masked-flags branch delay without adding non-retail arithmetic,
   dummy instructions or broad guards. Measure real differences and label PCs.
3. Require all674 original table targets to agree before installation. Re-run
   semantic/native/fault/alias/owner/padder/rebase and all-symbol/data/guard/
   conversion checks after meaningful fits. Promote address rows only at that gate.
4. Update README aggregates only for a qualified installed match. Broader Game,
   resolver C84/40, matrix, full callee and runtime goals remain open.
