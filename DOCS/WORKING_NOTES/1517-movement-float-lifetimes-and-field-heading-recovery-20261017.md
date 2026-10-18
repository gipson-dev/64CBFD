# Movement Float Lifetimes And Field Heading Recovery

Verified 2026-10-17. Consumer predecessor `7662fcc6`, tools predecessor
`de8f5ff`; both active repositories began clean. The previous goal turn was
progress. Continue the same complete `func_150F34F4` from
[Note1516](1516-movement-preloads-and-smoothing-lifetimes-20261017.md).

Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`:
**959 words / 3,836 bytes, frame `0x80`, 392 unequal words instead of 420.**
The first **361 words** are exact, up from 337. The high-position cap and the
first smoothing FP lifetime gap are recovered. The candidate remains
uninstalled and earns no matching/conversion credit; production still has the
old placeholder. No new guards, profile, trimming or padding variables.

## Recovered Source Lifetimes

`tools/experiments/game_actor_input_movement_float_lifetimes.py` preserves all
301 protected predecessor entries / 277 distinct paths and reuses the existing
complete owner/link/padder, frame transport and actual AS1 observer.

- Use the existing `velocity` float for the high-position cap, and perform its
  load in the comparison: `-30.0f < (velocity = actor->verticalVelocity)`.
  This recovers retail's constant-transfer-before-load order and FPR2 value.
  A separate assignment recovers the register but not the two-word schedule.
- Sample signed X into the existing `magnitude` local. Its optimizer operand
  is R44 and the emitted conversion targets FPR12, as retail requires. Keeping
  the previous `amount` sample instead assigns R34/FPR2 at this point.
- Update the heading directly in the actor field, preserving explicit unsigned
  32-bit subtraction and the final u16 field/callback boundary. Removing the
  separate `u32 heading` lifetime avoids its V0 carrier and improves later GPR
  allocation. It is a real local removal, not a retained unused padding slot.
- Use a compound smoothing update, retaining the previous-input sample for the
  subtraction. This recovers retail's final add-operand order without changing
  the arithmetic tree or removing any required emitted field access.

| Complete Source Form | Words | Frame | Differences | Exact Opening Words |
| --- | ---: | ---: | ---: | ---: |
| Previous qualified source | 959 | 128 | 420 | 337 |
| Separate velocity local | 959 | 128 | 418 | 337 |
| Velocity assignment in comparison | 959 | 128 | 416 | 361 |
| Combined FPR12 X sample | 959 | 128 | 414 | 361 |
| Direct heading field update | 959 | 128 | 393 | 361 |
| Selected compound smoothing | **959** | **128** | **392** | **361** |

Eight carrier/cap forms, nine expression forms, six heading forms and five
delta-first forms give **28 complete source controls**. Every saved full
source, raw object, real link and padded target is revalidated. All emit 959
words/frame 128 and preserve eleven raw/padded neighbors and owner pools.
These are word/shape controls, not full semantic qualification of every form.
The explicit delta-first locals do not restore retail's allocation and remain
rejected; the selected body uses no extra variable.

```text
Factory: tools.experiments.game_actor_input_movement_float_lifetimes.selected_body()
Form: field-heading-compound-X
Raw SHA256: 5fab097557f1f8a7b65ea3be5ac6fb7f0adb0d5547e8ef0392d7dd538a3710dd
Isolated source SHA256: ee123682996cf912de6246b854e7934e316687daba1b02760b7d1629f5418b3a
Words/frame/differences: 959 / 0x80 / 392
First unequal word: 361, VA 0x150F3A98
```

## Actual Compiler Evidence

The completed selected capture requires normal/traced code/functions/
relocations/pools identity, whole-owner versus isolated equality, actual
producer/consumer/driver exits, fired probes, source/compiler/input hashes,
AS1 argv/profile/lifetime and real saved-link bindings. It correlates **74
actual emitter events** with **684 real AS1 instruction records**. Prepared
compiler fingerprints, including AS1, remain unchanged.

The frontend extent falls from 88 to **84** after removing `heading`; the
buttons home consequently moves from -88 to **-84**. Optimizer locals remain
76, rounded locals 80, frame 128, saved/outgoing budgets 16/32. Eight earlier
source homes and five emitted storage sites remain checked. The cap, X and
previous-input frontend homes are **-32, -16 and -60**. The cap and X optimizer
stores use **R34/FPR2 and R44/FPR12**, verified against the emitted words.
The compound update eliminates the source-marked optimizer previous-input
store; that absence is not treated as proof of a missing runtime load.

All **21 FP arithmetic/load/store words** in the checked smoothing window now
match. The mixed-register `mfc1` at `0x150F3B0C` deliberately remains different:
retail `0x440F2000`, candidate `0x440E2000`, transferring FPR4 into different
GPRs. It is not waived as a floating-point match.

## Fresh Qualification

The final **eight-test run passes in 143.145s**:

- The complete 2,496 public core/width/filter/mutation cases plus 20 modeled
  FP edges; all nine effective provider-mutation modes, all 947 reachable
  retail words and actual 21-word curve execution. Twelve original unreachable
  duplicate words remain required and untrimmed.
- Thirty-six additional cap boundary cases, with **24 confirmed gate entries**
  in both retail and candidate. The retail threshold is exactly 2100. Held
  movement subtracts 16 first, so 2101 with a held object does not test the cap.
  The tests use the actual boundary/next float and 2200, not a setup-only claim.
- **100 active initial states / 4,600 equal complete fault-prefix states**:
  880 low-position prefixes plus 3,720 prefixes in eighty actually entered
  high-position cases. Both stack phases, byte patterns, five gates and four
  high-position velocity boundaries are covered. At the first rejecting cut,
  all FPRs, memory, PC, modeled LO and FPU condition agree; only GPR10/11/24
  differ at `0x150F3AB8`.
- All **80 disabled final private states / 2,700 fault prefixes**, and all
  **160 mode-0 final private states / 8,320 fault prefixes**, still agree.
- Native32 O2/O0 with UBSan, **149 cases/profile**, eight effective controls,
  nine unsigned heading extremes and ten additional fired-cap cases. Two
  independent text rebases / twelve cases and twelve guest aliases also pass.
- Eleven effective capture/AS1 rejections, **55 frame/home/emitted-store
  controls**, and an additional complete wrong-C equality control. Changing
  the cap's strict comparison to `<=` at velocity -30 is observably rejected;
  the actual cap gate is required to have fired.
- All 301 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

The first run exposed a test-only classification error: it included `mfc1` in
the pure-FP word equality set despite that instruction's known GPR destination
gap. The corrected test checks FP arithmetic/storage and explicitly requires
the remaining transfer mismatch. Only the complete final rerun is counted as
passing. A separate diagnostic also hit the historical Python import-depth
limit; the new helper now imports its actual shared recovery module before
the newer wrappers. No recursion setting, old helper or dependency is changed.

This remains bounded-provider/model evidence. Full opaque-provider/caller,
hardware/FCSR and gameplay acceptance remain open.

## Banked Baseline And Next Work

Tools **7a40f3f** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks, with four ASCII/AST parses and two identical
new task pairs. Both mirror destinations were absent. All **1,158** prior
mirror hashes and HEAD `ddbdd16b` survive, with **1,160** dirty paths afterward.
No mirror commit/reset, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init 492/492 and
Debugger 181/181 remain exact among converted functions. Root README is
unchanged. No production build, host-port or frozen Release action. Older
unchanged neighbor suites remain prior receipts, not newly run tests.

```sh
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --group velocity
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --group expression
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --group heading
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --group delta
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --trace
python3 -m tools.experiments.game_actor_input_movement_float_lifetimes --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_float_lifetimes -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned sources, traces and qualification receipts are under
`conker/build/game-actor-input-movement-float-lifetimes/`. Earlier immutable
snapshots and the excluded failed observer receipt remain untouched.

- [x] Recover the high-position cap and initial smoothing FP lifetimes, retain
  all 959 executable words/frame `0x80`, and extend the exact opening to 361.
- [x] Remove the separate heading-result local and qualify the full successor
  without installing it or changing any production byte or aggregate credit.
- [ ] Continue the same function's temporary GPR allocation at `0x150F3A98`:
  candidate `lhu T2`, retail `lhu T8`. The turn-step immediate/store and later
  FPR4-to-GPR transfer, subtraction and callback halfword argument also differ.
  Inspect the real UGEN/AS1 operand order before another targeted source form;
  a combined callback-argument update is a hypothesis, not a measured recovery.
- [ ] Close all 392 literal differences and full private/fault/rebase/caller/
  first-normal-image gates before installation. Do not substitute a broad
  instruction guard list or skip to `func_150F43F0`.
- [ ] Keep the gate, both fade lifetime gaps, full opaque providers/runtime
  and wider Game objective open.
