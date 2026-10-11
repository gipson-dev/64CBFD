# Record Index Query Direct Match And Census

Verified 2026-10-11. Consumer baseline
492b40444e2b0abd5d21f93d9ec2d3d040a19ea4; mounted tools baseline
71822b664ed9b10993bc6d86628445b1311a7df8. New tools
630eaf9708a09de4dcdb2f4729e227228b48ba47 committed first. No push.
Single Codex writer, zero Claude calls; DOCS/AGENT_WORKFLOW.md applies.
Previous goal turn banked the complete animation child cleanup. This finishes
another complete routine and fixes its omitted native census boundary;
the wider Game goal remains open.

## Recovery And Direct Match

Recover func_15083E0C, VA 0x15083E0C..0x15083E90,
ROM 0xB12BC..0xB1340, in conker/src/game/generated_AEB40.c.
Replace the 12-byte zero-return placeholder with s32 (u8 selector).
All 33 words / 132 bytes emit directly from C, no frame, four relocations,
no new guards, pools or compiler profiles. The first complete candidate
matches; returning the loop index instead emits 26 words/18 differences,
and using a word selector emits 29 words/32 differences. Do not abbreviate
the retail pointer-difference return to optimize compiler shape.

- Store the full incoming argument word at SP+0 before narrowing to its low
  unsigned byte, preserving private argument-home aliases.
- Zero selector returns -1 without reading either global. Read unsigned
  D_800D2100 once; zero count returns -1 without reading D_800D20FC.
- Positive count caches the record base pointer. Scan 48-byte records,
  identity byte at +0x28, from index zero. First duplicate match wins;
  there is no occupancy/active flag gate. Return signed pointer difference
  divided by 48; absent identity returns -1.
- Preserve original memory access order, full register lifetimes, loop
  update and return delay slot. All 33 retail words are dynamically reached.

Inspect retail call contexts in 49D30.s, C4DC0.s, 15BD90.s, 20AE20.s and
EC420.s, and C callers game_83300.c, init_EB00.c and generated_20AE20.c.
Explicit -1 checks and downstream index scaling establish a value-returning
query, not void or unconditional zero. The complete 47-word original retail
caller func_15097910 is exercised below. Its current consumer C body remains
unrecovered; this is not a linked/current-C-caller acceptance claim.

## Native Definition And Census Correction

Initial direct rebuild was exact, but matching totals did not change because
the target was absent from progress.csv and retail_layout.us.txt. The previous
func_15083DA0 row incorrectly spanned 240 bytes through 0x15083E90 instead
of its 108-byte body ending at 0x15083E0C. The ignored auto assignment also
overrode the C definition as SHN_ABS. Follow the already qualified local
precedent in Note 1233, not a new shared resolver or parser.

- Split only that retail-layout row into the 108-byte predecessor and the
  132-byte target. Preserve all other layout bytes.
- Append only func_15083E0C = 0x15083E0C; // type:func defined:true to tracked
  symbol_addrs.us.txt, retaining the complete previous byte prefix.
- Remove only the stale func_15083E0C assignment from the ignored local
  undefined_funcs_auto.txt. Do not commit generated auto files or progress.csv.
- Exercise the actual vendored Splat symbol parser and undefined writer:
  referenced defined target is excluded, unresolved canary is retained;
  changing only defined:true to false recreates the stale assignment.
  No full extraction, vendored edits or dependency changes.

The linked target changes SHN_ABS 0xFFF1 to section 5 (.game). The generated
census now includes one previously omitted physical C function, not a fresh
asm-to-C conversion. Total functions 6,043 -> 6,044 and C 5,494 -> 5,495;
Game functions 5,322 -> 5,323 and C 4,821 -> 4,822. The predecessor loses
132 census bytes and the target gains the same 132, so converted bytes do
not change. Still-different count remains 2,038 because the target was not
represented as a differing function before this correction.

## Fresh Qualification

Ten final tests pass after the wider rebuild, 29.942 seconds. Independent
receipts and immutable baseline hashes live under
conker/build/game-record-index-query-test/. Consumer make tools-check and
mounted standalone check_project_tools.py both pass under WSL. A native
Windows invocation fails with WinError 193 when launching a Linux tool;
this is not reported as a successful native-platform tools check.

- 11,544 independent-reference cases / 23,088 original/C guest runs: every
  selector/count byte, zero/one/two/128/255 boundaries, first/middle/last/
  no-match/duplicates, upper GP argument words, two stack phases and wrapped
  record pointers. Full memory, ordered accesses, return, GP/FPR agree.
  Wrapped pointers and private access behavior are guest-only claims.
- 22 alias/short-circuit cases / 44 runs and 584 fired full-access fault
  pairs: count/pointer/record fields alias SP+0, selector zero skips unmapped
  globals, count zero skips unmapped pointer, first match skips later unmapped
  record. Each gate fires; partial memory/accesses/GP/FPR agree.
- Three independent symbol sets / nine original/C/production-padded links,
  15 cases / 45 runs. Both global HI16/LO16 pairs cross signed low-half carry
  boundaries. Private alias fixtures actually relink their chosen globals.
