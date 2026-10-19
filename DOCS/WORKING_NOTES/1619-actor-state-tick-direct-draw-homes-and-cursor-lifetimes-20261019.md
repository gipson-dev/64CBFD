# Actor State Tick Direct Draw Homes And Cursor Lifetimes

Date: 2026-10-19. Consumer predecessor: `b23d663e`; tools predecessor: `8a650a3`.
Tools checkpoint: `cdcece5`, committed before the consumer documentation/pin.

## Direct C Progress

Continue complete **func_1508A6FC**, VA `1508A6FC..1508B194`, ROM
`B7BAC..B8644`, from [Note 1618](1618-actor-state-tick-spill-ownership-and-cached-timer-20261019.md).
The new [selected experimental source](../../tools/experiments/game_actor_state_tick_draw.py)
retains **678 words/frame 288**, recovers **nineteen named homes** and reduces
raw aligned word differences **600 to 344**. No post-compile transform is used
for this result. It is still non-matching and is not installed in production.

This checkpoint closes the missing draw-index accesses and nonpositive-count
cursor-store gating demonstrated in Note 1618. The source changes are bounded:

- Reuse the dead selector as the draw index instead of extending the main slot
  local's saved-register lifetime. Rename the reused selector to `index`, since
  its group, difficulty and draw uses are all indices.
- Exchange that declaration with the already-real status cursor declaration.
  This recovers the draw index's actual SP+A0 save/reload around TEXT, without
  adding a local or moving the seventeen previously recovered homes.
- Recover `actorAction` as s32 rather than u8. Its public inputs remain byte
  loads, but its retained call-save value is a full word at SP+104, as in retail.
- Use the running byte offset for row-table accesses, retaining a separately
  expressed slot-indexed timer readback. The actual public read is not folded
  away or replaced with a literal zero.
- Compute the three opening cursor addresses eagerly through existing pointer
  locals, then assign reset/status/band only inside the positive-count branch.
  This retains the retail header shape without the three empty-path stores.
- Retain the latch row through the dead `context` pointer just before the timer
  updates. The sampled S6/S7 latch/elapsed roles now match retail. Earlier latch
  captures changed other roles and are retained as alternatives, not selected.

The generic `address` name replaces `otherActor`, since that existing pointer
also carries an opening cursor address. There are still 39 real declarations:
no dummy storage, volatile, assembly, physical-register binding, new compiler
profile, header change or production word guard.

The new homes are `index` at **A0** and `actorAction` at **104**; the other
seventeen are those qualified in Note 1617. Debug offsets are checked against
actual emitted SW/LW pairs, not treated as proof on their own. In this source,
the actor-action pair is at instruction origins **303/304** and draw-index pair
at **638/658**. Source and retail schedules still differ around these origins.

## Fresh Qualification

[Thirteen tests](../../tools/tests/test_game_actor_state_tick_draw.py) pass,
no skips: **33.740s primary / 36.482s mirror**. Each checkout separately compiles
and qualifies the selected complete source.

- All 262 completed fixtures compare independent state-machine results, helper
  calls/arguments, public stores, public memory, return masks and ordered public
  reads. The MIPS oracle also checks restored saved GPR/FPR state. These fixtures
  visit 660/678 retail words, not complete instruction or exception coverage.
- Twenty-four additional sixteen-slot read-footprint pairs pass. The existing
  no-readback source control still loses seven real timer reads, so it remains
  an effective negative rather than an accepted shorter body.
- Thirty-eight effective guest alias pairs cover all nineteen homes in both
  stack phases. Requested mutations fire, each retail alias has an observable
  effect, and new source agrees with retail. Four predecessor controls reject
  the old draw-index/action-save layout after their mutations fire.
- Twelve additional actor-action aliases cover 0, 4, 5, 0x105, 0x80000005 and
  0xFFFFFFFF in both phases. The retained value is a word, not truncated to a
  byte after ACTION. These are bounded guest-stack tests, not a portable C
  promise that a helper can access unescaped locals.
- Four count -1/0 and stack-phase pairs prove that retail and new source skip
  their three cursor-home stores; predecessor source performs them. All eleven
  eager table-pointer stores still agree at their fixed retail frame homes.
