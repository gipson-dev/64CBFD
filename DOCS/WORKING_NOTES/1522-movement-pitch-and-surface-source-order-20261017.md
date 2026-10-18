# Movement Pitch And Surface Source Order

Verified 2026-10-17. Consumer predecessor `5ecc488c`, tools predecessor
`201eff8`; both active repositories began clean. The preceding turn was
progress. Continue the same complete `func_150F34F4` from
[Note1521](1521-movement-release-index-speed-copy-and-heading-roles-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

Recovering the surface-exit source order improves **200 to 152 raw word
differences**, or **169 to 121** with the byte-identical 31-row private
research table. All improvement this turn is C-emitted: no new research or
production rows, inserted words, omitted words, installation or matching credit.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 152 | 121 |
| Exact opening words | 361 | 478 |
| First unequal PC | `0x150F3A98` | `0x150F3C6C` |

## Source Recovery

`tools/experiments/game_actor_input_movement_pitch_surface_order.py` protects
**311 predecessor entries / 287 distinct paths**. The historical run directory
is `conker/build/game-actor-input-movement-pitch-inputs/`; the module was named
for both investigated regions after the surface-order recovery was selected.

Thirty-one complete source controls cover equality spelling, coefficient
snapshots, surface multiply literals, expression snapshots, six store orders
and three additional mode-store placements. Every form preserves all eleven
raw neighbors and owner pools. Two overflowing 960/962-word forms are rejected
by the real padder; one shorter 957-word control retains its measured extent
and real padding. No control is trimmed or credited.

- Reversing the acceleration equality operands produces identical compiler
  output; it does not fix the remaining `C.EQ.S` operand order.
- Local and existing-variable coefficient snapshots retain 959 words but
  worsen the raw count to 267, 268, 273 or 372. These are rejected candidates,
  not evidence that retail's coefficient-read lifetime has been recovered.
- Integer surface multiplication is identical to the float spelling. Double
  multiplication overflows, unary negation is shorter, and the two whole
  expression snapshots are optimized back to the baseline.
- Moving the surface-depth assignment before the pitch clear recovers five
  raw words. Placing the vertical-velocity assignment before the mode clear
  recovers the earlier stack load and branch-delay constant setup as well.

The selected `surface-mode-1032` exit is:

```c
actor->verticalVelocity = speed * -1.0f;
actor->mode = 0;
actor->depth = D_800A19CC;
actor->valueB8 = 0.0f;
```

The previous order was mode, vertical velocity, pitch, depth. Of **62 changed
raw words, 48 become exact and zero previously exact words are lost**. The
other fourteen remain different. The emitted stack load at `0x150F4148`,
MTC1 in the branch-likely delay slot at `0x150F4154`, and the complete tail
`0x150F421C..150F4238` now match directly from C. The tail's global-depth load
at `0x150F4230` precedes the pitch clear at `0x150F4234`, as in retail.

```text
Factory: tools.experiments.game_actor_input_movement_pitch_surface_order.selected_body()
Form: surface-mode-1032
Raw target SHA256: 1a31a90ee6291e47eeead06e6359174d46ea6a4ddc597fb9069e243b6fea6da4
Normalized target SHA256: f62f784fb4a8303fd99778f5e7254746f023f9c4980b229f3342b52782073625
Isolated source SHA256: ae460d5b778c28c62323f1141c35ba54555f3eecf59ceb27d6537f84580f78a7
```

The actual full-owner padder/linker reproduces the independent 31-row role
vector, changing the same 39 bytes while preserving all target relocations
and eleven padded neighbors. `expected-surface-guards.csv` is byte-identical
to the predecessor's `expected-release-guards.csv`. The bounded heading proof
still checks 400 continuation states; no ABI clobber excuses a live-out read.

## Qualification

The final **thirteen-test run passes in 164.556s**. The first run passed the
behavioral checks but reported two test-adapter errors: the reused heading
receipt expected the old proof key, and the stale-guard control expected the
old CSV filename. Only those adapters were corrected; the complete suite was
then rerun successfully, without changing the selected source or capture.

- All 31 source/object/link/extent controls, two actual overflow rejections,
  one shorter control, real owner padding, unchanged pools and eleven neighbors.
- All 32 effective heading-role controls and **480 poisoned non-call kernel
  cases** rerun, checking the four physical registers and actual FP/memory
  state. Both actual stale-word/unexpected-relocation padder controls rerun.
- Retail/raw/normalized execution of **2,496 public cases**, twenty modeled
  FP edges, nine effective provider-mutation modes, actual 21-word curve and
  947 reachable retail words. All twelve unreachable retail duplicates remain
  present. The 36 cap cases pass, with 24 gates fired.
- All 200 release cases across 25 valid record slots and both stack phases,
  including fifty actual release multiplies. The hundred speed/flags guest
  overlaps still agree with actual retail and reject the old late-speed read.
- Sixteen signed-Y guest aliases/older-candidate rejections and forty clamp
  cases with two compiled wrong limits rerun. The positive unescaped-zero
  lifetime check reruns; the prior eight AST-zero negative controls are not
  claimed fresh this turn.
- **256 new surface kernel cases**, including 128 global/actor overlaps and
  224 cases with callbacks. All three objects agree on complete RAM, FPRs,
  semantic packets, provider observations and fired gates at `0x150F423C`.
  In sixteen affected overlaps, the pitch clear aliases `D_800A19CC`; the old
  C reads the cleared value and is rejected. Actual retail is the oracle,
  not the high-level model's earlier read order. Interior-entry guest tests
  do not claim arbitrary caller state, native partial-structure aliasing,
  native byte order, general FCSR or hardware/gameplay equivalence.
- Native32 O2/O0 UBSan: **369 cases/profile**, eight effective controls, two
  actual normalized-object rebases/twelve cases, and twelve established guest
  aliases. New partial-structure/global overlaps stay guest-only.
- **100 active states / 6,700 equal normalized fault prefixes**. The first
  private frontier remains `0x150F3C88`, GPR10/13/14/15/25 only, with RAM/FPRs
  equal. All hundred prior-28-row controls reject at `0x150F3C6C`; all eighty
  disabled final states / 2,700 prefixes and 160 mode-zero final states /
  8,320 prefixes remain equal. This later source recovery does not advance
  the earlier private frontier or prove whole-function private equivalence.
- New owned compiler capture: **74 emitter events / 687 actual AS1 records**,
  byte/relocation-identical to the normal target. Frontend88, optimizer76,
  rounded80, frame128, saved16/outgoing32 and all earlier homes remain fixed;
  release-index home remains J4 M-88 / optimizer J4 R4. Nine surface-site
  corruptions and two frame-budget corruptions are rejected. Earlier 41
  layout negative controls are prior evidence, not claimed rerun in full.
- All 311 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

## Banked Baseline And Continuation

Tools **74c3bf7** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks; four ASCII/AST parses and two identical task
pairs pass. Both new mirror destinations were absent. All **1,168** prior
hashes and HEAD `ddbdd16b` survive, with **1,170** dirty paths afterward.
No mirror commit/reset/clean, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Totals remain Game **2,965 / 4,828 (61.41%)**, total **3,638 / 5,501 (66.13%)**,
1,863 different, zero drift; Init492/492 and Debugger181/181 among converted
functions. Main README is unchanged. No production build, host-port or frozen
Release action; this is not a host-port synchronization or runtime claim.

Scoped AST graph refresh completes with **42,322 nodes / 82,446 links / 4,086
communities**. The new note is indexed. Only three shifted UPDATE_LOG heading
IDs disappear, with their labels retained at new locations; there are no
unrelated losses. All 19,398 existing excluded nodes from 2,972 still-present
files remain preserved, with no purge or full re-extraction.

```sh
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --group equality
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --group coefficient
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --group surface
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --group store
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --group mode
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --normalize
python3 -m tools.experiments.game_actor_input_movement_pitch_surface_order --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_pitch_surface_order -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the surface exit's real source order: 48 new C-exact words,
  no previously exact losses, same complete length/frame, no new guards.
- [x] Qualify the new actual-retail surface overlaps, whole public/FP/native
  corpus, prior role kernels, bounded prefixes and fresh compiler capture.
- [ ] Continue **the same function**, normalized word478 / `0x150F3C6C`, private
  frontier `0x150F3C88`. There are **111 GPR-field-only differences and ten
  other words**. Classification is not permission for a global rename.
- [ ] The ten other PCs are `0x150F3D44` (FP equality operand order),
  `0x150F3E1C/24/28/30/34` (coefficient/read/store order), `0x150F4098/9C`
  (count-loop setup order), and `0x150F434C/50` (late zero/comparison schedule).
  Reuse the rejected source controls rather than repeating them blindly.
- [ ] Finish remaining literal/private/caller/provider/first-image gates
  before installation. Keep the gate, both fade lifetime gaps, full runtime
  acceptance and the wider Game matching objective open.