- Actual copied-owner preprocessing, IDO compilation and asm post-processing
  preserve all 30 neighbors' full fingerprints, extents, relocations and
  normalized pools with zero owner diagnostics. Before-owner uses the saved
  old layout, after-owner uses corrected layout. Both production padding
  routes preserve all non-target bytes/relocations and guard fingerprints.
- Six effective freshly compiled semantic negatives: zero/-1 result,
  argument narrowing, identity offset/comparison, scan bound and signed count.
  The signed-byte negative uses existing local CopyOracle execution support,
  with no shared helper change. The bound fixture explicitly matches the first
  outside-count record. An additional native zero-return negative fails.
- Native32 O2/O0 each pass 5,120 cases, 10,240 total. Verify 48-byte records,
  32-bit pointers/integers, selector/count domains and complete record bytes/
  globals unchanged. Wrapped addresses/private guest faults are not portable
  native-C acceptance. No host gameplay claim.
- Complete 47-word retail func_15097910 connection: 144 cases / 288 runs,
  160 query calls per form. Independently check -1 sentinel, 0x2000 flags,
  zero index and requery after modeled initialization. Peer func_15083E90
  and func_15082A44 remain bounded callbacks. Assert this retail caller is
  not the current linked caller; its C body still needs recovery.
- Actual Splat parser/writer and missing-defined negative qualify durable
  symbol ownership. Census audit allows only the shortened preceding row
  and inserted target C row, not arbitrary conversion changes.

Initial test-fixture corrections: relink private alias symbols rather than
only changing oracle metadata; make the first outside-count identity match;
execute the signed-byte negative with existing local support; verify all
native record bytes, not just identity fields. Final receipts are fresh;
these fixture failures were not accepted as production qualification.
Historical neighboring suites are reused only after fresh complete fingerprint
equality, not reported as freshly rerun historical tests.

## Linked Audit And Progress

Only 102 ELF bytes change: target's 132-byte slot, ST_SIZE 12 -> 132 and
SHN_ABS -> .game section. Every other ELF byte and metadata field is exact.
ELF 3,261,160 bytes, SHA-256
9dd9031dfa18a3bc7f7adcd9c1ceb26315fc2b72f15a553ed1c73c2c7b9fc2c3.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner: 12,789 bytes, SHA-256
c46883beb4bbb819591e4ac8d8a875a873d4cab44be9b1f2efa80277605600c9.
Guards stay byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Generated census: 317,252 bytes, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
Rodata remains exact. Symbol/layout/generated-auto deltas are bounded above.

An initial forced narrow relink passes, then ordinary match-progress triggers
a wider rebuild because retail_layout.us.txt is a dependency. Let the original
build finish and rerun the whole ten-test qualification. Its linked ELF is
still exactly the bounded 102-byte delta. Existing duplicate generated_12D630
recipe warnings and legacy IDO diagnostics in unchanged owners persist;
successful build is not a warning-free-build claim.

Fresh matching: Game 2,784/4,822 (57.74%), total 3,457/5,495 (62.91%),
zero drift / 2,038 different. Converted total 5,495/6,044 (90.92%),
Game 4,822/5,323 (90.59%); converted bytes remain total 86.01%, Game 85.37%.
Init 492/492 and Debugger 181/181 already-converted functions remain exact.
README changes four aggregate rows only; function narratives stay in DOCS.

```sh
python3 -m tools.experiments.game_record_index_query_candidates
python3 -m unittest tools.tests.test_game_record_index_query -v
make -C conker match-progress NON_MATCHING=1
make tools-check
cd tools && python3 check_project_tools.py
```

Older standalone tools HEAD ddbdd16 stays unchanged: 273 existing dirty
entries plus two absent-only byte-identical new mirrors = 275. Protected
older helpers remain exact; no existing paths overwritten or committed.
Native Graphify query found 59 nodes, showed 25 and truncated 34. Native
update exits 1, refusing unsafe shrink 39,674 -> 17,892 and retaining
19,398 nodes from 2,972 excluded-but-existing files. Preserve version and
devcontainer.json zero-node warnings; no force, purge or install. Require
fresh post-commit log growth/Rebuilt tail and zero actual workers before
reporting clean. No OGL/Release, saves, editor or private inputs changed.

## Next

Recover complete 72-word func_15083E90 in the same owner,
VA 0x15083E90..0x15083FB0, ROM 0xB1340..0xB1460.
Completed in [Note 1253](1253-game-actor-identity-lookup-direct-match-20261011.md),
which corrects the original handoff bound to 26 slots, 0..25.
At this checkpoint the body returned NULL. Inspect caller contract and original full argument
home/byte selector, slot-zero special presence gate, D_800CC2D0 actor pool,
812-byte stride, identity +0x3B, slots 1..25 with peeled slot one and four-record unrolling,
presence-gated identity reads and first-active-match pointer/NULL result.
Preserve branch-likely prefetch/access order and completed neighbors/guards.
Broader timeline matching and real child/allocator/hardware/renderer/gameplay
acceptance remain separate open work; keep the wider Game goal active.
