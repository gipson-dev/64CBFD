# Game Actor Pass Array Layout And Connected Selector

Date: 2026-10-05. Starting HEAD: `36351570`, the tested local-storage screen
after [Note 1007](1007-game-actor-update-pass-semantic-recovery-and-captured-order-20261005.md).
The checkout was clean. Work continues on `func_1502BEE4`; this note does not
declare it matched or the Game decompilation complete.

## Matching Progress

The same retail **176-word / 704-byte** slot at **0x1502BEE4..0x1502C1A4**,
ROM **0x59394**, now emits **175 body words** rather than 174. Default IDO
O2/g3 still uses frame **0x88**; different words fall from **115 to 109**.
There are **no new guards, compiler-profile overrides or inserted retail words**.
The padded linked slot SHA-256 is now
`c32708201e59edf73b9986867a0afa76d7a8da115d8a38d0f703cbaa85422758`.

The production change is deliberately limited:

- Interleave the scalar declarations and two 25-byte arrays so the depth
  array is at **SP+0x3C**, the ordered queue at **SP+0x58**, and the queue-count
  spill at **SP+0x38**, matching their retail offsets.
- Use the existing fixed `D_800D121C` end symbol for the final activity scan.
  Both the mask and final activity scans still exclude the reserved actor.
- Correct the first-phase declaration to `void func_1503F964(void)`, agreeing
  with its existing recovered definition. It already occupies an exact linked
  35-word slot; its original recovery and fourteen allocation guards are
  documented in [Note 502](502-game-actor-slot-selector-match-20260929.md).
  The selector source and its guard entries do not change in this turn.

No gameplay gate, predecessor validation, callback order or captured queue
rule changes. The explicit five-bit shift mask remains, keeping every mask-ID
byte defined in native C while agreeing with MIPS shift wrapping.

The maximum-depth spill **still uses SP+0x78**, not retail's **SP+0x34**.
That difference is explicitly pinned by the test, alongside the three now
correct offsets; it must not be mistaken for a completed stack-layout match.

The remaining words, counted at fixed retail address intervals, are:

| Retail Interval | Different / Total Words |
| --- | ---: |
| 0x1502BEE4..0x1502BF58, opening/mask | 20 / 29 |
| 0x1502BF58..0x1502C01C, zero/depth/immediate pass | 29 / 49 |
| 0x1502C01C..0x1502C0D4, queue capture | 22 / 46 |
| 0x1502C0D4..0x1502C12C, queued dispatch | 10 / 22 |
| 0x1502C12C..0x1502C1A4, final phases | 28 / 30 |

These sum to 109 / 176. They are not independent semantic failures or a
classification of root causes: shifted scheduling can move instructions
between the fixed intervals.

## Compiler Evidence

The prior 60-form initial screen and eight local-storage controls are retained.
Their frozen source is named `RECOVERY`; the current `SELECTED` body comes
from `interleave-3-slot-maxDepth-index-count`. Freezing the old controls keeps
their published measurements reproducible instead of silently retargeting
them to each new production body.

This turn screens **172 additional isolated forms**:

| Family | Forms | Body Words | Frame | Different Words |
| --- | ---: | ---: | ---: | ---: |
| Phase ends / predecessor-loop shapes | 20 | 170..175 | 0x88 | 115 or 167 |
| Scalar/pointer declaration permutations | 48 | 175 | 0x88 | 115 |
| Interleaved scalar/array declarations | 72 | 175 | 0x88 | 109..115 |
| Grouped counter/workspace storage | 8 | 174..181 | 0x80 or 0x88 | 115 or 175 |
| Byte cursor shared with sorting | 24 | 149 | 0x80 | 171 |

Grouping all workspace fields and the shared byte cursor move away from the
retail frame or unrolled loop; neither is adopted. Changing declaration order
can move spill homes without changing the aggregate mismatch count. Equal
counts therefore do not prove equal instruction streams.

Only the selected semantic body is qualified by the complete caller/native
matrix. Compiling a discarded control is not a claim of gameplay acceptance,
native equivalence, or a supported alternative implementation.

