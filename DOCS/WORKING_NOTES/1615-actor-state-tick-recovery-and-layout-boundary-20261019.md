# Actor State Tick Recovery And Layout Boundary

Date: 2026-10-19. Consumer predecessor: `02a8217`; tools predecessor: `4a805fc`.
Tools checkpoint: `e831838`, committed before the consumer documentation/pin.

## Result

Recover a complete, typed experimental body for **func_1508A6FC**, following
[Note 1614](1614-zone-selection-complete-match-20261019.md). Retail occupies
678 words/2,712 bytes, frame 288, VA 1508A6FC..1508B194, ROM B7BAC..B8644.
The production definition remains its original 12-byte zero-return stub.
**No installation, guard additions, compiler change or matching credit.**

The complete retail routine and its direct script-dispatch caller at
`func_1509E0A4` establish a no-argument interface and a returned changed-slot
mask. It captures the actor count, active/seen masks and state tables, advances
per-actor timers and transitions, updates signed steering bytes, calls the
now-exact zone pass, and conditionally draws per-player counters in category B9.
The independent reference retains captured inputs versus live global reloads.

The donor snapshot's complete-looking body is not a byte-exact import. Its
32-bit reads/stores at byte/halfword offsets, word-pointer increments by four,
integer interpretations of floats, and stale context after helpers are wrong.
The candidate instead uses the retail byte/halfword widths and signedness,
four-byte cursor strides, real float expressions and current-global reloads.
It keeps the original function name and a short purpose comment. Offset-based
table names are retained where stronger domain names are not established.

## Measured Source Boundary

[Candidate and owner screen](../../tools/experiments/game_actor_state_tick_candidates.py)
emit **658 words/frame 328, 662 aligned differences**, with 62 relocation
entries and no compiler diagnostics. These aligned differences include length
delta; they are not the installed classifier's 665 stub differences.
Both normal and existing no-unroll profiles emit identical raw words/bindings.

Seven source forms are retained for reproducible screens. Reusing drawing
cursors yields 656 words/frame 320, not a match. Word-sized action temporaries,
initialized captures and integer context expressions do not close the gap.
The earlier artificial saved-action local was removed before final tests.
No dummy storage, volatile, register binding, instruction array or broad
compiler-profile search is used.

The opening is the first concrete layout boundary: retail materializes eleven
table bases before the positive-count branch and retains their pointer homes.
The current compiler folds many derived accesses into one captured context
base and sinks address work into the loop. Its larger private frame also
differs. Do not manufacture a whole-function guard rewrite from these results;
recover the actual source lifetimes and homes first.

## Bounded Qualification

[Seven tests](../../tools/tests/test_game_actor_state_tick_candidates.py) pass
in **29.462s primary / 34.835s mirror**, with no skips. Fresh receipts cover:

- 262 completed fixtures comparing retail and the full raw C against an
  independent state-machine reference. Ordered public stores, all public
  memory, helper arguments/results, return masks and saved GPR/FPR lifetimes
  agree. Fixtures visit 660/678 retail words, not the entire routine.
- Nonpositive and 1/4/16-slot counts, both stack phases for mask/count cases,
  active/seen masks, first visits, B7/B8/B9 gates, signed timer boundaries,
  action types, signed steering, group transfers and random threshold paths.
- Thirty requested helper-mutation fixtures, each with a fired-call gate:
  replacement globals and changes to delta, difficulty, captured count/masks
  and action data. All ten opaque helper types are exercised. These are
  bounded provider contracts, not recovered helper implementations.
- Three compiled effective negatives reject a widened actor flag, four-word
  cursor stride and inclusive random comparison. A corrupted input fingerprint
  is rejected. Seven pinned production inputs remain byte-identical.
- Both complete owner profiles preserve all 72 other function bodies and
  normalized pools. Complete-owner target words and bindings equal the
  isolated typed candidate. The owner-only fixture keeps the inherited
  old-style `func_1508CAD8()` declaration because that unrecovered callee is
  still an empty-parameter stub; the isolated fixture uses its six-word call
  interface. No production neighbor signature is changed.

The first model run exposed missing signed-byte-load support in the reused
bounded oracle; a local decoder now handles that opcode. A transition-mutation
fixture initially never reached its provider; the explicit fired-call gate
caught it and the final fixture drives the real transition. Failed runs are
not acceptance evidence. Final comparison counts increment only after both
implementations pass, not after failed subtests.

Native32/UBSan, complete instruction coverage, private-frame/access-fault and
alias equivalence, independent GNU rebases, actual padding/Make/strict first
link and installation gates remain **open**. No hardware/FCSR, full caller,
helper or gameplay acceptance is inferred from this bounded semantic screen.

## Preservation And Receipts

Primary and mirror shared tools checks pass. Only two absent task files are
copied into the independent mirror; its HEAD `ddbdd16b` and all **1,434 older
dirty leaf hashes** are preserved. No mirror commit/reset/stash/clean or push.
No host source/build, frozen Release, save, account, dependency or advisory
agent operation. The user confirmed the previously overwritten `Conkers`
compiler scratch file was disposable; no recovery is needed. Compiler source
and output operands remain relative to `conker`, avoiding space truncation.

Production C, guard CSV, ELF, Makefile and progress CSV retain Note 1614's
fingerprints. Installed totals therefore remain Game **3,017/4,832** and
overall **3,690/5,505**, 1,815 different/zero drift; owner **69/73** exact.
These are the unchanged installed checkpoint, not a new matching increment or
fresh full recount. Root README is untouched.

```text
Raw C: 6603fe611bd81263bfec8076976c2cd45cbda2e895445ed18b8d2c2ea751fb55
```

Ignored receipts: `conker/build/game-actor-state-tick/`, including both profile
screens, owner comparisons, primary test log and `mirror/test/mirror-tests.log`.
The consumer commit hook refreshes Graphify; preserve and audit its prior nodes.

## Next Steps

1. Recover retail's eager table-pointer captures and their named private homes
   from the complete source. Preserve count/mask snapshots and live global
   reloads across providers; do not replace them with repeated queries.
2. Recover frame 288, saved-register allocation and complete 678-word shape.
   Use the existing compiler profile; the normal screen gives no improvement.
3. Extend the focused qualification to the remaining instructions, actual
   native C, private/access-fault/alias cases and independent original-assembly
   rebases before selecting a source-origin normalization, if still needed.
4. Only after qualification, run owner/padding/Make/strict-image gates, install,
   rebuild and recount. Keep the wider Game goal active. The other owner
   nonmatches remain func_15086364, func_1508CAD8 and func_1508DC24.
