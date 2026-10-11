# Game Vertex Coordinate Copy Guarded Match

Date: 2026-10-11. Complete func_1503D804, VA 0x1503D804..0x1503D984,
ROM 0x6ACB4..0x6AE34, 96 words / 384 bytes. Owner:
conker/src/game/generated_6A3D0.c. Semantic C emits 92 words directly;
four closed frame/count-spill guards make all 96 linked words byte-exact.
This is a guarded match, not a direct C match. The wider Game goal is active.

## Baseline And Contract

Consumer e44d6a3fa0b52e52f9e0d9c33bc1c7c2c5fd2e89, mounted tools
23570e99b9cc1fd3e0dc16f4ce909b02c48fca8e. Both active checkouts were clean.
[Note 1268](1268-game-command-weight-counter-direct-match-20261011.md)
banked the complete direct 46-word counter. The secondary allocation/copy
helper was still a zero-return placeholder and modeled in the loader chain.
Local native Graphify query and complete assembly identify the direct caller
func_1503CF20, which joins this routine's status into its failure accumulator.

Recover the s32 (s32 identity) interface and the existing allocator's signed
32-bit address return contract. Only identity 0x24 sets count 94 and kind 0.
All other identities return zero before public-table reads; an already
published D_800C6360[identity] pointer also returns zero without allocating.
Retain the original generic kind != -1 branch, not a new identity/bounds gate.

Cache the slot, D_800D19A0[identity] base and unsigned first record offset
from ((u32 *)D_800C4020[identity])[kind] before calling
allocate_memory(94 * 4, 1, 0, 2). Publish the allocator result before testing
NULL, including publication on failure. Failure returns one; success reloads
the published pointer and copies 94 signed halfword pairs in sequence.

Source offsets +8/+10 and 16-byte stride agree with the local SDK
[Vtx layout](../../conker/include/2.0L/PR/gbi.h): Vtx.v.tc[0/1], size 16 and
eight-byte alignment. The four-byte destination is a local
TextureCoordinatePair with signed s/t fields. This name is a layout-grounded
interpretation, not a demonstrated gameplay identity or renderer contract.
Do not replace live ordered reads/stores with a bulk snapshot. Cached source
inputs survive caller-saved clobber and callback mutation; payloads stay live.
There is no new NULL-base check, identity bound or destination alias gate.

## Profile And Four Guards

The original routine has a 0x38 frame, RA at +0x14 and no saved S registers.
The selected complete SDK/index-first body under -O2 -g3 emits 96 words with
a 0x40 frame and four differences. Remainder-two/four-record unroll, branches,
delay slots, load/store widths, operands and call arguments already match.

The full diagnostic sweep measures 132 forms: 66 source forms under two
profiles, with zero diagnostics or data pools. Some bodies repeat; this is
not 132 unique bodies or a full semantic qualification of every form.
No direct zero-difference form was found. Declaration order reduces six
differences to four. The qualified, record-index-first and Vtx-index-first
retail forms reach four; only the canonical SDK body is installed.

The owner normally uses -O2 -g3 -Wo,-loopunroll,0. That profile gives this
body only 66 words and does not qualify. Preserve the owner's no-unroll
object, compile a second -O2 -g3 object, and use the existing padder's
--function-object selector for only func_1503D804. Add this owner to the
existing mixed-profile exclusion list, with one explicit recipe. No core
padder changes, owner-wide profile switch or new duplicate recipe warning.

Exactly four expected-word guards, all with empty expected/replacement
relocations, are appended to retail_word_patches.us.csv:

| Offset | Expected Raw Word | Retail Word | Closed Change |
| --- | --- | --- | --- |
| 0x000 | 0x27BDFFC0 | 0x27BDFFC8 | Frame allocation 0x40 -> 0x38 |
| 0x094 | 0xAFA80038 | 0xAFA80034 | Count spill +0x38 -> +0x34 |
| 0x0A8 | 0x8FA80038 | 0x8FA80034 | Paired count reload |
| 0x174 | 0x27BD0040 | 0x27BD0038 | Paired frame release |

