# Game Attachment Selection Dispatcher Recovery

Date: 2026-10-08

## Result And Boundary

Recover the complete semantic C candidate for **`func_15031FC8`**, not another
small substitute target. The candidate is retained in the
[experiment driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_selection_candidates.py);
**the production zero-return placeholder is deliberately unchanged**.

Retail: [5D2C0.s](../../conker/asm/5D2C0.s), VA
`0x15031FC8..0x150331B8`, ROM `0x5F478..0x60668`, **1,148 words / 4,592 bytes**,
frame **0x48**. Production owner:
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
Continues [Note 1113](1113-game-fourth-tile-size-command-direct-match-20261008.md).

The complete selected C emits **1,147 words / 4,588 bytes**, frame **0x38**,
**394 fixed-slot word differences**, seven useful tables / 674 entries,
2,704 aligned isolated pool bytes. All isolated and copied-owner compilation
uses the existing IDO 5.3 MIPS2/o32 SDK profile with zero strict diagnostics.
This is **qualified semantic recovery, not a byte match or installed recovery**.
No guards, padding promotion, instruction insertions, Makefile/profile/shared
header/production edits, runtime or sibling Release actions.

## Complete Contract

1. Read actor+0x2D0 as the cached source before reading node+0x48. A null
   attachment returns zero, but does not waive the required actor-source read.
2. Read the initial attachment's unsigned flags+4, clear bit15, and cache
   actor model byte+4 and unsigned type halfword+0x84 before any node writes.
3. Model0x58 optionally sets node+2 to0x12 for node action0x9B, then selects
   from type2/3/0x27/0x28. The default rereads node+1 after the optional store.
   Model0x5B always selects0. Models0x5A/0x74/0x7A write the signed halfword
   at node+0x18 from D_800902D0/D4 according to actor+0x2E8, then dispatch
   type through the 43-entry table and explicit0x50/0x51 branches.
4. Other models dispatch on **node+1**, not actor+4. The actor model remains
   separately cached for conditional0x87/0x8B/0x99/0xB5 branches. Node actions
  0x83/85/87/88/89/8D/8E/8F/90/91/98/9A/9B/9C/9D/9E/9F have complete routes;
   other actions retain choice-1. Model overrides take precedence over actions.
5. Recover every type-to-choice case, including the large sparse0x8F/0x90
   switch and distinct equal-value cases. Recover mode-byte5 bypasses, node
   state-byte changes,0x9E's node+0x1E/+0x20 parent setup, required node+2
   reread and parent clear. Only the0x9E action disables state copying.
6. Unsupported types for actions0x83/87/89/8E/98 return **one before setup,
   source progress/state copying or clamp**. Mode/model overrides may bypass
   these type restrictions. Other completed paths return zero.
7. Action0x85 selects5/4/2 for types0x13E/0x13F/0x7C; otherwise use the ordered
   comparison0 < actor+0x3C. Action0x91's mode5 branch first clears node+2,
   then selects3 only if actor+0x24 compares equal to floating zero.
8. A choice other than-1 calls `func_1503F5B8` with the **current**, reloaded
   node attachment and six-word arguments `(attachment, 0, choice, 0.0f, 0.0f, 1)`.
   Cached source, choice, original flags and copy-state policy survive this call.
9. If the cached source is nonnull, reload the attachment. When choice equals
   the initial low15 flags and source+0x3C's signed halfword is0x3FF, call
   `func_1505E060(attachment)` and reload node+0x48 afterward.
10. Copy source+8's binary32 progress to attachment+8, then reload node+0x48.
    If copying is enabled and signed byte+0x39 is nonzero or unsigned byte+0x215
    is zero, copy source state halfwords+0x3A/+0x3C. Reload the attachment
    pointer between these stores and after the second store.
11. Read the final attachment's end+0x18 before current+8; compute binary32
    `limit = end - 1`. Store limit when **limit <= current**, including equality.
    There is no newly invented post-call null gate, bound, clamp policy or
    source-pointer reload from actor+0x2D0.

