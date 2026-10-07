# Game Scaled Sphere Query Capture Lifetime

Date: 2026-10-07. Baseline: `0841512b`,
[Note 1088](1088-game-scaled-sphere-query-boundary-audit-20261007.md).

Continue the full `func_15145AD8`, VA `0x15145AD8..0x15145C90`,
ROM `0x172F88..0x173140`, retail 110 words/frame `0x88`.
Broader private-actor evidence finds an observable defect in the prior
experimental candidate. The new capture-first candidate corrects it while
retaining the original frame/local offsets, but still emits **111 words,
72 aligned differences**. Production retains the zero-return placeholder;
no installation, guard/profile/header/padder change or matching increment.

## Natural Private-Actor Counterexample

Place the actor so its field `0xDC` is the caller's private inverse slot,
`SP+0x3C`, and its field `0xE0` is `SP+0x40`. Entry scale/inverse are 2.0/0.5,
actor ID 186, center `(5, 5, 0)`, direction `(10, 10, 0)`, ordinary point
outputs and both entry stack phases. No helper return is replaced or forced.

The original caller prologue naturally overwrites actor `0xD2/0xD4/0xD6`
through its saved S0/RA words. With the runner's entry S0 `0x5A000010` and
RA `0xDEAD0000`, the real dimension helper reads radius 16.0, height -8531.0
and zero vertical adjustment. The reference now optionally models these two
caller-save stores before invoking its independent dimension arithmetic.
Do not freeze the actor's entry halfwords or seed replacement dimension outputs.

Retail reads both actor scale fields before storing the private inverse.
The old emitted C stores inverse 0.5 at `SP+0x3C` before reading actor `0xDC`,
thereby reading back 0.5 as the scale. The discrepancy reaches both output points:

| Observable | Retail / Capture-First C | Prior Selected C |
| --- | --- | --- |
| Return status | 1 | 1 |
| Scale before normalizer | `0x40000000` (2.0) | `0x3F000000` (0.5) |
| First output Y | `0x41427C98` | `0x409A7C98` |
| Second output Y | `0xC009F25D` | `0xC014F92F` |

The [preferred experimental body](../../tools/experiments/game_scaled_sphere_query_source_layout_candidates.py)
is `SCALE_FIRST`: capture `arg2->unkDC` before `arg2->unkE0` in C. Its emitted
instructions retain both values before the inverse spill. Tests require exactly
one ordinary mapped read of each field before that write, preserving both
captured values. Retail's read-pair order is reversed; complete instruction
timing equivalence is not claimed. No MMIO, concurrent mutation or native
actor-in-private-stack semantics are inferred from these guest probes.

The old candidate remains reproducible as an effective compiled negative.
Its earlier green suites were bounded to different actor/input placements;
they did not qualify this private-actor window. Do not resume installation
from that older candidate or treat its earlier results as full-frame acceptance.

## Expanded Qualification

[Seventeen caller tests](../../tools/tests/test_game_scaled_sphere_query_source_layout.py)
reuse the maintained complete-caller bank with the new emitted candidate and
[independent evolving-memory reference](../../tools/tests/game_scaled_sphere_query_reference.py).
The existing suite stays reproducible; only the new private-actor checks opt
into the two known caller-save stores. Private helper prologues and whole-frame
byte/timing acceptance remain outside this reference's scope.

- 10,368 new private-actor cases move `0xDC` across `SP+0x38..0x7C`, vary
  both stack phases, IDs 186/187, four output-alias layouts, four scale pairs,
  three centers and three nonzero directions. Execute all five real helpers.
  Compare status, every external byte, ordered external writes, helper argument
  tuples and the bounded caller-local/incoming-home call snapshots.
- Requalify the prior 27,440 bulk guest fixtures against the capture-first C:
  finite geometry, every ID byte, all null masks, signed vertical extrema,
  private input/output windows, natural late homes, lazy/fail-closed fields
  and effective compiled negatives. The improved bulk bank totals 37,808
  fixtures; the old candidate remains a separate bounded regression surface.
- Requalify 126,720 actual 32-bit native calls through the new caller and
  all five real C helpers, comparing status and all 1,920 storage bytes to
  the independent native algorithm. Do not add old/new execution counts
  together as new unique geometry coverage. Native optional inputs remain
  non-null and do not model guest private/home aliases.
- Add an explicit zero-radius case with origin/direction, actor scale fields
  and point storage removed. Both retail and improved C reject after the
  dimension call without touching the absent fields or invoking the normalizer.
- The copied production-preprocessed O2/g3 owner binds the same improved raw
  target and relocations, preserves all 88 other functions/pools/relocation
  ownership and the same two warnings. The actual padder still emits a
  110-word overflow trampoline slot, not the original routine.

