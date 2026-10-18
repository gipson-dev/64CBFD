# Movement Scalar Lifetimes And Counter Scope

Verified 2026-10-17. Consumer predecessor `499b6495`, tools predecessor
`74c3bf7`; both active repositories began clean. The preceding turn was
progress. Continue the same complete `func_150F34F4` from
[Note1522](1522-movement-pitch-and-surface-source-order-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

Recovered C scalar lifetimes improve **152 to 139 raw word differences**, or
**121 to 108** with the byte-identical 31-row private research table. All
thirteen gains emit directly from C. No new research/production guards,
insertions, omissions, installation or matching credit.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 139 | 108 |
| Exact opening words | 361 | 478 |
| First unequal PC | `0x150F3A98` | `0x150F3C6C` |

## Source Recovery

`tools/experiments/game_actor_input_movement_scalar_lifetimes.py` protects
**313 predecessor entries / 289 distinct paths**. Twenty-seven complete
forms screen zero operand spelling, counter initialization, pointer scope,
explicit loop-end pointers, counter reuse, final threshold spelling and
snapshots, inline speed sampling, and measured combinations. All forms retain
959 words/frame0x80, eleven raw/padded neighbors and unchanged owner pools.
None is trimmed or padded to fake a complete source recovery.

- `if (contactHeight == acceleration)` recovers the retail FP equality
  operands at `0x150F3D44`. The same local on the right is optimized back to
  the baseline. This local is still its initial zero at the comparison.
- A real block-local `MovementActor34F4 *countRecord` replaces the shared
  record temporary only in the active-object counter. The count, cursor and
  bound now use retail's V1/V0/A1 roles, recovering ten raw words. The pointer
  traverses **24 records**, `0x800CC5FC..0x800D121C`, exclusive end, at stride
  `0x32C`: slots 1..24 of the 25-slot table, excluding the player's slot zero.
- Sampling the final speed in `if ((value = actor->speed) < 20.0f && ...)`
  recovers the independent MTC1/LWC1 order at `0x150F434C/50`. A reversed
  comparison with the same assignment emits identical bytes. Integer/reversed
  constant spelling and four separate threshold snapshots do not help;
  double comparison worsens the match and the old role verifier refuses its
  unsupported FP instruction rather than normalizing it speculatively.

Counter initialization moves alone do not improve the full candidate. Reusing
`index` gains three words, but reusing `heldIndex` perturbs the early routine
and worsens the raw count to 305. A local `cursor` emits the same bytes as the
selected descriptive `countRecord`. Explicit loop-end pointers improve some
isolated forms but worsen the combined pointer/zero candidate; these remain
rejected controls. In particular, `0x150F4098/9C` are **not** recovered yet.

The selected complete form is `count-pointer-zero-speed-left`. Of **nineteen
changed raw words, thirteen become exact and zero previously exact words are
lost**. The remaining six changed words still differ. The earlier surface,
release, clamp and pitch recoveries are retained.

The zero-lifetime proof is extended structurally, not waived. It preprocesses
and parses C, verifies the additional comparison's exact operands and scope,
requires the actor acceleration/velocity samples to precede it, and rejects
an enclosing loop. The prior AST proof still verifies the rest of the body:
initial zero dominates, the pitch use is earlier than the only update to 50,
there is no address escape, and the only goto is the forward disabled path.
There are now **five identifier uses / two writes**. New comparison line197
precedes pitch line220 and the update at line233 in the parsed body.

```text
Factory: tools.experiments.game_actor_input_movement_scalar_lifetimes.selected_body()
Form: count-pointer-zero-speed-left
Raw target SHA256: bb6adfabfc1313eacf798fce43423b75eea912051212638b373e18e1808235eb
Normalized target SHA256: e78c78662ddcf369e8aaa8fbdcc0946c92b57fbc2ade58c5c023f8474f931987
Isolated source SHA256: 2727840689183c6453d7e407639ddbd86d4088cefadd8bdaa53a7c6c12cb9eea
```

Actual owner padding/linking equals the independently computed role vector.
`expected-scalar-guards.csv` is byte-identical to the previous surface table;
the same 31 words / 39 target bytes change, with target relocations and all
eleven padded neighbors preserved. The existing heading certificate still
checks 400 continuation states. Research-normalized bytes are not attributed
to the C compiler or AS1, and raw private-register identity is not an ABI claim.

## Qualification

The first full **fifteen-test run passes in 178.135s**:

- All 27 complete source/object/link controls, measured 19/13/0 change/gain/loss,
  real owner padding, 959-word extents, unchanged pools and eleven neighbors.
- **Twelve effective AST controls**: the earlier eight zero-lifetime negatives
  rerun, plus four comparison loop/input/order controls. The positive five-use
  zero proof reruns on the selected complete body.
- All 32 heading-role negative controls, **480 poisoned non-call kernel cases**
  and both actual stale-word/unexpected-relocation padder controls rerun.
- Full retail/raw/normalized **2,496-case public corpus**, twenty modeled FP
  edges, nine effective provider-mutation modes, actual 21-word curve and
  947 reachable retail words. Twelve original unreachable duplicates remain;
  all 36 cap cases pass, with 24 gates fired.
- All 200 release cases across 25 valid slots / fifty actual multiplies,
  hundred speed/flags overlaps and old late-speed-read rejections, sixteen
  signed-Y aliases/older-candidate rejections, and forty clamp cases with two
  freshly compiled wrong-limit controls rerun.
- **400 new counter cases / 320 spawn calls** vary all 25 table slots, active
  words, kind bytes, stack phases and RAM patterns. Every object reads exactly
  slots 1..24 in order, with no slot-zero or end-record read. Actual retail
  agrees on public RAM, call packets, observations and fired gates. Two actual
  compiled controls, including the player slot or changing the limit to four,
  are rejected at a real four-record threshold, not by crashing or skipping it.
- Native32 O2/O0 UBSan: **397 cases/profile**, eight effective controls,
  including 28 new count/pressed-button cases. Actual normalized-object rebases
  pass two links/twelve cases and twelve established guest aliases agree.
- The prior **256 surface kernel cases / 128 global overlaps / sixteen old
  global-read rejections / 224 callback cases** rerun against actual retail,
  comparing complete RAM/FPRs and semantic packets at the bounded stop.
- **100 active states / 6,700 equal normalized fault prefixes** still stop
  at `0x150F3C88`, GPR10/13/14/15/25 only, RAM/FPRs equal. All hundred prior
  28-row controls reject at `0x150F3C6C`; eighty disabled final states / 2,700
  prefixes and 160 mode-zero final states / 8,320 prefixes remain equal.
  Later scalar recovery does not advance that earlier private frontier.
- Fresh owned compiler capture: **74 emitter events / 687 actual AS1 records**,
  normal/observed target bytes and relocations identical. Frontend grows from
  88 to **92** for the used A4 pointer at M-92; optimizer places it in R2.
  Earlier homes, J4 release index M-88/R4, optimizer76, rounded80, frame128,
  saved16/outgoing32 are retained. **47 effective layout/site controls** reject
  changed homes/types/widths, budgets, event identity and emitted instructions.
- All 313 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

These are C/ABI and modeled guest checks. Partial-structure/global overlaps
remain guest-only; arbitrary caller-stack aliases, unpassed-provider private
observations, full private equivalence, general FCSR, hardware and gameplay
acceptance are not established by these tests.

## Banked Baseline And Continuation

Tools **5910e6c** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks; four ASCII/AST parses and two identical task
pairs pass. Both new mirror destinations were absent. All **1,170** prior
hashes and HEAD `ddbdd16b` survive, with **1,172** dirty paths afterward.
No mirror commit/reset/clean, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Totals remain Game **2,965 / 4,828 (61.41%)**, total **3,638 / 5,501 (66.13%)**,
1,863 different, zero drift; Init492/492 and Debugger181/181 among converted
functions. Main README remains unchanged. No production build, host-port or
frozen Release action, and no host-runtime synchronization claim.

Scoped AST graph refresh completes with **42,329 nodes / 82,452 links / 3,970
communities**. The new note is indexed. Only three shifted UPDATE_LOG heading
IDs disappear, with their labels retained at new locations; no unrelated
entries are lost. All 19,398 existing excluded nodes from 2,972 still-present
files remain preserved, with no purge or full re-extraction.

```sh
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --group zero
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --group count
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --group final
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --group coupled
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --normalize
python3 -m tools.experiments.game_actor_input_movement_scalar_lifetimes --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_scalar_lifetimes -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Sources, objects, guarded owner/link receipts and the successful owned trace
are under `conker/build/game-actor-input-movement-scalar-lifetimes/`. Revalidate
the completed trace; do not restart it just to inspect its results.

- [x] Recover zero comparison, independent counter pointer and inline final
  speed sample: thirteen new raw C-exact words, no formerly exact losses.
- [x] Qualify the five-use zero lifetime, exact 24-record counter scan, two
  compiled wrong count gates, expanded native corpus and fresh pointer home.
- [ ] Continue **the same function**, normalized word478 / `0x150F3C6C` and
  private frontier `0x150F3C88`. There are **101 GPR-field-only differences and
  seven other words**. Classification does not authorize a global rename.
- [ ] The seven other PCs are coefficient/read/store ordering at
  `0x150F3E1C/24/28/30/34` and loop-address setup at `0x150F4098/9C`.
  Reuse the negative coefficient/end-pointer screens rather than repeating
  them blindly. Bounded role proofs must cover entry, definitions, branches,
  identity collisions and live-out uses, not just visual register similarity.
- [ ] An untested coefficient hypothesis is to keep the early B8 snapshot in
  `pitchValue` and the coefficient in `value`, rather than the previously
  rejected coefficient carriers. Measure the complete source and its actual
  read/store order before retaining any such candidate.
- [ ] Finish remaining literal/private/caller/provider/first-image gates
  before installation. Keep the gate, both fade lifetime gaps, full runtime
  acceptance and the wider Game matching objective open.
