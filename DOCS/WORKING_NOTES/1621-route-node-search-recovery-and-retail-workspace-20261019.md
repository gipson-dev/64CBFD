# Route Node Search Recovery And Retail Workspace

Date: 2026-10-19. Consumer predecessor: `92059061`; tools predecessor: `f48f2f9`.
Tools checkpoint: `e70e8dc`, committed before the consumer documentation/pin.

## Target And Steps

Continue **func_15086364**, VA `15086364..15086BD0`, ROM `B3814..B4080`,
**539 words/2,156 bytes, frame 1536 (0x600)**, from
[Note 1620](1620-actor-state-tick-complete-match-20261019.md). Production is still
its 12-byte zero-return C stub with 522 classified differences.

1. Read the complete retail body and callers; recover the real interface and
   widths, using donor C only as an untrusted reference. Completed.
2. Recover and behaviorally qualify the entire semantic routine; recover its
   frame, real workspace arrays and live float call-save from C. Completed
   within the bounded cases below, not a claim of exact instruction layout.
3. Finish the remaining extent/register/private-layout/access-order fitting,
   literal/independent assembly qualification and actual integration. Pending.

The three calls in the already recovered `func_15086098`, the C4DC0 caller and
the retained `func_15077508` call pass five integer/pointer arguments. Retail
narrows arguments 1/2 to signed bytes. The recovered interface is
`s32(s32 start, s8 goalCount, s8 avoidCount, u8 *goals, u8 *avoid)`.
Original symbols are retained, with semantic local names and one purpose
comment. No shared header, dummy local, volatile, physical-register binding,
assembly array, production guard or compiler-profile change is introduced.

## Complete Semantic Recovery

[Selected source and bounded candidates](../../tools/experiments/game_route_node_search_candidates.py)
recover the complete five-neighbor least-cost frontier walk, parent-path
reconstruction, special-node compression and accumulated helper distance.

The donor draft has material access-width and control-flow errors. Retail uses
unsigned-byte neighbor/goal IDs, signed-halfword XYZ coordinates and word costs,
not the draft's word neighbor reads, float coordinates or halfword cost array.
Only opening edge lengths are narrowed through s16 after float-to-word
truncation; later relaxations retain the full word. The returned waypoint and
public distance are distinct outputs from the selected goal byte.

Strict first-entry ties, duplicate neighbors, frontier holes, last-slot count
reduction and queue update versus append are retained. In the donor's append
test, the scan variable was reset before testing its XOR result; retail tests
the old scan result and resets the register in a branch delay. The reconstructed
source preserves the actual update/append distinction.

The initial complete source emits 548 words/frame 1544 on normal O2/g3, or
391/frame 1528 with the owner's existing no-unroll selection. Sixteen bounded
lifetime forms reuse the path counter as its later traversal index and the
current-node local as the later result, and recover the opening absent flag.
The selected lifetime form emits 546 words/frame 1536.

Twenty-four declaration partitions move only existing real declarations. The
selected partition retains these five contiguous workspace ranges:

| Role | Capacity | Retail And Selected SP Offset |
| --- | ---: | --- |
| Special flags | 64 bytes | 7C |
| Reversed path | 64 bytes | BC |
| Parents | 200 bytes | FC |
| Frontier | 200 bytes | 1C4 |
| Costs | 200 words | 28C |

Reusing two dead pointer locals for the opening cost-fill cursor/end produces
545 words/frame 1536. Explicit helper-loop pointers and cached path-argument
controls produce longer bodies and are not selected. Exchanging the existing
word-sized `proposed` and `distance` declarations also moves the live F2 save
from SP+74 to retail SP+5D0 without moving arrays or changing the frame.

**Selected normal output is still non-matching: 545 words, six over retail,
with 488 aligned word differences.** The selected no-unroll output is
388 words/frame 1520. Both are complete semantic bodies; their distinct shapes
must not be conflated. Actual per-function Make selection remains a future
installation gate; no production flags were edited.

## Fresh Qualification

[Seven tests](../../tools/tests/test_game_route_node_search_candidates.py)
pass with zero skips/errors/failures in **20.557s primary / 19.711s mirror**.
Each copy compiles and qualifies the final selected source independently.

