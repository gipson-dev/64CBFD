# Route-Search Start Home, Extent And Ordered Reads

Date: 2026-10-19. Consumer predecessor: `d1c19455`; tools predecessor:
`5830074`. Tools checkpoint: `a7eba1d`, committed before the consumer pin.

## Result And Scope

Continue complete **func_15086364**, VA `15086364..15086BD0`, ROM
`B3814..B4080`, from
[Note 1623](1623-route-search-capture-closure-and-start-home-boundary-20261019.md).
The [new experiment](../../tools/experiments/game_route_node_search_start_home.py)
retains the complete typed semantic C and reconstructs its real start spill
and three reloads. Its normal linked result now has **539 words/frame 1536**,
equal to retail, with **426 actual word differences and no missing words**.

Both previously failing start-home aliases close. All **426 fixture/phases**
now finish with byte-identical complete public/private memory, and all **213
phase-zero public-read sequences** agree in address, width, value and order.
These are bounded acceptance results, **not a byte match or installation**.
The production target is still its 12-byte zero-return C stub/522 classified
differences; installed totals and matching credit do not change.

## Real Start Lifetime

Retail holds the incoming start in a register through validation and initial
goal membership. After cost initialization/table capture, it spills that value
to incoming SP+0 / frame SP+600, before initial neighbor expansion. Three later
load sites recover it for initial parent writes, path termination and neighbor
exclusion. The selected raw C retains the value in S8 instead.

The new pure transform preserves all **535 raw C origins**, inserts exactly
four derived private-memory instructions, and retains all **14 relocation
entries** at their moved origins:

| Output Word | Derived Instruction | Source Value/Use |
| --- | --- | --- |
| 95 | SW S8, SP+600 | incoming start captured by raw origin 12 |
| 146 | LW S8, SP+600 | initial parent-byte store, raw origin 148 |
| 309 | LW S8, SP+600 | path termination, raw origin 311 |
| 337 | LW S8, SP+600 | relaxation neighbor exclusion, raw origin 336 |

These are functional stores/reloads, not NOP padding. The predecessor's table
SP+5FC-to-SP+60 mapping and directly emitted typed avoid-pointer reloads remain
qualified. No source instruction is omitted or duplicated. All branch targets
are recomputed from source origins; no branch/delay pair is separated, and
absolute internal jumps are rejected. Whole raw/binding fingerprints, expected
start definitions/uses, destination ownership and output SHA are mandatory.
The normalizer cannot read files/ROM; its test forbids that operation.

The source C itself remains **535 words/frame 1536/492 counted differences**,
including its four missing words. The separately checked no-unroll source is
379 words/frame 1520/531 differences. The 539-word result is explicitly a
**post-compile reconstruction**, not direct compiler output or a new profile.

## Ordered Public Reads

The opening distance calculation previously read origin X before neighbor X.
Reorder exactly raw origins **151, 152, 150**: form the neighbor address, read
neighbor X, then read origin X. These three expected words have no intervening
control entry or conflicting definitions. No memory access is invented or
removed; all operands remain source-derived. A branch into this reordered
group is rejected rather than silently redirected into its middle.

All 213 bounded public-read lists now agree literally. The prior 535-word
capture candidate remains an effective schedule control: its default read
multiset agrees, but its ordered list differs at the initial X-coordinate
loads. This is not proof of every private-access order, full fault prefix,
arbitrary concurrent mutation or hardware behavior.

## Fresh Qualification

[Eleven tests](../../tools/tests/test_game_route_node_search_start_home.py) pass
in both copies with zero skips/errors/failures. Final harness elapsed times:
**101.745s primary / 24.205s mirror**. Earlier 11-test runs predate the final
complete-memory assertion and are not substituted for these final receipts.

- **426 fixture/phases** retain the independent reference's return, helper
  calls/arguments, ordered public stores and public memory across retail,
  rolled C and reconstructed normal C. Saved-register/provider-clobber checks
  remain in the existing guest runner.
- **426 retail/reconstructed comparisons** prove complete final memory
  equality, including seeded private RAM, plus identical SP+600 read/store
  histories. This is final-memory equality, not full intermediate machine
  state or equality of caller-saved register/FPR contents at every instruction.
- **Two start-home aliases** after the second executed GOALS-byte read now
  yield waypoint **3 in both**; the old capture candidate yields baseline 1.
  Both gates and requested stores must fire, and full public signatures agree.
