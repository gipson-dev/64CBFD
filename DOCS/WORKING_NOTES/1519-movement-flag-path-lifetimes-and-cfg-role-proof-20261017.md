# Movement Flag Path Lifetimes And CFG Role Proof

Verified 2026-10-17. Consumer predecessor `3d212c4`, tools predecessor
`a0ea7dd`; both active repositories began clean. Continue the same complete
`func_150F34F4` from [Note1518](1518-movement-turn-role-certificate-and-argument-controls-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

The natural button-path `velocity` lifetime recovers **three real C-emitted
FP words**, reducing raw differences from 392 to **389**. A separately proven
63-word branch region adds 21 private GPR rewrites to the preceding seven.
The actual research-normalized owner now has **361 differences and 469 exact
opening words**, versus 385 and 406 previously. Neither candidate is installed
or credited: the complete function remains 959 words/frame `0x80`, unmatched.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 389 | 361 |
| Exact opening words | 361 | 469 |
| First unequal PC | `0x150F3A98` | `0x150F3C48` |

## Source And Actual Compiler Evidence

`tools/experiments/game_actor_input_movement_flag_paths.py` protects **305
predecessor entries / 281 distinct paths** and uses the existing complete
owner/compiler/link/padder machinery. Nine complete forms screen the prior
body, button temporary versus inline field access, and six initializer orders.
The selected form uses the existing `velocity` float instead of generic
`value` only inside the `0x4000` button block. It naturally emits FPR2 in
the load at `0x150F3BF4`, comparison at `0x150F3C00` and multiplication at
`0x150F3C1C`. Subsequent uses have independent assignments; no inert local,
profile change, instruction trimming or semantic guard is introduced.

The inline form remains 392 differences. Initializer orders give 389, 389,
396, 397, 561 and 397 overlapping differences respectively. The 561 form has
960 words and is correctly rejected by the padder; it is not a 959-word
candidate. Accepted forms preserve all eleven raw/padded neighbors and pools.

A **newly owned** compiler trace, not the predecessor trace, finishes exit0
and reproduces the normal object exactly. It retains 74 actual emitter events
and 684 AS1 instruction records. The qualified frontend/optimizer/rounded
local budgets are 84/76/80, frame 128, saved 16 and outgoing 32. All earlier
live homes remain unchanged. The first button velocity assignment has
frontend float M-32/length4 and optimizer float R34/length4; the later identical
source statement is disambiguated by its actual line marker. The three FPR2
words and nine effective new home/instruction controls are checked. The
post-compile normalized object is not falsely attributed to AS1 output.

```text
Factory: tools.experiments.game_actor_input_movement_flag_paths.selected_body()
Raw form: button-velocity
Raw target SHA256: 732a850e84d11dea6e8e79d6a3134249fa40d1692345ce33c76f5c47bdf98d20
Normalized target SHA256: febdb974cb00937fd7288bef8203c0f65197787b099d4b024d249ad031d7c6ad
Isolated source SHA256: ca327d2076a0b3593124fc1931e9cc8ccdcfcc97080a88cd2a6547140353a586
Raw / research-normalized differences: 389 / 361
Research rows: 28 total, 21 new, zero production rows
```

## Branch-Sensitive Temporary Proof

The new region is words **406..468**, `0x150F3B4C..0x150F3C44`, ending at the
actual `func_1505A3A8` call and delay slot. It uses the fixed closed temporary
permutation `13->10, 12->14, 25->12, 11->13, 10->24, 14->15, 15->25, 24->11`.
It is not a global rename or an extension of the earlier straight-line map.

The verifier decodes GPR operand fields and compares all 63 transformed words
literally with retail. It scans the complete function for computed/interior
entry, rejects region exits, delay-slot targets and control in delay slots,
and overapproximates conditional outcomes. Ordinary delays execute on both
outcomes; likely delays execute only on the taken outcome. The unconditional
branch cannot create a spurious fallthrough. Every permuted read must have a
definition on its actual abstract path; repeated definitions are allowed.
The analysis visits 140 region states and six terminal definition states.

The unreachable duplicate LBU at word420 / `0x150F3B84` is retained and checked
literally, not falsely called path-covered. The caller continuation has a
separate 411-state scan through return: no permuted temporary is read before
a caller-side redefinition. ABI clobber assumptions are not used to excuse
such a read, including past subsequent calls. Identity registers, FP fields,
immediates, memory addresses, callback binding, ordering and delay positions
are preserved. Arbitrary opaque providers observing unpassed raw temporaries,
hardware/FCSR and self-modifying-code behavior are not proven.

Four new changed words carry controller HI16/LO16 relocations: offsets
`0x658`, `0x6AC`, `0x6D8`, `0x6E0`. The private CSV uses the **raw object words**,
preserves their low16 addends and declares identical expected/replacement
relocation type and symbol. No relocation is moved or dropped. All other
new changed words have no relocation. The complete production CSV is an
unchanged prefix. Actual full-owner padder/link output equals the independently
computed vector, changing 36 target bytes in 28 words while preserving target
relocation metadata, eleven neighbors, extent and pools.

## Qualification

The final **nine-test run passes in 108.496s**. Earlier runs exposed test
assertion/fixture issues, not qualified results: the kernel count was doubled,
a value-defining mutation was incorrectly expected to fail def-use analysis,
and isolated entry initially retained the alternate controller selection.
The corrected kernel installs the selection performed by normal function entry
and requires actual coverage of every reachable region word and both likely
delay outcomes. These gates are now demonstrably fired.

- **95 effective CFG/literal/binding controls**, including all 63 region-word
  corruptions, altered controller/callback relocations, bad maps, interior
  entry, undefined live-ins, removed reload, likely-slot definition, lower-path
  join, post-call heading definition, backward/delay control and extent/frame.
- **Three actual padder rejections** for stale raw word, missing relocation
  and wrong relocation symbol; not merely mocked proof failures.
- **3,072 raw-versus-normalized kernel cases**: eight poisoned GPR/FPR seeds,
  eight button combinations, both initial conditions/flags, three vertical
  values, two stack phases and two actor bases. One aliases C0 with the later
  D_800A19A4 read. All 62 reachable words execute; word420 alone stays dead.
  Complete memory, FP state, ordered events, callback packets, observations,
  protected GPRs and actually defined mapped roles agree at real call entry.
- Three-way retail/raw/normalized execution of **2,496 public cases**, twenty
  modeled FP edges and 36 cap boundaries, with 24 cap gates fired. All nine
  provider-mutation modes, 947 reachable retail words and actual 21-word curve
  execution remain covered; twelve original unreachable duplicates are retained.
- **100 active states / 6,600 equal private fault-prefix states**, up from
  5,900. All first remaining fault-boundary PCs are `0x150F3C6C`. An additional
  focused low-position/gate0 cut62 confirms GPR11/12/13/14 differ there while
  all FPRs and RAM agree. This is not complete private acceptance.
- All 80 disabled final private states / 2,700 fault prefixes and all 160
  mode-0 final private states / 8,320 fault prefixes remain equal.
- Native32 O2/O0 UBSan, **149 cases/profile**, eight effective controls, nine
  unsigned-heading extremes and ten cap cases. Actual normalized-object rebases
  pass two links/twelve cases; twelve guest aliases also agree with retail.
- All 305 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

## Advisory Reconciliation

One justified **packet-only Claude Pro advisory** completed exit0, one turn,
with safe mode and tools disabled, no permission denials, no repository edits
or builds. It reviewed the proposal, not the finished implementation or tests.
Packet SHA256 `731109d2fadbc62ef29b25cfb07f497588ba53fc8bdd393b5326dd457a746b8b`.

Accepted: executable live-in dominance and explicit post-call liveness gates,
actual reload-definition evidence, and literal-only coverage for the dead word.
The full instructions establish the reload LUI/LW at `0x150F3BCC/0x150F3BD4`;
negative controls remove the definition or insert a mismatching clobber. FP
convergence is independently checked by full literal FP fields and actual
kernel outcomes. The packet's proposed ban on any relocation-bearing rewrite
was too restrictive: only GPR fields are changed, with the four actual raw-word
HI16/LO16 pairs and addends preserved and padder-qualified as described above.
No second call, approval claim or attribution of Codex tests to Claude.

## Banked Baseline And Continuation

Tools **852c2eb** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks. Four ASCII/AST parses and two identical task
pairs pass. Both mirror destinations were absent; all **1,162** prior hashes
and HEAD `ddbdd16b` survive, with **1,164** dirty paths afterward. No mirror
commit/reset/clean, push or dependency update.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init492/492 and
Debugger181/181 remain exact among converted functions. Root README remains
unchanged. No production build, host-port or frozen Release action.

Scoped AST graph refresh reaches **42,299 nodes / 82,426 links / 3,947
communities**. The new note is indexed; the only three removed IDs are shifted
UPDATE_LOG headings, with their labels retained at new line locations. All
19,398 existing excluded nodes from 2,972 still-present files are preserved;
no purge/full re-extraction or dependency update. This local `_rebuild_code`
adapter requires `Path` objects in `changed_paths`, not strings. The initial
string-argument attempt failed; the corrected owned refresh completes exit0.

```sh
python3 -m tools.experiments.game_actor_input_movement_flag_paths --group button
python3 -m tools.experiments.game_actor_input_movement_flag_paths --group initializers
python3 -m tools.experiments.game_actor_input_movement_flag_paths --normalize
python3 -m tools.tests.test_game_actor_input_movement_flag_paths -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned sources, raw/normalized objects, private expected-flag-guards CSV,
trace, advisory packet/receipts and qualification receipts are under
`conker/build/game-actor-input-movement-flag-paths/`. Earlier immutable captures
remain untouched.

- [x] Recover the natural button velocity lifetime and all three real FP words.
- [x] Prove/qualify only the 21 new branch-region GPR words in private output,
  preserve the previous seven, and leave production guards/credit at zero.
- [x] Bank tools first and preserve both tools copies and every installed byte.
- [ ] Continue the same routine at normalized word469 / `0x150F3C48`: candidate
  LH uses GPR11 versus retail GPR13. Recover the heading/continuation temporary
  allocation, subsequent FP scheduling and private gap at `0x150F3C6C`.
- [ ] Complete all remaining literal, private, caller/provider and immutable
  first-image gates before any installation; keep wider Game work open.