- At STATUS for slot 1 in the retained sixteen-slot B9 fixture, the complete
  sampled S0..S7/FP role vector now agrees: offset, GLOBAL, slot, actor, first,
  group, latch row, elapsed row and bit. This is one measured call boundary,
  not whole-function register/PC equivalence.
- Fifty-seven native32 fixtures pass O0/O2/O3 with UBSan on the newly selected
  source. All three compiled semantic negatives remain effective, and the
  separate signed-overflow control fires SIGILL -4. These are fresh receipts,
  not inherited native results from the previous source.
- Both complete-owner profiles preserve all 72 other bodies and normalized
  pools; isolated words/bindings equal complete-owner output. Both profiles
  produce the pinned 678-word body with frame 288. All seven production input
  hashes remain unchanged.

Project-tools smoke checks pass in both copies, all four new Python files parse,
and the primary `--names selected` CLI reports the same source hash, nineteen
homes and 344 differences. The initial test fixture guessed the action-pair
origins two words early; reading the object corrected that assertion before the
final complete runs. No production fix was needed for that test error.

## Remaining Layout And Alias Boundary

The timer-reset alias is still open in the direct source. Two tests mutate the
timer-table home at SP+C4 during STATUS and explicitly require the real reset
store. Both new-source runs still differ from retail's cached current-row
readback. Note 1618's partial transform qualified that distinction for its older
raw body; its source/binding fingerprints must not be applied to this new body.

Live slot-0 STATUS probes give these remaining row/cursor homes. Table-base
homes are separate and remain unchanged; equal values at slot 0 are interpreted
with emitted uses, not as proof of every lifetime.

| Role | Selected SP Offset | Retail SP Offset |
| --- | --- | --- |
| Timer row | 70 | 7C |
| Cooldown row | 68 | 74 |
| State row | 60 | 6C |
| Event row | 5C | 68 |
| Action row | 54 | 54 |
| Reset cursor | A4 | 84 |
| Status cursor | FC | 60 |
| Band cursor | 9C | 5C |

Do not install merely because the shape, nineteen homes and sampled main roles
now agree. Anonymous spill ownership, whole-function temporary roles and
instruction scheduling, remaining aliases/private memory/fault prefixes/FCSR,
complete instruction coverage, independent original-assembly/GNU rebases,
actual padding/Make/strict first image and installed-state gates remain open.

An exploratory import of a disassembly helper also evaluated its transitive
legacy candidate screen. Its ignored outputs are not acceptance evidence here;
production fingerprints are unchanged. Avoid importing
`game_route_actor_update_extent` just for its helper on resume; use the bounded
objdump invocation or a side-effect-free helper instead.

## Preservation And Resume

Only the two absent new task files were copied into the independent mirror.
Their subsequent updates were guarded by their own pre-edit hashes. Mirror
HEAD `ddbdd16b` and all **1,442 older dirty leaf hashes** remain intact; no older
path disappeared or changed status. No mirror commit/reset/stash/clean, push,
host edit or frozen Release operation, dependency change or advisory call.

Production C, assembly, guards, ELF, Makefile, progress and root README are
unchanged. Installed totals remain the Note 1614 checkpoint, not a new recount:
Game **3,017/4,832**, overall **3,690/5,505**, 1,815 different/zero drift; owner
**69/73** exact. Production A6FC is still its 12-byte stub/665 classified
differences; the experimental complete source's 344 differences are separate.

```text
Selected raw: 9fa41b55435921115dfe029d37b330f90b787329f0b8b83dfb3630a3b242ffd9
Bindings:     449c7456ea2d4a9f6df7e195bbe27a810b6d08ececef40ca52232167582f4a49
```

Ignored receipts: `conker/build/game-actor-state-tick/lifetimes/homes/draw/`,
including candidate/control sources, final primary/mirror logs, owner/native
artifacts, input snapshots and measured register-boundary JSON. The consumer
commit hook refreshes Graphify; audit the retained prior nodes before closing.

Next: use this selected source, not the older homes/spill source, to recover the
remaining frame slots and cached timer readback, then complete lifetime-scoped
instruction-origin/schedule qualification. Keep the wider Game goal active.
