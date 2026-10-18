# Movement Turn Role Certificate And Argument Controls

Verified 2026-10-17. Consumer predecessor `e9d9aa25`, tools predecessor
`7a40f3f`; both active repositories began clean. The previous goal turn was
progress. Continue the same complete `func_150F34F4` from
[Note1517](1517-movement-float-lifetimes-and-field-heading-recovery-20261017.md).

Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.
The complete semantic C body is unchanged: **959 words, frame `0x80`, 392 raw
differences and 361 exact opening words**. Seven bounded temporary-register
rewrites in a private research guard table give **385 remaining differences
and 406 exact opening words**. This is not a fully matched function, a new C
conversion, an installation or seven new production guards.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 392 | 385 |
| Exact opening words | 361 | 406 |
| First unequal PC | `0x150F3A98` | `0x150F3B4C` |

## Source Controls And Actual Producer Order

`tools/experiments/game_actor_input_movement_turn_argument.py` protects 303
predecessor entries / 279 distinct paths and reuses the existing complete
owner/compiler/link/padder machinery. Ten complete source forms test combined
callback assignment/compound assignment, comma sequencing and narrowed turn
deltas. Four produce 960 words and are correctly rejected by the padder. The
six 959-word forms preserve eleven raw/padded neighbors; no source form improves
the qualified 392-difference baseline. Overflow words are not trimmed.

The completed predecessor compiler capture is revalidated, not restarted or
called a new trace. Its actual AS1 input already contains the float-to-integer
transfer before the heading load. Normal AS1 later hoists that load. The gap
is therefore not merely a reversed emitted load/conversion pair. Callback
argument spelling alone does not reproduce retail's temporary allocation.

The raw target equals the predecessor normal and observed objects, with the
same source/compiler/input identities, frontend locals 84, optimizer locals
76, rounded locals 80, frame 128, buttons home -84 and earlier live homes.
The revalidated capture still contains 74 actual emitter events / 684 AS1
instruction records. The research-normalized object is post-compile output,
not an output falsely attributed to AS1. Prior frame-negative suites remain
prior receipts, not fresh tests in this turn.

## Bounded Temporary Role Proof

Only the 35-word window `0x150F3A98..0x150F3B24` is considered. It ends at the
real turn callback and its delay slot. Four local roles have this correspondence:

| Role | Raw Temporary | Retail Temporary |
| --- | --- | --- |
| Heading input | T2 / GPR10 | T8 / GPR24 |
| Turn-step 25 | T8 / GPR24 | T3 / GPR11 |
| Truncated turn delta | T6 / GPR14 | T7 / GPR15 |
| Updated heading | T7 / GPR15 | T9 / GPR25 |

The proof decodes only the observed kernel's GPR operand fields and refuses
unsupported instructions. Each role is defined once, never read before its
definition, and does not collide with a used identity register after mapping.
All local direct control targets are scanned to reject interior entry. The
callback binding and delay-slot position remain fixed; the delay instruction's
GPR operand changes as one of the seven certified words. FP operands, memory
addresses, arithmetic operations, immediate values and instruction order are
preserved. This is local C-ABI temporary-role reasoning, not a global rename
or proof about unpassed registers observed by arbitrary opaque providers.

The seven expected-word rows affect offsets `0x5A4`, `0x5A8`, `0x5FC`, `0x618`,
`0x620`, `0x624` and `0x62C`. None has a relocation. The private CSV preserves
the entire production CSV byte prefix and appends exactly seven rows. The
actual full-owner padder/linker agrees with the role map, changes only **ten
target bytes**, preserves all target relocation metadata and eleven neighbors,
and keeps the complete 959-word slot. Production CSV/source/ELF are untouched.

```text
Raw factory: tools.experiments.game_actor_input_movement_float_lifetimes.selected_body()
Raw form: field-heading-compound-X
Raw SHA256: 5fab097557f1f8a7b65ea3be5ac6fb7f0adb0d5547e8ef0392d7dd538a3710dd
Normalized raw target SHA256: 752d65b6308d86281109d9c3237d4ddc52a943597b1d3e6c8b9e231c92d25218
Isolated source SHA256: ee123682996cf912de6246b854e7934e316687daba1b02760b7d1629f5418b3a
Raw / research-normalized differences: 392 / 385
Normalized first unequal word: 406, VA 0x150F3B4C
```