The initial two private-actor tests pass in **37.389 seconds**; the initial
sixteen-test complete caller run passes in **195.870 seconds**. The final
combined regression passes **93 tests in 529.685 seconds**, zero skips,
errors or failures. After strengthening the native fixture's old/new source
binding assertions, rerun its 126,720 calls, the captured-read counterexample
and the removed-field zero-radius case: **three tests pass in 4.276 seconds**.
The final 39-control driver also completes successfully.

```sh
PYTHONPATH=. python3 -m unittest \
  tools.tests.test_game_sphere_callee_allocation_match \
  tools.tests.test_game_sphere_callee_frame_recovery \
  tools.tests.test_game_sphere_callee_recovery \
  tools.tests.test_game_sphere_wrapper_match \
  tools.tests.test_game_projection_schedule_match \
  tools.tests.test_game_owner_pool \
  tools.tests.test_game_actor_dimensions_match \
  tools.tests.test_game_scaled_sphere_query_recovery \
  tools.tests.test_game_scaled_sphere_query_source_layout
```

Preserve `full-regression-coverage.json` from that full run: caller 109/110,
dimensions 40/41, normalizer 41/50, wrapper 49/53, sphere 126/126 and dot 13/13
retail words reached. The later focused recheck overwrites `coverage.json`
with its smaller scope; it is not the full-run coverage receipt.

## Source And Scope Controls

The [driver](../../tools/experiments/game_scaled_sphere_query_source_layout_candidates.py)
retains **39 new measurements**, all with empty isolated diagnostics and none
raw exact; 140 measured controls including the earlier 101. Controls are
code-generation evidence, not blanket semantic acceptance of every body.

- Six explicit const/volatile field-access controls and fifteen focused
  physical source-line controls emit exactly the old 111-word/frame `0x88`
  body. Grouped three-vector storage and an empty success scope also emit
  those same words: 23 bit-invariant controls in total.
- Three meaningful grouped scalar/whole-workspace controls retain the original
  storage field offsets but emit 113 words/frame `0x88`, 76 differences.
  Every field is used; no padding, dummy locals or extra vector components.
- Nine nonempty declaration scopes and two inverse-initializer scopes emit
  111 words/frame `0x88`, 73 differences, retaining all original local offsets.
  They remove the duplicated inverse load and produce a plain `bc1f`, but a
  comparison-delay NOP remains. Tests bind the actual branch word, NOP and
  single actor `0xE0` load; deleting that NOP and changing branches is not a fit.
- Straight capture-first emits 111 words/frame `0x88`, 72 differences; scoped
  capture-first emits 111/frame `0x88`, 73 differences. The latter corrects the
  specific counterexample in the disposable probe, but the full new caller
  suite qualifies the straight form, not all scope alternatives.

The preferred raw call relocations remain `0x58/0x100/0x16C`, versus retail
`0x58/0xFC/0x168`; its first 34 words and structured `.mdebug` private offsets
remain direct. Straight capture-first now duplicates the first scale load,
not the inverse load. No closed fitting permutation has been established.

## Retained Baseline And Resume

Keep the production placeholder, linked baseline and README aggregate rows
unchanged. Detailed progress belongs in this note and the DOCS handoffs.
No production rebuild, installed-caller or ROM-checksum acceptance is claimed
for these opt-in candidates.

Fresh retained-ELF audit confirms all **6,059 function slots**, their addresses,
extents and bytes, protected sections, **720 data owners / 189,088 bytes** and
**11,006 guards** unchanged. Converted functions remain **5,466 / 6,042**,
Game **4,793 / 5,321**; exact converted functions remain **3,355 / 5,466**,
Game **2,682 / 4,793**, zero address drift. `make tools-check`, changed Python
syntax checks and `git diff --check` pass. The scoped documentation gate checks
**71 documents / 3,813 relative links**, zero broken links.

1. Start from `SCALE_FIRST`, retaining the new private-actor counterexample and
   37,808-case reference/native qualification. The prior inverse-first body
   is now known to violate this capture lifetime and must remain a negative.
2. Recover the 110-word fit under the existing O2/g3 profile, preserving frame
   `0x88`, private slots, lazy gates and live incoming/output homes. Scoped
   source changes the second branch decision, but does not yet eliminate the
   extra word. Do not repeat the banked access/line/storage/scope controls.
3. Qualify complete caller/helper-frame and instruction-read/input effects
   for the fitting body; then classify only closed differences. Repeat actual
   fitting-body owner/pool/padder/relocation/stale gates before narrow installation,
   a US ELF rebuild and the whole-slot/data/history/regression audit.

Sampler `func_151432BC` and oriented `func_15142600` remain open. No sibling,
frozen Release, real save, runtime or push work.

Ignored receipts: `conker/build/game-scaled-sphere-query-source-layout/` and
`conker/build/game-scaled-sphere-query-source-layout-test/` (measurements,
preferred/scoped bodies, copied owner/overflow, coverage and baseline audits).