- An [independent frontier/path reference](../../tools/tests/game_route_node_search_oracle.py)
  and retail, rolled C and normal C agree across **426 fixture/stack-phase
  runs**: returns, helper arguments/order, ordered public stores and complete
  public memory. The guest runner checks restored saved GPR/FPR state and
  clobbers caller-saved registers/FPRs across opaque helpers.
- The 213-case corpus includes signed-byte count truncation/high input bits,
  invalid starts/counts, duplicate goals/neighbors, strict ties, avoided nodes,
  disconnected/random graphs, negative opening-edge narrowing, signed XYZ
  extremes, node ID 199, paths through 63 nodes, all 64 special-flag masks and
  fractional/negative helper distances. Public goal/global aliases preserve
  the two opening stores. Requested helper mutations are required to fire.
- **Six effective live-home alias pairs** mutate the reversed path, special
  flags or live F2 save in both stack phases. Retail and selected normal C
  agree after the mutations, and ordinary behavior differs as required.
  **Two completed old-distance-home negatives** retain the SP+74 save and
  demonstrably reject the SP+5D0 mutation after it fires.
- All 213 native32 fixtures pass **O0/O2/O3 with trap-mode UBSan**. Three
  separately compiled semantic negatives reject losing the opening s16
  narrowing, changing strict ties to last-entry ties, and signed goal IDs.
  A separate signed-overflow control fires SIGILL -4.
- Both complete-owner profiles preserve **all 72 other bodies and normalized
  pools**. Isolated and complete-owner target words/bindings agree; the typed
  forward declaration does not change the recovered caller. All seven pinned
  production inputs remain byte-identical.
- Both project-tools checks pass, all six copied Python files parse, and the
  three new task files are byte-identical between the tools copies.

Fixtures visit **538/539 retail words**; offset **0x7C8** is unvisited. The
qualified domain has at most 200 node records, 64 path entries and 127 elements
per signed-byte list. Deliberate frame aliases are guest compiler-layout probes,
not portable C helper contracts; they are excluded from native cases.

The inherited guest core initially lacked sqrt.s and XOR. The new local runner
adds those instructions with direct unit checks; it does not modify shared
oracles. An oversized normal candidate also overlapped helper `15086BD0` at
its retail address. Raw C is therefore run at disjoint `18000000`, with same
JAL region, unchanged PC-relative branches and checked absence of absolute
internal jumps. Retail remains at its real entry. Final complete tests use
this corrected harness; no source behavior or acceptance gate was removed.

These are bounded public/ABI/home-alias receipts, **not** literal whole-machine
equivalence, ordered-read/fault-prefix/FCSR/hardware coverage, independently
assembled/rebased acceptance, full helper-chain or gameplay qualification.

## Preservation And Resume

Tools are committed first. Only the three absent new task files are copied
into the independent mirror; later updates are confined to those owned files.
Mirror HEAD `ddbdd16b` and all **1,448 older dirty leaf hashes/statuses** remain
intact; final dirty paths 1,451. No mirror commit/reset/stash/clean, push,
host/frozen Release, save, dependency installation or advisory-agent call.

Production C, original assembly, guard CSV, Makefile, ELF, progress CSV and
root README remain unchanged. Installed totals are the verified Note 1620
baseline, not new matching credit: Game **3,018/4,832**, overall
**3,691/5,505**, 1,814 different/zero drift; owner **70/73 exact**.

```text
Selected normal raw:
76c2344e05cad317bd98cd766b95a2d6d6b43fc1e9970c0bf80bce195224d27f
```

Ignored receipts: `conker/build/game-route-node-search/`, with separate mirror
tests, the initial/lifetime/workspace/pointer/tail screens, native and complete
owner outputs, production snapshots, mirror preservation chunks and graph
baseline/audit. The consumer commit hook refreshes Graphify; preserve and
audit the excluded-but-existing historical nodes rather than purging them.

Next: continue **this same function**, not another owner batch. Recover the
six excess words, remaining scalar/private homes, saved-register lifetimes and
access schedule while retaining the exact arrays and F2 home. Then qualify
complete origins/literal state, missing instruction/access-cut and independent
GNU original-assembly cases, actual Make/padding/strict first image and
installed state before installation/recount. The wider Game work is unfinished.
