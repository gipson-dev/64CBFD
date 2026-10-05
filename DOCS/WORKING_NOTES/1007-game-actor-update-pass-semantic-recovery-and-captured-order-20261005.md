# Game Actor Update Pass And Captured Predecessor Order

Date: 2026-10-05. Starting HEAD: `db20e039`, the direct dispatcher recovery
in [Note 1006](1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md).
The previous checkpoint was clean before this recovery. No push is requested.

## Recovery

`func_1502BEE4` in `conker/src/game/generated_58F80.c` now contains its
semantic actor-update pass instead of a false zero-return placeholder.
The retail slot is **176 words / 704 bytes**, ROM **0x59394**, address
**0x1502BEE4..0x1502C1A4**, frame **0x88**.

Default IDO 5.3 O2/g3 emits **174 body words**, padded to the existing slot,
with **115 different words**. The frame and original slot boundaries are
preserved. This is **not a byte-exact match**; no word guards, compiler-profile
override, instruction insertion or retail body replacement is added.

Linked slot SHA-256:
`04befd7009ca98429965f86dfc87558243ab24f2f60b5831f212baff314d42e3`.
Previous placeholder SHA-256:
`0fec5b32d47b6d2b7a1045ba46ba1333914fddc792e91fab482c1dca76bab842`.

The existing stride-0x32C actor view gains predecessor byte **+0x65** and
mask-ID byte **+0x274**, without moving existing fields. Casts retain the
owner's existing display-view declaration of `D_800CC2D0`; no broad header
or unrelated ABI refactor is introduced. The dispatcher experiment shares
the extended view and continues to match directly.

## Ordered Behavior

1. Invoke `func_1503F964()`, then clear `D_800C3E90` and `D_800C3E74`.
2. Scan mask IDs for slots **0..24**, regardless of activity. Nonzero values
   set `1u << ((value + 31) & 31)`. The explicit mask preserves MIPS SLLV's
   five-bit shift wrapping while keeping native C defined for all byte values.
   The reserved 26th actor is not mask-scanned.
3. Zero exactly 25 private depth bytes. Scan each actor's activity and
   predecessor live. Active actors with no predecessor invoke
   `func_1502BD84(actor, slot)` immediately.
4. For an active predecessor-linked actor, follow one-based predecessor
   indices, counting into its private byte and tracking the maximum depth.
   An inactive predecessor still participates in traversal; the reserved
   actor may be a predecessor/root but is not itself updated by these scans.
5. Capture positive-depth slots in ascending depth and ascending slot order.
   Invoke the dispatcher for that captured queue **without rechecking
   activity or predecessor**. Earlier updates may mutate actors but must not
   reorder or cancel already captured entries.
6. Invoke `func_1502F3C8()`. Rescan slots 0..24 using fresh activity reads;
   invoke `func_1502F948(actor)` for active actors. A callback can change
   later actors' eligibility.
7. Invoke `func_15030468()`, reread `D_800BEAC0`, invoke
   `func_1507C22C(0)` only when that byte is zero, and finally clear
   `D_800C3E70`.

Before fixture construction, the actual ASM bodies of all five phase callees
were reviewed for consumed incoming registers. The first, middle and final
phase calls take no caller input; the post-actor callback consumes the actor
pointer and the optional last call consumes the mode. Unlike the carried-slot
discovery in Note 1006, no additional hidden argument was found here.

No cycle detection, predecessor validation, new active gate or null fallback
is added. Retail cycles remain nonterminating and the depth byte wraps. Bad
indices and native out-of-bounds arithmetic are not supported inputs.

## Qualification

`tools/tests/test_game_actor_update_pass_match.py` supplies **8 tests**.
Together with the previous dispatcher's 9 tests, **17 focused checks pass in
26.790 seconds, no skips**, against the rebuilt production ELF:

- **771 completed three-way cases** compare retail instructions, selected C
  instructions and the baseline C control: 256 mask-byte cases, 512 randomized
  acyclic graph cases, a maximum-depth reserved-root case and two live-state
  mutation cases. Both incoming stack phases are exercised.
- **257 cases connect the actual 88-word retail/direct-C dispatcher**, rather
  than replacing it with an opaque update hook. Its downstream callees remain
  ABI-aware, clobbering fixtures. The previous dispatcher stays byte-exact.
- All **176 retail caller words** execute across the randomized cases.
  Saved-register and stack restoration checks run on every completed trace.
