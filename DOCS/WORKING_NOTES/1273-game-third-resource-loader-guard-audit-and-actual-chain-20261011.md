# Game Third Resource Loader Guard Audit And Actual Chain

Date: 2026-10-11. Complete func_1503D774, owner
conker/src/game/generated_6A3D0.c. VA 0x1503D774..0x1503D804,
ROM 0x6AC24..0x6ACB4: 36 words / 144-byte function and slot.
The existing guarded body remains byte-exact. This checkpoint adds audit,
diagnostics and real parent-chain qualification, not a direct C match.
No production source, ELF, guards, profile, recipe or matching credit changes.
The wider Game goal stays active; guard elimination remains open.

## Baseline And Contract

Consumer ac54b4a2b7cb1c99e5244391296b9bddb95ca303 and mounted tools
663f63b706836e8064be619136042acd5965c165 were clean at entry.
[Note 1272](1272-game-record-resource-cleanup-direct-match-20261011.md)
banked the direct 43-word cleanup and actual sixteen-body parent chain.
Native Graphify query, complete retail assembly and the direct caller were
inspected before probing this already-exact loader. No Claude calls.

Cache &D_800D1C90[identity]. An occupied slot returns zero without a request
or header read. Otherwise request (&output, 2, NULL, 2, 0x11, identity) from
func_1502B6BC, preserving the full incoming identity and ignoring arg1 and
the written output size. NULL clears the cached destination and returns two.
Success publishes the returned block pointer, reads its first word, then
publishes that word to the same cached slot and returns zero. This order is
observable when the returned block aliases the destination or its neighbor.
No new identity bounds, NULL-header gate or size-output gate is justified.

Retail frame is 0x30: RA +0x1C, incoming identity +0x30, unused argument
+0x34, output +0x2C and cached slot +0x24. The request clobbers caller-saved
registers. Raw C instead spills the slot at +0x20 and copies returned V0
into A0; raw private-stack/register equivalence is not claimed.

## Direct Match Diagnostics

The existing raw body emits 37 words with 15 differences. Six expected-word
normalizations and one instruction drop retain the exact linked 36 words:
offsets 0x38, 0x50, 0x5C, 0x60, 0x64 (drop), 0x74 and 0x78. These preserve
the branch target, cached-slot spill/reload, result branch/delay scheduling
and returned-pointer lifetime. All seven original rows remain unchanged.

Fresh focused measurements under the owner profile, all frame 0x30 and
zero diagnostics/pools:

| Source Shape | Raw Words | Differences |
| --- | ---: | ---: |
| Banked | 37 | 15 |
| Success first | 36 | 10 |
| Publish request expression | 36 | 8 |
| Labelled success/shared argument status | 37 | 9 |
| Outer NULL slot condition | 33 | 22 |

None is selected for installation. Fewer differences do not prove equivalent
access order or private scheduling. The publication expression and explicitly
named inverted-result negative control are diagnostic shapes, not acceptance.
Earlier filtered declaration/type/status/control-flow probes also did not
match; their partial receipts are not represented as a complete final sweep.
The final banked-family/two-profile CLI sweep completes eight measurements:
banked/register-slot/integer-loaded each 37/15 under owner and retail; goto
34/22 under both. No profile or padding workaround is installed.

## Fresh Qualification

New tools: experiments/game_third_resource_loader_candidates.py and
tests/test_game_third_resource_loader_match.py. Reuse existing IDO, MIPS and
native32 oracles, structured ELF/CSV parsers and both real padders. Ignored
receipts live under conker/build/game-third-resource-loader-match-test/.

- Twelve new tests pass in 54.497 seconds. Original and fitted forms are
  exactly 36 words with extent 144. Raw public semantic equivalence only.
- The 768-case identity/presence/result/header/unused/phase matrix passes
  across original/raw/fitted forms and reaches all 36 retail instructions.
  Invalid identities are mapped guest fixtures, not real-table bounds proof.
- Twenty-eight callback/alias cases preserve cached destinations, live
  returned headers and first publication before an aliased header read.
- Four independent links pass 64 rebased cases with global HI/LO carries
  and request JAL relocation. Original/fitted words remain equal.
- All 80 original/fitted private/public/request fault-prefix pairs fire and
  preserve partial memory, events, calls and registers. Not portable C faults.