- **Two early aliases** after the first GOALS-byte read are overwritten by
  the real late start spill: the candidate records mutation 1 then saved start
  0, and agrees with retail's baseline result. This rejects an early-only
  capture interpretation. **Two selected-cost aliases** still agree at 2.
- **Four table/avoid capture aliases**, their **four old-capture negatives**,
  six established path/flag/F2 aliases and two old-F2-save negatives remain
  effective. Alias tests qualify their stated public signatures and fired
  homes; complete private equality under all aliases is not claimed.
- **213 underlying C native32 fixtures** pass O0/O2/O3 with trap-mode UBSan;
  five compiled semantic negatives remain effective and the overflow control
  still fires SIGILL -4. Native tests qualify the underlying complete C, not
  execution of the post-compile MIPS mapping on the native host.
- **535 raw-word**, **14 binding** and **535 linked non-binding-field**
  mutations reject stale input. Independent branch-target/delay accounting
  verifies the full origin map. All four new Python copies parse, both new
  task files are byte-identical and both project-tools checks pass.
- Both raw full-owner profiles preserve **72 other bodies/pools**, and raw
  isolated/owner payloads agree. Applying the transform to the actual GNU-
  linked owner target yields the isolated reconstructed target exactly. A
  resized/padded 539-word owner object and its metadata are **not built or
  qualified** at this stage; actual integration remains gated below.

Coverage stays **538/539 retail words**, with offset **0x7C8** unvisited.
The prepared guest code map remains disjoint at 18000000. Deliberate frame
mutations are layout probes, not portable C semantics.

## Rejected Source Screens

Nine early-capture/late-home source forms use existing current/next/previous
values or a real original-start local, with late assignments before costs or
table setup. They still emit an entry-time parameter store and shift the
frame to 1544 (544-548 words), changing accepted homes. Typed versus ordinary
late assignment does not cure that. None is selected or installed.

The ten cached screen objects, including the predecessor control, are retained
with their complete source text and raw object fingerprints checked against
the current generator. The corrected summary measures the incoming home from
each candidate's actual frame, not an assumed literal offset 600. These are
reused compiler screens, distinct from the fresh final two-copy tests above.

## Preservation And Next Action

All seven production input fingerprints, assembly, manifest, ELF, Makefile,
progress CSV and root README are unchanged. Installed baseline stays **Game
3,018/4,832 (62.46%)**, **overall 3,691/5,505 (67.05%)**, 1,814 different/zero
drift; owner **70/73 exact**. No new matching credit.

All **1,455 older dirty mirror leaves/statuses** and HEAD `ddbdd16b` are
preserved. Only two previously absent task files are added, giving **1,457
dirty paths**. The final assertion update touches only this turn's owned new
test after an exact fingerprint check. No mirror commit/reset/stash/clean,
push, host/frozen Release, save/config, dependency/compiler or advisory change.

```text
Raw C:      c9cc61e01da4a0bf630aa5ff8a88a5f4b3c3a4a1709e2fd8142a56110fd5b9b7
Bindings:   d773bb14cc8b0e5c4f019c38b74b90010d7d46e5cc0dd2786ab3dd0e2e6d2161
Normalized: 8b56fc62945059f660315733aeec17aec682bbed9e2b9d7f1552b40c14a3bfb4
Semantic C: fe18ad7f5939c490f2389da778d33ebdacf529e0f0fbee2b6f6298cdbd5258d2
```

Ignored receipts live in
`conker/build/game-route-node-search/loop/captures/qualified/start-home/`:
final primary/mirror logs and JSON, test receipts, full start histories,
closed alias and old-read-order controls, source/object screens, fingerprints,
production snapshots, mirror baseline and graph baseline/audit. The consumer
commit hook refreshes the graph; preserve all old nodes or unique relocations,
including the 19,398 excluded-but-existing nodes from 2,972 files.

Next, continue **this same 426-difference function**: recover lifetime-scoped
GPR/FPR allocation and the remaining original instruction/private-store
schedule. Early retail start/goal-count/avoid-count/goals roles are S2/S3/S1/S6,
versus raw C's S8/S1/S0/S2; later reuse must be scoped, not globally substituted.
Require complete literal/intermediate/access-fault/FCSR boundaries, independent
original-assembly/GNU rebases, actual Make/padding/metadata/strict-first-image
and installed-state gates before replacing production and recounting.
The wider Game goal remains unfinished.
