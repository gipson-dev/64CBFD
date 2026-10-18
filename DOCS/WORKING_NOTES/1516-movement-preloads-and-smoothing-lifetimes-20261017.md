# Movement Preloads And Smoothing Lifetimes

Verified 2026-10-17. Consumer predecessor `d7de8c0`, tools predecessor
`22cdaac`; both active repositories began clean. The previous goal turn was
progress. Continue the same complete `func_150F34F4` from
[Note1515](1515-movement-return-boundary-and-full-width-buttons-20261017.md).

Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`:
**959 words / 3,836 bytes, frame `0x80`, 420 unequal words instead of 475.**
The first **337 words** are exact, up from 137. This is an uninstalled research
candidate, not another converted or matching function. No new guards, compiler
profile, executable trimming, padding variables or production rebuild.

## Source Recovery

`tools/experiments/game_actor_input_movement_preload.py` reuses the previous
complete owner/link/padder and qualified compiler observer. All 299 protected
predecessor entries / 275 distinct paths remain byte-identical.

Four source changes produce the selected successor:

- Update target speed before the default animation/state stores. This allows
  the actual `D_800A1988` load before the animation-byte write and restores the
  animation-8 preload into the earlier delay slot. All three updates remain.
- Assign the held-object byte before changing mode after the pickup call.
  The resulting normal code samples `D_800CC26D` before both stores, then emits
  retail's mode-store/held-store order. An explicit integer snapshot does not
  recover the same scheduling; it remains a rejected source control.
- Sample the signed stick X into the existing meaningful float `amount`
  before smoothing. This recovers the FPR4/FPR6 constant loads and subsequent
  temporary allocation without changing the floating arithmetic tree. A new
  `stickX` local produces identical words, so it is not retained.
- Move the turn-step assignment after the heading update, before the turn
  callback. AS1 now schedules its byte store at retail's later position.

The helper compiles six initializer orders, eight smoothing forms and eight
flow/lifetime forms: **22 complete source controls**. Their saved full source,
raw objects, real links, padded targets and eleven raw/padded neighbors are
checked. Owner pools remain unchanged. This is source/word-shape evidence for
the alternatives, not complete semantic qualification of every alternative.

| Complete Form | Words | Frame | Differences | Exact Opening Words |
| --- | ---: | ---: | ---: | ---: |
| Previous qualified source | 959 | 128 | 475 | 137 |
| Target speed first | 959 | 128 | 466 | 208 |
| Explicit signed X sample | 959 | 128 | 445 | 208 |
| Held before mode | 959 | 128 | 440 | 337 |
| Late turn-step store | 959 | 128 | 425 | 208 |
| Combined selected source | **959** | **128** | **420** | **337** |

Removing the independent previous-input local is not adopted: although still
959 words, it changes the frame to 120 and worsens the fit to 491 differences.
Reusing `amount` instead of introducing `stickX` gives the exact same selected
object while retaining the previous source-local extent and live homes.

```text
Factory: tools.experiments.game_actor_input_movement_preload.selected_body()
Form: held-before-mode-late-step-reuse-amount
Raw SHA256: 5a5d99ac87599139e2c06f4adc5f415d2f8397c8760dddd747e4e06e5382e3a2
Isolated source SHA256: 56dabe73c9e7aaf0faa48fa2788c37bb4ce6d7d0a3dcf4910de6b481ce9acf67
Words/frame/differences: 959 / 0x80 / 420
First unequal word: 337, VA 0x150F3A38
```

## Fresh Qualification

The selected compiler capture completes normally. Normal/traced code,
functions, relocations and pools agree, as do the complete-owner and isolated
targets. Revalidation requires actual producer/consumer/driver exits, fired
probes, source/compiler/input hashes, AS1 profile/lifetime and saved-link
bindings. It correlates **74 actual immediate/memory emitter events** with
the **684 instruction records** in the real AS1 input. No synthetic records,
compiler modification, external debugger or external process is involved.

The existing layout checker passes unchanged: frontend locals 88, optimizer
locals 76, rounded locals 80, frame 128, saved/outgoing budgets 16/32, all
eight previous source homes, the buttons home and five emitted storage sites.
The new source-marked X sample uses `amount`'s real float home **-8**. Three
effective controls reject changes to that home/type/width; no extra local or
late frame growth is needed.

The final **eight-test run passes in 84.180s**:

- 2,496 complete public core/width/filter/mutation cases plus 20 modeled FP
  edges, all 256 stick/cooldown values, all nine effective provider-mutation
  modes, actual curve execution and all 947 reachable retail words. Twelve
  original unreachable duplicate words remain required and untrimmed.
- Native32 O2/O0 with UBSan, 139 cases/profile and eight effective controls;
  nine unsigned heading extremes also compared in the guest. Two independent
  text rebases / twelve cases and twelve guest aliases remain covered.
- Sixteen effective capture/AS1 rejection controls, thirty existing frame/
  home/emitted-store controls and the three new sample-home controls.
- Twenty active initial states: **880 equal complete fault-prefix states**,
  up from 800. The first rejecting cuts are **[42,50,41,43,44]**, all at
  `0x150F3AB8`. Memory/PC agree, while GPR10/11/15/24 and the sampled-X FP
  lifetime still differ. Modeled LO and FPU condition are compared explicitly.
- All **80 disabled final private states / 2,700 fault prefixes** still agree.
- All **160 mode-0 final private states / 8,320 fault prefixes** now agree:
  both stack phases, both byte patterns, five gates, nearby 0/101, depths
  0/100.00001, and pressed 0/0xC000 with the corresponding above/below-threshold
  positions. This is bounded fixture/provider evidence, not arbitrary opaque
  providers, hardware/FCSR or full caller/gameplay acceptance.
- All protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

The first test run exposed a test-only reporting assumption: older audit JSON
does not contain `first_unequal_word`. The corrected test derives that field
from the actual linked words, while continuing to revalidate the original
audit's shape/hash/difference fields. The final complete rerun above is the
acceptance receipt; the earlier run is not counted as passing.

## Banked Baseline

Tools **de8f5ff** is committed first. Both tools copies freshly pass twelve
shared tests and their smoke checks; four ASCII/AST parses and two identical
task pairs pass. Both new mirror destinations were absent. All **1,156** prior
mirror hashes and HEAD `ddbdd16b` survive, with **1,158** dirty paths afterward.
No mirror commit/reset, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals are unchanged: Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init 492/492 and
Debugger 181/181 remain exact among converted functions. Root README is
unchanged; no host-port or frozen Release action. Historical unchanged
neighbor suites are prior receipts, not newly run tests.

```sh
python3 -m tools.experiments.game_actor_input_movement_preload --group animation
python3 -m tools.experiments.game_actor_input_movement_preload --group smoothing
python3 -m tools.experiments.game_actor_input_movement_preload --group flow
python3 -m tools.experiments.game_actor_input_movement_preload --trace
python3 -m tools.experiments.game_actor_input_movement_preload --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_preload -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned sources, compiler inputs, complete traces and qualification receipts are
under `conker/build/game-actor-input-movement-preload/`. Older frozen snapshots
are not replaced. The earlier failed observer receipt remains excluded.

## Continue The Same Function

- [x] Recover mode-0 initializers/pickup scheduling and extend the exact opening
  to 337 words while preserving all 959 executable words and frame `0x80`.
- [x] Recover smoothing sample/turn-step lifetimes and qualify the complete
  selected successor without changing any installed byte or claiming credit.
- [ ] Continue at word 337 / `0x150F3A38`: retail transfers the -30.0f constant
  before loading vertical velocity into FPR2; candidate loads velocity into
  FPR0 first. This guarded high-position block is not traversed by the default
  active-prefix fixture, so its literal gap and the later prefix gap are distinct.
- [ ] Continue the active smoothing GPR10/11/15/24 and sampled-X FPR2/FPR12
  lifetime at `0x150F3AB8`, then the remaining full literal/private/caller gates.
  Do not convert the 420 differences into a broad instruction guard list.
- [ ] Require all 959 literal words and a byte-exact complete first normal
  image before installation. Keep the gate, both fade lifetime gaps, opaque
  providers/runtime and wider Game objective open; do not skip to `func_150F43F0`.
