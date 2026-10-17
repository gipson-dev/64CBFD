# Movement Return Boundary And Full-Width Buttons

Verified 2026-10-17. Consumer predecessor `5a0df533`; tools predecessor
`f63eb42`. Both active repositories began clean. The previous goal turn was
progress. Continue the same complete `func_150F34F4` from
[Note1514](1514-movement-controller-allocation-and-pickup-access-order-20261017.md).

Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`:
**959 words / 3,836 bytes, frame `0x80`, now 475 unequal words instead of 721.**
The first **137 words** are exact, including the formerly different disabled
return. The candidate remains uninstalled and earns no matching/conversion
credit. No new guards, compiler profile, executable trimming or dummy padding.

## Real Return And Button Recovery

`tools/experiments/game_actor_input_movement_return.py` preserves the prior
helper and all 297 protected predecessor entries / 273 distinct paths. It
reuses complete owner compilation, linking, padding, frame observation and
binary-assembly parsers, without modifying shared helpers or compiler binaries.

The successful source changes are:

- A real `disabled_done` join and explicit return inside the disabled branch.
  The zero-held case jumps to that local exit; the release case reaches it after
  clearing the held byte. Retail's clear-before-branch, branch-delay RA load and
  unreachable mode-byte load now emit naturally. Return spelling or a global
  exit alone did not achieve this.
- A distinct **u32 `buttons`** snapshot instead of reusing the u16 angle local.
  The old narrowed lifetime required an extra `move V0,V1` in the active button
  block. A separate u32/s32, or a reused existing 32-bit local, removes that
  executable word; a separate u16 reproduces it. The explicit u32 name is kept.
- Place the unsigned narrowed heading advance before the default yaw copy,
  and read that copy through the corresponding unsigned halfword view. This
  recovers more of retail's load/preload order while preserving the signed yaw
  used by the facing-angle calculations. The unsigned heading addition remains
  defined at 32-bit wrap boundaries.

No heading read is removed merely to fit the slot. The local-exit-only form was
960 words / 605 overlapping differences. Reintroducing a conditional heading
read made a 959-word control but worsened the fit to 693. Keeping retail's
unconditional heading access and recovering the full-width buttons instead
gives the complete 959-word successor.

```text
Factory: tools.experiments.game_actor_input_movement_return.selected_body()
Form: heading-before-unsigned-yaw
Raw SHA256: ba72844ce4ee23c39a00a669951e6ab8891c58104360f4fceaf605879acee082
Isolated source SHA256: 4f6e0feb2127302dbf15ae845f3a4d2768fab41cd28dccd67dd37fd4e8c2f395
Words/frame/differences: 959 / 0x80 / 475
First unequal word: 137, VA 0x150F3718
```

## Proven Backend Boundary

The new observer composes the existing frame transport with the qualified
finalizer emitter/AS1 collector and parser. It additionally fingerprints the
prepared AS1 executable:

```text
dc18ffdd8cb629eaf71489507d4186674d44b9aa86bf26d8821d4e138e9ab2b6
```

Four completed owned captures qualify the old source, local-exit-only control,
separate-u32-buttons intermediate and final selected source. A further final
selected CLI capture exercises the new live-probe guard. All require actual
cc/CFE/UOPT/UGEN/AS1 lifetimes, fired probes, producer/consumer/driver exits,
source and input hashes, real AS1 argv/profile, normal/traced code/functions/
relocations/pools identity, and whole-owner versus isolated target equality.
Revalidation also relinks the real object to verify saved symbol bindings.

Each capture correlates **74 raw immediate/memory emitter events** with actual
AS1 instruction records. The old/local-exit controls have 686 such records;
the separate-buttons and final forms have 684. Each input contains one emitted
RA restore. UGEN emits the held-byte clear before its jump in both old and new
forms. The local-exit forms add an intervening kind-0 label record; normal AS1
output then keeps the clear before the branch and duplicates the RA load into
its delay slot. This identifies an assembler scheduling boundary, not an absent
C store. It does not prove the unavailable original source spelling.

Seventeen complete source forms are compiled and their saved source/object/
shape/neighbor evidence is revalidated: three overflow rejections, two short
forms and twelve full-length forms. Eleven raw neighbors and owner pools stay
unchanged throughout; non-overflow forms also preserve eleven padded neighbors.
The selected raw and padded 959-word targets are identical.

| Complete Form | Words | Overlapping Differences | Exact Opening Words |
| --- | ---: | ---: | ---: |
| Previous source | 959 | 721 | 66 |
| Early return or global exit | 959 | 713 | 66 |
| Local disabled exit | 960 | 605 | 91 |
| Local exit, conditional heading control | 959 | 693 | 111 |
| Separate u32/s32 buttons | 959 | 486 | 134 |
| Heading advance before yaw copy | 959 | 476 | 137 |
| Final corresponding unsigned yaw read | **959** | **475** | **137** |

The nonvoid ABI control emits the old words and is not adopted. Source-shape
controls are not matching credit or claims that all alternatives are the
original source.

The frontend local extent increases from 84 to **88** for the real buttons
local, whose home is -88. Optimizer locals remain **76**, rounded UGEN locals
80, frame 128, saved-area budget 16 and outgoing budget 32. All eight existing
source homes, the new buttons home and five emitted storage sites are checked.
There is no late temporary/frame growth. Budgets are not literal save counts.

## Fresh Full Qualification

The final **eight-test run passes in 79.421s**:

- 2,496 complete public core/width/filter/mutation cases plus 20 modeled FP
  edges; all 256 stick-byte/cooldown values, all nine effective provider-mutation
  modes and all 947 reachable retail words remain covered.
- The twelve original unreachable duplicate words remain required for literal
  matching; none is trimmed or waived.
- Two independent text rebases / twelve complete cases, actual 21-word curve
  execution, complete public packet/call snapshots and twelve guest aliases
  against the controller global, pressed-input global or pointer slot.
- Native32 O2/O0 with UBSan, 139 cases per profile, eight effective semantic
  controls, and nine unsigned heading extremes also compared in the guest.
- Thirteen effective observer/AS1 lifetime/profile/digest controls, including a
  guard that rejects live UGEN probes before AS1 can run; thirty effective
  frame/home/emitted-store controls.
- Twenty active-path initial states: **800 equal complete fault-prefix states**
  instead of 460. Modeled LO and FPU condition are compared explicitly.
- Eighty disabled-path states, across both stack phases, both byte patterns,
  all five gates and held values 0/100/101/124: **all 80 final private states and
  all 2,700 modeled memory-fault prefixes agree**. This is bounded-provider/model
  evidence, not arbitrary opaque-provider or hardware/FCSR acceptance.
- All 297 protected entries, all 6,057 installed bodies, 189,088 Game-data bytes
  / 720 owners, the callback slot and ten immutable first-image members.

The active path now first rejects at gate cuts **[38,46,37,39,40]**, all at
`0x150F3A80`. Memory, GPRs and PC agree; **FPR4/FPR18** differ. The old return/PC
gap is closed. The earlier literal mode-0 gap is word 137 / `0x150F3718`:
candidate `0x240E0007` versus retail `0x24180008`, involving the independent
animation-constant preloads. The full routine still requires 475 word fixes.

## Failed Experiments Are Not Qualification

The first owned extended trace left address probes active into AS1 and that
child failed. Its incomplete `traces/selected/receipt.json` remains rejected.
The fix deletes the probes on the actual UGEN exit event, before the next child
executes; the additional AS1-entry guard now refuses any surviving probe.
No compiler file, user debugger or external process is modified.

The corrected producer completed normally, but the reused parser initially
expected its older node-transport exit marker. It was revalidated using the
actual frame-transport exit marker through a scoped adapter, not synthetic log
records or an unnecessary compiler restart. Three further body captures and
the final CLI guard run complete normally.

A direct test import reached the pre-existing historical import-chain limit;
the new test preloads its stdlib `ctypes` leaf without changing Python's global
configuration. The first full run also exposed two test-only expectations:
rejecting a missing completed receipt, and selecting the intended source-marked
pointer store for a negative control. Both are fixed; only the final complete
eight-test run above is counted as final qualification. Its rejection control
uses a self-contained failed-summary fixture, so a fresh prepared checkout does
not need to recreate the observer crash. The actual failed receipt is also
checked when present, without becoming a required test input.

## Banked Baseline And Continuation

Tools **e14e489** banks the recovery; **22cdaac** makes the rejection control
self-contained. Both precede the consumer docs/pin at 22cdaac. Both local tools copies
freshly pass twelve shared tests and smoke checks; four ASCII/AST parses and
two identical task pairs pass. New mirror destinations were absent. All 1,154
prior mirror hashes and HEAD `ddbdd16b` survive, with 1,156 dirty paths afterward.
No mirror commit/reset or push.

The production ELF stays
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different and zero drift. Init 492/492 and
Debugger 181/181 stay exact among converted functions. Root README unchanged;
no production installation/rebuild, host-port or frozen Release action,
dependency update or Claude call.

```sh
python3 -m tools.experiments.game_actor_input_movement_return --group basic
python3 -m tools.experiments.game_actor_input_movement_return --group exits
python3 -m tools.experiments.game_actor_input_movement_return --group buttons
python3 -m tools.experiments.game_actor_input_movement_return --group heading
python3 -m tools.experiments.game_actor_input_movement_return --trace --form selected --label selected-exit-cleanup
python3 -m tools.experiments.game_actor_input_movement_return --trace --form local-disabled-exit
python3 -m tools.experiments.game_actor_input_movement_return --trace --form separate-u32-buttons
python3 -m tools.experiments.game_actor_input_movement_return --trace
python3 -m tools.tests.test_game_actor_input_movement_return -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned packets are in `conker/build/game-actor-input-movement-return/`: four
qualified body captures plus `traces/final-selected-guard/`, source screens,
private/public/native/rebase/alias results and protected-input receipts. Older
unchanged neighbor suites remain prior receipts, not newly run tests.

- [x] Recover the disabled return boundary through a real local exit join.
- [x] Remove the extra button-copy word through a real 32-bit local; preserve
  unconditional heading access, all 959 words, frame and live homes.
- [x] Qualify the complete successor and bounded disabled private path while
  preserving every installed byte. No installation or matching credit.
- [ ] Continue the same `func_150F34F4` at word 137 / `0x150F3718`, then the
  active-path FPR4/FPR18 allocation at `0x150F3A80` and remaining literal words.
  Do not turn the 475 differences into a broad guard list.
- [ ] Require all 959 literal words, appropriate full private/fault/rebase/
  caller gates and a byte-exact complete first image before installation.
- [ ] Keep the gate, both fade lifetime gaps, full opaque-provider/runtime
  acceptance and wider Game goal open. Do not skip to `func_150F43F0`.
