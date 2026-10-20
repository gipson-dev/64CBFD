# Route-Search Capture Closure And Start-Home Boundary

Date: 2026-10-19. Consumer predecessor: `08a8cde5`; tools predecessor:
`6c7b058`. Tools changes are banked first as `a2d506c` (capture source/layout
qualification) and `5830074` (remaining start-home regression probe).

## Scope And Result

Continue complete **func_15086364**, VA `15086364..15086BD0`, ROM
`B3814..B4080`, retail **539 words/frame 1536**, from
[Note 1622](1622-route-search-sentinel-and-capture-boundaries-20261019.md).

The [new experiment](../../tools/experiments/game_route_node_search_captures.py)
closes the four previously failing table/avoid-pointer alias probes. The avoid
reloads now emit directly from semantic C. The table-home correction is an
explicitly post-compile, five-displacement mapping, not a compiler-only match.
The complete normal candidate remains **535 words/frame 1536**, with **492
counted differences: 488 linked overlap differences plus four missing words**.
It is **not byte-exact, not installed, and earns no matching credit**.

## Incoming Avoid Pointer

The selected source changes the two indexed avoid scans from `avoid[i]` to
`(*(u8 **)&avoid)[i]`. This keeps the correctly typed incoming pointer lvalue
addressable under the prepared IDO compiler. It emits the four actual incoming
SP+10 / frame SP+610 pointer reloads, rather than retaining the old capture.
Plain `(*(&avoid))[i]` folds away and does not close the failing probe.

This is a real typed pointer access, not volatile, dummy storage, a physical
register binding or a compiler-profile change. All five established array
homes SP+7C/BC/FC/1C4/28C and the live F2 save SP+5D0 remain intact. The selected
normal raw source is 535 words; the separately checked no-unroll source is
379 words/frame 1520 and is not the selected mapping input.

## Cached Table Home

The complete C still places the cached table at SP+5FC, not retail SP+60.
The pure normalizer changes exactly these five source-origin displacements:

| Raw Word Index | Expected Raw Word | Change |
| --- | --- | --- |
| 99 | AFB805FC | table SW: SP+5FC to SP+60 |
| 149 | 8FB805FC | table LW: SP+5FC to SP+60 |
| 323 | 8FAF05FC | table LW: SP+5FC to SP+60 |
| 355 | 8FAE05FC | table LW: SP+5FC to SP+60 |
| 377 | 8FAE05FC | table LW: SP+5FC to SP+60 |

Full raw/binding fingerprints, exact expected words, an unused destination
home and absence of relocation bindings at those fields are mandatory. The
output fingerprint is checked too. **All 535 instruction origins and all 14
relocation entries are retained unchanged in number and order**. No instruction
is inserted or omitted; no opcode, register, branch, delay or public-memory
instruction is changed by this mapping. The pure normalizer does not read ROM
or other files; its test rejects any attempted file read.

The object fixture uses the parsed function's actual ELF section and modifies
only those five words in the original object. All other bytes, including raw
symbol/debug/section metadata, remain identical. This preserves metadata; it
does not repair source-debug location metadata for the mapped home. Both full
owner profiles preserve 72 other bodies/pools. The normalized whole-owner
target payload equals the isolated normalized payload.

An initial scratch GNU-objcopy route changed parsed section indices/bindings
and was rejected. The original-object structured patch replaced that route;
no verifier or metadata allowance was weakened.

## Fresh Qualification

[Ten tests](../../tools/tests/test_game_route_node_search_captures.py) pass in
both copies, with zero skips/errors/failures: **32.825s primary / 31.836s
mirror**. These final runs include the added start/cost follow-up test.

- All **426 guest fixture/stack-phase runs** agree with the independent
  reference for returns, helper calls/arguments, ordered public stores and
  complete public memory, across retail, rolled C and normalized normal C.
- All **213 native32 fixtures** pass at O0/O2/O3 with trap-mode UBSan. Five
  compiled semantic negatives remain effective, and the independent overflow
  control still fires SIGILL -4.
- All **213 public read footprints** agree as address/width/value multisets.
  Their order still differs; this is not ordered-access equivalence.
- The **six established live-home aliases** and **two old-F2-home negatives**
  remain effective in both stack phases.
