# Movement Controller Allocation And Pickup Access Order

Verified 2026-10-17. Consumer predecessor `e63e0b5c`; tools predecessor
`f0fadc5`. Both active repositories began clean. The preceding goal turn was
progress, not a blocked wait. This continues the same complete `func_150F34F4`
from [Note1513](1513-movement-retail-extent-frame-and-live-homes-20261017.md).

Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`:
**959 words / 3,836 bytes, frame `0x80`, now 721 unequal words instead of 744.**
The first 66 words are exact. This is an uninstalled research candidate, not a
byte-exact recovery or additional converted/matching credit. No new guards,
compiler profile, executable trimming, inserted padding or production edit.

## Allocation Cause And Complete Source

`tools/experiments/game_actor_input_movement_allocation.py` builds complete
source forms using existing owner/compiler/link/padder helpers. All 292
protected predecessor entries / 269 distinct paths are fingerprint-locked.
Existing frame, recovery, compiler-observer and oracle modules are unchanged.

The previous candidate's controller local is assigned V1/GPR3 by UOPT. Simply
using the global instead does not recover retail: the complete global-only
control still reserves GPR2..10 and UGEN uses T3/GPR11 for the controller.
The later pickup/release block carries a repeated `-81200` address constant in
GPR9 and the table base in GPR10. This explains why changing only the opening
declaration did not free retail's T2 temporary.

The new complete form uses these real source changes together:

- Recover global controller assignment/access instead of retaining the
  separately promoted controller local.
- Give the disabled path's `(held - 100)` a real signed index before record
  scaling, rather than folding the subtraction into the final byte address.
- Read the nearby record's indexed position before writing actor velocity,
  consistent with retail's actual access order. This avoids reloading the
  nearby ID and recalculating its address after an alias-visible actor store.
- Restore the early narrowed heading update before its magnitude selection.
  Unsigned 32-bit addition followed by u16 narrowing preserves wrap without
  introducing signed C overflow. It emits the same complete words as the
  measured compound-assignment form.
- Put the disabled record's speed assignment immediately after its held-by
  clear. The emitted words 67..105 now also equal retail, including the
  subtract/scale sequence and real actor-speed/flags load order.

The selected source and raw object are:

```text
Factory: tools.experiments.game_actor_input_movement_allocation.selected_body()
Form: first-heldIndex-heading-release-speed
Raw SHA256: b87c2558ec5faccd9da9c0214da280fcc06cfbc5e16a152a067ea4732f95e181
Isolated source SHA256: cf6cba369653beb53b03e0b59c7ccd563995d54735a5f267dd1a7029c77a9474
Words/frame/differences: 959 / 0x80 / 721
First unequal word: 66, VA 0x150F35FC
```

## Qualified Compiler Evidence

Two fresh owned-compiler captures, for the selected form and global-controller
control, complete with normal-object identity. A further final selected CLI
capture passes the strengthened revalidation path. Each binds actual source
content/hash, prepared cc/CFE/UOPT/UGEN fingerprints, fired probes, complete
producer/consumer/driver exits, decoded input hashes, complete normal/traced
functions and relocations/pools, and whole-owner versus isolated target equality.
No compiler installation, modified executable or user-debugger attachment.

| Complete Form | UOPT Volatile GPR Reservation | Initial Controller | Address Constant Carrier | Differences |
| --- | --- | --- | --- | ---: |
| Previous fitted form | GPR2..10 | V1/GPR3 | GPR9: `-81200` | 744 |
| Global-only control | GPR2..10 | T3/GPR11 | GPR9: `-81200` | 763 |
| Selected source | **GPR2..9** | **T2/GPR10** | No address-constant carrier | **721** |

The selected optimizer wire advertises `[1,8,2]` instead of `[1,9,2]`.
Its first controller indirect load feeds the actual global-address store, not
an explicit V1 store. Emitted controller load, global store and x-byte clear
all use T2. The table base moves from GPR10 to GPR9; stride 812 remains in GPR8.
This establishes the candidate's compiler allocation, not the unavailable
original source declarations or a replay of retail's original compiler run.

The existing strict frame/home checker also passes unchanged: frontend local
bytes 84, optimizer local bytes 76, rounded UGEN locals 80, frame 128, saved-area
budget 16 and outgoing budget 32. All seven source homes and the five emitted
contact/angle/call-save sites checked in Note1513 remain valid; no late growth.

## Complete Screens And Acceptance Boundary

Thirty-seven complete source forms are compiled this turn. Their retained
source text, raw object hashes, linked shapes and owner receipts are separately
revalidated: 13 overflow rejections, 12 short forms and 12 full-length forms.
All preserve eleven raw owner neighbors and pools; non-overflow forms also
preserve all eleven padded neighbors. Short forms are not counted as matches.

Representative controls:

| Form | Words | Frame | Overlapping Unequal Words | First Unequal Word |
| --- | ---: | --- | ---: | ---: |
| Previous fitted / register or integer carrier | 959 | `0x80` | 744 | 17 |
| Global-only controller | 959 | `0x80` | 763 | 17 |
| Global controller plus pickup order | 960 | `0x80` | 707 | 66 |
| First link index plus early heading | 959 | `0x80` | 731 | 66 |
| Selected plus recovered release-speed order | 959 | `0x80` | 721 | 66 |

Overflow, short, pointer-reuse and intermediate out-of-array pointer controls
are source-shape measurements only, not adopted portable-C recoveries. Direct
selected array accesses use the final valid record index. Explicit return
spelling alone produces identical words and does not repair the return gap.
Raw and padded selected target words are identical across the complete slot.

## Fresh Qualification

The final **eight-test run passes in 46.048s**:

- 2,496 complete public core/width/filter/mutation cases plus 20 modeled FP
  edges. All 256 stick-byte/cooldown values and nine effective provider
  mutation modes remain covered; all 947 reachable retail words are exercised.
- The twelve original unreachable duplicate words remain in retail and are
  required for literal matching; reachability does not waive them.
- Two independent text rebases / twelve complete cases, actual 21-word curve
  execution and complete public call/packet snapshots.
- Native32 O2/O0 with UBSan, **139 cases per profile**, including nine added
  unsigned heading-extreme cases. Eight negative controls fail actual semantic
  gates. The nine heading cases also pass retail/candidate/model guest checks.
- Twelve guest input-packet aliases with the controller global, pressed-input
  global or pointer slot. No general native pointer-alias claim.
- Sixteen effective reservation/wire/machine controls and an additional
  effective old-controller word control at fault cut 10.
- All five input gates across two stack phases and two byte patterns:
  **20 initial states / 460 equal complete fault-prefix states**. LO and the
  modeled FPU condition are compared explicitly as well as the existing
  register/stack/memory/call/PC state.
- All 292 protected entries, all 6,057 installed bodies, 189,088 Game-data
  bytes / 720 owners, the callback slot and ten immutable first-image members.

For the same eight initial states from Note1513, equal prefixes increase from
80 to 200. The broader five-gate first remaining cuts are `[21,29,20,22,23]`.
All twenty combinations still reject at **retail PC `0x150F36B4` versus
candidate PC `0x150F36B0`**. Memory, GPRs, FPRs, LO and modeled condition agree
there; PC/branch provenance does not. This closes the old controller mismatch,
not full private/fault, opaque-provider, hardware or gameplay acceptance.

The first unittest-loader launch reached the pre-existing historical import
chain's recursion limit. Direct module execution below succeeds without a
dependency or Python-configuration change. An initial direct eight-test run
also exposed a receipt keyword collision; that test-only naming error is
fixed, and the final entire run above passes. Neither failed launch is counted
as passing qualification.

## Banked Baseline And Next Work

Tools **f63eb42** is committed before the consumer docs/pin. Both local tools
copies freshly pass twelve shared tests plus smoke checks. Four ASCII/AST
parses and two identical task pairs pass. Both mirror destinations were absent;
all 1,152 predecessor hashes and HEAD `ddbdd16b` survive, with 1,154 dirty paths
afterward. No mirror commit/reset or push.

The installed ELF remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different and zero drift. Init 492/492 and
Debugger 181/181 remain exact among converted functions. Root README is
unchanged. No production rebuild/installation, host-port or frozen Release
action, dependency update or Claude call.

```sh
python3 -m tools.experiments.game_actor_input_movement_allocation --group basic
python3 -m tools.experiments.game_actor_input_movement_allocation --group structural
python3 -m tools.experiments.game_actor_input_movement_allocation --group direct
python3 -m tools.experiments.game_actor_input_movement_allocation --group pickup
python3 -m tools.experiments.game_actor_input_movement_allocation --group first-link
python3 -m tools.experiments.game_actor_input_movement_allocation --group combined
python3 -m tools.experiments.game_actor_input_movement_allocation --group returns
python3 -m tools.experiments.game_actor_input_movement_allocation --capture --form global-controller
python3 -m tools.experiments.game_actor_input_movement_allocation --capture
python3 -m tools.tests.test_game_actor_input_movement_allocation -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned receipts are in `conker/build/game-actor-input-movement-allocation/`,
including `traces/`, complete source screens, shape, public, native, rebases,
aliases, prefix and protected-input results. Older unchanged suites remain
prior receipts, not fresh tests.

- [x] Close the initial controller allocation gap without a register/word guard.
- [x] Qualify the complete 959-word/frame-0x80, 721-difference successor and
  preserve every installed byte/checkpoint. Do not install it as byte-exact.
- [ ] Continue the same `func_150F34F4` at word 66 / `0x150F35FC` and the
  disabled-path tail at `0x150F369C`: candidate delays the held-byte clear into
  its return branch, while retail has the clear before a branch-delay RA load
  and another unreachable mode-byte load. Recover actual control-flow and
  scheduling; do not insert a dummy word or treat 721 differences as a patch list.
- [ ] Require every one of 959 literal words, appropriate complete private/
  fault/rebase/caller gates and a byte-exact full first image before installation.
- [ ] Keep the gate, both fade lifetime gaps, full opaque-provider/runtime
  acceptance and wider Game goal open. Do not move to `func_150F43F0` yet.