- Five fresh semantic mutations fail effectively. All seven guard rows reject
  both expected-word and expected-relocation corruption: fourteen rejections.
  The isolated padder gets only these seven rows, not unrelated owner guards.
- Both full owner profiles compile without diagnostics. Both actual padders
  retain the existing D804 object selector, all 15 extents and 14 neighbors.
  Independently resolve the complete 3,760-byte owner from actual ELF symbol
  values; both routes equal each other and the complete current linked bytes.
- Native32 O2/O0 each pass 65,536 low-halfword first-word payloads with fixed
  upper halfword 0xFFFF, 6,144 valid-identity/unused/callback cases and four
  publication-alias cases. An effective status-two-to-four mutation fails.
  No exhaustive 32-bit payload, portable64 or hardware claim.
- The actual seventeen-body parent chain passes 1,920 cases / 3,840
  executions with the third-loader hook removed: 1,440 real success requests
  and 576 real NULL failures returning status two. It reaches 34 loader words;
  focused coverage establishes all 36. Deeper SDK request/lookup/allocator,
  free, heap, hardware and gameplay remain bounded or unqualified.
- Fifteen existing SDK variadic-loader tests pass freshly in 12.513 seconds,
  including actual two-component lazy loader, three-component table loader,
  constructor/helper/relocator C connections and freshly compiled IDO slots.
  These do not turn the bounded seventeen-body MIPS request into full runtime.

Initial failures were harness-only: unfiltered owner guards, then a parent
fixture whose third slot stayed occupied. Map the actual destination empty
and assert both request outcomes fire; do not infer behavior from absent calls.
The 97-test Note 1272 installed/regression receipt remains prior evidence,
not 97 fresh tests here. Existing tools dependencies and all nine production
assignment inputs remain unchanged. No production installation or rebuild.

## Literal Audit And Progress

Freeze and compare source, ELF, guards, progress, rodata, symbol addresses,
undefined functions, layout and Makefile literally. No projection or refreshed
baseline. Every one of these nine inputs stays byte-identical, including:

| Input | SHA-256 |
| --- | --- |
| Source | f580435626504c2fda5ecf8b7fa7a87feaf4d1f2a1332be1118923a6492e5dcb |
| ELF | 9f2c45ce2994dafadbaa9bce9c640e61852b6f2ebf4d2a34a41d1d1438bbcb25 |
| Guards | 92679ed3e2a6439969298cd769daf69d41e9619c81360046094cf34f1ec3faf4 |
| Makefile | 8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc |

All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Fresh match-progress: Game 2,796/4,822 (57.98%), total 3,469/5,495 (63.13%),
Init 492/492 and Debugger 181/181. Zero address drift, 2,026 still different.
Zero conversion/matching credit. Root README stays unchanged. The known
duplicate generated_12D630 Makefile warnings remain, not compiler diagnostics.

## Checkpoint And Next Work

Consumer/mounted/older tools checks and native py_compile pass. Commit tools
b6877d5b9cb1b5c9b6266eeb99fcefa544100d3e before this consumer documentation/
gitlink checkpoint. Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
and all 37 protected fingerprints stay unchanged. Copy only two absent final
files with identical hashes: its dirty count changes 314 -> 316, without a
reset, overwrite, older-history commit or push. Active checkouts are clean
after committing; no push authorized/performed. Detailed updates stay here,
with concise indexes rather than new root README narratives.

Native graphify update . exits one on its protective shrink refusal:
18,096 candidate nodes versus 39,877 in the saved graph. It keeps 19,398
nodes from 2,972 excluded-but-existing files; saved graph is not overwritten.
Existing version/empty-source warnings are separate from compiler checks.
No force, purge or install. After consumer commit, verify fresh hook completion from its
recorded log offset/bytes/UTC and zero workers, not the launch message alone.

Next: retain these exact guards while probing the 0x24 cached-slot spill and
V0/result-branch lifetime in complete semantic source. Guard elimination is
still unchecked; do not claim a direct match or double-count this already
exact function. Parent/pair guard elimination and deeper full caller/SDK/
heap/hardware/renderer/gameplay qualification remain separate. OGL Release,
real saves, private inputs and active editor/debugger state are untouched.
