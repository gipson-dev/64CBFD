# Movement Physics Call Register Roles

Verified 2026-10-18. Consumer predecessor `46d8adf3`, tools predecessor
`12befaa`; both active repositories began clean. The wider Game goal remains
active. Continue complete `func_150F34F4` from
[Note1524](1524-movement-coefficient-read-store-schedule-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

This is a **private normalization qualification, not a C-emission gain**.
The selected complete C and raw object remain unchanged at 134 differences.
Fifteen new research guards reduce normalized differences **103 to 88**,
and extend the literal opening **478 to 633 words**. No production guards,
installation, inserted/omitted words or matching credit.
The production function remains its pre-existing zero-return placeholder;
the complete C discussed here is the isolated, non-installable candidate.

| Measurement | Raw C | Previous 31 Rows | Private 46 Rows |
| --- | ---: | ---: | ---: |
| Complete words | 959 | 959 | 959 |
| Frame | 128 | 128 | 128 |
| Different words | 134 | 103 | 88 |
| Exact opening words | 361 | 478 | 633 |
| First unequal PC | `0x150F3A98` | `0x150F3C6C` | `0x150F3ED8` |

## Bounded Proof

`tools/experiments/game_actor_input_movement_physics_call_roles.py` protects
317 predecessor entries / 293 distinct paths. Its ignored run directory is
`conker/build/game-actor-input-movement-physics-call-roles/`. It reuses the
selected `dataflow-423` source and existing padder, relocation parser, CFG
scanner and original measurement helper; it does not regenerate the project.

The 149-word region is words478..626 inclusive, PC
`0x150F3C6C..0x150F3EBC`, through the call to `func_15059140` at `0x150F3EB8`
and its `SB` delay slot. Source-to-retail temporary roles:

```text
13 -> 10, 14 -> 15, 25 -> 13, 10 -> 24,
15 -> 25, 24 -> 11, 3 -> 12
```

This map is injective but **not closed**. The continuation proof checks all
nine physical registers on both sides: 3,10,11,12,13,14,15,24,25. There is no
mapped target/identity collision, incoming interior entry or computed entry.
Forward branches and likely-slot annulment are modeled; targets cannot enter
delay slots or leave the region. All source-role reads follow definitions.
The local scan has 127 states; the continuation has 1,457. Later calls are
not counted as definitions to excuse live-out reads.

Four unreachable duplicate words, 543/567/598/615, are retained and checked
literally, not claimed as executed coverage. The initial all-words-visited
assumption was rejected by the CFG scan. All 149 transformed instructions
equal actual retail, including these duplicates. Only fifteen GPR fields
change, at indices478/480/483/494/516/519/572/576/578/580/581/582/584/587/626.
FP fields, opcodes, addresses, immediates and instruction count are retained.

All eighteen region relocation bindings are locked. The call remains
`R_MIPS_26:func_15059140`; the changed delay slot retains
`R_MIPS_LO16:D_800CBDD3` and its addend. The actual guarded padder/link matches
the derived words. The previous 31-row table is an exact byte prefix of the
46-row research table. All 46 rows change 57 target bytes, retaining complete
relocation metadata, eleven padded neighbors and owner pools.

| Artifact | SHA256 |
| --- | --- |
| Raw target | `4a4c3574716a6ab788981a28d6af57e8bd46c6c01d6a92aed2c100edfc38b5a7` |
| Private normalized target | `8b603db223015c85cc6a955d1791a0518e52f292094f71011b8242f91e62b69c` |
| Unchanged isolated source | `0b89776bd3c14abb3f18407fb0f45af318c1803add086c3b60960fdce1b52980` |

## Qualification Record

The final complete suite passes **eighteen tests in 213.375 seconds**. The
initial test harness omitted the previous 28-row comparison image needed by
two inherited heading tests; that fixture is restored without changing any
predecessor. A later fixed-access-count assumption for the old frontier was
also rejected: branch paths have different access counts. The final test
measures each old first-failing prefix instead of using their average.
A direct core-helper import avoids the existing deep import
chain's recursion limit, without changing Python's global limit or tools.

- **89 effective static controls** reject all fifteen changed words, missing
  and wrong bindings at all eighteen sites, invalid/colliding/incomplete maps,
  frame/extent/target changes, incoming/computed/backward/escaping/delay-slot
  control, all seven source live-ins, all nine physical live-outs, non-GPR/FP
  changes, both region boundaries and a changed rewrite-site table.
- **576 poisoned kernel cases** cover two actor bases, two controller
  locations, eight held/flag/button/Y/velocity/depth scenarios, two stack
  phases, three GPR/FPR seeds and provider modes 0/2/8. The 384 mutation cases
  confirm both the fired hook and an actual RAM change. The kernel visits
  129 words; the separate static/literal proof checks all 149 words.
- At the call boundary, the normalized full state equals actual retail.
  The old 31-row candidate's defined roles correspond under the map, with
  all non-affected identity GPRs checked **before** callee clobber. Complete
  post-call RAM/GPR/FPR/events/LO/condition equality is also checked. The
  delay-slot global byte is observed as one, and the actor argument is exact.
- The complete retail/raw/normalized public corpus reruns: 2,496 cases,
  twenty modeled FP edges, nine mutation modes, actual curve, 947 reachable
  words and twelve retained unreachable duplicates. Existing cap, release,
  speed/controller aliases, signed-Y, clamp, counter and surface checks pass.
- Native32 O2/O0 UBSan reruns 397 cases/profile and eight controls, two actual
  normalized-object rebases/twelve cases and twelve established guest aliases.
  The prior 640 coefficient cases / 320 old-C rejections also rerun.
- Both actual stale-word/unexpected-relocation padder controls pass at the
  new delay-slot row. All 317 protected entries, 6,057 installed bodies,
  189,088 Game-data bytes / 720 owners, callback slot and ten immutable
  first-image members remain unchanged.

Measured active private frontier advances from `0x150F3C88` to
`0x150F3EE0`: 100 states / 8,844 equal access-fault prefixes, with RAM/FPRs
equal at the first difference and only GPR11/14 different. Eighty disabled
states / 2,700 prefixes and 160 mode-zero states / 8,320 prefixes remain
complete. All hundred old-image controls are rejected at their measured
earlier frontier, with 6,700 equal old prefixes; no fixed average cut is used.

The unchanged completed compiler capture is explicitly reused, not recaptured:
source/normal/observed/fresh object identity is required. The 32 prior source
screens are reused, not recompiled or reported as fresh. Zero Claude calls
are needed for this bounded qualification. The reused capture retains 74
emitter events / 687 AS1 records and 52 prior layout controls; five pitch-site
controls rerun freshly. Frontend 92, optimizer 76, rounded 80, frame 128 and all
homes remain unchanged. Full private-register, arbitrary
unpassed provider-register, FCSR, caller-stack, native alias, hardware and
gameplay acceptance remain separate and unclaimed.

## Checkpoint And Continuation

Tools **d5406cd** is committed first. Both tools copies pass twelve shared
tests and smoke checks, with four ASCII/AST parses and two byte-identical
task pairs. The standalone shared checks use the documented `unittest
discover -s tests` form; direct `tests.*` module names resolve to a foreign
namespace there and were rejected without changing the environment.

The two mirror destinations were absent before copying. All **1,174** prior
hashes and HEAD `ddbdd16b` survive; the mirror now has **1,176** dirty paths.
No duplicate mirror commit, reset/clean, push, dependency update, host-port
change or frozen Release action. Main README stays unchanged.

Production ELF remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total **3,638 / 5,501
(66.13%)**, 1,863 different, zero drift; Init 492/492 and Debugger 181/181 among
converted functions. No production build is claimed or needed.

```sh
python3 -m tools.experiments.game_actor_input_movement_physics_call_roles
python3 -m tools.tests.test_game_actor_input_movement_physics_call_roles -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Derive fifteen register-field changes with complete local/continuation
  dataflow, literal duplicate, call-slot and relocation checks.
- [x] Pass 89 effective controls, 576 poisoned call cases / 384 mutations,
  measured old/new prefixes and the complete eighteen-test suite.
- [x] Bank the tools checkpoint first, then consumer documentation and pin.
- [ ] Continue the same function at word633 / `0x150F3ED8`: 86 GPR-field-only
  differences and the two independent address ADDIU words at `0x150F4098/9C`.
- [ ] Keep complete matching/private/caller/provider/first-image gates, the
  gate, both fade lifetime gaps, runtime acceptance and wider Game goal open.

The scoped AST graph refresh completes with **42,344 nodes / 82,465 links /
3,949 communities**. The new note is indexed. Only three shifted UPDATE_LOG
heading IDs disappear, with all three labels retained at new locations; no
unrelated nodes are lost. All 19,398 existing excluded nodes from 2,972
still-present files are preserved without a purge or full re-extraction.
The two new tools modules have no nodes in this consumer graph; this receipt
does not claim they were newly indexed or change the graph's scan settings.