- External memory, ordered writes/calls, arguments and field reads agree.
  Consecutive identical nonvolatile reads are collapsed only when no external
  event intervenes; private stack addresses/schedules are not equated. This
  is a semantic-boundary check, **not** an instruction/stack-trace match.
- **16384 native C cases** agree with an independent stable-insertion-sort
  reference, including all mask-byte values and seven callback-mutation
  modes. Entire actor storage, reserved-slot contents, call order/arguments,
  mask result and final state bytes are checked. Size/field offsets are pinned
  under 32-bit compilation with warnings as errors.
- Wrong mask shift and wrongly rechecking queued activity produce observable
  differences. These negative controls do not enter production.
- Two **bounded cyclic-prefix checks** intentionally exhaust the interpreter
  budget, demonstrate 255-to-zero depth wrapping, and show no later update or
  phase call. They do not claim that a cyclic pass completes.

Other phase callees remain opaque fixtures. This does not establish complete
actor physics, animation, SDK behavior, hardware gameplay, rendering or PC
runtime acceptance. No sibling source, build, save or frozen Release change
is made; this is guest DECOMP work, not a host source transplant.

## Audit And Progress

The pre-edit snapshot covers **6060 function slots**. After rebuilding, only
`func_1502BEE4` changes, with no added/deleted slots or address/length drift.
The actor scan and dispatcher remain exact. The patch CSV remains **10606
rows**, with unique filename/function/offset keys and unchanged SHA-256
`22f784b5c5dc38114c6d2ed9da81fb74ea9ac3eb5c97c4a3be57d129d1fa4099`.

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3302 / 5463 (60.44%) | 0 | 2161 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2629 / 4790 (54.89%) | 0 | 2161 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts and the 47 retained Init ASM functions are unchanged: this
placeholder was already included in the converted-C count. README aggregates
therefore remain correct and unchanged; recovery detail belongs in this note.
The owner build and `make tools-check` pass.

Complete protected sections remain retail-exact: Init code **164048 bytes**,
Init data/rodata **17376 bytes**, Debugger **19800 bytes** and Game data
**189088 bytes / 720 owners**. The full actor/viewport/SDK/resource/matching/
tool regression passes **319 tests in 305.557 seconds, no skips**.
Whitespace checks and all **2927 relative documentation links** pass after
the post-commit handoff update.
Existing unrelated duplicate-recipe warnings remain; the isolated candidate
emits no diagnostics.

## Reproduction And Next

### Post-Commit Matching Screen

After commit **`981ec732`** banked the audited semantic recovery, matching
continued with eight additional local-storage controls. Four combinations
of pointer/scalar `register` hints all emit the unchanged **174 words /
frame 0x88 / 115 differences**. Four grouped-scratch forms (25/28 depth bytes,
depth-first/queue-first) emit **172 words / frame 0x80 / 175 differences**.
No form improves the match; no production/profile/patch change is adopted.

These controls pass **64 retail-versus-candidate boundary comparisons**, 32
with the actual dispatcher connected and 32 with live mutation hooks. Both
stack phases, a full 25-deep chain and queue recheck counterexamples are
included. All **18 focused pass/dispatcher tests pass in 39.427 seconds, no
skips**; tools checks pass. The production ELF remains the audited semantic
checkpoint. The 319-test combined result above is that checkpoint's corpus;
the additional experimental test was run in the focused 18-test corpus.

This separates failed matching hypotheses from implementation: `register`
hints are ineffective, and grouping these byte arrays changes the frame
away from retail. The remaining work is still the caller's original local
layout and schedule, not a new gameplay behavior correction.

Run from `64CBFD` in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_actor_update_pass_candidates
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --followup
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

The initial screen contains 60 forms; `--followup` selects the eight later
local-storage controls. Unmasked-shift forms in the initial screen are compiler
experiments only, not native-C equivalence candidates. The selected source
retains an explicit five-bit mask and the recovered phase/callback contracts.

For the combined regression, prepend `tools.tests.test_game_actor_update_pass_match`
to [Note 1006's combined corpus](1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md).

Next matching work is **`func_1502BEE4` itself**: recover the original private
array offsets (**SP+0x3C / SP+0x58**), max-depth/count spills (**SP+0x34 /
SP+0x38**), repeated predecessor-load loop, phase-local base/end lifetimes
and the 176-word schedule. Do not normalize the whole 115-word difference
set or remove defined shift wrapping merely to improve the numeric score.
The semantic checkpoint and counterexamples provide a bounded baseline for
that work.