The reference consumes retail table targets and verified case-delay constants
independently of the driver's literal semantic case/value lists. It checks
those lists against all applicable original table entries before execution.
No opaque instruction arrays or guessed function names replace these routes.

## Fit And Owner Measurements

The first shared-initial-and-final attachment local forced choice into saved
S0. Separating the **initial attachment pointer** from the later pointer
removes that saved-register lifetime and recovers the original A2 choice.
It is a semantic lifetime distinction, not a volatile annotation or dummy frame.

| Complete Form | Body Words | Frame | Fixed-Slot Differences | Isolated Pool |
| --- | ---: | ---: | ---: | ---: |
| Selected O2/g3 | 1,147 | 0x38 | 394 | 2,704 bytes |
| Selected O2 | 1,146 | 0x38 | 927 | 2,704 bytes |
| Selected O1/g3 | 1,558 | 0x50 | 1,529 | 2,704 bytes |
| Selected O1 | 1,558 | 0x50 | 1,529 | 2,704 bytes |
| Shared initial pointer O2/g3 | 1,149 | 0x40 | 1,117 | 2,704 bytes |
| Literal low-mask O2/g3 | 1,146 | 0x38 | 925 | 2,704 bytes |
| Register locals O2/g3 | 1,147 | 0x38 | 394 | 2,704 bytes |

Masking with `~0x8000` preserves the original full-width mask expression.
The shorter7FFF literal emits a different opening sequence and is only an
ordinary-effect control. None of these forms is promoted by filling its slot.

The copied complete owner compiles with **40 functions / 39 unchanged
neighbors**, including each neighbor's relative relocations. Selected target
text differs from the isolated object **only at seven checked pool addends**;
relocations and normalized target identities agree after the measured412-byte
pool prefix. Existing useful action/cleanup tables remain unchanged.

The actual owner pool grows from **416 to3,120 aligned bytes**. New table
addends are **412,552,724,840,904,2756,3068**. Their original physical offsets
from `jtbl_80096F40_game` are **416,556,728,844,908,2760,3072**.
Every new table is therefore **four bytes early** under blind shared-anchor
binding. The original scalar **D_800970DC =0x3C088889** occupies that gap.
Prior final alignment does not become an internal scalar gap automatically.

Do not install the current candidate with the existing shared anchor, modify
retained Game data, emit replacement data, or disguise a wrong addend with a
text guard. Owner pool binding remains an explicit separate gate.

## Qualification

[Nine recovery tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_selection_recovery.py)
pass across targeted runs. Evidence is bounded to defined return, callback
arguments, exact public read/store order, object memory and required faults.
Saved GP/FP/SP/RA are checked by the guest runner; incidental caller GP/FP and
the retail private frame/home layout are **not** claimed to match.

- **92,992 guest dispatch cases**, including all65,536 unsigned type values
  on the broad route, every model/action byte, specialized model routes,
  explicit early returns and mode-byte overrides. Exhaustive dispatch test
  passes in **390.083 seconds**.
- **2,415 callback/state/float cases**, six callback mutation modes, two SP
  phases, four signed-state byte patterns, three active-byte patterns and15
  binary32 patterns. Both callees clobber caller GP/FP in the model. Pointer
  rebinding, source data mutation, cached actor-source lifetime, skip-state
  gates, signed zero, finite thresholds, infinities and quiet NaNs qualify.
- **Thirteen required-storage faults** preserve exact public read/store
  prefixes and partial effects, including missing initial source with absent
  attachment, initial flags, selected parameter global, source state/progress,
  final end and a callback that clears node+0x48. No extra null gate is added.
- **Six valid aliases**, including actor/node identity, source/node/actor/
  attachment identity and a final attachment on the node. A source-state
  halfword store changes the high half of node+0x48; the subsequent clamp
  correctly uses the changed pointer. Arbitrary private stack aliasing is open.
