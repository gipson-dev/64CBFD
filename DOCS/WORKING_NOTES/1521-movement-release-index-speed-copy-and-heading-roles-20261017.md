# Movement Release Index Speed Copy And Heading Roles

Verified 2026-10-17. Consumer predecessor `ded1aa4e`, tools predecessor
`ad45714`; both active repositories began clean. The previous turn was
progress. Continue the same complete `func_150F34F4` from
[Note1520](1520-movement-clamp-acceleration-and-pitch-lifetimes-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

The complete C candidate improves **270 to 200 raw differences**. Three new
bounded heading-role rewrites bring the private research-normalized object
from 242 to **169 differences**, with **478 exact opening words** rather
than 469. Both objects retain all 959 words/frame `0x80`. Neither is installed
or credited as a complete match. There are 31 total private rows, **three new
research rows and zero new production rows**.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 200 | 169 |
| Exact opening words | 361 | 478 |
| First unequal PC | `0x150F3A98` | `0x150F3C6C` |

Of 229 changed raw words, **110 become exact and 40 previously exact words
differ**, a net gain of 70. The additional three normalized gains are explicitly
post-compile research, not falsely called C-emitted or AS1-emitted words.

## Source Recovery

`tools/experiments/game_actor_input_movement_release_addressing.py` protects
**309 predecessor entries / 285 distinct paths**, using the stronger freeze
and existing complete-owner compiler/link/padder machinery. Forty-six complete
forms test pitch compound assignment/coefficient carriers, typed release
addressing, explicit contact joins, zero lifetimes, comparison literal types
and speed-copy order. All raw neighbors/pools remain preserved. Four 960/961-word
forms are rejected by the real padder. Seventeen shorter 957/958-word controls
retain their measured extents and real padding; none is trimmed or credited.

The selected complete form is `copy-after-heldBy`:

- Compound `actor->valueB8 += ...` recovers retail's floating-add operand order
  directly from C, improving the first baseline from 270 to 269 differences.
- A real block-local **signed `releaseIndex`** holds `actor->held - 100` before
  the control-flags clear. The address uses that index times `0x32C`, recovering
  retail's subtract-before-multiply shape instead of a distributed negative
  base constant. Merely spelling the old pointer as a typed array does not help.
- The final negative-speed comparison uses **integer literal `0`**, not `0.0f`.
  The actual compiler emits retail's separate zero in FPR4. The local-index form
  alone is 958 words; this combination restores the complete 959-word layout
  and gives 207 raw differences. Named zero carriers are folded or disturb
  earlier allocation; a double-zero control overflows. No artificial NOP or
  padding variable is introduced.
- Copying `actor->speed` immediately after clearing `record->heldBy`, before
  clearing record flags, recovers its actual retail read order. The emitted
  code stores the copied value later, at `0x150F4034`, after the flags clear.
  This improves 207 to 200 differences. Float snapshot carriers are worse.

The active release block now emits the signed index ADDIU at `0x150F3FE0`,
MULTU at `0x150F3FF0`, held-byte store at `0x150F4014`, actor-speed load at
`0x150F4018`, speed store at `0x150F4034`, and retail exit NOP at `0x150F4050`.
The late FPR4-zero instruction is at `0x150F4354`. These are measured compiler
outputs, not instructions inserted by the new guard rows.

One hundred new guest cases overlap actor speed with released-record flags.
The flags word contains a cleared `0x400` bit, so a late speed read is observable.
Actual retail, raw candidate and normalized candidate agree; the otherwise
matching `copy-base` candidate fails all hundred. The established high-level
reference samples speed late in this overlap and is not used as its oracle.
These are guest-only partial-structure aliases, not portable C alias guarantees.

```text
Factory: tools.experiments.game_actor_input_movement_release_addressing.selected_body()
Form: copy-after-heldBy
Raw target SHA256: baf3b1d68ff8fea1d6b9d8b572f45244c76d74a90c40017184840b9ebf49dcb1
Normalized target SHA256: 435560ad975b9affbb0f4875d838f956a6c49ebdec2c32d2f55013332c22870a
Isolated source SHA256: fa5c3de8a7a24808b7ea63f0906458472c7cd8c9e1920ae06ffb962cc7899cbe
Raw / prior-28-row / new-31-row differences: 200 / 172 / 169
```

## Bounded Heading Proof

Only words **469..477**, `0x150F3C48..0x150F3C68`, are newly normalized.
Source yaw GPR11 maps to retail GPR13; source adjusted-yaw GPR12 maps to
retail GPR14. The LH, ADDIU and MTC1 words at offsets `0x754`, `0x760`, `0x764`
change. No relocation is present on them. Other instructions, FP fields,
memory addresses, immediate values and instruction order remain unchanged.

Unlike the prior windows, this one does **not** end at a call. Its verifier
therefore checks both directions of the lifetime boundary. Both source roles
have exactly one definition before their single use; mapped targets do not
collide with a used identity register. The complete routine is scanned for
interior/computed entry, and all nine transformed words must equal retail.
A separate **400-state continuation scan** requires every one of the four
affected physical registers, GPR11/12/13/14, to be redefined before any later
read. ABI clobbers at subsequent calls are not used to excuse a read.

The private CSV preserves the preceding 28-row table as an exact byte prefix
and appends only the three expected-word rows. Actual full-owner padding and
linking reproduce the independently computed vector, change 39 target bytes
in 31 words, retain all target relocation metadata and all eleven neighbors,
and keep the complete slot. Production CSV, source and ELF are untouched.
Arbitrary unpassed-provider observations, raw private register identity and
hardware/FCSR/gameplay equivalence remain outside the claim.

## Qualification

The complete **twelve-test run passes in 173.520s**:

- Forty-six source/extent controls, four actual overflow rejections, real
  owner padding, unchanged pools/bindings and eleven raw/padded neighbors.
- **32 effective heading controls** reject input-word/FP corruption, relocations,
  invalid maps, interior/computed control, identity collisions, altered extent,
  replacement/boundary changes and reads of each of the four physical roles
  before a continuation definition. Two additional actual padder controls reject
  a stale expected word and unexpected relocation.
- **480 non-call kernel cases**: sixteen poisoned GPR/FPR seeds, five signed
  yaw values, three guest actor bases and two stack phases. Tests stop before
  the next flag load, require exactly one data access and no callback, and
  compare complete RAM, FP state, events, identity registers and both roles.
- Three-way retail/raw/normalized execution of **2,496 public cases**, twenty
  modeled FP edges, nine provider-mutation modes and the actual 21-word curve.
  All 947 reachable retail words remain covered; twelve original unreachable
  duplicate words are retained. The 36 cap cases still pass with 24 gates fired.
- **200 release cases** cover all 25 valid slots, control/pressed-button gates
  and both stack phases. Fifty actually enter the release multiply. Another
  **100 overlapping-speed cases** cover all slots, phases and RAM patterns,
  using actual retail and rejecting the old late-read candidate every time.
- The existing sixteen signed-Y guest aliases/older-candidate rejections and
  forty clamp cases/two compiled wrong-limit controls pass again. The prior
  eight AST-zero negative controls remain prior receipts; the positive unescaped
  zero-lifetime check re-runs on this selected complete source.
- **100 active states / 6,700 equal normalized fault prefixes**, up from 6,600.
  The new first frontier is `0x150F3C88`, GPR10/13/14/15/25 only; RAM and all
  FPRs agree there. All hundred prior-28-row controls still reject one access
  earlier at `0x150F3C6C`. All 80 disabled final states / 2,700 prefixes and
  160 mode-0 final states / 8,320 prefixes remain equal.
- Native32 O2/O0 UBSan: **369 cases/profile**, eight effective controls,
  including 200 new ordinary release cases. Actual normalized-object rebases
  pass two links/twelve cases and twelve established guest aliases agree.
  The new overlapping-structure cases stay guest-only.
- A new owned compiler capture finishes exit0 and equals the normal complete
  owner target: **74 emitter events / 687 actual AS1 instruction records**.
  Frontend locals grow from 84 to **88** for the real signed index; optimizer
  locals remain 76, rounded locals80, frame128, saved16/outgoing32. Earlier
  homes and emitted entry saves are unchanged. The new index is frontend J4
  M-88 and optimizer J4 R4, not inert padding. **41 effective layout/instruction
  controls** reject altered homes, budgets, event identity and emitted sites.
  Research-normalized output is not attributed to AS1.
- All 309 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

## Banked Baseline And Continuation

Tools **201eff8** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks; four ASCII/AST parses and two identical task
pairs pass. Both mirror destinations were absent. All **1,166** prior hashes
and HEAD `ddbdd16b` survive, with **1,168** dirty paths afterward. No mirror
commit/reset/clean, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init492/492 and
Debugger181/181 remain exact among converted functions. Root README remains
unchanged. No production build, host-port or frozen Release action.

Scoped AST graph refresh completes with **42,315 nodes / 82,440 links / 3,933
communities**. The new note is indexed; only three shifted UPDATE_LOG heading
IDs disappear, with their labels retained at new locations. All 19,398 existing
excluded nodes from 2,972 still-present files remain preserved; no purge or
full re-extraction is performed.

```sh
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group release
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group pitch
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group flow
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group tail
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group literal
python3 -m tools.experiments.game_actor_input_movement_release_addressing --group copy
python3 -m tools.experiments.game_actor_input_movement_release_addressing --normalize
python3 -m tools.experiments.game_actor_input_movement_release_addressing --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_release_addressing -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Complete sources, objects, private guards, the successful owned trace and
qualification receipts are under
`conker/build/game-actor-input-movement-release-addressing/`. Earlier immutable
captures are untouched. Revalidate the successful trace rather than restarting it.

- [x] Recover the signed release index, speed read order, compound pitch add
  and comparison literal type, improving real C differences by 70.
- [x] Prove/qualify only the three dead heading-role words at the non-call
  boundary; no global rename or production patch is introduced.
- [ ] Continue **the same function** at normalized word478 / `0x150F3C6C`:
  source flag load uses GPR13, retail GPR10. Following flag/constant roles
  diverge at private frontier `0x150F3C88`; prove separate bounded lifetimes.
- [ ] The remaining audit has 97 GPR-field-only differences and 72 other words.
  This is classification, not permission to rename globally. Address the FP
  equality operands at `0x150F3D44`, coefficient/load/store scheduling near
  `0x150F3E1C`, and surfacing control/FP ordering around `0x150F4130..4234`.
  Existing whole-function coefficient carriers were worse; a block-local
  coefficient snapshot is a hypothesis, not an implemented recovery.
- [ ] Finish all remaining literal/private/caller/provider/first-image gates
  before installation, and keep the wider Game goal open.
