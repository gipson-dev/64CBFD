# Movement Coefficient Read Store Schedule

Verified 2026-10-17. Consumer predecessor `3fc44cd5`, tools predecessor
`5910e6c`; both active repositories began clean. The previous turn was
progress. Continue the same complete `func_150F34F4` from
[Note1523](1523-movement-scalar-lifetimes-and-counter-scope-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

The pitch coefficient read/store schedule now emits directly from C,
improving **139 to 134 raw differences**, or **108 to 103** after the same
31 private research rows. Exactly **five words change, all five become
retail-exact, and zero formerly exact words are lost**. No new research or
production guards, inserted/omitted words, installation or matching credit.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 134 | 103 |
| Exact opening words | 361 | 478 |
| First unequal PC | `0x150F3A98` | `0x150F3C6C` |

## Source Recovery

`tools/experiments/game_actor_input_movement_remaining_schedules.py` protects
**315 predecessor entries / 291 distinct paths**. The historical run directory
is `conker/build/game-actor-input-movement-pitch-coefficient/`; the module also
records the measured counter-address controls. Thirty-two complete forms all
retain 959 words/frame0x80, eleven raw/padded neighbors and owner pools.

The selected `dataflow-423` places the compound pitch calculation before
the independent zero stores, retaining the coefficient as an expression
temporary rather than introducing a separately allocated FP local:

```c
index = D_800CC284->y;
value = actor->valueB8;
actor->valueB8 += (((f32)index - value) * D_800A19C4);
actor->verticalVelocity = 0.0f;
actor->acceleration = 0.0f;
```

The actual compiler schedules both zero stores before the final B8 store,
using the FP latency slots. The emitted sequence matches retail at all five
previously different PCs:

| PC | C-Emitted Retail Instruction |
| --- | --- |
| `0x150F3E1C` | LUI AT, coefficient high address |
| `0x150F3E24` | LWC1 F8, coefficient |
| `0x150F3E28` | SWC1 F16, actor vertical velocity |
| `0x150F3E30` | LWC1 F2, actor vertical velocity |
| `0x150F3E34` | SWC1 F16, actor acceleration |

The final B8 store remains in the branch delay slot at `0x150F3E48`. No extra
coefficient local, dummy operation or artificial padding is introduced.

The thirty-two controls also establish useful negative results:

- B8/coefficient carriers using `pitchValue`, `previousInput`, `magnitude`,
  `amount` and `value` recover an early load but allocate the coefficient in
  F12 and worsen the complete raw count to 226/231. Explicit addition does
  not fix the allocation. These are rejected, not retained semantic fixes.
- Typed/reversed counter bounds and preincrement spellings emit the same
  139-difference predecessor. `0x150F4098/9C` remain different.
- `D_800A19C4` is verified in `246440.rodata.s`, word `0x3E4CCCCD` (0.2f).
  Its scoped const declaration emits identical predecessor code; no qualifier
  change is selected or applied to shared declarations.
- Three separate cast carriers and the advisory's source variant emit the
  139-difference predecessor. Other compute/store permutations are worse or
  equal; reversing the two zero stores after the early calculation gives 136.
- Four inline-Y/B8 controls give 134 differences, with either identical bytes
  or an equal-score GPR variant. They do not improve the retained profile.

```text
Factory: tools.experiments.game_actor_input_movement_remaining_schedules.selected_body()
Form: dataflow-423
Raw target SHA256: 4a4c3574716a6ab788981a28d6af57e8bd46c6c01d6a92aed2c100edfc38b5a7
Normalized target SHA256: 0e13d4c7659efcacf847a1f0abc249b0e24eeaecb851a2fee1586a642aa3445b
Isolated source SHA256: 0b89776bd3c14abb3f18407fb0f45af318c1803add086c3b60960fdce1b52980
```

Actual owner padding/linking agrees with the independently computed role
vector. `expected-schedule-guards.csv` is byte-identical to the prior scalar
table: 31 words / 39 bytes, unchanged relocations and eleven padded neighbors.
The prior heading proof still checks 400 continuation states. No research
normalization is falsely attributed to the C compiler or AS1.

## Qualification

The final full **sixteen-test run passes in 175.995s**. The first full run's
only failure was the final count assertion in the new kernel: all 640
behavior cases passed, but the expected cardinality had been calculated as
1,280. That bookkeeping was corrected to **640 cases / 320 rejections**,
four additional inline controls were measured, and the complete suite rerun.

- All 32 source/object/link controls, actual five-word delta, unchanged pools,
  eleven neighbors, full extents/frame and byte-identical private CSV.
- Twelve fresh AST zero-lifetime controls, the five-use/two-write positive
  proof, 32 heading-role negatives and 480 poisoned non-call kernel cases.
- Full retail/raw/normalized 2,496 public cases, twenty modeled FP edges,
  nine effective provider-mutation modes, actual 21-word curve, 947 reachable
  retail words and twelve retained unreachable duplicates. All 36 cap cases
  pass with 24 gates fired.
- All 200 release cases / fifty multiplies, hundred speed/flags overlaps and
  old late-speed rejections, sixteen signed-Y aliases, forty clamp cases/two
  compiled wrong limits, and 400 exact 24-record scans / 320 spawn calls with
  both compiled wrong start/threshold controls rerun.
- Native32 O2/O0 UBSan: 397 cases/profile, eight effective controls, two actual
  normalized-object rebases/twelve cases and twelve established guest aliases.
- The 256 surface kernel cases / 128 global overlaps / sixteen old-read
  rejections / 224 callback cases rerun against actual retail.
- **640 new coefficient-kernel cases** cover four actor bases, two aligned
  controller locations, five signed Y values, two stack phases, two RAM
  patterns and four poisoned GPR/FPR seeds. Actor VV, acceleration or B8 may
  overlap the coefficient; controller Y may overlap a velocity byte. Actual
  retail, raw and normalized candidates agree on complete RAM, all FPRs,
  access events, LO and FP condition, with exactly ten accesses each and no
  callback executed before the bounded stop at `0x150F3EBC`.
- The previous 139-difference C is effectively rejected in **320** of those
  cases, when its late coefficient read observes the cleared VV/acceleration
  word. The high-level reference is not substituted for actual retail in
  these new overlaps. Partial-structure aliases remain guest-only.
- Private frontier remains `0x150F3C88`: 100 active states / 6,700 equal
  normalized fault prefixes, RAM/FPRs equal, GPR10/13/14/15/25 different. The
  hundred prior-28-row controls reject earlier at `0x150F3C6C`; eighty disabled
  states / 2,700 prefixes and 160 mode-zero states / 8,320 prefixes stay equal.
- Fresh owned compiler capture is normal/observed byte-and-relocation
  identical: **74 emitter events / 687 AS1 records**. Frontend92, optimizer76,
  rounded80, frame128, saved16/outgoing32 and all prior homes remain unchanged.
  The 47 existing layout/site negatives plus five new pitch-order corruptions
  give **52 effective controls**. No new coefficient FP-local allocation.
- Both real stale-word/unexpected-relocation padder controls, all 315 protected
  entries, 6,057 installed bodies, 189,088 Game-data bytes / 720 owners,
  callback slot `0x80086068` and ten immutable first-image members.

These are C/ABI and modeled guest checks, not arbitrary private-register,
caller-stack, native alias, general FCSR, hardware or gameplay acceptance.

## Advisory Reconciliation

One bounded packet-only Claude analysis was used for the difficult scheduling
question. Live CLI auth reported `claude.ai` / Pro; the requested Sonnet model
reported `claude-sonnet-5`. Safe mode, disabled built-in tools, strict empty
MCP, no browser and no session persistence were selected. No second call.

Packet SHA256:
`dc92089f8cfe8546eb18563e98bab1f7974b1bbbb5cbf2e9bb82d1b9a8f6992b`.
The packet/reconciliation are in the ignored target build directory, not the
tools repository. The review's explanation described a store/load ordering
contradicted by retail PCs; that explanation and fragment-only compilation
were rejected. The separate-cast/variant-A hypotheses were tested on the full
owner and did not improve it; its variant B duplicated the baseline. The
retained early-calculation hypothesis was independently formulated by Codex
and is supported by the actual compiled words and guest tests, not the review.

## Banked Baseline And Continuation

Tools **12befaa** is committed first. Both local tools copies freshly pass
twelve shared tests and smoke checks; four ASCII/AST parses and two identical
task pairs pass. Both mirror destinations were absent. All **1,172** prior
hashes and HEAD `ddbdd16b` survive, with **1,174** dirty paths afterward.
No mirror commit/reset/clean, push, dependency update or frozen Release action.

Production ELF remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total **3,638 / 5,501
(66.13%)**, 1,863 different, zero drift; Init492/492 and Debugger181/181 among
converted functions. Main README is unchanged. No production build or host
port change/synchronization claim.

Scoped AST graph refresh completes with **42,337 nodes / 82,459 links / 3,999
communities**. The new note is indexed. Only three shifted UPDATE_LOG heading
IDs disappear, with their labels retained at new locations; no unrelated
entries are lost. All 19,398 existing excluded nodes from 2,972 still-present
files remain preserved, with no purge or full re-extraction.

```sh
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --group coefficient
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --group loop
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --group qualifier
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --group dataflow
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --group inline
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --normalize
python3 -m tools.experiments.game_actor_input_movement_remaining_schedules --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_remaining_schedules -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover all five coefficient read/store words directly from C, without
  an extra FP local, new guards, lost exact words or extent/frame change.
- [x] Qualify the actual-retail coefficient overlaps, old-C rejections,
  complete public/native corpus and new normal/observed compiler capture.
- [ ] Continue the same function: **101 GPR-field-only differences and two
  other words**, the independent address-setup order at `0x150F4098/9C`.
- [ ] Qualify the next bounded role window: words478..626, PC
  `0x150F3C6C..0x150F3EBC`, ending at the `func_15059140` call/delay slot.
  Static reconnaissance finds fifteen register-field differences and the
  consistent map `{13:10,14:15,25:13,10:24,15:25,24:11,3:12}`. All 149
  transformed words equal retail, with no incoming interior edge or identity
  collision; existing scans traverse 127 local / 1,457 continuation states.
  This is **not a qualified certificate or new guard set**. Negative controls,
  poisoned kernel/call ABI, actual padder/relocations and new private-prefix
  gates are still required. Without those changes the first literal mismatch
  remains word478, not the hypothetical next word633.
- [ ] Keep remaining literal/private/caller/provider/first-image gates,
  the gate, both fade lifetime gaps, full runtime acceptance and wider Game
  objective open. Do not globally rename or install this incomplete candidate.