- Three source controls pass **252 ordinary-effect executions**. Five compiled
  negatives are caught: wrong last sparse choice, always-copy-state, inverted
  reset eligibility, strict clamp and stale attachment after setup. Equal-value
  clamp stores remain observable in the exact trace even when bytes agree.
- **12,348 actual native32 C executions**, all model/action bytes, every
  literal broad choice, specialized routes and six callback modes. Compare
  callback ABI and complete snapshots of all five objects against independent
  expected stores. Assert32-bit pointers, binary32 and16-bit halfwords. Native
  little-endian tests do not establish guest-endian/FCSR/private-frame/hardware.
- **4,005 focused coverage cases** exercise all674 original table keys and
  **1,125/1,148 retail words**. The23 unexecuted indices are retained in
  `coverage.json`; this is measured coverage, not a whole-slot match claim.
- All **21 installed tile/cleanup/action regressions pass in225.613 seconds**,
  zero skips/errors/failures. Tools, Python syntax, CLI and whitespace checks pass.
  Documentation validation covers **96 documents /4,104 relative links /zero
  broken links**.

The initial harness's `super()` reuse and receipt serialization were corrected;
the attachment fixture was also moved away from the oracle's private stack.
None of those test-only corrections changed production or the recovered contract.
Focused coverage was strengthened with the alternate parameter read, nonnull
attachment/null source and inclusive-clamp store instead of lowering its gate.

```sh
python3 -m tools.experiments.game_node_selection_candidates --owner --controls
python3 -m unittest tools.tests.test_game_node_selection_recovery -v
python3 -m unittest tools.tests.test_game_node_tile_match tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match -v
make tools-check
```

Full FCSR, actual callee bodies, hardware, gameplay, renderer and PC-port
acceptance remain open. No production rebuild is needed for this experiment-only
checkpoint; the live installed ELF is audited against the previous baseline.

## Preserved Baseline

All **6,058 linked symbols /6,042 retail slots /sixteen overflow symbols**
remain unchanged against `conker/build/game-node-tile-test/after.json`, including
every body/address/extent. `.init`, `.init_data`, `.debugger`, `.game_data`, all
**720 Game-data owners /189,088 bytes**, **11,063 guards** and conversion CSV
hash remain unchanged. The target's production slot is still its padded stub.

README remains unchanged: exact total **3,370/5,467 (61.64%)**, Game
**2,697/4,794 (56.26%)**, **2,097 different /zero drift**. No new conversion or
byte-match credit. This history belongs in DOCS, not the root README.

Ignored receipts: `conker/build/game-node-selection/{profiles,controls,owner}.json`
and `conker/build/game-node-selection-test/{slot,dispatch,callbacks,gates,aliases,controls,native,coverage,owner,installed,audit}.json`.
The authoritative installed baseline remains **`game-node-tile-test/after.json`**.

## Next Work

1. Continue **this dispatcher**, using the complete selected C and semantic
   qualification. Recover frame0x48 and the original choice/source/flags/
   copy-state homes without dummy bytes or forced instruction insertion.
2. Fit the opening schedule, nested model dispatch and post-reset attachment
   register lifetime. Selected code still copies model into A0 at the opening
   and uses A0 for the tail attachment; retail retains V1 until the nested
   route and uses A3 for the tail. Track actual differences, not just body size.
3. Recover/qualify per-table physical binding across the original four-byte
   scalar gap in the complete owner. Keep all existing tables and the scalar
   intact; qualify actual padder output and independent entry/symbol/carry rebases
   before installation. Do not blindly bind the current packed pool.
4. Re-run the complete dispatcher tests, installed regressions and all-owner/
   data/guard/conversion audit after any fit or binding change. Install only at
   the explicitly measured boundary; update README aggregate counts only then.

The broader Game matching goal stays active. Resolver C84/frame0x20/40
differences, matrix wrapper/basis/translator/sampler and full callee/runtime
boundaries remain open. No sibling Release, save, runtime or push action.
