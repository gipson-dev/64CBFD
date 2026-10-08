# Game Scaled Sphere Query Boundary Audit

Date: 2026-10-07. Baseline: `01fd54c8`,
[Note 1087](1087-game-scaled-sphere-query-recovery-20261007.md).

Continue the complete `func_15145AD8` recovery, VA
`0x15145AD8..0x15145C90`, ROM `0x172F88..0x173140`, retail 110 words/frame
`0x88`. The selected experimental C remains **111 words, frame `0x88`,
72 aligned differences**, with the original private-local offsets. It is
not installed; production still has its zero-return placeholder. No new
matching increment, production-source/profile/shared-header/padder change or target guard.

## Signed Offset And Call Boundaries

Extend the [maintained caller tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_scaled_sphere_query_recovery.py)
and [independent reference](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/game_scaled_sphere_query_reference.py):

- 9,216 new connected guest cases vary signed actor `unkD6` values
  `-32768/-187/-2/-1/0/1/187/32767`, IDs `0/186/187/255`, four Y-scale pairs,
  three center-Y values, three nonzero directions, four external output aliases
  and both stack phases. Check the original dimension center Y before the
  normalizer and the scaled center Y before the wrapper. Below ID `0xBB`,
  the signed adjustment participates; at/above the boundary it is ignored.
- 216 new private input-window cases place origin or direction at caller
  frame offsets `0x38..0x7C`, with three finite vectors and both stack phases.
  The reference retains sequential copies and live alias effects; it does
  not replace overwritten private input with an entry-time frozen vector.
- Every existing and new reference-backed guest fixture now compares two
  call-boundary snapshots when reached: 20 caller words at `SP+0x38..0x84`
  and all eight incoming homes, immediately before the real normalizer and
  wrapper calls. These cover initialized vectors/scales/dimensions and
  untouched seeded locals, not the entire caller/helper stack frame. The
  observer reads memory directly without adding fake guest read events.
- Expand the actual 32-bit native fixture from 25,344 to **126,720 calls**
  with `unkD6 = 0/-32768/-1/1/32767`. Run the selected C and all five real
  C helpers against the independent native algorithm, comparing status and
  all 1,920 storage bytes. Optional inputs remain non-null; native private
  stack/incoming-home aliases are not claimed.

The maintained bulk guest bank is now **27,440 fixtures**, each checked against
original retail instructions and emitted experimental C with all five real
helpers connected. Ordered external writes, external bytes, helper arguments,
status and the bounded call snapshots agree. Natural late-output-home writes,
lazy/fail-closed fields and effective compiled semantic negatives remain.
The first twelve expanded tests pass in **75.168 seconds**, zero skips/errors/
failures. Coverage and final combined regression are checked below.

This does not qualify every raw instruction read, arbitrary invalid pointers,
all floating-point/FCSR/NaN payload behavior, complete private helper frames,
native stack aliases, hardware, gameplay or host adoption.

## Scheduling Controls

The [new focused driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_scaled_sphere_query_schedule_candidates.py)
retains 30 O2/g3 controls, all with empty isolated compiler diagnostics and
none raw exact. Together with the prior 71 controls, **101 measurements**
are maintained. The selected source/profile and its ABI remain unchanged.

| Family | Controls | Words / Frame / Aligned Differences |
| --- | ---: | --- |
| Equal/reversed-equal/boolean-not zero gates | 9 | 111 / `0x88` / 72 or 112 / `0x88` / 79 |
| Nested height/radius gates | 4 | 111 / `0x88` / 72, 73 or 77; both nested 112 / `0x80` / 109 |
| Struct/union scale pairs | 2 | 111 / `0x88` / 72; 113 / `0x88` / 76 |
| Three-component array views | 3 | 111 / `0x88` / 72 |
| Volatile incoming pointer homes | 8 | 111..114 / `0x80`, `0x88` or `0x90` / 78..112 |
| Shared failure exits | 4 | 111 / `0x88` / 77 or 73; 109 or 105 / `0x88` / 77 |

Tests pin all 30 compiled results and structured `.mdebug` receipts. These
controls are measured code-generation evidence, not semantic acceptance of
every alternative body. Shorter shared-failure forms alter branch layout and
are not selected; do not insert instructions or patch branches to force retail.

