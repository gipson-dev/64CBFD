# Game Third Resource Loader Exit Scheduling And Drop Removal

Date: 2026-10-11. Complete func_1503D774 in
conker/src/game/generated_6A3D0.c. VA 0x1503D774..0x1503D804,
ROM 0x6AC24..0x6ACB4: 36 words / 144-byte function and slot.
Install the qualified early failure assignment and shared success exit.
Raw C improves from 37 words / 7 differences to 36 / 2. Three normalizations
and one instruction drop become two final scheduling normalizations, no drop.
All 36 linked words remain exact; the entire rebuilt ELF is byte-identical.
This is further guard reduction, NOT a direct C match or new matching credit.
The full Game matching goal stays active.

## Baseline And Contract

Consumer 2e1ba4d9b7915b7c16040985439ea332230fb391 and mounted tools
5eb0c4a12506e2db2d6e8d684fcbddd33789dab6 were clean at entry.
[Note 1274](1274-game-third-resource-loader-incoming-result-lifetime-and-guard-reduction-20261011.md)
banked native cached-slot/request/pointer lifetimes. Query native Graphify and
inspect complete retail assembly, current compiler objects and caller source
before probing the remaining A0/status-to-V0 copy. Reuse existing IDO, MIPS,
native32, ELF/CSV parsers and both real padders. No new dependencies, compiler
profiles, recipes, global types or caller ABI changes. Zero Claude calls;
the source/profile measurements and independent-word diagnosis suffice.

Cache &D_800D1C90[identity]. An occupied slot returns zero without request or
header read. Otherwise request func_1502B6BC(&output, 2, NULL, 2, 0x11,
identity), preserving the full identity and ignoring the incoming second
argument and written output size. NULL clears the cached destination and
returns two. Success publishes the returned block pointer, reads its live
first word, then publishes that word to the same cached slot and returns zero.
Callbacks may change globals/header contents. First publication is observable
when the returned block aliases the destination or its neighbor. No new bounds,
NULL-header or size-output gates. Casts retain the existing 32-bit guest ABI;
no portable64 claim.

Retail frame 0x30, RA +0x1C, identity home +0x30, unused home +0x34,
output +0x2C, cached slot +0x24, result branch/reload and pointer lifetime all
emit natively. Failure uses return loaded = 2. Success clears loaded and
retains an explicit shared-exit goto/label. Removing that label changes IDO
allocation back to 37 / 14; retain the measured complete exit shape, not an
unqualified cosmetic rewrite. The goto emits no extra linked instruction.

## Two Remaining Words

Thirty-four of 36 retail words emit directly, versus 33 previously. The former
cached-exit adjustment, status-register corrections and redundant move/drop
are gone. The final header publication and V0 clear are independent, but IDO
schedules them in the opposite order to retail:

| Raw Offset | Expected Raw Word | Retail Replacement |
| --- | --- | --- |
| 0x078 | 0xAC6A0000, sw T2 to cached slot | 0x00001025, clear V0 |
| 0x07C | 0x00001025, clear V0 | 0xAC6A0000, sw T2 to cached slot |

Only this function's four-row guard block changes to these two rows. No
instruction drop or relocation change. Other guard bytes are unchanged,
including all 298 pre-existing CRLF lines; source remains LF-only. Git's
existing CRLF-to-LF normalization warning is not new whole-file churn.

Raw public semantics are qualified, not full private fault/register agreement:
at a missing final destination write, raw V0 can still hold the block address
where retail has already cleared it. Original/fitted fault-prefix agreement
is separately checked. Keep the two expected-word guards until direct scheduling
is recovered; do not describe the raw body as byte-exact.

## Diagnostics And Fresh Qualification

New tools: experiments/game_third_resource_loader_status_candidates.py and
tests/test_game_third_resource_loader_status_match.py. Ignored receipts and
immutable before-inputs live in
conker/build/game-third-resource-loader-status-match-test/.

The initial owner-only 51-shape screen and subsequent 24/18/22 filtered
two-profile measurements find no direct body. These are partial diagnostic
subsets, not a complete two-profile sweep of the final 83-shape generator.
The named cleared-failure-status negative is never qualified. Fresh test_11
independently measures these four complete shapes under both profiles:

| Source Shape | Raw Words | Differences, Owner / Retail |
| --- | ---: | ---: |
| Previous installed shared status | 37 | 7 / 7 |
| Early failure assignment, unused exit label | 36 | 2 / 2 |
| Explicit shared success exit, selected | 36 | 2 / 2 |
| Volatile-header diagnostic | 36 | 2 / 2 |

All eight have frame 0x30 and zero diagnostics/pool bytes. No pointer-parameter,
volatile or profile experiment is installed. Source alone is not direct.

- Fourteen pre-install tests pass in 57.501 seconds. Tighten predecessor
  corruption rejection and rerun both affected tests: two pass in 3.625 seconds.
  Candidate body/guard fingerprints are unchanged by that harness tightening.
- After the guard-triggered rebuild exits zero, the literal installed audit
  passes in 1.977 seconds. Final full affected regression selection: 151 tests
  in 641.990 seconds, all passing, no skips. This is the previous 137-test
  selection plus all fourteen new tests, not reused passing receipts.
