# Game Attachment Selection Lifetime And Table Binding

Date: 2026-10-08

## Result And Boundary

Continue **`func_15031FC8`** from
[Note 1114](1114-game-attachment-selection-dispatcher-recovery-20261008.md).
The [complete semantic candidate](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_selection_candidates.py)
now emits **1,148 words / 4,592 bytes**, frame **0x38**, **349 fixed-slot word
differences**, down from 394. Retail's body is also 1,148 words, but its frame
is **0x48**. This is a fit improvement, **not a byte match or installed recovery**.

The explicit reset/no-reset attachment assignments recover retail's **A3 tail
attachment lifetime** and the pre-reset A0 argument move. No dummy frame,
volatile annotation, instruction insertion, omission or padding is used.
The complete model/action/type, early-return, cached-source, callback, state-copy
and inclusive binary32 clamp contract from Note 1114 remains the qualification
boundary. Its previous selected body is retained as `BASELINE` and an ordinary
effect control, not overwritten or promoted.

Seven table-address bindings across the original scalar gap qualify through
the existing padder using **14 experimental relocation-aware rows**. These rows
are written only into ignored test CSVs. The production CSV, owner, Makefile,
profiles, shared headers and Game data remain unchanged. Correct table bases
do **not** yet prove that the original tables' jump-target PCs fit this C body.

## Lifetime Measurements

| Complete Form | Body Words | Frame | Fixed-Slot Differences |
| --- | ---: | ---: | ---: |
| Previous selected / separated initial pointer | 1,147 | 0x38 | 394 |
| Separated pointer / reread reset argument | 1,148 | 0x38 | 361 |
| Shared pointer / reread reset argument | 1,148 | 0x38 | 407 |
| Selected shared pointer / explicit reset else | 1,148 | 0x38 | 349 |
| Shared pointer / nested model comparisons reread | 1,148 | 0x38 | 351 |

The shared selected pointer is assigned on both sides of the reset branch;
the compiler removes the redundant read on the non-reset side. This changes
allocation without adding an observable read. Callback mutation, fault-prefix,
alias and native checks qualify the emitted result, not just source intuition.

Three bounded screens measured 27 pointer/model/switch forms, 11 reset/reread
forms and 14 model-use forms. None improves on 349 differences. These are raw
fit measurements; the unselected screen forms are not all semantically qualified.
Original frame/private homes and the early nested-model V1-to-A0 copy schedule
remain open. Recovering A3 does not establish the remaining register lifetimes.

The selected tail's calls still occur at retail `0x150330DC` and `0x1503311C`.
Direct disassembly measures these private addresses, not original source names:

| Logical Home | Retail SP Offset | Selected SP Offset |
| --- | ---: | ---: |
| Incoming node | 0x48 | 0x38 |
| Cached source / T0 | 0x44 | 0x34 |
| Choice / A2 | 0x40 | 0x2C |
| Initial masked flags / T2 | 0x30 | 0x24 |
| Copy-state policy / T1 | 0x24 | 0x28 |
| Saved RA | 0x1C | 0x1C |

In the opening, selected C copies V1 to A0 in the outer switch branch delay at
`0x1503201C`, while retail keeps V1 until the nested route. The first selected
table target begins at `0x15032038`, versus retail `0x15032034`. These are
concrete next-fit measurements; no private-home offset patches are installed.

## Physical Table Binding

The complete copied owner still preserves **39 neighboring functions** and
the existing useful 412-byte table prefix. Its seven new tables pack four bytes
before their original addresses because the original scalar
**D_800970DC = 0x3C088889** occupies a gap that packed generated rodata omits.

| Original Symbol | Entries | Packed Owner Addend | Original Anchor Offset |
| --- | ---: | ---: | ---: |
| `jtbl_800970E0_game` | 35 | 412 | 416 |
| `jtbl_8009716C_game` | 43 | 552 | 556 |
| `jtbl_80097218_game` | 29 | 724 | 728 |
| `jtbl_8009728C_game` | 16 | 840 | 844 |
| `jtbl_800972CC_game` | 463 | 904 | 908 |
| `jtbl_80097A08_game` | 78 | 2,756 | 2,760 |
| `jtbl_80097B40_game` | 10 | 3,068 | 3,072 |

`table_binding_guards()` checks the target's exact 674-entry pool ownership,
unique known addends, HI/LO relocation pairs and LUI/index-add/LW topology.
Each expected-word/expected-relocation pair replaces only the address immediate
and binds it to that table's existing physical symbol. Registers/opcodes remain
unchanged. No insertion, omission, new data or shared-tool change is needed.

[Four binding tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_selection_binding.py)
pass in **6.223 seconds** after strengthening the original-target PC measurement:

- Compile and asm-processor-postprocess both complete owners. All 40 function
  identities, 39 neighbor bodies/relative relocations and prior useful pools
  agree. The candidate's actual padded target is exactly 4,592 bytes, has no
  padding/generated-data payload, and links identically to isolated selected C.
- **56 independent links**: seven symbols, four addresses each, two entry phases.
  Signed LO carry boundaries are included. Only the selected table's two address
  words change; all other words remain unchanged.