## Fresh Qualification

The complete **eight-test run passes in 97.898s**. Two additional focused
source/proof checks pass in **16.278s** after tightening only the report's
entry-path and delay-position terminology; emitted bytes are unchanged.

- Thirty-eight effective role/entry/opcode/guard-table controls reject changed
  expected words, relocations, replacements, invalid/colliding maps, incoming
  control, read-before-definition, identity-register collisions, an FP operand
  change, callback changes, frame/extent changes and malformed/duplicate CSVs.
- **480 raw-versus-normalized kernel cases**: sixteen poisoned GPR/FPR seeds,
  five signed stick values, two stack phases and three aligned actor bases.
  Aliases include C4 overlapping the later D_800D1550 or D_800A1994 read. Tests
  stop at the actual callback entry and compare complete memory, FP state,
  ordered events, declared packets, observations, protected GPRs and every
  mapped role. Raw private GPR identity and hardware/FCSR parity are not claimed.
- Three-way retail/raw-C/normalized execution for all 2,496 public core/width/
  filter/mutation cases, 20 modeled FP edges and 36 additional cap cases. All
  nine provider-mutation modes, 947 reachable retail words and actual 21-word
  curve execution remain covered. The cap gate fires in 24 boundary cases;
  the twelve original unreachable duplicate words remain untrimmed.
- **100 normalized active states / 5,900 equal fault-prefix states**, up from
  4,600: 1,140 low-position and 4,760 actually entered high-position prefixes.
  Each of the hundred raw controls still rejects thirteen accesses earlier at
  `0x150F3AB8`. The normalized first gap is `0x150F3B58`, only GPR10/13;
  all FPRs, memory, PC, modeled LO and FPU condition agree there.
- All 80 disabled final private states / 2,700 fault prefixes and all 160
  mode-0 final private states / 8,320 fault prefixes still agree.
- Fresh native32 O2/O0 UBSan on the unchanged semantic C, 149 cases/profile,
  eight effective controls, nine unsigned heading extremes and ten cap cases.
  Actual normalized-object text rebases pass two links / twelve cases; twelve
  normalized guest aliases also agree with retail. Native C is not presented
  as literal execution of the post-compile research rewrites.
- All 303 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

Full opaque-provider/caller, arbitrary register-private, hardware/FCSR and
gameplay acceptance remain open. No partial candidate is installed merely
because these bounded checks pass.

## Banked Baseline And Continuation

Tools **a0ea7dd** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks; four ASCII/AST parses and two identical task
pairs pass. Both new mirror destinations were absent. All **1,160** prior
mirror hashes and HEAD `ddbdd16b` survive, with **1,162** dirty paths afterward.
No mirror commit/reset, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init 492/492 and
Debugger 181/181 remain exact among converted functions. Root README remains
unchanged. No production build, host-port or frozen Release action.

```sh
python3 -m tools.experiments.game_actor_input_movement_turn_argument --group arguments
python3 -m tools.experiments.game_actor_input_movement_turn_argument --group widths
python3 -m tools.experiments.game_actor_input_movement_turn_argument --normalize
python3 -m tools.tests.test_game_actor_input_movement_turn_argument -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned sources, the private expected-turn-guards CSV, raw/normalized objects,
proof and qualification receipts are under
`conker/build/game-actor-input-movement-turn-argument/`. Prior immutable
snapshots remain untouched.

- [x] Measure the ten complete argument/width controls and retain the full
  qualified source instead of trimming an overflow or adopting a worse form.
- [x] Certify only the seven-word local turn correspondence and qualify the
  actual normalized owner without adding production guards or claiming credit.
- [ ] Continue the same routine at normalized word 406 / `0x150F3B4C`: the
  controller-global LUI uses candidate GPR13 versus retail GPR10. The following
  threshold/flag branch reaches the GPR10/13 private gap at `0x150F3B58`.
  Inspect actual operand and branch lifetimes; do not extend this map globally.
- [ ] Close all remaining 385 normalized differences and complete literal,
  private/fault/rebase/caller/first-normal-image gates before installation.
  Raw C still differs in 392 words; do not turn either count into a broad list.
- [ ] Keep the gate, both fade lifetime gaps, full runtime/provider acceptance
  and wider Game objective open; do not skip to `func_150F43F0`.
