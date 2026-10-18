# Route Actor Update Frame And Save Layout Recovery

Date: 2026-10-18. **Source-level frame/save recovery; not installed; zero credit.**

## Result And Baseline

Continue the same func_15087350 after
[Note 1569](1569-route-actor-update-semantic-recovery-and-frame-boundary-20261018.md),
not a different function. That turn made verified progress by banking the full
semantic recovery in consumer **467adc41**, with tools **a71464c** first.
This turn commits tools **b00486f**, then the retained-capture guard in
**c767262**, before the consumer pin and handoff.

Target generated_B3020, VA `15087350..15087CC0`, ROM `B4800..B5170`,
retail **604 words / frame 0x1C8**. Preserve the complete recovered interface:

```c
void func_15087350(s32 recordIndex, s32 active, f32 lookAhead);
```

The selected complete C point now emits **589 words / frame 0x1C8**, with
the original **five saved S registers plus RA, three saved FP pairs, their
stack slots, and all three incoming argument spill homes**. The first **15**
linked words and final **11** return words are byte-exact. This is still
**15 words short / 481 positional word differences**, including missing words.
There is **no normalizer, frame guard, padding or production installation**.

| Point | Words | Frame | Differences | Status |
| --- | ---: | ---: | ---: | --- |
| Note1569 initial | 588 | 480 | 599 | Original semantic checkpoint retained |
| Earlier frame-only control | 591 | 456 | 595 | Correct size but one extra saved S register |
| Selected phase-bound point | 589 | 456 | 481 | Original save/spill layout, extent still wrong |
| Retail | 604 | 456 | 0 | Required end state |

The selected source is `game_route_actor_update_fit.selected()`, named
`start-gain-offset-bound-10`. Reuse the disjoint scalar lifetimes without
inserting dead locals or raw instructions: loop step/point-X/angle/score
carrier, normalization/absolute-error carrier, point-Z/error, post-loop
start-Z/gain and sort/loop flag. Preserve the **full-width modular record
offset until its gate**, then reuse it as the signed ranking bound using an
explicit `(s32)` comparison. Do not replace that gate with `recordIndex == 0`.
The selected point retains the original s32 ranking counter; byte-counter
alternatives remain separate controls.

Raw selected SHA-256:
`2cf5b5c91a70d570c609fb89d9d6da3516bb690cdf46cdfc6eeb519694ef4902`.
Its **70 relative bindings** have canonical SHA-256:
`d58b6498d00706402c7b74606be29f8fe973b12a6caf1c5b13bfbb4338b98297`.

## Owned Compiler Evidence

One newly owned read-only compiler capture investigates the **old588/frame480
point**, not the new589 point. An isolated complete translation unit must first
match all full-owner target words and bindings. Existing normal O2/g3/no-unroll
flags remain unchanged; no compiler-decision patches or engine installs.
Check the prepared cc/cfe/uopt/ugen fingerprints before and after observation,
all four child paths/exits and driver exit0, final null inferior, and identical
normal/traced text, definitions, bindings and pools.

The four fired frame observations are:

| Frame | Locals | Saved | Outgoing | Observed Temporary Pool |
| ---: | ---: | ---: | ---: | --- |
| 0 | 0 | 0 | 0 | empty |
| 48 | 0 | 48 | 0 | empty |
| 64 | 0 | 48 | 16 | empty |
| 480 | 416 | 48 | 16 | empty |

For isolated procedure769, CFE defines **396 local bytes**, UOPT defines
**416**, and UGEN consumes that span. Thus the excess already exists upstream
of UGEN's final frame construction. Do not call the20-byte span growth20
independent spill bytes: alignment/storage accounting is not established by
that subtraction alone. The new lower M-404 home is a **four-byte J integer**,
not a float spill; the original first point-X home remains M-372.

The observed frontend array extents are x/y/z16 bytes at M-56/-72/-88,
copy132 at M-228, order32 at M-260 and scores68 at M-328. These describe this
captured candidate, not the original retail C layout. No capture of the new
589-word optimizer frame is claimed. The completed capture is audited and
reused by tests without another debugger launch.

The retained concatenated stdout/stderr log contains three nonfatal unresolved
UGEN-probe messages. It is not warning-free; do not infer their timing from
the concatenated log order. All producer/consumer completion, fired-probe and
unchanged-object gates still pass. No existing game/application was attached.

## Fresh Qualification

**All18 tests pass in56.811 seconds, no skips.** This includes strengthened
literal argument-load/register checks and an effective retained-capture guard:
an existing capture directory rejects another capture before setup or baseline
rewrites. The earlier17-test run passed in55.086 seconds and two focused tests
in8.696 seconds; the follow-up guard changes no candidate bytes or bindings.

- Re-run703 paired real-helper cases on the selected589-word C, not just on
  the old588 point. Compare complete public RAM, canonical calls and saved ABI
  against retail and the independent ordered-binary32 reference.
