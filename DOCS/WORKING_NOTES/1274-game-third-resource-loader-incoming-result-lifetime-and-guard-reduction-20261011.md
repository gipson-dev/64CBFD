# Game Third Resource Loader Incoming Result Lifetime And Guard Reduction

Date: 2026-10-11. Complete func_1503D774, owner
conker/src/game/generated_6A3D0.c. VA 0x1503D774..0x1503D804,
ROM 0x6AC24..0x6ACB4: 36 words / 144-byte function and slot.
Install qualified semantic C that reuses the ignored second argument as the
request result and shared status. Six normalizations become three; one
instruction drop remains. Raw C improves from 37 words / 15 differences to
37 / 7. All 36 linked words remain exact, and the entire ELF is unchanged.
This is guard reduction, NOT a direct C match or new matching credit.
The wider Game goal stays active.

## Baseline And Contract

Consumer 2ea4d65e647a965ee8318326555b59672aaf52ba and mounted tools
b6877d5b9cb1b5c9b6266eeb99fcefa544100d3e were clean at entry.
[Note 1273](1273-game-third-resource-loader-guard-audit-and-actual-chain-20261011.md)
banked the complete guarded loader and actual seventeen-body parent chain.
Use its retail assembly, caller interface and existing compiler/padder/oracle
helpers. No new dependency, compiler profile, recipe or global type changes.
Codex is the single writer; zero Claude calls.

Cache &D_800D1C90[identity]. An occupied slot returns zero without a request
or header read. Otherwise call func_1502B6BC(&output, 2, NULL, 2, 0x11,
identity), preserving the full identity and ignoring the incoming second
word and written output size. NULL clears the cached destination and returns
two. Success publishes the returned block pointer before reading its first
word, then publishes that word to the same cached slot and returns zero.
Callbacks may change globals/header contents; the cached destination and live
header read are preserved. First publication matters when the returned block
aliases the destination or its neighbor. No new bounds, NULL-header or
size-output gates. Pointer/result casts retain the existing 32-bit guest ABI;
no portable64 claim.

Retail frame 0x30, RA +0x1C, incoming identity +0x30, unused argument +0x34,
output +0x2C and cached slot +0x24 now emit natively. The request branch/reload
and V0 pointer-publication lifetime also emit natively. Reusing the parameter
and the common status exit leaves A0 status initialization and a redundant
A0-to-V0 copy. Raw public semantics are qualified; full raw private register
equivalence is not claimed.

## Installed Guard Reduction

Thirty-three of 36 retail words now emit directly, versus thirty previously.
The old spill/branch/pointer-normalization sites become native; the new shared
status shape needs two status normalizations and the cached-exit adjustment.
The net reduction is three rows, not simply deletion of three unchanged sites.
Only this function's seven-row block changes to these four rows:

| Raw Offset | Expected | Replacement | Purpose |
| --- | --- | --- | --- |
| 0x038 | 0x10000012 | 0x10000011 | Cached exit across omitted status copy |
| 0x06C | 0x24040002 | 0x24020002 | Failure status in V0 rather than A0 |
| 0x078 | 0x00002025 | 0x00001025 | Success status in V0 rather than A0 |
| 0x080 | 0x00801025 | instruction drop | Redundant shared-status copy |

The other guard bytes are unchanged, including 298 pre-existing CRLF lines.
Git's CRLF-to-LF warning is existing normalization policy, not a full-file
rewrite. Source is LF-only. Original assembly remains preserved.

Fresh canonical five-source/two-profile measurements from test_11:

| Complete Source Shape | Raw Words | Differences, Owner / Retail |
| --- | ---: | ---: |
| Banked | 37 | 15 / 15 |
| Incoming result | 37 | 14 / 14 |
| Incoming result and shared status, selected | 37 | 7 / 7 |
| Local shared status | 37 | 9 / 9 |
| Inline result expression | 37 | 14 / 14 |

All ten measurements have frame 0x30, no diagnostics or pool bytes. Earlier
filtered probes are partial diagnostic evidence, not another complete sweep.
No shape is direct. The selected source is accepted only with the four exact
guards and the complete qualification below.

## Fresh Qualification

New tools: experiments/game_third_resource_loader_lifetime_candidates.py and
tests/test_game_third_resource_loader_lifetime_match.py. Ignored immutable
before-inputs and JSON receipts live under
conker/build/game-third-resource-loader-lifetime-match-test/.

- Thirteen pre-install tests pass in 56.438 seconds. Final installed and
  affected regression selection: 137 tests in 503.641 seconds, all passing,
  no skips. It includes new/previous third-loader, cleanup, propagation,
  descriptor, pair, counter, relocator, guarded-main and SDK variadic suites,
  plus ten historical shape/audit checks and two flow-cost checks.
- Original/fitted forms retain all 36 words and extent 144. The 768-case
  identity/presence/result/header/unused/phase matrix reaches every retail
  word. Invalid identities are mapped guest fixtures, not real bounds proof.