- The 768-case identity/presence/result/header/unused/phase matrix reaches all
  36 retail words across original/raw/fitted forms. Invalid identities are
  mapped guest fixtures, not real-table bounds proof.
- Twenty-eight callback/alias cases, four independent links / 64 rebased
  cases and all 80 fired original/fitted private/public/request fault-prefix
  pairs pass. Guest fault ordering is not portable C fault semantics.
- Five freshly compiled semantic mutations fail effectively. Both guards
  reject expected-word and relocation corruption: four effective failures.
  Four source, three guard, two word/extent and two stale-install controls
  reject the exact historical successor; no historical baseline refresh.
- Both complete owner profiles compile with zero diagnostics. All 14
  neighbors, pools, relocations and extents remain exact. Both actual padders
  resolve all four before/after routes to the same 3,760-byte current owner;
  the existing D804 alternate-object selector remains unchanged.
- Native32 O2/O0 each pass 65,536 low-halfword payloads with fixed upper
  halfword 0xFFFF, 6,144 valid-native-fixture identity/unused/callback cases
  and four aliases. A status-two-to-four mutation fails. No exhaustive 32-bit
  payload, native invalid-identity, portable64 or hardware qualification.
- Actual seventeen-body parent chain: 1,920 cases / 3,840 executions,
  1,440 real success requests and 576 NULL/status-two failures, third hook
  removed. It reaches 34 loader words; focused tests reach all 36. Deeper
  request/lookup/allocator/free/heap/hardware/gameplay remain bounded.
- Fifteen SDK variadic tests are fresh within the 151-test run, including
  actual two-component lazy-loader C, SDK helper/relocator connections and
  fresh IDO slots. This does not establish live hardware/gameplay behavior.

Historical source/guard views reverse only the complete qualified body and
exact two-row block, checking full predecessor hashes, round-trip installation,
actual retail words and extent 144. Both older loader views remain exact.
Prior lifetime receipts now explicitly label these views; they do not call the
current source/guards literally unchanged. The new installed audit reads every
actual input literally, without projection, to prove the current delta.

```sh
python3 -m tools.experiments.game_third_resource_loader_status_candidates --profiles
python3 -m unittest tools.tests.test_game_third_resource_loader_status_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Existing warnings in unchanged modules and the duplicate generated_12D630
recipe remain. Do not call the complete rebuild warning-free.

## Literal Audit And Checkpoint

Source and guards are exactly the qualified successors. The seven other
assignment inputs (ELF, progress, rodata, symbol addresses, undefined functions,
layout and Makefile), every ELF byte/metadata/address/extent/body and all
189,088 protected data bytes / 720 owners remain unchanged. Data SHA-256:
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source after | 160574dbd03ec68f975472eb9d580e46dd7c3d40eda306955b2c8a9acd9373d4 |
| Guards after | 2c86d53acedfcb94ac1e3fcd03bab86a3b0854c6813f07dfb080f415b26255a7 |
| ELF unchanged | 9f2c45ce2994dafadbaa9bce9c640e61852b6f2ebf4d2a34a41d1d1438bbcb25 |

Fresh match-progress: Game 2,796/4,822 (57.98%), total 3,469/5,495 (63.13%),
Init 492/492 and Debugger 181/181. Zero drift, 2,026 still different.
Zero matching/conversion credit. Root README remains unchanged.

Consumer, mounted and older tools shared checks pass; all four mounted task
paths and two new older copies pass native py_compile. Commit tools
36adf10b4be3a9887b11b9d5ace57d9f64d4a2f2 before source/guards, this note,
five concise indexes and consumer gitlink. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 41 protected fingerprints
remain unchanged. Copy only two absent finalized files with identical hashes;
dirty count 318 -> 320. Existing older helper/test paths are not overwritten;
its history is not committed/reset/pushed. Full function regressions ran in
the mounted consumer, not the older standalone checkout. Active checkouts are
clean after banking. No push requested/performed; zero Claude calls.

Native graphify update . exits one on protective shrink refusal: 18,114
candidate nodes versus 39,895 saved, keeping 19,398 nodes from 2,972
excluded-but-existing files. No saved-graph overwrite, force, purge or install.
Version/empty-source warnings remain separate. After consumer commit, verify
fresh hook terminal completion from recorded log offset/bytes/UTC and zero
workers, not just the launch receipt.

## Next Game Body

Live linked checks find func_1503DA3C (24 words), func_1503DA9C (104) and
func_1503DC3C (56) already exact; do not double-count those neighbors.
The next unmatched body in address order is func_1503DE70, owner
generated_6B320: VA 0x1503DE70..0x1503DF0C, ROM 0x6B320..0x6B3BC,
39 words / 156 bytes, still a zero-return placeholder with 38 linked word
differences. Inspect its complete actor/group/entry interface: signed actor-slot
difference divided by 0x32C, entry-minus-one gate, D_8008446C mask pair or two
all-bit masks, then actual func_1503DF0C. The three current C call sites ignore
the result; recover the proper command signature and qualify the full body,
real helper and callers rather than another already-exact neighbor.

The two final third-loader scheduling guards, parent/pair guard elimination
and deeper SDK/allocator/heap/hardware/renderer/gameplay remain separate open
work. No OGL Release build/change, real save mutation, private-input rewrite
or active editor/debugger changes. Keep the full Game matching goal active.