- Connect494 real helper words, independently equal to retail: vector83,
  cubic49, derivative62, progress212 and neighbor88. The703 cases comprise
  216 core,80 provider effects,319 signed-lap/ranking,16 width/actor and72
  active/signed-tick cases. All earlier finite/provider exclusions remain.
- Six axis-aligned error-limit witnesses and sixteen actual retail caller
  windows still pass. The latter execute complete callees, actual argument/
  delay words, saved caller state and poisoned-V0 consumers in both parents.
  Full callers, unknown indirect interfaces and hardware traps are not proved.
- Seven freshly compiled negatives of this selected point produce ordinary
  wrong results/call contracts, not crashes or exhausted budgets.
- Thirty-one new primary-profile source screens preserve72 neighbors/pools.
  Register-keyword variants emit unchanged words; nested blocks increase the
  frame rather than repair it. The25 initial/scalar screens add300 paired
  cases, and six phase-bound screens add72. Keep these372 cases separate from
  the703 selected-point cases and from older Note1569 screens.
- A fresh normal-profile before/after compile preserves all72 non-target
  bodies, pools and the strict raw projection-override words/bindings. Both
  profiles keep their existing flags. This is not actual production Make/
  padding qualification or a normal-profile target byte match.
- All589 raw-word and70 binding mutations fail the fingerprint gate. Compiler
  evidence adds24 frame/wire fact controls,11 lifecycle controls and four
  retained payload controls. These are not additional semantic-negative runs.

## Remaining Opening Boundary

Thirty-four fired memory-access prefixes cover cuts0..16 in both stack phases.
**28 agree / six reject** for the compared RAM, GPR/FPR, access/call trace,
PC and delay identity. Both phases first reject at **cut14 / PC150873A4**.
RAM, FPRs and access trace still agree there; **GPR14 and24 differ**.

The first15 linked words now match. At the next word both load the same
incoming index from SP+0x1C8, but use different temporary registers:

| Retail | Selected Raw C |
| --- | --- |
| `8FB801C8` - LW T8,0x1C8(SP) | `8FAE01C8` - LW T6,0x1C8(SP) |

This is real argument-register evidence after the prior saved-RA/address gap
closed, not a statement that all private states match. Instruction bytes and
physical trap behavior are not equated by the prefix model. Later local array/
scalar homes, roles, access order and the full604-word extent remain open.

The original save slots now emit directly from source:
RA44; S4/S3/S2/S1/S0 at40/3C/38/34/30; F24/F22/F20 pairs at28/20/18.
Do not use the older591-word extra-save control as the current candidate.
Its named source/object/receipts remain preserved separately.

## Bank And Resume

Tools **b00486f**, then **c767262**, first. Three task files are identical, ASCII and AST-valid
in both tools copies. Both copies pass three repository-setup tests and smoke
checks; consumer `make tools-check` passes. Preserve all1,281 old dirty mirror
hashes and its ddbdd16 HEAD. Add only the three absent files:1,284 dirty leaf
paths, no mirror commit/reset.

All23 production/reference inputs remain frozen. The installed Note1568
baseline audit is freshly rechecked and passes. Whole ELF/source/guard hashes
remain respectively `3c8fd041...dd5591a`, `fb512dd6...c8ddbd` and
`cc92cdc4...ab49d4` as fully recorded in Note1569. No new production build,
guard/Makefile/progress/root-README change, or fresh matching recount. Carry
forward Note1568's **Game2991/4828**, **total3664/5501**, **1,837 different /
zero drift**. This checkpoint earns **zero** matching/conversion credit.
No push, Claude call, emulator, host edit or frozen Release action.

```sh
python3 -m tools.experiments.game_route_actor_update_frame --audit
python3 -m tools.experiments.game_route_actor_update_fit --qualify
python3 -m unittest tools.tests.test_game_route_actor_update_frame -v
python3 -m tools.experiments.game_route_record_integration --audit
```

The existing screen artifacts are prerequisites of the suite. To regenerate
them with unchanged inputs, run the fit module separately with no options,
`--roles`, `--locals` and `--bounds`. Do **not** rerun `--capture`: audit the
completed evidence instead. Ignored `game-route-actor-update-frame/` keeps
the original owned capture; `game-route-actor-update-fit/` keeps31 complete
source/object/command screens, the older frame control and `qualified-bound`
with model-labelled `bound-*.json` receipts.

Next continue **the same function**: restore604 words, the argument temporary
roles and the remaining local homes/scheduling. Keep the recovered frame,
save/spill layout, full-width offset semantics and complete body fixed.
Then complete native32/UBSan, aliases/private access prefixes, all-word/binding
matching, actual mixed-profile padding/Make, independent GNU rebases, first
whole-ELF prediction, installation, protected-data/body/address audit and a
fresh recount. Preserve the installed setup/vector/spline/dispatcher baseline.
The broader Game goal remains active.
