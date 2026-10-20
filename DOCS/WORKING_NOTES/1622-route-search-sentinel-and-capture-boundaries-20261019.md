# Route-Search Sentinel And Capture Boundaries

Date: 2026-10-19. Consumer predecessor: `afc5fde4`; tools predecessor: `e70e8dc`.
Tools checkpoint: `6c7b058`, committed before the consumer documentation/pin.

## Direct C Recovery

Continue complete **func_15086364**, VA `15086364..15086BD0`, ROM
`B3814..B4080`, retail **539 words/frame 1536**, from
[Note 1621](1621-route-node-search-recovery-and-retail-workspace-20261019.md).

The [new selected source](../../tools/experiments/game_route_node_search_loop.py)
recovers the actual outer-loop control: a do/while with the selection variable
also carrying the relaxation frontier scan counter. Finding a goal sets its
0xFF stop sentinel. A relaxation resets it to zero after testing the old scan
result for update versus append. The predecessor's unconditional loop and two
breaks were semantically correct for ordinary public behavior but produced a
different control/data-flow graph and ten more instructions.

Three meaningful scoped s32 locals capture signed-halfword origin X/Y/Z before
the relaxation's avoid scan, as in retail. Integer subtraction still precedes
float32 conversion; no float-coordinate reinterpretation, volatile, physical
register binding, dummy storage, guard, shared header or compiler change.

The selected normal O2/g3 body is **535 words/frame 1536**, four words short,
with **483 counted word differences: 479 linked overlap differences plus four
missing words**. It retains all fourteen relocation entries, array homes
SP+7C/BC/FC/1C4/28C and live F2 save SP+5D0. This is **not a byte match**.
The selected no-unroll profile is separately **379 words/frame 1520**; it must
not be reported as the normal candidate or silently selected for installation.

Source is `game_route_node_search_loop.SELECTED`, not the older candidate
module's SELECTED or this module's intermediate SENTINEL body. The latter is
535 words too, but lacks the early coordinate captures and has 492 differences.

## Fresh Qualification

[Eight tests](../../tools/tests/test_game_route_node_search_loop.py) pass with
zero skips/errors/failures: **33.311s primary / 33.183s mirror**. Both copies
separately compile and qualify the final selected complete source.

- All **426 fixture/stack-phase runs** retain the independent reference's
  return, helper calls/arguments, ordered public stores and complete public
  memory. Both rolled and normal complete C run with original retail code.
  Saved GPR/FPR restoration and hostile caller-saved clobbers remain checked.
- All **213 native32 fixtures** pass O0/O2/O3 with trap-mode UBSan. The three
  existing compiled semantic negatives remain effective. Two new compiled
  controls reject an inverted outer-loop sentinel and the donor-style lost
  frontier append. The separate overflow control still fires SIGILL -4.
- **Six effective live-home alias pairs** retain the path, flags and F2 save
  in both stack phases. **Two old-distance-home negatives** reject the wrong
  SP+74 save after their requested mutations fire.
- All **213 public read footprints** agree as multisets of address, width and
  value. Their order does not yet agree. In the default fixture both have 79
  public reads; the first difference is initial neighbor-X versus origin-X
  load scheduling. The test explicitly retains this open order boundary.
- Both complete owner profiles preserve **72 other bodies and normalized
  pools**, and isolated/whole-owner words and bindings agree. All seven
  production pins remain exact; no integration or matching credit is taken.
- Both project-tools checks pass. All four new Python copies parse, and the
  two new task files are byte-identical between the copies.

Coverage stays **538/539 retail words**, with offset **0x7C8** unvisited. These
bounded models do not prove literal whole-machine state, full instruction,
fault-prefix/FCSR/hardware, connected helper-chain or gameplay acceptance.
Deliberate frame mutations remain compiler-layout probes, not portable C
contracts. Raw C keeps the prepared disjoint 18000000 guest code map; no
absolute internal jumps are silently rebased or allowed.

## Demonstrated Capture Boundaries

Four additional probes, two kinds in both stack phases, establish specific
unfinished behavior. They fire immediately after the **second executed public
goal-byte read**, once initial neighbors and the table capture exist. No
observer/provider reads are used to satisfy that gate.

| Probe | Mutated Home | Retail Result | Selected C Result |
| --- | --- | --- | --- |
| Cached node table | frame SP+60 | Uses the altered table and route | Keeps baseline route |
| Avoid-list pointer | incoming SP+10, frame SP+610 | Reloads altered list and changes route | Keeps baseline capture |

Both mutations are required to fire and be recorded. Each changes retail's
observable calls relative to its own baseline; the selected source still
matches that baseline and differs from mutated retail. These are expected
open-boundary assertions, **not successful equivalence tests**.

The source's table capture is stored at **SP+5FC**, not retail SP+60. Its avoid
pointer is retained across regions where retail reloads the incoming home.
The static opcode census also differs: five fewer LW and two additional LB,
with changed branches/moves. Thus the four-word length deficit is not four
independent NOPs or permission to pad over real lifetime differences.

## Controls And Preservation

The source screens retain shared versus separate scan signals, do/forever,
coordinate reuse, pointer cursors, copied goal bounds, scopes and an initial-X
capture. Explicit pointer cursors produce 541/547-word alternatives. Copying
the goal bound loses the retail unroll and produces 506-512 words. A node scope
moves its table home to SP+74/78, not 60. An initial-X local grows the frame to
1544 without closing the initial read-order gap. None is selected as a match.
The first copied-bound draft placed a declaration after statements; moving the
declaration to its C89 block opening fixed that scratch-only syntax error.

Only the two absent new files are copied into the independent mirror. Its
HEAD `ddbdd16b` and all **1,451 older dirty leaf hashes/statuses** are preserved;
final dirty paths **1,453**. No older task file is rewritten. No mirror commit,
reset/stash/clean, push, host/frozen Release, save, dependency or advisory call.

Production C, assembly, manifest, ELF, Makefile, progress CSV and root README
are unchanged. Installed baseline remains **Game 3,018/4,832**, **overall
3,691/5,505**, 1,814 different/zero drift; owner **70/73 exact**, no new credit.

```text
Normal raw: 1afc816d05f80feb62d85d47c0aa69bc6c0bfbadd49377851b170b211e129443
Bindings:   77b0f5dc8c18f87ecbcb8fef9fadf18fc2c95cb226d56270bcf570a941f09a11
Semantic C: 98236ba7646cca9c7367ff47df314b3ce5f679fafe24327001a20ef229e0bf10
```

Ignored receipts: `conker/build/game-route-node-search/loop/`, with final
primary/mirror tests, separate owner/native builds, read-order and open-capture
JSON, selected fingerprints, scratch candidate/control sources, production
snapshots, mirror preservation chunks and graph baseline/audit. The consumer
commit hook refreshes Graphify; retain and audit excluded-but-existing nodes.

## Next Action

Continue **this function** from the new SELECTED source. Recover table home
SP+60 and avoid-pointer reload lifetimes while preserving all six accepted
homes, then require the four capture probes to demonstrate closure rather than
expected divergence. Finish scalar/register/access scheduling and the four
missing words without padding over those failures. Only after literal/private,
access-cut, independent GNU original-assembly, actual Make/padding/strict image
and installed-state gates pass should production be replaced and recounted.
The wider Game goal is unfinished.