- **Six rejected stale controls**: expected word, expected relocation, unknown
  addend, store opcode replacing the load, wrong HI relocation and changed table
  ownership. Existing padder guards and the binding generator fail closed.
- **Two effective negatives**: omitting the first LO binding addresses scalar
  `0x800970DC`, not table `0x800970E0`; substituting the next table's symbol also
  changes the linked address. Neither is silently accepted as correct binding.

GNU assembler creates empty `.data`/`.bss` sections. The test checks zero
payload, not section absence. This is a test-only correction, not production
data or assembler behavior changed to satisfy a test.

**Remaining installation gate:** original table entries encode retail label PCs.
The binding tests compare address relocation/link results, not execution of
padded C through original target PCs. Raw C still differs at 349 words; never
install it merely because its body size and table bases now agree.

The postprocessed owner now measures **590/674 exact target PCs**; the other
**84 entries are exactly one word late** in the candidate. Per-table exact
counts are **0/35, 0/43, 23/29, 16/16, 463/463, 78/78, 10/10**, respectively.
The first original target `0x15032034` would need candidate `0x15032038`.
These are entry-weighted label-PC comparisons, not execution parity or unique
label counts. Correcting the early scheduling/word layout remains necessary;
this measured mismatch explicitly rejects current original-target compatibility.

## Qualification

The six targeted callback/float, fault, owner, alias, control and native tests
pass in **32.032 seconds** after selecting the new lifetime form. Four ordinary
source controls now qualify **336 executions**; all five compiled negatives
remain effective, including the previous lifetime's stale attachment negative.

All **34 tests pass together in 578.223 seconds**: nine complete recovery,
four binding and 21 installed tile/cleanup/action regressions, zero skips,
errors or failures. The strengthened target-PC measurement also passes in
the separate four-test binding run above.

- **92,992 guest dispatch cases**, including all 65,536 unsigned types and
  every model/action byte; defined returns, calls, public order and memory agree.
- **2,415 callback/state/float cases**, six mutation modes, two SP phases and
  15 binary32 patterns. Cached source and attachment rereads qualify while
  callback hooks clobber caller GP/FP.
- **Thirteen required faults**, exact public prefixes/partial effects, lazy
  early returns and **six valid aliases**, including store-induced pointer changes.
- **12,348 actual native32 C executions**, six-argument setup ABI and complete
  snapshots of all five objects. Host-endian execution is not guest FCSR proof.
- **4,005 focused coverage cases**, all 674 original table keys and
  **1,125/1,148 retail words**. The 23 unexecuted indices remain in the receipt;
  measured coverage is not a whole-slot parity claim.
- All **ten padder/word-patch regressions pass in 0.044 seconds**. Tools,
  Python syntax, CLI/profile/owner screens and whitespace checks pass.
  Documentation validation: **97 documents / 4,115 relative links / zero broken**.

Full callee bodies, incidental GP/FP, private frame aliasing, FCSR, hardware,
gameplay and PC-port acceptance remain open. No production rebuild is needed
for an experiment-only checkpoint.

```sh
python3 -m tools.experiments.game_node_selection_candidates --owner --controls
python3 -m unittest tools.tests.test_game_node_selection_recovery tools.tests.test_game_node_selection_binding tools.tests.test_game_node_tile_match tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match -v
make tools-check
```

## Preserved Baseline

The unchanged-installed audit verifies **6,058 symbols / 6,042 slots / sixteen
overflow symbols**, every body/address/extent, protected `.init`, `.init_data`,
`.debugger`, `.game_data`, all **720 Game-data owners / 189,088 bytes**, **11,063
production guards**, and the conversion CSV hash against
`conker/build/game-node-tile-test/after.json`.

Production [generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c) still
contains the padded zero-return placeholder with **1,119 differences**.
No new byte-match/conversion credit: README unchanged at exact total
**3,370/5,467 (61.64%)**, Game **2,697/4,794 (56.26%)**, **2,097 different / zero
drift**. Detailed progress belongs in DOCS, not the root README.
No sibling Release, saves, runtime, hardware or push action.

Ignored receipts: `game-node-selection-test/{slot,dispatch,callbacks,gates,aliases,controls,native,coverage,owner,installed,audit}.json`,
`game-node-selection-binding-test/{binding,rebases,stale,negatives,target-pcs}.json`,
and `game-node-selection-{lifetimes,rereads,model-use}/measurements.json`.
The authoritative installed baseline remains **`game-node-tile-test/after.json`**.

## Next Work

1. Continue this complete dispatcher. Recover the original **0x48 frame** and
   choice/source/flags/copy-state private homes without dummy bytes or forced
   instruction insertion. Retain the selected A3 attachment lifetime.
2. Fit the opening and nested model dispatch schedule, then measure each original
   table target against the corresponding emitted C label PC. Do not substitute
   regenerated table data or broad guards for a non-fitting body.
3. Re-run semantic, actual owner/padder/rebase, installed-regression and all-symbol/
   data/guard/conversion checks after each meaningful fit. Promote the experimental
   table rows only after the body and original target-PC compatibility qualify.
4. Update README aggregate counts only for a qualified installed match. The wider
   Game matching goal, resolver C84/frame0x20/40 differences, matrix and full
   callee/runtime boundaries remain open.