- **Four newly closed capture aliases** mutate the cached table or incoming
  avoid pointer after the second executed public GOALS-byte read. Every gate
  and requested store must fire. Each changes retail relative to baseline;
  the normalized candidate now agrees with that changed public signature.
- **Four effective old-capture controls** reject the predecessor: raw new C
  retains the baseline table route, whereas the normalized table agrees with
  retail; the old loop C retains the baseline avoid route, whereas typed raw
  C already agrees with retail. These distinguish the two fix mechanisms.
- All **535 raw-word** and **14 relocation-binding** mutations reject stale
  normalization. All four new Python copies parse; the two task files are
  byte-identical between checkouts; both project-tools checks pass.
- Both owner profiles preserve 72 other bodies and normalized pools, with
  isolated/whole-owner raw words and bindings equal. All seven production
  input fingerprints still match; no installed image was rebuilt or changed.

Coverage remains **538/539 retail words**, with offset **0x7C8** unvisited.
The guest's provider/frame mutations are compiler-layout probes, not portable
C contracts. Full literal private/register state, instruction/access-fault
prefixes, FCSR/hardware, connected helper/caller chains, independent original-
assembly rebases, actual Make/padding/strict-image and installed-state gates
remain open. The raw guest code map stays disjoint at 18000000.

## Next Demonstrated Boundary

A follow-up test uses the same second executed GOALS-byte-read gate, with
both stack phases and a required mutation receipt:

| Probe | Mutated Home / Value | Retail | Normalized Candidate | Result |
| --- | --- | --- | --- | --- |
| Incoming start | frame SP+600 / 1 | waypoint 3 | waypoint 1 | Open |
| Selected cost | frame SP+290 / 1000000 | waypoint 2 | waypoint 2 | Closed |

The start mutation changes retail's public signature, while the candidate
retains baseline. The cost mutation changes both from baseline and their full
public signatures agree. Thus **two selected-cost samples are closed and two
incoming-start samples remain demonstrably open**. Do not invent a missing
selected-cost reload or pad the four-word deficit to conceal the start issue.

Typed start-home source screens currently emit 545 words and/or shift the
frame to 1544, with premature incoming-home stores. Table-address/local-scope
and pointer-carrier screens likewise move accepted homes or lose layout; none
is selected. A possible next source experiment is an early real start capture
with late incoming-home reuse after the initial guards. This is a hypothesis,
not a recovered lifetime or an acceptance result.

## Preservation And Checkpoints

All **1,453 older dirty mirror leaf hashes/statuses** and mirror HEAD
`ddbdd16b` are preserved. Only the two previously absent task files are added,
for **1,455 final dirty paths**; the follow-up modifies only this turn's new
test file. No mirror commit/reset/stash/clean, push, host/frozen Release,
save/config, compiler/dependency or advisory changes.

Production C, assembly, manifest, ELF, Makefile, progress CSV and root README
remain unchanged. Installed totals stay **Game 3,018/4,832**, **overall
3,691/5,505**, 1,814 different/zero drift; owner **70/73 exact**. The production
target remains its 12-byte zero-return C stub, with 522 classified differences.

```text
Normal raw: c9cc61e01da4a0bf630aa5ff8a88a5f4b3c3a4a1709e2fd8142a56110fd5b9b7
Bindings:   d773bb14cc8b0e5c4f019c38b74b90010d7d46e5cc0dd2786ab3dd0e2e6d2161
Normalized: 9a685456fec70e6faf985bb68efd18af68f2112b5500bdf6d981027048e2612e
Semantic C: fe18ad7f5939c490f2389da778d33ebdacf529e0f0fbee2b6f6298cdbd5258d2
```

Ignored receipts: `conker/build/game-route-node-search/loop/captures/qualified/`.
Final primary/mirror test summaries and logs, test-receipt JSON, fired capture
and start/cost probes, isolated and owner objects, fingerprints, unchanged
production snapshots, mirror preservation chunks and graph baseline/audit are
kept there. The consumer commit hook refreshes Graphify; audit that all older
nodes are retained or uniquely relocated, including 19,398 excluded-but-existing
nodes from 2,972 files. Do not purge the wider historical graph.

Continue **this function**, first the start-home SP+600 lifetime and guarded
stores/reloads, then remaining roles/read order and the four missing words.
Install and recount only after the complete literal/integration gates pass.
The wider Game goal remains unfinished.