## Qualification

All **19 focused caller/dispatcher tests pass in 42.839 seconds, no skips**,
against the final rebuilt ELF. They retain the previous 771 three-way caller
cases, 257 actual-dispatcher connections, 16384 native independent-reference
cases, two semantic negative controls, cyclic-prefix checks and the eight
post-checkpoint local-storage controls' 64 boundary comparisons.

The new test adds **400 completed three-way cases connecting both the actual
selector and the actual dispatcher** before/during the recovered caller:

- All 25 valid saved selector indices, disabled/enabled selector states,
  no eligible flag, current-slot-only flag, next-slot and wraparound choices.
- Both incoming stack phases. Parent state is restored after the actual
  frameless selector and nested dispatcher executions.
- The selector's enable byte is preserved and its current-slot byte has the
  independently expected result. Its flag scan runs before the parent's mask
  and active/depth scans, with original ordered memory/call effects.
- The three admitted actors are dispatched in captured order 0, 1, 2.
  Flags on inactive actors can still affect the selector, as in retail.
- All 33 reachable selector body words execute. The duplicate increment at
  **0x1503F9C8** and padding at **0x1503F9EC** remain in the exact 35-word slot
  but are not falsely counted as executed.

This brings completed caller comparisons to **1171 three-way cases**, with
**657 actual-dispatcher connections**, 400 of those also running the selector.
All 176 retail caller words remain covered by the randomized graph matrix.

Private stack traces are not claimed identical while the spill/schedule work
is incomplete. The comparison keeps every external write/call and its order,
collapsing only consecutive identical nonvolatile reads with no intervening
external event. The earlier missing-slot and queued-activity negative controls
remain active; saved-register/stack restoration is checked on completed traces.

The native fixture models the fixed end symbol as `D_800CC2D0 + 25`, rather
than allocating a different object at an unrelated address. It still uses
opaque phase callbacks; the actual selector connection is guest-instruction
qualification, not a claim that every downstream phase runs natively.
Selector indices outside 0..24 and complete SDK/physics/animation/rendering/
hardware/PC gameplay acceptance are not claimed by the new matrix.

## Audit And Progress

The pre-edit snapshot covers **6060 function slots**. The rebuilt audit finds
only `func_1502BEE4` changed, with no added/deleted slots, moved addresses or
changed lengths. The scan, dispatcher and selector remain exact. Full Init
code **164048 bytes**, Init data/rodata **17376 bytes**, Debugger **19800
bytes** and Game data **189088 bytes / 720 owners** remain retail-exact.

The patch table is unchanged: **10606 unique rows**, SHA-256
`22f784b5c5dc38114c6d2ed9da81fb74ea9ac3eb5c97c4a3be57d129d1fa4099`.
Owner build and tools checks pass; existing unrelated recipe warnings remain.
The complete actor/viewport/SDK/resource/matching/tool corpus passes **321
tests in 289.549 seconds, no skips**, against the final rebuilt ELF.
`git diff --check` and all **2934 relative documentation links** pass.

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3302 / 5463 (60.44%) | 0 | 2161 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2629 / 4790 (54.89%) | 0 | 2161 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

No converted-function increase is claimed for adjusting this already-counted
C routine. README aggregates, conversion counts and the 47 retained Init ASM
functions are unchanged. No sibling source/build/save/frozen Release change,
host transplant or push is made.

## Reproduction And Next

Run from `64CBFD` in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --schedule
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --declarations
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --interleave
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --workspace
wsl python3 -m tools.experiments.game_actor_update_pass_candidates --cursor
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next: recover the **maximum-depth spill at SP+0x34**, the phase-local base/end
address lifetime, redundant predecessor-load/clear scheduling and the final
176-word schedule. The explicit mask and captured-queue mutation contracts
must remain intact. A reduced word count or equal mismatch score alone is not
a matching proof. The Game objective remains active, with 2161 differing C
functions still outstanding.