In the selected body, the second zero-check uses a branch-likely inverse-load
delay slot plus an unreachable duplicate actor `0xE0` load. Retail instead
prepares the normalizer addresses around the comparison and has a plain
`bc1f` with a NOP delay slot. Both have the separate unreachable radius load
after the first rejection. The extra inverse load contributes the additional
word and shifts later calls. Raw call relocations remain `0x58/0x100/0x16C`
versus retail `0x58/0xFC/0x168`. This is not yet a closed word permutation.

## Copied Owner And Overflow

The production-preprocessed O2/g3 copied owner emits exactly the same raw
selected body and target-relative relocations as the isolated compilation.
It retains all **88 other functions** byte-for-byte with their relocation
ownership, normalized `.rodata`/`.data` pools, and the same two warnings.
The owner still contains 89 functions; this is a disposable copy, not a
production edit.

Invoke the actual existing padder with the unchanged retail layout and all
11,006 historical guards. Its emitted target slot contains a jump relocation
to `__retail_overflow_func_15145AD8` followed by 109 zero words, not the original
110-word routine. The full selected body is emitted in the overflow section.
This directly confirms that the current candidate is **not an in-slot match**;
no new assembly/link/runtime acceptance of that overflow candidate is claimed.
The copied-owner and initial 26-control tests pass in **35.949 seconds**.

## Retained Baseline And Resume

All **76 focused tests pass in 317.745 seconds**, zero skips/errors/failures.
This includes all fourteen expanded caller tests, dimension tests, callee
allocation/frame/recovery, wrapper, projection-schedule and owner-pool tests.
Original coverage remains caller 109/110, dimensions 40/41, normalizer 41/50,
wrapper 49/53, sphere 126/126 and dot 13/13. The caller's one unvisited word is
the structurally unreachable radius load at `+0x90`, not an acceptance shortcut.

The fresh retained-ELF audit preserves all 6,059 linked slot bytes/addresses/
extents, protected sections, 720 Game-data owners/189,088 bytes and the complete
11,006-row guard history. Counts remain total 5,466/6,042 converted,
3,355/5,466 exact; Game 4,793/5,321 converted, 2,682/4,793 exact; 2,111 still
different and zero drift. Init and Debugger counts are unchanged.
Project-tool smoke checks, changed Python syntax and whitespace gates pass.
Documentation gate: 70 documents, 3,800 relative links, zero broken.

No production rebuild is required or claimed for these opt-in experiments.
Keep the original linked baseline and the main README aggregate tables intact.
Detailed progress belongs in this note and the DOCS handoffs, not the root README.

1. Recover a 110-word form under the existing O2/g3 owner profile, retaining
   frame `0x88`, every original local offset, lazy dimension checks and the
   live incoming/output-home behavior. The controls above are already banked;
   do not repeat them as a new recovery result.
2. Once the fit exists, qualify complete caller/helper-frame effects and raw
   read/instruction-input timing, then classify only closed scheduling/register
   differences. Call-boundary equality is not a substitute for that gate.
3. Repeat copied-owner/pool/warning checks for the actual fitting body; finish
   relocation/padder/stale-guard/installation gates, a US ELF rebuild and the
   whole-slot/data/history/regression audit before claiming a match.

Sampler `func_151432BC` and oriented `func_15142600` remain open. No sibling,
frozen Release, real save, runtime or push work.

Focused regression command, from the repository root in Linux/WSL:

```sh
PYTHONPATH=. python3 -m unittest \
  tools.tests.test_game_sphere_callee_allocation_match \
  tools.tests.test_game_sphere_callee_frame_recovery \
  tools.tests.test_game_sphere_callee_recovery \
  tools.tests.test_game_sphere_wrapper_match \
  tools.tests.test_game_projection_schedule_match \
  tools.tests.test_game_owner_pool \
  tools.tests.test_game_actor_dimensions_match \
  tools.tests.test_game_scaled_sphere_query_recovery
```

Ignored receipts: `conker/build/game-scaled-sphere-query-schedule/` and
`conker/build/game-scaled-sphere-query-test/` (including `schedule-records.json`,
copied owners, warning records, and `owner-overflow.s`).