The other 92 words are directly exact. Guards do not change control flow,
public load/store widths or the unrolled copy. Raw-C private-stack fault
parity is not claimed; original and actual guarded instruction streams are
qualified separately, including every private/public access fault.

## Qualification

New authored tools: experiments/game_record_pair_copy_candidates.py and
tests/test_game_record_pair_copy_match.py. Reuse existing IDO, MIPS oracle,
native32, owner, pool, relocation and actual padding helpers. Receipts live
under ignored conker/build/game-record-pair-copy-match-test/.

- Twelve final pre-install tests pass in 45.055 seconds. Complete 96-word
  original/actual-padded streams agree, with 92 direct and four guarded words.
- The identity/present/failure/payload matrix passes 352 cases / three forms
  and reaches all 96 words. Invalid no-op identities include negative,
  256, INT_MIN and INT_MAX. This does not make the dead kind-minus-one or
  variable-count branch outcomes reachable.
- Eighty-two alias/callback cases cover source, source+8/+10/+16, publication,
  base-table and offset-table destinations, cached inputs and live payloads.
  Wrapped unsigned offsets use mapped guest fixtures, not portable C bounds.
- Nine independent links pass 144 cases with three independent global
  HI16/LO16 carries, allocator JAL rebases, unused A1/A2/A3 and stack phases.
- All 798 original/guarded memory-access fault pairs fire and preserve full
  partial memory, access events, calls and registers, including private
  stack accesses. This is a guest-model result, not hardware acceptance.
- Eight freshly compiled semantic mutations fail effectively; three stale
  source install attempts and duplicate mixed-profile installation reject.
- Complete no-unroll before/after owners and the unrolled alternate compile
  without diagnostics. Both real padders preserve all 14 neighbors, extents,
  bytes, relocations and pools; the typed parent's instructions stay exact.
  Omitting the target selector fails both routes. Actual GNU make dry-run
  verifies the two intended compile profiles and one selected function.
- Native32 O2/O0 each pass 66,896 cases: all 65,536 halfword values, 1,024
  valid-identity/present/failure cases, 320 valid offset/callback/overlap
  cases and 16 invalid no-op cases. Full arrays and 256 pointer slots agree
  with an independent reference; a changed second coordinate fails.
  SDK size/offset assertions pass. Existing no-strict-aliasing policy applies;
  no 64-bit portable-host or mapped-guest-wrap acceptance is inferred.
- Sixteen fired stale-word/relocation rejections cover every guard and both
  actual padders. Four source/prototype/declaration/newline corruptions,
  two linked word/extent changes and three guard suffix/header corruptions
  reject before historical projection. Unrelated ELF bytes remain visible.
- The actual 104/274/52/46/96/56/9/194-word parent/main/command/counter/pair/
  extras/relocator/buffer chain passes 1,536 cases for identities 7 and 36.
  Its secondary hook is replaced by the actual guarded body; allocator NULL
  produces the real return-one path. The chain reaches 94 pair words; the
  focused matrix separately reaches all 96. Deeper helpers remain bounded.

During pre-install qualification, two chain-fixture interface mistakes were
resolved: the reused counter test was initially handed the new 96-word body
instead of the actual 46-word counter, and the outer fixture still forced
identity 7. Explicitly supply the counter words and scope the outer identity
to the tested case, restoring fields in finally. No production defect.

The first post-install run passed 59 tests but failed the older status-join
suite's setup: it compared literal appended guards with an already-projected
expected hash. Its guard input now uses the existing strict successor-aware
validator. Two focused historical checks pass in 31.700 seconds. The final
full rerun passes all 61 tests in 203.510 seconds: twelve pair, eleven counter,
eleven command, fifteen guarded parent, ten earlier loader shape/audit checks
and two historical status-join checks. No skips, errors or failures.
The 31 historical candidates are recompiled; their full behavioral matrix
is not rerun. Prior unchanged semantic receipts remain prior evidence.

## Immutable Historical Audits