- Twenty-eight callback/alias cases, four independent links / 64 rebased
  cases, and all 80 fired original/fitted private/public/request fault-prefix
  pairs pass. Guest fault order is not portable C fault behavior.
- Five freshly compiled semantic mutations fail effectively. Each of four
  remaining guards rejects expected-word and relocation corruption: eight
  effective failures. Four source, three guard, two word/extent and two stale
  installation corruptions reject the exact historical projection.
- Both full owner profiles compile with zero diagnostics. All 14 neighbors,
  relocations, pools and extents remain exact. Both actual padders resolve
  all four before/after routes to the same complete 3,760-byte current owner;
  the existing D804 object selector is unchanged.
- Native32 O2/O0 each pass 65,536 low-halfword payloads with fixed upper
  halfword 0xFFFF, 6,144 valid-identity/unused/callback cases and four aliases.
  A status-two-to-four mutation fails. Not exhaustive 32-bit payloads,
  native invalid identities, portable64 or hardware qualification.
- Actual seventeen-body parent chain: 1,920 cases / 3,840 executions,
  1,440 real success requests and 576 NULL/status-two failures. Third-loader
  hook removed; 34 loader words reached here, all 36 in focused coverage.
  Deeper request/lookup/allocator/free/heap/hardware/gameplay remain bounded.
- Fifteen SDK variadic tests are fresh within the 137-test run, including
  actual two-component lazy-loader C, real SDK helper/relocator connections
  and freshly compiled IDO slots. This is not live hardware/gameplay proof.

Initial harness-only failure used nonmatching inherited test override names;
correct exact overrides before the green thirteen-test receipt. The first
installed regression run stopped after 45 tests on an old literal guard audit.
Update only the affected historical source/guard views; three focused audits
pass in 8.987 seconds, followed by the complete green 137-test rerun.
Historical baselines are not refreshed. Projections reverse only the complete
qualified source and exact four-row guard block, with full predecessor hashes,
round-trip installation and actual retail slot/extent checks. Historical
receipts explicitly label projected views. The new installed audit reads all
actual inputs literally and uses no projection to prove the current delta.

Reproduction from the prepared consumer checkout:

```sh
python3 -m tools.experiments.game_third_resource_loader_lifetime_candidates --filter= --profiles
python3 -m unittest tools.tests.test_game_third_resource_loader_lifetime_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The guard-triggered rebuild exits zero. Existing warnings from unchanged
modules and the duplicate generated_12D630 recipe remain; this is not a
warning-free full build. Target/complete-owner compiler diagnostics are zero.

## Literal Audit And Progress

Source and guards are exactly the qualified successors. All seven other
assignment inputs (ELF, progress, rodata, symbol addresses, undefined
functions, layout and Makefile) remain byte-identical. Entire ELF, metadata,
all function addresses/extents/bodies and protected data have zero delta.

| Input | SHA-256 |
| --- | --- |
| Source after | 52e22c65fca3a59f418c6589b84d9653e432e7343e1351d47b3fbf3353c38ae2 |
| Guards after | 0aea2b7a3d2d610fcb8c6f4fa02cac6922af82868a9b447c70ccdd16b6db35b4 |
| ELF unchanged | 9f2c45ce2994dafadbaa9bce9c640e61852b6f2ebf4d2a34a41d1d1438bbcb25 |
| Makefile unchanged | 8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc |
| Conversion CSV unchanged | 32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c |

All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Fresh match-progress: Game 2,796/4,822 (57.98%), total 3,469/5,495 (63.13%),
Init 492/492 and Debugger 181/181. Zero drift, 2,026 still different.
Zero matching/conversion credit. Root README remains unchanged.

## Checkpoint And Next Work

Consumer, mounted and older tools shared checks pass; all nine mounted task
paths and both new older copies pass native py_compile. Commit tools
5eb0c4a12506e2db2d6e8d684fcbddd33789dab6 first, then source/guards, this note,
five concise indexes and consumer gitlink. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 39 protected fingerprints
stay unchanged. Copy only two absent new files with identical hashes; dirty
count 316 -> 318. Do not overwrite its seven existing helper/test paths,
reset, commit older history or push. Active checkouts are clean after banking.
No push requested/performed; no Claude invocation or billing/settings change.

Native graphify update . exits one on protective shrink refusal: 18,105
candidate nodes versus 39,886 saved. It keeps 19,398 nodes from 2,972
excluded-but-existing files; no saved-graph overwrite, force, purge or install.
Existing version/empty-source warnings remain separate. After consumer commit,
verify fresh hook completion from recorded log offset/bytes/UTC and zero
workers, not its launch message alone.

Next: probe the remaining A0/shared-status exit and extra move using complete
semantic C. Eliminate three normalizations and one drop before claiming a
direct match; do not double-count this already-exact loader. Parent/pair guard
elimination and deeper SDK/allocator/heap/hardware/renderer/gameplay remain
separate. OGL Release, real saves, private inputs and active editor/debugger
state are untouched. Keep the wider Game matching goal active.