Only the exact qualified pair body, typed prototype and allocator declaration
may reverse to the frozen counter-stage source SHA-256
6456ebae21a9227a74bbd15b19dba47cba8319f01c1e02d2d517da09a8df6fa2.
Before ELF projection, require all 96 current linked words to equal retail
and the symbol extent to be 384 bytes. Reverse only that complete slot and
extent onto the trusted historical ELF. All other current bytes survive.

Guard projection accepts only the known prefix plus these exact four rows,
after independently validating the current source, full linked slot and
extent. The recovered prefix must retain SHA-256
aa80c31e9eef9326b6a64100be34df67037a4d3dff3dfb76f89a15d054e0f6eb.
The existing exact counter/command projections then serve older parent
audits. Frozen source/ELF/guard inputs, historical candidates and negative
controls are not refreshed. Historical receipts describe projected views,
not an unchanged literal current source/ELF/guard file. The new suite audits
the actual installation. Parent func_1503CF20 still needs its existing
22 guards; the new child does not eliminate them.

## Actual Delta And Progress

Installed source SHA-256:
c5e63d79936dc66521f8cd1bc284c0f09c854e8a33889994d1876c076fb0450b.
Installed ELF SHA-256:
68ba892ee6637eaf7c043fbebf0466037570fdd86b58d587d0265f3060acfe55.

Exactly 298 ELF bytes change: 296 target-slot bytes and two extent bytes,
12 -> 384. Every other ELF byte, metadata byte, symbol name/value/extent,
protected data byte and conversion/assignment input remains identical.
All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guard SHA-256 after the four exact appended rows:
92679ed3e2a6439969298cd769daf69d41e9619c81360046094cf34f1ec3faf4.
Only the qualified mixed-profile rule/exclusion changes the Makefile, SHA-256
8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc.
Conversion CSV remains byte-identical, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.

Required ELF/progress rebuild exits zero; existing duplicate generated_12D630
recipe and unrelated legacy compiler warnings remain. No new owner diagnostics.
Fresh make -C conker match-progress NON_MATCHING=1 exits zero:

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,466 / 5,495 (63.08%) | 0 | 2,029 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,793 / 4,822 (57.92%) | 0 | 2,029 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Conversion/converted-byte metrics stay fixed.
Root README changes only the two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools
1310ff74cb9bfdda580c23e04cc0a29d4ebdf235 is committed first; the consumer pins
that checkpoint with source, guards, recipe, notes and aggregate rows. No push.
Consumer/mounted/older WSL tools checks pass, as do native py_compile for all
eight changed tools and the two identical absent-path copies. Older sibling
HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 29 protected existing
fingerprints remain unchanged. Dirty entries 306 -> 308 are only the two new
copies. Existing older audit paths are not overwritten or committed/reset.

Native Graphify refresh exits one after refusing shrink 39,839 -> 18,058
nodes, retaining 19,398 nodes from 2,972 still-existing excluded files.
Known skill/package-version and devcontainer zero-node warnings remain;
no force, purge or install. Refresh terminates with zero actual native
Python/Graphify workers. Require a fresh consumer post-commit hook log
length/UTC, fresh Rebuilt record and zero actual workers before calling
the commit settled. No OGL/Release/save/editor/private-input changes.
Real allocator/heap/hardware/renderer/gameplay and portable 64-bit host
acceptance remain open; Release stays frozen.

Next complete connected recovery: func_1503D660, VA
0x1503D660..0x1503D774, ROM 0x6AB10..0x6AC24, 69 words / 276 bytes,
same owner, still a zero-return placeholder. Recover its existing-publication
gate, identity remapper/request(2, 15, remapped identity), private result
lifetime, failure publication/count clear/status four, descriptor's live
pointer relocations and +0x10 publication, downstream count/helper calls,
original 0x38 frame/S0/RA and unused incoming A1 lifetime. Qualify the full
routine and actual helper interfaces before replacing another chain model.
Its func_1503D510 helper remains a separate recovery gate. Parent guard
elimination and wider runtime acceptance remain separate work.
